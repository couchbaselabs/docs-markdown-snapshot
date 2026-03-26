---
title: Using Couchbase Transactions
description: A practical guide to using Couchbase's distributed ACID
  transactions, via the .NET SDK.
editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.6/modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.6@dotnet-sdk:howtos:distributed-acid-transactions-from-the-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/3.6/howtos/distributed-acid-transactions-from-the-sdk.html)

# Using Couchbase Transactions

> A practical guide to using Couchbase's distributed ACID transactions, via the .NET SDK. 

This guide will show you examples of how to perform multi-document ACID (atomic, consistent, isolated, and durable) database transactions within your application, using the Couchbase .NET SDK and transactions library.

Refer to the [Transaction Concepts](../concept-docs/transactions.md) page for a high-level overview.

## [](#prerequisites)Prerequisites

* Couchbase Capella
* Couchbase Server

* Couchbase Capella account.
* You should know how to perform [key-value](kv-operations.md) or [query](n1ql-queries-with-sdk.md) operations with the SDK.
* Your application should have the relevant roles and permissions on the required buckets, scopes, and collections, to perform transactional operations. Refer to the [Organizations & Access](../../../cloud/organizations/organization-projects-overview.md) page for more details.
* If your application is using [extended attributes (XATTRs)](../concept-docs/xattr.md), you should avoid using the XATTR field `txn` — this is reserved for Couchbase use.

* Couchbase Server (6.6.2 or above).
* You should know how to perform [key-value](kv-operations.md) or [query](n1ql-queries-with-sdk.md) operations with the SDK.
* Your application should have the relevant roles and permissions on the required buckets, scopes, and collections, to perform transactional operations. Refer to the [Roles](../../../server/7.6/learn/security/roles.md) page for more details.
* If your application is using [extended attributes (XATTRs)](../concept-docs/xattr.md), you should avoid using the XATTR field `txn` — this is reserved for Couchbase use.
* NTP should be configured so nodes of the Couchbase cluster are in sync with time.

> [!CAUTION]
> Single Node Cluster
> 
> When using a single node cluster (for example, during development), the default number of replicas for a newly created bucket is **1**. If left at this default, all key-value writes performed with durability will fail with a `DurabilityImpossibleException`. In turn, this will cause all transactions (which perform all key-value writes durably) to fail. This setting can be changed via:
> 
> * [Capella UI](../../../cloud/clusters/data-service/manage-buckets.md#add-bucket)
> * [Couchbase Server UI](../../../server/7.6/manage/manage-buckets/create-bucket.md#couchbase-bucket-settings)
> * [Command Line](../../../server/7.6/cli/cbcli/couchbase-cli-bucket-create.md#options)
> 
> If the bucket already exists, then the server needs to be rebalanced for the setting to take effect.

### [](#transactions-library)Transactions Library

Couchbase transactions require no additional components or services to be configured. Simply add the transactions library into your project. Version `1.1.0` was released October 29th, 2021.  
See the [Release Notes](../project-docs/distributed-transactions-dotnet-release-notes.md) for the latest version.

Installation

* NuGet
* CLI
* .csproj file

With NuGet this can be accomplished by using the NuGet Package Manager in your IDE:

PM > Install-Package Couchbase.Transactions -Version 1.1.0

You can also install the library with the dotnet CLI.

```console
$ dotnet add package Couchbase.Transactions --version 1.1.0
```

If you're using a .csproj file, add this `PackageReference`:

```xml
<PackageReference Include="Couchbase.Transactions" Version="1.1.0" />
```

## [](#creating-a-transaction)Creating a Transaction

The starting point is the `Transactions` object. It is very important that an application ensures that only one of these is created per cluster, as it performs automated background clean-up processes that should not be duplicated. In a dependency injection context, this instance should be injected as a singleton.

```csharp
// Initialize the Couchbase cluster
var options = new ClusterOptions().WithCredentials("Administrator", "password");
var cluster = await Cluster.ConnectAsync("couchbase://your-ip", options).ConfigureAwait(false);
var bucket = await cluster.BucketAsync("default").ConfigureAwait(false);
var collection = await bucket.ScopeAsync("inventory").CollectionAsync("airport").ConfigureAwait(false);

// Create the single Transactions object
var transactions = Transactions.Create(cluster, TransactionConfigBuilder.Create());
```

To create a transaction, an application must supply its logic inside a `lambda`, including any conditional logic required. Once the lambda has successfully run to conclusion, the transaction will be automatically committed. If at any point an error occurs, the transaction will rollback and the lambda may run again.

```csharp
try
{
    var result = await _transactions.RunAsync(async (ctx) =>
    {
        // Inserting a doc:
        var insertedDoc = await ctx.InsertAsync(_collection, "doc-a", new {}).ConfigureAwait(false);

        // Getting documents:
        // Use ctx.GetAsync if the document should exist, and the transaction
        // will fail if it does not
        var docA = await ctx.GetAsync(_collection, "doc-a").ConfigureAwait(false);

        // Replacing a doc:
        var docB = await ctx.GetAsync(_collection, "doc-b").ConfigureAwait(false);
        var content = docB.ContentAs<dynamic>();
        content.put("transactions", "are awesome");
        var replacedDoc = await ctx.ReplaceAsync(docB, content);

        // Removing a doc:
        var docC = await ctx.GetAsync(_collection, "doc-c").ConfigureAwait(false);
        await ctx.RemoveAsync(docC).ConfigureAwait(false);

        // This call is optional - if you leave it off, the transaction
        // will be committed anyway.
        await ctx.CommitAsync().ConfigureAwait(false);
    }).ConfigureAwait(false);
}
catch (TransactionCommitAmbiguousException e)
{
    Console.WriteLine("Transaction possibly committed");
    Console.WriteLine(e);
}
catch (TransactionFailedException e)
{
    Console.WriteLine("Transaction did not reach commit point");
    Console.WriteLine(e);
}
```

The transaction lambda gets passed an `AttemptContext` object — generally referred to as `ctx` in these examples. Since the lambda could be rerun multiple times, it is important that it does not contain any side effects. In particular, you should never perform regular operations on a `Collection`, such as `collection.InsertAsync()`, inside the lambda. Such operations may be performed multiple times, and will not be performed transactionally. Instead, you should perform these operations through the `ctx` object, e.g. `ctx.InsertAsync()`.

The result of a transaction is represented by a `TransactionResult` object, which can be used to expose debugging and logging information to help track what happened during a transaction.

> [!IMPORTANT]
> As with the Couchbase .NET Client, you should use the transactions library asynchronously using the async/await keywords. The asynchronous API allows you to use the thread pool, which can help you scale with excellent efficiency. However, operations inside an individual transaction should be kept in-order and executed using `await` immediately. Do not use fire-and-forget tasks under any circumstances.

In the event that a transaction fails, your application could run into the following errors:

* `TransactionCommitAmbiguousException`
* `TransactionFailedException`

Refer to [Error Handling](../concept-docs/transactions-error-handling.md#transaction%5Ferrors) for more details on these.

### [](#logging)Logging

To aid troubleshooting, each transaction maintains a list of log entries, which can be logged on failure like this:

```csharp
try
{
    var result = await transactions.RunAsync(async ctx => {
        // ... transactional code here ...
    });
}
catch (TransactionFailedException err)
{
    // ... log the error as you normally would
    // then include the logs
    foreach (var logLine in err.Result.Logs)
    {
        Console.Error.WriteLine(logLine);
    }
}
```

A failed transaction can involve dozens, even hundreds, of lines of logging, so it may be preferable to write failed transactions into a separate file.

Please see the [.NET SDK logging documentation](collecting-information-and-logging.md) for details.

Here is an example of configuring a `Microsoft.Extensions.Logging.ILoggingFactory`:

```csharp
//Logging dependencies
var services = new ServiceCollection();
services.AddLogging(builder =>
{
    builder.AddFile(AppContext.BaseDirectory);
    builder.AddConsole();
});
await using var provider = services.BuildServiceProvider();
var loggerFactory = provider.GetService<ILoggerFactory>();
var logger = loggerFactory.CreateLogger<Program>();

//create the transactions object and add the ILoggerFactory
var transactions = Transactions.Create(_cluster,
    TransactionConfigBuilder.Create().LoggerFactory(loggerFactory));
try
{
    var result = await transactions.RunAsync(async ctx => {
        // ... transactional code here ...
    });
}
catch (TransactionCommitAmbiguousException err)
{
    // The transaction may or may not have reached commit point
    logger.LogInformation("Transaction returned TransactionCommitAmbiguous and" +
                " may have succeeded, logs:");
    Console.Error.WriteLine(err);
}
catch (TransactionFailedException err)
{
    // The transaction definitely did not reach commit point
    logger.LogInformation("Transaction failed with TransactionFailed, logs:");
    Console.Error.WriteLine(err);
}
```

## [](#key-value-operations)Key-Value Operations

You can perform transactional database operations using familiar key-value CRUD methods:

* **C**reate - `InsertAsync()`
* **R**ead - `GetAsync()` or `GetOptionalAsync()`
* **U**pdate - `ReplaceAsync()`
* **D**elete - `RemoveAsync()`

> [!IMPORTANT]
> As mentioned [previously](#lambda-ops), make sure your application uses the transactional key-value operations inside the lambda — such as `ctx.InsertAsync()`, rather than `collection.InsertAsync()`.

### [](#insert)Insert

To insert a document within a transaction lambda, simply call `ctx.InsertAsync()`.

```csharp
await _transactions.RunAsync(async ctx =>
{
    var insertedDoc = await ctx.InsertAsync(_collection, "docId", new { }).ConfigureAwait(false);
}).ConfigureAwait(false);
```

### [](#get)Get

There are two ways to get a document, `GetAsync` and `GetOptionalAsync`:

```csharp
await _transactions.RunAsync(async ctx =>
{
    var docId = "a-doc";
    var docOpt = await ctx.GetAsync(_collection, docId).ConfigureAwait(false);
}).ConfigureAwait(false);
```

`GetAsync` may return a `TransactionFailedException` if a document doesn't exist, for example. It is provided as a convenience method, so a developer does not have to check for `null` if the document must exist for the transaction to succeed — which is the case with `GetAsyncOptional`.

Gets will "Read Your Own Writes", e.g. this will succeed:

```csharp
await _transactions.RunAsync(async ctx =>
{
    var docId = "docId";
    _ = await ctx.InsertAsync(_collection, docId, new { }).ConfigureAwait(false);
    var doc = await ctx.GetAsync(_collection, docId).ConfigureAwait(false);
    Console.WriteLine((object) doc.ContentAs<dynamic>());
}).ConfigureAwait(false);
```

Of course, no other transaction will be able to read that inserted document, until this transaction reaches the commit point.

### [](#replace)Replace

Replacing a document requires awaiting a `TransactionGetResult` returned from `ctx.GetAsync()`, `ctx.InsertAsync()`, or another `ctx.ReplaceAsync()` call first. This is necessary to ensure that the document is not involved in another transaction. If it is, then the transaction will handle this, generally by rolling back what has been done so far, and retrying the lambda.

```csharp
await _transactions.RunAsync(async ctx =>
{
    var anotherDoc = await ctx.GetAsync(_collection, "anotherDoc").ConfigureAwait(false);
    var content = anotherDoc.ContentAs<dynamic>();
    content.put("transactions", "are awesome");
    _ = await ctx.ReplaceAsync(anotherDoc, content);
}).ConfigureAwait(false);
```

### [](#remove)Remove

As with replaces, removing a document requires awaiting a `TransactionGetResult` from a previous transaction operation first.

```csharp
await _transactions.RunAsync(async ctx =>
{
    var anotherDoc = await ctx.GetAsync(_collection, "anotherDoc").ConfigureAwait(false);
    await ctx.RemoveAsync(anotherDoc).ConfigureAwait(false);
}).ConfigureAwait(false);
```

## [](#sql-queries)SQL++ Queries

If you already use [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql), then its use in transactions is very similar. A query returns the same `IQueryResult<T>` you are used to, and takes most of the same options.

> [!IMPORTANT]
> As mentioned [previously](#lambda-ops), make sure your application uses the transactional query operations inside the lambda — such as `ctx.QueryAsync()`, rather than `cluster.QueryAsync()` or `scope.QueryAsync()`.

Here is an example of selecting some rows from the `travel-sample` bucket:

```csharp
IBucket travelSample = await cluster.BucketAsync("travel-sample");
IScope inventory = travelSample.Scope("inventory");

var transactionResult = await transactions.RunAsync(async ctx =>
{
    var st = "SELECT * FROM `travel-sample`.inventory.hotel WHERE country = $1";
    IQueryResult<object> qr = await ctx.QueryAsync<object>(st,
        options: new TransactionQueryOptions().Parameter("United Kingdom"),
        scope: inventory);
});
```

An example using a `IScope` for an UPDATE:

```csharp
var hotelChain = "http://marriot%";
var country = "United States";

await transactions.RunAsync(async ctx => {
    var qr = await ctx.QueryAsync<object>(
        statement: "UPDATE hotel SET price = $price WHERE url LIKE $url AND country = $country",
        configure: options => options.Parameter("price", 99.99m)
                          .Parameter("url", hotelChain)
                          .Parameter("country", country),
        scope: inventory);

    Console.Out.WriteLine($"Records Updated = {qr?.MetaData.Metrics.MutationCount}");
});
```

And an example combining `SELECT` and `UPDATE`.

```csharp
await transactions.RunAsync(async ctx => {
    // Find all hotels of the chain
    IQueryResult<Review> qr = await ctx.QueryAsync<Review>(
        statement: "SELECT reviews FROM hotel WHERE url LIKE $1 AND country = $2",
        configure: options => options.Parameter(hotelChain).Parameter(country),
        scope: inventory);

    // This function (not provided here) will use a trained machine learning model to provide a
    // suitable price based on recent customer reviews.
    var updatedPrice = PriceFromRecentReviews(qr);

    // Set the price of all hotels in the chain
    await ctx.QueryAsync<object>(
        statement: "UPDATE hotel SET price = $1 WHERE url LIKE $2 AND country = $3",
            configure: options => options.Parameter(hotelChain, country, updatedPrice),
            scope: inventory);
});
```

As you can see from the snippet above, it is possible to call regular C# methods from the lambda, permitting complex logic to be performed. Just remember that since the lambda may be called multiple times, so may the method.

Like key-value operations, queries support "Read Your Own Writes". This example shows inserting a document and then selecting it again:

```csharp
await transactions.RunAsync(async ctx => {
    await ctx.QueryAsync<object>(
        "INSERT INTO `default` VALUES ('doc', {'hello':'world'})",
        TransactionQueryConfigBuilder.Create()
    );  (1)

    // Performing a 'Read Your Own Write'
    var st = "SELECT `default`.* FROM `default` WHERE META().id = 'doc'"; (2)
    IQueryResult<object> qr = await ctx.QueryAsync<object>(st, TransactionQueryConfigBuilder.Create());
    Console.Out.WriteLine($"ResultCount = {qr?.MetaData.Metrics.ResultCount}");
});
```

| **1** | The inserted document is only staged at this point, as the transaction has not yet committed.Other transactions, and other non-transactional actors, will not be able to see this staged insert yet. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | But the SELECT can, as we are reading a mutation staged inside the same transaction.                                                                                                                 |

### [](#query-options)Query Options

Query options can be provided via `TransactionQueryOptions` object:

```csharp
await transactions.RunAsync(async ctx => {
    await ctx.QueryAsync<object>("INSERT INTO `default` VALUES ('doc', {'hello':'world'})",
            new TransactionQueryOptions().FlexIndex(true));
});
```

__Table 1\. Supported Transaction Query Options__
| Name                                  | Description                                                                      |
| ------------------------------------- | -------------------------------------------------------------------------------- |
| Parameter(Object)                     | Allows to set positional arguments for a parameterized query.                    |
| Parameters(Object\[\])                | Allows you to set named arguments for a parameterized query.                     |
| ScanConsistency(QueryScanConsistency) | Sets a different scan consistency for this query.                                |
| FlexIndex(Boolean)                    | Tells the query engine to use a flex index (utilizing the search service).       |
| Serializer(ITypeSerializer)           | Allows to use a different serializer for the decoding of the rows.               |
| ClientContextId(String)               | Sets a context ID returned by the service for debugging purposes.                |
| ScanWait(TimeSpan)                    | Allows to specify a maximum scan wait time.                                      |
| ScanCap(Int32)                        | Specifies a maximum cap on the query scan size.                                  |
| PipelineBatch(Int32)                  | Sets the batch size for the query pipeline.                                      |
| PipelineCap(Int32)                    | Sets the cap for the query pipeline.                                             |
| Readonly(Boolean)                     | Tells the client and server that this query is readonly.                         |
| AdHoc(Boolean)                        | If set to false will prepare the query and later execute the prepared statement. |
| Raw(String, Object)                   | Escape hatch to add arguments that are not covered by these options.             |

## [](#mixing-key-value-and-sql)Mixing Key-Value and SQL++

Key-Value and SQL++ query operations can be freely intermixed, and will interact with each other as you would expect. In this example we insert a document with a key-value operation, and read it with a `SELECT` query.

```csharp
await transactions.RunAsync(async ctx => {
    _ = await ctx.InsertAsync(collection, "doc", new { Hello = "world" }); (1)

    // Performing a 'Read Your Own Write'
    var st = "SELECT `default`.* FROM `default` WHERE META().id = 'doc'"; (2)
    var qr = await ctx.QueryAsync<object>(st);
    Console.Out.WriteLine($"ResultCount = {qr?.MetaData.Metrics.ResultCount}");
});
```

| **1** | The key-value insert operation is only staged, and so it is not visible to other transactions or non-transactional actors. |
| ----- | -------------------------------------------------------------------------------------------------------------------------- |
| **2** | But the SELECT can view it, as the insert was in the same transaction.                                                     |

> [!IMPORTANT]
> Query Mode
> 
> When a transaction executes a query statement, the transaction enters **query mode**, which means that the query is executed with the user's query permissions. Any **key-value** operations which are executed by the transaction _after_ the query statement are _also_ executed with the user's query permissions. These may or may not be different to the user's data permissions; if they are different, you may get unexpected results.

## [](#configuration)Configuration

The default configuration should be appropriate for most use-cases. If needed, transactions can optionally be configured at the point of creating the `Transactions` object:

```csharp
var transactions = Transactions.Create(_cluster,
    TransactionConfigBuilder.Create()
        .DurabilityLevel(DurabilityLevel.PersistToMajority)
        .Build());
```

The default configuration will perform all writes with the durability setting `Majority`, ensuring that each write is available in-memory on the majority of replicas before the transaction continues. There are two higher durability settings available that will additionally wait for all mutations to be written to physical storage on either the active or the majority of replicas, before continuing. This further increases safety, at a cost of additional latency.

> [!CAUTION]
> A level of `None` is present but its use is discouraged and unsupported. If durability is set to `None`, then ACID semantics are not guaranteed.

## [](#additional-resources)Additional Resources

* Learn more about [Distributed ACID Transactions](../concept-docs/transactions.md).
* Check out the Couchbase Transactions library [API Reference](https://docs.couchbase.com/sdk-api/couchbase-transactions-dotnet/).