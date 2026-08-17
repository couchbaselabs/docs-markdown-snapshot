---
title: Logging
description: Node.js SDK logging.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.5/modules/howtos/pages/collecting-information-and-logging.adoc
  xref: xref:4.5@nodejs-sdk:howtos:collecting-information-and-logging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/4.5/howtos/collecting-information-and-logging.html)

# Logging

> Node.js SDK logging. 

> [!IMPORTANT]
> the Logging implementation has changed substantially in 4.x. Customized logging is not yet implemented, this will be resolved in a future 4.x release. Use of the console logger (detailed below) is currently recommended.

## [](#library-logging)Library logging

The Node.js SDK allows logging via the `CBPPLOGLEVEL` environment variable.

Note that these logs will go to `stderr` — on most developers' laptops, `stderr` will be redirected to `stdout` (standard output), and displayed in the terminal running the app. Redirection to a log file may depend upon which shell you use. For the `BASH` shell, for example, see the [Bash Scripting Guide](https://tldp.org/LDP/abs/html/io-redirection.html).

### [](#environmental-settings)Environmental Settings

In the command line environment, the `CBPPLOGLEVEL` variable is set as follows:

GNU/Linux and Mac

```console
export CBPPLOGLEVEL=<log-level>
```

Windows

```console
set CBPPLOGLEVEL=<log-level>
```

Version 4.4.3 of the SDK introduces the `CBPPLOGFILE` variable that can be used in conjunction with `CBPPLOGLEVEL`. Set `CBPPLOGFILE` to a filename in order to have the log output to a file (instead of `stderr`).

In the command line environment, the `CBPPLOGFILE` variable is set as follows:

GNU/Linux and Mac

```console
export CBPPLOGFILE=<filename>
```

Windows

```console
set CBPPLOGFILE=<filename>
```

## [](#log-levels)Log Levels

You can increase the log level for greater verbosity (more information) in the logs:

* off — disables all logging, which is normally set by default.
* error — error messages.
* warn — error notifications.
* info — useful notices, not often.
* debug — diagnostic information, minimum level required to investigate problems.
* trace — detailed diagnostic information, often required to investigate problems.

When logging is turned on, the SDK will output messages similar to this:

```console
[2022-05-17 15:23:46.221] [85833,13741777] [debug] 1ms, [2aed64fd-5d38-416a-cc09-e67c371b8444]: use default CA for TLS verify
```