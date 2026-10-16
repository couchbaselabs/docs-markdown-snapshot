---
title: Hello World
description: Install, connect, try. A quick start guide to get you up and
  running with Couchbase and the .NET SDK.
pubDate: 2026-10-16T07:26:40.932Z
meta:
  component:
    title: .NET SDK
    version: "3.10"
antora:
  editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/release/3.10/modules/hello-world/pages/start-using-sdk.adoc
  xref: xref:dotnet-sdk:hello-world:start-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/current/hello-world/start-using-sdk.html)

# Hello World

> Install, connect, try. A quick start guide to get you up and running with Couchbase and the .NET SDK. 

Couchbase has a simple interface for creating and modifying records in a document, based upon the **collection** into which the documents are organized. You can read more about data modeling [below](#data-modeling), but first let's look at those data operations, and installing the .NET SDK.

Creating a new database entry with the .NET SDK, using `upsert()`

```csharp
var document = new { foo = "bar", bar = "foo" };
var result = await collection.UpsertAsync("document-key", document,
    options =>
    {
        options.Expiry(TimeSpan.FromMinutes(1));
        options.Durability(DurabilityLevel.Majority);
        options.Timeout(TimeSpan.FromSeconds(5));
    }
);
```

`upsert` inserts (creates) the document if it does not exist, or replaces it if it does. We'll explore creating and retrieving data records in more detail [below](#create-read-update-delete)after walking through a quick installation.

## [](#before-you-start)Before You Start

Couchbase Capella, our Database-as-a-Service, lets you get on with what matters, while we take care of the administration for you. Alternately, if you need to control every aspect of deployment — or just want to run the Server in a VM on your laptop — there are several self-managed options available:

* Couchbase Capella
* Self-Managed Couchbase Server

If you haven't already got a cluster set up, the easiest route is to [sign up to a trial of Couchbase Capella](https://cloud.couchbase.com/sign-up), then come back to this page. Make a note of the [endpoint](../../../cloud/get-started/connect.md) to connect to, and remember the credentials for the user that you set up.

You may want to look at one of the self-managed installation options:

* [Deployment overview](../../../server/current/install/get-started.md)
* [Docker Install](../../../server/current/install/getting-started-docker.md)
* [Couchbase Autonomous Operator](../../../operator/current/overview.md)

  * [Kubernetes](../../../operator/current/install-kubernetes.md)
  * [Openshift](../../../operator/current/install-openshift.md)
* [Cloud Marketplace](#8.0server:cloud:couchbase-cloud-deployment.adoc):

  * [AWS Marketplace](../../../server/current/cloud/couchbase-aws-marketplace.md)
  * [Azure Marketplace](../../../server/current/cloud/couchbase-azure-marketplace.md)
  * [GCP Marketplace](../../../server/current/cloud/couchbase-gcp-cloud-launcher.md)

### [](#prerequisites)Prerequisites

The Couchbase .NET SDK is compatible with [.NET Standard](https://docs.microsoft.com/en-us/dotnet/standard/net-standard) 2.0 and .NET Standard 2.1, via the currently supported Microsoft .NET SDKs. Currently, that includes [.NET 6.0 and later](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core) for .NET Standard 2.1 and [.NET Framework 4.6.2 and later](https://learn.microsoft.com/en-us/lifecycle/products/microsoft-net-framework) for .NET Standard 2.0\. The [.NET Standard documentation](https://docs.microsoft.com/en-us/dotnet/standard/net-standard) and [.NET Standard version chart](https://dotnet.microsoft.com/platform/dotnet-standard#versions) may be useful to help understand other available options.

Couchbase strongly recommends using the [latest LTS version of .NET that's officially supported](https://versionsof.net/) by both Microsoft and Couchbase. Other .NET implementations may work, but aren't tested, and are outside the scope of technical support. See the [Compatibility](../project-docs/compatibility.md#dotnet-compatibility) section for more details.

The code examples also assume:

* Couchbase Capella
* Self-Managed Couchbase Server

* You have signed up to [Couchbase Capella](https://cloud.couchbase.com/sign-up).
* You have created your own bucket, or loaded the Travel Sample dataset. Note, the Travel Sample dataset is installed automatically by the Capella free trial.
* A user is created with permissions to access the cluster (at least Application Access permissions). See the [Capella connection page](../../../cloud/get-started/run-first-queries.md#credentials) for more details.

> [!IMPORTANT]
> Couchbase Capella uses [Roles](../../../cloud/organizations/organization-projects-overview.md) to control user access to cluster resources. For the purposes of this guide, you can use the **Organization Owner** role automatically assigned to your account during installation of the Capella cluster. In production, Couchbase strongly recommends setting up users with more granular access roles as a best practice for data security.

* [Couchbase Server](#8.0@server:getting-started/do-a-quick-install.adoc) is installed and accessible locally.
* You have created your own bucket, or loaded the Travel Sample dataset using the [Web interface](../../../server/current/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui).
* A user is created with permissions to access your cluster (at least Application Access permissions). See [Manage Users, Groups and Roles](../../../server/current/manage/manage-security/manage-users-and-roles.md) for more details.

> [!IMPORTANT]
> Couchbase Server uses [Role-Based Access Control (RBAC)](../../../server/current/learn/security/roles.md) to control access to cluster resources. In this guide we suggest using the **Full Admin** role created during setup of your local Couchbase Server cluster. In production, Couchbase strongly recommends setting up users with more granular access roles as a best practice for data security.

## [](#installation)Installation

The quickest way to get up and running is with NuGet, from the Package Manager Console, within your project:

1. From the Visual Studio menu bar, click **Tools**.
2. Select **NuGet Package Manager > Package Manager Console**.
3. In the console, enter the package installation command:

  * To install the latest version:

```console
Install-Package CouchbaseNetClient
```

All other installation methods can be found in our [full installation guide](../project-docs/sdk-full-installation.md).

### [](#ide-plugins)IDE Plugins

To make development easier, Couchbase plugins are available for VSCode and the IntelliJ family of IDEs and editors. For links and more information on these and other integrations across the .NET ecosystem, check out the [3rd Party Integrations](../project-docs/third-party-integrations.md) page.

### [](#grab-the-code)Grab the Code

If you're all set up and in a real hurry, just grab this code sample and add in your Capella details.

Complete Hello World code sample \[**Click to open or collapse the listing**\] 

```csharp
include::devguide:example$dotnet/StartUsingCapella.cs[]
```

Otherwise, read on as we introduce the CRUD API and connection to Capella or self-managed Couchbase Server.

> [!TIP]
> There's a **View** link to the complete sample code on GitHub above each of the snippets on the page, and a **Copy** icon to grab just the snippet shown.

## [](#connect-to-your-database)Connect to your Database

Connect to your Couchbase Capella operational cluster (or your local Couchbase Cluster, if you are trying out self-managed Couchbase).

* Couchbase Capella
* Self-Managed Couchbase Server
* Cloud Native Gateway (CNG)

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

```csharp
var cluster = await Cluster.ConnectAsync(
    // Update these credentials for your Local Couchbase instance!
    "couchbase://localhost",
    "Administrator",
    "password");
```

Couchbase's large number of ports across the URLs of many services can be proxied by using a `couchbase2://` endpoint as the connection string — compatible with recent versions of [Couchbase Autonomous Operator](../../../cloud-native-gateway/current/intro/about-cng.md) or [install alongside self-managed Server](../../../cloud-native-gateway/current/intro/about-cng.md):

```csharp
    var cluster = await Cluster.ConnectAsync(
        // Update these credentials for your Local Couchbase instance!
        "couchbase2://<your-ip-address>",
        "Administrator",
        "password");
```

Read more on the [Connections](../howtos/managing-connections.md#cloud-native-gateway) page.

For a deeper look at connection options, read [Managing Connections](../howtos/managing-connections.md).

> [!TIP]
> The connection code for getting started uses the Administrator password that you were given during set up. In any production app you should create a role restricted to the permissions needed for your app — more on this in [the Security documentation](../concept-docs/best-practices.md#roles-and-rbac).

### [](#opening-a-bucket)Opening a Bucket

Following successful authentication, open the bucket with:

```csharp
public class ClusterExample
{
    public async Task ExecuteAsync()
    {
        var cluster = await Cluster.ConnectAsync("your-ip", "Administrator", "password");
        await cluster.WaitUntilReadyAsync(TimeSpan.FromSeconds(10));
        var bucket = await cluster.BucketAsync("travel-sample");
        var collection = bucket.DefaultCollection();
        //..
    }
}
```

`waitUntilReady` is an optional call, but it is good practice to use it. Opening resources such as buckets is asynchronous — that is, the `cluster.bucket` call returns immediately and proceeds in the background. `waitUntilReady` ensures that the bucket resource is fully loaded before proceeding. If not present, then the first key-value (KV) operation on the bucket will wait for it to be ready.

**Collections** allow documents to be grouped by purpose or theme, according to a specified **scope** — see data modeling, [below](#data-modeling). Here we will use the `airport` collection within the `inventory` scope from `travel-sample` bucket as an example.

```csharp
var scope = await bucket.ScopeAsync("inventory");
var collection = await scope.CollectionAsync("airport");
```

## [](#create-read-update-delete)Create, Read, Update, Delete

Couchbase documents are organized into buckets, scopes, and collections. [CRUD operations](https://en.wikipedia.org/wiki/CRUD) — Create, Read, Update, Delete — can be performed upon documents in a collection.

### [](#insert-create-and-upsert)Insert (Create) and Upsert

[Data operations](../howtos/kv-operations.md), like storing and retrieving documents, can be done using simple methods on the `Collection` class such as `Collection.InsertAsync()` and `Collection.UpsertAsync()`. `insert` and `upsert` will both create a new document. The difference between the two is that if a document with that key already exists, the `insert` operation will fail, throwing a `DocumentExistsException` — while the `upsert` operation will succeed, replacing the content.

Insert

```csharp
var document = new {foo = "bar", bar = "foo"};
try {
    var result = await collection.InsertAsync("document-key", document);
}
catch (DocumentExistsException) {
    Console.WriteLine("Document already exists");
}
```

### [](#get-read)Get (Read)

The `get` method reads a document from a collection. If the collection does not have a document with this ID, the `get` method also throws `DocumentNotFoundException`.

The following code snippet creates a new document in a custom scope and collection and then fetches it again, printing the result.

```csharp
// Upsert Document
var upsertResult = await collection.UpsertAsync("my-document-key", new { Name = "Ted", Age = 31 });
var getResult = await collection.GetAsync("my-document-key");

Console.WriteLine(getResult.ContentAs<dynamic>());
```

### [](#replace-update-and-overloads)Replace (Update) and Overloads

The replace method updates the value of an existing document. Here we add a couple of useful options for expiry and timeout — read more on our [using the Data Service](../howtos/kv-operations.md) page.

```csharp
var previousResult = await collection.GetAsync("document-key");
var cas = previousResult.Cas;

var document = new {foo = "bar", bar = "foo"};

var result = await collection.ReplaceAsync("document-key", document,
    options =>
    {
        options.Cas(cas);
        options.Expiry(TimeSpan.FromMinutes(1));
        options.Timeout(TimeSpan.FromSeconds(5));
    }
);
```

> [!CAUTION]
> When you replace a document, it's usually good practice to use [optimistic locking](../howtos/kv-operations.md#optimistic-locking). Otherwise, changes might get lost if two people change the same document at the same time.

### [](#remove-delete)Remove (Delete)

When removing a document, you will have the same concern for durability as with any additive modification to the Bucket:

Remove (with options)

```csharp
var previousResult = await collection.GetAsync("document-key");

await collection.RemoveAsync("document-key",
    options =>
    {
        options.Cas(previousResult.Cas);
        options.Timeout(TimeSpan.FromSeconds(5));
    }
);
```

Like `Replace`, `Remove` also optionally takes the [CAS value](../howtos/kv-operations.md#what-is-cas) if you want to make sure you are only removing the document if it hasn't changed since you last fetched it.

## [](#data-modeling)Data Modeling

Documents are organized into collections — collections of documents that belong together. You get to decide what it means to "belong". Developers usually put documents of the same type in the same collection.

For example, imagine you have two types of documents: customers and invoices. You could put the customer documents in a collection called `customers`, and the invoice documents in a collection called `invoices`.

Each document belongs to exactly one collection. A document's ID is unique _within_ the collection.

Different scopes can hold collections with different names. There is no relationship between collections in different scopes.

Each collection belongs to just one scope. A collection's name is unique within the scope.

More details can be found on the [Data Model page](#concept-docs.data-model.adoc). The [Student Records Tutorial](#student-record-developer-tutorial.adoc) gives an introduction to data modeling in a document database alongside using the .NET SDK.

## [](#what-next)What Next?

### [](#help-and-troubleshooting)Help and Troubleshooting

* [Troubleshooting common network problems](../howtos/troubleshooting-cloud-connections.md).
* [Help forum](https://www.couchbase.com/forums/c/scala-sdk/37).
* [Discord channel](https://discord.com/channels/915294689681362954/955424070076338177).
* Read the [error handling page](../howtos/error-handling.md).
* [Get help from Couchbase iQ](../../../cloud/get-started/capella-iq/get-started-with-iq.md#generate-sdk-code-preview).

### [](#next-steps)Next Steps

* Take a look at the [Sample Application](sample-application.md).
* [Learn more about the Data Service](../concept-docs/data-durability-acid-transactions.md).
* [Discover SQL++](../concept-docs/querying-your-data.md) — our SQL-family querying language.
* Explore some of the [third party integrations](../project-docs/third-party-integrations.md) with Couchbase and the .NET SDK, across the .NET ecosystem.