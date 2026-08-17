---
title: Logging
description: Logging with <code>gocb.Logger</code> & using other implementations.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.10/modules/howtos/pages/collecting-information-and-logging.adoc
  xref: xref:2.10@go-sdk:howtos:collecting-information-and-logging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/2.10/howtos/collecting-information-and-logging.html)

# Logging

> Logging with `gocb.Logger` & using other implementations. 

The Go SDK offers simple logging of library internals to help debug issues. Logging may be configured on a global library-level basis. **Note that the logging API is subject to change**.

You can configure logging using the `gocb.SetLogger`, which accepts an implementation of `gocb.Logger`. The SDK comes with two built-in `Logger` implementations, which can be instantiated using the following _methods_:

* `gocb.DefaultStdioLogger()` returns a logger that logs errors and warnings. This is fairly non-disruptive and does not produce a lot of output.
* `gocb.VerboseStdioLogger()` returns a logger that logs more detailed tracing information. This logger should only be used when trying to diagnose an issue.

```golang
import (
        "github.com/couchbase/gocb/v2"
)

func main() {
        gocb.SetLogger(gocb.DefaultStdioLogger())

        // Use the gocb library.
}
```

It is also possible to provide other logger implementations to `gocb.SetLogger`. Implementations must satisify the `gocb.Logger` interface.

```golang
  type Logger interface {
	// Outputs logging information:
	// level is the verbosity level
	// offset is the position within the calling stack from which the message
	// originated. This is useful for contextual loggers which retrieve file/line
	// information.
	Log(level LogLevel, offset int, format string, v ...interface{}) error
}
```

The `gocb.DefaultStdioLogger()` and `gocb.VerboseStdioLogger()` wrap their `gocbcore` counterparts to provide a stable interface. The `gocb` versions should be used.

## [](#log-redaction)Log Redaction

Redacting logs is a two-stage process. If you want to redact client logs (for example before handing them off to the Couchbase Support team) you first need to enable log redaction in your application.

```golang
gocb.SetLogRedactionLevel(gocb.RedactFull)
```

Different redaction levels are supported — please see the `RedactionLevel` enum description for more information.

Note that you need to run this command before any of the SDK code is initialized so all of the logs are captured properly. Once the SDK writes the logs with the tags to a file, you can then use the [cblogredaction tool](#7.1@server:cli:cbcli/cblogredaction.adoc) to obfuscate the log.

* You may wish to read more on Log Redaction [in the Server docs](#7.1@server:manage:manage-logging/manage-logging.adoc#understanding%5Fredaction).

## [](#using-your-own-logger)Using your own Logger

Sometimes you want to use your own logger with the SDK. You might want your logging to use a popular logging framework such as logrus. In the following examples we show to use the SDK with a logrus logger:

First we need to create our own logger that wraps the logrus logger. The logrus `Log`/`Logf` functions don't quite match the gocb logging interface and the log levels are slightly different. This means that we need to do a bit of marshalling to get the data into a set of parameters that logrus can use.

```golang
type MyLogrusLogger struct {
	logger *logrus.Logger
}

// The logrus Log function doesn't match the gocb Log function so we need to do a bit of marshalling.
func (logger *MyLogrusLogger) Log(level gocb.LogLevel, offset int, format string, v ...interface{}) error {
	// We need to do some conversion between gocb and logrus levels as they don't match up.
	var logrusLevel logrus.Level
	switch level {
	case gocb.LogError:
		logrusLevel = logrus.ErrorLevel
	case gocb.LogWarn:
		logrusLevel = logrus.WarnLevel
	case gocb.LogInfo:
		logrusLevel = logrus.InfoLevel
	case gocb.LogDebug:
		logrusLevel = logrus.DebugLevel
	case gocb.LogTrace:
		logrusLevel = logrus.TraceLevel
	case gocb.LogSched:
		logrusLevel = logrus.TraceLevel
	case gocb.LogMaxVerbosity:
		logrusLevel = logrus.TraceLevel
	}

	// Send the data to the logrus Logf function to make sure that it gets formatted correctly.
	logger.logger.Logf(logrusLevel, format, v...)
	return nil
}
```

Next we need to create a logrus logger instance, wrap it in our own logger and then pass it to gocb:

```golang
	logger := logrus.New()
	logger.SetFormatter(&logrus.JSONFormatter{})
	logger.SetOutput(os.Stdout)
	logger.SetLevel(logrus.DebugLevel)

	gocb.SetLogger(&MyLogrusLogger{
		logger: logger,
	})
```

Now all of the gocb logging output will go through our logger and be outputted to stdout (e.g. the terminal) in JSON.