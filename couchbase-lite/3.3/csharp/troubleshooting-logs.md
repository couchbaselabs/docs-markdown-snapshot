---
title: Using the Legacy Logging API for Troubleshooting
description: Couchbase Lite on C# -- Using Logs for Troubleshooting
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.3/modules/csharp/pages/troubleshooting-logs.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/couchbase-lite/3.3/csharp/troubleshooting-logs.html)

# Using the Legacy Logging API for Troubleshooting

> Description — _Couchbase Lite on C# — Using Logs for Troubleshooting_  
> Related Content — [Troubleshooting Queries](troubleshooting-queries.md)

> [!NOTE]
> Constraints
> 
> * The retrieval of logs from the device is out of scope of this feature.
> * This content applies to the post 2.5 versions. If you are using a Couchbase Lite release prior to 2.5 see [Deprecated functionality](#pre-2x5-logging)

## [](#introduction)Introduction

Couchbase Lite provides a robust Logging API \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] — see: API References for [Logging classes](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.html) — which make debugging and troubleshooting easier during development and in production. It delivers flexibility in terms of how logs are generated and retained, whilst also maintaining the level of logging required by Couchbase Support for investigation of issues.

Log output is split into the following streams:

* [File based logging](#lbl-file-logs)  
Here logs are written to [separate log files](#log-file-outputs) filtered by log level, with each log level supporting individual retention policies.
* [Console based logging](#lbl-console-logs)  
You can independently configure and control console logs, which provides a convenient method of accessing diagnostic information during debugging scenarios. With console logging, you can fine-tune diagnostic output to suit specific debug scenarios, without interfering with any logging required by Couchbase Support for the investigation of issues.
* [Custom logging](#lbl-custom-logs)  
For greater flexibility you can implement a custom logging class using the [ILogger](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.ILogger.html) interface.

In all instances, you control what is logged and at what level using the [Log](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.Log.html) class.

## [](#lbl-console-logs)Console based logging

Console based logging is often used to facilitate troubleshooting during development.

Console logs are your go-to resource for diagnostic information. You can easily fine-tune their diagnostic content to meet the needs of a particular debugging scenario, perhaps by increasing the verbosity and-or choosing to focus on messages from a specific domain; to better focus on the problem area.

Changes to console logging are independent of file logging, so you can make change without compromising any files logging streams. It is enabled by default. To change default settings use database’s [Log](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.Log.html) method to set the required values — see [Example 1](#eg-cons-log)

You will primarily use [log.getConsole()](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.Log.html#Couchbase%5FLite%5FLogging%5FLog%5FConsole) and [IConsoleLogger](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.IConsoleLogger.html) to control console logging.

Example 1\. Change Console Logging Settings

This example enables and defines console-based logging settings.

```C#
    Database.Log.Console.Domains = LogDomain.All; (1)
    Database.Log.Console.Level = LogLevel.Verbose; (2)
Database.Log.Console.Level = LogLevel.Verbose;
```

| **1** | Define the required domain ; here we turn on logging for all available domains — see: [log.getConsole().setDomain()](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.ConsoleLogger.html#Couchbase%5FLite%5FLogging%5FIConsoleLogger%5FDomains) and enum [LogDomain](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.LogDomain.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                             |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **2** | Here we turn on the most verbose log level — see: [log.getConsole().setLevel()](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.ConsoleLogger.html#Couchbase%5FLite%5FLogging%5FIConsoleLogger%5FDomains) and enum [LogLevel](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.LogLevel.html).To disable logging for the specified [LogDomain](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.LogDomain.html) set the [LogLevel](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.LogLevel.html) to None. Related [Log](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.Log.html) \| [log.getConsole()](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.Log.html#Couchbase%5FLite%5FLogging%5FLog%5FConsole) | [IConsoleLogger](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.IConsoleLogger.html) |

## [](#lbl-file-logs)File based logging

File based logging is disabled by default — see: [Example 2](#eg-file-log) for how to enable it.

You will primarily use [log.getFile()](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.Log.html#Couchbase%5FLite%5FLogging%5FLog%5FFile) and [FileLogger](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.FileLogger.html) to control file-based logging.

### [](#formats)Formats

Available file based logging formats:

* Binary — most efficient for storage and performance. It is the default for file based logging.  
Use this format and a decoder, such as **cbl-log**, to view them — see: [Decoding binary logs](#decoding-binary-logs).
* Plaintext

### [](#configuration)Configuration

As with console logging you can set the log level — see: the [FileLogger](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.FileLogger.html) class.

With file based logging you can also use the [LogFileConfiguration](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.LogFileConfiguration.html) class’s properties to specify the:

* log file path to the directory to store the log file Once this limit is exceeded a new log file is started.
* log file format  
The default is _binary_. You can over ride that where necessary and output a plain text log.
* maximum number of rotated log files to keep
* maximum size of the log file (bytes).

Example 2\. Enabling file logging

```C#
    var tempFolder = Path.Combine(Service.GetInstance<IDefaultDirectoryResolver>().DefaultDirectory(), "cbllog");
    var config = new LogFileConfiguration(tempFolder) (1)
    {
        MaxRotateCount = 5, (2)
        MaxSize = 10240, (3)
        UsePlaintext = false  (4)
    };
    Database.Log.File.Config = config; // Apply configuration
    Database.Log.File.Level = LogLevel.Info; (5)
Database.Log.File.Config = new LogFileConfiguration("path/to/log/directory")
{
    MaxRotateCount = 2, // Save 3 log files (i.e. 2 rotated and 1 current)
    MaxSize = 1024 * 512, // 512KB per file, then rotated
};

Database.Log.File.Level = LogLevel.Verbose;
```

| **1** | Set the log file directory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                     |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **2** | Here we change the max rotation count from the default (1) to 5. **Note** this means six files may exist at any one time; the five rotated log files, plus the active log file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                     |
| **3** | Here we set the maximum size (bytes) for our log file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                     |
| **4** | Here we select the binary log format (included for reference only as this is the default)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                     |
| **5** | Here we increase the log output level from the default (_warnings_) to _info_ — see: [log.getFile().setLevel()](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.FileLogger.html#Couchbase%5FLite%5FLogging%5FFileLogger%5FLevel) **Note** that the use of [Database.SetLogLevel()](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Database.html#Couchbase%5FLite%5FDatabase%5FCouchbase%5FLite%5FDatabase%5FSetLogLevel%5FCouchbase%5FLite%5FLogging%5FLogDomain%5FCouchbase%5FLite%5FLogging%5FLogLevel%5F) is now deprecated. Further, you can no longer set a log level for a specific domain. Related [Log](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.Log.html) \| [log.getFile()](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.Log.html#Couchbase%5FLite%5FLogging%5FLog%5FFile) | [FileLogger](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.FileLogger.html) |

## [](#lbl-custom-logs)Custom logging

Couchbase Lite allows for the registration of a callback function to receive Couchbase Lite log messages, which may be logged using any external logging framework.

To do this, apps must implement the [ILogger](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.ILogger.html) interface — see [Example 3](#eg-impl-log) — and enable custom logging using [log.setCustom()](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.Log.html#Couchbase%5FLite%5FLogging%5FLog%5FCustom) — see [Example 4](#eg-cust-log).

Example 3\. Implementing logger interface

Here we introduce the code that implements the [ILogger](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.ILogger.html) interface.

```C#
class LogTestLogger : ILogger
{
    public LogLevel Level { get; set; }

    public void Reset()
    {
    }

    public void Log(LogLevel level, LogDomain domain, string message)
    {
        // handle the message, for example piping it to
        // a third party framework
    }
}
```

Example 4\. Enabling custom logging

This example show how to enable the custom logger from [Example 3](#eg-impl-log).

```C#
 Database.Log.Custom = new LogTestLogger(); (1)

 // You can also specify the level of logging the logger receives
 Database.Log.Custom = new LogTestLogger { Level = LogLevel.Warning };
```

| **1** | Here we set the custom logger with a level of 'warning'. The custom logger is called with every log and may choose to filter it, using its configured level. Related [Log](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.Log.html) \| [log.getCustom()](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.Log.html#Couchbase%5FLite%5FLogging%5FLog%5FCustom) | [ILogger](https://docs.couchbase.com/mobile/3.3.4/couchbase-lite-net/api/Couchbase.Lite.Logging.ILogger.html) |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |

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