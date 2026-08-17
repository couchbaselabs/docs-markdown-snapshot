---
title: Using Logs for Troubleshooting
description: Couchbase Lite on Objective-C -- Using Logs for Troubleshooting
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/objc/pages/troubleshooting-logs.adoc
  xref: xref:3.0@couchbase-lite:objc:troubleshooting-logs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/objc/troubleshooting-logs.html)

# Using Logs for Troubleshooting

> Description — _Couchbase Lite on Objective-C — Using Logs for Troubleshooting_  
> Related Content — [Troubleshooting Queries](troubleshooting-queries.md) | [Decoding Crash Logs](troubleshooting-crashes.md)

> [!NOTE]
> Constraints
> 
> * The retrieval of logs from the device is out of scope of this feature.
> * This content applies to the post 2.5 versions. If you are using a Couchbase Lite release prior to 2.5 see [Deprecated functionality](#pre-2x5-logging)

## [](#introduction)Introduction

Couchbase Lite provides a robust Logging API \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] — see: API References for [CBLLog](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLLog.html), [CBLFileLogger](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLFileLogger.html) and [CBLLogFileConfiguration](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLLogFileConfiguration.html) — which make debugging and troubleshooting easier during development and in production. It delivers flexibility in terms of how logs are generated and retained, whilst also maintaining the level of logging required by Couchbase Support for investigation of issues.

Log output is split into the following streams:

* [File based logging](#lbl-file-logs)  
Here logs are written to [separate log files](#log-file-outputs) filtered by log level, with each log level supporting individual retention policies.
* [Console based logging](#lbl-console-logs)  
You can independently configure and control console logs, which provides a convenient method of accessing diagnostic information during debugging scenarios. With console logging, you can fine-tune diagnostic output to suit specific debug scenarios, without interfering with any logging required by Couchbase Support for the investigation of issues.
* [Custom logging](#lbl-custom-logs)  
For greater flexibility you can implement a custom logging class using the [CBLLogger](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Protocols/CBLLogger.html) interface.

In all instances, you control what is logged and at what level using the [CBLLog](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLLog.html) class.

## [](#lbl-console-logs)Console based logging

Console based logging is often used to facilitate troubleshooting during development.

Console logs are your go-to resource for diagnostic information. You can easily fine-tune their diagnostic content to meet the needs of a particular debugging scenario, perhaps by increasing the verbosity and-or choosing to focus on messages from a specific domain; to better focus on the problem area.

Changes to console logging are independent of file logging, so you can make change without compromising any files logging streams. It is enabled by default. To change default settings use database's [CBLLog](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLLog.html) method to set the required values — see [Example 1](#eg-cons-log)

You will primarily use [CBLLog.console](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLLog.html#/c:objc%28cs%29CBLLog%28py%29console) and [CBLConsoleLogger](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLConsoleLogger.html) to control console logging.

Example 1\. Change Console Logging Settings

This example enables and defines console-based logging settings.

```objc
CBLDatabase.log.console.domains = kCBLLogDomainAll; (1)
CBLDatabase.log.console.level = kCBLLogLevelVerbose; (2)
```

| **1** | Define the required domain ; here we turn on logging for all available domains — see: [CBLLog.console.domains](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLConsoleLogger.html#/c:objc%28cs%29CBLConsoleLogger%28py%29domains) and enum [CBLLogDomain](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Enums/CBLLogDomain.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                               |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **2** | Here we turn on the most verbose log level — see: [CBLLog.console.level](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLConsoleLogger.html#/c:objc%28cs%29CBLConsoleLogger%28py%29level) and enum [CBLLogLevel](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Enums/CBLLogLevel.html).To disable logging for the specified [CBLLogDomain](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Enums/CBLLogDomain.html) set the [CBLLogLevel](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Enums/CBLLogLevel.html) to None. Related [CBLLog](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLLog.html) \| [CBLLog.console](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLLog.html#/c:objc%28cs%29CBLLog%28py%29console) | [CBLConsoleLogger](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLConsoleLogger.html) |

## [](#lbl-file-logs)File based logging

File based logging is disabled by default — see: [Example 2](#eg-file-log) for how to enable it.

You will primarily use [CBLLog.file](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLLog.html#/c:objc%28cs%29CBLLog%28py%29file) and [CBLFileLogger](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLFileLogger.html) to control file-based logging.

### [](#formats)Formats

Available file based logging formats:

* Binary — most efficient for storage and performance. It is the default for file based logging.  
Use this format and a decoder, such as **cbl-log**, to view them — see: [Decoding binary logs](#decoding-binary-logs).
* Plaintext

### [](#configuration)Configuration

As with console logging you can set the log level — see: the [CBLFileLogger](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLFileLogger.html) class.

With file based logging you can also use the [CBLLogFileConfiguration](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLLogFileConfiguration.html) class's properties to specify the:

* log file path to the directory to store the log file Once this limit is exceeded a new log file is started.
* log file format  
The default is _binary_. You can over ride that where necessary and output a plain text log.
* maximum number of rotated log files to keep
* maximum size of the log file (bytes).

Example 2\. Enabling file logging

```objc
NSString *tempFolder = [NSTemporaryDirectory() stringByAppendingPathComponent:@"cbllog"];
CBLLogFileConfiguration *config = [[CBLLogFileConfiguration alloc] initWithDirectory:tempFolder]; (1)
config.maxRotateCount = 2; (2)
config.maxSize = 1024; (3)
config.usePlainText = YES; (4)
[CBLDatabase.log.file setConfig:config];
[CBLDatabase.log.file setLevel:kCBLLogLevelInfo]; (5)
```

| **1** | Set the log file directory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                         |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **2** | Here we change the max rotation count from the default (1) to 5. **Note** this means six files may exist at any one time; the five rotated log files, plus the active log file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                         |
| **3** | Here we set the maximum size (bytes) for our log file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                         |
| **4** | Here we select the binary log format (included for reference only as this is the default)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                         |
| **5** | Here we increase the log output level from the default (_warnings_) to _info_ — see: [CBLLog.file.level: LogLevel](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLFileLogger.html#/c:objc%28cs%29%29CBLFileLogger%28py%29level) **Note** that the use of [CBLDatabase.setLogLevel()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLDatabase.html#/c:objc%28cs%29CBLDatabase%28cm%29setLogLevel:domain:) is now deprecated. Further, you can no longer set a log level for a specific domain. Related [CBLLog](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLLog.html) \| [CBLLog.file](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLLog.html#/c:objc%28cs%29CBLLog%28py%29file) | [CBLFileLogger](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLFileLogger.html) |

## [](#lbl-custom-logs)Custom logging

Couchbase Lite allows for the registration of a callback function to receive Couchbase Lite log messages, which may be logged using any external logging framework.

To do this, apps must implement the [CBLLogger](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Protocols/CBLLogger.html) interface — see [Example 3](#eg-impl-log) — and enable custom logging using [CBLLog.custom](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLLog.html#/c:objc%28cs%29CBLLog%28py%29custom) — see [Example 4](#eg-cust-log).

Example 3\. Implementing logger interface

Here we introduce the code that implements the [CBLLogger](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Protocols/CBLLogger.html) interface.

```objc
@interface LogTestLogger :NSObject<CBLLogger>

// set the log level
@property (nonatomic) CBLLogLevel level;

@end

@implementation LogTestLogger

@synthesize level=_level;

- (void) logWithLevel:(CBLLogLevel)level domain:(CBLLogDomain)domain message:(NSString*)message {
    // handle the message, for example piping it to
    // a third party framework
}

@end
```

Example 4\. Enabling custom logging

This example show how to enable the custom logger from <\>. 

```objc
LogTestLogger *logger = [[LogTestLogger alloc] init];
logger.level = kCBLLogLevelWarning;
[CBLDatabase.log setCustom:logger];
```

| **1** | Here we set the custom logger with a level of 'warning'. The custom logger is called with every log and may choose to filter it, using its configured level. Related [CBLLog](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLLog.html) \| [CBLLog.custom](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLLog.html#/c:objc%28cs%29CBLLog%28py%29custom) | [CBLLogger](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Protocols/CBLLogger.html) |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |

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