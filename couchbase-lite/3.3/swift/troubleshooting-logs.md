---
title: Using the Legacy Logging API for Troubleshooting
description: Couchbase Lite on Swift -- Using Logs for Troubleshooting
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.3/modules/swift/pages/troubleshooting-logs.adoc
  xref: xref:3.3@couchbase-lite:swift:troubleshooting-logs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.3/swift/troubleshooting-logs.html)

# Using the Legacy Logging API for Troubleshooting

> Description — _Couchbase Lite on Swift — Using Logs for Troubleshooting_  
> Related Content — [Troubleshooting Queries](troubleshooting-queries.md) | [Decoding Crash Logs](troubleshooting-crashes.md)

> [!NOTE]
> Constraints
> 
> * The retrieval of logs from the device is out of scope of this feature.
> * This content applies to the post 2.5 versions. If you are using a Couchbase Lite release prior to 2.5 see [Deprecated functionality](#pre-2x5-logging)

## [](#introduction)Introduction

Couchbase Lite provides a robust Logging API \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] — see: API References for [Log](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/Log.html), [FileLogger](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/FileLogger.html) and [LogFileConfiguration](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/LogFileConfiguration.html) — which make debugging and troubleshooting easier during development and in production. It delivers flexibility in terms of how logs are generated and retained, whilst also maintaining the level of logging required by Couchbase Support for investigation of issues.

Log output is split into the following streams:

* [File based logging](#lbl-file-logs)  
Here logs are written to [separate log files](#log-file-outputs) filtered by log level, with each log level supporting individual retention policies.
* [Console based logging](#lbl-console-logs)  
You can independently configure and control console logs, which provides a convenient method of accessing diagnostic information during debugging scenarios. With console logging, you can fine-tune diagnostic output to suit specific debug scenarios, without interfering with any logging required by Couchbase Support for the investigation of issues.
* [Custom logging](#lbl-custom-logs)  
For greater flexibility you can implement a custom logging class using the [Logger](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/Logger.html) interface.

In all instances, you control what is logged and at what level using the [Log](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/Log.html) class.

## [](#lbl-console-logs)Console based logging

Console based logging is often used to facilitate troubleshooting during development.

Console logs are your go-to resource for diagnostic information. You can easily fine-tune their diagnostic content to meet the needs of a particular debugging scenario, perhaps by increasing the verbosity and-or choosing to focus on messages from a specific domain; to better focus on the problem area.

Changes to console logging are independent of file logging, so you can make change without compromising any files logging streams. It is enabled by default. To change default settings use database's [Log](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/Log.html) method to set the required values — see [Example 1](#eg-cons-log)

You will primarily use [log.console](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/Log.html#/s:18CouchbaseLiteSwift3LogC7consoleAA13ConsoleLoggerCvp) and [ConsoleLogger](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/ConsoleLogger.html) to control console logging.

Example 1\. Change Console Logging Settings

This example enables and defines console-based logging settings.

```swift
Database.log.console.domains = .all (1)
Database.log.console.level = .verbose (2)
```

| **1** | Define the required domain ; here we turn on logging for all available domains — see: [log.console.domains](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/ConsoleLogger.html#/s:18CouchbaseLiteSwift13ConsoleLoggerC7domainsAA10LogDomainsVvp) and enum [LogDomain](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Enums/LogDomain.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                          |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **2** | Here we turn on the most verbose log level — see: [log.console.level](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/ConsoleLogger.html#/s:18CouchbaseLiteSwift13ConsoleLoggerC5levelAA8LogLevelOvp) and enum [LogLevel](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Enums/LogLevel.html).To disable logging for the specified [LogDomain](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Enums/LogDomain.html) set the [LogLevel](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Enums/LogLevel.html) to None. Related [Log](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/Log.html) \| [log.console](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/Log.html#/s:18CouchbaseLiteSwift3LogC7consoleAA13ConsoleLoggerCvp) | [ConsoleLogger](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/ConsoleLogger.html) |

## [](#lbl-file-logs)File based logging

File based logging is disabled by default — see: [Example 2](#eg-file-log) for how to enable it.

You will primarily use [log.file](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/Log.html#/s:18CouchbaseLiteSwift3LogC4fileAA10FileLoggerCvp) and [FileLogger](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/FileLogger.html) to control file-based logging.

### [](#formats)Formats

Available file based logging formats:

* Binary — most efficient for storage and performance. It is the default for file based logging.  
Use this format and a decoder, such as **cbl-log**, to view them — see: [Decoding binary logs](#decoding-binary-logs).
* Plaintext

### [](#configuration)Configuration

As with console logging you can set the log level — see: the [FileLogger](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/FileLogger.html) class.

With file based logging you can also use the [LogFileConfiguration](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/LogFileConfiguration.html) class's properties to specify the:

* log file path to the directory to store the log file Once this limit is exceeded a new log file is started.
* log file format  
The default is _binary_. You can over ride that where necessary and output a plain text log.
* maximum number of rotated log files to keep
* maximum size of the log file (bytes).

Example 2\. Enabling file logging

```swift
let tempFolder = NSTemporaryDirectory().appending("cbllog")
let config = LogFileConfiguration(directory: tempFolder) (1)
config.usePlainText = false (2)
config.maxRotateCount = 12 (3)
config.maxSize = 524288 (4)
Database.log.file.config = config (5)
Database.log.file.level = .verbose (6)
```

| **1** | Set the log file directory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                    |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| **2** | Set the logging format to binary by disabling text logging. This is the default, and you only need to include this for reference.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                    |
| **3** | Change the max rotation count from the default (1) to 12\. Thirteen files may exist at any one time; the twelve rotated log files, plus the active log file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                    |
| **4** | Set the maximum size (bytes) for your log file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                    |
| **5** | Set the global [LogFileConfiguration](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/LogFileConfiguration.html) to use the config you just created, which will cause file logging to be enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                    |
| **6** | Increase the log output level from the default (_warnings_) to _verbose_ — see: [log.file.level: LogLevel](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/FileLogger.html#/s:18CouchbaseLiteSwift10FileLoggerC5levelAA8LogLevelOvp). You can no longer use [Database.setLogLevel()](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/Database.html#/s:18CouchbaseLiteSwift8DatabaseC11setLogLevel%5F6domainyAA0fG0O%5FAA0F6DomainOtFZ) as it is now deprecated. Further, you can no longer set a log level for a specific domain. Related [Log](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/Log.html) \| [log.file](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/Log.html#/s:18CouchbaseLiteSwift3LogC4fileAA10FileLoggerCvp) | [FileLogger](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/FileLogger.html) |

## [](#lbl-custom-logs)Custom logging

Couchbase Lite allows for the registration of a callback function to receive Couchbase Lite log messages, which may be logged using any external logging framework.

To do this, apps must implement the [Logger](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/Logger.html) interface — see [Example 3](#eg-impl-log) — and enable custom logging using [log.custom](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/Log.html#/s:18CouchbaseLiteSwift3LogC6customAA6Logger%5FpSgvp) — see [Example 4](#eg-cust-log).

Example 3\. Implementing logger interface

Here we introduce the code that implements the [Logger](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/Logger.html) interface.

```swift
class LogTestLogger: Logger {

    // set the log level
    var level: LogLevel = .none

    // constructor for easiness
    init(_ level: LogLevel) {
        self.level = level
    }

    func log(level: LogLevel, domain: LogDomain, message: String) {
        // handle the message, for example piping it to
        // a third party framework
    }
}
```

Example 4\. Enabling custom logging

This example show how to enable the custom logger from [Example 3](#eg-impl-log).

```swift
let logger = LogTestLogger(.warning)
Database.log.custom =  logger (1)
```

| **1** | Here we set the custom logger with a level of 'warning'. The custom logger is called with every log and may choose to filter it, using its configured level. Related [Log](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/Log.html) \| [log.custom](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/Log.html#/s:18CouchbaseLiteSwift3LogC6customAA6Logger%5FpSgvp) | [Logger](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-swift/Classes/Logger.html) |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |

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

Navigate to the **bin** directory and run the `cbl-log` executable.

```console
$ ./cbl-log logcat LOGFILE <OUTPUT_PATH>
```

Download the **cbl-log** tool using `wget`.

```console
wget https://packages.couchbase.com/releases/couchbase-lite-log/3.0.0/couchbase-lite-log-3.0.0-centos.zip
```

Navigate to the **bin** directory and run the `cbl-log` executable.

```console
cbl-log logcat LOGFILE <OUTPUT_PATH>
```

Download the **cbl-log** tool using PowerShell.

```powershell
Invoke-WebRequest https://packages.couchbase.com/releases/couchbase-lite-log/3.0.0/couchbase-lite-log-3.0.0-windows.zip -OutFile couchbase-lite-log-3.0.0-windows.zip
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