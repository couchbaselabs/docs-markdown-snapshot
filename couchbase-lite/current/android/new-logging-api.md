[View original HTML](/couchbase-lite/current/android/new-logging-api.html)

> Introduced in Couchbase Lite 3.2.2.  
> Related Content — [Troubleshooting Queries](troubleshooting-queries.md)

## [](#logsinks)LogSinks

Log sinks are thread safe, removing risk of inconsistent states during initialization.

The three destinations for logs have been named as `LogSinks`, following the common source–sink terminology.

The `FileLogSink`, the `ConsoleLogSink` and the `CustomLogSink` are all to be installed in an instance of `LogSinks`.

Only `ConsoleLogSink` is enabled for all logging domains at the warning level by default. To enable a specific type of log sink, create a log sink object of that type, set its minimum log level and domains, and assign it to `LogSinks`. To disable a log sink, set it to null or use a log sink with `LogLevel.NONE`.

Couchbase still logs its messages in a handful of named domains and at common log levels: `LogLevel.DEBUG` the most verbose, and `LogLevel.ERROR` only for serious failures.

Accessing `LogSinks` depends on the platform. In Java, use the method `LogSinks.get()` to obtain an instance. In Swift, Objective-C, .NET, and C, `LogSinks` provides only static methods, without a singleton instance.

`LogSinks` are immutable: you set the level and domain at which they log in their constructors.

Log output is split into the following streams:

* [Logging to the Couchbase File Log](#lbl-file-logsink)  
Each log level writes to a separate file and there is a single retention policy for all files
* [Logging to the Console](#lbl-console-logsink)  
You can independently configure and control console logs, which provides a convenient method of accessing diagnostic information during debugging scenarios.  
With console logging, you can fine-tune diagnostic output to suit specific debug scenarios, without interfering with any logging required by Couchbase Support for the investigation of issues.
* [Using a Custom Logger](#lbl-custom-logsink)  
For greater flexibility you can implement a custom logging class.

### [](#lbl-console-logsink)Logging to the Console

Create an instance of `ConsoleLogSink` initialized with the desired log level and domains and install it.

* Java
* Kotlin

```java
LogSinks.get().setConsole(new ConsoleLogSink(LogLevel.WARNING));
```

```kotlin
LogSinks.get().console = ConsoleLogSink(LogLevel.WARNING)
```

### [](#lbl-file-logsink)Logging to the Couchbase File Log

Create a new `FileLogSink` with the desired properties and install it.

|  | setRotateCount from before 3.2.2 API is slightly different from setMaxKeptFiles. setMaxKeptFiles is the maximum number of log files that will exist at any time and is the count of rotated files (setRotateCount) plus one. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

* Java
* Kotlin

```java
LogSinks.get().setFile(new FileLogSink.Builder()
     .setLevel(LogLevel.VERBOSE)
     .setDirectory("/tmp/logs")
     .setMaxKeptFiles(12)
     .setPlainText(false)
     .build());
```

```kotlin
FileLogSinkFactory.install(
     level = LogLevel.VERBOSE,
     directory = "/tmp/logs",
     maxKeptFiles = 12,
     isPlainText = true
 )
```

### [](#lbl-custom-logsink)Using a Custom Logger

Create an instance of your custom sink, and to install it use `LogSinks.get().setCustom` in Java, or the appropriate static method in Swift, Objective-C, .NET, and C.

As with the other log sinks, you will have to specify the level and domain at which Couchbase logs are forwarded to your custom sink at its creation.

Your custom log sink code will have to change as well. For Android, the most significant change is that instead of _implementing_ the `Logger` interface, a custom log sink must _extend_ the `BaseLogSink` class.

The `BaseLogSink` class does not have a no-args constructor: you must specify at least the level at which Couchbase logs will be forwarded to the logger.

Your logger will receive only logs at the level and domain for which it is initialized. There is no need to record or filter the logs forwarded to the protected `writeLog` method.

`LogSinks` are meant to support logging by the Couchbase Lite platform. They were never meant as a general framework for logging.

|  | Customer code can no longer log, directly, to any of the Couchbase log sinks. The Console and File log sinks cannot be subclassed and do not publish methods that allow writing logs. If you need to log to the console for example, you’ll have to create your own way of doing so. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

* Java
* Kotlin

```java
LogSinks.get().setCustom(new BaseLogSink(LogLevel.WARNING, LogDomain.NETWORK, LogDomain.REPLICATOR) {
    @Override
    public void writeLog(LogLevel level, LogDomain domain, String message) {
        // this method will be called only with messages from the NETWORK and REPLICATOR
        // domains with a log level of WARNING or higher.
        sendToNetwork(String.format("%s/%s: %s", domain, level, message));
    }
});
```

```kotlin
LogSinks.get().custom =
    object : BaseLogSink(LogLevel.WARNING, LogDomain.NETWORK, LogDomain.REPLICATOR) {
        public override fun writeLog(level: LogLevel, domain: LogDomain, message: String) {
            // sendToNetwork will be called only with messages from the NETWORK and REPLICATOR
            // domains with a log level of WARNING or higher.
            sendToNetwork(String.format("%s/%s: %s", domain, level, message))
        }
    }
```

## [](#decoding-binary-logs)Decoding binary logs

|  | The latest version of the cbl-log tool is 3.0.0. |
|  | ------------------------------------------------ |

You can use the **cbl-log** tool to decode binary log files — see [Example 1](#eg-cbl-log).

Example 1\. Using the cbl-log tool

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

Extract the downloaded zip file.

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