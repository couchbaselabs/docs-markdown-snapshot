---
title: Cleanup
description: The SDK takes care of failed or lost transactions, using an
  asynchronous cleanup background task.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.2/modules/concept-docs/pages/transactions-cleanup.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/php-sdk/4.2/concept-docs/transactions-cleanup.html)

# Cleanup

> The SDK takes care of failed or lost transactions, using an asynchronous cleanup background task. 

Unresolved include directive in modules/concept-docs/pages/transactions-cleanup.adoc - include::7.5@sdk:shared:partial$acid-transactions.adoc\[\]

### [](#tuning-cleanup)Configuring Cleanup

The cleanup settings can be configured as so:

| Setting                       | Default    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cleanupWindow()               | 60 seconds | This determines how long a cleanup 'run' is; that is, how frequently this client will check its subset of ATR documents. It is perfectly valid for the application to change this setting, which is at a conservative default. Decreasing this will cause expiration transactions to be found more swiftly (generally, within this cleanup window), with the tradeoff of increasing the number of reads per second used for the scanning process. |
| disableLostAttemptCleanup()   | true       | This is the thread that takes part in the distributed cleanup process described above, that cleans up expired transactions created by any client. It is strongly recommended that it is left enabled.                                                                                                                                                                                                                                             |
| disableClientAttemptCleanup() | true       | This thread is for cleaning up transactions created just by this client. The client will preferentially aim to send any transactions it creates to this thread, leaving transactions for the distributed cleanup process only when it is forced to (for example, on an application crash). It is strongly recommended that it is left enabled.                                                                                                    |

## [](#monitoring-cleanup)Monitoring Cleanup

To monitor cleanup, increase the verbosity on the logging.

Please see the [PHP SDK logging documentation](../howtos/collecting-information-and-logging.md) for details.