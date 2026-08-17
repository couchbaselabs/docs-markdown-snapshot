---
title: Work with Documents in Bulk
description: How to perform bulk CRUD operations with a command line tool or an SDK.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/guides/pages/bulk-operations.adoc
  xref: xref:cloud:guides:bulk-operations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/guides/bulk-operations.html)

# Work with Documents in Bulk

> How to perform bulk CRUD operations with a command line tool or an SDK. 

## [](#introduction)Introduction

Performing bulk operations with Couchbase Capella can be done in several ways, depending on the SDK or command line tool used to perform them. This guide contains basic procedures for performing bulk CRUD operations on documents.

Read the following for further information about the clients available:

* [Couchbase Shell (cbsh)](https://couchbase.sh/docs/)
* [SDK Clients](../../home/sdk.md)

> [!WARNING]
> Please note that the examples in this guide will alter the data in your sample database. To restore your sample data, remove and reinstall the travel sample data. Refer to [Import Data with the Capella UI](../clusters/data-service/import-data-documents.md) for details.

## [](#creating-multiple-documents)Creating Multiple Documents

To create multiple documents, perform a bulk insert operation.

* cbsh
* .NET
* Java
* Node.js
* Python

1. If you have not already done so, use `cb-env` to set the bucket, scope, and collection in which to store the documents.
2. Create an array of structured documents to insert.
3. Pipe each item through the `wrap` filter to wrap it in a `content` field.
4. Pipe each item through the `insert` filter to add an `id` field with a unique value: for example, by copying a unique field from the content.
5. Pipe the output through the `doc insert` command to create the documents.

---

The example below inserts multiple JSON documents in the `users` keyspace in the `tenant_agent_00` scope.

```sh
cb-env bucket travel-sample
cb-env scope tenant_agent_00
cb-env collection users

[
  {id: "user_111", email: "tom_the_cat@example.com"},
  {id: "user_222", email: "jerry_mouse@example.com"},
  {id: "user_333", email: "mickey_mouse@example.com"}
] | wrap content | insert id { |this| echo $this.content.id } | doc insert
```

Result

```console
╭───┬───────────┬─────────┬────────┬──────────┬─────────╮
│ # │ processed │ success │ failed │ failures │ cluster │
├───┼───────────┼─────────┼────────┼──────────┼─────────┤
│ 0 │         3 │       3 │      0 │          │ capella │
╰───┴───────────┴─────────┴────────┴──────────┴─────────╯
```

For more information, see [Mutating](https://couchbase.sh/docs/#%5Fmutating) in the Couchbase Shell documentation.

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
Unresolved include directive in modules/guides/pages/bulk-operations.adoc - include::nodejs-sdk:hello-world:example$kv-bulk-hello-world.js[]
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Collection.html).

1. Create a dictionary of structured JSON documents.
2. Pass the dictionary to the `insert_multi()` function. This will insert all the documents in the database.

A dictionary of `MutationResult` objects is returned.

> [!CAUTION]
> `CBCollection.insert_multi` is a [volatile](../../python-sdk/current/project-docs/compatibility.md#interface-stability) API call that's still in flux and may likely be changed.

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

To read multiple documents, perform a bulk `get` operation.

* cbsh
* .NET
* Java
* Node.js
* Python

1. If you have not already done so, use `cb-env` to set the bucket, scope, and collection where the documents are stored.
2. Create an array of document IDs.
3. Pipe each document ID through the `wrap` filter to wrap it in an `id` field.
4. Pipe the output through the `doc get` command to retrieve multiple documents by their IDs.

---

The example below fetches multiple JSON documents from the `users` keyspace in the `tenant_agent_00` scope.

```sh
cb-env bucket travel-sample
cb-env scope tenant_agent_00
cb-env collection users

['0' '1'] | wrap id | doc get
```

Result

```console
╭───┬────┬────────────────────┬─────────────────────┬───────┬─────────╮
│ # │ id │      content       │         cas         │ error │ cluster │
├───┼────┼────────────────────┼─────────────────────┼───────┼─────────┤
│ 0 │ 1  │ {record 11 fields} │ 1717505682500419584 │       │ capella │
│ 1 │ 0  │ {record 11 fields} │ 1717505682774949888 │       │ capella │
╰───┴────┴────────────────────┴─────────────────────┴───────┴─────────╯
```

For more information, see [Reading](https://couchbase.sh/docs/#%5Freading) in the Couchbase Shell documentation.

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
Unresolved include directive in modules/guides/pages/bulk-operations.adoc - include::nodejs-sdk:hello-world:example$kv-bulk-hello-world.js[]
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Collection.html).

Pass some document IDs to fetch to the `get_multi()` function. This will fetch the documents from the database.

A dictionary of `GetResult` objects is returned.

> [!CAUTION]
> `CBCollection.get_multi` is a [volatile](../../python-sdk/current/project-docs/compatibility.md#interface-stability) API call that's still in flux and may likely be changed.

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

To update multiple documents, perform a bulk upsert or replace operation.

* cbsh
* .NET
* Java
* Node.js
* Python

1. If you have not already done so, use `cb-env` to set the bucket, scope, and collection where the documents are stored.
2. Create an array of updated structured documents.
3. Pipe each item through the `wrap` filter to wrap it in a `content` field.
4. Pipe each item through the `insert` filter to add an `id` field with a unique value: for example, by copying a unique field from the content.
5. Pipe the output through the `doc upsert` or `doc replace` command to update the documents.

---

The example below upserts multiple JSON documents in the `users` keyspace in the `tenant_agent_00` scope.

```sh
cb-env bucket travel-sample
cb-env scope tenant_agent_00
cb-env collection users

[
  {id: "user_111", email: "tom@example.com"},
  {id: "user_222", email: "jerry@example.com"},
  {id: "user_333", email: "mickey@example.com"}
] | wrap content | insert id { |this| echo $this.content.id } | doc upsert
```

Result

```console
╭───┬───────────┬─────────┬────────┬──────────┬─────────╮
│ # │ processed │ success │ failed │ failures │ cluster │
├───┼───────────┼─────────┼────────┼──────────┼─────────┤
│ 0 │         3 │       3 │      0 │          │ capella │
╰───┴───────────┴─────────┴────────┴──────────┴─────────╯
```

For more information, see [Mutating](https://couchbase.sh/docs/#%5Fmutating) in the Couchbase Shell documentation.

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
Unresolved include directive in modules/guides/pages/bulk-operations.adoc - include::nodejs-sdk:hello-world:example$kv-bulk-hello-world.js[]
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Collection.html).

1. Add new data to update some existing JSON documents.
2. Pass the new document data to `upsert_multi()`. This will update all the documents in the database.

A dictionary of `MutationResult` objects is returned.

> [!CAUTION]
> `CBCollection.upsert_multi` is a [volatile](../../python-sdk/current/project-docs/compatibility.md#interface-stability) API call that's still in flux and may likely be changed.

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

To delete multiple documents, perform a bulk remove operation.

* cbsh
* .NET
* Java
* Node.js
* Python

1. If you have not already done so, use `cb-env` to set the bucket, scope, and collection where the documents are stored.
2. Create an array of document IDs.
3. Pipe each document ID through the `wrap` filter to wrap it in an `id` field.
4. Pipe the output through the `doc remove` command to delete multiple documents by their IDs.

---

The example below deletes multiple JSON documents from the `users` keyspace in the `tenant_agent_00` scope.

```sh
cb-env bucket travel-sample
cb-env scope tenant_agent_00
cb-env collection users

[user_111 user_222 user_333] | wrap id | doc remove
```

Result

```console
╭───┬───────────┬─────────┬────────┬──────────┬─────────╮
│ # │ processed │ success │ failed │ failures │ cluster │
├───┼───────────┼─────────┼────────┼──────────┼─────────┤
│ 0 │         3 │       3 │      0 │          │ capella │
╰───┴───────────┴─────────┴────────┴──────────┴─────────╯
```

For more information, see [Removing](https://couchbase.sh/docs/#%5Fremoving) in the Couchbase Shell documentation.

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
Unresolved include directive in modules/guides/pages/bulk-operations.adoc - include::nodejs-sdk:hello-world:example$kv-bulk-hello-world.js[]
```

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Collection.html).

Pass the document IDs to remove to the `remove_multi()` function. This will delete the documents from the database.

A dictionary of `MutationResult` objects is returned.

> [!CAUTION]
> `CBCollection.remove_multi` is a [volatile](../../python-sdk/current/project-docs/compatibility.md#interface-stability) API call that's still in flux and may likely be changed.

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

* [C](../../c-sdk/current/howtos/concurrent-async-apis.md)| [C++](../../cxx-sdk/current/howtos/concurrent-async-apis.md)| [.NET](../../dotnet-sdk/current/howtos/concurrent-async-apis.md)| [Go](../../go-sdk/current/howtos/concurrent-async-apis.md)| [Java](../../java-sdk/current/howtos/concurrent-async-apis.md)| [Kotlin](../../kotlin-sdk/current/howtos/kv-operations.md#bulk)| [Node.js](../../nodejs-sdk/current/howtos/concurrent-async-apis.md)| [PHP](../../php-sdk/current/howtos/concurrent-async-apis.md)| [Python](../../python-sdk/current/howtos/concurrent-async-apis.md)| [Ruby](../../ruby-sdk/current/howtos/concurrent-async-apis.md)| Rust | [Scala](../../scala-sdk/current/howtos/concurrent-async-apis.md)