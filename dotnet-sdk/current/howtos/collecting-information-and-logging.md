---
title: Logging
description: Couchbase .NET SDK3 relies on the Microsoft.Extensions.Logging API
  and specifically on the
  <code>Microsoft.Extensions.Logging.ILoggerFactory</code> interface to support
  a wide variety of compatible 3rd party logging implementations such as
  Serilog, NLog, and others.
editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.8/modules/howtos/pages/collecting-information-and-logging.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:dotnet-sdk:howtos:collecting-information-and-logging.adoc[]
---

[View original HTML](/dotnet-sdk/current/howtos/collecting-information-and-logging.html)

# Logging

> Couchbase .NET SDK3 relies on the Microsoft.Extensions.Logging API and specifically on the `Microsoft.Extensions.Logging.ILoggerFactory` interface to support a wide variety of compatible 3rd party logging implementations such as Serilog, NLog, and others. Further details can be found in the Microsoft documentation for [Logging](https://docs.microsoft.com/en-us/dotnet/core/extensions/logging) and [Logging Providers](https://docs.microsoft.com/en-us/dotnet/core/extensions/logging-providers). 

## [](#couchbase-net-sdk-logging-basics)Couchbase .NET SDK Logging Basics

The Couchbase .NET SDK allows for any logging provider to be plugged in as long as it implements the `Microsoft.Extensions.Logging.ILoggerFactory` interface. It does this via Method injection in the `ClusterOptions` class which is passed to the Cluster object when `Cluster.ConnectAsync` is called.

Note: In most of the examples below, the default .NET logging providers are used, — otherwise, we are using the [Serilog one-liner](https://github.com/serilog/serilog-extensions-logging-file) logging [package](https://www.nuget.org/packages/Serilog.Extensions.Logging.File/):

```powershell
Install-Package Serilog.Extensions.Logging.File -Version 2.0.0
```

```powershell
<PackageReference Include="Serilog.Extensions.Logging.File" Version="2.0.0" />
```

## [](#logging-in-a-net-core-non-host-application)Logging in a .NET Core Non-Host Application

If you are not using a `Host`, and not using Dependency Injection, you can still configure a `ILoggerFactory` using the SDK. In this example we have a dependency on Serilog single file logging:

```powershell
Install-Package Serilog.Extensions.Logging.File -Version 2.0.0
```

We are using a .NET Core Console Application, and simply instantiate the `ILoggingProvider`:

```csharp
IServiceCollection serviceCollection = new ServiceCollection();
serviceCollection.AddLogging(builder => builder
    .AddFilter(level => level >= LogLevel.Debug)
);
var loggerFactory = serviceCollection.BuildServiceProvider().GetService<ILoggerFactory>();
loggerFactory.AddFile("Logs/myapp-{Date}.txt", LogLevel.Debug);

var clusterOptions = new ClusterOptions().
    WithCredentials("Administrator", "password").
    WithLogging(loggerFactory);

var cluster = Cluster.ConnectAsync("couchbase://10.112.211.101", clusterOptions).
    GetAwaiter().
    GetResult();
```

We then call `ClusterOptions.WithLogging` and pass in the `ILoggerProvider` that we instatiated, and connect to the `Cluster` as usual.

## [](#logging-in-applications-targeting-the-net-core-generic-host)Logging in applications targeting the .NET Core Generic Host

For .NET Core 3.0 and greater applications, the Generic [Host](https://docs.microsoft.com/en-us/dotnet/core/extensions/generic-host) is used to configure logging.

```csharp
public static void Main(string[] args)
{
    CreateHostBuilder(args).Build().Run();
}

public static IHostBuilder CreateHostBuilder(string[] args) =>
    Host.CreateDefaultBuilder(args)
        .ConfigureLogging(logging =>
        {
            logging.ClearProviders();
            logging.AddFile("Logs/myapp-{Date}.txt", LogLevel.Debug);
        })
        .ConfigureServices((hostContext, services) =>
        {
            services.AddHostedService<Worker>();
            services.AddCouchbase(hostContext.Configuration.GetSection("couchbase"));
            services.AddCouchbaseBucket<INamedBucketProvider>("default");
        });
```

In the example above, `Host.ConfigureLogging` is called in the `CreateHostBuilder` method where we clear any previously registered logging providers (.NET registers a couple by default). Then `AddConsole` is called to configure logging to the console which will be visible when you run the application.

Note that because we are using [Couchbase Dependency Injection](https://www.nuget.org/packages/Couchbase.Extensions.DependencyInjection/), we do not have to explicitly call `ClusterOptions.WithLogging(ILoggerFactory factory)` and pass in the `ILoggerFactory`; this will be handled by [Couchbase Dependency Injection](https://www.nuget.org/packages/Couchbase.Extensions.DependencyInjection/) internally.

## [](#logging-in-applications-targeting-the-net-full-framework)Logging in applications targeting the .NET Full Framework

Targeting logging in .NET Full applications is a bit more challenging in that there is no DI container, thus the standard way of injecting the logging dependencies won’t work. Furthermore, since there is no support for the `Microsoft.Extensions.Logging` interfaces, we’ll need to create our own wrappers. One for a Log4Net `ILogger` implementation:

```csharp
public class Log4NetLogger : ILogger
{
    private readonly ILog _log;

    public Log4NetLogger(string name, XmlElement xmlElement)
    {
        var loggerRepository = log4net.LogManager.CreateRepository(
            Assembly.GetEntryAssembly(), typeof(log4net.Repository.Hierarchy.Hierarchy));
        _log = LogManager.GetLogger(loggerRepository.Name, name);
        log4net.Config.XmlConfigurator.Configure(loggerRepository, xmlElement);
    }
    public IDisposable BeginScope<TState>(TState state)
    {
        return null;
    }

    public bool IsEnabled(LogLevel logLevel)
    {
        switch (logLevel)
        {
            case LogLevel.Critical:
                return _log.IsFatalEnabled;
            case LogLevel.Debug:
            case LogLevel.Trace:
                return _log.IsDebugEnabled;
            case LogLevel.Error:
                return _log.IsErrorEnabled;
            case LogLevel.Information:
                return _log.IsInfoEnabled;
            case LogLevel.Warning:
                return _log.IsWarnEnabled;
            default:
                throw new ArgumentOutOfRangeException(nameof(logLevel));
        }
    }

    public void Log<TState>(LogLevel logLevel, EventId eventId, TState state,
        Exception exception, Func<TState, Exception, string> formatter)
    {
        if (!IsEnabled(logLevel))
        {
            return;
        }

        if (formatter == null)
        {
            throw new ArgumentNullException(nameof(formatter));
        }
        string message = null;
        message = formatter(state, exception);
        if (!string.IsNullOrEmpty(message) || exception != null)
        {
            switch (logLevel)
            {
                case LogLevel.Critical:
                    _log.Fatal(message);
                    break;
                case LogLevel.Debug:
                case LogLevel.Trace:
                    _log.Debug(message);
                    break;
                case LogLevel.Error:
                    _log.Error(message);
                    break;
                case LogLevel.Information:
                    _log.Info(message);
                    break;
                case LogLevel.Warning:
                    _log.Warn(message);
                    break;
                default:
                    _log.Warn($"Encountered unknown log level {logLevel}, writing out as Info.");
                    _log.Info(message, exception);
                    break;
            }
        }
    }
}
```

Then a `Microsoft.Extensions.Logging.ILoggingProvider` implementation:

```csharp
public class Log4NetProvider : ILoggerProvider
{
    private readonly string _log4NetConfigFile;
    private readonly ConcurrentDictionary<string, Log4NetLogger> _loggers =
        new ConcurrentDictionary<string, Log4NetLogger>();
    public Log4NetProvider(string log4NetConfigFile)
    {
        _log4NetConfigFile = log4NetConfigFile;
    }

    public ILogger CreateLogger(string categoryName)
    {
        return _loggers.GetOrAdd(categoryName, CreateLoggerImplementation);
    }

    public void Dispose()
    {
        _loggers.Clear();
    }
    private Log4NetLogger CreateLoggerImplementation(string name)
    {
        return new Log4NetLogger(name, ParseLog4NetConfigFile(_log4NetConfigFile));
    }

    private static XmlElement ParseLog4NetConfigFile(string filename)
    {
        var log4NetConfig = new XmlDocument();
        log4NetConfig.Load(File.OpenRead(filename));
        return log4NetConfig["log4net"];
    }
}
```

And some extensions to make it easier to use:

```csharp
public static class Log4netExtensions
{
    public static ILoggerFactory AddLog4Net(this ILoggerFactory factory, string log4NetConfigFile)
    {
        factory.AddProvider(new Log4NetProvider(log4NetConfigFile));
        return factory;
    }

    public static ILoggerFactory AddLog4Net(this ILoggerFactory factory)
    {
        factory.AddProvider(new Log4NetProvider("log4net.config"));
        return factory;
    }
}
```

Finally, we put it all together:

```csharp
ILoggerFactory factory = new LoggerFactory();
factory.AddLog4Net("log4net.config");

var ipAddressList = new List<string> { "10.112.205.101" };
var config = new ClusterOptions()
    .WithConnectionString(string.Concat("http://", string.Join(", ", ipAddressList)))
    .WithCredentials("Administrator", "password")
    .WithBuckets("default")
    .WithLogging(factory); //<= Need to add the ILoggerFactory via DI

config.KvConnectTimeout = TimeSpan.FromMilliseconds(12000);

var cluster = await Cluster.ConnectAsync(config);
var bucket = await cluster.BucketAsync("default");
Console.ReadKey();
```

Note that we suggest .NET Core or .NET 5.0 over using SDK3 in .NET Full Framework apps, as the integration is much more difficult.

## [](#sdk-telemetry-from-the-server)SDK Telemetry from the Server

In addition to Tracing and other metrics, and client logging, SDK telemetry is also sent to the Server — available from 8.0, and in new Capella Operational clusters — for ingestion with other Prometheus metrics. Capella Operational exposes these metrics through the UI.

For self-managed Server, collection can be disabled and enabled through the REST API:

```console
curl --user Administrator:password http://172.17.0.2:8091/settings/appTelemetry -d enabled=true
```

And the Prometheus-format metrics fetched with:

```console
curl --user Administrator:password http://172.17.0.2:8091/metrics
```

There may be advantages to collecting information this way, but note that metrics are collected per node, and a central Prometheus instance should be set to collect all metrics so that information is not lost in case of a sudden failover.

Also note that if the cluster is behind a load balancer, the collected metrics may not accurately record the actual correct node with which the SDK interacts.