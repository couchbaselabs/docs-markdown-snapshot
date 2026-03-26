---
title: Using Logs for Troubleshooting
description: Couchbase Lite on Android -- Using Logs for Troubleshooting
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/android/pages/troubleshooting-logs.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.0@couchbase-lite:android:troubleshooting-logs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/android/troubleshooting-logs.html)

# Using Logs for Troubleshooting

> Description — _Couchbase Lite on Android — Using Logs for Troubleshooting_  
> Related Content — [Troubleshooting Queries](troubleshooting-queries.md)

> [!NOTE]
> Constraints
> 
> * The value returned by `LogLevel.getValue()` is not the Android log level. Do not use this API call.
> * The retrieval of logs from the device is out of scope of this feature.
> * This content applies to the post 2.5 versions. If you are using a Couchbase Lite release prior to 2.5 see [Deprecated functionality](#pre-2x5-logging)

## [](#introduction)Introduction

Couchbase Lite provides a robust Logging API \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] — see: API References for [Log](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Log.html), [FileLogger](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/FileLogger.html) and [LogFileConfiguration(String directory)](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/LogFileConfiguration.html) — which make debugging and troubleshooting easier during development and in production. It delivers flexibility in terms of how logs are generated and retained, whilst also maintaining the level of logging required by Couchbase Support for investigation of issues.

Log output is split into the following streams:

* [File based logging](#lbl-file-logs)  
Here logs are written to [separate log files](#log-file-outputs) filtered by log level, with each log level supporting individual retention policies.
* [Console based logging](#lbl-console-logs)  
You can independently configure and control console logs, which provides a convenient method of accessing diagnostic information during debugging scenarios. With console logging, you can fine-tune diagnostic output to suit specific debug scenarios, without interfering with any logging required by Couchbase Support for the investigation of issues.
* [Custom logging](#lbl-custom-logs)  
For greater flexibility you can implement a custom logging class using the [Logger](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Logger.html) interface.

In all instances, you control what is logged and at what level using the [Log](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Log.html) class.

## [](#lbl-console-logs)Console based logging

Console based logging is often used to facilitate troubleshooting during development.

Console logs are your go-to resource for diagnostic information. You can easily fine-tune their diagnostic content to meet the needs of a particular debugging scenario, perhaps by increasing the verbosity and-or choosing to focus on messages from a specific domain; to better focus on the problem area.

Changes to console logging are independent of file logging, so you can make change without compromising any files logging streams. It is enabled by default. To change default settings use database's [Log](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Log.html) method to set the required values — see [Example 1](#eg-cons-log)

You will primarily use [log.getConsole()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/ConsoleLogger.html) and [ConsoleLogger](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/ConsoleLogger.html) to control console logging.

> [!TIP]
> It can often be more effective to just use the Console logger (which logs to logcat).  
> Note, a warning is displayed when you set continuous (file) logging **off**.

Example 1\. Change Console Logging Settings

This example enables and defines console-based logging settings.

* Kotlin
* Java

```Kotlin
Database.log.console.domains = LogDomain.ALL_DOMAINS (1)
Database.log.console.level = LogLevel.VERBOSE (2)
```

```Java
Database.log.getConsole().setDomain(LogDomain.ALL_DOMAINS);  (1)
Database.log.getConsole().setLevel(LogLevel.VERBOSE); (2)
```

| **1** | Define the required domain ; here we turn on logging for all available domains — see: [log.getConsole().setDomain()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/ConsoleLogger.html##setDomains-java.util.EnumSet-) and enum [LogDomain](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/LogDomain.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                       |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **2** | Here we turn on the most verbose log level — see: [log.getConsole().setLevel()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/ConsoleLogger.html#setLevel-com.couchbase.lite.LogLevel-) and enum [LogLevel](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/LogLevel.html).To disable logging for the specified [LogDomain](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/LogDomain.html) set the [LogLevel](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/LogLevel.html) to None. Related [Log](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Log.html) \| [log.getConsole()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/ConsoleLogger.html) | [ConsoleLogger](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/ConsoleLogger.html) |

## [](#lbl-file-logs)File based logging

File based logging is disabled by default — see: [Example 2](#eg-file-log) for how to enable it.

You will primarily use [log.getFile()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/FileLogger.html) and [FileLogger](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/FileLogger.html) to control file-based logging.

### [](#formats)Formats

Available file based logging formats:

* Binary — most efficient for storage and performance. It is the default for file based logging.  
Use this format and a decoder, such as **cbl-log**, to view them — see: [Decoding binary logs](#decoding-binary-logs).
* Plaintext

### [](#configuration)Configuration

As with console logging you can set the log level — see: the [FileLogger](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/FileLogger.html) class.

With file based logging you can also use the [LogFileConfiguration(String directory)](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/LogFileConfiguration.html) class's properties to specify the:

* log file path to the directory to store the log file Once this limit is exceeded a new log file is started.
* log file format  
The default is _binary_. You can over ride that where necessary and output a plain text log.
* maximum number of rotated log files to keep
* maximum size of the log file (bytes).

Example 2\. Enabling file logging

* Kotlin
* Java

```Kotlin
Database.log.file.let {
  it.config = LogFileConfigurationFactory.create(
    context.cacheDir.absolutePath, (1)
    maxSize = 10240, (2)
    maxRotateCount = 5, (3)
    usePlainText = false
    ) (4)
    it.level = LogLevel.INFO (5)
```

```Java
final File path = context.getCacheDir();

LogFileConfiguration LogCfg =
  new LogFileConfiguration(path.toString()); (1)
LogCfg.setMaxSize(10240); (2)
LogCfg.setMaxRotateCount(5); (3)
LogCfg.setUsePlainText(false); (4)
Database.log.getFile().setConfig(LogCfg);
Database.log.getFile().setLevel(LogLevel.INFO); (5)
```

| **1** | Set the log file directory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                 |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| **2** | Here we change the max rotation count from the default (1) to 5. **Note** this means six files may exist at any one time; the five rotated log files, plus the active log file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                 |
| **3** | Here we set the maximum size (bytes) for our log file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                 |
| **4** | Here we select the binary log format (included for reference only as this is the default)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                 |
| **5** | Here we increase the log output level from the default (_warnings_) to _info_ — see: [log.getFile().setLevel()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/FileLogger.html#setLevel-com.couchbase.lite.LogLevel-) **Note** that the use of [Database.setLogLevel()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Database.html#setLogLevel-com.couchbase.lite.LogDomain-com.couchbase.lite.LogLevel-) is now deprecated. Further, you can no longer set a log level for a specific domain. Related [Log](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Log.html) \| [log.getFile()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/FileLogger.html) | [FileLogger](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/FileLogger.html) |

## [](#lbl-custom-logs)Custom logging

Couchbase Lite allows for the registration of a callback function to receive Couchbase Lite log messages, which may be logged using any external logging framework.

To do this, apps must implement the [Logger](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Logger.html) interface — see [Example 3](#eg-impl-log) — and enable custom logging using [log.setCustom()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Logger.html) — see [Example 4](#eg-cust-log).

Example 3\. Implementing logger interface

Here we introduce the code that implements the [Logger](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Logger.html) interface.

* Kotlin
* Java

```Kotlin
class LogTestLogger(private val level: LogLevel) : Logger {
    override fun getLevel() = level

    override fun log(level: LogLevel, domain: LogDomain, message: String) {
        // this method will never be called if param level < this.level
        // handle the message, for example piping it to a third party framework
    }
}
```

```Java
class LogTestLogger implements Logger {
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

This example show how to enable the custom logger from <\>. 

* Kotlin
* Java

```Kotlin
// this custom logger will not log an event with a log level < WARNING
Database.log.custom = LogTestLogger(LogLevel.WARNING) (1)
```

```Java
Database.log.setCustom(new LogTestLogger(LogLevel.WARNING)); (1)
```

| **1** | Here we set the custom logger with a level of 'warning'. The custom logger is called with every log and may choose to filter it, using its configured level. Related [Log](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Log.html) \| [log.getCustom()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Logger.html) | [Logger](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Logger.html) |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |

## [](#decoding-binary-logs)Decoding binary logs

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

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

---

[1](#%5Ffootnoteref%5F1). From version 2.5