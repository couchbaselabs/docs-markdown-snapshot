---
title: Work with Documents in Bulk
description: How to perform bulk CRUD operations with a command line tool or an SDK.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/guides/pages/bulk-operations.adoc
pubDate: 2026-07-22T05:30:13.485Z
link: xref:server:guides:bulk-operations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/guides/bulk-operations.html)

# Work with Documents in Bulk

> How to perform bulk CRUD operations with a command line tool or an SDK. 

## [](#introduction)Introduction

Performing bulk operations with Couchbase Server can be done in several ways, depending on the SDK or command line tool used to perform them. This guide contains basic procedures for performing bulk CRUD operations on Couchbase documents.

Read the following for further information about the clients available:

* [Command Line Clients](../../../c-sdk/current/hello-world/cbc.md)
* [SDK Clients](../../../home/sdk.md)

> [!WARNING]
> Please note that the examples in this guide will alter the data in your sample database. To restore your sample data, remove and reinstall the travel sample data. Refer to [Sample Buckets](../manage/manage-settings/install-sample-buckets.md) for details.

## [](#creating-multiple-documents)Creating Multiple Documents

To create multiple documents in Couchbase perform a bulk insert operation.

* .NET
* Java
* Node.js
* Python

1. Create some structured JSON documents to insert.
2. Initialize a list of `IMutationResult` tasks.
3. Perform an insert operation on each document and store the result in the tasks list.
4. Wait for all the tasks to complete before accessing the results.

---

The example below inserts multiple JSON documents in the `users` keyspace in the `tenant_agent_00` scope.

```csharp
var documents = new[]
{
	new { id = "user_111", email = "tom_the_cat@gmail.com"},
	new { id = "user_222", email = "jerry_mouse@gmail.com"},
	new { id = "user_333", email = "mickey_mouse@gmail.com"}
};
	// Collection of things that will complete in the future.
	var tasks = new List<Task<IMutationResult>>();

	// Create tasks to be executed concurrently.
	foreach (var document in documents)
	{
		Console.WriteLine($"Inserting document: {document.id}");
		var task = usersCollection.InsertAsync(document.id, document);
		tasks.Add(task);
	}

	// Wait until all of the tasks have completed.
	await Task.WhenAll(tasks);

	// Iterate task list to get results.
	foreach (var task in tasks)
		Console.WriteLine($"CAS: {task.Result.Cas}");
```

Click the  View button to see this code in context.

For more information, see [CollectionExtensions](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.KeyValue.CollectionExtensions.html).

1. Create some structured JSON documents to insert.
2. Using the `reactor.core.publisher.Flux` reactive library, call the `fromIterable()` method to perform multiple insert operations.

The example below inserts multiple JSON documents in the `users` keyspace in the `tenant_agent_00` scope.

```java
JsonObject user1 = JsonObject.create().put("id", "user_111").put("email", "tom_the_cat@gmail.com");
JsonObject user2 = JsonObject.create().put("id", "user_222").put("email", "jerry_mouse@gmail.com");
JsonObject user3 = JsonObject.create().put("id", "user_333").put("email", "mickey_mouse@gmail.com");

List<JsonDocument> documents = Arrays.asList(
  new JsonDocument("user_111", user1),
  new JsonDocument("user_222", user2),
  new JsonDocument("user_333", user3)
);

// Iterate over a list of documents to insert.
List<MutationResult> results = Flux.fromIterable(documents)
    .flatMap(document -> reactiveCollection.insert(
        document.getId(), document.getContent()
      )
    )
    .collectList()
    .block(); // Wait until all operations have completed.

// Print all the results.
for (MutationResult result : results) {
  System.out.println("CAS: " + result.cas());
}
```

> [!NOTE]
> A `JsonDocument` class is used to supplement the example.

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

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Collection.html) and [Project Reactor](https://projectreactor.io/docs/core/release/api/reactor/core/publisher/Flux.html).

1. Create some structured JSON documents to insert.
2. Perform an insert operation on each document and wait for all the promises to complete before accessing the results.

---

The example below inserts multiple JSON documents in the `users` keyspace in the `tenant_agent_00` scope.

```nodejs
Unresolved include directive in modules/guides/pages/bulk-operations.adoc - include::nodejs-sdk:devguide:example$nodejs/kv-bulk-hello-world.js[]
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Collection.html).

1. Create a dictionary of structured JSON documents.
2. Pass the dictionary to the `insert_multi()` function. This will insert all the documents in the database.

A dictionary of `MutationResult` objects is returned.

> [!CAUTION]
> `CBCollection.insert_multi` is a [volatile](../../../python-sdk/current/project-docs/compatibility.md#interface-stability) API call that's still in flux and may likely be changed.

---

The example below inserts multiple JSON documents in the `users` keyspace in the `tenant_agent_00` scope.

```python
documents = {
    "user_111": {"id": "user_111", "email": "tom_the_cat@gmail.com"},
    "user_222": {"id": "user_222", "email": "jerry_mouse@gmail.com"},
    "user_333": {"id": "user_333", "email": "mickey_mouse@gmail.com"}
}
# Insert some documents in the users collection.
insert_results = users_collection.insert_multi(documents)

# Print each document's CAS metadata to the console.
for key in documents:
    print("Inserted Document:", key)
    print("CAS:", insert_results[key].cas)
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#collection-object).

## [](#reading-multiple-documents)Reading Multiple Documents

To read multiple documents in Couchbase perform a bulk `get` operation.

* cbc
* .NET
* Java
* Node.js
* Python

Use the `cbc cat` command to retrieve multiple documents by their IDs.

---

The example below fetches multiple JSON documents from the `users` keyspace in the `tenant_agent_00` scope.

```shell
cbc cat -u Administrator -P password -U couchbase://localhost/travel-sample \
	--scope='tenant_agent_00' \
	--collection='users' \
	0 1
```

Result

```console
0                    CAS=0x16be2392ca2e0000, Flags=0x0, Size=904, Datatype=0x01(JSON)
{
  "name": "Keon Hoppe",
  "addresses": [
    {
      "type": "home",
      "address": "222 Sauer Neck",
      "city": "London",
      "country": "United Kingdom"
    },
  ],
  ...
}
1                    CAS=0x16be2392c9870000, Flags=0x0, Size=697, Datatype=0x01(JSON)
{
  "name": "Rigoberto Bernier",
  "addresses": [
    {
      "type": "home",
      "address": "0622 Adams Mills",
      "city": "Manchester",
      "country": "United Kingdom"
    }
  ],
  ...
}
```

For further details, refer to [cbc(1)](https://docs.couchbase.com/sdk-api/couchbase-c-client/md%5Fdoc%5F2cbc.html).

1. Initialize a list of `IGetResult` tasks.
2. Perform a `get` operation on each document and store the results in the tasks list.
3. Wait for all the tasks to complete before accessing the results.

---

The example below fetches multiple JSON documents from the `users` keyspace in the `tenant_agent_00` scope.

```csharp
var documents = new[]
{
	new { id = "user_111", email = "tom_the_cat@gmail.com"},
	new { id = "user_222", email = "jerry_mouse@gmail.com"},
	new { id = "user_333", email = "mickey_mouse@gmail.com"}
};
	// Collection of things that will complete in the future.
	var tasks = new List<Task<IGetResult>>();

	// Create tasks to be executed concurrently.
	foreach (var document in documents)
	{
		Console.WriteLine($"Getting document: {document.id}");
		var task = usersCollection.GetAsync(document.id);
		tasks.Add(task);
	}

	// Wait until all of the tasks have completed.
	await Task.WhenAll(tasks);

	// Iterate task list to get results.
	foreach (var task in tasks)
		Console.WriteLine($"Document: {task.Result.ContentAs<dynamic>()}");
```

Click the  View button to see this code in context.

For more information, see [CollectionExtensions](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.KeyValue.CollectionExtensions.html).

Using the `reactor.core.publisher.Flux` reactive library, call the `fromIterable()` method to perform multiple `get` operations.

---

The example below fetches multiple JSON documents from the `users` keyspace in the `tenant_agent_00` scope.

```java
JsonObject user1 = JsonObject.create().put("id", "user_111").put("email", "tom_the_cat@gmail.com");
JsonObject user2 = JsonObject.create().put("id", "user_222").put("email", "jerry_mouse@gmail.com");
JsonObject user3 = JsonObject.create().put("id", "user_333").put("email", "mickey_mouse@gmail.com");

List<JsonDocument> documents = Arrays.asList(
  new JsonDocument("user_111", user1),
  new JsonDocument("user_222", user2),
  new JsonDocument("user_333", user3)
);

// Iterate over a list of documents to fetch.
List<GetResult> results = Flux.fromIterable(documents)
    .flatMap(document -> reactiveCollection.get(document.getId()))
    .collectList()
    .block(); // Wait until all operations have completed.

// Print all the results.
for (GetResult result : results) {
  JsonObject document = result.contentAsObject();
  System.out.println("Document: "  + document);
  System.out.println("CAS: " + result.cas());
}
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Collection.html) and [Project Reactor](https://projectreactor.io/docs/core/release/api/reactor/core/publisher/Flux.html).

Perform a `get` operation on each document and wait for all the promises to complete before accessing the results.

---

The example below fetches multiple JSON documents from the `users` keyspace in the `tenant_agent_00` scope.

```nodejs
Unresolved include directive in modules/guides/pages/bulk-operations.adoc - include::nodejs-sdk:devguide:example$nodejs/kv-bulk-hello-world.js[]
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Collection.html).

Pass some document IDs to fetch to the `get_multi()` function. This will fetch the documents from the database.

A dictionary of `GetResult` objects is returned.

> [!CAUTION]
> `CBCollection.get_multi` is a [volatile](../../../python-sdk/current/project-docs/compatibility.md#interface-stability) API call that's still in flux and may likely be changed.

---

The example below fetches multiple JSON documents from the `users` keyspace in the `tenant_agent_00` scope.

```python
documents = {
    "user_111": {"id": "user_111", "email": "tom_the_cat@gmail.com"},
    "user_222": {"id": "user_222", "email": "jerry_mouse@gmail.com"},
    "user_333": {"id": "user_333", "email": "mickey_mouse@gmail.com"}
}
# Get some documents from the users collection.
get_results = users_collection.get_multi(documents.keys())

# Print each document's CAS metadata to the console.
for key in documents:
    print("Fetched Document:", key)
    print("CAS:", get_results[key].cas)
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#collection-object).

## [](#updating-multiple-documents)Updating Multiple Documents

To update multiple documents in Couchbase perform a bulk upsert or replace operation.

* .NET
* Java
* Node.js
* Python

1. Add new data to update some existing JSON documents.
2. Initialize a list of `IMutationResult` tasks.
3. Perform an upsert or replace operation on each document and store the results in the tasks list.
4. Wait for all the tasks to complete before accessing the results.

---

The example below inserts multiple JSON documents in the `users` keyspace in the `tenant_agent_00` scope.

```csharp
var documents = new[]
{
	new { id = "user_111", email = "tom_the_cat@gmail.com"},
	new { id = "user_222", email = "jerry_mouse@gmail.com"},
	new { id = "user_333", email = "mickey_mouse@gmail.com"}
};
	// Collection of things that will complete in the future.
	var tasks = new List<Task<IMutationResult>>();

	// Create tasks to be executed concurrently.
	foreach (var document in documents)
	{
		Console.WriteLine($"Inserting document: {document.id}");
		var task = usersCollection.InsertAsync(document.id, document);
		tasks.Add(task);
	}

	// Wait until all of the tasks have completed.
	await Task.WhenAll(tasks);

	// Iterate task list to get results.
	foreach (var task in tasks)
		Console.WriteLine($"CAS: {task.Result.Cas}");
```

Click the  View button to see this code in context.

For more information, see [CollectionExtensions](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.KeyValue.CollectionExtensions.html).

1. Add new data to update some existing JSON documents.
2. Using the `reactor.core.publisher.Flux` reactive library, call the `fromIterable()` method to perform multiple upsert or replace operations.

---

The example below upserts multiple JSON documents in the `users` keyspace in the `tenant_agent_00` scope.

```java
JsonObject user1 = JsonObject.create().put("id", "user_111").put("email", "tom_the_cat@gmail.com");
JsonObject user2 = JsonObject.create().put("id", "user_222").put("email", "jerry_mouse@gmail.com");
JsonObject user3 = JsonObject.create().put("id", "user_333").put("email", "mickey_mouse@gmail.com");

List<JsonDocument> documents = Arrays.asList(
  new JsonDocument("user_111", user1),
  new JsonDocument("user_222", user2),
  new JsonDocument("user_333", user3)
);

JsonObject newUser1 = JsonObject.create().put("id", "user_111").put("email", "tom@gmail.com");
JsonObject newUser2 = JsonObject.create().put("id", "user_222").put("email", "jerry@gmail.com");
JsonObject newUser3 = JsonObject.create().put("id", "user_333").put("email", "mickey@gmail.com");

List<JsonDocument> newDocuments = Arrays.asList(
  new JsonDocument("user_111", newUser1),
  new JsonDocument("user_222", newUser2),
  new JsonDocument("user_333", newUser3)
);

// Iterate over a list of documents to upsert.
List<MutationResult> results = Flux.fromIterable(newDocuments)
    .flatMap(newDocument -> reactiveCollection.upsert(
        newDocument.getId(), newDocument.getContent()
      )
    )
    .collectList()
    .block(); // Wait until all operations have completed.

// Print all the results.
for (MutationResult result : results) {
  System.out.println("CAS: " + result.cas());
}
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Collection.html) and [Project Reactor](https://projectreactor.io/docs/core/release/api/reactor/core/publisher/Flux.html).

1. Add new data to update some existing JSON documents.
2. Perform an upsert operation on each document and wait for all the promises to complete before accessing the results.

---

The example below upserts multiple JSON documents in the `users` keyspace in the `tenant_agent_00` scope.

```nodejs
Unresolved include directive in modules/guides/pages/bulk-operations.adoc - include::nodejs-sdk:devguide:example$nodejs/kv-bulk-hello-world.js[]
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Collection.html).

1. Add new data to update some existing JSON documents.
2. Pass the new document data to `upsert_multi()`. This will update all the documents in the database.

A dictionary of `MutationResult` objects is returned.

> [!CAUTION]
> `CBCollection.upsert_multi` is a [volatile](../../../python-sdk/current/project-docs/compatibility.md#interface-stability) API call that's still in flux and may likely be changed.

---

The example below upserts multiple JSON documents in the `users` keyspace in the `tenant_agent_00` scope.

```python
documents = {
    "user_111": {"id": "user_111", "email": "tom_the_cat@gmail.com"},
    "user_222": {"id": "user_222", "email": "jerry_mouse@gmail.com"},
    "user_333": {"id": "user_333", "email": "mickey_mouse@gmail.com"}
}
# Upsert some documents in the users collection.
upsert_results = users_collection.upsert_multi(documents)

# Print each document's CAS metadata to the console.
for key in documents:
    print("Upserted Document:", key)
    print("CAS:", upsert_results[key].cas)
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#collection-object).

## [](#deleting-multiple-documents)Deleting Multiple Documents

To delete multiple documents in Couchbase perform a bulk remove operation.

* .NET
* Java
* Node.js
* Python

1. Initialize a list of tasks.
2. Perform a remove operation on each document and store the results in the tasks list.
3. Wait for all the tasks to complete.

---

The example below deletes multiple JSON documents from the `users` keyspace in the `tenant_agent_00` scope.

```csharp
var documents = new[]
{
	new { id = "user_111", email = "tom_the_cat@gmail.com"},
	new { id = "user_222", email = "jerry_mouse@gmail.com"},
	new { id = "user_333", email = "mickey_mouse@gmail.com"}
};
	// Collection of things that will complete in the future.
	var tasks = new List<Task>();

	// Create tasks to be executed concurrently.
	foreach (var document in documents)
	{
		Console.WriteLine($"Removing document: {document.id}");
		var task = usersCollection.RemoveAsync(document.id);
		tasks.Add(task);
	}

	// Wait until all of the tasks have completed.
	// NOTE: RemoveAsync returns void, so no need to loop through each task.
	await Task.WhenAll(tasks);
```

Click the  View button to see this code in context.

For more information, see [CollectionExtensions](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.KeyValue.CollectionExtensions.html).

Using the `reactor.core.publisher.Flux` reactive library, call the `fromIterable()` method to perform multiple remove operations.

---

The example below deletes multiple JSON documents from the `users` keyspace in the `tenant_agent_00` scope.

```java
JsonObject user1 = JsonObject.create().put("id", "user_111").put("email", "tom_the_cat@gmail.com");
JsonObject user2 = JsonObject.create().put("id", "user_222").put("email", "jerry_mouse@gmail.com");
JsonObject user3 = JsonObject.create().put("id", "user_333").put("email", "mickey_mouse@gmail.com");

List<JsonDocument> documents = Arrays.asList(
  new JsonDocument("user_111", user1),
  new JsonDocument("user_222", user2),
  new JsonDocument("user_333", user3)
);

// Iterate over a list of documents to remove.
List<MutationResult> results = Flux.fromIterable(documents)
    .flatMap(document -> reactiveCollection.remove(document.getId()))
    .collectList()
    .block(); // Wait until all operations have completed.

// Print all the results.
for (MutationResult result : results) {
  System.out.println("CAS: " + result.cas());
}
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Collection.html) and [Project Reactor](https://projectreactor.io/docs/core/release/api/reactor/core/publisher/Flux.html).

Perform a remove operation on each document and wait for all the promises to complete before accessing the results.

---

The example below deletes multiple JSON documents from the `users` keyspace in the `tenant_agent_00` scope.

```nodejs
Unresolved include directive in modules/guides/pages/bulk-operations.adoc - include::nodejs-sdk:devguide:example$nodejs/kv-bulk-hello-world.js[]
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Collection.html).

Pass the document IDs to remove to the `remove_multi()` function. This will delete the documents from the database.

A dictionary of `MutationResult` objects is returned.

> [!CAUTION]
> `CBCollection.remove_multi` is a [volatile](../../../python-sdk/current/project-docs/compatibility.md#interface-stability) API call that's still in flux and may likely be changed.

---

The example below deletes multiple JSON documents from the `users` keyspace in the `tenant_agent_00` scope.

```python
documents = {
    "user_111": {"id": "user_111", "email": "tom_the_cat@gmail.com"},
    "user_222": {"id": "user_222", "email": "jerry_mouse@gmail.com"},
    "user_333": {"id": "user_333", "email": "mickey_mouse@gmail.com"}
}
# Remove some documents from the users collection.
remove_results = users_collection.remove_multi(documents.keys())

# Print each document's CAS metadata to the console.
for key in documents:
    print("Removed Document:", key)
    print("CAS:", remove_results[key].cas)
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#collection-object).

## [](#related-links)Related Links

Bulk Operations with SDKs:

* [C](../../../c-sdk/current/howtos/concurrent-async-apis.md)| [C++](../../../cxx-sdk/current/howtos/concurrent-async-apis.md)| [.NET](../../../dotnet-sdk/current/howtos/concurrent-async-apis.md)| [Go](../../../go-sdk/current/howtos/concurrent-async-apis.md)| [Java](../../../java-sdk/current/howtos/concurrent-async-apis.md)| [Kotlin](../../../kotlin-sdk/current/howtos/kv-operations.md#bulk)| [Node.js](../../../nodejs-sdk/current/howtos/concurrent-async-apis.md)| [PHP](../../../php-sdk/current/howtos/concurrent-async-apis.md)| [Python](../../../python-sdk/current/howtos/concurrent-async-apis.md)| [Ruby](../../../ruby-sdk/current/howtos/concurrent-async-apis.md)| [Rust](../../../rust-sdk/current/howtos/concurrent-async-apis.md)| [Scala](../../../scala-sdk/current/howtos/concurrent-async-apis.md)