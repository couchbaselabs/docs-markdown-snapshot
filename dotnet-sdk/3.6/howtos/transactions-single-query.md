---
title: Single Query Transactions
description: Learn how to perform bulk-loading transactions with the SDK.
editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.6/modules/howtos/pages/transactions-single-query.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:3.6@dotnet-sdk:howtos:transactions-single-query.adoc[]
---

[View original HTML](/dotnet-sdk/3.6/howtos/transactions-single-query.html)

# Single Query Transactions

> Learn how to perform bulk-loading transactions with the SDK. 

Single query transactions can be useful if you need to do large, bulk-loading transactions.

The Query service maintains where required some in-memory state for each document in a transaction, that is freed on commit or rollback. For most use-cases this presents no issue, but there are some workloads, such as bulk loading many documents, where this could exceed the server resources allocated to the service. Solutions to this include breaking the workload up into smaller batches, and allocating additional memory to the Query service. Alternatively, single query transaction, described here, may be used.

Single query transactions have these characteristics:

* They have greatly reduced memory usage inside the Query service.
* As the name suggests, they consist of exactly one query, and no key-value operations.

You will see reference elsewhere in Couchbase documentation to the `tximplicit` query parameter. Single query transactions internally are setting this parameter. In addition, they provide automatic error and retry handling.

```csharp
var bulkLoadStatement = "<a bulk-loading N1QL statement>";

try
{
    SingleQueryTransactionResult<object> result = await transactions.QueryAsync<object>(bulkLoadStatement);

    IQueryResult<object> queryResult = result.QueryResult;
}
catch (TransactionCommitAmbiguousException e)
{
    Console.Error.WriteLine("Transaction possibly committed");
    foreach (var log in e.Result.Logs)
    {
        Console.Error.WriteLine(log);
    }
}
catch (TransactionFailedException e)
{
    Console.Error.WriteLine("Transaction did not reach commit point");
    foreach (var log in e.Result.Logs)
    {
        Console.Error.WriteLine(log);
    }
}
```

You can also run a single query transaction against a particular `IScope` (these examples will exclude the full error handling for brevity):

```csharp
IBucket travelSample = await cluster.BucketAsync("travel-sample");
IScope inventory = travelSample.Scope("inventory");

await transactions.QueryAsync<object>(bulkLoadStatement, scope: inventory);
```

and configure it:

```csharp
// with the Builder pattern.
await transactions.QueryAsync<object>(bulkLoadStatement, SingleQueryTransactionConfigBuilder.Create()
    // Single query transactions will often want to increase the default timeout
    .ExpirationTime(TimeSpan.FromSeconds(360)));

// using the lambda style
await transactions.QueryAsync<object>(bulkLoadStatement, config => config.ExpirationTime(TimeSpan.FromSeconds(360)));
```