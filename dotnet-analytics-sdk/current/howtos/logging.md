[View original HTML](/dotnet-analytics-sdk/current/howtos/logging.html)

> Configuring logging with the .NET Analytics SDK. 

The .NET Analytics SDK emits log messages that can help with troubleshooting.

## [](#logging)Logging

An `ILoggerFactory` can be provided to the `ClusterOptions` when creating a `Cluster`.

Example 1\. Using Serilog

Using `Serilog` and wiring it to the SDK’s `Microsoft.Extensions.Logging` API:

Add the following dependencies to your project, as required:

```xml
<PackageReference Include="Microsoft.Extensions.Logging" />
<PackageReference Include="Serilog" />
<PackageReference Include="Serilog.Extensions.Logging" />
<PackageReference Include="Serilog.Sinks.Console" />
<PackageReference Include="Serilog.Sinks.File" />
```

```csharp
Log.Logger = new LoggerConfiguration()
    .MinimumLevel.Is(LogEventLevel.Debug)
    .Enrich.FromLogContext()
    .WriteTo.Console()
    .WriteTo.File(
        path: "Logs/my-logs.log",
        rollingInterval: RollingInterval.Day,
        shared: true)
    .CreateLogger();

var loggerFactory = LoggerFactory.Create(builder =>
{
    builder.ClearProviders();
    builder.AddSerilog();
});

var clusterOptions = new ClusterOptions().WithLogging(loggerFactory);

var credential = Credential.Create("username", "password");

var cluster = Cluster.Create(
    connectionString: "https://analytics.my-couchbase.example.com:18095",
    credential: credential,
    clusterOptions: clusterOptions
);
```

Using minimal logging without 3rd party sinks

```csharp
var loggerFactory = LoggerFactory.Create(builder =>
{
    builder.ClearProviders();
    builder.SetMinimumLevel(LogLevel.Debug);
    builder.AddConsole();
});
```