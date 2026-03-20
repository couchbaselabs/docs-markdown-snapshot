---
title: Using the Legacy Logging API for Troubleshooting
description: Couchbase Lite on Java -- Using Logs for Troubleshooting
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.2/modules/java/pages/troubleshooting-logs.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.2@couchbase-lite:java:troubleshooting-logs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.2/java/troubleshooting-logs.html)

# Using the Legacy Logging API for Troubleshooting

> Description — _Couchbase Lite on Java — Using Logs for Troubleshooting_  
> Related Content — [Troubleshooting Queries](troubleshooting-queries.md)

> [!NOTE]
> Constraints
> 
> * The retrieval of logs from the device is out of scope of this feature.
> * This content applies to the post 2.5 versions. If you’re using a Couchbase Lite release prior to 2.5 see [Deprecated functionality](#pre-2x5-logging)

## [](#introduction)Introduction

Couchbase Lite provides a robust Logging API \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] — see: API References for [Log](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/Log.html), [FileLogger](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/FileLogger.html) and [LogFileConfiguration(String directory)](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/LogFileConfiguration.html) — which make debugging and troubleshooting easier during development and in production. It delivers flexibility in generating and retaining logs, while also maintaining the logging level that Couchbase Support requires for investigating issues.

Log output splits into the following streams:

* [File based logging](#lbl-file-logs)  
Here Couchbase Lite write logs to [separate log files](#log-file-outputs) filtered by log level, with each log level supporting individual retention policies.
* [Console based logging](#lbl-console-logs)  
You can independently configure and control console logs, which provides a convenient method of accessing diagnostic information during debugging scenarios. With console logging, you can fine-tune diagnostic output to suit specific debug scenarios, without interfering with any logging required by Couchbase Support for the investigation of issues.
* [Custom logging](#lbl-custom-logs)  
For greater flexibility you can implement a custom logging class using the [Logger](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/Logger.html) interface.

In all instances, you control what’s logged and at what level using the [Log](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/Log.html) class.

## [](#lbl-console-logs)Console based logging

Console based logging is often used to facilitate troubleshooting during development.

Console logs are your go-to resource for diagnostic information. You can fine-tune their diagnostic content to meet the needs of a particular debugging scenario, perhaps by increasing the verbosity and-or choosing to focus on messages from a specific domain; to better focus on the problem area.

Changes to console logging are independent of file logging, so you can make change without compromising any files logging streams. Console logging enables by default. To change default settings use database’s [Log](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/Log.html) method to set the required values — see [Example 1](#eg-cons-log)

You’ll primarily use `Database.log.getConsole()` to get the `ConsoleLogger` used to control console logging.

Example 1\. Change Console Logging Settings

This example enables and defines console-based logging settings.

```Java
Database.log.getConsole().setLevel(LogLevel.DEBUG); (1)
```

| **1** | Set the domains you want to log. This example turns on logging for all available domains — see: [log.getConsole().setDomain()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/ConsoleLogger.html#setDomains-java.util.EnumSet-) and enum [LogDomain](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/LogDomain.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                    |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **2** | Here the most verbose log level is turned on — see: [log.getConsole().setLevel()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/ConsoleLogger.html#setLevel-com.couchbase.lite.LogLevel-) and enum [LogLevel](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/LogLevel.html).To turn off logging for the specified [LogDomain](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/LogDomain.html) set the [LogLevel](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/LogLevel.html) to None. Related [Log](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/Log.html) \| [log.getConsole()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/Log.html) | [ConsoleLogger](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/ConsoleLogger.html) |

## [](#lbl-file-logs)File based logging

File based logging disables by default — see: [Example 2](#eg-file-log) for how to enable it.

You’ll primarily use [log.getFile()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/Log.html) and [FileLogger](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/FileLogger.html) to control file-based logging.

### [](#formats)Formats

Available file based logging formats:

* Binary — most efficient for storage and performance. It’s the default for file based logging.  
Use this format and a decoder, such as **cbl-log**, to view them — see: [Decoding binary logs](#decoding-binary-logs).
* Plaintext

### [](#configuration)Configuration

As with console logging you can set the log level — see: the [FileLogger](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/FileLogger.html) class.

With file based logging you can also use the [LogFileConfiguration](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/LogFileConfiguration.html) class’s properties to specify the:

* log file path to the directory to store the log file Once this limit is exceeded, logging starts a new log file.
* log file format  
The default is _binary_. You can over ride that where necessary and output a plain text log.
* maximum number of rotated log files to keep
* maximum size of the log file (bytes).

Example 2\. Enabling file logging

```Java
LogFileConfiguration LogCfg = new LogFileConfiguration(
    (System.getProperty("user.dir") + "/MyApp/logs")); (1)
LogCfg.setMaxSize(10240); (2)
LogCfg.setMaxRotateCount(5); (3)
LogCfg.setUsePlaintext(false); (4)
Database.log.getFile().setConfig(LogCfg);
Database.log.getFile().setLevel(LogLevel.INFO); (5)
```

| **1** | Set the log file directory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                              |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **2** | Change the max rotation count from the default (1) to 5. **Note** this means six files may exist at any one time; the five rotated log files, plus the active log file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                              |
| **3** | Set the maximum size (bytes) for the log file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                              |
| **4** | Select the binary log format (included for reference only as binary format is the default)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                              |
| **5** | Increase the log output level from the default (warnings) to info — see: [log.getFile().setLevel()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/FileLogger.html#setLevel-com.couchbase.lite.LogLevel-) **Note** that the use of [Database.setLogLevel()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/Database.html#setLogLevel-com.couchbase.lite.LogDomain-com.couchbase.lite.LogLevel-) is now deprecated. Further, you can no longer set a log level for a specific domain. Related [Log](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/Log.html) \| [log.getFile()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/Log.html) | [FileLogger](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/FileLogger.html) |

## [](#lbl-custom-logs)Custom logging

Couchbase Lite allows you to register a callback function to receive Couchbase Lite log messages, which you can log using any external logging framework.

To do this, apps must implement the [Logger](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/Logger.html) interface — see [Example 3](#eg-impl-log) — and enable custom logging using [log.setCustom()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/Log.html) — see [Example 4](#eg-cust-log).

Example 3\. Implementing logger interface

Here the code that implements the [Logger](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/Logger.html) interface is introduced.

```Java
class LogTestLogger implements com.couchbase.lite.Logger {
    @NonNull
    private final LogLevel level;

    public LogTestLogger(@NonNull LogLevel level) { this.level = level; }

    @NonNull
    @Override
    public LogLevel getLevel() { return level; }

    @Override
    public void log(@NonNull LogLevel level, @NonNull LogDomain domain, @NonNull String message) {

    }
}
```

Example 4\. Enabling custom logging

This example shows how to enable the custom logger from [Implementing logger interface](#eg-impl-log).

```Java
Database.log.setCustom(new LogTestLogger(LogLevel.WARNING)); (1)
```

| **1** | Set the custom logger with a level of 'warning'. The application calls the custom logger with every log, and the logger may choose to filter it using its configured level. Related [Log](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/Log.html) \| [log.getCustom()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/Log.html) | [Logger](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-java/com/couchbase/lite/Logger.html) |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |

## [](#decoding-binary-logs)Decoding binary logs

> [!NOTE]
> The latest version of the cbl-log tool is `3.0.0`.

You can use the **cbl-log** tool to decode binary log files — see [Example 5](#eg-cbl-log).

Example 5\. Using the cbl-log tool

* macOS
* CentOS
* Windows

Download the **cbl-log** tool using `wget`.

```console
wget https://packages.couchbase.com/releases/couchbase-lite-log/3.0.0/couchbase-lite-log-3.0.0-macos.zip
```

Extract the downloaded zip file.

```console
unzip couchbase-lite-log-3.0.0-macos.zip
```

Navigate to the **bin** directory and run the `cbl-log` executable.

```console
$ ./cbl-log logcat LOGFILE <OUTPUT_PATH>
```

Download the **cbl-log** tool using `wget`.

```console
wget https://packages.couchbase.com/releases/couchbase-lite-log/3.0.0/couchbase-lite-log-3.0.0-centos.zip
```

Extract the downloaded zip file.

```console
unzip couchbase-lite-log-3.0.0-centos.zip
```

Navigate to the **bin** directory and run the `cbl-log` executable.

```console
cbl-log logcat LOGFILE <OUTPUT_PATH>
```

Download the **cbl-log** tool using PowerShell.

```powershell
Invoke-WebRequest https://packages.couchbase.com/releases/couchbase-lite-log/3.0.0/couchbase-lite-log-3.0.0-windows.zip -OutFile couchbase-lite-log-3.0.0-windows.zip
```

Extract the downloaded zip file using PowerShell.

```powershell
Expand-Archive -Path couchbase-lite-log-3.0.0-windows.zip -DestinationPath .
```

Run the `cbl-log` executable.

```powershell
$ .\cbl-log.exe logcat LOGFILE <OUTPUT_PATH>
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [QueryBuilder](querybuilder.md)
* [SQL++ for Mobile](query-n1ql-mobile.md)
* [Live Queries](query-live.md)
* [Full Text Search](fts.md)

.

###### [](#-2)

Learn more . . .

* [SQL++ Mobile - Querybuilder Differences](query-n1ql-mobile-querybuilder-diffs.md)
* [SQL++ Mobile - SQL++ Server Differences](query-n1ql-mobile-server-diffs.md)
* [Query Resultsets](query-resultsets.md)
* [Query Troubleshooting](query-troubleshooting.md)
* [Live Queries](query-live.md)
* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)

.

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.

---

[1](#%5Ffootnoteref%5F1). From version 2.5