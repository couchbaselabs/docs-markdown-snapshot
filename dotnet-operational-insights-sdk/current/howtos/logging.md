---
title: Logging
description: Configuring logging with the .NET Operational Insights SDK.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: .NET Operational Insights SDK
    version: "1.0"
antora:
  editUrl: https://github.com/couchbase/docs-operational-insights-sdk-dotnet/edit/release/1.0/modules/howtos/pages/logging.adoc
  xref: xref:dotnet-operational-insights-sdk:howtos:logging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-operational-insights-sdk/current/howtos/logging.html)

# Logging

> Configuring logging with the .NET Operational Insights SDK. 

The .NET Operational Insights SDK emits log messages that can help with troubleshooting.

## [](#logging)Logging

An `ILoggerFactory` can be provided to the `ClusterOptions` when creating a `Cluster`.

Example 1\. Using Serilog

Using `Serilog` and wiring it to the SDK's `Microsoft.Extensions.Logging` API:

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
    connectionString: "https://insights.my-couchbase.example.com:18095",
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