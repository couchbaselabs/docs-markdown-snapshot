---
title: Delete Documents
description: How to delete documents with a command line tool or an SDK.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/guides/pages/deleting-data.adoc
  xref: xref:cloud:guides:deleting-data.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/guides/deleting-data.html)

# Delete Documents

> How to delete documents with a command line tool or an SDK. 

## [](#introduction)Introduction

In situations where data is no longer needed, Couchbase Capella provides a remove operation to delete a document from the database permanently.

Read the following for further information about the clients available:

* [Couchbase Shell (cbsh)](https://couchbase.sh/docs/)
* [SDK Clients](../../home/sdk.md)

> [!WARNING]
> Please note that the examples in this guide will alter the data in your sample database. To restore your sample data, remove and reinstall the travel sample data. Refer to [Import Data with the Capella UI](../clusters/data-service/import-data-documents.md) for details.

## [](#deleting-a-document)Deleting a Document

To delete a document, perform a remove operation.

* cbsh
* .NET
* Java
* Node.js
* Python

1. If you have not already done so, use `cb-env` to set the bucket, scope, and collection where the document is stored.
2. Use the `doc remove` command to delete the document by ID.

---

The example below deletes document `hotel-123` from the database.

```sh
cb-env bucket travel-sample
cb-env scope inventory
cb-env collection hotel

doc remove hotel-123
```

Result

```console
╭───┬───────────┬─────────┬────────┬──────────┬─────────╮
│ # │ processed │ success │ failed │ failures │ cluster │
├───┼───────────┼─────────┼────────┼──────────┼─────────┤
│ 0 │         1 │       1 │      0 │          │ capella │
╰───┴───────────┴─────────┴────────┴──────────┴─────────╯
```

For more information, see [Removing](https://couchbase.sh/docs/#%5Fremoving) in the Couchbase Shell documentation.

Use the `RemoveAsync()` method to delete a document from the database.

---

The example below deletes document `hotel-123` from the database.

```csharp
await hotelCollection.RemoveAsync("hotel-123");
```

> [!NOTE]
> If the document does not exist, the SDK will return a `DocumentNotFoundException` error.

Click the  View button to see this code in context.

For more information, see [CollectionExtensions](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.KeyValue.CollectionExtensions.html).

Use the `remove()` method to delete a document from the database.

---

The example below deletes document `hotel-123` from the database.

```java
MutationResult removeResult = hotelCollection.remove("hotel-123");
System.out.println("CAS:" + removeResult.cas());
```

> [!NOTE]
> If the document does not exist, the SDK will return a `DocumentNotFoundException` error.

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Collection.html).

Use the `remove()` function to delete a document from the database.

---

The example below deletes document `hotel-123` from the database.

```nodejs
Unresolved include directive in modules/guides/pages/deleting-data.adoc - include::nodejs-sdk:hello-world:example$kv-hello-world-scoped.js[]
```

> [!NOTE]
> If the document does not exist, the SDK will return a `DocumentNotFoundError` error.

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Collection.html).

Use the `remove()` function to delete a document from the database.

---

The example below deletes document `hotel-123` from the database.

```python
remove_result = hotel_collection.remove("hotel-123")
print("CAS:", remove_result.cas)
```

> [!NOTE]
> If the document does not exist, the SDK will return a `DocumentNotFoundException` error.

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#collection-object).

## [](#deleting-a-sub-document)Deleting a Sub-Document

To delete a specific field within a document you can perform a Sub-Document remove operation.

* cbsh
* .NET
* Java
* Node.js
* Python

1. If you have not already done so, use `cb-env` to set the bucket, scope, and collection where the document is stored.
2. Use the `doc get` command to retrieve a document by ID.
3. Pipe the document through the `reject` filter to remove the field containing the Sub-Document.
4. Pipe the output, including the `id` and `content` fields, through the `doc replace` command to update the document.

---

The example below deletes the `url` field from document `hotel-123`.

```sh
cb-env bucket travel-sample
cb-env scope inventory
cb-env collection hotel

doc get hotel-123 | reject content.url | doc replace
```

Result

```console
╭───┬───────────┬─────────┬────────┬──────────┬─────────╮
│ # │ processed │ success │ failed │ failures │ cluster │
├───┼───────────┼─────────┼────────┼──────────┼─────────┤
│ 0 │         1 │       1 │      0 │          │ capella │
╰───┴───────────┴─────────┴────────┴──────────┴─────────╯
```

> [!NOTE]
> If the field containing the Sub-Document cannot be found, the `reject` command returns a `Cannot find column` error.

For more information, see [reject for filters](https://www.nushell.sh/commands/docs/reject.html) in the Nushell documentation.

1. Call the `MutateInAsync()` method, which takes a document ID and an IEnumerable containing `MutateInSpec` objects.
2. Use a `MutateInSpec` object to specify the sub-operation to be performed within the lookup.

A `MutateInResult` object is returned containing the result and metadata relevant to the Sub-Document remove operation.

---

The example below deletes the `url` field from document `hotel-123`.

```csharp
var mutateInResult = await hotelCollection.MutateInAsync("hotel-123",
	specs => specs.Remove("url")
);
Console.WriteLine($"Cas: {mutateInResult.Cas}");
```

> [!NOTE]
> If the path does not exist, the SDK will return a `PathNotFoundException` error.

Click the  View button to see this code in context.

For more information, see [CollectionExtensions](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.KeyValue.CollectionExtensions.html).

1. Call the `mutateIn()` method, which takes a document ID and an array of `MutateInSpec` objects.
2. Use a `MutateInSpec` object to specify the sub-operation to be performed within the lookup.

A `MutateInResult` object is returned, containing the result and metadata relevant to the Sub-Document remove operation.

---

The example below deletes the `url` field from document `hotel-123`.

```java
List<MutateInSpec> specs = Arrays.asList(MutateInSpec.remove("url"));

MutateInResult mutateInResult = hotelCollection.mutateIn("hotel-123", specs);
System.out.println("CAS:" + mutateInResult.cas());
```

> [!NOTE]
> If the path does not exist, the SDK will return a `PathNotFoundException` error.

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Collection.html).

1. Call the `mutateIn()` method, which takes a document ID and an array of `MutateInSpec` objects.
2. Use a `MutateInSpec` object to specify the sub-operation to be performed within the lookup.

A `MutateInResult` object is returned, containing the result and metadata relevant to the Sub-Document remove operation.

---

The example below deletes the `url` field from document `hotel-123`.

```nodejs
Unresolved include directive in modules/guides/pages/deleting-data.adoc - include::nodejs-sdk:hello-world:example$kv-hello-world-scoped.js[]
```

> [!NOTE]
> If the path does not exist, the SDK will return a `PathNotFoundError` error.

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Collection.html).

1. Call the `lookup_in()` function, which takes a document ID and a list of `MutateInSpec` objects.
2. Use a `MutateInSpec` object to specify the sub-operation to be performed within the lookup.

A `MutateInResult` object is returned, containing the result and metadata relevant to the Sub-Document remove operation.

---

The example below deletes the `url` field from document `hotel-123`.

```python
mutate_in_result = hotel_collection.mutate_in(
    "hotel-123", [subdocument.remove("url")]
)
print("CAS:", mutate_in_result.cas)
```

> [!NOTE]
> If the path does not exist, the SDK will return a `PathNotFoundException` error.

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#collection-object).

## [](#related-links)Related Links

Key-Value Operations with SDKs:

* [C](../../c-sdk/current/howtos/kv-operations.md)| [C++](../../cxx-sdk/current/howtos/kv-operations.md)| [.NET](../../dotnet-sdk/current/howtos/kv-operations.md)| [Go](../../go-sdk/current/howtos/kv-operations.md)| [Java](../../java-sdk/current/howtos/kv-operations.md)| [Kotlin](../../kotlin-sdk/current/howtos/kv-operations.md)| [Node.js](../../nodejs-sdk/current/howtos/kv-operations.md)| [PHP](../../php-sdk/current/howtos/kv-operations.md)| [Python](../../python-sdk/current/howtos/kv-operations.md)| [Ruby](../../ruby-sdk/current/howtos/kv-operations.md)| [Rust](../../rust-sdk/current/howtos/kv-operations.md)| [Scala](../../scala-sdk/current/howtos/kv-operations.md)

Sub-Document operations with SDKs:

* [C](../../c-sdk/current/howtos/subdocument-operations.md)| [C++](../../cxx-sdk/current/howtos/subdocument-operations.md)| [.NET](../../dotnet-sdk/current/howtos/subdocument-operations.md)| [Go](../../go-sdk/current/howtos/subdocument-operations.md)| [Java](../../java-sdk/current/howtos/subdocument-operations.md)| Kotlin | [Node.js](../../nodejs-sdk/current/howtos/subdocument-operations.md)| [PHP](../../php-sdk/current/howtos/subdocument-operations.md)| [Python](../../python-sdk/current/howtos/subdocument-operations.md)| [Ruby](../../ruby-sdk/current/howtos/subdocument-operations.md)| [Rust](../../rust-sdk/current/howtos/subdocument-operations.md)| [Scala](../../scala-sdk/current/howtos/subdocument-operations.md)