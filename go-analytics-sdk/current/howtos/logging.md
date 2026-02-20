---
title: Logging
description: Configuring logging with the Analytics Go SDK.
editUrl: https://github.com/couchbase/docs-analytics-sdk-go/edit/release/1.0/modules/howtos/pages/logging.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:go-analytics-sdk:howtos:logging.adoc[]
---

[View original HTML](/go-analytics-sdk/current/howtos/logging.html)

# Logging

> Configuring logging with the Analytics Go SDK. 

The Analytics Go SDK offers simple logging of library internals to help debug issues. Logging may be configured on a global library-level basis. **Note that the logging API is subject to change**.

You can configure logging using the `ClusterOptions.SetLogger` function, which accepts an implementation of `cbanalytics.Logger`. The SDK comes with three built-in `Logger` implementations which can be used with `SetLogger`:

* `cbanalytics.InfoLogger()` returns a logger with log level set to `Info` which logs errors, warnings, and informational messages. This is fairly non-disruptive and does not produce a lot of output.
* `cbanalytics.VerboseLogger()` returns a logger with log level set to `Trace` which logs more detailed tracing information. This logger should only be used when trying to diagnose an issue.
* `cbanalytics.NoopLogger()` returns a logger which does not log any output at all. This logger is equivalent to not setting a logger at all.

```golang
	cbanalytics.NewClusterOptions().SetLogger(cbanalytics.NewInfoLogger())
```

It is also possible to provide other logger implementations to `SetLogger`. Implementations must satisify the `cbanalytics.Logger` interface.

```golang
type Logger interface {
	// Error outputs an error level log message.
	Error(format string, v ...interface{})

	// Warn outputs an warn level log message.
	Warn(format string, v ...interface{})

	// Info outputs an info level log message.
	Info(format string, v ...interface{})

	// Debug outputs a debug level error log message.
	Debug(format string, v ...interface{})

	// Trace outputs a trace level error log message.
	Trace(format string, v ...interface{})
}
```

## [](#using-your-own-logger)Using your own Logger

Sometimes you want to use your own logger with the SDK. You might want your logging to use a popular logging framework such as logrus. In the following examples we show to use the SDK with a logrus logger:

First we need to create our own logger that wraps the logrus logger. The logrus logging functions don’t quite match the gocbanalytics logging interface. This means that we need to do a bit of marshalling to get the data into a set of parameters that logrus can use.

```golang
type MyLogrusLogger struct {
	logrusLogger *logrus.Logger
}

func (logger *MyLogrusLogger) Error(format string, v ...interface{}) {
	logger.logrusLogger.Error(fmt.Sprintf(format, v...))
}

func (logger *MyLogrusLogger) Warn(format string, v ...interface{}) {
	logger.logrusLogger.Warn(fmt.Sprintf(format, v...))
}

func (logger *MyLogrusLogger) Info(format string, v ...interface{}) {
	logger.logrusLogger.Info(fmt.Sprintf(format, v...))
}

func (logger *MyLogrusLogger) Debug(format string, v ...interface{}) {
	logger.logrusLogger.Debug(fmt.Sprintf(format, v...))
}

func (logger *MyLogrusLogger) Trace(format string, v ...interface{}) {
	logger.logrusLogger.Trace(fmt.Sprintf(format, v...))
}
```

Next we need to create a logrus logger instance, wrap it in our own logger and then pass it to the options:

```golang
	logger := logrus.New()
	logger.SetFormatter(&logrus.JSONFormatter{})
	logger.SetOutput(os.Stdout)
	logger.SetLevel(logrus.DebugLevel)

	opts := cbanalytics.NewClusterOptions().SetLogger(&MyLogrusLogger{logger})
```

Now all the cbanalytics logging output will go through our logger and be outputted to stdout (e.g. the terminal) in JSON.