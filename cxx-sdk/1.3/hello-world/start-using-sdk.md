---
title: Hello World
description: Install, connect, try. A quick start guide to get you up and
  running with Couchbase and the C++ SDK.
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.3/modules/hello-world/pages/start-using-sdk.adoc
  xref: xref:1.3@cxx-sdk:hello-world:start-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/1.3/hello-world/start-using-sdk.html)

# Hello World

> Install, connect, try. A quick start guide to get you up and running with Couchbase and the C++ SDK. 

Couchbase has a simple interface for creating and modifying records in a document, based upon the **collection** into which the documents are organized. You can read more about data modeling [below](#data-modeling), but first let's look at those data operations, and installing the C++ SDK.

Creating a new database entry with the C++ SDK, using `upsert()`

```c++
auto collection = cluster.bucket(bucket_name).scope(scope_name).collection(collection_name);

const std::string document_id{ "minimal_example" };
const tao::json::value basic_doc{
        { "a", 1.0 },
        { "b", 2.0 },
};

auto [err, res] = collection.upsert(document_id, basic_doc, {}).get();
if (err) {
    fmt::println("Unable to perform upsert: {}", err);
} else {
    fmt::println("id: {}, CAS: {}", document_id, res.cas().value());
}
```

`upsert` inserts (creates) the document if it does not exist, or replaces it if it does. We'll explore creating and retrieving data records in more detail [below](#create-read-update-delete), after walking through a quick installation.

## [](#before-you-start)Before You Start

Couchbase Capella, our Database-as-a-Service, lets you get on with what matters, while we take care of the administration for you. Alternately, if you need to control every aspect of deployment — or just want to run the Server in a VM on your laptop — there are several self-managed options available:

* Couchbase Capella
* Self-Managed Couchbase Server

If you haven't already got a cluster set up, the easiest route is to [sign up to Couchbase Capella and deploy a free tier operational cluster](https://cloud.couchbase.com/sign-up), then come back to this page. Make a note of the [endpoint](../../../cloud/get-started/connect.md) to connect to, and remember the credentials for the user that you set up.

Install Couchbase Server locally, or in your private Cloud:

* [Deployment overview](../../../server/current/install/get-started.md)
* [Docker Install](../../../server/current/install/getting-started-docker.md)
* [Couchbase Autonomous Operator](../../../operator/current/overview.md)

  * [Kubernetes](../../../operator/current/install-kubernetes.md)
  * [Openshift](../../../operator/current/install-openshift.md)
* [Cloud Marketplace](#8.0server:cloud:couchbase-cloud-deployment.adoc):

  * [AWS Marketplace](../../../server/current/cloud/couchbase-aws-marketplace.md)
  * [Azure Marketplace](../../../server/current/cloud/couchbase-azure-marketplace.md)
  * [GCP Marketplace](../../../server/current/cloud/couchbase-gcp-cloud-launcher.md)

For the example code below to run, you'll need the username and password of the Administrator user that you create, and the IP address of at least one of the nodes of the cluster.

### [](#prerequisites)Prerequisites

Check that you have the dependencies installed:

* C++ 17 compiler
* [CMake](https://cmake.org/) version 3.19 or newer

Supprted Operating Systems are listed on the [compatibility page](../project-docs/compatibility.md#platform-compatibility).

The code examples also assume:

* Couchbase Capella
* Self-Managed Couchbase Server

* You have signed up to [Couchbase Capella](https://cloud.couchbase.com/sign-up).
* You have created your own bucket, or loaded the Travel Sample dataset. Note, the Travel Sample dataset is installed automatically when deploying a Capella free tier cluster.
* A user is created with permissions to access the cluster (at least Application Access permissions). See the [Capella connection page](../../../cloud/get-started/run-first-queries.md#credentials) for more details.

> [!IMPORTANT]
> Couchbase Capella uses [Roles](../../../cloud/organizations/organization-projects-overview.md) to control user access to cluster resources. For the purposes of this guide, you can use the **Organization Owner** role automatically assigned to your account during installation of the Capella cluster. In production, Couchbase strongly recommends setting up users with more granular access roles as a best practice for data security.

* [Couchbase Server](#8.0@server:getting-started/do-a-quick-install.adoc) is installed and accessible locally.
* You have created your own bucket, or loaded the Travel Sample dataset using the [Web interface](../../../server/current/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui).
* A user is created with permissions to access your cluster (at least Application Access permissions). See [Manage Users, Groups and Roles](../../../server/current/manage/manage-security/manage-users-and-roles.md) for more details.

> [!IMPORTANT]
> Couchbase Server uses [Role-Based Access Control (RBAC)](../../../server/current/learn/security/roles.md) to control access to cluster resources. In this guide we suggest using the **Full Admin** role created during setup of your local Couchbase Server cluster. In production, Couchbase strongly recommends setting up users with more granular access roles as a best practice for data security.

## [](#installation)Installation

More details of the installation process are in the [full installation guide](../project-docs/sdk-full-installation.md).

[CPM.cmake](https://github.com/cpm-cmake/CPM.cmake) is the recommended way to include the library in your project. You need to include the following command in your `CMakeLists.txt`.

```cmake
CPMAddPackage(
  NAME
  couchbase_cxx_client
  GIT_TAG
  1.3.2
  VERSION
  1.3.2
  GITHUB_REPOSITORY
  "couchbase/couchbase-cxx-client"
  OPTIONS
  "COUCHBASE_CXX_CLIENT_STATIC_BORINGSSL ON")
```

### [](#ide-plugins)IDE Plugins

To make development easier, Couchbase plugins are available for VSCode and the IntelliJ family of IDEs and editors. For links and more information on these and other integrations across the C++ ecosystem, check out the [Integrations & Ecosystem](../project-docs/third-party-integrations.md) page.

## [](#connect-to-your-database)Connect to your Database

Connect to your Couchbase Capella operational cluster (or your local Couchbase Cluster, if you are trying out self-managed Couchbase).

* Couchbase Capella
* Self-Managed Couchbase Server

```c++
auto options = couchbase::cluster_options(username, password);
options.apply_profile("wan_development");

auto [err, cluster] = couchbase::cluster::connect(connection_string, options).get();

if (err) {
    fmt::println("Unable to connect to the cluster: {}", err);
} else {
    // Application code here
}
```

Note, the client certificate for connecting to a Capella cluster is included in the SDK installation.

```c++
couchbase::cluster_options options(username, password);

auto [err, cluster] = couchbase::cluster::connect(connection_string, options).get();
if (err) {
    fmt::println("Unable to connect to the cluster: {}", err);
} else {
    // Application code here
}
```

For a deeper look at connection options, read [Managing Connections](../howtos/managing-connections.md).

> [!TIP]
> The connection code for getting started uses the Administrator password that you were given during set up. In any production app you should create a role restricted to the permissions needed for your app — more on this in [the Security documentation](../concept-docs/best-practices.md#roles-and-rbac).

## [](#create-read-update-delete)Create, Read, Update, Delete

Couchbase documents are organized into buckets, scopes, and collections. [CRUD operations](https://en.wikipedia.org/wiki/CRUD) — Create, Read, Update, Delete — can be performed upon documents in a collection.

### [](#insert-create-and-upsert)Insert (Create) and Upsert

`insert` and `upsert` will both create a new document. The difference between the two is that if a document with that key already exists, the `insert` operation will fail, returning a `document_exists` error — while the `upsert` operation will succeed, replacing the content.

### [](#get-read)Get (Read)

The `get` method reads a document from a collection. If the collection does not have a document with this ID, the `get` method also returns a `document_not_found` error.

```c++
const std::string document_id{ "minimal_example" };

auto collection = cluster.bucket(bucket_name).scope(scope_name).collection(collection_name);

auto [err, res] = collection.get(document_id).get();

if (err) {
    fmt::println("Unable to perform get: {}", err);
} else {
    std::cout << "id: " << document_id << ", result: " << res.content_as<tao::json::value>() << "\n";
}
```

### [](#replace-update-and-overloads)Replace (Update) and Overloads

The replace method updates the value of an existing document

```c++
auto collection = cluster.bucket(bucket_name).scope(scope_name).collection(collection_name);

const std::string document_id{ "minimal_example" };
const tao::json::value basic_doc{
        { "a", 1.0 },
        { "b", 2.0 },
};

auto [err, res] = collection.replace(document_id, basic_doc).get();
if (err) {
    fmt::println("Unable to perform replace: {}", err);
} else {
    fmt::println("id: {}, CAS: {}", document_id, res.cas().value());
}
```

> [!CAUTION]
> When you replace a document, it's usually good practice to use [optimistic locking](../howtos/kv-operations.md#optimistic-locking). Otherwise, changes might get lost if two people change the same document at the same time.

### [](#remove-delete)Remove (Delete)

The remove method deletes a document from a collection:

```c++
auto collection = cluster.bucket(bucket_name).scope(scope_name).collection(collection_name);

const std::string document_id{ "minimal_example" };

auto [err, res] = collection.remove(document_id).get();
if (err) {
    fmt::println("Unable to perform remove: {}", err);
} else {
    fmt::println("id: {}, CAS: {}", document_id, res.cas().value());
}
```

## [](#data-modeling)Data Modeling

Documents are organized into collections — collections of documents that belong together. You get to decide what it means to "belong." Developers usually put documents of the same type in the same collection.

For example, imagine you have two types of documents: customers and invoices. You could put the customer documents in a collection called `customers`, and the invoice documents in a collection called `invoices`.

Each document belongs to exactly one collection. A document's ID is unique _within_ the collection.

Different scopes can hold collections with different names. There is no relationship between collections in different scopes. Each collection belongs to just one scope and a collection's name is unique within the scope.

More details can be found on the [Data Model page](../concept-docs/data-model.md).

## [](#what-next)What Next?

### [](#help-and-troubleshooting)Help and Troubleshooting

* [Troubleshooting common network problems](../howtos/troubleshooting-cloud-connections.md).
* [Discord channel](https://discord.com/channels/915294689681362954/1217642561645318194).
* Read the [error handling page](../howtos/error-handling.md).
* [Get help from Couchbase iQ](../../../cloud/get-started/capella-iq/get-started-with-iq.md#generate-sdk-code-preview).

### [](#next-steps)Next Steps

* [Learn more about the Data Service](../concept-docs/data-durability-acid-transactions.md).
* [Discover SQL++](../concept-docs/querying-your-data.md) — our SQL-family querying language.
* Explore some of the [third party integrations](../project-docs/third-party-integrations.md) with Couchbase and the C++ SDK, across the C++ ecosystem.