---
title: Read Documents
description: How to read documents with a command line tool or an SDK.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/guides/pages/reading-data.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:cloud:guides:reading-data.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/guides/reading-data.html)

# Read Documents

> How to read documents with a command line tool or an SDK. 

## [](#introduction)Introduction

Retrieving documents by ID is the fastest and simplest way to read [data](../../server/current/learn/data/data.md) in Couchbase Capella. The [Key-Value (KV) or Data Service](../clusters/data-service/data-service.md) allows you to retrieve a full document when you need to fetch all of the data stored. However, in instances where this can be costly and unnecessary, Couchbase also provides access to specific paths within a document.

Read the following for further information about the clients available:

* [Couchbase Shell (cbsh)](https://couchbase.sh/docs/)
* [SDK Clients](../../home/sdk.md)

> [!WARNING]
> Please note that the examples in this guide will alter the data in your sample database. To restore your sample data, remove and reinstall the travel sample data. Refer to [Import Data with the Capella UI](../clusters/data-service/import-data-documents.md) for details.

## [](#reading-a-document)Reading a Document

To read a single document, perform a get operation.

* cbsh
* .NET
* Java
* Node.js
* Python

1. If you have not already done so, use `cb-env` to set the bucket, scope, and collection where the document is stored.
2. Use the `doc get` command to retrieve a document by ID and output its data.

An object is returned, which includes the `id`, `content`, and other metadata. The document itself is wrapped in the `content` field.

---

The example below retrieves document `hotel-123` from the `hotel` keyspace in the `inventory` scope.

```sh
cb-env bucket travel-sample
cb-env scope inventory
cb-env collection hotel

doc get hotel-123
```

Result

```console
╭───┬───────────┬────────────────────┬─────────────────────┬───────┬─────────╮
│ # │    id     │      content       │         cas         │ error │ cluster │
├───┼───────────┼────────────────────┼─────────────────────┼───────┼─────────┤
│ 0 │ hotel-123 │ {record 11 fields} │ 1717190781443309568 │       │ capella │
╰───┴───────────┴────────────────────┴─────────────────────┴───────┴─────────╯
```

> [!NOTE]
> If the document cannot be found, Couchbase Shell returns a `Key not found` error.

For more information, see [Reading](https://couchbase.sh/docs/#%5Freading) in the Couchbase Shell documentation.

Use the `GetAsync()` method to retrieve a document by ID.

A `GetResult` object is returned, which includes the `content`, `cas` value, and other valuable metadata.

---

The example below retrieves document `hotel-123` from the `hotel` keyspace in the `inventory` scope.

```csharp
var getResult = await hotelCollection.GetAsync("hotel-123");

// Print some result metadata to the console.
Console.WriteLine($"CAS: {getResult.Cas}");
Console.WriteLine($"Data: {getResult.ContentAs<JObject>()}");
```

> [!NOTE]
> If the document does not exist, the SDK returns a `DocumentNotFoundException` error.

Click the  View button to see this code in context.

For more information, see [CollectionExtensions](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.KeyValue.CollectionExtensions.html).

Use the `get()` method to retrieve a document by ID.

A `GetResult` object is returned, which includes the `content`, `cas` value, and other valuable metadata.

---

The example below retrieves document `hotel-123` from the `hotel` keyspace in the `inventory` scope.

```java
GetResult getResult = hotelCollection.get("hotel-123");

// Print the result's CAS metadata to the console.
System.out.println("CAS:" + getResult.cas());
```

> [!NOTE]
> If the document does not exist, the SDK returns a `DocumentNotFoundException` error.

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Collection.html).

Use the `get()` function to retrieve a document by ID.

A `GetResult` promise is returned, which includes the `content`, `cas` value, and other valuable metadata.

---

The example below retrieves document `hotel-123` from the `hotel` keyspace in the `inventory` scope.

```nodejs
const getResult = await hotelCollection.get('hotel-123')

// Print some result metadata to the console.
console.log('CAS:', getResult.cas)
console.log('Data:', JSON.stringify(getResult.content, null, '  '))
```

> [!NOTE]
> If the document does not exist, the SDK returns a `DocumentNotFoundError` error.

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Collection.html).

Use the `get()` function to retrieve a document by ID.

A `GetResult` object is returned, which includes the `content`, `cas` value, and other valuable metadata.

---

The example below retrieves document `hotel-123` from the `hotel` keyspace in the `inventory` scope.

```python
get_result = hotel_collection.get("hotel-123")

# Print some result metadata to the console.
print("CAS:", get_result.cas)
print("Data: {}".format(get_result.content_as[dict]))
```

> [!NOTE]
> If the document does not exist, the SDK returns a `DocumentNotFoundException` error.

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#collection-object).

### [](#reading-with-options)Reading with Options

To specify further parameters, add options to the get operation.

* cbsh
* .NET
* Java
* Node.js
* Python

1. If you have not already done so, use `cb-env` to set the bucket, scope, and collection where the document is stored.
2. Use the `doc get` command to retrieve a document by ID, and pass options as required.

---

The example below pipes the `hotel-123` document and its metadata through the `to json` filter to transform the output to JSON.

```sh
cb-env bucket travel-sample
cb-env scope inventory
cb-env collection hotel

doc get hotel-123 | to json
```

Result

```json
[
  {
    "id": "hotel-123",
    "content":
    {
      "address": "Capstone Road, ME7 3JE",
      "city": "Medway",
      "country": "United Kingdom",
      "description": "40 bed summer hostel about 3 miles from Gillingham.",
      "geo":
      {
        "accuracy": "RANGE_INTERPOLATED",
        "lat": 51.35785,
        "lon": 0.55818
      },
      "id": 123,
      "name": "Medway Youth Hostel",
      "reviews":
      [
        {
          "author": "Ozella Sipes",
          "content": "This was our 2nd trip here and we enjoyed it more than last year.",
          "date": "2021-11-17T17:35:05.351Z"
        }
      ],
      "state": null,
      "url": "http://www.yha.org.uk",
      "vacancy": true
    },
    "cas": 1717190781443309568,
    "error": "",
    "cluster": "capella"
  }
]
```

For more information, see [Reading](https://couchbase.sh/docs/#%5Freading) in the Couchbase Shell documentation.

Pass any required options to the `GetAsync()` method when retrieving a document.

A `GetResult` object is returned, which may include extra metadata, depending on the options passed.

---

The example below retrieves a document `hotel-123` with additional expiry metadata.

```csharp
var getResult = await hotelCollection.GetAsync("hotel-456", options =>
{
	options.Expiry();
});

// Print some result metadata to the console.
Console.WriteLine($"CAS: {getResult.Cas}");
Console.WriteLine($"Data: {getResult.ContentAs<JObject>()}");
Console.WriteLine($"Expiry: {getResult.ExpiryTime}");
```

Click the  View button to see this code in context.

For more information, see [CollectionExtensions](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.KeyValue.CollectionExtensions.html).

Pass any required options to the `get()` method when retrieving a document.

A `GetResult` object is returned, which may include extra metadata, depending on the options passed.

---

The example below retrieves a document `hotel-123` with additional expiry metadata.

```java
GetResult getResult = hotelCollection.get("hotel-123", 
    GetOptions.getOptions().withExpiry(true)
);

// Print the result's CAS metadata to the console.
System.out.println("CAS:" + getResult.cas());
System.out.println("Data:" + getResult.contentAsObject());
System.out.println("Expiry:" + getResult.expiryTime());
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Collection.html).

Pass any required options to the `get()` method when retrieving a document.

A `GetResult` object is returned, which may include extra metadata, depending on the options passed.

---

The example below retrieves a document `hotel-123` with additional expiry metadata.

```nodejs
const getResult = await hotelCollection.get('hotel-456', {
  withExpiry: true,
})

// Print some result metadata to the console.
console.log('CAS:', getResult.cas)
console.log('Data:', JSON.stringify(getResult.content, null, '  '))
console.log('Expiry time:', getResult.expiryTime)
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Collection.html).

Pass any required options to the `get()` method when retrieving a document.

A `GetResult` object is returned, which may include extra metadata, depending on the options passed.

---

The example below retrieves a document `hotel-123` with additional expiry metadata.

```python
get_result = hotel_collection.get(
    "hotel-456", GetOptions(with_expiry=True)
)

# Print some result metadata to the console.
print("CAS:", get_result.cas)
print("Data: {}".format(get_result.content_as[dict]))
print("Expiry time: {}".format(get_result.expiryTime))
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#collection-object).

## [](#reading-a-sub-document)Reading a Sub-Document

JSON documents can contain a lot of nested data — which might not necessarily need to be accessed all at once. For example, the document `airport_1254` contains a Sub-Document called `geo`.

airport\_1254

```json
{
  "id": 1254,
//  ...
  "geo": {
    "lat": 50.962097,
    "lon": 1.954764,
    "alt": 12
  }
}
```

Reading full documents to access a field or two is not ideal and could cause performance issues in your application. Instead, a better practice would be to access specific paths, or Sub-Documents, to perform more efficient read operations. To fetch a specific field inside a document, you can perform a Sub-Document get operation.

* cbsh
* .NET
* Java
* Node.js
* Python

1. If you have not already done so, use `cb-env` to set the bucket, scope, and collection where the document is stored.
2. Use the `doc get` command to retrieve a document by ID.
3. Pipe the document through the `get` filter and specify the path to the field containing the Sub-Document.

---

The example below fetches the `geo` data from the `hotel-123` document.

```sh
cb-env bucket travel-sample
cb-env scope inventory
cb-env collection hotel

doc get hotel-123 | get content.geo
```

Result

```console
╭───┬────────────────────┬─────────┬────────╮
│ # │      accuracy      │   lat   │  lon   │
├───┼────────────────────┼─────────┼────────┤
│ 0 │ RANGE_INTERPOLATED │ 51.3578 │ 0.5582 │
╰───┴────────────────────┴─────────┴────────╯
```

> [!NOTE]
> If the field containing the Sub-Document cannot be found, the `get` command returns a `Cannot find column` error.

For more information, see [get for filters](https://www.nushell.sh/commands/docs/get.html) in the Nushell documentation.

1. Call the `LookupInAsync()` method, which takes a document ID and an IEnumerable containing `LookUpInSpec` objects.
2. Use the `LookUpInSpec` object to specify the sub-operation to be performed within the lookup.

A `LookupInResult` object is returned, containing the result and metadata relevant to the Sub-Document get operation.

---

The example below fetches the `geo` data from the `hotel-123` document.

```csharp
var lookupInResult = await hotelCollection.LookupInAsync("hotel-123",
		specs => specs.Get("geo")
);

Console.WriteLine($"CAS: {lookupInResult.Cas}");
Console.WriteLine($"Geo: {lookupInResult.ContentAs<JObject>(0)}");
```

Click the  View button to see this code in context.

For more information, see [CollectionExtensions](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.KeyValue.CollectionExtensions.html).

1. Call the `lookupIn()` method, which takes a document ID and an array of `LookUpInSpec` objects.
2. Use the `LookUpInSpec` object to specify the sub-operation to be performed within the lookup.

A `LookupInResult` object is returned, containing the result and metadata relevant to the Sub-Document get operation.

---

The example below fetches the `geo` data from the `hotel-123` document.

```java
List<LookupInSpec> specs = Arrays.asList(LookupInSpec.get("geo"));

LookupInResult lookupInResult = hotelCollection.lookupIn("hotel-123", specs);
System.out.println("CAS:" + lookupInResult.cas());
System.out.println("Geo:" + lookupInResult.contentAsObject(0));
```

> [!NOTE]
> If the document path cannot be found, the SDK returns a `PathNotFoundException` error.

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Collection.html).

1. Call the `lookupIn()` function, which takes a document ID and an array of `LookUpInSpec` objects.
2. Use the `LookUpInSpec` object to specify the sub-operation to be performed within the lookup.

A `LookupInResult` promise is returned containing the result and metadata relevant to the Sub-Document get operation.

---

The example below fetches the `geo` data from the `hotel-123` document.

```nodejs
const lookupInResult = await hotelCollection.lookupIn('hotel-123', [
  couchbase.LookupInSpec.get('geo'),
])
console.log('CAS:', lookupInResult.cas)
console.log('Geo:', lookupInResult.content[0].value)
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Collection.html).

1. Call the `lookup_in()` function, which takes a document ID and a list of `LookUpInSpec` objects.
2. Use the `LookUpInSpec` object to represent the sub-operation to be performed within the lookup.

A `LookupInResult` object is returned containing the result and metadata relevant to the Sub-Document get operation.

---

The example below fetches the `geo` data from the `hotel-123` document.

```python
lookup_in_result = hotel_collection.lookup_in(
    "hotel-123", [subdocument.get("geo")]
)
print("CAS:", lookup_in_result.cas)
print("Data:", lookup_in_result.content_as[dict](0))
```

> [!NOTE]
> If the document path cannot be found, the SDK returns a `PathNotFoundException` error.

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#collection-object).

## [](#related-links)Related Links

Key-Value Operations with SDKs:

* [C](../../c-sdk/current/howtos/kv-operations.md)| [C++](../../cxx-sdk/current/howtos/kv-operations.md)| [.NET](../../dotnet-sdk/current/howtos/kv-operations.md)| [Go](../../go-sdk/current/howtos/kv-operations.md)| [Java](../../java-sdk/current/howtos/kv-operations.md)| [Kotlin](../../kotlin-sdk/current/howtos/kv-operations.md)| [Node.js](../../nodejs-sdk/current/howtos/kv-operations.md)| [PHP](../../php-sdk/current/howtos/kv-operations.md)| [Python](../../python-sdk/current/howtos/kv-operations.md)| [Ruby](../../ruby-sdk/current/howtos/kv-operations.md)| [Rust](../../rust-sdk/current/howtos/kv-operations.md)| [Scala](../../scala-sdk/current/howtos/kv-operations.md)

Sub-Document operations with SDKs:

* [C](../../c-sdk/current/howtos/subdocument-operations.md)| [C++](../../cxx-sdk/current/howtos/subdocument-operations.md)| [.NET](../../dotnet-sdk/current/howtos/subdocument-operations.md)| [Go](../../go-sdk/current/howtos/subdocument-operations.md)| [Java](../../java-sdk/current/howtos/subdocument-operations.md)| [Node.js](../../nodejs-sdk/current/howtos/subdocument-operations.md)| Kotlin | [PHP](../../php-sdk/current/howtos/subdocument-operations.md)| [Python](../../python-sdk/current/howtos/subdocument-operations.md)| [Ruby](../../ruby-sdk/current/howtos/subdocument-operations.md)| [Rust](../../rust-sdk/current/howtos/subdocument-operations.md)| [Scala](../../scala-sdk/current/howtos/subdocument-operations.md)