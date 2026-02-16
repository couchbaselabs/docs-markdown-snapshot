[View original HTML](/go-sdk/current/howtos/subdocument-operations.html)

> Sub-Document operations can be used to efficiently access and change parts of documents. 

Sub-Document operations may be quicker and more network-efficient than _full-document_ operations such as _Upsert_, _Replace_ and _Get_ because they only transmit the accessed sections of the document over the network.

Sub-Document operations are also atomic, in that if one Sub-Document mutation fails then all will, allowing safe modifications to documents with built-in concurrency control.

## [](#sub-documents)Sub-documents

Starting with Couchbase Server 4.5 you can atomically and efficiently update and retrieve _parts_ of a document.

These parts are called _Sub-Documents_.

While full-document retrievals retrieve the entire document and full document updates require sending the entire document, Sub-Document retrievals only retrieve relevant parts of a document and Sub-Document updates only require sending the updated portions of a document.

You should use sub-document operations when you are modifying only portions of a document, and full-document operations when the contents of a document is to change significantly.

|  | The Sub-Document operations described on this page are for _Key-Value_ requests only: they are not related to Sub-Document [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) queries. Sub-document SQL++ queries are explained in the [Query page](n1ql-queries-with-sdk.md). |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

In order to use Sub-Document operations you need to specify a _path_ indicating the location of the Sub-Document. The _path_ follows [SQL++ syntax](#Path syntax).

Considering the document:

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

## [](#lookupin-and-mutatein)LookupIn and MutateIn

The `LookupIn` and `MutateIn` operations the executors for subdocument specifications. These two functions are located on the `Collection` and both accept a list of "Specs" which describe what work needs to be done. Each different type of operation has a corresponding "spec", for example `GetSpec` or `UpsertSpec`. Other than specs which are unique to subdoc the naming should be very similar to corresponding KV operations with "Spec" added on the end. Note: Unlike KV or the _LookupIn_ and _MutateIn_ operations the "Spec" functions live on the root level, i.e. `gocb.GetSpec`These specs can be combined to fetch or mutate multiple fields in a document, more detail can be seen in [_Executing Multiple Documents_](#executing-multiple-operations).

## [](#retrieving)Retrieving

The _LookupIn_ operations query the document for certain path(s); these path(s) are then returned. You have a choice of actually retrieving the document path using the `GetSpec` Sub-Document specification, or simply querying the existence of the path using the `ExistsSpec` Sub-Document specification. The latter saves even more bandwidth by not retrieving the contents of the path if it is not needed. The `LookupInResult` contains two functions for inspecting the results:

* `err := result.ContentAt(idx, &valuePtr)` which will either assign the value at the index specified into the value pointer or it will return an error (such as if the path does not exist)
* `exists := result.Exists(idx)` which will return whether or not the path at the index specified exists.

| Spec       | Function                | Path exists | Result         |
| ---------- | ----------------------- | ----------- | -------------- |
| GetSpec    | ContentAt(idx, &valPtr) | Yes         | Value assigned |
| GetSpec    | ContentAt(idx, &valPtr) | No          | Error returned |
| GetSpec    | Exists(idx)             | Yes         | true           |
| GetSpec    | Exists(idx)             | No          | false          |
| ExistsSpec | ContentAt(idx, &valPtr) | Yes         | Value assigned |
| ExistsSpec | ContentAt(idx, &valPtr) | No          | Error returned |
| ExistsSpec | Exists(idx)             | Yes         | true           |
| ExistsSpec | Exists(idx)             | No          | false          |

Retrieve Sub-Document value

```go
ops := []gocb.LookupInSpec{
	gocb.GetSpec("addresses.delivery.country", &gocb.GetSpecOptions{}),
}
res, err := collection.LookupIn("customer123", ops, &gocb.LookupInOptions{})
if err != nil {
	panic(err)
}

var country string
err = res.ContentAt(0, &country)
if err != nil {
	panic(err)
}
fmt.Println(country) // United Kingdom
```

|  | The value pointer provided to the ContentAt function must match the type at the provided index. |
|  | ----------------------------------------------------------------------------------------------- |

Check existence of Sub-Document path

```go
ops := []gocb.LookupInSpec{
	gocb.ExistsSpec("purchases.pending[-1]", &gocb.ExistsSpecOptions{}),
}
res, err := collection.LookupIn("customer123", ops, &gocb.LookupInOptions{})
if err != nil {
	panic(err)
}

exists := res.Exists(0)

fmt.Printf("Path exists? %t\n", exists) // Path exists? false
```

|  | Using ExistsSpec with ContentAt will return an error if the path does not exist. |
|  | -------------------------------------------------------------------------------- |

Multiple operations can be combined as well:

Combine multiple lookup operations

```go
ops := []gocb.LookupInSpec{
	gocb.GetSpec("addresses.delivery.country", nil),
	gocb.ExistsSpec("purchases.pending[-1]", nil),
}
res, err := collection.LookupIn("customer123", ops, &gocb.LookupInOptions{
	Timeout: 50 * time.Millisecond,
})
if err != nil {
	panic(err)
}

var country string
err = res.ContentAt(0, &country)
if err != nil {
	panic(err)
}
exists := res.Exists(1)

fmt.Println(country)                    // United Kingdom
fmt.Printf("Path exists? %t\n", exists) // Path exists? false
```

## [](#mutating)Mutating

Mutation operations modify one or more paths in the document. The simplest of these operations is _Upsert_, which, similar to the fulldoc-level _Upsert_, will either modify the value of an existing path or create it if it does not exist:

Upserting a new Sub-Document

```go
mops := []gocb.MutateInSpec{
	gocb.UpsertSpec("fax", "311-555-0151", &gocb.UpsertSpecOptions{}),
}
upsertResult, err := collection.MutateIn("customer123", mops, &gocb.MutateInOptions{
	Timeout: 10050 * time.Millisecond,
})
if err != nil {
	panic(err)
}
```

Likewise, the _Insert_ operation will only add the new value to the path if it does not exist:

Inserting a Sub-Document

```go
mops = []gocb.MutateInSpec{
	gocb.InsertSpec("purchases.pending", []interface{}{32, true, "None"}, &gocb.InsertSpecOptions{}),
}
insertResult, err := collection.MutateIn("customer123", mops, &gocb.MutateInOptions{})
if err != nil {
	panic(err)
}
```

Dictionary values can also be replaced or removed, and you may combine any number of mutation operations within the same general _mutateIn_ API. Here’s an example of one which replaces one path and removes another.

Combine multiple mutate operations

```go
mops = []gocb.MutateInSpec{
	gocb.RemoveSpec("addresses.billing", nil),
	gocb.ReplaceSpec("email", "dougr96@hotmail.com", nil),
}
multiMutateResult, err := collection.MutateIn("customer123", mops, &gocb.MutateInOptions{})
if err != nil {
	panic(err)
}
```

|  | MutateIn is an _atomic_ operation. If any single ops fails, then the entire document is left unchanged. |
|  | ------------------------------------------------------------------------------------------------------- |

## [](#array-append-and-prepend)Array Append and Prepend

The _ArrayPrepend_ and _ArrayAppend_ operations are true array prepend and append operations. Unlike fulldoc _Append_/_Prepend_ operations (which simply concatenate bytes to the existing value), _ArrayAppend_ and _ArrayPrepend_ are JSON-aware:

Array appending a sub-document

```go
mops := []gocb.MutateInSpec{
	gocb.ArrayAppendSpec("purchases.complete", 777, nil),
}
arrayAppendResult, err := collection.MutateIn("customer123", mops, &gocb.MutateInOptions{})
if err != nil {
	panic(err)
}
// purchases.complete is now [339, 976, 442, 666, 777]
```

Array prepending a sub-document

```go
mops = []gocb.MutateInSpec{
	gocb.ArrayPrependSpec("purchases.abandoned", 17, nil),
}
arrayPrependResult, err := collection.MutateIn("customer123", mops, &gocb.MutateInOptions{})
if err != nil {
	panic(err)
}
// purchases.abandoned is now [18, 157, 49, 999]
```

If your document only needs to contain an array, you do not have to create a top-level object wrapper to contain it. Simply initialize the document with an empty array and then use the empty path for subsequent Sub-Document array operations:

Creating and populating an array document

```go
upsertDocResult, err := collection.Upsert("my_array", []int{}, nil)
if err != nil {
	panic(err)
}

mops = []gocb.MutateInSpec{
	gocb.ArrayAppendSpec("", "some element", &gocb.ArrayAppendSpecOptions{}),
}
arrayAppendRootResult, err := collection.MutateIn("my_array", mops, &gocb.MutateInOptions{
	Cas: upsertDocResult.Cas(),
})
if err != nil {
	panic(err)
}
// the document my_array is now ["some element"]
```

Note that in the above we carried over the CAS value from the Upsert operation to ensure that if someone else modified the document first then our change would error. You can read more about CAS in the [CAS page](concurrent-document-mutations.md).

If you wish to add multiple values to an array, you may do so by passing multiple values to the _ArrayAppend_, _ArrayPrepend_, or _ArrayInsert_ operations.

Be sure to know the difference between the use of the _HasMultiple_ option being false (in which case the collection is inserted as a single element in the array, as a sub-array) and it being true (in which case the elements are appended individually to the array):

Add multiple elements to an array

```go
mops = []gocb.MutateInSpec{
	gocb.ArrayAppendSpec("", []string{"elem1", "elem2", "elem3"}, &gocb.ArrayAppendSpecOptions{
		HasMultiple: true, // this signifies that the value is multiple array elements rather than one
	}),
}
multiArrayAppendResult, err := collection.MutateIn("my_array", mops, &gocb.MutateInOptions{})
if err != nil {
	panic(err)
}
// the document my_array is now ["some_element", "elem1", "elem2", "elem3"]
```

Add single array as element to existing array

```go
mops = []gocb.MutateInSpec{
	gocb.ArrayAppendSpec("", []string{"elem1", "elem2", "elem3"}, &gocb.ArrayAppendSpecOptions{}),
}
singleArrayAppendResult, err := collection.MutateIn("my_array", mops, &gocb.MutateInOptions{})
if err != nil {
	panic(err)
}
// the document my_array is now ["some_element", "elem1", "elem2", "elem3", ["elem1", "elem2", "elem3"]]
```

Note that using _HasMultiple_ with a single _ArrayAppend_ operation results in greater performance increase and bandwidth savings than simply specifying a single _ArrayAppend_ for each element. Below we set elements individually to achieve the same as the `HasMultiple` example above:

Adding multiple elements to array (slow)

```go
mops = []gocb.MutateInSpec{
	gocb.ArrayAppendSpec("", "elem1", &gocb.ArrayAppendSpecOptions{}),
	gocb.ArrayAppendSpec("", "elem2", &gocb.ArrayAppendSpecOptions{}),
	gocb.ArrayAppendSpec("", "elem3", &gocb.ArrayAppendSpecOptions{}),
}
individualArrayAppendResult, err := collection.MutateIn("my_array", mops, &gocb.MutateInOptions{})
if err != nil {
	panic(err)
}
```

If you wish to create an array if it does not exist and also push elements to it within the same operation you may use the [_CreatePath_](#subdoc%5Fcreate%5Fpath) option:

Array appending a sub-document with create path

```go
// Create an empty document so that MutateIn can create the path.
_, err = collection.Upsert("my_object", map[string]interface{}{}, nil)
if err != nil {
	panic(err)
}

mops = []gocb.MutateInSpec{
	gocb.ArrayAppendSpec("some.array", []string{"Hello", "World"}, &gocb.ArrayAppendSpecOptions{
		HasMultiple: true,
		CreatePath:  true,
	}),
}
createPathResult, err := collection.MutateIn("my_object", mops, &gocb.MutateInOptions{})
if err != nil {
	panic(err)
}
```

## [](#arrays-as-unique-sets)Arrays as Unique Sets

Limited support also exists for treating arrays like unique sets, using the _ArrayAddUnique_ command. This will do a check to determine if the given value exists or not before actually adding the item to the array:

Adding unique elements to arrays

```go
mops = []gocb.MutateInSpec{
	gocb.ArrayAddUniqueSpec("purchases.complete", 95, &gocb.ArrayAddUniqueSpecOptions{}),
}
arrayAddUniqueResult, err := collection.MutateIn("customer123", mops, &gocb.MutateInOptions{})
if err != nil {
	panic(err)
}

mops = []gocb.MutateInSpec{
	gocb.ArrayAddUniqueSpec("purchases.complete", 95, &gocb.ArrayAddUniqueSpecOptions{}),
}
_, err = collection.MutateIn("customer123", mops, &gocb.MutateInOptions{})
fmt.Println(errors.Is(err, gocb.ErrPathExists)) // true
```

Note that currently the _ArrayAddUnique_ will fail with a _Path Mismatch_ error if the array contains JSON _floats_, _objects_, or _arrays_. The _ArrayAddUnique_ operation will also fail with _Cannot Insert_ if the value to be added is one of those types as well.

Note that the actual position of the new element is undefined, and that the array is not ordered.

## [](#array-insertion)Array Insertion

New elements can also be _inserted_ into an array.

While _append_ will place a new item at the _end_ of an array and _prepend_ will place it at the beginning, _insert_ allows an element to be inserted at a specific _position_.

The position is indicated by the last path component, which should be an array index. For example, to insert `"Cruel"` as the second element in the array `["Hello", "world"]`, the code would look like:

Inserting elements into arrays

```go
mops = []gocb.MutateInSpec{
	gocb.ArrayInsertSpec("some.array[1]", "Cruel", &gocb.ArrayInsertSpecOptions{}),
}
arrayInsertResult, err := collection.MutateIn("my_object", mops, &gocb.MutateInOptions{})
if err != nil {
	panic(err)
}
// The value at some.array is now [Hello, Cruel, World]
```

Note that the array must already exist and that the index must be valid (i.e. it must not point to an element which is out of bounds).

## [](#counters-and-numeric-fields)Counters and Numeric Fields

Counter operations allow the manipulation of a _numeric_ value inside a document. These operations are logically similar to the _counter_ operation on an entire document:

Incrementing a counter

```go
mops := []gocb.MutateInSpec{
	gocb.IncrementSpec("logins", 1, &gocb.CounterSpecOptions{}),
}
incrementResult, err := collection.MutateIn("customer123", mops, &gocb.MutateInOptions{})
if err != nil {
	panic(err)
}

var logins int
err = incrementResult.ContentAt(0, &logins)
if err != nil {
	panic(err)
}
fmt.Println(logins) // 1
```

The _Increment_ and _Decrement_ operations perform simple arithmetic against a numeric value. The updated value is returned.

Decrementing a counter

```go
_, err = collection.Upsert("player432", map[string]int{"gold": 1000}, &gocb.UpsertOptions{})
if err != nil {
	panic(err)
}

mops = []gocb.MutateInSpec{
	gocb.DecrementSpec("gold", 150, &gocb.CounterSpecOptions{}),
}
decrementResult, err := collection.MutateIn("player432", mops, &gocb.MutateInOptions{})
if err != nil {
	panic(err)
}

var gold int
err = decrementResult.ContentAt(0, &gold)
if err != nil {
	panic(err)
}
fmt.Printf("player 432 now has %d gold remaining\n", gold)
// player 432 now has 850 gold remaining
```

The existing value for _counter_ operations must be within range of a 64 bit signed integer. If the value does not exist, the operation will create it (and its parents, if _CreatePath_ is enabled).

Note that there are several differences as compared the full-document _counter_ operations:

* Sub-Document counters have a range of -9223372036854775807 to 9223372036854775807 (i.e. `Iint64.MinValue` and `` Int64.MaxValue), whereas full-document counters have a range of 0 to 18446744073709551615 (`UInt64.MaxValue ``)
* Sub-Document counter operations protect against overflow and underflow, returning an error if the operation would exceed the range. Full-document counters will use normal C semantics for overflow (in which the overflow value is carried over above 0), and will silently fail on underflow, setting the value to 0 instead.
* Sub-Document counter operations can operate on any numeric value within a document, while [full-document counter operations](kv-operations.md#atomic-counters) require a specially formatted counter document with only the counter value.

## [](#executing-multiple-operations)Executing Multiple Operations

Multiple Sub-Document operations can be executed at once on the same document, allowing you to retrieve or modify several Sub-Documents at once. When multiple operations are submitted within the context of a single _LookupIn_ or _MutateIn_ command, the server will execute all the operations with the same version of the document.

|  | Unlike _batched operations_ which is simply a way of sending multiple individual operations efficiently on the network, multiple Sub-Document operations are formed into a single command packet, which is then executed atomically on the server. You can submit up to 16 operations at a time. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

When submitting multiple _mutation_ operations within a single _MutateIn_ command, those operations are considered to be part of a single transaction: if any of the mutation operations fail, the server will logically roll-back any other mutation operations performed within the _MutateIn_, even if those commands would have been successful had another command not failed.

When submitting multiple _retrieval_ operations within a single _LookupIn_ command, the status of each command does not affect any other command. This means that it is possible for some retrieval operations to succeed and others to fail. While their statuses are independent of each other, you should note that operations submitted within a single _LookupIn_ are all executed against the same _version_ of the document.

## [](#subdoc-create-path)Creating Paths

Sub-Document mutation operations such as _Upsert_ or _Insert_ will fail if the _immediate parent_ is not present in the document. Consider:

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

Looking at the `some_field` field (which is really `level_0.level_1.level_2.level_3.some_field`), its _immediate_ parent is `level_3`.

If we were to attempt to insert another field, `level_0.level_1.level_2.level_3.another_field`, it would succeed because the immediate parent is present.

However if we were to attempt to _Insert_ to `level_1.level_2.foo.bar` it would fail, because `level_1.level_2.foo` (which would be the immediate parent) does not exist.

Attempting to perform such an operation would result in a Path Not Found error.

By default the automatic creation of parents is disabled, as a simple typo in application code can result in a rather confusing document structure. Sometimes it is necessary to have the server create the hierarchy however.

In this case, the _CreatePath_ option may be used.

Upsert with CreatePath

```go
mops = []gocb.MutateInSpec{
	gocb.UpsertSpec("level_0.level_1.foo.bar.phone", map[string]interface{}{
		"num": "311-555-0101",
		"ext": 16,
	}, &gocb.UpsertSpecOptions{
		CreatePath: true,
	}),
}
createPathUpsertResult, err := collection.MutateIn("customer123", mops, &gocb.MutateInOptions{})
if err != nil {
	panic(err)
}
```

## [](#reading-sub-documents-from-replicas)Reading Sub-Documents From Replicas

Couchbase Server 7.6 and later support Sub-Doc lookup from replicas.

The `Collection.LookupInAnyReplica` method returns the first response — from active or replica:

Sub-Document read from any replica

```go
ops := []gocb.LookupInSpec{
	gocb.GetSpec("addresses.delivery.country", &gocb.GetSpecOptions{}),
}
res, err := collection.LookupInAnyReplica("customer123", ops, nil)
if err != nil {
	panic(err)
}

var country string
err = res.ContentAt(0, &country)
if err != nil {
	panic(err)
}

fmt.Println(country) // United Kingdom
fmt.Printf("Is replica? %t\n", res.IsReplica())
```

The `Collection.LookupInAllReplicas` method fetches all available replicas (and the active copy), and returns all responses:

Sub-Document read from all replicas

```go
ops := []gocb.LookupInSpec{
	gocb.GetSpec("addresses.delivery.country", &gocb.GetSpecOptions{}),
}
stream, err := collection.LookupInAllReplicas("customer123", ops, nil)
if err != nil {
	panic(err)
}

for {
	replicaRes := stream.Next()
	if replicaRes == nil {
		break
	}

	var country string
	err = replicaRes.ContentAt(0, &country)
	if err != nil {
		panic(err)
	}

	fmt.Println(country) // United Kingdom
	fmt.Printf("Is replica? %t\n", replicaRes.IsReplica())
}
```

The results for both operations have type `LookupInReplicaResult` which exposes the same interface as `LookupInResult`, with the addition of an `IsReplica()` method that indicates whether the result originated from a replica or an active node.

## [](#concurrent-modifications)Concurrent Modifications

Concurrent Sub-Document operations on different parts of a document will not conflict. For example the following two blocks can execute concurrently without any risk of conflict:

Performing concurrent Sub Document mutations

```go
mops := []gocb.MutateInSpec{
	gocb.ArrayAppendSpec("purchases.complete", 99, &gocb.ArrayAppendSpecOptions{}),
}
firstConcurrentResult, err := collection.MutateIn("customer123", mops, &gocb.MutateInOptions{})
if err != nil {
	panic(err)
}

mops = []gocb.MutateInSpec{
	gocb.ArrayAppendSpec("purchases.abandoned", 101, &gocb.ArrayAppendSpecOptions{}),
}
secondConcurrentResult, err := collection.MutateIn("customer123", mops, &gocb.MutateInOptions{})
if err != nil {
	panic(err)
}
```

Even when modifying the _same_ part of the document, operations will not necessarily conflict. For example, two concurrent _ArrayAppend_ operations to the same array will both succeed, never overwriting the other.

So in some cases the application will not need to supply a [CAS](concurrent-document-mutations.md) value to protect against concurrent modifications. If CAS is required then it can be provided like this:

Performing concurrent Sub Document mutations with CAS

```go
getRes, err := collection.Get("player432", &gocb.GetOptions{})
if err != nil {
	panic(err)
}

mops = []gocb.MutateInSpec{
	gocb.DecrementSpec("gold", 150, &gocb.CounterSpecOptions{}),
}
decrementCasResult, err := collection.MutateIn("player432", mops, &gocb.MutateInOptions{
	Cas: getRes.Cas(),
})
if err != nil {
	panic(err)
}
```

## [](#durability)Durability

Couchbase’s [traditional durability](#1.6@go-sdk::durability.adoc), using `PersistTo` and `ReplicateTo`, is [still available](../concept-docs/durability-replication-failure-considerations.md#older-server-versions), particularly for talking to Couchbase Server 6.0 and earlier:

Performing Sub Document mutations with traditional durability

```go
mops := []gocb.MutateInSpec{
	gocb.InsertSpec("name", "mike", nil),
}
observeResult, err := collection.MutateIn("key", mops, &gocb.MutateInOptions{
	PersistTo:     1,
	ReplicateTo:   1,
	StoreSemantic: gocb.StoreSemanticsUpsert,
})
if err != nil {
	panic(err)
}
```

In Couchbase Server 6.5 and up, this is built upon with [Durable Writes](../concept-docs/durability-replication-failure-considerations.md#durable-writes), which uses the concept of [majority](../../../server/current/learn/data/durability.md#majority) to indicate the number of configured Data Service nodes to which commitment is required:

Performing Sub Document mutations with Durable Writes

```go
mops = []gocb.MutateInSpec{
	gocb.InsertSpec("name", "mike", nil),
}
durableResult, err := collection.MutateIn("key2", mops, &gocb.MutateInOptions{
	DurabilityLevel: gocb.DurabilityLevelMajority,
	StoreSemantic:   gocb.StoreSemanticsUpsert,
})
if err != nil {
	panic(err)
}
```

## [](#error-handling)Error handling

Subdoc operations have their own set of errors. When programming with subdoc, be prepared for any of the full-document errors (such as _Document Not Found_) as well as special sub-document errors which are received when certain constraints are not satisfied.

Some of the errors include:

* **Path does not exist**: When retrieving a path, this means the path does not exist in the document. When inserting or upserting a path, this means the _immediate parent_ does not exist. This can be detected with `errors.Is(err, gocb.ErrPathNotFound)`.
* **Path already exists**: In the context of an _Insert_, it means the given path already exists. In the context of _ArrayAddUnique_, it means the given value already exists. This can be detected with `errors.Is(err, gocb.ErrPathExists)`.
* **Path mismatch**: This means the path may exist in the document, but that there is a type conflict between the path in the document and the path in the command. This can be detected with `errors.Is(err, gocb.ErrPathMismatch)`.

Consider the document:

```json
{ "tags": ["reno", "nevada", "west", "sierra"] }
```

\+ The path `tags.sierra` is a mismatch, since `tags` is actually an array, while the path assumes it is a JSON object (dictionary).

* **Document not JSON**: This means you are attempting to modify a binary document using sub-document operations.
* **Invalid path**: This means the path is invalid for the command. Certain commands such as _ArrayInsert_ expect array elements as their final component, while others such as _Upsert_ and _Insert_ expect dictionary (object) keys.

If a Sub-Document command fails a top-level error is reported (_Multi Command Failure_), rather than an individual error code (e.g. _Path Not Found_). When receiving a top-level error code, you should traverse the results of the command to see which individual code failed.

## [](#path-syntax)Path Syntax

Path syntax largely follows SQL++ conventions: A path is divided into components, with each component referencing a specific _level_ in a document hierarchy. Components are separated by dots (`.`) in the case where the element left of the dot is a dictionary, or by brackets (`[n]`) where the element left of the bracket is an array and `n` is the index within the array.

As a special extension, you can indicate the _last element_ of an array by using an index of `-1`, for example to get the last element of the array in the document

```json
{"some":{"array":[1,2,3,4,5,6,7,8,9,0]}}
```

Use `some.array[-1]` as the path, which will return the element `0`.

Each path component must conform as a JSON string, as if it were surrounded by quotes, and any character in the path which may invalidate it as a JSON string must be escaped by a backslash (`\`). In other words, the path component must match exactly the path inside the document itself.

For example:

```json
{"literal\"quote": {"array": []}}
```

must be referenced as `literal\"quote.array`.

If the path also has special path characters (i.e. a dot or brackets) it may be escaped using SQL++ escapes.

Considering the document

```json
{"literal[]bracket": {"literal.dot": true}}
```

A path such as \`literal\[\]bracket\`.\`literal.dot\`. You can use double-backticks (\`\`) to reference a literal backtick.

If you need to combine both JSON _and_ path-syntax literals you can do so by escaping the component from any JSON string characters (e.g. a quote or backslash) and then encapsulating it in backticks (`` `path` ``).

|  | Currently, paths cannot exceed 1024 characters, and cannot be more than 32 levels deep. |
|  | --------------------------------------------------------------------------------------- |

## [](#extended-attributes)Extended Attributes

Extended Attributes (also known as XATTRs), built upon the Sub-Document API, allow developers to define application-specific metadata that will only be visible to those applications that request it or attempt to modify it. This might be, for example, meta-data specific to a programming framework that should be hidden by default from other frameworks or libraries, or possibly from other versions of the same framework. They are not intended for use in general applications, and data stored there cannot be accessed easily by some Couchbase services, such as Search.