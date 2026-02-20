---
title: Update Documents
description: How to update documents with a command line tool or an SDK.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/guides/pages/updating-data.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:guides:updating-data.adoc[]
---

[View original HTML](/server/7.6/guides/updating-data.html)

# Update Documents

> How to update documents with a command line tool or an SDK. 

## [](#introduction)Introduction

Couchbase Server allows you to update data within a document by ID using either an upsert or a replace operation. An upsert operation will update or create a full document with the given data. A replace operation, on the other hand, will only replace a document if it exists within the database.

Read the following for further information about the clients available:

* [Command Line Clients](../../../c-sdk/current/hello-world/cbc.md)
* [SDK Clients](#home::sdk.adoc)

> [!WARNING]
> Please note that the examples in this guide will alter the data in your sample database. To restore your sample data, remove and reinstall the travel sample data. Refer to [Sample Buckets](../manage/manage-settings/install-sample-buckets.md) for details.

## [](#upserting-a-document)Upserting a Document

To update a document, or create the document if it does not exist, perform an upsert operation.

* cbc
* .NET
* Java
* Node.js
* Python

1. Create a JSON document containing the updated data.
2. Use the `cbc create` command with `--mode upsert` to update the document in the database. If it does not exist, Couchbase creates a new document.

---

The example below updates the existing document `hotel-123`.

First, create the updated file `hotel-123.json` and store it the `tmp` directory:

hotel-123

```json
{
  "id": 123,
  "name": "Medway Youth Hostel",
  "address": "Capstone Road, ME7 3JE",
  "url": "http://www.yha.org.uk",
  "country": "United Kingdom",
  "city": "Medway",
  "state": null,
  "vacancy": true,
  "description": "40 bed summer hostel about 3 miles from Gillingham."
}
```

Now insert the document:

```shell
cbc create -u Administrator -P password -U couchbase://localhost/travel-sample \
	--scope='inventory' \
	--collection='hotel' \
	--mode upsert hotel-123 <./tmp/hotel-123.json
```

Result

```console
hotel-123            Stored. CAS=0x16bd48617f9d0000
                     SYNCTOKEN=500,228620113724555,292
```

For further details, refer to [cbc(1)](https://docs.couchbase.com/sdk-api/couchbase-c-client/md%5Fdoc%5F2cbc.html).

Use the `UpsertAsync()` method to update a document in the database. If it does not exist, Couchbase creates a new document.

---

The example below updates the existing document `hotel-123`.

```csharp
// Update or create a document in the hotel collection.
var upsertResult = await hotelCollection.UpsertAsync("hotel-123", document);

// Print the result's CAS metadata to the console.
Console.WriteLine($"Cas: {upsertResult.Cas}");
```

Click the  View button to see this code in context.

For more information, see [CollectionExtensions](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.KeyValue.CollectionExtensions.html).

Use the `upsert()` method to update a document in the database. If it does not exist, Couchbase creates a new document.

---

The example below updates the existing document `hotel-123`.

```java
// Update or create a document in the hotel collection.
MutationResult upsertResult = hotelCollection.upsert("hotel-123", document);

// Print the result's CAS metadata to the console.
System.out.println("CAS:" + upsertResult.cas());
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Collection.html).

Use the `upsert()` function to update a document in the database. If it does not exist, Couchbase creates a new document.

---

The example below updates the existing document `hotel-123`.

```nodejs
// Update or create a document in the hotel collection.
const upsertResult = await hotelCollection.upsert('hotel-123', document)

// Print the result's CAS metadata to the console.
console.log('CAS:', upsertResult.cas)
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Collection.html).

Use the `upsert()` function to update a document in the database. If it does not exist, Couchbase creates a new document.

---

The example below updates the existing document `hotel-123`.

```python
# Update or create a document in the hotel collection.
upsert_result = hotel_collection.upsert("hotel-123", document)

# Print the result's CAS metadata to the console.
print("CAS:", upsert_result.cas)
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#collection-object).

## [](#replacing-a-document)Replacing a Document

To update a document that already exists, perform a replace operation.

* cbc
* .NET
* Java
* Node.js
* Python

1. Update a JSON document with some new data.
2. Use the `cbc create` command with `--mode replace` to update a document.

---

The example below adds a new entry to the `reviews` array in document `hotel-123`.

First, create the updated file `hotel-123.json` and store it the `tmp` directory:

hotel-123

```json
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
      "date": "2021-12-13T17:38:02.935Z"
    },
    {
      "content": "This hotel was cozy, conveniently located and clean.",
      "author": "Carmella O'Keefe",
      "date": "2021-12-13T17:38:02.974Z"
    }
  ],
  "vacancy": true,
  "description": "40 bed summer hostel about 3 miles from Gillingham."
}
```

Now insert the document:

```shell
cbc create -u Administrator -P password -U couchbase://localhost/travel-sample \
	--scope='inventory' \
	--collection='hotel' \
	--mode replace hotel-123 <./tmp/hotel-123.json
```

Result

```console
hotel-123            Stored. CAS=0x16bd486ce6250000
                     SYNCTOKEN=500,228620113724555,293
```

> [!NOTE]
> If the document cannot be found, `cbc` will return a `LCB_ERR_DOCUMENT_NOT_FOUND` error.

For further details, refer to [cbc(1)](https://docs.couchbase.com/sdk-api/couchbase-c-client/md%5Fdoc%5F2cbc.html).

1. Fetch an existing document and change some of its data.
2. Use the `ReplaceAsync()` function to update a document in Couchbase. To ensure data has not been modified before executing the replace operation, pass the document’s `CAS` value to the method.

A new `CAS` value is provided in the returned `MutationResult` object.

---

The example below adds a new entry to the `reviews` array in document `hotel-123`.

```csharp
// Fetch an existing hotel document.
var getResult = await hotelCollection.GetAsync("hotel-123");
var existingDoc = getResult.ContentAs<JObject>();

// Get the current CAS value.
var currentCas = getResult.Cas;
Console.WriteLine($"Current Cas: {currentCas}");

// Add a new review to the reviews array.
var reviews = (JArray)existingDoc["reviews"];
reviews.Add(new JObject(
	new JProperty("content", "This hotel was cozy, conveniently located and clean."),
	new JProperty("author", "Carmella O'Keefe"),
	new JProperty("date", DateTime.UtcNow))
);

// Update the document with new data and pass the current CAS value. 
var replaceResult = await hotelCollection.ReplaceAsync("hotel-123", existingDoc, options =>
{
	options.Cas(currentCas);
});

// Print the new CAS value.
Console.WriteLine($"New Cas: {replaceResult.Cas}");
```

> [!NOTE]
> If the document does not exist, the SDK will return a `DocumentNotFoundException` error.

Click the  View button to see this code in context.

For more information, see [CollectionExtensions](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.KeyValue.CollectionExtensions.html).

1. Fetch an existing document and change some of its data.
2. Use the `replace()` method to update a document in Couchbase. To ensure data has not been modified before executing the replace operation, pass the document’s `CAS` value to the method.

A new `CAS` value is provided in the returned `MutationResult` object.

---

The example below adds a new entry to the `reviews` array in document `hotel-123`.

```java
// Fetch an existing hotel document
GetResult getResult = hotelCollection.get("hotel-123");
JsonObject existingDoc = getResult.contentAsObject();

// Get the current CAS value.
Long currentCas = getResult.cas();
System.out.println("Current CAS:" + currentCas);

// Add a new review to the reviews array.
existingDoc.getArray("reviews").add(JsonObject.create()
    .put("content", "This hotel was cozy, conveniently located and clean.")
    .put("author", "Carmella O'Keefe")
    .put("date", DateTimeFormatter.ISO_INSTANT.format(Instant.now())
  )
);

// Update the document with new data and pass the current CAS value. 
MutationResult replaceResult = hotelCollection.replace(
    "hotel-123",
    existingDoc,
    ReplaceOptions.replaceOptions().cas(currentCas)
);

// Print the new CAS value.
System.out.println("New CAS:" + replaceResult.cas());
```

> [!NOTE]
> If the document does not exist, the SDK will return a `DocumentNotFoundException` error.

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Collection.html).

1. Fetch an existing document and change some of its data.
2. Use the `replace()` function to update a document in Couchbase. To ensure data has not been modified before executing the replace operation, pass the document’s `CAS` value to the method.

A new `CAS` value is provided in the returned `MutationResult` object.

---

The example below adds a new entry to the `reviews` array in document `hotel-123`.

```nodejs
// Fetch an existing hotel document.
getResult = await hotelCollection.get('hotel-123')
const existingDoc = getResult.content

// Get the current CAS value.
const currentCas = getResult.cas
console.log('Current CAS:', currentCas)

// Add a new review to the reviews array.
existingDoc['reviews'].push({
  content: 'This hotel was cozy, conveniently located and clean.',
  author: "Carmella O'Keefe",
  date: new Date().toISOString(),
})

// Update the document with new data and pass the current CAS value.
const replaceResult = await hotelCollection.replace(
  'hotel-123',
  existingDoc
)

// Print the new CAS value.
console.log('New CAS:', replaceResult.cas)
```

> [!NOTE]
> If the document does not exist, the SDK will return a `DocumentNotFoundError` error.

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Collection.html).

1. Fetch an existing document and change some of its data.
2. Use the `replace()` function to update a document in Couchbase. To ensure data has not been modified before executing the replace operation, pass the document’s `CAS` value to the method.

A new `CAS` value is provided in the returned `MutationResult` object.

---

The example below adds a new entry to the `reviews` array in document `hotel-123`.

```python
# Fetch an existing hotel document.
get_result = hotel_collection.get("hotel-123")
existing_doc = get_result.content_as[dict]

# Get the current CAS value.
current_cas = get_result.cas
print("Current CAS:", get_result.cas)

# Add a new review to the reviews array.
existing_doc["reviews"].append({
    "content": "This hotel was cozy, conveniently located and clean.",
    "author": "Carmella O'Keefe",
    "date": datetime.now().isoformat(),
})

# Update the document with new data and pass the current CAS value.
replace_result = hotel_collection.replace(
    "hotel-123", existing_doc, ReplaceOptions(cas=current_cas)
)
print("New CAS:", replace_result.cas)
```

> [!NOTE]
> If the document does not exist, the SDK will return a `DocumentNotFoundException` error.

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#collection-object).

## [](#updating-a-sub-document)Updating a Sub-Document

To change a specific field inside a document, you can perform a Sub-Document operation. You can use either a Sub-Document upsert or replace operation depending on what’s required for your application.

* cbc-subdoc
* .NET
* Java
* Node.js
* Python

1. Connect to the `cbc-subdoc` interactive shell.
2. Use the `dict-upsert` command to update/add a field in a document, or use the `replace` command if you require the field to exist.
3. Pass the field to update/add and its value with the `--path` argument.

---

The example below upserts a `pets_ok` field in document `hotel-123` and sets the value to true.

```console
cbc-subdoc -u Administrator -P password -U couchbase://localhost/travel-sample
subdoc> dict-upsert airport_1254 --path pets_ok=true
```

Result

```console
airport_1254         CAS=0x16be23af9f630000
0. Size=0, RC=LCB_SUCCESS (0)
```

For further details, refer to [cbc-subdoc(1)](https://docs.couchbase.com/sdk-api/couchbase-c-client/md%5Fdoc%5Fcbc%5Fsubdoc.html).

1. Call the `MutateInAsync()` method, which takes a document ID and an IEnumerable containing `MutateInSpec` objects.
2. Use a `MutateInSpec` object to specify the sub-operation to be performed within the lookup.

A `MutateInResult` object is returned, containing the result and metadata relevant to the Sub-Document update operation.

---

The example below upserts a `pets_ok` field in document `hotel-123` and sets the value to true.

```csharp
var mutateInResult = await hotelCollection.MutateInAsync("hotel-123",
	specs => specs.Upsert("pets_ok", true)
);
Console.WriteLine($"Cas: {mutateInResult.Cas}");
```

Click the  View button to see this code in context.

For more information, see [CollectionExtensions](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.KeyValue.CollectionExtensions.html).

1. Call the `mutateIn()` method, which takes a document ID and an array of `MutateInSpec` objects.
2. Use a `MutateInSpec` object to specify the sub-operation to be performed within the lookup.

A `MutateInResult` object is returned, containing the result and metadata relevant to the Sub-Document update operation.

---

The example below upserts a `pets_ok` field in document `hotel-123` and sets the value to true.

```java
List<MutateInSpec> specs = Arrays.asList(MutateInSpec.upsert("pets_ok", true));

MutateInResult mutateInResult = hotelCollection.mutateIn("hotel-123", specs);
System.out.println("CAS:" + mutateInResult.cas());
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Collection.html).

1. Call the `mutateIn()` method, which takes a document ID and an array of `MutateInSpec` objects.
2. Use a `MutateInSpec` object to specify the sub-operation to be performed within the lookup.

A `MutateInResult` object is returned, containing the result and metadata relevant to the Sub-Document update operation.

---

The example below upserts a `pets_ok` field in document `hotel-123` and sets the value to true.

```nodejs
const mutateInResult = await hotelCollection.mutateIn('hotel-123', [
  couchbase.MutateInSpec.upsert('pets_ok', true),
])
console.log('CAS:', mutateInResult.cas)
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Collection.html).

1. Call the `mutate_in()` function, which takes a document ID and a list of `MutateInSpec` objects.
2. Use a `MutateInSpec` object to specify the sub-operation to be performed within the lookup.

A `MutateInResult` object is returned, containing the result and metadata relevant to the Sub-Document get operation.

---

The example below upserts a `pets_ok` field in document `hotel-123` and sets the value to true.

```python
mutate_in_result = hotel_collection.mutate_in(
    "hotel-123", [subdocument.upsert("pets_ok", True)]
)
print("CAS:", mutate_in_result.cas)
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#collection-object).

## [](#related-links)Related Links

Key-Value Operations with SDKs:

* [C](../../../c-sdk/current/howtos/kv-operations.md)| [C++](../../../cxx-sdk/current/howtos/kv-operations.md)| [.NET](../../../dotnet-sdk/current/howtos/kv-operations.md)| [Go](../../../go-sdk/current/howtos/kv-operations.md)| [Java](../../../java-sdk/current/howtos/kv-operations.md)| [Kotlin](../../../kotlin-sdk/current/howtos/kv-operations.md)| [Node.js](../../../nodejs-sdk/current/howtos/kv-operations.md)| [PHP](../../../php-sdk/current/howtos/kv-operations.md)| [Python](../../../python-sdk/current/howtos/kv-operations.md)| [Ruby](../../../ruby-sdk/current/howtos/kv-operations.md)| [Rust](../../../rust-sdk/current/howtos/kv-operations.md)| [Scala](../../../scala-sdk/current/howtos/kv-operations.md)

Sub-Document operations with SDKs:

* [C](../../../c-sdk/current/howtos/subdocument-operations.md)| [C++](../../../cxx-sdk/current/howtos/subdocument-operations.md)| [.NET](../../../dotnet-sdk/current/howtos/subdocument-operations.md)| [Go](../../../go-sdk/current/howtos/subdocument-operations.md)| [Java](../../../java-sdk/current/howtos/subdocument-operations.md)| Kotlin | [Node.js](../../../nodejs-sdk/current/howtos/subdocument-operations.md)| [PHP](../../../php-sdk/current/howtos/subdocument-operations.md)| [Python](../../../python-sdk/current/howtos/subdocument-operations.md)| [Ruby](../../../ruby-sdk/current/howtos/subdocument-operations.md)| [Rust](../../../rust-sdk/current/howtos/subdocument-operations.md)| [Scala](../../../scala-sdk/current/howtos/subdocument-operations.md)