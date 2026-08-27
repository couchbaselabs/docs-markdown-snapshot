---
title: Full Installation
description: Installation instructions for the Couchbase .NET Client.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.7/modules/project-docs/pages/sdk-full-installation.adoc
  xref: xref:3.7@dotnet-sdk:project-docs:sdk-full-installation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/3.7/project-docs/sdk-full-installation.html)

# Full Installation

> Installation instructions for the Couchbase .NET Client. 

This page covers installation of the SDK. A quick start guide in our [Getting Started Guide](../hello-world/start-using-sdk.md) should work for most users — and for anyone in a hurry to try out the SDK and our _Hello World_ program, that page is usually the best place to get started — but more detailed installation instructions are provided here on this page for every supported platform. This guide assumes you have some familiarity with development using .NET — if you are evaluating the SDK as a software architect, tester, or other non-.NET role, you will benefit from our [Platform Help page](../hello-world/platform-help.md).

## [](#net-compatibility).NET Compatibility

The Couchbase .NET SDK is compatible with [.NET Standard](https://docs.microsoft.com/en-us/dotnet/standard/net-standard) 2.0 and .NET Standard 2.1, via the currently supported Microsoft .NET SDKs. Currently, that includes [.NET 6.0 and later](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core) for .NET Standard 2.1 and [.NET Framework 4.6.2 and later](https://learn.microsoft.com/en-us/lifecycle/products/microsoft-net-framework) for .NET Standard 2.0\. The [.NET Standard documentation](https://docs.microsoft.com/en-us/dotnet/standard/net-standard) and [.NET Standard version chart](https://dotnet.microsoft.com/platform/dotnet-standard#versions) may be useful to help understand other available options.

Couchbase strongly recommends using the [latest LTS version of .NET that's officially supported](https://versionsof.net/) by both Microsoft and Couchbase. Other .NET implementations may work, but aren't tested, and are outside the scope of technical support. See the [Compatibility](compatibility.md#dotnet-compatibility) section for more details.

The library is distributed in a number of ways:

| NuGet             | NuGet package host at [nuget.org](https://www.nuget.org/packages/CouchbaseNetClient/) (_recommended_)                              |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Zip               | Zip files for each release are linked from the Release Notes [here](sdk-release-notes.md).                                         |
| Build from Source | Build the library from [source available on GitHub](https://github.com/couchbase/couchbase-net-client/) (not officially supported) |

## [](#installation)Installation

### [](#quick-installation-using-nuget)Quick Installation Using NuGet

For every release, we currently package the binaries and store the latest version in [NuGet](https://www.nuget.org/packages/CouchbaseNetClient/). If you are not familiar with NuGet, it's the official and most widely supported package manager for Microsoft Visual Studio and .NET in general.

#### [](#nuget-from-visual-studio)NuGet from Visual Studio

Using Visual Studio 2013 or later, follow these steps to get started with the Couchbase .NET SDK:

1. From the IDE, right-click the project you want to add the dependency to.
2. In the context menu, click **Manage NuGet Packages**. The NuGet package manager modal dialog opens.
3. From the Tree View menu on the left, select **Online > nuget.org**.
4. In the search box at the top right-hand side of the dialog, type CouchbaseNetClient and then press enter on your keyboard.
5. In the search results, select the CouchbaseNetClient package and then click **Install**.

#### [](#nuget-from-the-package-manager-console)NuGet from the Package Manager Console

From the Package Manager Console within your project:

1. From the Visual Studio menu bar, click **Tools**.
2. Select **NuGet Package Manager > Package Manager Console**.
3. In the console, enter the package installation command:

  * To install the latest version:

```console
 Install-Package CouchbaseNetClient
```

* To install a specific version, include the version parameter. For example:

```console
 Install-Package CouchbaseNetClient -Version 3.2.3
```

### [](#downloading-and-referencing-the-binaries)Downloading and referencing the binaries

If you do not want to use NuGet to include the Couchbase .NET SDK in your project, you can download and reference the binaries directly. If you chose this route, you'll also be responsible for including and resolving dependencies used internally by the SDK.

To download and reference the binaries directly:

1. Download the version of the SDK you want to install.
2. In Visual Studio, right-click the project you want to include the SDK in and then click **Add**.
3. Click **Reference** to open the Reference Manager.
4. On the left side, click **Browse** and select the binaries you downloaded.
5. Click **OK**.

After you have referenced the Couchbase .NET SDK binaries, you need to locate and reference the dependencies it uses in a similar fashion. At the time of this writing, the dependencies are:

* Apache Common Infrastructure Libraries for .NET v3.3.1: <https://www.nuget.org/packages/Common.Logging/3.3.1>
* Json.NET v9.0.1: [https://www.nuget.org/packages/Newtonsoft.Json/9.0.1](https://www.nuget.org/packages/Newtonsoft.Json/8.0.3)

Other versions might not be compatible with the current SDK version.

### [](#building-from-source)Building from source

If none of the other installation options suffice or if you want to debug the source or perhaps contribute, building directly from the source is the best option for you. All source is located on GitHub.

> [!NOTE]
> The software provided via NuGet and S3 are the official releases that have been through a rigorous testing process. Code on GitHub that is not tagged as an official release is still in development.

To build the .NET SDK from source:

1. (Optional) Fork the GitHub repository: <https://github.com/couchbase/couchbase-net-client/fork>
2. Using a Git console, enter the command to clone the repository:

```console
git clone https://github.com/couchbase/couchbase-net-client.git
```

1. Enter the command to retrieve the latest code from GitHub:

```console
git pull origin master
```

1. Navigate to the directory that the source was cloned to and open the solution.
2. Build the solution.

After you have successfully built the source, it's then just a matter of referencing the binaries (.DLL files) from your consuming project. _Note that you can checkout a specific tag for each release as well._