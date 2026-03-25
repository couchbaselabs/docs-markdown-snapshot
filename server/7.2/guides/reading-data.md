---
title: Reading Data
description: How to read documents in Couchbase.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/guides/pages/reading-data.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:7.2@server:guides:reading-data.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/guides/reading-data.html)

# Reading Data

> How to read documents in Couchbase.  
> This guide is for Couchbase Server.

## [](#introduction)Introduction

Retrieving documents by ID is the fastest and simplest way to read [data](../learn/data/data.md) in Couchbase. The [Key-Value (KV) or Data Service](../learn/services-and-indexes/services/data-service.md) allows you to retrieve a full document when you need to fetch all of the data stored. However, in instances where this can be costly and unnecessary, Couchbase also provides access to specific paths within a document.

Read the following for further information about the clients available:

* [Command Line Clients](../../../c-sdk/current/hello-world/cbc.md)
* [SDK Clients](../../../home/sdk.md)

> [!WARNING]
> Please note that the examples in this guide will alter the data in your sample database. To restore your sample data, remove and reinstall the travel sample data. Refer to [Sample Buckets](../manage/manage-settings/install-sample-buckets.md) for details.

## [](#reading-a-document)Reading a Document

To read a single document in Couchbase, perform a get operation.

* cbc
* .NET
* Java
* Node.js
* Python

Use the `cbc cat` command to retrieve a document by ID and output its data.

---

The example below retrieves document `hotel-123` from the `hotel` keyspace in the `inventory` scope.

```shell
cbc cat hotel-123 -u Administrator -P password -U couchbase://localhost/travel-sample \
	--scope='inventory' \
	--collection='hotel'
```

Result

```console
hotel-123            CAS=0x16ba896b78930000, Flags=0x0, Size=567, Datatype=0x01(JSON)

{
  "id": 123,
  "name": "Medway Youth Hostel",
  "address": "Capstone Road, ME7 3JE",
  "url": "http://www.yha.org.uk",
  "geo": {
    "lat": 51.35785,
    "lon": 0.55818,
    "accuracy": "RANGE_INTERPOLATED"
  },
  "country": "United Kingdom",
  "city": "Medway",
  "state": null,
  "reviews": [
    {
      "content": "This was our 2nd trip here and we enjoyed it more than last year.",
      "author": "Ozella Sipes",
      "date": "2021-11-17T17:35:05.351Z"
    }
  ],
  "vacancy": true,
  "description": "40 bed summer hostel about 3 miles from Gillingham."
}
```

The output has been prettified for readability.

> [!NOTE]
> If the document cannot be found, `cbc` will return a `LCB_ERR_DOCUMENT_NOT_FOUND` error.

For further details, refer to [cbc(1)](https://docs.couchbase.com/sdk-api/couchbase-c-client/md%5Fdoc%5Fcbc.html).

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
> If the document does not exist, the SDK will return a `DocumentNotFoundException` error.

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
> If the document does not exist, the SDK will return a `DocumentNotFoundException` error.

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
> If the document does not exist, the SDK will return a `DocumentNotFoundError` error.

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
> If the document does not exist, the SDK will return a `DocumentNotFoundException` error.

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#collection-object).

### [](#reading-with-options)Reading with Options

To specify further parameters, such as expiry, add options to the get operation.

* cbc
* .NET
* Java
* Node.js
* Python

Use the `cbc cat` command to retrieve a document by ID and pass options as required.

---

The example below uses an `--expiry` option for the `cat` command which adds an expiry of 60 seconds to the `hotel-123` document.

```shell
cbc cat hotel-123 -u Administrator -P password -U couchbase://localhost/travel-sample \
	--scope='inventory' \
	--collection='hotel' \
	--expiry=60
```

Result

```console
hotel-123            CAS=0x16bcec98e00c0000, Flags=0x0, Size=567, Datatype=0x01(JSON)

{
  "id": 123,
  "name": "Medway Youth Hostel",
  "address": "Capstone Road, ME7 3JE",
  "url": "http://www.yha.org.uk",
  "geo": {
    "lat": 51.35785,
    "lon": 0.55818,
    "accuracy": "RANGE_INTERPOLATED"
  },
  "country": "United Kingdom",
  "city": "Medway",
  "state": null,
  "reviews": [
    {
      "content": "This was our 2nd trip here and we enjoyed it more than last year.",
      "author": "Ozella Sipes",
      "date": "2021-11-17T17:35:05.351Z"
    }
  ],
  "vacancy": true,
  "description": "40 bed summer hostel about 3 miles from Gillingham."
}
```

The output has been prettified for readability.

For further details, refer to [cbc(1)](https://docs.couchbase.com/sdk-api/couchbase-c-client/md%5Fdoc%5Fcbc.html).

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

JSON documents can contain a lot of nested data — which might not necessarily need to be accessed all at once. Reading full documents to access a field or two is not ideal and could cause performance issues in your application. Instead, a better practice would be to access specific paths, or Sub-Documents, to perform more efficient read operations.

To fetch a specific field inside a document, you can perform a Sub-Document get operation.

* cbc-subdoc
* .NET
* Java
* Node.js
* Python

1. Connect to the `cbc-subdoc` interactive shell.
2. Use the `get` command to access specific fields in a JSON document with the `--path` argument.

---

The example below fetches the `geo` data from the `airport_1254` document.

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

```console
cbc-subdoc -u Administrator -P password -U couchbase://localhost/travel-sample
subdoc> get airport_1254 --path geo
```

Result

```console
airport_1254         CAS=0x16b815068df80000
0. Size=43, RC=LCB_SUCCESS (0)
{"lat":50.962097,"lon":1.954764,"alt":12.0}
```

> [!NOTE]
> If the path cannot be found, `cbc-subdoc` will return a `LCB_ERR_SUBDOC_PATH_NOT_FOUND` error.

For further details, refer to [cbc-subdoc(1)](https://docs.couchbase.com/sdk-api/couchbase-c-client/md%5Fdoc%5Fcbc%5Fsubdoc.html).

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
> If the document path cannot be found, the SDK will return a `PathNotFoundException` error.

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
> If the document path cannot be found, the SDK will return a `PathNotFoundException` error.

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#collection-object).

## [](#related-links)Related Links

Key-Value Operations with SDKs:

* [C](../../../c-sdk/current/howtos/kv-operations.md)| [C++](../../../cxx-sdk/current/howtos/kv-operations.md)| [.NET](../../../dotnet-sdk/current/howtos/kv-operations.md)| [Go](../../../go-sdk/current/howtos/kv-operations.md)| [Java](../../../java-sdk/current/howtos/kv-operations.md)| [Kotlin](../../../kotlin-sdk/current/howtos/kv-operations.md)| [Node.js](../../../nodejs-sdk/current/howtos/kv-operations.md)| [PHP](../../../php-sdk/current/howtos/kv-operations.md)| [Python](../../../python-sdk/current/howtos/kv-operations.md)| [Ruby](../../../ruby-sdk/current/howtos/kv-operations.md)| [Scala](../../../scala-sdk/current/howtos/kv-operations.md)

Sub-Document operations with SDKs:

* [C](../../../c-sdk/current/howtos/subdocument-operations.md)| [C++](../../../cxx-sdk/current/howtos/subdocument-operations.md)| [.NET](../../../dotnet-sdk/current/howtos/subdocument-operations.md)| [Go](../../../go-sdk/current/howtos/subdocument-operations.md)| [Java](../../../java-sdk/current/howtos/subdocument-operations.md)| [Node.js](../../../nodejs-sdk/current/howtos/subdocument-operations.md)| Kotlin | [PHP](../../../php-sdk/current/howtos/subdocument-operations.md)| [Python](../../../python-sdk/current/howtos/subdocument-operations.md)| [Ruby](../../../ruby-sdk/current/howtos/subdocument-operations.md)| [Scala](../../../scala-sdk/current/howtos/subdocument-operations.md)