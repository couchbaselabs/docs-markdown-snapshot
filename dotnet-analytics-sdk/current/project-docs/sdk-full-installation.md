---
title: Install the SDK
description: How to install the .NET Analytics SDK from NuGet.
editUrl: https://github.com/couchbase/docs-analytics-sdk-dotnet/edit/release/1.1/modules/project-docs/pages/sdk-full-installation.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:dotnet-analytics-sdk:project-docs:sdk-full-installation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-analytics-sdk/current/project-docs/sdk-full-installation.html)

# Install the SDK

> How to install the .NET Analytics SDK from NuGet. 

## [](#getting-the-sdk)Getting the SDK

Couchbase publishes all stable artifacts to [NuGet](https://www.nuget.org/profiles/couchbase).

Install using your preferred method:

### [](#net-cli).NET CLI

```shell
dotnet add package Couchbase.AnalyticsClient --version 1.1.0
```

### [](#add-to-csproj)Add to .csproj

```xml
<ItemGroup>
  <PackageReference Include="Couchbase.AnalyticsClient" Version="1.1.0" />
</ItemGroup>
```