---
title: Logging
description: Logging with the Analytics Node.js SDK.
editUrl: https://github.com/couchbase/docs-analytics-sdk-nodejs/edit/release/1.0/modules/howtos/pages/logging.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/nodejs-analytics-sdk/current/howtos/logging.html)

# Logging

> Logging with the Analytics Node.js SDK. 

Customized logging is not yet implemented. Use of the console logger (detailed below) is currently recommended.

## [](#logging-via-environmental-settings)Logging via Environmental Settings

In the command line environment, the `CBPPLOGLEVEL` variable is set as follows:

GNU/Linux and Mac

```console
export CBPPLOGLEVEL=<log-level>
```

Windows

```console
set CBPPLOGLEVEL=<log-level>
```

## [](#log-levels)Log Levels

You can increase the log level for greater verbosity (more information) in the logs:

* off — disables all logging, which is normally set by default.
* error — error messages.
* warn — error notifications.
* info — useful notices, not often.
* debug — diagnostic information, required to investigate problems.
* trace — the most verbose level.