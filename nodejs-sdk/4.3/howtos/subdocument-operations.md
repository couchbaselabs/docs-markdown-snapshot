---
title: Sub-Document Operations
description: <em>Sub-document</em> operations can be used to efficiently access
  <em>parts</em> of documents.
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.3/modules/howtos/pages/subdocument-operations.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:4.3@nodejs-sdk:howtos:subdocument-operations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/4.3/howtos/subdocument-operations.html)

# Sub-Document Operations

> _Sub-document_ operations can be used to efficiently access _parts_ of documents. 

Sub-document operations may be quicker and more network-efficient than _full-document_ operations such as _upsert_, _replace_ and _get_ because they only transmit the accessed sections of the document over the network.

Sub-document operations are also atomic, allowing safe modifications to documents with built-in concurrency control.

## [](#sub-documents)Sub-documents

Starting with Couchbase Server 4.5 you can atomically and efficiently update and retrieve _parts_ of a document. These parts are called _sub-documents_. While full-document retrievals retrieve the entire document and full document updates require sending the entire document, sub-document retrievals only retrieve relevant parts of a document and sub-document updates only require sending the updated portions of a document. You should use sub-document operations when you are modifying only portions of a document, and full-document operations when the contents of a document is to change significantly.

> [!IMPORTANT]
> The sub-document operations described on this page are for _Key-Value_ requests only: they are not related to sub-document SQL++ (formerly N1QL) queries. (Sub-document SQL++ queries are explained in the section [Querying with SQL++](n1ql-queries-with-sdk.md).)

In order to use sub-document operations you need to specify a _path_ indicating the location of the sub-document. The _path_ follows SQL++ syntax (see [below](https://developer.couchbase.com/documentation/server/current/sdk/subdocument-operations.html#story-h2-12), and [SQL++ Queries and Results](../../../server/7.6/n1ql/n1ql-intro/queriesandresults.md)). Considering the document:

customer123.json

```json
{
  "name": "Douglas Reynholm",
  "email": "douglas@reynholmindustries.com",
  "addresses": {
    "billing": {
      "line1": "123 Any Street",
      "line2": "Anytown",
      "country": "United Kingdom"
    },
    "delivery": {
      "line1": "123 Any Street",
      "line2": "Anytown",
      "country": "United Kingdom"
    }
  },
  "purchases": {
    "complete": [
      339, 976, 442, 666
    ],
    "abandoned": [
      157, 42, 999
    ]
  }
}
```

The paths `name`, `addresses.billing.country` and `purchases.complete[0]` are all valid paths.

## [](#retrieving)Retrieving

The _lookup-in_ operations query the document for certain path(s); these path(s) are then returned. You have a choice of actually retrieving the document path using the _subdoc-get_ sub-document operation, or simply querying the existence of the path using the _subdoc-exists_ sub-document operation. The latter saves even more bandwidth by not retrieving the contents of the path if it is not needed.

Retrieve sub-document value

```javascript
var result = await collection.lookupIn('customer123', [
  couchbase.LookupInSpec.get('addresses.delivery.country'),
])
var country = result.content[0].value //'United Kingdom'
```

Check existence of sub-document path

```javascript
  var result = await collection.lookupIn('customer123', [
    couchbase.LookupInSpec.exists('purchases.pending[-1]'),
  ])
  console.log('Path exists? ', result.content[0].value)

  // Path exists? false
```

Multiple operations can be combined as well:

Combine multiple lookup operations

```javascript
  var result = await collection.lookupIn('customer123', [
    couchbase.LookupInSpec.get('addresses.delivery.country'),
    couchbase.LookupInSpec.exists('purchases.pending[-1]'),
  ])

  console.log(result.content[0].value) // United Kingdom
  console.log('Path exists?', result.content[1].value) // false
```

## [](#mutating)Mutating

Mutation operations modify one or more paths in the document. The simplest of these operations is _subdoc-upsert_, which, similar to the fulldoc-level _upsert_, will either modify the value of an existing path or create it if it does not exist:

Upserting a new sub-document

```javascript
await collection.mutateIn('customer123', [
  couchbase.MutateInSpec.upsert('fax', '311-555-0151'),
])
```

Likewise, the _subdoc-insert_ operation will only add the new value to the path if it does not exist:

Inserting a sub-document

```javascript
  await collection.mutateIn('customer123', [
    couchbase.MutateInSpec.insert('purchases.complete', [42, true, 'None']),
  ])
  // Success

  try {
    await collection.mutateIn('customer123', [
      couchbase.MutateInSpec.insert('purchases.complete', [42, true, 'None']),
    ])
  } catch (e) {
    if (e instanceof couchbase.PathExistsError) {
      console.log('Path already exists...')
    } else {
      throw e
    }
  }
```

Dictionary values can also be replaced or removed, and you may combine any number of mutation operations within the same general _mutate-in_ API. Here's an example of one which replaces one path and removes another.

```javascript
await collection.mutateIn('customer123', [
  couchbase.MutateInSpec.remove('addresses.billing'),
  couchbase.MutateInSpec.replace('email', 'dougr96@hotmail.com'),
])
```

Mutate with store semantics

The `storeSemantics` option can be used to define the document storage semantics for a _mutate-in_ operation. In this particular example we use the `Upsert` semantics, which means the document will be updated if it exists, and created if it doesn't. Note that when a document is updated, only the specified paths will be modified.

```javascript
try {
  // Mutate fields in a document that may or may not exist.
  await collection.mutateIn(
    'alice-123',
    [
      couchbase.MutateInSpec.insert('name', 'Alice'),
      couchbase.MutateInSpec.upsert('email', 'alice@test.com'),
    ],
    {
      storeSemantics: couchbase.StoreSemantics.Upsert,
    }
  )
} catch (e) {
  if (e instanceof couchbase.PathExistsError) {
    console.log('Path already exists, not adding unique value')
  } else {
    throw e
  }
}
```

> [!NOTE]
> `mutateIn` is an _atomic_ operation. If any single `ops` fails, then the entire document is left unchanged.

## [](#array-append-and-prepend)Array append and prepend

The _subdoc-array-prepend_ and _subdoc-array-append_ operations are true array prepend and append operations. Unlike fulldoc _append_/_prepend_ operations (which simply concatenate bytes to the existing value), _subdoc-array-append_ and _subdoc-array-prepend_ are JSON-aware:

```javascript
  await collection.mutateIn('customer123', [
    couchbase.MutateInSpec.arrayAppend('purchases.complete', 777),
  ])

  // purchases.complete is now [339, 976, 442, 666, 777]
```

```javascript
  await collection.mutateIn('customer123', [
    couchbase.MutateInSpec.arrayPrepend('purchases.abandoned', 18),
  ])

  // purchases.abandoned is now [18, 157, 49, 999]
```

If your document only needs to contain an array, you do not have to create a top-level object wrapper to contain it. Simply initialize the document with an empty array and then use the empty path for subsequent sub-document array operations:

Creating and populating an array document

```javascript
  await collection.upsert('my_array', [])
  await collection.mutateIn('my_array', [
    couchbase.MutateInSpec.arrayAppend('', 'some element'),
  ])

  // the document my_array is now ['some element']
```

If you wish to add multiple values to an array, you may do so by passing multiple values to the _array-append_, _array-prepend_, or _array-insert_ operations. Be sure to know the difference between passing a collection of multiple elements (in which case the collection is inserted as a single element in the array, as a sub-array) and passing multiple elements (in which case the elements are appended individually to the array):

Add multiple elements to an array

```javascript
  await collection.mutateIn('my_array', [
    couchbase.MutateInSpec.arrayAppend('', ['elem1', 'elem2', 'elem3'], {
      multi: true,
    }),
  ])

  // the document my_array is now ['some_element', 'elem1', 'elem2', 'elem3']
```

Add single array as element to existing array

```javascript
  await collection.mutateIn('my_array', [
    couchbase.MutateInSpec.arrayAppend('', ['elem1', 'elem2', 'elem3']),
  ])

  // the document my_array is now ['some_element', ['elem1', 'elem2', 'elem3']]
```

Note that passing multiple values to a single _array-append_ operation results in greater performance increase and bandwidth savings than simply specifying a single _array-append_ for each element.

Adding multiple elements to array (slow)

```javascript
await collection.mutateIn('my_array', [
  couchbase.MutateInSpec.arrayAppend('', 'elem1'),
  couchbase.MutateInSpec.arrayAppend('', 'elem2'),
  couchbase.MutateInSpec.arrayAppend('', 'elem3'),
])
```

If you wish to create an array if it does not exist and also push elements to it within the same operation you may use the [_create-path_](#subdoc-create-parents) option:

```javascript
await collection.mutateIn('customer123', [
  couchbase.MutateInSpec.arrayAppend('some.path', 'Hello World', {
    createPath: true,
  }),
])
```

## [](#arrays-as-unique-sets)Arrays as Unique Sets

Limited support also exists for treating arrays like unique sets, using the _subdoc-array-addunique_ command. This will do a check to determine if the given value exists or not before actually adding the item to the array:

```javascript
  await collection.mutateIn('customer123', [
    couchbase.MutateInSpec.arrayAddUnique('purchases.complete', 95),
  ])

  // => Success

  try {
    await collection.mutateIn('customer123', [
      couchbase.MutateInSpec.arrayAddUnique('purchases.complete', 95),
    ])
  } catch (e) {
    if (e instanceof couchbase.PathExistsError) {
      console.log('Path already exists, not adding unique value')
    } else {
      throw e
    }
  }
```

Note that currently the _addunique_ will fail with a _Path Mismatch_ error if the array contains JSON _floats_, _objects_, or _arrays_. The _addunique_ operation will also fail with _Cannot Insert_ if the value to be added is one of those types as well.

Note that the actual position of the new element is undefined, and that the array is not ordered.

## [](#array-insertion)Array insertion

New elements can also be _inserted_ into an array. While _append_ will place a new item at the _end_ of an array and _prepend_ will place it at the beginning, _insert_ allows an element to be inserted at a specific _position_. The position is indicated by the last path component, which should be an array index. For example, to insert `'cruel'` as the second element in the array `['Hello', 'world']`, the code would look like:

```javascript
await collection.mutateIn('customer123', [
  couchbase.MutateInSpec.arrayInsert('tags[0]', 'cruel'),
])
```

Note that the array must already exist and that the index must be valid (i.e. it must not point to an element which is out of bounds).

## [](#counters-and-numeric-fields)Counters and numeric fields

Counter operations allow the manipulation of a _numeric_ value inside a document. These operations are logically similar to the _counter_ operation on an entire document:

```javascript
  var result = await collection.mutateIn('customer123', [
    couchbase.MutateInSpec.increment('logins', 1),
  ])

  console.log(result.content[0]) // 1
```

The _subdoc-counter_ operation performs simple arithmetic against a numeric value, either incrementing or decrementing the existing value. The new value is returned.

```javascript
  await collection.upsert('player432', {
    gold: 1000,
  })

  var result = await collection.mutateIn('player432', [
    couchbase.MutateInSpec.decrement('gold', 150),
  ])
  // => player 432 now has 850 gold remaining
```

The existing value for _subdoc-counter_ operations must be within range of a 64 bit signed integer. If the value does not exist, the _subdoc-counter_ operation will create it (and its parents, if _create-path_ is enabled).

Note that there are several differences between _subdoc-counter_ and the full-document _counter_ operations:

* Sub-document counters have a range of -9223372036854775807 to 9223372036854775807 (i.e. `Iint64.MinValue` and `` Int64.MaxValue), whereas full-document counters have a range of 0 to 18446744073709551615 (`UInt64.MaxValue ``)
* Sub-document counter operations protect against overflow and underflow, returning an error if the operation would exceed the range. Full-document counters will use normal C semantics for overflow (in which the overflow value is carried over above 0), and will silently fail on underflow, setting the value to 0 instead.
* Sub-Document counter operations can operate on any numeric value within a document, while [full-document counter operations](kv-operations.md#atomic-counters) require a specially formatted counter document with only the counter value.

## [](#executing-multiple-operations)Executing multiple operations

Multiple sub-document operations can be executed at once on the same document, allowing you to retrieve or modify several sub-documents at once. When multiple operations are submitted within the context of a single _lookup-in_ or _mutate-in_ command, the server will execute all the operations with the same version of the document.

> [!NOTE]
> Unlike _batched operations_ which is simply a way of sending multiple individual operations efficiently on the network, multiple subdoc operations are formed into a single command packet, which is then executed atomically on the server. You can submit up to 16 operations at a time.

When submitting multiple _mutation_ operations within a single _mutate-in_ command, those operations are considered to be part of a single transaction: if any of the mutation operations fail, the server will logically roll-back any other mutation operations performed within the _mutate-in_, even if those commands would have been successful had another command not failed.

When submitting multiple _retrieval_ operations within a single _lookup-in_ command, the status of each command does not affect any other command. This means that it is possible for some retrieval operations to succeed and others to fail. While their statuses are independent of each other, you should note that operations submitted within a single _lookup-in_ are all executed against the same _version_ of the document.

## [](#subdoc-create-parents)Creating parents

Sub-document mutation operations such as _subdoc-upsert_ or _subdoc-insert_ will fail if the _immediate parent_ is not present in the document. Consider:

```json
{
    'level_0': {
        'level_1': {
            'level_2': {
                'level_3': {
                    'some_field': 'some_value'
                }
            }
        }
    }
}
```

Looking at the `some_field` field (which is really `level_0.level_1.level_2.level_3.some_field`), its _immediate_ parent is `level_3`. If we were to attempt to insert another field, `level_0.level_1.level_2.level_3.another_field`, it would succeed because the immediate parent is present. However if we were to attempt to _subdoc-insert_ to `level_1.level_2.foo.bar` it would fail, because `level_1.level_2.foo` (which would be the immediate parent) does not exist. Attempting to perform such an operation would result in a Path Not Found error.

By default the automatic creation of parents is disabled, as a simple typo in application code can result in a rather confusing document structure. Sometimes it is necessary to have the server create the hierarchy however. In this case, the _create-path_ option may be used.

```javascript
await collection.mutateIn('customer123', [
  couchbase.MutateInSpec.upsert(
    'level_0.level_1.foo.bar.phone',
    {
      num: '311-555-0101',
      ext: 16,
    },
    {
      createPath: true,
    }
  ),
])
```

## [](#reading-sub-documents-from-replicas)Reading Sub-Documents From Replicas

Couchbase Server 7.6 and later support Sub-Doc lookup from replicas.

The `collection.lookupInAnyReplica()` method returns the first response — from active or replica:

```javascript
try {
  result = await collection.lookupInAnyReplica('customer123', [
    couchbase.LookupInSpec.get('addresses.delivery.country'),
  ])
  const country = result.content[0].value //'United Kingdom'
  console.log(`Country=${country}`)
  console.log(`Is result replica=${result.isReplica}`)
} catch (err) {
  if (err instanceof couchbase.PathNotFoundError) {
    console.log(`The version of the document on the server node 
    that responded quickest did not have the requested 
    field.`)
  } else if (err instanceof couchbase.DocumentUnretrievableError) {
    console.log('Document not present on any server node.')
  }
}
```

The `collection.lookupInAllReplicas()` fetches all available replicas (and the active copy), and returns all responses.

```javascript
result = await collection.lookupInAllReplicas('customer123', [
  couchbase.LookupInSpec.get('addresses.delivery.country'),
])
result.forEach((res) => {
  try {
    const country = res.content[0].value //'United Kingdom'
    console.log(`Country=${country}`)
    console.log(`Is result replica=${res.isReplica}`)
  } catch (err) {
    if (err instanceof couchbase.PathNotFoundError) {
      console.log(`The version of the document on one of the server nodes 
      did not have the requested field.`)
    }
  }
})
```

You may want to use `lookupInAllReplicas` to build a consensus, but it's more likely that you'll make use of `lookupInAnyReplica` as a fallback to a `lookupIn`, when the active node times out.

## [](#cas-semantics)CAS Semantics

Subdoc mostly eliminates the need for tracking the [CAS](concurrent-document-mutations.md) value. Subdoc operations are atomic and therefore if two different threads access two different sub-documents then no conflict will arise. For example the following two blocks can execute concurrently without any risk of conflict:

```javascript
await collection.mutateIn('customer123', [
  couchbase.MutateInSpec.arrayAppend('purchases.complete', {
    some_id: SOME_ID,
  }),
])
```

```javascript
await collection.mutateIn('customer123', [
  couchbase.MutateInSpec.arrayAppend('purchases.abandoned', {
    some_other_id: SOME_OTHER_ID,
  }),
])
```

Even when modifying the _same_ part of the document, operations will not necessarily conflict. For example, two concurrent _subdoc-array-append_ operations to the same array will both succeed, never overwriting the other.

While CAS is no longer so strongly required to ensure document updates are preserved, as Sub-Doc reduces the chance of losing a mutation, it may still be needed to ensure document state remains consistent over multiple invocations of _mutate-in_: Sometimes it's important to ensure the entire document didn't change state since the last operation, such as in the case _subdoc-remove_ operations to ensure that the element being removed was not already replaced by something else.

```javascript
await collection.mutateIn(
  'customer123',
  [couchbase.MutateInSpec.insert('addresses.delivery.line1', '17 Olcott St')],
  {
    cas: SOME_CAS,
  }
)
```

## [](#error-handling)Error handling

Subdoc operations have their own set of errors. When programming with subdoc, be prepared for any of the full-document errors (such as _Document Not Found_) as well as special sub-document errors which are received when certain constraints are not satisfied. Some of the errors include:

* **Path does not exist**: When retrieving a path, this means the path does not exist in the document. When inserting or upserting a path, this means the _immediate parent_ does not exist.
* **Path already exists**: In the context of an _insert_, it means the given path already exists. In the context of _array-add-unique_, it means the given value already exists.
* **Path mismatch**: This means the path may exist in the document, but that there is a type conflict between the path in the document and the path in the command. Consider the document:  
```json  
{ 'tags': ['reno', 'nevada', 'west', 'sierra'] }  
```  
The path `tags.sierra` is a mismatch, since `tags` is actually an array, while the path assumes it is a JSON object (dictionary).
* **Document not JSON**: This means you are attempting to modify a binary document using sub-document operations.
* **Invalid path**: This means the path is invalid for the command. Certain commands such as _subdoc-array-insert_ expect array elements as their final component, while others such as _subdoc-upsert_ and _subdoc-insert_ expect dictionary (object) keys.

If a Sub-Document command fails a top-level error is reported (_Multi Command Failure_), rather than an individual error code (e.g. _Path Not Found_). When receiving a top-level error code, you should traverse the results of the command to see which individual code failed.

## [](#path-syntax)Path syntax

Path syntax largely follows SQL++ conventions: A path is divided into components, with each component referencing a specific _level_ in a document hierarchy. Components are separated by dots (`.`) in the case where the element left of the dot is a dictionary, or by brackets (`[n]`) where the element left of the bracket is an array and `n` is the index within the array.

As a special extension, you can indicate the _last element_ of an array by using an index of `-1`, for example to get the last element of the array in the document

```json
{'some':{'array':[1,2,3,4,5,6,7,8,9,0]}}
```

Use `some.array[-1]` as the path, which will return the element `0`.

Each path component must conform as a JSON string, as if it were surrounded by quotes, and any character in the path which may invalidate it as a JSON string must be escaped by a backslash (`\`). In other words, the path component must match exactly the path inside the document itself. For example:

```json
{'literal\'quote': {'array': []}}
```

must be referenced as `literal'quote.array`.

If the path also has special path characters (i.e. a dot or brackets) it may be escaped using SQL++ escapes. Considering the document

```json
{'literal[]bracket': {'literal.dot': true}}
```

A path such as `` \`literal[]bracket ``.\`literal.dot\`\`. You can use double-backticks (\`\`) to reference a literal backtick.

If you need to combine both JSON _and_ path-syntax literals you can do so by escaping the component from any JSON string characters (e.g. a quote or backslash) and then encapsulating it in backticks (`` `path` ``).

> [!NOTE]
> Currently, paths cannot exceed 1024 characters, and cannot be more than 32 levels deep.

## [](#extended-attributes)Extended Attributes

Extended Attributes (also known as XATTRs), built upon the Sub-Document API, allow developers to define application-specific metadata that will only be visible to those applications that request it or attempt to modify it. This might be, for example, meta-data specific to a programming framework that should be hidden by default from other frameworks or libraries, or possibly from other versions of the same framework. They are not intended for use in general applications, and data stored there cannot be accessed easily by some Couchbase services, such as Search.

## [](#xdcr)XDCR

XDCR only replicates full documents. Sub-documents are only replicated as part of the full document.