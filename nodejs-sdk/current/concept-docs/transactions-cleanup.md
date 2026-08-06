---
title: Cleanup
description: The SDK takes care of failed or lost transactions, using an
  asynchronous cleanup background task.
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.7/modules/concept-docs/pages/transactions-cleanup.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:nodejs-sdk:concept-docs:transactions-cleanup.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/current/concept-docs/transactions-cleanup.html)

# Cleanup

> The SDK takes care of failed or lost transactions, using an asynchronous cleanup background task. 

Transactions will try to clean up after themselves in the advent of failures. However, there are situations that inevitably created failed, or 'lost' transactions, such as an application crash.

This requires an asynchronous cleanup task, described in this section.

## [](#background-cleanup)Background Cleanup

The first transaction triggered by an application will spawn a background cleanup task, whose job it is to periodically scan for expired transactions and clean them up. It does this by scanning a subset of the Active Transaction Record (ATR) transaction metadata documents, for each collection used by any transactions.

The default settings are tuned to find expired transactions reasonably quickly, while creating negligible impact from the background reads required by the scanning process. To be exact, with default settings it will generally find expired transactions within 60 seconds, and use less than 20 reads per second, per collection of metadata documents being checked. This is unlikely to impact performance on any cluster, but the settings may be [tuned](#tuning-cleanup) as desired.

All applications connected to the same cluster and running transactions will share in the cleanup, via a low-touch communication protocol on the `_txn:client-record` metadata document that will be created in each collection in the cluster involved with transaction metadata. This document is visible and should not be modified externally as it is maintained automatically. All ATRs will be distributed between all cleanup clients, so increasing the number of applications will not increase the reads required for scanning.

An application may cleanup transactions created by another application.

> [!NOTE]
> It is important to understand that if an application is not running, then cleanup is not running. This is particularly relevant to developers running unit tests or similar.

### [](#tuning-cleanup)Configuring Cleanup

The settings supported by `TransactionsCleanupConfig` are:

| Setting                     | Default    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cleanupWindow               | 60 seconds | This determines how long a cleanup 'run' is; that is, how frequently this client will check its subset of ATR documents. It is perfectly valid for the application to change this setting, which is at a conservative default. Decreasing this will cause expiration transactions to be found more swiftly (generally, within this cleanup window), with the tradeoff of increasing the number of reads per second used for the scanning process. |
| disableLostAttemptCleanup   | true       | This is the thread that takes part in the distributed cleanup process described above, that cleans up expired transactions created by any client. It is strongly recommended that it is left enabled.                                                                                                                                                                                                                                             |
| disableClientAttemptCleanup | true       | This thread is for cleaning up transactions created just by this client. The client will preferentially aim to send any transactions it creates to this thread, leaving transactions for the distributed cleanup process only when it is forced to (for example, on an application crash). It is strongly recommended that it is left enabled.                                                                                                    |

### [](#monitoring-cleanup)Monitoring Cleanup

To monitor cleanup, increase the verbosity on the logging.

Please see the [Node.js SDK logging documentation](../howtos/collecting-information-and-logging.md) for details.