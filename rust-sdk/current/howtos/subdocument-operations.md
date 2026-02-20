---
title: Sub-Document Operations
description: Sub-Document operations can be used to efficiently access and
  change parts of documents.
editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/howtos/pages/subdocument-operations.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:rust-sdk:howtos:subdocument-operations.adoc[]
---

[View original HTML](/rust-sdk/current/howtos/subdocument-operations.html)

# Sub-Document Operations

> Sub-Document operations can be used to efficiently access and change parts of documents. 

Sub-Document operations may be quicker and more network-efficient than _full-document_ operations such as _upsert_, _replace_, and _get_ because they only transmit the accessed sections of the document over the network.

Sub-Document operations are also atomic, in that if one Sub-Document mutation fails then all will, allowing safe modifications to documents with built-in concurrency control.

## [](#sub-documents)Sub-Documents

You can atomically and efficiently update and retrieve _parts_ of a document. These parts are called _Sub-Documents_. While full-document retrievals retrieve the entire document and full document updates require sending the entire document, Sub-Document retrievals only retrieve relevant parts of a document and Sub-Document updates only require sending the updated portions of a document.

You should use Sub-Document operations when you are modifying only portions of a document, and full-document operations when the contents of a document is to change significantly.

> [!IMPORTANT]
> The Sub-Document operations described on this page are for _Key-Value_ requests only: they are not related to [Sub-Document SQL++ queries](../../../cloud/n1ql/n1ql-intro/queriesandresults.md#paths).

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

The paths `name`, `addresses.billing.country`, and `purchases.complete[0]` are all valid paths.

## [](#retrieving)Retrieving

The _lookupIn_ operations query the document for certain path(s); these path(s) are then returned. You have a choice of actually retrieving the document path using the _get_ Sub-Document operation, or simply querying the existence of the path using the _exists_ Sub-Document operation. The latter saves even more bandwidth by not retrieving the contents of the path if it is not needed.

Retrieve Sub-Document value

```rust
let result = collection
    .lookup_in(
        "customer123",
        &[LookupInSpec::get("addresses.delivery.country", None)],
        None,
    )
    .await?;

let country: String = result.content_as(0)?;
println!("Country: {country}");
```

Check existence of Sub-Document path

```rust
let result = collection
    .lookup_in(
        "customer123",
        &[LookupInSpec::exists(
            "addresses.delivery.does_not_exist",
            None,
        )],
        None,
    )
    .await?;

let exists: bool = result.content_as(0)?;
println!("Does field exist? {exists}");
```

> [!NOTE]
> LookupInResult has an `exists` method, but this should not be confused with the exists _operation_. The `exists` method is used to check if anything was returned by the server for a given operation. The result of the exists operation should be checked with `contentAs[Boolean]`, as in the example.

Multiple operations can be combined, and this can be most neatly done with a for-comprehension:

Combine multiple lookup operations

```rust
let result = {
    match collection
        .lookup_in(
            "customer123",
            &[
                LookupInSpec::get("addresses.delivery.country", None),
                LookupInSpec::exists("addresses.delivery.country", None),
            ],
            None,
        )
        .await
    {
        Ok(res) => {
            let country = res.content_as::<String>(0)?;
            let exists = res.content_as::<bool>(1)?;
            Ok((country, exists))
        }
        Err(e) => Err(e),
    }
};

match result {
    Ok((country, exists)) => {
        println!("Country: {country}, Exists: {exists}");
    }
    Err(e) => {
        println!("error: {e}")
    }
}
```

## [](#mutating)Mutating

Mutation operations modify one or more paths in the document. The simplest of these operations is _upsert_, which, similar to the fulldoc-level _upsert_, will either modify the value of an existing path or create it if it does not exist:

Upserting a new Sub-Document value

```rust
let result = collection
    .mutate_in(
        "customer123",
        &[MutateInSpec::upsert("email", "dougr96@hotmail.com", None)?],
        None,
    )
    .await;

match result {
    Ok(res) => {
        println!("Success!");
    }
    Err(e) => {
        println!("error: {e}")
    }
}
```

Likewise, the _insert_ operation will only add the new value to the path if it does not exist:

Inserting a Sub-Document value

```rust
let result = collection
    .mutate_in(
        "customer123",
        &[MutateInSpec::insert("email", "dougr96@hotmail.com", None)?],
        None,
    )
    .await;

match result {
    Ok(res) => {
        println!("Success!");
    }
    Err(e) => match e.kind() {
        couchbase::error::ErrorKind::PathExists => {
            println!("The field already exists.");
        }
        _ => {
            println!("error: {e}")
        }
    },
}
```

Dictionary values can also be replaced or removed, and you may combine any number of mutation operations within the same general _mutateIn_ API. Here’s an example of one which replaces one path and removes another.

```rust
let result = collection
    .mutate_in(
        "customer123",
        &[
            MutateInSpec::remove("addresses.billing", None),
            MutateInSpec::replace("email", "dougr96@hotmail.com", None)?,
        ],
        None,
    )
    .await;
```

> [!NOTE]
> `mutateIn` is an _atomic_ operation. If any single operation fails, then the entire document is left unchanged.

## [](#supported-types)Supported Types

Mutation operations can take primitives (`String`, `Int`, etc.), along with any type for which a `Serialize` implementation can be found.

See the [Data Operations page](kv-operations.md#json) for more details.

## [](#array-append-and-prepend)Array Append and Prepend

The _arrayPrepend_ and _arrayAppend_ operations are true array prepend and append operations. Unlike fulldoc _append_/_prepend_ operations (which simply concatenate bytes to the existing value), _arrayAppend_ and _arrayPrepend_ are JSON-aware:

```rust
let result = collection
    .mutate_in(
        "customer123",
        &[MutateInSpec::array_append(
            "purchases.complete",
            &[777],
            None,
        )?],
        None,
    )
    .await;
```

```rust
let result = collection
    .mutate_in(
        "customer123",
        &[MutateInSpec::array_prepend(
            "purchases.abandoned",
            &[18],
            None,
        )?],
        None,
    )
    .await;
```

If your document only needs to contain an array, you do not have to create a top-level object wrapper to contain it. Simply initialize the document with an empty array and then use the empty path for subsequent Sub-Document array operations:

Creating and populating an array document

```rust
let result = collection
    .mutate_in(
        "customer123",
        &[MutateInSpec::array_append("", &["some element"], None)?],
        None,
    )
    .await;
```

If you wish to create an array if it does not exist and also push elements to it within the same operation you may use the [_createPath_](#subdoc%5Fcreate%5Fpath) option:

```rust
let result = collection
    .mutate_in(
        "customer123",
        &[MutateInSpec::array_append(
            "some.array",
            &["hello world"],
            ArrayAppendSpecOptions::new().create_path(true),
        )?],
        None,
    )
    .await;
```

## [](#arrays-as-unique-sets)Arrays as Unique Sets

Limited support also exists for treating arrays like unique sets, using the _arrayAddUnique_ command. This will do a check to determine if the given value exists or not before actually adding the item to the array:

```rust
collection
    .mutate_in(
        "customer123",
        &[MutateInSpec::array_add_unique(
            "purchases.complete",
            95,
            None,
        )?],
        None,
    )
    .await?;

match collection
    .mutate_in(
        "customer123",
        &[MutateInSpec::array_add_unique(
            "purchases.complete",
            95,
            None,
        )?],
        None,
    )
    .await
{
    Ok(_) => println!("Added 95 to the array"),
    Err(e) => match e.kind() {
        couchbase::error::ErrorKind::PathExists => {
            println!("Path already exists");
        }
        _ => {
            println!("error: {e}")
        }
    },
}
```

Note that currently the _arrayAddUnique_ will fail with a _PathMismatchException_ if the array contains JSON _floats_, _objects_, or _arrays_. The _arrayAddUnique_ operation will also fail with _CannotInsertValueException_ if the value to be added is one of those types as well.

Note that the actual position of the new element is undefined, and that the array is not ordered.

## [](#array-insertion)Array Insertion

New elements can also be _inserted_ into an array. While _append_ will place a new item at the _end_ of an array and _prepend_ will place it at the beginning, _insert_ allows an element to be inserted at a specific _position_. The position is indicated by the last path component, which should be an array index. For example, to insert `"cruel"` as the second element in the array `["Hello", "world"]`, the code would look like:

```rust
let result = collection
    .mutate_in(
        "some_doc",
        &[MutateInSpec::array_insert("foo.bar[1]", &["cruel"], None)?],
        None,
    )
    .await;
```

Note that the array must already exist and that the index must be valid (i.e. it must not point to an element which is out of bounds).

## [](#counters-and-numeric-fields)Counters and Numeric Fields

Counter operations allow the manipulation of a _numeric_ value inside a document. These operations are logically similar to the _increment_ and _decrement_ full-document operations:

```rust
let result = collection
    .mutate_in(
        "customer123",
        &[MutateInSpec::increment("logins", 1, None)?],
        None,
    )
    .await?;

let new_value: i64 = result.content_as(0)?;
println!("New age: {new_value}");
```

The _increment_ and _decrement_ operations perform simple arithmetic against a numeric value. The updated value is returned.

```rust
collection
    .upsert("player432", json!({"gold": 1000}), None)
    .await?;

let result = collection
    .mutate_in(
        "player432",
        &[MutateInSpec::decrement("gold", 150, None)?],
        None,
    )
    .await?;

let new_value: i64 = result.content_as(0)?;
println!("New gold amount: {new_value}");
```

The existing value for counter operations must be within range of a 64 bit signed integer. If the value does not exist, the operation will create it (and its parents, if _createPath_ is enabled).

Note that there are several differences as compared to the full-document counter operations:

* Sub-Document counters have a range of -9223372036854775807 to 9223372036854775807, whereas full-document counters have a range of 0 to 18446744073709551615
* Sub-Document counter operations protect against overflow and underflow, returning an error if the operation would exceed the range. Full-document counters will use normal C semantics for overflow (in which the overflow value is carried over above 0), and will silently fail on underflow, setting the value to 0 instead.
* Sub-Document counter operations can operate on any numeric value within a document, while [full-document counter operations](kv-operations.md#atomic-counter-operations) require a specially formatted counter document with only the counter value.

## [](#executing-multiple-operations)Executing Multiple Operations

Multiple Sub-Document operations can be executed at once on the same document, allowing you to retrieve or modify several Sub-Documents at once. When multiple operations are submitted within the context of a single _lookupIn_ or _mutateIn_ command, the server will execute all the operations with the same version of the document.

> [!NOTE]
> Multiple Sub-Document operations are formed into a single command packet, which is then executed atomically on the server. You can submit up to 16 operations at a time.

When submitting multiple _mutation_ operations within a single _mutateIn_ command, those operations are considered to be part of a single transaction: if any of the mutation operations fail, the server will logically roll-back any other mutation operations performed within the _mutateIn_, even if those commands would have been successful had another command not failed.

When submitting multiple _retrieval_ operations within a single _lookupIn_ command, the status of each command does not affect any other command. This means that it is possible for some retrieval operations to succeed and others to fail. While their statuses are independent of each other, you should note that operations submitted within a single _lookupIn_ are all executed against the same _version_ of the document.

## [](#creating-paths)Creating Paths

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

By default the automatic creation of parents is disabled, as a simple typo in application code can result in a rather confusing document structure. Sometimes it is necessary to have the server create the hierarchy however. In this case, the _createPath_ option may be used.

```rust
let result = collection
    .mutate_in(
        "customer123",
        &[MutateInSpec::upsert(
            "level_0.level_1.foo.bar.phone",
            json!({"num": "311-555-0101", "ext": 16}),
            UpsertSpecOptions::new().create_path(true),
        )?],
        None,
    )
    .await;
```

## [](#concurrent-modifications)Concurrent Modifications

Concurrent Sub-Document operations on different parts of a document will not conflict. For example the following two blocks can execute concurrently without any risk of conflict:

```rust
let collection1 = collection.clone();
let handle1 = tokio::spawn(async move {
    collection1
        .mutate_in(
            "customer123",
            &[MutateInSpec::array_append(
                "purchases.complete",
                &[99],
                None,
            )?],
            None,
        )
        .await
});

let handle2 = tokio::spawn(async move {
    collection
        .mutate_in(
            "customer123",
            &[MutateInSpec::array_append(
                "purchases.abandoned",
                &[101],
                None,
            )?],
            None,
        )
        .await
});

// These are spawned tasks, so they run concurrently even though we await in serial.
// We use unwrap for brevity, it only applies here if the task itself panicked.
handle1.await.unwrap()?;
handle2.await.unwrap()?;
```

Even when modifying the _same_ part of the document, operations will not necessarily conflict. For example, two concurrent _arrayAppend_ operations to the same array will both succeed, never overwriting the other.

So in some cases the application will not need to supply a [CAS](concurrent-document-mutations.md) value to protect against concurrent modifications.

If CAS is required then it can be provided like this:

```rust
collection
    .mutate_in(
        "player432",
        &[MutateInSpec::decrement("gold", 150, None)?],
        MutateInOptions::new().cas(12345),
    )
    .await?;
```

## [](#durability)Durability

For more information see [Durable Writes](../concept-docs/durability-replication-failure-considerations.md#durable-writes), which uses the concept of [majority](../../../server/current/learn/data/durability.md#majority) to indicate the number of configured Data Service nodes to which commitment is required:

```rust
collection
    .mutate_in(
        "player432",
        &[MutateInSpec::decrement("gold", 150, None)?],
        MutateInOptions::new().durability_level(DurabilityLevel::MAJORITY),
    )
    .await?;
```

## [](#error-handling)Error Handling

Sub-Document operations have their own set of errors. When programming with Sub-Document, be prepared for any of the full-document errors (such as _DocumentNotFoundException_) as well as special Sub-Document errors which are received when certain constraints are not satisfied. Some of the errors include:

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