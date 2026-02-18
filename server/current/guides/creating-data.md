---
title: Create Documents
description: How to create documents with a command line tool or an SDK.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/guides/pages/creating-data.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/guides/creating-data.html)

# Create Documents

> How to create documents with a command line tool or an SDK. 

## [](#introduction)Introduction

Couchbase stores its [data](../learn/data/data.md) as either JSON or Binary documents with unique IDs (primary keys) by which they can be located.

Documents are organized and grouped in buckets using [scopes and collections](../tutorials/buckets-scopes-and-collections.md). If a scope or collection is not provided when creating a document, Couchbase will automatically store data in the `_default` collection or `_default` scope.

Read the following for further information about the clients available:

* [Command Line Clients](../../../c-sdk/current/hello-world/cbc.md)
* [SDK Clients](#home::sdk.adoc)

> [!WARNING]
> Please note that the examples in this guide will alter the data in your sample database. To restore your sample data, remove and reinstall the travel sample data. Refer to [Sample Buckets](../manage/manage-settings/install-sample-buckets.md) for details.

## [](#inserting-a-document)Inserting a Document

To create a single document in Couchbase, perform an insert operation.

* cbc
* .NET
* Java
* Node.js
* Python

1. Create a structured JSON document to insert in the database.
2. Use the `cbc create` command with `--mode insert` to create the document.
3. Pass the `--scope` and `--collection` parameters to specify the keyspace in which to store the document, and use `<` to specify the JSON document to insert.

---

The example below inserts a new JSON document in the `hotel` keyspace in the `inventory` scope.

First, create the file `hotel-123.json` and store it in the `tmp` directory:

hotel-123.json

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
      "date": "2021-11-17T17:35:05.351Z"
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
	--mode insert hotel-123 <./tmp/hotel-123.json
```

`hotel-123` is the document’s ID. The document is redirected (`<`) to the `cbc` command’s standard input.

Result

```console
hotel-123          Stored. CAS=0x16b37e5081690000
                   SYNCTOKEN=829,51260943619833,92
```

> [!NOTE]
> If the document already exists, `cbc` will return a `LCB_ERR_DOCUMENT_EXISTS` error.

For further details, refer to [cbc(1)](https://docs.couchbase.com/sdk-api/couchbase-c-client/md%5Fdoc%5F2cbc.html).

1. Create a structured document object containing your data.
2. Use the `InsertAsync()` method to insert the document in a given keyspace.

A `MutationResult` object is returned containing the result and metadata relevant to the insert operation.

---

The example below inserts a new JSON document in the `hotel` keyspace in the `inventory` scope.

```csharp
// Create a document object.
var document = new
{
	id = 123,
	name = "Medway Youth Hostel ",
	address = "Capstone Road, ME7 3JE",
	url = "http://www.yha.org.uk",
	geo = new
	{
		lat = 51.35785,
		lon = 0.55818,
		accuracy = "RANGE_INTERPOLATED"
	},
	country = "United Kingdom",
	city = "Medway",
	state = (string)null,
	reviews = new[]
	{
		new {
			content = "This was our 2nd trip here and we enjoyed it more than last year.",
			author = "Ozella Sipes",
			date = DateTime.UtcNow
		}
	},
	vacancy = true,
	description = "40 bed summer hostel about 3 miles from Gillingham."
};

// Insert the document in the hotel collection.
var insertResult = await hotelCollection.InsertAsync("hotel-123", document);

// Print the result's CAS metadata to the console.
Console.WriteLine($"Cas: {insertResult.Cas}");
```

> [!NOTE]
> If the document already exists, the SDK will return a `DocumentExistsException` error.

Click the  View button to see this code in context.

For more information, see [CollectionExtensions](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.KeyValue.CollectionExtensions.html).

1. Create a structured document object containing your data.
2. Use the `insert()` method to insert the document in a given keyspace.

A `MutationResult` object is returned containing the result and metadata relevant to the insert operation.

---

The example below inserts a new JSON document in the `hotel` keyspace in the `inventory` scope.

```java
// Create the document object.
JsonObject geo = JsonObject.create()
    .put("lat", 51.35785)
    .put("lon", 0.55818)
    .put("accuracy", "RANGE_INTERPOLATED");

JsonArray reviews = JsonArray.create();
reviews.add(JsonObject.create()
    .put("content", "This was our 2nd trip here and we enjoyed it more than last year.")
    .put("author", "Ozella Sipes")
    .put("date", DateTimeFormatter.ISO_INSTANT.format(Instant.now())));

JsonObject document = JsonObject.create()
    .put("id", "hotel-123")
    .put("name", "Medway Youth Hostel")
    .put("address", "Capstone Road, ME7 3JE")
    .put("url", "http://www.yha.org.uk")
    .put("geo", geo)
    .put("country", "United Kingdom")
    .put("city", "Medway")
    .put("state", (String) null)
    .put("reviews", reviews)
    .put("vacancy", true)
    .put("description", "40 bed summer hostel about 3 miles from Gillingham.");

// Insert the document in the hotel collection.
MutationResult insertResult = hotelCollection.insert("hotel-123", document);

// Print the result's CAS metadata to the console.
System.out.println("CAS:" + insertResult.cas());
```

> [!NOTE]
> If the document already exists, the SDK will return a `DocumentExistsException` error.

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Collection.html).

1. Create a structured document object containing your data.
2. Use the `insert()` method to insert the document in a given keyspace.

A `MutationResult` promise is returned containing the result and metadata relevant to the insert operation.

---

The example below inserts a new JSON document in the `hotel` keyspace in the `inventory` scope.

```nodejs
// Create a document object.
const document = {
  id: 123,
  name: 'Medway Youth Hostel',
  address: 'Capstone Road, ME7 3JE',
  url: 'http://www.yha.org.uk',
  geo: {
    lat: 51.35785,
    lon: 0.55818,
    accuracy: 'RANGE_INTERPOLATED',
  },
  country: 'United Kingdom',
  city: 'Medway',
  state: null,
  reviews: [
    {
      content:
        'This was our 2nd trip here and we enjoyed it more than last year.',
      author: 'Ozella Sipes',
      date: new Date().toISOString(),
    },
  ],
  vacancy: true,
  description: '40 bed summer hostel about 3 miles from Gillingham.',
}

// Insert the document in the hotel collection.
const insertResult = await hotelCollection.insert('hotel-123', document)

// Print the result's CAS metadata to the console.
console.log('CAS:', insertResult.cas)
```

> [!NOTE]
> If the document already exists, the SDK will return a `DocumentExistsError` error.

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Collection.html).

1. Create a structured document object containing your data.
2. Use the `insert()` function to insert the document in a given keyspace.

A `MutationResult` object is returned containing the result and metadata relevant to the insert operation.

---

The example below inserts a new JSON document in the `hotel` keyspace in the `inventory` scope.

```python
# Create a document object.
document = {
    "id": 123,
    "name": "Medway Youth Hostel",
    "address": "Capstone Road, ME7 3JE",
    "url": "http://www.yha.org.uk",
    "geo": {
        "lat": 51.35785,
        "lon": 0.55818,
        "accuracy": "RANGE_INTERPOLATED",
    },
    "country": "United Kingdom",
    "city": "Medway",
    "state": None,
    "reviews": [
        {
            "content": "This was our 2nd trip here and we enjoyed it more than last year.",
            "author": "Ozella Sipes",
            "date": datetime.now().isoformat(),
        },
    ],
    "vacancy": True,
    "description": "40 bed summer hostel about 3 miles from Gillingham.",
}

# Insert the document in the hotel collection.
insert_result = hotel_collection.insert("hotel-123", document)

# Print the result's CAS metadata to the console.
print("CAS:", insert_result.cas)
```

> [!NOTE]
> If the document already exists, the SDK will return a `DocumentExistsException` error.

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#collection-object).

When a document is created, Couchbase assigns it a [CAS (Compare and Swap)](../../../java-sdk/current/howtos/concurrent-document-mutations.md) value to keep track of the document’s state within the database. Each time a document is mutated the CAS will change accordingly. This unique value allows the database to protect against concurrent updates to the same document.

### [](#inserting-with-options)Inserting with Options

To specify further parameters for the inserted document, such as expiry, add the options to the insert operation.

* cbc
* .NET
* Java
* Node.js
* Python

1. Create a structured document object containing your data.
2. Use the `cbc create` command with `--mode insert` to create the document.
3. Pass the `--scope` and `--collection` parameters to specify the keyspace in which to store the document.
4. Pass any required options, such as `--expiry`, and use `<` to specify the JSON document to insert.

---

The example below inserts a new JSON document and sets it to expire after 60 seconds. The document will be automatically deleted once expired.

First, create the file `hotel-456.json` and store it in the `tmp` directory:

hotel-456.json

```json
{
  "id": 456,
  "title": "Ardèche",
  "name": "La Pradella",
  "address": "rue du village, 07290 Preaux, France",
  "phone": "+33 4 75 32 08 52",
  "url": "http://www.lapradella.fr", 
  "country": "France",
  "city": "Preaux",
  "state": "Rhône-Alpes",
  "vacancy": false
}
```

Now insert the document:

```shell
cbc create -u Administrator -P password -U couchbase://localhost/travel-sample \
	--scope='inventory' \
	--collection='hotel' \
	--mode insert hotel-456 \
	--expiry 60 <./tmp/hotel-456.json
```

Result

```console
hotel-456          Stored. CAS=0x16b5dc9223f30000
                   SYNCTOKEN=733,211618429638288,95
```

For further details, refer to [cbc(1)](https://docs.couchbase.com/sdk-api/couchbase-c-client/md%5Fdoc%5F2cbc.html).

1. Create a structured document object containing your data.
2. Use the `InsertAsync()` method to insert the document with a given option parameter.

---

The example below inserts a new JSON document and sets it to expire after 60 seconds. The document will be automatically deleted once expired.

```csharp
var document = new
{
	id = 456,
	title = "Ardèche",
	name = "La Pradella",
	address = "rue du village, 07290 Preaux, France",
	phone = "+33 4 75 32 08 52",
	url = "http://www.lapradella.fr",
	country = "France",
	city = "Preaux",
	state = "Rhône-Alpes",
	vacancy = false
};

// Insert the document with an expiry time option of 60 seconds.
var insertResult = await hotelCollection.InsertAsync("hotel-456", document, options =>
{
	options.Expiry(TimeSpan.FromSeconds(60));
});

// Print the result's CAS metadata to the console.
Console.WriteLine($"CAS: {insertResult.Cas}");
```

Click the  View button to see this code in context.

For more information, see [CollectionExtensions](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.KeyValue.CollectionExtensions.html).

1. Create a structured document object containing your data.
2. Use the `insert()` method to insert the document with a given option parameter.

---

The example below inserts a new JSON document and sets it to expire after 60 seconds. The document will be automatically deleted once expired.

```java
JsonObject document = JsonObject.create()
    .put("id", 456)
    .put("title", "Ardèche")
    .put("name", "La Pradella")
    .put("address", "rue du village, 07290 Preaux, France")
    .put("phone", "+33 4 75 32 08 52")
    .put("url", "http://www.lapradella.fr")
    .put("country", "France")
    .put("city", "Preaux")
    .put("state", "Rhône-Alpes")
    .put("vacancy", false);

// Insert the document with an expiry time option of 60 seconds.
MutationResult insertResult = hotelCollection.insert(
  "hotel-456",
  document,
  InsertOptions.insertOptions().expiry(Duration.ofSeconds(2))
);

// Print the result's CAS metadata to the console.
System.out.println("CAS:" + insertResult.cas());
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Collection.html).

1. Create a structured document object containing your data.
2. Use the `insert()` function to insert the document with a given option parameter.

---

The example below inserts a new JSON document and sets it to expire after 60 seconds. The document will be automatically deleted once expired.

```nodejs
document = {
  id: 456,
  title: 'Ardèche',
  name: 'La Pradella',
  address: 'rue du village, 07290 Preaux, France',
  phone: '+33 4 75 32 08 52',
  url: 'http://www.lapradella.fr',
  country: 'France',
  city: 'Preaux',
  state: 'Rhône-Alpes',
  vacancy: false,
}

// Insert the document with an expiry time option of 60 seconds.
const insertResult = await hotelCollection.insert('hotel-456', document, {
  expiry: 60,
})

// Print the result's CAS metadata to the console.
console.log('CAS:', insertResult.cas)
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Collection.html).

1. Create a structured document object containing your data.
2. Use the `insert()` function to insert the document with a given option parameter.

---

The example below inserts a new JSON document and sets it to expire after 60 seconds. The document will be automatically deleted once expired.

```python
document = {
    "id": 456,
    "title": "Ardèche",
    "name": "La Pradella",
    "address": "rue du village, 07290 Preaux, France",
    "phone": "+33 4 75 32 08 52",
    "url": "http://www.lapradella.fr",
    "country": "France",
    "city": "Preaux",
    "state": "Rhône-Alpes",
    "vacancy": False,
}
# Insert the document with an expiry time option of 60 seconds.
insert_result = hotel_collection.insert(
    "hotel-456", document, InsertOptions(expiry=timedelta(seconds=60))
)

# Print the result's CAS metadata to the console.
print("CAS:", insert_result.cas)
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#collection-object).

## [](#related-links)Related Links

Key-Value Operations with SDKs:

* [C](../../../c-sdk/current/howtos/kv-operations.md)| [C++](../../../cxx-sdk/current/howtos/kv-operations.md)| [.NET](../../../dotnet-sdk/current/howtos/kv-operations.md)| [Go](../../../go-sdk/current/howtos/kv-operations.md)| [Java](../../../java-sdk/current/howtos/kv-operations.md)| [Kotlin](../../../kotlin-sdk/current/howtos/kv-operations.md)| [Node.js](../../../nodejs-sdk/current/howtos/kv-operations.md)| [PHP](../../../php-sdk/current/howtos/kv-operations.md)| [Python](../../../python-sdk/current/howtos/kv-operations.md)| [Ruby](../../../ruby-sdk/current/howtos/kv-operations.md)| [Rust](../../../rust-sdk/current/howtos/kv-operations.md)| [Scala](../../../scala-sdk/current/howtos/kv-operations.md)