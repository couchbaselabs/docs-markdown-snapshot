[View original HTML](/go-columnar-sdk/current/howtos/logging.html)

> Configuring logging with the Columnar Go SDK. 

The Columnar Go SDK offers simple logging of library internals to help debug issues. Logging may be configured on a global library-level basis. **Note that the logging API is subject to change**.

You can configure logging using the `cbcolumnar.SetLogger`, which accepts an implementation of `cbcolumnar.Logger`. The SDK comes with two built-in `Logger` implementations, which can be instantiated using the following _methods_:

* `cbcolumnar.DefaultStdioLogger()` returns a logger that logs errors and warnings. This is fairly non-disruptive and does not produce a lot of output.
* `cbcolumnar.VerboseStdioLogger()` returns a logger that logs more detailed tracing information. This logger should only be used when trying to diagnose an issue.

```golang
import (
        "github.com/couchbase/gocbcolumnar"
)

func main() {
        cbcolumnar.SetLogger(cbcolumnar.DefaultStdioLogger())

        // Use the cbcolumnar library.
}
```

It is also possible to provide other logger implementations to `cbcolumnar.SetLogger`. Implementations must satisify the `cbcolumnar.Logger` interface.

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

The `cbcolumnar.DefaultStdioLogger()` and `cbcolumnar.VerboseStdioLogger()` wrap their `gocbcore` counterparts to provide a stable interface. The `cbcolumnar` versions should be used.

## [](#log-redaction)Log Redaction

Redacting logs is a two-stage process. If you want to redact client logs (for example before handing them off to the Couchbase Support team) you first need to enable log redaction in your application.

```golang
cbcolumnar.SetLogRedactionLevel(cbcolumnar.RedactFull)
```

Different redaction levels are supported — please see the `RedactionLevel` enum description for more information.

Note that you need to run this command before any of the SDK code is initialized so all of the logs are captured properly. Once the SDK writes the logs with the tags to a file, you can then use the xref:7.1@server:cli:cbcli/cblogredac

* You may wish to read more on Log Redaction [in the Server docs](#7.1@server:manage:manage-logging/manage-logging.adoc#understanding%5Fredaction).

## [](#using-your-own-logger)Using your own Logger

Sometimes you want to use your own logger with the SDK. You might want your logging to use a popular logging framework such as logrus. In the following examples we show to use the SDK with a logrus logger:

First we need to create our own logger that wraps the logrus logger. The logrus `Log`/`Logf` functions don’t quite match the cbcolumnar logging interface and the log levels are slightly different. This means that we need to do a bit of marshalling to get the data into a set of parameters that logrus can use.

```golang
type MyLogrusLogger struct {
	logger *logrus.Logger
}

// Log function doesn't match the gocb Log function so we need to do a bit of marshalling.
func (logger *MyLogrusLogger) Log(level cbcolumnar.LogLevel, offset int, format string, v ...interface{}) error {
	// We need to do some conversion between gocb and logrus levels as they don't match up.
	var logrusLevel logrus.Level
	switch level {
	case cbcolumnar.LogError:
		logrusLevel = logrus.ErrorLevel
	case cbcolumnar.LogWarn:
		logrusLevel = logrus.WarnLevel
	case cbcolumnar.LogInfo:
		logrusLevel = logrus.InfoLevel
	case cbcolumnar.LogDebug:
		logrusLevel = logrus.DebugLevel
	case cbcolumnar.LogTrace:
		logrusLevel = logrus.TraceLevel
	case cbcolumnar.LogSched:
		logrusLevel = logrus.TraceLevel
	case cbcolumnar.LogMaxVerbosity:
		logrusLevel = logrus.TraceLevel
	}

	// Send the data to the logrus Logf function to make sure that it gets formatted correctly.
	logger.logger.Logf(logrusLevel, format, v...)
	return nil
}
```

Next we need to create a logrus logger instance, wrap it in our own logger and then pass it to cbcolumnar:

```golang
	logger := logrus.New()
	logger.SetFormatter(&logrus.JSONFormatter{})
	logger.SetOutput(os.Stdout)
	logger.SetLevel(logrus.DebugLevel)

	cbcolumnar.SetLogger(&MyLogrusLogger{
		logger: logger,
	})
```

Now all of the cbcolumnar logging output will go through our logger and be outputted to stdout (e.g. the terminal) in JSON.