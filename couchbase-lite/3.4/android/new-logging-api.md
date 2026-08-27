---
title: New Logging API
description: A new Logging API.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.4/modules/android/pages/new-logging-api.adoc
  xref: xref:3.4@couchbase-lite:android:new-logging-api.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.4/android/new-logging-api.html)

# New Logging API

> A new Logging API. 

## [](#upgrading-to-the-new-cbl-logging-api)Upgrading to the New CBL Logging API

> [!CAUTION]
> Use of the deprecated and new Logging API at the same time is not supported.

You can find information about the new Couchbase Lite Logging API introduced in Couchbase Lite 3.2.2.

For information about the now deprecated earlier version of the Logging API, see [Using Logs for Troubleshooting](../../3.1/android/troubleshooting-logs.md).

## [](#logsinks)LogSinks

Couchbase Lite 3.2.2 introduced a new Logging API. The new Logging API has the following benefits:

* Log sinks are now thread safe, removing risk of inconsistent states during initialization.
* Simplified API and reduced implementation complexity.

The new logging API retains many of the core concepts of the previous API.

The first thing to note is that the three destinations for logs have been renamed as `LogSinks`, in keeping with common source/sink terminology.

The `FileLogSink`, the `ConsoleLogSink` and the `CustomLogSink` are all to be installed in an instance of `LogSinks`.

Only `ConsoleLogSink` is enabled for all logging domains at the warning level by default. To enable a specific type of log sink, create a log sink object of that type, set its minimum log level and domains, and assign it to `LogSinks`. To disable a log sink, set it to null or use a log sink with `LogLevel.NONE`.

Couchbase still logs its messages in a handful of named domains and at common log levels: `LogLevel.DEBUG` the most verbose, and `LogLevel.ERROR` only for serious failures.

Accessing `LogSinks` depends on the platform. In Java, use the method `LogSinks.get()` to obtain an instance. In Swift, Objective-C, .NET, and C, `LogSinks` provides only static methods, without a singleton instance.

The biggest difference between the new and the old API is that `LogSinks` are immutable: you set the level and domain at which they log in their constructors. For example, you can only change the level at which the `ConsoleLogSink` forwards messages to the console by installing a new one created for the new log level.

Log output is split into the following streams:

* [Logging to the Couchbase File Log](#lbl-file-logsink)  
Each log level writes to a separate file and there is a single retention policy for all files
* [Logging to the Console](#lbl-console-logsink)  
You can independently configure and control console logs, which provides a convenient method of accessing diagnostic information during debugging scenarios.  
With console logging, you can fine-tune diagnostic output to suit specific debug scenarios, without interfering with any logging required by Couchbase Support for the investigation of issues.
* [Using a Custom Logger](#lbl-custom-logsink)  
For greater flexibility you can implement a custom logging class.

### [](#lbl-console-logsink)Logging to the Console

The changes necessary convert the installation of a console logger from the old to the new API are minimal. Create an instance of `ConsoleLogSink` initialized with the desired log level and domains and install it.

* Java
* Kotlin

Old API

```java
Database.log.getConsole().setLevel(LogLevel.WARNING); (1)
```

New API

```java
LogSinks.get().setConsole(new ConsoleLogSink(LogLevel.WARNING));
```

Old API

```kotlin
Database.log.console.domains = LogDomain.ALL_DOMAINS (1)
Database.log.console.level = LogLevel.WARNING (2)
```

New API

```kotlin
LogSinks.get().console = ConsoleLogSink(LogLevel.WARNING)
```

### [](#lbl-file-logsink)Logging to the Couchbase File Log

The changes necessary to convert the installation of a file logger are also similar. Instead of configuring a `FileLogger` using a `LogFileConfiguration`, create a new `FileLogSink` with the desired properties and install it.

> [!NOTE]
> `setRotateCount` from the old API is slightly different from `setMaxKeptFiles`. `setMaxKeptFiles` is the maximum number of log files that will exist at any time and is the count of rotated files (`setRotateCount`) plus one.

* Java
* Kotlin

Old API

```java
LogFileConfiguration LogCfg = new LogFileConfiguration(
    (System.getProperty("user.dir") + "/MyApp/logs")); (1)
LogCfg.setMaxSize(10240); (2)
LogCfg.setMaxRotateCount(5); (3)
LogCfg.setUsePlaintext(false); (4)
Database.log.getFile().setConfig(LogCfg);
Database.log.getFile().setLevel(LogLevel.INFO); (5)
```

New API

```java
LogSinks.get().setFile(new FileLogSink.Builder()
     .setLevel(LogLevel.VERBOSE)
     .setDirectory("/tmp/logs")
     .setMaxKeptFiles(12)
     .setPlainText(false)
     .build());
```

Old API

```kotlin
Database.log.file.let {
    it.config = LogFileConfigurationFactory.newConfig(
        context.cacheDir.absolutePath, (1)
        maxSize = 10240, (2)
        maxRotateCount = 5, (3)
        usePlainText = false
    ) (4)
    it.level = LogLevel.INFO (5)
```

New API

```kotlin
FileLogSinkFactory.install(
     level = LogLevel.VERBOSE,
     directory = "/tmp/logs",
     maxKeptFiles = 12,
     isPlainText = true
 )
```

### [](#lbl-custom-logsink)Using a Custom Logger

Installing a custom log sink with the new API is also streamlined: create an instance of your custom sink, and to install it use `LogSinks.get().setCustom` in Java, or the appropriate static method in Swift, Objective-C, .NET, and C.

As with the other log sinks, you will have to specify the level and domain at which Couchbase logs are forwarded to your custom sink at its creation.

Your custom log sink code will have to change as well. For Android, the most significant change is that instead of _implementing_ the `Logger` interface, a custom log sink must _extend_ the `BaseLogSink` class.

The `BaseLogSink` class does not have a no-args constructor: you must specify at least the level at which Couchbase logs will be forwarded to the logger.

A second important change is that your logger will receive only logs at the level and domain for which it is initialized. There is no need to record or filter the logs forwarded to the protected `writeLog` method which replaces the public `log` method from the old API.

Related to this last point, the Couchbase `Loggers`, now `LogSinks` are meant to support logging by the Couchbase Lite platform. They were never meant as a general framework for logging.

> [!IMPORTANT]
> With the new API, customer code can no longer log, directly, to any of the Couchbase log sinks. The Console and File log sinks cannot be subclassed and do not publish methods that allow writing logs. If you need to log to the console for example, you'll have to create your own way of doing so.

* Java
* Kotlin

Old API Implementing The Custom Logger Interface

```java
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

Old API Enable Custom Logger

```java
Database.log.setCustom(new LogTestLogger(LogLevel.WARNING)); (1)
```

New API

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

Old API Implementing The Custom Logger Interface

```kotlin
class LogTestLogger(private val level: LogLevel) : Logger {
    override fun getLevel() = level

    override fun log(level: LogLevel, domain: LogDomain, message: String) {
        // this method will never be called if param level < this.level
        // handle the message, for example piping it to a third party framework
    }
}

private fun sendToNetwork(format: String) { }
```

Old API Enable Custom Logger

```kotlin
// this custom logger will not log an event with a log level < WARNING
Database.log.custom = LogTestLogger(LogLevel.WARNING) (1)
```

New API

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