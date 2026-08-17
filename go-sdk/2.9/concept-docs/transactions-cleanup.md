---
title: Cleanup
description: The SDK takes care of failed or lost transactions, using an
  asynchronous cleanup background task.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.9/modules/concept-docs/pages/transactions-cleanup.adoc
  xref: xref:2.9@go-sdk:concept-docs:transactions-cleanup.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/2.9/concept-docs/transactions-cleanup.html)

# Cleanup

> The SDK takes care of failed or lost transactions, using an asynchronous cleanup background task. 

Transactions will try to clean up after themselves in the advent of failures. However, there are situations that inevitably created failed, or 'lost' transactions, such as an application crash.

This requires an asynchronous cleanup task, described in this section.

## [](#background-cleanup)Background Cleanup

Calling `Connect` spawns a background cleanup task, whose job it is to periodically scan for expired transactions and clean them up. It does this by scanning a subset of the Active Transaction Record (ATR) transaction metadata documents, for each metadata collection used by any transactions.

> [!NOTE]
> Unless there are any metadata collections registered (either from config or by running a transaction) then the background cleanup task will do no work and so is very lightweight.

The default settings are tuned to find expired transactions reasonably quickly, while creating negligible impact from the background reads required by the scanning process. To be exact, with default settings it will generally find expired transactions within 60 seconds, and use less than 20 reads per second. This is unlikely to impact performance on any cluster, but the settings may be [tuned](#tuning-cleanup) as desired.

All applications connected to the same cluster and running `Transactions` will share in the cleanup, via a low-touch communication protocol on the `_txn:client-record` metadata document that will be created in each metadata collection used during transactions. This document is visible and should not be modified externally as is maintained automatically. All ATRs on a metadata collection will be distributed between all cleanup clients, so increasing the number of applications will not increase the reads required for scanning.

An application may cleanup transactions created by another application.

> [!NOTE]
> It is important to understand that if an application is not running, then cleanup is not running. This is particularly relevant to developers running unit tests or similar.
> 
> If this is an issue, then developers may want to consider running a simple application at all times that just calls `Connect`, to guarantee that cleanup is running. When an application is used solely for cleanup it **must** register any collections to monitor via the `CleanupCollections` config option, otherwise the cleanup task will not do any work. Only the collections registered will be monitored.

### [](#tuning-cleanup)Configuring Cleanup

| Setting                     | Default                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CleanupWindow               | 60 seconds                | This determines how long a cleanup 'run' is; that is, how frequently this client will check its subset of ATR documents. It is perfectly valid for the application to change this setting, which is at a conservative default. Decreasing this will cause expiration transactions to be found more swiftly (generally, within this cleanup window), with the tradeoff of increasing the number of reads per second used for the scanning process. |
| DisableLostAttemptCleanup   | false                     | This is the thread that takes part in the distributed cleanup process described above, that cleans up expired transactions created by any client. It is strongly recommended that it is left enabled.                                                                                                                                                                                                                                             |
| DisableClientAttemptCleanup | false                     | This thread is for cleaning up transactions created just by this client. The client will preferentially aim to send any transactions it creates to this thread, leaving transactions for the distributed cleanup process only when it is forced to (for example, on an application crash). It is strongly recommended that it is left enabled.                                                                                                    |
| CleanupCollections          | \[\]TransactionKeyspace{} | This is the set of additional collections that the lost transactions cleanup task will monitor                                                                                                                                                                                                                                                                                                                                                    |

## [](#monitoring-cleanup)Monitoring Cleanup

To monitor cleanup, increase the verbosity on the logging.

Please see the [Go SDK logging documentation](../howtos/collecting-information-and-logging.md) for details.