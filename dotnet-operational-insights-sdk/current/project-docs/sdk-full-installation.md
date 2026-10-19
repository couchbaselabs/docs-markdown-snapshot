---
title: Install the SDK
description: How to install the .NET Operational Insights SDK from NuGet.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: .NET Operational Insights SDK
    version: "1.0"
antora:
  editUrl: https://github.com/couchbase/docs-operational-insights-sdk-dotnet/edit/release/1.0/modules/project-docs/pages/sdk-full-installation.adoc
  xref: xref:dotnet-operational-insights-sdk:project-docs:sdk-full-installation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-operational-insights-sdk/current/project-docs/sdk-full-installation.html)

# Install the SDK

> How to install the .NET Operational Insights SDK from NuGet. 

## [](#getting-the-sdk)Getting the SDK

Couchbase publishes all stable artifacts to [NuGet](https://www.nuget.org/profiles/couchbase).

Install using your preferred method:

### [](#net-cli).NET CLI

```console
dotnet add package Couchbase.OperationalInsightsClient --version 1.0.0
```

### [](#add-to-csproj)Add to .csproj

```xml
<ItemGroup>
  <PackageReference Include="Couchbase.OperationalInsightsClient" Version="1.0.0" />
</ItemGroup>
```