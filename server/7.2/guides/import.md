---
title: Importing Data
description: How to import documents into Couchbase.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/guides/pages/import.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:guides:import.adoc[]
---

[View original HTML](/server/7.2/guides/import.html)

# Importing Data

> How to import documents into Couchbase.  
> This guide is for Couchbase Server.

## [](#introduction)Introduction

Importing data can be done from the Couchbase Server UI, via the [cbimport](../tools/cbimport.md) command-line tool shipped with Couchbase Server, or using the SDK to script the process.

Data load essentially consists of the following steps:

1. Prepare data in some well known format such as Comma Separated Values (.csv) or JSON documents.
2. Parse this data, and iterate over each document.
3. Connect to your Couchbase instance.
4. Connect to the appropriate bucket, scope, and collection.
5. Decide on the key for this document (could be an ID, a sequence number, or some combination of fields).
6. Do any additional processing if required.
7. Insert the document.

### [](#couchbase-clients)Couchbase Clients

Clients access data by connecting to a Couchbase cluster over the network. The most common type of client is a Couchbase SDK, which is a full programmatic API that enables applications to take the best advantage of Couchbase. This developer guide focuses on the most commonly used SDKs, but full explanations and reference documentation for all SDKs is available.

The command line clients also provide a quick and streamlined interface for access and are suitable if you just want to access an item without writing any code. For this guide, we’re especially interested in the `cbimport` tool.

> [!NOTE]
> With some editions, the command line clients are provided as part of the installation of Couchbase Server. Assuming a default installation, you can find them in the following location, depending on your operating system:
> 
> | Linux   | /opt/couchbase/bin                                                       |
> | ------- | ------------------------------------------------------------------------ |
> | Windows | C:\\Program Files\\Couchbase\\Server\\bin                                |
> | macOS   | /Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin |

The Couchbase Server UI also offers a graphical interface to `cbimport`.

Read the following for further information about the clients available for importing data:

* [cbimport](../tools/cbimport.md)
* [SDK Clients](#home::sdk.adoc)
* [Couchbase Server UI](../manage/import-documents/import-documents.md)

## [](#preparing-the-data)Preparing the Data

To prepare the data, extract or generate your data in an appropriate data format.

The following are well supported for export as well as by `cbimport` and the module ecosystems of all Couchbase SDKs.

* CSV
* TSV
* JSON
* JSONL

Comma Separated Values (.csv) are easily exported from many spreadsheet and database applications.

Ensure that the first row is a header row containing the names of the columns within the document.

```csv
id,type,name
20001,airline,CSV-air-1
20002,airline,CSV-air-2
```

Tab Separated Values (.tsv) are a common variant of CSV files.

```tsv
id	type	name
20011	airline	TSV-air-1
20012	airline	TSV-air-2
```

JSON (.json) files are especially well suited to import into Couchbase, as it’s the default native datatype.

A .json file contains only one single value, so to give flexibility to import one or many values, format this as an **array** of the values you want to store.

```json
[
	{"id":20021, "type":"airline", "name":"JSON-air-1"},
	{"id":20022, "type":"airline", "name":"JSON-air-2"},
	{"id":20023, "type":"airline", "name":"JSON-air-3"}
]
```

JSON Lines (.json) also known as NDJSON is a common format for streaming JSON, with one JSON object per line of text.

```json
{"id":20031, "type":"airline", "name":"JSONL-air-1"}
{"id":20032, "type":"airline", "name":"JSONL-air-2"}
{"id":20033, "type":"airline", "name":"JSONL-air-3"}
```

## [](#using-cbimport)Using `cbimport`

Using [cbimport](../tools/cbimport.md) is straightforward. Ensure you have the path to the command line clients in Couchbase Server in your path.

You can import all of the data formats described above.

* CSV
* TSV
* JSON
* JSONL

To import a CSV file using `cbimport csv`:

1. Use the `--dataset` argument to specify the CSV file.
2. Use the `--cluster`, `--username`, and `--password` arguments to specify your connection details.
3. Use the `--bucket` and `--scope-collection-exp` arguments to specify the bucket, scope, and collection as required.
4. Use the `--generate-key` argument to specify an ID for the imported documents.

---

The following example imports a local CSV file, generating IDs such as `airline_1234`.

```sh
cbimport csv \
  --dataset file://./import.csv \
  --cluster localhost --username Administrator --password password \
  --bucket travel-sample --scope-collection-exp inventory.airline \
  --generate-key %type%_%id%
```

To import a TSV file using `cbimport csv`:

1. Use the `--dataset` argument to specify the TSV file.
2. Use the `--field-separator` argument to specify the field separation character, such as `"\t"` for tab.
3. Use the `--cluster`, `--username`, and `--password` arguments to specify your connection details.
4. Use the `--bucket` and `--scope-collection-exp` arguments to specify the bucket, scope, and collection as required.
5. Use the `--generate-key` argument to specify an ID for the imported documents.

---

The following example imports a local TSV file, generating IDs such as `airline_1234`.

```sh
cbimport csv \
  --dataset file://./import.tsv --field-separator "\t" \
  --cluster localhost --username Administrator --password password \
  --bucket travel-sample --scope-collection-exp inventory.airline \
  --generate-key %type%_%id%
```

To import a JSON file using `cbimport json`:

1. Use the `--dataset` argument to specify the JSON file.
2. Set the `--format` argument to `list`.
3. Use the `--cluster`, `--username`, and `--password` arguments to specify your connection details.
4. Use the `--bucket` and `--scope-collection-exp` arguments to specify the bucket, scope, and collection as required.
5. Use the `--generate-key` argument to specify an ID for the imported documents.

---

The following example imports a local JSON file, generating IDs such as `airline_1234`.

```sh
cbimport json \
  --dataset file://./import.json --format list \
  --cluster localhost --username Administrator --password password \
  --bucket travel-sample --scope-collection-exp inventory.airline \
  --generate-key %type%_%id%
```

To import a CSV file using `cbimport json`:

1. Use the `--dataset` argument to specify the JSONL file.
2. Set the `--format` argument to `lines`.
3. Use the `--cluster`, `--username`, and `--password` arguments to specify your connection details.
4. Use the `--bucket` and `--scope-collection-exp` arguments to specify the bucket, scope, and collection as required.
5. Use the `--generate-key` argument to specify an ID for the imported documents.

---

The following example imports a local JSONL file, generating IDs such as `airline_1234`.

```sh
cbimport json \
  --dataset file://./import.jsonl --format lines \
  --cluster localhost --username Administrator --password password \
  --bucket travel-sample --scope-collection-exp inventory.airline \
  --generate-key %type%_%id%
```

## [](#importing-using-an-sdk)Importing Using an SDK

While `cbimport` accomplishes all the necessary steps in a single command, as above, using an SDK gives you more flexibility and control. However all the same considerations apply, so let us look at those in turn.

### [](#parsing-the-import-into-an-array-or-stream-of-records)Parsing the Import into an Array or Stream of Records

The details of how to parse the import data vary depending on the chosen input format, and the most appropriate library for your SDK.

#### [](#parsing-csv-and-tsv-data)Parsing CSV and TSV Data

* .NET
* Java
* Node.js
* Python

To parse CSV and TSV data, use the [CsvHelper](https://joshclose.github.io/CsvHelper/) library.

```csharp
using CsvHelper;
using CsvHelper.Configuration;
using System.Globalization;
```

```csharp
public async Task importCSV(string filename)
{
    using (var reader = new StreamReader(filename))
    using (var csv = new CsvReader(reader, CultureInfo.InvariantCulture))
    {
        var records = csv.GetRecords<dynamic>();
        foreach (dynamic record in records) {
            await upsertDocument(record);
        }
    }
}
```

```csharp
public async Task importTSV(string filename)
{
    using (var reader = new StreamReader("import.tsv"))
    using (var tsv = new CsvReader(reader,
        new CsvConfiguration(CultureInfo.InvariantCulture)
            { Delimiter = "\t" }))
    {
        var records = tsv.GetRecords<dynamic>();
        foreach (dynamic record in records) {
            await upsertDocument(record);
        }
    }
}
```

Click the  View button to see any code sample in context.

To parse CSV and TSV data, use the [opencsv](http://opencsv.sourceforge.net/) library.

```java
import com.opencsv.*;
```

```java
public void importCSV() {
  try (CSVReaderHeaderAware csv = new CSVReaderHeaderAware(
      new FileReader("modules/howtos/examples/import.csv"))) {
          
    Map<String, String> row;
    while ((row = csv.readMap()) != null) {
      upsertRow(row);
    }
  }
  catch (java.io.FileNotFoundException e) {
    System.out.println("handle FileNotFoundException...");
  }
  catch (java.io.IOException e) {
    System.out.println("handle IOException...");
  }
  catch (com.opencsv.exceptions.CsvValidationException e) {
    System.out.println("handle CsvValidationException...");
  }
}
```

```java
public void importTSV() {
  CSVParser parser =
    new CSVParserBuilder()
    .withSeparator('\t')
    .withIgnoreQuotations(true)
    .build();
  
  try (CSVReaderHeaderAware tsv =
      new CSVReaderHeaderAwareBuilder(
        new FileReader("modules/howtos/examples/import.tsv"))
      .withCSVParser(parser)
      .build()) {

    Map<String, String> row;
    while ((row = tsv.readMap()) != null) {
      upsertRow(row);
    }
  }
  // ...
}
```

If you’re using the **Reactor API** then, as OpenCSV does not have a built-in converter, use the [Flux::generate](https://projectreactor.io/docs/core/release/api/reactor/core/publisher/Flux.html#generate-java.util.concurrent.Callable-java.util.function.BiFunction-java.util.function.Consumer-) method to convert the CSV or TSV file into a stream:

```java
public void importCSV_batch() {
  
  Flux<Map<String,String>> rows = Flux.generate(
    
    () -> new CSVReaderHeaderAware(
      new FileReader("modules/howtos/examples/import.csv")),
    
    (state, sink) -> {
      try {
        Map<String,String> row = state.readMap();
        if (row == null) { sink.complete(); }
        else { sink.next(row); }
        return state;
      }
      catch (Exception e) { throw new RuntimeException(e); }
    },
    state -> {
      try { state.close(); }
      catch (Exception e) { throw new RuntimeException(e); }
    }
  );

  Flux<MutationResult> results = 
    rows
    .map(row -> preprocess(row))
    .flatMap(doc -> reactiveCollection.upsert(doc.getId(), doc.getContent()))
    .doOnNext(System.out::println);

  results.blockLast(Duration.ofSeconds(60));
}
```

```java
public void importTSV_batch() {

  Flux<Map<String,String>> rows = Flux.generate(
    
    () -> {
      CSVParser parser =
        new CSVParserBuilder()
        .withSeparator('\t')
        .withIgnoreQuotations(true)
        .build();
      return
        new CSVReaderHeaderAwareBuilder(
          new FileReader("modules/howtos/examples/import.tsv"))
        .withCSVParser(parser)
        .build();
    },
    
    // ...
}
```

Click the  View button to see any code sample in context.

To parse CSV and TSV data, use the [csv-parse](https://csv.js.org/parse/) library.

```nodejs
const { parse: csvParser } = require('csv-parse');
```

```nodejs
const csvStream = (filename) =>
  fs.createReadStream(filename)
  .pipe(
      csvParser({columns: true}))
```

```nodejs
const tsvStream = (filename) =>
  fs.createReadStream(filename)
    .pipe(
      csvParser({
        columns: true,
        delimiter: '\t'}))
```

Click the  View button to see any code sample in context.

To parse CSV and TSV data, use the [csv](https://docs.python.org/3/library/csv.html) library.

```python
import csv
```

```python
def csv_import(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            upsert(row)
```

```python
def tsv_import(filename):
    with open(filename, newline='') as tsvfile:
        reader = csv.DictReader(tsvfile, delimiter='\t')
        for row in reader:
            upsert(row)
```

Click the  View button to see any code sample in context.

#### [](#parsing-json-and-jsonl-data)Parsing JSON and JSONL Data

* .NET
* Java
* Node.js
* Python

To parse JSON and JSONL data, use [Newtonsoft](https://www.newtonsoft.com/json).

```csharp
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
```

```csharp
public async Task importJSON(string filename)
{
    using (var reader = new StreamReader("import.json"))
    {
        var jsonReader = new JsonTextReader(reader);
        JArray arr = (JArray)JToken.ReadFrom(jsonReader);
        
        foreach (JObject record in arr)
        {
            await upsertDocument(record);
        }
    }
}
```

```csharp
public async Task importJSONL(string filename)
{
    using (var reader = new StreamReader("import.jsonl"))
    {
        var jsonlReader = new JsonTextReader(reader)
        {
            SupportMultipleContent = true
        };
        while (jsonlReader.Read())
        {
            var record = (JObject)JToken.ReadFrom(jsonlReader);
            await upsertDocument(record);
        }
    }
}
```

Click the  View button to see any code sample in context.

To parse **JSON** data, read the file as a string, then use the built-in Couchbase [JSON](../../../java-sdk/current/howtos/json.md) handling to parse the result into an array of JSON objects.

```java
import com.couchbase.client.java.json.*;
```

```java
public void importJSON() {
  try {
    String content  = new String(
      Files.readAllBytes( // read whole document into memory
        Paths.get("modules/howtos/examples/import.json")),
      StandardCharsets.UTF_8);
    
    for (Object row: JsonArray.fromJson(content)) {
      JsonObject json = ((JsonObject) row);
      upsertRow(json.toMap());
    }
  }
  catch (java.io.FileNotFoundException e) {
    System.out.println("handle FileNotFoundException...");
  }
  catch (java.io.IOException e) {
    System.out.println("handle IOException...");
  }
}
```

If you’re using the **Reactor API** then, once you have read the JSON array, use the [Flux::fromIterable](https://projectreactor.io/docs/core/release/api/reactor/core/publisher/Flux.html#fromIterable-java.lang.Iterable-) method to convert it into streams:

```java
public void importJSON_batch() {

  try {
    String content  = new String(
      Files.readAllBytes( // read whole document into memory
        Paths.get("modules/howtos/examples/import.json")),
      StandardCharsets.UTF_8);
    
    Flux<MutationResult> results = 
      Flux.fromIterable(JsonArray.fromJson(content))
        .map(row -> ((JsonObject) row).toMap())
        .map(map -> preprocess(map))
        .flatMap(doc -> reactiveCollection.upsert(doc.getId(), doc.getContent()))
        .doOnNext(System.out::println);

    results.blockLast(Duration.ofSeconds(60));
  }
  // ...
}
```

To parse **JSONL** data: do the same, but read the file line-by-line.

```java
public void importJSONL() {
  try (BufferedReader br =
        new BufferedReader(
          new FileReader("modules/howtos/examples/import.jsonl"))) {
            
      String line;
      while ((line = br.readLine()) != null) {
        Map<String,Object> row =
          JsonObject.fromJson(line).toMap();
          
        upsertRow(row);
    }
  }
  // ...
}
```

If you’re using the **Reactor API** then open the JSONL file as a stream using the [Flux::using](https://projectreactor.io/docs/core/release/api/reactor/core/publisher/Flux.html#using-java.util.concurrent.Callable-java.util.function.Function-java.util.function.Consumer-) method.

```java
public void importJSONL_batch() {

  Flux<String> lines = Flux.using(
    () -> Files.lines(Paths.get("modules/howtos/examples/import.jsonl")),
    Flux::fromStream,
    BaseStream::close);

  Flux<MutationResult> results =
    lines
        .map(line -> JsonObject.fromJson(line).toMap())
        .map(map -> preprocess(map))
        .flatMap(doc -> reactiveCollection.upsert(doc.getId(), doc.getContent()))
        .doOnNext(System.out::println);

  results.blockLast(Duration.ofSeconds(60));
}
```

Click the  View button to see any code sample in context.

Use the [stream-json](https://github.com/uhop/stream-json) library.

> [!NOTE]
> stream-json formats its output with a `{ key: …​, value: …​}` wrapper, so we need to map the stream into the expected format.

```nodejs
const stream = require('stream'); 

// for JSON
const StreamArray = require('stream-json/streamers/StreamArray')

// for JsonL
const {parser: jsonlParser} = require('stream-json/jsonl/Parser');
```

```nodejs
const map = (f) =>
  new stream.Transform({
    objectMode: true,
    transform: (obj, _, next) => next(null, f(obj))
  })
  
const jsonStream = (filename) =>
  fs.createReadStream(filename)
    .pipe(StreamArray.withParser())
    .pipe(map(obj => obj.value))
```

```nodejs
const jsonlStream = (filename) =>
  fs.createReadStream(filename)
    .pipe(jsonlParser())
    .pipe(map(obj => obj.value))
```

Click the  View button to see any code sample in context.

Use the [json](https://docs.python.org/3/library/json.html) library:

```python
import json
```

```python
def json_import(filename):
    with open(filename) as jsonfile:
        data = json.load(jsonfile)
        for row in data:
            upsert(row)
```

```python
def jsonl_import(filename):
    with open(filename) as jsonlfile:
        for line in jsonlfile:
            row = json.loads(line)
            upsert(row)
```

Click the  View button to see any code sample in context.

### [](#connecting-to-the-couchbase-server)Connecting to the Couchbase Server

First, you need the connection details for the Couchbase Server.

Now decide which bucket and [scope and collection](../tutorials/buckets-scopes-and-collections.md) you want to import to, and create them if they do not already exist.

* .NET
* Java
* Node.js
* Python

```csharp
var cluster = await Cluster.ConnectAsync(
    "couchbase://your-ip",
    "Administrator", "password");
var bucket =  await cluster.BucketAsync("travel-sample");
var scope = await bucket.ScopeAsync("inventory");
var _collection = await scope.CollectionAsync("airline");
```

Click the  View button to see any code sample in context.

For more information, see [Managing Connections](../../../dotnet-sdk/current/howtos/managing-connections.md).

```java
Cluster cluster = Cluster.connect(
  connectionString,
  ClusterOptions
    .clusterOptions(username, password));

Bucket bucket = cluster.bucket(bucketName);
Scope scope = bucket.scope("inventory");

collection = scope.collection("airline");
```

If you’re using the [Reactive API](../../../java-sdk/current/howtos/concurrent-async-apis.md#reactive-programming-with-reactor), then use the reactive collection instead:

```java
reactiveCollection = collection.reactive();
```

Click the  View button to see any code sample in context.

For more information, see [Managing Connections](../../../java-sdk/current/howtos/managing-connections.md).

```nodejs
const cluster = await couchbase.connect('couchbase://localhost', {
  username: 'Administrator',
  password: 'password',
})

const bucket = cluster.bucket('travel-sample')
const collection = bucket.scope('inventory').collection('airline')
```

Click the  View button to see any code sample in context.

For more information, see [Managing Connections](../../../nodejs-sdk/current/howtos/managing-connections.md).

```python
cluster = Cluster(
    "couchbase://localhost",
    authenticator=PasswordAuthenticator(
        "Administrator", "password"))

bucket = cluster.bucket("travel-sample")

collection = bucket.scope("inventory").collection("airline")
```

Click the  View button to see any code sample in context.

For more information, see [Managing Connections](../../../python-sdk/current/howtos/managing-connections.md).

### [](#inserting-the-documents)Inserting the Documents

Having processed each imported document, you can insert it into the keyspace. Couchbase is a key-value store, and the document is the value, so before you can insert the document, you need to determine the key.

To insert an imported document into the keyspace:

1. Specify the key. This could be as easy as extracting the `id` field from the document, or using an incrementing sequence number.
2. Do any additional processing, for example calculating fields, or adding metadata about the importer.
3. Finally, use an upsert operation to the store the document.

> [!TIP]
> Use `upsert` rather than `insert` to upload the document even if the target key already has a value. This means that in the case of any error, it’s easy to make any required tweaks to the import file and re-run the whole import.

* .NET
* Java
* Node.js
* Python

To store the data, hook the prepared data into an `upsert` routine.

> [!NOTE]
> As CsvHelper and Newtonsoft generate different outputs, we have provided some overloaded options that work for either.

```csharp
// CsvHelper emits `dynamic` records
public async Task upsertDocument(dynamic record) {
    // define the key
    string key = record.type + "_" + record.id;

    // do any additional processing
    record.importer = ".NET SDK";

    // upsert the document
    await _collection.UpsertAsync(key, record);

    // any required logging
    Console.WriteLine(key);
}

// Newtonsoft.Json.Linq emits `JObjects`
public async Task upsertDocument(JObject record) {
    // define the key
    string key = record["type"] + "_" + record["id"];

    // do any additional processing
    record["importer"] = ".NET SDK";
    
    // upsert the document
    await _collection.UpsertAsync(key, record);
    
    // any required logging
    Console.WriteLine(key);
}
```

Click the  View button to see any code sample in context.

For more information, see [Data Operations](../../../dotnet-sdk/current/howtos/kv-operations.md).

To store the data, hook the prepared data into an `upsert` routine. For the blocking API, use the method below.

```java
public void upsertRow(Map row) {
  
  JsonDocument doc = preprocess(row);
  
  String key = doc.getId();
  Object value = doc.getContent();
  
  // upsert the document
  collection.upsert(key, value);
  
  // any required logging
  System.out.println(key);
  System.out.println(value);
}
```

The **Reactive API** examples above already include a call to `ReactiveCollection::upsert`.

In both cases, you must provide a preprocess routine which returns a key-value tuple object:

```java
class JsonDocument {
  private final String id;
  private final JsonObject content;

  public JsonDocument(String id, JsonObject content) {
    this.id = id;
    this.content = content;
  }

  public String getId() {
    return id;
  }

  public JsonObject getContent() {
    return content;
  }

  @Override
  public String toString() {
    return "JsonDocument{id='" + id + "', content=" + content + "}";
  }
}
```

```java
public JsonDocument preprocess(Map row) {
  Map value = new HashMap(row);

  // define the KEY
  String key = value.get("type") + "_" + value.get("id");

  // do any additional processing
  value.put("importer", "Java SDK");
  
  return new JsonDocument(key, JsonObject.from(value));
}
```

Click the  View button to see any code sample in context.

For more information, see [Data Operations](../../../java-sdk/current/howtos/kv-operations.md).

To iterate the prepared data stream, use a `for` loop in the same way as an array.

```nodejs
const importStream = async (stream) => {
  for await (const doc of stream) {
    upsertDocument(doc)
  }
}
```

Hook the prepared stream in to an `upsertDocument` routine:

```nodejs
const upsertDocument = async (doc) => {
  try {
    // Build the key
    const key = `${doc.type}_${doc.id}`
    
    // Do any processing, logging etc.
    doc.importer = "import.js"
    console.log(key, doc)
    
    // Upsert the document
    await collection.upsert(key, doc)
  }
  catch (error) {
    // Error handling, retry, logging etc.
    console.error(error)
  }
}
```

Click the  View button to see any code sample in context.

For more information, see [Data Operations](../../../nodejs-sdk/current/howtos/kv-operations.md).

To store the data, define functions to determine the key, and process the value.

```python
def key(row):
    return "{type}_{id}".format(**row)
```

```python
def process(row):
    row["importer"] = "Python SDK"
    return row
```

Hook the prepared data into an `upsertDocument` routine which uses these functions.

```python
def upsert(row):
    k = key(row)
    v = process(row)
    print(k, v)
    collection.upsert(k, v)
```

For more information, see [Data Operations](../../../python-sdk/current/howtos/kv-operations.md).

The Python SDK offers a set of batch operations which are marked as volatile as of SDK 3.2.3, which may be more efficient. Here’s a brief example for CSV:

```python
# multi operations volatile as of SDK 3.2.3
def csv_import_multi(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = { key(row): process(row) for row in reader }
        print(data)
        collection.upsert_multi(data)
```

Click the  View button to see any code sample in context.

## [](#related-links)Related Links

Reference and information:

* The [Couchbase Server UI](../manage/import-documents/import-documents.md) offers a graphical view of documents, to check your imports interactively.

How-to guides:

* The [Key-Value Operations](kv-operations.md) guide shows how to read and update the data you have imported.

Key-Value Operations with SDKs:

* [C](../../../c-sdk/current/howtos/kv-operations.md)| [C++](../../../cxx-sdk/current/howtos/kv-operations.md)| [.NET](../../../dotnet-sdk/current/howtos/kv-operations.md)| [Go](../../../go-sdk/current/howtos/kv-operations.md)| [Java](../../../java-sdk/current/howtos/kv-operations.md)| [Kotlin](../../../kotlin-sdk/current/howtos/kv-operations.md)| [Node.js](../../../nodejs-sdk/current/howtos/kv-operations.md)| [PHP](../../../php-sdk/current/howtos/kv-operations.md)| [Python](../../../python-sdk/current/howtos/kv-operations.md)| [Ruby](../../../ruby-sdk/current/howtos/kv-operations.md)| [Scala](../../../scala-sdk/current/howtos/kv-operations.md)