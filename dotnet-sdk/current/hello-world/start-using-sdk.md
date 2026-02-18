---
title: Start Using the .NET SDK
description: The Couchbase .NET SDK enables you to interact with a Couchbase
  Server cluster from .NET using C# and other .NET languages.
editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.8/modules/hello-world/pages/start-using-sdk.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/dotnet-sdk/current/hello-world/start-using-sdk.html)

# Start Using the .NET SDK

> The Couchbase .NET SDK enables you to interact with a Couchbase Server cluster from .NET using C# and other .NET languages. It offers an asynchronous API based on the [_Task-based Asynchronous Pattern (TAP)_](https://docs.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/task-based-asynchronous-pattern-tap). 

The Couchbase .NET client allows applications to connect to Couchbase Server using any Common Language Runtime (CLR) language, including C#, F#, and VB.NET. The SDK is written in C#, and some of its idiomatic patterns reflect that choice.

In this guide, you will learn:

* How to [connect to Couchbase Capella or Couchbase Server](#connect).
* How to [add and retrieve Documents](#add-and-retrieve-documents).
* How to [lookup documents](#sql-lookup) with the [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) query language.

## [](#hello-couchbase)Hello Couchbase

We will go through the code sample step by step, but for those in a hurry to see it, here it is:

* Couchbase Capella Sample
* Local Couchbase Server

If you are connecting to [Couchbase Capella](https://docs.couchbase.com/cloud/index.html), be sure to get the correct endpoint as well as user, password — and see the [Cloud section](#cloud-connections), below.

```csharp
using System;
using System.Threading.Tasks;

namespace Couchbase.Net.DevGuide.Cloud;

public class Progam
{
    public static async Task Main(string[] args)
    {
        await new CloudExample().Main();
    }
}

class CloudExample
{
    public async Task Main()
    {
        var options = new ClusterOptions
        {
            // Update these credentials for your Capella instance
            UserName = "username",
            Password = "Password!123",
        };

        // Sets a pre-configured profile called "wan-development" to help avoid latency issues
        // when accessing Capella from a different Wide Area Network
        // or Availability Zone (e.g. your laptop).
        options.ApplyProfile("wan-development");

        var cluster = await Cluster.ConnectAsync(
            // Update these credentials for your Capella instance
            "couchbases://cb.<your-endpoint>.cloud.couchbase.com",
            options
        );

        // get a bucket reference
        var bucket = await cluster.BucketAsync("travel-sample");

        // get a user-defined collection reference
        var scope = await bucket.ScopeAsync("tenant_agent_00");
        var collection = await scope.CollectionAsync("users");

        // Upsert Document
        var upsertResult = await collection.UpsertAsync("my-document-key", new { Name = "Ted", Age = 31 });
        using var getResult = await collection.GetAsync("my-document-key");

        Console.WriteLine(getResult.ContentAs<dynamic>());

        // Call the QueryAsync() function on the scope object and store the result.
        var inventoryScope = bucket.Scope("inventory");
        var queryResult = await inventoryScope.QueryAsync<dynamic>("SELECT * FROM airline WHERE id = 10");
        
        // Iterate over the rows to access result data and print to the terminal.
        await foreach (var row in queryResult) {
            Console.WriteLine(row);
        }
    }
}
```

The Couchbase Capella free tier version comes with the Travel Sample Bucket, and its Query indexes, loaded and ready.

```csharp
using System;
using System.Threading.Tasks;
using Couchbase;await ExampleUsing();
async Task ExampleUsing()
{
    var cluster = await Cluster.ConnectAsync(
        // Update these credentials for your Local Couchbase instance!
        "couchbase://localhost",
        "Administrator",
        "password");

    // get a bucket reference
    var bucket = await cluster.BucketAsync("travel-sample");

    // get a user-defined collection reference
    var scope = await bucket.ScopeAsync("tenant_agent_00");
    var collection = await scope.CollectionAsync("users");

    // Upsert Document
    var upsertResult = await collection.UpsertAsync("my-document-key", new { Name = "Ted", Age = 31 });
    var getResult = await collection.GetAsync("my-document-key");

    Console.WriteLine(getResult.ContentAs<dynamic>());

    // Call the QueryAsync() function on the scope object and store the result.
    var inventoryScope = bucket.Scope("inventory");
    var queryResult = await inventoryScope.QueryAsync<dynamic>("SELECT * FROM airline WHERE id = 10");

    // Iterate over the rows to access result data and print to the terminal.
    await foreach (var row in queryResult) {
        Console.WriteLine(row);
    }
}
```

As well as the .NET SDK (see below), and a running instance of Couchbase Server, you will need to load up the Travel Sample Bucket using either the [Web interface](../../../server/7.2/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui)or the [command line](../../../server/7.2/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-cli).

## [](#installing-the-sdk)Installing the SDK

The Couchbase .NET SDK is compatible with [.NET Standard](https://docs.microsoft.com/en-us/dotnet/standard/net-standard) 2.0 and .NET Standard 2.1, via the currently supported Microsoft .NET SDKs. Currently, that includes [.NET 6.0 and later](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core) for .NET Standard 2.1 and [.NET Framework 4.6.2 and later](https://learn.microsoft.com/en-us/lifecycle/products/microsoft-net-framework) for .NET Standard 2.0\. The [.NET Standard documentation](https://docs.microsoft.com/en-us/dotnet/standard/net-standard) and [.NET Standard version chart](https://dotnet.microsoft.com/platform/dotnet-standard#versions) may be useful to help understand other available options.

Couchbase strongly recommends using the [latest LTS version of .NET that’s officially supported](https://versionsof.net/) by both Microsoft and Couchbase. Other .NET implementations may work, but aren’t tested, and are outside the scope of technical support. See the [Compatibility](../project-docs/compatibility.md#dotnet-compatibility) section for more details.

> [!NOTE]
> Capella’s root certificate is **not** signed by a well known CA (Certificate Authority). However, as the certificate is bundled with the SDK when using .NET 6.0 or later, it is trusted by default. .NET Framework clients will have to add it to the Windows certificate store.

### [](#quick-installation)Quick Installation

The quickest way to get up and running is with NuGet, from the Package Manager Console, within your project:

1. From the Visual Studio menu bar, click **Tools**.
2. Select **NuGet Package Manager > Package Manager Console**.
3. In the console, enter the package installation command:

  * To install the latest version:

```console
Install-Package CouchbaseNetClient
```

All other installation methods can be found in our [full installation guide](../project-docs/sdk-full-installation.md).

## [](#prerequisites)Prerequisites

The following code samples assume:

* Couchbase Capella
* Local Couchbase Server

* You have signed up to [Couchbase Capella](https://cloud.couchbase.com/sign-up).
* You have created your own bucket, or loaded the Travel Sample dataset. Note, the Travel Sample dataset is installed automatically when deploying a Capella free tier cluster.
* A user is created with permissions to access the cluster (at least Application Access permissions). See the [Capella connection page](../../../cloud/get-started/run-first-queries.md#credentials) for more details.

> [!IMPORTANT]
> Couchbase Capella uses [Roles](../../../cloud/organizations/organization-projects-overview.md) to control user access to cluster resources. For the purposes of this guide, you can use the **Organization Owner** role automatically assigned to your account during installation of the Capella cluster. In a production scenario, we strongly recommend setting up users with more granular access roles as a best practice.

* [Couchbase Server](#8.0@server:getting-started/do-a-quick-install.adoc) is installed and accessible locally.
* You have created your own bucket, or loaded the Travel Sample dataset using the [Web interface](../../../server/current/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui).
* A user is created with permissions to access your cluster (at least Application Access permissions). See [Manage Users, Groups and Roles](../../../server/current/manage/manage-security/manage-users-and-roles.md) for more details.

> [!IMPORTANT]
> Couchbase Server uses [Role Based Access Control (RBAC)](../../../server/current/learn/security/roles.md) to control access to resources. In this guide we suggest using the **Full Admin** role created during setup of your local Couchbase Server cluster. For production client code, you will want to use more appropriate, restrictive settings.

## [](#step-by-step)Step by Step

Start a new console project (in Visual Studio or VS Code, etc). Go to our [Platform Introduction](platform-help.md) if you don’t already have an editor or IDE setup for working in .NET — e.g. you are evaluating the .NET SDK, but .NET is not your normal platform.

Firstly, you will need to have a few `using` statements at the top of **Program.cs** in your console program:

```csharp
using System;
using System.Threading.Tasks;
using Couchbase;await ExampleUsing();
```

### [](#connect)Connect

Connect to your cluster by calling the `Cluster.ConnectAsync()` method and pass it your connection details. The basic connection details that you’ll need are given below — for more background information, see [Managing Connections](../howtos/managing-connections.md).

* Capella Connection
* Local Server Connection

From version 3.3, the .NET SDK includes Capella’s standard certificates by default, so you do not need to additional configuration. You do need to enable TLS, which can be done by simply using `couchbases://` in the connection string as in this example.

```csharp
var options = new ClusterOptions
{
    // Update these credentials for your Capella instance
    UserName = "username",
    Password = "Password!123",
};

// Sets a pre-configured profile called "wan-development" to help avoid latency issues
// when accessing Capella from a different Wide Area Network
// or Availability Zone (e.g. your laptop).
options.ApplyProfile("wan-development");

var cluster = await Cluster.ConnectAsync(
    // Update these credentials for your Capella instance
    "couchbases://cb.<your-endpoint>.cloud.couchbase.com",
    options
);
```

When accessing Capella from a different Wide Area Network or Availability Zone, you may experience latency issues with the default connection settings. SDK 3.4 introduces a `wan-development` Configuration Profile, which provides pre-configured timeout settings suitable for working in high latency environments. Basic usage is shown in the example above, but if you want to learn more see [Constrained Network Environments](../ref/client-settings.md#constrained-network-environments).

> [!CAUTION]
> The Configuration Profiles feature is currently a [Volatile API](../project-docs/compatibility.md#interface-stability) and may be subject to change.

```csharp
var cluster = await Cluster.ConnectAsync(
    // Update these credentials for your Local Couchbase instance!
    "couchbase://localhost",
    "Administrator",
    "password");
```

For developing locally on the same machine as Couchbase Server, your URI can be `couchbase://localhost`. For production deployments, you will want to use a secure server, with `couchbases://`.

Following successful authentication, add this code snippet to access your `Bucket`:

```csharp
// get a bucket reference
var bucket = await cluster.BucketAsync("travel-sample");
```

### [](#add-and-retrieve-documents)Add and Retrieve Documents

Collections allow Documents to be grouped by purpose or theme, according to specified _Scope_. Our Travel Sample bucket has separate scopes for inventory (flights, etc.), and for tenants (different travel agents).

```csharp
// get a user-defined collection reference
var scope = await bucket.ScopeAsync("tenant_agent_00");
var collection = await scope.CollectionAsync("users");
```

[Data operations](../howtos/kv-operations.md), like storing and retrieving documents, can be done using simple methods on the `Collection` class such as `Collection.GetAsync()` and `Collection.UpsertAsync()`.

To get you started the following code creates a new document in a custom scope and collection and then fetches it again, printing the result.

```csharp
// Upsert Document
var upsertResult = await collection.UpsertAsync("my-document-key", new { Name = "Ted", Age = 31 });
var getResult = await collection.GetAsync("my-document-key");

Console.WriteLine(getResult.ContentAs<dynamic>());
```

### [](#sql-lookup)SQL++ Lookup

Couchbase SQL++ queries can be performed at the `Cluster` or `Scope` level by invoking `Cluster.QueryAsync()` or `Scope.QueryAsync()`.

Cluster level queries require you to specify the fully qualified keyspace each time (e.g. `travel-sample.inventory.airline`). However, with a Scope level query you only need to specify the Collection name — which in this case is `airline`:

```csharp
// Call the QueryAsync() function on the scope object and store the result.
var inventoryScope = bucket.Scope("inventory");
var queryResult = await inventoryScope.QueryAsync<dynamic>("SELECT * FROM airline WHERE id = 10");

// Iterate over the rows to access result data and print to the terminal.
await foreach (var row in queryResult) {
    Console.WriteLine(row);
}
```

You can learn more about SQL++ queries on the [Query page](../howtos/n1ql-queries-with-sdk.md).

## [](#next-steps)Next Steps

Now you’re up and running, try one of the following:

* Our [Travel Sample Application](sample-application.md) demonstrates all the basics you need to know;
* Explore [Key Value Operations](../howtos/kv-operations.md) against a document database;
* Or [Query](../howtos/n1ql-queries-with-sdk.md) with our SQL-based SQL++ query language;
* Or read up on [which service fits your use case](../concept-docs/data-services.md).

### [](#additional-resources)Additional Resources

The [API reference](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/index.html) is generated for each release. Older API references are linked from their respective sections in the [Release Notes](../project-docs/sdk-release-notes.md).

[The Migrating from SDK2 to 3 page](../project-docs/migrating-sdk-code-to-3.n.md) highlights the main differences to be aware of when migrating your code from our earlier 2.x .NET SDK.

### [](#troubleshooting)Troubleshooting

* Couchbase Server is designed to work in the same WAN or availability zone as the client application. If you’re running the SDK on your laptop against a Capella cluster, see further information on:

  * Notes on [Constrained Network Environments](../ref/client-settings.md#constrained-network-environments).
  * [Network Requirements](../project-docs/compatibility.md#network-requirements).
  * If you have a consumer-grade router which has problems with DNS-SRV records review our [Troubleshooting Guide](../howtos/troubleshooting-cloud-connections.md#troubleshooting-host-not-found).
* Our [community forum](https://forums.couchbase.com/c/net-sdk/6) is a great source of help.