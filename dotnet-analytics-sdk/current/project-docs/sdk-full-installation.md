[View original HTML](/dotnet-analytics-sdk/current/project-docs/sdk-full-installation.html)

> How to install the .NET Analytics SDK from NuGet. 

## [](#getting-the-sdk)Getting the SDK

Couchbase publishes all stable artifacts to [NuGet](https://www.nuget.org/profiles/couchbase).

Install using your preferred method:

### [](#net-cli).NET CLI

```shell
dotnet add package Couchbase.AnalyticsClient --version 1.0.1
```

### [](#add-to-csproj)Add to .csproj

```xml
<ItemGroup>
  <PackageReference Include="Couchbase.AnalyticsClient" Version="1.0.1" />
</ItemGroup>
```