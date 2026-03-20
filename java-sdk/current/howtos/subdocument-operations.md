---
title: Sub-Document Operations
description: Sub-Document operations can be used to efficiently access and
  change parts of documents.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.11/modules/howtos/pages/subdocument-operations.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:java-sdk:howtos:subdocument-operations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/current/howtos/subdocument-operations.html)

# Sub-Document Operations

> Sub-Document operations can be used to efficiently access and change parts of documents. 

Sub-Document operations may be quicker and more network-efficient than _full-document_ operations such as _upsert_, _replace_ and _get_ because they only transmit the accessed sections of the document over the network.

Sub-Document operations are also atomic, in that if one Sub-Document mutation fails then all will, allowing safe modifications to documents with built-in concurrency control.

## [](#sub-documents)Sub-Documents

While full-document retrievals retrieve the entire document and full document updates require sending the entire document, Sub-Document retrievals only retrieve relevant parts of a document and Sub-Document updates only require sending the updated portions of a document.

You should use Sub-Document operations when you are modifying only portions of a document, and full-document operations when the contents of a document is to change significantly.

> [!IMPORTANT]
> The Sub-Document operations described on this page are for _Key-Value_ requests only: they are not related to Sub-Document [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) queries.  
> Sub-Document SQL++ queries are explained in the section [Querying with SQL++](sqlpp-queries-with-sdk.md).

In order to use Sub-Document operations you need to specify a _path_ indicating the location of the Sub-Document. The _path_ follows [Path syntax](#path-syntax). Considering the document:

hotel\_1368.json

```json
{
  "title": "Ayr (Scotland)",
  "name": "Enterkine House Hotel",
  "address": "by Annbank. Ayrshire",
  "directions": "5 miles off A77, follow B742 to Mossblown then Annbank",
  "phone": "+44 1292 520580",
  "tollfree": null,
  "email": null,
  "fax": null,
  "url": "http://www.enterkine.com",
  "checkin": "2.00pm",
  "checkout": "11am",
  "price": "from £100",
  "geo": {
    "lat": 55.48034590743372,
    "lon": -4.51612114906311,
    "accuracy": "ROOFTOP"
  },
  "type": "hotel",
  "id": 1368,
  "country": "United Kingdom",
  "city": "South Ayrshire",
  "state": null,
  "reviews": [],
  "public_likes": ["Georgette Rutherford V", "Ms. Devante Bruen", "Anderson Schmidt", "Mr. Kareem Harvey", "Tessie Shields", "Floyd Bradtke III", "Maurice McDermott", "Michel Franecki", "Laila Ernser"],
  "vacancy": true,
  "description": "four star country house hotel situated in 350 acres of woodland estate yet only 10 mins from Prestwick ,Ayr and Troon. Award winning food by Paul Moffat and team",
  "alias": null,
  "pets_ok": false,
  "free_breakfast": true,
  "free_internet": false,
  "free_parking": false
}
```

The paths `name`, `geo.lat` and `public_likes[0]` are all valid paths.

## [](#retrieving)Retrieving

The _lookupIn_ operations query the document for certain path(s); these path(s) are then returned. You have a choice of actually retrieving the document path using the _get_ Sub-Document operation, or simply querying the existence of the path using the _exists_ Sub-Document operation. The latter saves even more bandwidth by not retrieving the contents of the path if it is not needed.

Imports

The examples use the following imports:

```java
import static com.couchbase.client.java.kv.LookupInSpec.exists;
import static com.couchbase.client.java.kv.LookupInSpec.get;
import static com.couchbase.client.java.kv.MutateInOptions.mutateInOptions;
import static com.couchbase.client.java.kv.MutateInSpec.arrayAddUnique;
import static com.couchbase.client.java.kv.MutateInSpec.arrayAppend;
import static com.couchbase.client.java.kv.MutateInSpec.arrayInsert;
import static com.couchbase.client.java.kv.MutateInSpec.arrayPrepend;
import static com.couchbase.client.java.kv.MutateInSpec.decrement;
import static com.couchbase.client.java.kv.MutateInSpec.increment;
import static com.couchbase.client.java.kv.MutateInSpec.insert;
import static com.couchbase.client.java.kv.MutateInSpec.remove;
import static com.couchbase.client.java.kv.MutateInSpec.upsert;

import java.time.Duration;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.stream.Stream;

import com.couchbase.client.core.error.CasMismatchException;
import com.couchbase.client.core.error.DocumentUnretrievableException;
import com.couchbase.client.core.error.DurabilityImpossibleException;
import com.couchbase.client.core.error.subdoc.PathExistsException;
import com.couchbase.client.core.error.subdoc.PathNotFoundException;
import com.couchbase.client.core.msg.kv.DurabilityLevel;
import com.couchbase.client.java.Bucket;
import com.couchbase.client.java.Cluster;
import com.couchbase.client.java.Collection;
import com.couchbase.client.java.Scope;
import com.couchbase.client.java.json.JsonArray;
import com.couchbase.client.java.json.JsonObject;
import com.couchbase.client.java.kv.GetResult;
import com.couchbase.client.java.kv.LookupInReplicaResult;
import com.couchbase.client.java.kv.LookupInResult;
import com.couchbase.client.java.kv.LookupInSpec;
import com.couchbase.client.java.kv.MutateInResult;
import com.couchbase.client.java.kv.MutateInSpec;
import com.couchbase.client.java.kv.MutationResult;
import com.couchbase.client.java.kv.PersistTo;
import com.couchbase.client.java.kv.ReplicateTo;

import reactor.core.publisher.Mono;
```

Retrieve Sub-Document value

```java
LookupInResult result = collection.lookupIn("hotel_1368",
    List.of(get("geo.lat")));

try {
  String str = result.contentAs(0, String.class);
  System.out.println("getFunc: Latitude = " + str);
} catch (PathNotFoundException e) {
  e.printStackTrace();
}
```

> [!NOTE]
> The operation used here is `LookupInSpec.get`, but we import this static method directly for readability.

Check existence of Sub-Document path

```java
LookupInResult result = collection.lookupIn("hotel_1368",
    List.of(exists("address.does_not_exist")));
boolean pathExists = result.exists(0);
System.out.println("Non-existent path exists? " + pathExists);
```

Multiple operations can be combined:

Combine multiple lookup operations

```java
LookupInResult result = collection.lookupIn("hotel_1368",
    List.of(
        get("geo.lat"), // index 0
        exists("address.does_not_exist") // index 1
    )
);

String lat = result.contentAs(0, String.class);
boolean otherExists = result.exists(1);

System.out.println("Latitude: " + lat);
System.out.println("Non-existent path exists? " + otherExists);
```

## [](#choosing-an-api)Choosing an API

The Java SDK provides three APIs for all operations. There’s the simple blocking one you’ve already seen, then this asynchronous variant that returns Java `CompletableFuture`:

```java
CompletableFuture<LookupInResult> future = collection.async().lookupIn("hotel_1368",
    List.of(get("geo.lat")));

try {
  LookupInResult result = future.get();
  System.out.println("future: Latitude: " + result.contentAs(0, Number.class));
} catch (InterruptedException | ExecutionException e) {
  e.printStackTrace();
}
```

And a third that uses reactive programming primitives from [Project Reactor](https://projectreactor.io/):

```java
Mono<LookupInResult> mono = collection.reactive().lookupIn("hotel_1368",
    List.of(get("geo.lat")));

// Just for example, block on the result - this is not best practice
LookupInResult result = mono.block();
```

## [](#mutating)Mutating

Mutation operations modify one or more paths in the document. The simplest of these operations is _upsert_, which, similar to the fulldoc-level _upsert_, will either modify the value of an existing path or create it if it does not exist:

Upserting a new Sub-Document value

```java
collection.mutateIn("hotel_1368", List.of(upsert("email", "hotel96@hotmail.com")));
```

Likewise, the _insert_ operation will only add the new value to the path if it does not exist:

Inserting a Sub-Document value

```java
try {
  collection.mutateIn("hotel_1368", List.of(insert("alt_email", "alt_hotel96@hotmail.com")));
} catch (PathExistsException err) {
  System.out.println("insertFunc: exception caught, path already exists");
}
```

Dictionary values can also be replaced or removed, and you may combine any number of mutation operations within the same general _mutateIn_ API. Here’s an example of one which replaces one path and removes another.

```java
collection.mutateIn("hotel_1368", List.of(remove("tz"), insert("alt_email", "hotel84@hotmail.com")));
```

> [!NOTE]
> `mutateIn` is an _atomic_ operation. If any single operation fails, then the entire document is left unchanged.

## [](#array-append-and-prepend)Array Append and Prepend

The _arrayPrepend_ and _arrayAppend_ operations are true array prepend and append operations. Unlike fulldoc _append_/_prepend_ operations (which simply concatenate bytes to the existing value), _arrayAppend_ and _arrayPrepend_ are JSON-aware:

```java
MutationResult result = collection.mutateIn("hotel_1368",
    List.of(arrayAppend("public_likes", List.of("Mike Rutherford"))));
/*
  public_likes is now:
  ["Georgette Rutherford V", "Ms. Devante Bruen", "Anderson Schmidt", "Mr. Kareem Harvey", "Tessie Shields",
  "Floyd Bradtke III", "Maurice McDermott", "Michel Franecki", "Laila Ernser", "Mike Rutherford"]
*/
```

```java
MutationResult result = collection.mutateIn("hotel_1368",
    List.of(arrayPrepend("public_likes", List.of("John Smith"))));

/*
  public_likes is now:
  ["John Smith", "Georgette Rutherford V", "Ms. Devante Bruen", "Anderson Schmidt", "Mr. Kareem Harvey", "Tessie Shields",
  "Floyd Bradtke III", "Maurice McDermott", "Michel Franecki", "Laila Ernser", "Mike Rutherford"]
*/
```

If your document only needs to contain an array, you do not have to create a top-level object wrapper to contain it. Simply initialize the document with an empty array and then use the empty path for subsequent Sub-Document array operations:

Creating and populating an array document

```java
collection.upsert("my_array", JsonArray.create());

collection.mutateIn("my_array",
    List.of(arrayAppend("", List.of("some element"))));
// the document my_array is now ["some element"]
```

If you wish to create an array if it does not exist and also push elements to it within the same operation you may use the [_createPath_](#subdoc%5Fcreate%5Fpath) option:

```java
MutateInResult result = collection.mutateIn("hotel_14225",
    List.of(arrayAppend("some.array", List.of("hello world")).createPath()));
```

## [](#arrays-as-unique-sets)Arrays as Unique Sets

Limited support also exists for treating arrays like unique sets, using the _arrayAddUnique_ command. This will do a check to determine if the given value exists or not before actually adding the item to the array:

```java
collection.mutateIn("hotel_14226", List.of(arrayAddUnique("unique", 95)));

try {
  collection.mutateIn("hotel_14226", List.of(arrayAddUnique("unique", 95)));
  throw new RuntimeException("should have thrown PathExistsException");
} catch (PathExistsException err) {
  System.out.println("arrayUnique: caught exception, path already exists");
}
```

Note that currently the _arrayAddUnique_ will fail with a _PathMismatchException_ if the array contains JSON _floats_, _objects_, or _arrays_. The _arrayAddUnique_ operation will also fail with _CannotInsertValueException_ if the value to be added is one of those types as well.

Note that the actual position of the new element is undefined, and that the array is not ordered.

## [](#array-insertion)Array Insertion

New elements can also be _inserted_ into an array. While _append_ will place a new item at the _end_ of an array and _prepend_ will place it at the beginning, _insert_ allows an element to be inserted at a specific _position_. The position is indicated by the last path component, which should be an array index. For example, to insert `"cruel"` as the second element in the array `["Hello", "world"]`, the code would look like:

```java
MutateInResult result = collection.mutateIn("hotel_1501",
    List.of(arrayInsert("foo[1]", List.of("cruel"))));
```

Note that the array must already exist and that the index must be valid (i.e. it must not point to an element which is out of bounds).

## [](#counters-and-numeric-fields)Counters and Numeric Fields

Counter operations allow the manipulation of a _numeric_ value inside a document. These operations are logically similar to the _increment_ and _decrement_ full-document operations:

```java
MutateInResult result = collection.mutateIn("hotel_1368", List.of(increment("logins", 1)));

// Counter operations return the updated count
Long count = result.contentAs(0, Long.class);
```

The _increment_ and _decrement_ operations perform simple arithmetic against a numeric value. The updated value is returned.

```java

MutateInResult result = collection.mutateIn("hotel_1368", List.of(decrement("logouts", 150)));
// Counter operations return the updated count
Long count = result.contentAs(0, Long.class);
```

The existing value for counter operations must be within range of a 64 bit signed integer. If the value does not exist, the operation will create it (and its parents, if _createPath_ is enabled).

Note that there are several differences as compared to the full-document counter operations:

* Sub-Document counters have a range of -9223372036854775807 to 9223372036854775807, whereas full-document counters have a range of 0 to 18446744073709551615
* Sub-Document counter operations protect against overflow and underflow, returning an error if the operation would exceed the range. Full-document counters will use normal C semantics for overflow (in which the overflow value is carried over above 0), and will silently fail on underflow, setting the value to 0 instead.
* Sub-Document counter operations can operate on any numeric value within a document, while [full-document counter operations](kv-operations.md#atomic-counters) require a specially formatted counter document with only the counter value.

## [](#executing-multiple-operations)Executing Multiple Operations

Multiple Sub-Document operations can be executed at once on the same document, allowing you to retrieve or modify several Sub-Documents at once. When multiple operations are submitted within the context of a single _lookupIn_ or _mutateIn_ command, the server will execute all the operations with the same version of the document.

> [!NOTE]
> Unlike _batched operations_ which is simply a way of sending multiple individual operations efficiently on the network, multiple Sub-Document operations are formed into a single command packet, which is then executed atomically on the server. You can submit up to 16 operations at a time.

When submitting multiple _mutation_ operations within a single _mutateIn_ command, those operations are considered to be part of a single transaction: if any of the mutation operations fail, the server will logically roll-back any other mutation operations performed within the _mutateIn_, even if those commands would have been successful had another command not failed.

When submitting multiple _retrieval_ operations within a single _lookupIn_ command, the status of each command does not affect any other command. This means that it is possible for some retrieval operations to succeed and others to fail. While their statuses are independent of each other, you should note that operations submitted within a single _lookupIn_ are all executed against the same _version_ of the document.

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

By default the automatic creation of parents is disabled, as a simple typo in application code can result in a rather confusing document structure. Sometimes it is necessary to have the server create the hierarchy however. In this case, the _createPath_ option may be used.

```java
MutateInResult result = collection.mutateIn("hotel_1368",
    List.of(
        upsert("level_0.level_1.foo.bar.phone", JsonObject.create().put("num", "311-555-0101").put("ext", 16))
            .createPath()));
```

## [](#reading-sub-documents-from-replicas)Reading Sub-Documents From Replicas

Couchbase Server 7.6 and later support Sub-Doc lookup from replicas.

The `collection.lookupInAnyReplica()` method returns the first response — from active or replica:

```java
try {
  LookupInResult result = collection.lookupInAnyReplica(
      "hotel_1368",
      List.of(LookupInSpec.get("geo.lat"))
  );

  String str = result.contentAs(0, String.class);
  System.out.println("getFunc: Latitude = " + str);

} catch (PathNotFoundException e) {
  System.out.println("The version of the document" +
      " on the server node that responded quickest" +
      " did not have the requested field.");

} catch (DocumentUnretrievableException e) {
  System.out.println("Document was not present" +
      " on any server node.");
}
```

The `collection.lookupInAllReplicas()` fetches all available replicas (and the active copy), and returns all responses.

```java
Stream<LookupInReplicaResult> results = collection.lookupInAllReplicas(
    "hotel_1368",
    List.of(LookupInSpec.get("geo.lat"))
);

results.forEach(it -> {
  try {
    String str = it.contentAs(0, String.class);
    System.out.println("getFunc: Latitude = " + str);

  } catch (PathNotFoundException e) {
    System.out.println("The version of the document" +
        " on one of the server nodes" +
        " did not have the requested field.");
  }
});
```

You may want to use `lookupInAllReplicas` to build a consensus, but it’s more likely that you’ll make use of `lookupInAnyReplica` as a fallback to a `lookupIn`, when the active node times out.

## [](#concurrent-modifications)Concurrent Modifications

Concurrent Sub-Document operations on different parts of a document will not conflict. For example the following two blocks can execute concurrently without any risk of conflict:

```java
Thread thread1 = new Thread() {
  public void run() {
    collection.mutateIn("hotel_1501",
        List.of(arrayAppend("foo", List.of(99))));
  }
};

Thread thread2 = new Thread() {
  public void run() {
    collection.mutateIn("hotel_1501",
        List.of(arrayAppend("foo", List.of(101))));
  }
};
thread1.start();
thread2.start();
```

Even when modifying the _same_ part of the document, operations will not necessarily conflict. For example, two concurrent _arrayAppend_ operations to the same array will both succeed, never overwriting the other.

So in some cases the application will not need to supply a [CAS](concurrent-document-mutations.md) value to protect against concurrent modifications.

If CAS is required then it can be provided like this:

```java
GetResult doc = collection.get("hotel_1368");
MutationResult result = collection.mutateIn("hotel_1368", List.of(decrement("logouts", 150)),
    mutateInOptions().cas(doc.cas()));
```

## [](#durability)Durability

Couchbase’s [traditional 'client verified' durability](../concept-docs/durability-replication-failure-considerations.md#older-server-versions), using `PersistTo` and `ReplicateTo`, is still available, particularly for talking to Couchbase Server 7.0 and earlier:

```java
MutationResult result = collection.mutateIn("hotel_1368",
    List.of(MutateInSpec.upsert("foo", "bar")),
    mutateInOptions().durability(PersistTo.ACTIVE, ReplicateTo.ONE));
```

In Couchbase Server 7.0 and up, this is built upon with [Durable Writes](../concept-docs/durability-replication-failure-considerations.md#durable-writes), which uses the concept of majority to indicate the number of configured Data Service nodes to which commitment is required:

```java
MutationResult result = collection.mutateIn("hotel_1368",
    List.of(MutateInSpec.upsert("foo", "bar")),
    mutateInOptions().durability(DurabilityLevel.MAJORITY));
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
> Currently, paths cannot exceed 1024 characters, and cannot be more than 32 levels deep. DJSON documents with more than 32 nested layers cannot be parsed, atttempting to do so will result in a\`DocumentTooDeepException\` exception.

## [](#extended-attributes)Extended Attributes

Extended Attributes (also known as XATTRs), built upon the Sub-Document API, allow developers to define application-specific metadata that will only be visible to those applications that request it or attempt to modify it. This might be, for example, meta-data specific to a programming framework that should be hidden by default from other frameworks or libraries, or possibly from other versions of the same framework. They are not intended for use in general applications, and data stored there cannot be accessed easily by some Couchbase services, such as Search.

Full Document Example

```java
JsonObject docContent = JsonObject.create().put("body", "value");
collection.mutateIn("hotel_14006",
    List.of(MutateInSpec.upsert("foo", "bar").xattr().createPath(), MutateInSpec.replace("", docContent)));
```

The full document can be replaced using the Sub-Doc API. In the above snippet, the full document is replaced, whilst xattrs are updated with the same command. The empty `""` in `MutateInSpec.replace("", docContent)` represents the full document.