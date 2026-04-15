---
title: Transactions Migration Guide
description: For those transitioning from using the Couchbase Transactions library for .NET.
editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.9/modules/project-docs/pages/distributed-acid-transactions-migration-guide.adoc
pubDate: 2026-04-15T05:26:28.652Z
link: xref:dotnet-sdk:project-docs:distributed-acid-transactions-migration-guide.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/current/project-docs/distributed-acid-transactions-migration-guide.html)

# Transactions Migration Guide

> For those transitioning from using the Couchbase Transactions library for .NET. 

Couchbase transactions for .NET were originally introduced as a library separate from the main Couchbase .NET SDK.

We subsequently chose to integrate transactions directly into the SDKs with the release of .NET SDK 3.3.0, to make it easier for users to get started.

This document details the small changes that existing users of the legacy transactions library need to make, to migrate to the SDK-integrated version.

The [legacy transactions library](https://docs-archive.couchbase.com/dotnet-sdk/3.2/project-docs/distributed-transactions-dotnet-release-notes.html) will continue to be supported with bugfixes for some time, but new transaction features will only be added to the SDK and it is recommended that all users migrate.

## [](#accessing-transactions)Accessing transactions

This is now done via a `Cluster` object. There is no longer any need to create a `Transactions` object.

Before

```csharp
var transactions = Transactions.Create(cluster);

await transactions.RunAsync(async (ctx) => {
    // Your transaction logic.
});
```

After

```csharp

var bucket = await cluster.BucketAsync("default").ConfigureAwait(false);
var collection = await bucket.ScopeAsync("inventory").CollectionAsync("airport").ConfigureAwait(false);

// Use the cluster's Transactions object
var transactions = cluster.Transactions;
```

## [](#configuration)Configuration

Configuration used to be performed when creating the `Transactions` object, and is now performed when creating the `Cluster` object.

Before

```csharp
var transactions = Transactions.Create(cluster,
    TransactionsConfigBuilder.Create()
      .DurabilityLevel(DurabilityLevel.PersistToMajority)
      .Build());
```

After

```csharp
var transactionsConfig = TransactionsConfigBuilder.Create()
    .DurabilityLevel(DurabilityLevel.PersistToMajority)
    .Build();
var options = new ClusterOptions()
{
    UserName = "Administrator",
    Password = "Administrator",
    TransactionsConfig = transactionsConfig,
};
var cluster = await Cluster.ConnectAsync("couchbase://your-ip", options).ConfigureAwait(false);
```

A few details of configuration change:

* `TransactionsConfigBuilder.MetadataCollection` takes a `Keyspace` instead of an `ICouchbaseCollection` (since a collection cannot be created at this point).
* `KeyValueTimeout` has been removed from `TransactionsConfig` and `TransactionOptions`.
* `TransactionDurabilityLevel` has been dropped in favour of using the SDK's `DurabilityLevel`.
* `TransactionOptions` now allows a `MetadataCollection` parameter.

### [](#cleanup-configuration)Cleanup configuration

Cleanup configuration options have been encapsulated into their own class:

Before

```csharp
var transactions = Transactions.Create(cluster,
    TransactionsConfigBuilder.Create()
      .CleanupConfig(TransactionCleanupConfigBuilder.Create()
        .CleanupClientAttempts(false)
        .CleanupLostAttempts(false)
        .CleanupWindow(TimeSpan.FromSeconds(30))
        .Build())
      .Build());
```

After

```csharp
var cleanupConfig = TransactionCleanupConfigBuilder.Create()
    .CleanupClientAttempts(false)
    .CleanupLostAttempts(false)
    .CleanupWindow(TimeSpan.FromSeconds(120))
    .Build();
var transactionsConfig =
    TransactionsConfigBuilder.Create()
        .CleanupConfig(cleanupConfig).Build();
var options = new ClusterOptions()
{
    UserName = "Administrator",
    Password = "Administrator",
    TransactionsConfig = transactionsConfig,
};
var cluster = await Cluster.ConnectAsync("couchbase://your-ip", options).ConfigureAwait(false);
```

## [](#lambda)Lambda

`ctx.CommitAsync()` has been removed from the public API, as it is redundant: commit automatically happens when the lambda successfully reaches the end.

`ctx.RollbackAsync()` has been removed from the public API, as it too is redundant: the application can throw any exception from the lambda to trigger a rollback.

## [](#package-changes)Package changes

All classes have changed namespaces to be compatible with the .NET SDK conventions.

The simplest way to convert many of the classes to their new locations is to search for `using Couchbase.Transactions;` and replace it with `using Couchbase.Client.Transactions;`.

Some additional manual conversion after this may be required.

## [](#single-query-transactions)Single query transactions

These are now integrated with the transactions object on the cluster.

Before

```csharp
SingleQueryTransactionResult sqr = await transactions.QueryAsync<dynamic>("INSERT...");
```

After

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

Or with configuration:

Before

```csharp
SingleQueryTransactionResult sqr = await transactions.QueryAsync<dynamic>("INSERT...",
  SingleQueryTransactionConfigBuilder.Create()
    // configure timeouts, durability etc
);
```

After

```csharp
// with the Builder pattern.
await transactions.QueryAsync<object>(bulkLoadStatement, SingleQueryTransactionConfigBuilder.Create()
    // Single query transactions will often want to increase the default timeout
    .ExpirationTime(TimeSpan.FromSeconds(360)));

// using the lambda style
await transactions.QueryAsync<object>(bulkLoadStatement, config => config.ExpirationTime(TimeSpan.FromSeconds(360)));
```

## [](#cleanup)Cleanup

This doesn't impact the API, but it is useful to know that lost cleanup has changed.

Previously, lost cleanup would look for expired transactions on the default collections of all buckets in the cluster. Unless a metadata collection was specified, in which case only that collection would be cleaned up.

Now, cleanup is dynamic. As transactions are run, the collection where metadata is created for that transaction, is added to what we call the 'cleanup set'. This is just the set of collections where cleanup, for this application, is looking for expired transactions.

The intent has always been that users without complex requirements should never need to think about or configure transaction cleanup, and this new dynamic cleanup allows us to be closer still to that goal.

## [](#naming)Naming

Exceptions and events have been renamed, if needed, to be compliant with the SDK.

## [](#logging)Logging

Failure logging remains largely the same, but note that `TransactionFailedException` contains a `Result` property which exposes the transaction `Logs`.

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

## [](#further-reading)Further Reading

* There's plenty of explanation about how Transactions work in Couchbase in our [Transactions documentation](../../../server/current/learn/data/transactions.md).
* The [.NET SDK transactions documentation](../howtos/distributed-acid-transactions-from-the-sdk.md).