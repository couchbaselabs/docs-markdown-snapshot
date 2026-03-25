---
title: Transactions Migration Guide
description: For those transitioning from using the Couchbase Transactions library for Java.
editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.9/modules/project-docs/pages/distributed-acid-transactions-migration-guide.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:dotnet-sdk:project-docs:distributed-acid-transactions-migration-guide.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/current/project-docs/distributed-acid-transactions-migration-guide.html)

# Transactions Migration Guide

> For those transitioning from using the Couchbase Transactions library for Java. 

Couchbase transactions for Java were originally introduced as a library separate from the Couchbase Java SDK.

We subsequently chose to integrate transactions directly into the SDKs with the release of Java SDK 3.3.0, to make it easier for users to get started.

This document details the small changes that existing users of the legacy transactions library need to make, to migrate to the SDK-integrated version.

The [legacy transactions library](https://docs-archive.couchbase.com/java-sdk/3.2/project-docs/distributed-transactions-java-release-notes.html) will continue to be supported with bugfixes for some time, but new transaction features will only be added to the SDK and it is recommended that all users migrate.

## [](#accessing-transactions)Accessing transactions

This is now done via a `Cluster` object. There is no longer any need to create a `Transactions` object.

Before

```java
var transactions = Transactions.create(cluster);

transactions.run((ctx) -> {
    // Your transaction logic.
});
```

After

```java
Unresolved include directive in modules/project-docs/pages/distributed-acid-transactions-migration-guide.adoc - include::devguide:example$java/TransactionsMigration.java[]
```

## [](#configuration)Configuration

Configuration used to be performed when creating the `Transactions` object, and is now performed when creating the `Cluster` object.

Before

```java
var transactions =
  Transactions.create(cluster,
    TransactionConfigBuilder.
      .durabilityLevel(TransactionDurabilityLevel.MAJORITY)
      .metadataCollection(collection));
```

After

```java
Unresolved include directive in modules/project-docs/pages/distributed-acid-transactions-migration-guide.adoc - include::devguide:example$java/TransactionsMigration.java[]
```

A few details of configuration change:

* `TransactionsConfig::metadataCollection` takes a `TransactionKeyspace` instead of a `Collection` (since a `Collection` cannot be created at this point).
* `keyValueTimeout` has been removed from `TransactionsConfig` and `TransactionOptions`.
* `TransactionDurabilityLevel` has been dropped in favour of using the SDK’s `DurabilityLevel`.
* `TransactionOptions` now allows a `metadataCollection` parameter.

And certain classes have been renamed to be compliant with the Java SDK:

| Before                              | After                         |  |
| ----------------------------------- | ----------------------------- |  |
| TransactionConfigBuilder            | TransactionsConfig            |  |
| TransactionQueryConfigBuilder       | TransactionsQueryConfig       |  |
| SingleQueryTransactionConfigBuilder | SingleQueryTransactionOptions |  |
| PerTransactionConfigBuilder         | TransactionOptions            |  |

### [](#cleanup-configuration)Cleanup configuration

Cleanup configuration options have been encapsulated into their own class:

Before

```java
var transactions =
  Transactions.create(cluster,
    TransactionConfigBuilder.create()
      .cleanupClientAttempts(false)
      .cleanupLostAttempts(false)
      .cleanupWindow(Duration.ofSeconds(30)));
```

After

```java
Unresolved include directive in modules/project-docs/pages/distributed-acid-transactions-migration-guide.adoc - include::devguide:example$java/TransactionsMigration.java[]
```

## [](#lambda)Lambda

`ctx.commit()` has been removed, as it is redundant: commit automatically happens when the lambda successfully reaches the end.

`ctx.rollback()` has been removed, as it too is redundant: the application can throw any exception from the lambda to trigger a rollback.

`ctx.getOptional()` has been replaced with `ctx.get()` throwing a `DocumentExistsException`. This may be caught, allowing the transaction to continue.

## [](#package-changes)Package changes

All classes have changed packages to be compatible with the Java SDK conventions.

The simplest way to convert many of the classes to their new locations is to search for `import com.couchbase.transactions.` and replace it with `import com.couchbase.client.java.transactions.`.

Some additional manual conversion after this may be required.

## [](#single-query-transactions)Single query transactions

These are now integrated with the existing SDK `QueryOptions`.

Before

```java
SingleQueryTransactionResult sqr = transactions.query("INSERT...");
```

After

```java
Unresolved include directive in modules/project-docs/pages/distributed-acid-transactions-migration-guide.adoc - include::devguide:example$java/TransactionsMigration.java[]
```

Or with configuration:

Before

```java
SingleQueryTransactionResult sqr = transactions.query("INSERT...",
  SingleQueryTransactionConfigBuilder.create()
    .durabilityLevel(TransactionDurabilityLevel.MAJORITY));

QueryResult qr = sqr.queryResult();
```

After

```java
Unresolved include directive in modules/project-docs/pages/distributed-acid-transactions-migration-guide.adoc - include::devguide:example$java/TransactionsMigration.java[]
```

## [](#cleanup)Cleanup

This doesn’t impact the API, but it is useful to know that lost cleanup has changed.

Previously, lost cleanup would look for expired transactions on the default collections of all buckets in the cluster. Unless a metadata collection was specified, in which case only that collection would be cleaned up.

Now, cleanup is dynamic. As transactions are run, the collection where metadata is created for that collection, is added to what we call the 'cleanup set'. This is just the set of collections where cleanup, for this application, is looking for expired transactions.

The intent has always been that users without complex requirements should never need to think about or configure transaction cleanup, and this new dynamic cleanup allows us to be closer still to that goal.

## [](#naming)Naming

All exceptions and events have been renamed to be compliant with the SDK. For example, `TransactionFailed` is now `TransactionFailedException`, and `TransactionCleanupAttempt` is now `TransactionCleanupAttemptEvent`.

## [](#logging)Logging

`TransactionFailedException` now exposes the logs directly, rather than containing a nested `TransactionResult`.

Before

```java
catch (TransactionFailedException err) {
    err.result().log().logs().forEach(msg -> logger.warning(msg.toString()));
}
```

After

```java
Unresolved include directive in modules/project-docs/pages/distributed-acid-transactions-migration-guide.adoc - include::devguide:example$java/TransactionsMigration.java[]
```

## [](#further-reading)Further Reading

* There’s plenty of explanation about how Transactions work in Couchbase in our [Transactions documentation](../../../server/current/learn/data/transactions.md).
* The [Java SDK transactions documentation](../howtos/distributed-acid-transactions-from-the-sdk.md).