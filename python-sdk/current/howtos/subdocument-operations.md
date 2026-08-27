---
title: Sub-Document Operations
description: Sub-Document operations can be used to efficiently access and
  change parts of documents.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-python/edit/release/4.6/modules/howtos/pages/subdocument-operations.adoc
  xref: xref:python-sdk:howtos:subdocument-operations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/current/howtos/subdocument-operations.html)

# Sub-Document Operations

> Sub-Document operations can be used to efficiently access and change parts of documents. 

Sub-Document operations may be quicker and more network-efficient than _full-document_ operations such as _Upsert_, _Replace_ and _Get_ because they only transmit the accessed sections of the document over the network.

Sub-Document operations are also atomic, in that if one Sub-Document mutation fails then all will, allowing safe modifications to documents with built-in concurrency control.

The complete code sample used on this page can be downloaded from [the GitHub repo for the Python docs](https://github.com/couchbase/docs-sdk-python/blob/release/3.1/modules/howtos/examples/subdocument%5Fops.py), from which you can see in context how to authenticate and connect to a Couchbase Cluster, then perform these sub-document operations.

## [](#sub-documents)Sub-documents

Starting with Couchbase Server 4.5 you can atomically and efficiently update and retrieve _parts_ of a document.

These parts are called _Sub-Documents_.

While full-document retrievals retrieve the entire document and full document updates require sending the entire document, Sub-Document retrievals only retrieve relevant parts of a document and Sub-Document updates only require sending the updated portions of a document.

You should use Sub-Document operations when you are modifying only portions of a document, and full-document operations when the contents of a document is to change significantly.

> [!IMPORTANT]
> The Sub-Document operations described on this page are for _Key-Value_ requests only: they are not related to Sub-Document SQL++ (formerly N1QL) queries. (Sub-Document SQL++ queries are explained in the section [Querying with SQL++](sqlpp-queries-with-sdk.md).)

In order to use Sub-Document operations you need to specify a _path_ indicating the location of the Sub-Document. The _path_ follows [SQL++ syntax](#path-syntax). Considering the document:

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

> [!IMPORTANT]
> The `lookup_in` method expects an `Iterable` of Sub-Document `Spec` (see [API reference doc](https://docs.couchbase.com/sdk-api/couchbase-python-client/couchbase%5Fapi/couchbase%5Fcore.html?highlight=collection%20lookup%5Fin#couchbase.collection.Collection.lookup%5Fin)). The examples below show how either a list or a tuple might be used. If using a tuple with only a single Sub-Document `Spec` **be sure** to include the trailing comma.

The _lookup\_in_ operations query the document for certain path(s); these path(s) are then returned. You have a choice of actually retrieving the document path using the _get_ Sub-Document operation, or simply querying the existence of the path using the _exists_ Sub-Document operation. The latter saves even more bandwidth by not retrieving the contents of the path if it is not needed.

Retrieve sub-document value

```python
result = collection.lookup_in('customer123',
                              [SD.get('addresses.delivery.country')])
country = result.content_as[str](0)  # 'United Kingdom'
```

Check existence of sub-document path

```python
result = collection.lookup_in('customer123', [SD.exists('purchases.pending[-1]')])
print(f'Path exists: {result.exists(0)}.')
# Path exists:  False.
```

Multiple operations can be combined:

Combine multiple lookup operations

```python
result = collection.lookup_in('customer123',[SD.get('addresses.delivery.country'),
                                             SD.exists('purchases.complete[-1]')])

print('{0}'.format(result.content_as[str](0)))
print('Path exists: {}.'.format(result.exists(1)))
# path exists: True.
```

## [](#mutating)Mutating

> [!IMPORTANT]
> The `mutate_in` method expects an `Iterable` of Sub-Document `Spec` (see [API reference doc](https://docs.couchbase.com/sdk-api/couchbase-python-client/couchbase%5Fapi/couchbase%5Fcore.html?highlight=collection%20mutate%5Fin#couchbase.collection.Collection.mutate%5Fin)). The examples below show how either a list or a tuple might be used. If using a tuple with only a single Sub-Document `Spec` **be sure** to include the trailing comma.

Mutation operations modify one or more paths in the document. The simplest of these operations is _upsert_, which, similar to the fulldoc-level _upsert_, will either modify the value of an existing path or create it if it does not exist:

Upserting a new sub-document

```python
collection.mutate_in('customer123', [SD.upsert('fax', '311-555-0151')])
```

Likewise, the _insert_ operation will only add the new value to the path if it does not exist:

Inserting a sub-document

```python
collection.mutate_in('customer123', [SD.insert('purchases.pending', [42, True, 'None'])])

try:
    collection.mutate_in('customer123', [SD.insert('purchases.complete',[42, True, 'None'])])
except PathExistsException:
    print('Path exists, cannot use insert.')
```

Dictionary values can also be replaced or removed, and you may combine any number of mutation operations within the same general _mutate\_in_ API. Here's an example of one which replaces one path and removes another.

```python
collection.mutate_in('customer123',(SD.remove('addresses.billing'),
                                    SD.replace('email','dougr96@hotmail.com')))
```

> [!NOTE]
> `mutateIn` is an _atomic_ operation. If any single `ops` fails, then the entire document is left unchanged.

## [](#array-append-and-prepend)Array append and prepend

The _array\_prepend_ and _array\_append_ operations are true array prepend and append operations. Unlike fulldoc _append_/_prepend_ operations (which simply concatenate bytes to the existing value), _array\_append_ and _array\_prepend_ are JSON-aware:

```python
collection.mutate_in('customer123', (SD.array_append('purchases.complete', 777),))

# purchases.complete is now [339, 976, 442, 666, 777]
```

```python
collection.mutate_in('customer123', [SD.array_prepend('purchases.abandoned', 18)])

# purchases.abandoned is now [18, 157, 42, 999]
```

If your document only needs to contain an array, you do not have to create a top-level object wrapper to contain it. Simply initialize the document with an empty array and then use the empty path for subsequent Sub-Document array operations:

Creating and populating an array document

```python
collection.upsert('my_array', [])
collection.mutate_in('my_array', [SD.array_append('', 'some element')])

# the document my_array is now ['some element']
```

If you wish to add multiple values to an array, you may do so by passing multiple values to the _array\_append_, _array\_prepend_, or _array\_insert_ operations. Be sure to know the difference between passing a collection of multiple elements (in which case the collection is inserted as a single element in the array, as a sub-array) and passing multiple elements (in which case the elements are appended individually to the array):

Add multiple elements to an array

```python
collection.mutate_in('my_array', [SD.array_append('', 'elem1', 'elem2', 'elem3')])

# the document my_array is now ['some_element', 'elem1', 'elem2', 'elem3']
```

Add single array as element to existing array

```python
collection.mutate_in('my_array', [SD.array_append('', ['elem4', 'elem5', 'elem6'])])

# the document my_array is now ['some_element', 'elem1', 'elem2', 'elem3',
#                                   ['elem4', 'elem5', 'elem6']]]
```

Note that passing multiple values to a single _array\_append_ operation results in greater performance increase and bandwidth savings than simply specifying a single _array\_append_ for each element.

Adding multiple elements to array (slow)

```python
collection.mutate_in('my_array', (SD.array_append('', 'elem7'),
                                  SD.array_append('', 'elem8'),
                                  SD.array_append('', 'elem9')))
```

If you wish to create an array if it does not exist and also push elements to it within the same operation you may use the _create\_parents_ option:

```python
collection.upsert('some_doc', {})
collection.mutate_in('some_doc', [SD.array_prepend('some.array',
                                                   'Hello',
                                                   'World',
                                                   create_parents=True)])
```

## [](#arrays-as-unique-sets)Arrays as Unique Sets

Limited support also exists for treating arrays like unique sets, using the _array\_addunique_ command. This will do a check to determine if the given value exists or not before actually adding the item to the array:

```python
try:
    collection.mutate_in('customer123', [SD.array_addunique('purchases.complete', 95)])
    print('Success!')
except PathExistsException:
    print('Path already exists.')

try:
    collection.mutate_in('customer123', [SD.array_addunique('purchases.complete', 95)])
    print('Success!')
except PathExistsException:
    print('Path already exists.')
```

Note that currently the _array\_addunique_ will fail with a _SubdocPathMismatchException_ if the array contains JSON _floats_, _objects_, or _arrays_. The _array\_addunique_ operation will also fail with _SubdocCantInsertValueException_ if the value to be added is one of those types as well.

Note that the actual position of the new element is undefined, and that the array is not ordered.

## [](#array-insertion)Array insertion

New elements can also be _inserted_ into an array. While _append_ will place a new item at the _end_ of an array and _prepend_ will place it at the beginning, _insert_ allows an element to be inserted at a specific _position_. The position is indicated by the last path component, which should be an array index. For example, to insert `"cruel"` as the second element in the array `["Hello", "world"]`, the code would look like:

```python
collection.upsert('array', [])
collection.mutate_in('array', [SD.array_append('', 'hello', 'world')])
collection.mutate_in('array', [SD.array_insert('[1]', 'cruel')])
```

Note that the array must already exist and that the index must be valid (i.e. it must not point to an element which is out of bounds).

## [](#counters-and-numeric-fields)Counters and Numeric Fields

Counter operations allow the manipulation of a _numeric_ value inside a document. These operations are logically similar to the _counter_ operation on an entire document:

```python
result = collection.mutate_in('customer123', (SD.counter('logins', 1),))
num_logins = collection.get('customer123').content_as[dict]['logins']
print(f'Number of logins: {num_logins}.')
# Number of logins: 1.
```

The _increment_ and _decrement_ operations perform simple arithmetic against a numeric value. The updated value is returned.

```python
player_key = 'player432'
collection.upsert(player_key, {'gold': 1000})

collection.mutate_in(player_key, (SD.counter('gold', -150),))
result = collection.lookup_in(player_key, (SD.get('gold'),))
print(f'{player_key} has {result.content_as[int](0)} gold remaining.')
# player432 has 850 gold remaining.
```

The existing value for counter operations must be within range of a 64 bit signed integer. If the value does not exist, the operation will create it (and its parents, if _create\_path_ is enabled).

Note that there are several differences as compared to the full-document counter operations:

* Sub-Document counters have a range of -9223372036854775807 to 9223372036854775807, whereas full-document counters have a range of 0 to 18446744073709551615
* Sub-Document counter operations protect against overflow and underflow, returning an error if the operation would exceed the range. Full-document counters will use normal C semantics for overflow (in which the overflow value is carried over above 0), and will silently fail on underflow, setting the value to 0 instead.
* Sub-Document counter operations can operate on any numeric value within a document, while [full-document counter operations](kv-operations.md#atomic-counters) require a specially formatted counter document with only the counter value.

## [](#executing-multiple-operations)Executing Multiple Operations

Multiple Sub-Document operations can be executed at once on the same document, allowing you to retrieve or modify several Sub-Documents at once. When multiple operations are submitted within the context of a single _lookup\_in_ or _mutate\_in_ command, the server will execute all the operations with the same version of the document.

> [!NOTE]
> Unlike _batched operations_ which is simply a way of sending multiple individual operations efficiently on the network, multiple Sub-Document operations are formed into a single command packet, which is then executed atomically on the server. You can submit up to 16 operations at a time.

When submitting multiple _mutation_ operations within a single _mutate\_in_ command, those operations are considered to be part of a single transaction: if any of the mutation operations fail, the server will logically roll-back any other mutation operations performed within the _mutate\_in_, even if those commands would have been successful had another command not failed.

When submitting multiple _retrieval_ operations within a single _lookup\_in_ command, the status of each command does not affect any other command. This means that it is possible for some retrieval operations to succeed and others to fail. While their statuses are independent of each other, you should note that operations submitted within a single _lookup\_in_ are all executed against the same _version_ of the document.

## [](#subdoc%5Fcreate%5Fpath)Creating Paths

Sub-Document mutation operations such as _upsert_ or _insert_ will fail if the _immediate parent_ is not present in the document. Consider:

```json
{
    "level_0": {
        "level_1": {
            "level_2": {
                "level_3": {
                    "some_field": "some_value"
                }
            }
        }
    }
}
```

Looking at the `some_field` field (which is really `level_0.level_1.level_2.level_3.some_field`), its _immediate_ parent is `level_3`. If we were to attempt to insert another field, `level_0.level_1.level_2.level_3.another_field`, it would succeed because the immediate parent is present. However if we were to attempt to _insert_ to `level_1.level_2.foo.bar` it would fail, because `level_1.level_2.foo` (which would be the immediate parent) does not exist. Attempting to perform such an operation would result in a Path Not Found error.

By default the automatic creation of parents is disabled, as a simple typo in application code can result in a rather confusing document structure. Sometimes it is necessary to have the server create the hierarchy however. In this case, the _create\_path_ option may be used.

```python
collection.mutate_in('customer123', [SD.upsert('level_0.level_1.foo.bar.phone',
                                               dict(
                                                   num='311-555-0101',
                                                   ext=16
                                               ), create_parents=True)])
```

## [](#reading-sub-documents-from-replicas)Reading Sub-Documents From Replicas

Couchbase Server 7.6 and later support Sub-Doc lookup from replicas.

The `collection.lookup_in_any_replica()` method returns the first response — from active or replica:

```python
try:    
    result = collection.lookup_in_any_replica('customer123',
                                              [SD.get('addresses.delivery.country')])
    country = result.content_as[str](0)  # 'United Kingdom'
    print(f'Country={country}')
    print(f'Is result replica={result.is_replica}')
except PathNotFoundException as ex:
    print(('The version of the document on the server node '
           'that responded quickest did not have the requested '
           'field.'))
    print(f'Exception={ex}')
except DocumentUnretrievableException as ex:
    print('Document not present on any server node.')
    print(f'Exception={ex}')
```

The `collection.lookup_in_all_replicas()` fetches all available replicas (and the active copy), and returns all responses.

```python
result = collection.lookup_in_all_replicas('customer123',
                                            [SD.get('addresses.delivery.country')])
for res in result:
    try:
        country = res.content_as[str](0)  # 'United Kingdom'
        print(f'Country={country}')
        print(f'Is result replica={res.is_replica}')
    except PathNotFoundException as ex:
        print(('The version of the document on one of the server nodes '
               'did not have the requested field.'))
        print(f'Exception={ex}')
```

You may want to use `lookup_in_all_replicas` to build a consensus, but it's more likely that you'll make use of `lookup_in_any_replica` as a fallback to a `lookupIn`, when the active node times out.

## [](#concurrent-modifications)Concurrent Modifications

Concurrent Sub-Document operations on different parts of a document will not conflict. For example the following two blocks can execute concurrently without any risk of conflict:

```python
collection.mutate_in('customer123', [SD.array_append('purchases.complete', 998)])
```

```python
collection.mutate_in('customer123', [SD.array_append('purchases.complete', 999)])
```

Even when modifying the _same_ part of the document, operations will not necessarily conflict. For example, two concurrent _array\_append_ operations to the same array will both succeed, never overwriting the other.

So in some cases the application will not need to supply a CAS value to protect against concurrent modifications.

If CAS is required then it can be provided like this:

```python
collection.mutate_in('customer123',
                     [SD.array_append('purchases.complete', 999)],
                     MutateInOptions(cas=1234))
```

## [](#durability)Durability

Couchbase's [traditional 'client verified' durability](../concept-docs/durability-replication-failure-considerations.md#older-server-versions), using `PersistTo` and `ReplicateTo`, is still available, particularly for talking to Couchbase Server 6.0 and earlier. Refer to the [API docs](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html?highlight=durability#couchbase.durability.ClientDurability.%5F%5Finit%5F%5F) for the legacy API.

```python
collection.mutate_in('key',
                     [SD.insert('username', 'dreynholm')],
                     MutateInOptions(durability=ClientDurability(ReplicateTo.ONE,
                                                                 PersistTo.ONE)))
```

In Couchbase Server 6.5 and up, this is built upon with [Durable Writes](../concept-docs/durability-replication-failure-considerations.md#durable-writes), which uses the concept of [majority](../../../server/current/learn/data/durability.md#majority) to indicate the number of configured Data Service nodes to which commitment is required:

```python
collection.mutate_in('customer123',
                     [SD.insert('username', 'dreynholm')],
                     MutateInOptions(durability=ServerDurability(Durability.MAJORITY)))
```

## [](#error-handling)Error Handling

Sub-Document operations have their own set of errors. When programming with Sub-Document, be prepared for any of the full-document errors (such as _DocumentDoesNotExistException_) as well as special Sub-Document errors which are received when certain constraints are not satisfied. Some of the errors include:

* **PathNotFoundException**: When retrieving a path, this means the path does not exist in the document. When inserting or upserting a path, this means the _immediate parent_ does not exist.
* **PathExistsException**: In the context of an _insert_, it means the given path already exists. In the context of _arrayAddUnique_, it means the given value already exists.
* **PathMismatchException**: This means the path may exist in the document, but that there is a type conflict between the path in the document and the path in the command. Consider the document:  
```json  
{ "tags": ["reno", "nevada", "west", "sierra"] }  
```  
The path `tags.sierra` is a mismatch, since `tags` is actually an array, while the path assumes it is a JSON object (dictionary).
* **DocumentNotJsonException**: This means you are attempting to modify a binary document using Sub-Document operations.
* **PathInvalidException**: This means the path is invalid for the command. Certain commands such as _arrayInsert_ expect array elements as their final component, while others such as _upsert_ and _insert_ expect dictionary (object) keys.

If a Sub-Document command fails a top-level error is reported (_MultiMutationException_), rather than an individual error code (e.g. _PathNotFoundException_). When receiving a top-level error code, you should traverse the results of the command to see which individual code failed.

## [](#path-syntax)Path Syntax

Path syntax largely follows SQL++ conventions: A path is divided into components, with each component referencing a specific _level_ in a document hierarchy. Components are separated by dots (`.`) in the case where the element left of the dot is a dictionary, or by brackets (`[n]`) where the element left of the bracket is an array and `n` is the index within the array.

As a special extension, you can indicate the _last element_ of an array by using an index of `-1`, for example to get the last element of the array in the document

```json
{"some":{"array":[1,2,3,4,5,6,7,8,9,0]}}
```

Use `some.array[-1]` as the path, which will return the element `0`.

Each path component must conform as a JSON string, as if it were surrounded by quotes, and any character in the path which may invalidate it as a JSON string must be escaped by a backslash (`\`). In other words, the path component must match exactly the path inside the document itself. For example:

```json
{"literal\"quote": {"array": []}}
```

must be referenced as `literal\"quote.array`.

If the path also has special path characters (i.e. a dot or brackets) it may be escaped using SQL++ escapes. Considering the document

```json
{"literal[]bracket": {"literal.dot": true}}
```

A path such as \`literal\[\]bracket\`.\`literal.dot\`. You can use double-backticks (\`\`) to reference a literal backtick.

If you need to combine both JSON _and_ path-syntax literals you can do so by escaping the component from any JSON string characters (e.g. a quote or backslash) and then encapsulating it in backticks (`` `path` ``).

> [!NOTE]
> Currently, paths cannot exceed 1024 characters, and cannot be more than 32 levels deep.

## [](#extended-attributes)Extended Attributes

Extended Attributes (also known as XATTRs), built upon the Sub-Document API, allow developers to define application-specific metadata that will only be visible to those applications that request it or attempt to modify it. This might be, for example, meta-data specific to a programming framework that should be hidden by default from other frameworks or libraries, or possibly from other versions of the same framework. They are not intended for use in general applications, and data stored there cannot be accessed easily by some Couchbase services, such as Search.