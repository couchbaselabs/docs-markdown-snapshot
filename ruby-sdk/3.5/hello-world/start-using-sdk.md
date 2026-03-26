---
title: Start Using the Ruby SDK
description: A quick start guide to get you up and running with Couchbase and the Ruby SDK.
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.5/modules/hello-world/pages/start-using-sdk.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.5@ruby-sdk:hello-world:start-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/3.5/hello-world/start-using-sdk.html)

# Start Using the Ruby SDK

> A quick start guide to get you up and running with Couchbase and the Ruby SDK. 

The Couchbase Ruby SDK allows you to connect to a Couchbase cluster from Ruby. The Ruby SDK includes high-performance native Ruby extensions to handle communicating to the cluster over Couchbase's binary protocols.

Ruby SDK supports [currently maintained Ruby versions](https://www.ruby-lang.org/en/downloads/branches/), and recommends the latest stable version where possible (currently 3.3 as of March 2024).

In this guide, you will learn:

* How to [connect to Couchbase Capella or Couchbase Server](#connect).
* How to [add and retrieve Documents](#add-and-retrieve-documents).
* How to [lookup documents](#sql-lookup) with the [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) query language.

## [](#hello-couchbase)Hello Couchbase

We will go through the code sample step by step, but for those in a hurry to see it, here it is:

* Couchbase Capella Sample
* Local Couchbase Server

If you are connecting to [Couchbase Capella](https://docs.couchbase.com/cloud/index.html), be sure to get the correct endpoint as well as user, password — and see the [Cloud section](#cloud-connections), below.

```ruby
require "couchbase"

# Update these credentials for your Capella instance!
options = Cluster::Options::Cluster.new
options.authenticate("username", "Password!123")

# Sets a pre-configured profile called "wan-development" to help avoid latency issues
# when accessing Capella from a different Wide Area Network
# or Availability Zone (e.g. your laptop).
options.apply_profile("wan_development")

cluster = Cluster.connect("couchbases://cb.<your-endpoint>.cloud.couchbase.com", options)

# get a bucket reference
bucket = cluster.bucket("travel-sample")

# get a user-defined collection reference
scope = bucket.scope("tenant_agent_00")
collection = scope.collection("users")

# Upsert Document
upsert_result = collection.upsert(
  "my-document-key",
  {
    "name" => "Ted",
    "age" => 31
  }
)
p cas: upsert_result.cas
#=> {:cas=>223322674373654}

# Get Document
get_result = collection.get("my-document-key")
p cas: get_result.cas,
  name: get_result.content["name"]
#=> {:cas=>223322674373654, :name=>"Ted"}

inventory_scope = bucket.scope("inventory")
result = inventory_scope.query('SELECT * FROM airline WHERE id = 10;')
result.rows.each do |row|
  p row
end

cluster.disconnect
```

The Couchbase Capella free tier version comes with the Travel Sample Bucket, and its Query indexes, loaded and ready.

```ruby
require "couchbase"

# Update these credentials for your Local instance!
options = Cluster::ClusterOptions.new
options.authenticate("username", "Password!123")
cluster = Cluster.connect("couchbase://localhost", options)

# get a bucket reference
bucket = cluster.bucket("travel-sample")

# get a user-defined collection reference
scope = bucket.scope("tenant_agent_00")
collection = scope.collection("users")

# Upsert Document
upsert_result = collection.upsert(
  "my-document-key",
  {
    "name" => "Ted",
    "age" => 31
  }
)
p cas: upsert_result.cas
#=> {:cas=>223322674373654}

# Get Document
get_result = collection.get("my-document-key")
p cas: get_result.cas,
  name: get_result.content["name"]
#=> {:cas=>223322674373654, :name=>"Ted"}

inventory_scope = bucket.scope("inventory")
result = inventory_scope.query('SELECT * FROM airline WHERE id = 10;')
result.rows.each do |row|
  p row
end

cluster.disconnect
```

As well as the Ruby SDK (see below), and a running instance of Couchbase Server, you will need to load up the Travel Sample Bucket using either the [Web interface](../../../server/7.6/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui)or the [command line](../../../server/7.6/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-cli).

## [](#quick-installation)Quick Installation

The source package is available through <https://rubygems.org/gems/couchbase> and can be installed with

```console
gem install couchbase
```

In addition to rubygems.org, we also maintain official gem repositories, where we publish not only source version of the package, but also precompiled binaries for Linux and MacOS.

## [](#prerequisites)Prerequisites

The following code samples assume:

* Couchbase Capella
* Local Couchbase Server

* You have signed up to [Couchbase Capella](https://cloud.couchbase.com/sign-up).
* You have created your own bucket, or loaded the Travel Sample dataset. Note, the Travel Sample dataset is installed automatically when deploying a Capella free tier cluster.
* A user is created with permissions to access the cluster (at least Application Access permissions). See the [Capella connection page](../../../cloud/get-started/run-first-queries.md#credentials) for more details.

> [!IMPORTANT]
> Couchbase Capella uses [Roles](../../../cloud/organizations/organization-projects-overview.md) to control user access to cluster resources. For the purposes of this guide, you can use the **Organization Owner** role automatically assigned to your account during installation of the Capella cluster. In a production scenario, we strongly recommend setting up users with more granular access roles as a best practice.

* [Couchbase Server](#7.6@server:getting-started/do-a-quick-install.adoc) is installed and accessible locally.
* You have created your own bucket, or loaded the Travel Sample dataset using the [Web interface](../../../server/7.6/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui).
* A user is created with permissions to access your cluster (at least Application Access permissions). See [Manage Users, Groups and Roles](../../../server/7.6/manage/manage-security/manage-users-and-roles.md) for more details.

> [!IMPORTANT]
> Couchbase Server uses [Role Based Access Control (RBAC)](../../../server/7.6/learn/security/roles.md) to control access to cluster resources. In this guide we suggest using the **Full Admin** role created during setup of your local Couchbase Server cluster. For production client code, you will want to use more appropriate, restrictive settings.

## [](#step-by-step)Step-by-step

Start a new project (in VS Code or RubyMine, etc.) and create a file `cb-test.rb`.

Firstly, you will need to have `require` statement at the top of your Ruby program:

```ruby
require "couchbase"
```

### [](#connect)Connect

Connect to your cluster by calling the `Cluster.connect()` method and pass it your connection details. The basic connection details that you'll need are given below — for more background information, see [Managing Connections](../howtos/managing-connections.md).

* Capella Connection
* Local Server Connection

From version 3.3, the Ruby SDK includes Capella's standard certificates by default, so you do not need to additional configuration. You do need to enable TLS, which can be done by simply using `couchbases://` in the connection string as in this example.

```ruby
# Update these credentials for your Capella instance!
options = Cluster::Options::Cluster.new
options.authenticate("username", "Password!123")

# Sets a pre-configured profile called "wan-development" to help avoid latency issues
# when accessing Capella from a different Wide Area Network
# or Availability Zone (e.g. your laptop).
options.apply_profile("wan_development")

cluster = Cluster.connect("couchbases://cb.<your-endpoint>.cloud.couchbase.com", options)
```

When accessing Capella from a different Wide Area Network or Availability Zone, you may experience latency issues with the default connection settings. SDK 3.4 introduces a `wan_development` Configuration Profile, which provides pre-configured timeout settings suitable for working in high latency environments. Basic usage is shown in the example above, but if you want to learn more see [Constrained Network Environments](../ref/client-settings.md#constrained-network-environments).

> [!CAUTION]
> The Configuration Profiles feature is currently a [Volatile API](../../current/project-docs/compatibility.md#interface-stability) and may be subject to change.

```ruby
# Update these credentials for your Local instance!
options = Cluster::ClusterOptions.new
options.authenticate("username", "Password!123")
cluster = Cluster.connect("couchbase://localhost", options)
```

For developing locally on the same machine as Couchbase Server, your URI can be `couchbase://localhost` as shown here. For production deployments, you will want to use a secure server, with `couchbases://`.

Following successful authentication, add this code snippet to access your `Bucket`:

```ruby
# get a bucket reference
bucket = cluster.bucket("travel-sample")
```

### [](#add-and-retrieve-documents)Add and Retrieve Documents

Collections allow Documents to be grouped by purpose or theme, according to specified _Scope_. Our Travel Sample bucket has separate scopes for inventory (flights, etc.), and for tenants (different travel agents).

Here we refer to the `users` collection within the `tenant_agent_00` scope from the Travel Sample bucket as an example, but you may replace this with your own data.

```ruby
# get a user-defined collection reference
scope = bucket.scope("tenant_agent_00")
collection = scope.collection("users")
```

[Data operations](../howtos/kv-operations.md), like storing and retrieving documents, can be done using simple methods on the `Collection` class such as `Collection.get()` and `Collection.upsert()`.

To get you started the following code creates a new document in a custom scope and collection and then fetches it again, printing the result.

```ruby
# Upsert Document
upsert_result = collection.upsert(
  "my-document-key",
  {
    "name" => "Ted",
    "age" => 31
  }
)
p cas: upsert_result.cas
#=> {:cas=>223322674373654}

# Get Document
get_result = collection.get("my-document-key")
p cas: get_result.cas,
  name: get_result.content["name"]
#=> {:cas=>223322674373654, :name=>"Ted"}
```

### [](#sql-lookup)SQL++ Lookup

Couchbase SQL++ queries can be performed at the `Cluster` or `Scope` level by invoking `Cluster.query()` or `Scope.query()`.

Cluster level queries require you to specify the fully qualified keyspace each time (e.g. `travel-sample.inventory.airline`). However, with a Scope level query you only need to specify the Collection name — which in this case is `airline`:

```rb
inventory_scope = bucket.scope("inventory")
result = inventory_scope.query('SELECT * FROM airline WHERE id = 10;')
result.rows.each do |row|
  p row
end
```

You can learn more about SQL++ queries on the [Query page](../howtos/n1ql-queries-with-sdk.md).

After completing operations, finish with (otherwise resources will be released by garbage collector):

```ruby
cluster.disconnect
```

## [](#next-steps)Next Steps

Now you're up and running, try one of the following:

* Our [Travel Sample Application](sample-application.md) demonstrates all the basics you need to know;
* Explore [Data Operations](../howtos/kv-operations.md) against a document database;
* Or [Query](../howtos/n1ql-queries-with-sdk.md) with our SQL++ query language;
* Or read up on [which service fits your use case](../concept-docs/data-services.md).

### [](#additional-resources)Additional Resources

The API reference is generated for each release and can be found [here](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/). Older API references are linked from their respective sections in the [Release Notes](../project-docs/sdk-release-notes.md).

Couchbase welcomes community contributions to the Ruby SDK. The Ruby SDK source code is available on [GitHub](https://github.com/couchbase/couchbase-ruby-client).

### [](#troubleshooting)Troubleshooting

* Couchbase Server is designed to work in the same WAN or availability zone as the client application. If you're running the SDK on your laptop against a Capella cluster, see further information on:

  * Notes on [Constrained Network Environments](../ref/client-settings.md#constrained-network-environments).
  * [Network Requirements](../project-docs/compatibility.md#network-requirements).
  * If you have a consumer-grade router which has problems with DNS-SRV records review our [Troubleshooting Guide](../howtos/troubleshooting-cloud-connections.md#troubleshooting-host-not-found).
* Our [community forum](https://forums.couchbase.com/c/ruby-sdk/9) is a great source of help.