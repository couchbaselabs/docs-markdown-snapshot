---
title: Hello World
description: Install, connect, try. A quick start guide to get you up and
  running with Couchbase and the Python SDK.
editUrl: https://github.com/couchbase/docs-sdk-python/edit/release/4.6/modules/hello-world/pages/start-using-sdk.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:python-sdk:hello-world:start-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/current/hello-world/start-using-sdk.html)

# Hello World

> Install, connect, try. A quick start guide to get you up and running with Couchbase and the Python SDK. 

Couchbase has a simple interface for creating and modifying records in a document, based upon the **collection** into which the documents are organized. You can read more about data modeling [below](#data-modeling), but first let's look at those data operations, and installing the Python SDK.

Upsert with Replication set to [Majority Durability](../concept-docs/data-durability-acid-transactions.md#durable-writes):

```python
# Upsert with Durability level Majority
document = dict(foo="bar", bar="foo")
opts = UpsertOptions(durability=ServerDurability(Durability.MAJORITY))
result = collection.upsert("document-key", document, opts)
```

`upsert` inserts (creates) the document if it does not exist, or replaces it if it does. We'll explore creating and retrieving data records in more detail [below](#create-read-update-delete), after walking through a quick installation.

> [!TIP]
> This page walks you through a quick installation, and CRUD examples against the Data Service. Elsewhere in this section you can find a fully worked-through [Sample Application](sample-application.md).

## [](#before-you-start)Before You Start

Couchbase Capella, our Database-as-a-Service, lets you get on with what matters, while we take care of the administration for you. Alternately, if you need to control every aspect of deployment — or just want to run the Server in a VM on your laptop — there are several self-managed options available:

* Couchbase Capella
* Self-Managed Couchbase Server

If you haven't already got a cluster set up, the easiest route is to [sign up to Couchbase Capella and deploy a free tier cluster](https://cloud.couchbase.com/sign-up), then come back to this page. Make a note of the [endpoint](../../../cloud/get-started/connect.md) to connect to, and remember the credentials for the user that you set up.

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

The Couchbase Python SDK aims to support [Python versions](https://devguide.python.org/versions/#supported-versions) in security or bug-fix (a.k.a. maintenance) status.

Details of all build dependencies are in the [full installation guide](../project-docs/sdk-full-installation.md).

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

Given the above prerequisites, use `pip` to install the SDK:

```console
$ sudo -H python3 -m pip install couchbase
```

Details of all build dependencies and platform variations are in the [full installation guide](../project-docs/sdk-full-installation.md). The [compatibility guide](../project-docs/compatibility.md) lists compatible OSs and Python versions.

### [](#ide-plugins)IDE Plugins

To make development easier, Couchbase plugins are available for VSCode and the IntelliJ family of IDEs and editors. For links and more information on these and other integrations across the Python ecosystem, check out the [Integrations & Ecosystem](../project-docs/third-party-integrations.md) page.

### [](#grab-the-code)Grab the Code

If you're all set up and in a real hurry, just grab this code sample and add in your Capella details.

Complete Hello World code sample \[**Click to open or collapse the listing**\] 

```python
# tag::imports[]
from datetime import timedelta

# needed for any cluster connection
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
# needed for options -- cluster, timeout, SQL++ (N1QL) query, etc.
from couchbase.options import (ClusterOptions, ClusterTimeoutOptions,
                               QueryOptions)

# end::imports[]

# tag::connect[]
# Update this to your cluster
endpoint = "--your-instance--.dp.cloud.couchbase.com"
username = "username"
password = "Password!123"
bucket_name = "travel-sample"
# User Input ends here.

# Connect options - authentication
auth = PasswordAuthenticator(username, password)

# get a reference to our cluster
options = ClusterOptions(auth)
# Sets a pre-configured profile called "wan_development" to help avoid latency issues
# when accessing Capella from a different Wide Area Network
# or Availability Zone(e.g. your laptop).
options.apply_profile('wan_development')
cluster = Cluster.connect(f'couchbases://{endpoint}', options)

# Wait until the cluster is ready for use.
cluster.wait_until_ready(timedelta(seconds=35))
# end::connect[]

# tag::bucket[]
# get a reference to our bucket
cb = cluster.bucket(bucket_name)
# end::bucket[]

# tag::collection[]
cb_coll = cb.scope("inventory").collection("airline")
# end::collection[]

# tag::upsert-func[]


def upsert_document(doc):
    print("\nUpsert CAS: ")
    try:
        # key will equal: "airline_8091"
        key = doc["type"] + "_" + str(doc["id"])
        result = cb_coll.upsert(key, doc)
        print(result.cas)
    except Exception as e:
        print(e)
# end::upsert-func[]

# tag::get-func[]
# get document function


def get_airline_by_key(key):
    print("\nGet Result: ")
    try:
        result = cb_coll.get(key)
        print(result.content_as[str])
    except Exception as e:
        print(e)
# end::get-func[]

# tag::lookup-func[]
# query for new document by callsign


def lookup_by_callsign(cs):
    print("\nLookup Result: ")
    try:
        inventory_scope = cb.scope('inventory')
        sql_query = 'SELECT VALUE name FROM airline WHERE callsign = $1'
        row_iter = inventory_scope.query(
            sql_query,
            QueryOptions(positional_parameters=[cs]))
        for row in row_iter:
            print(row)
    except Exception as e:
        print(e)
# end::lookup-func[]


# tag::test-doc[]
airline = {
    "type": "airline",
    "id": 8091,
    "callsign": "CBS",
    "iata": None,
    "icao": None,
    "name": "Couchbase Airways",
}
# end::test-doc[]

# tag::upsert-invoke[]
upsert_document(airline)
# end::upsert-invoke[]

# tag::get-invoke[]
get_airline_by_key("airline_8091")
# end::get-invoke[]

# tag::lookup-invoke[]
lookup_by_callsign("CBS")
# end::lookup-invoke[]
```

Otherwise, read on as we introduce the CRUD API and connection to Capella or self-managed Couchbase Server.

> [!TIP]
> There's a **View** link to the complete sample code on GitHub above each of the snippets on these SDK pages, and a **Copy** icon to grab just the snippet shown.

## [](#connect-to-your-database)Connect to your Database

Connect to your Couchbase Capella operational cluster (or your local Couchbase Cluster, if you are trying out self-managed Couchbase).

* Couchbase Capella
* Self-Managed Couchbase Server

```python
# Update this to your cluster
endpoint = "--your-instance--.dp.cloud.couchbase.com"
username = "username"
password = "Password!123"
bucket_name = "travel-sample"
# User Input ends here.

# Connect options - authentication
auth = PasswordAuthenticator(username, password)

# get a reference to our cluster
options = ClusterOptions(auth)
# Sets a pre-configured profile called "wan_development" to help avoid latency issues
# when accessing Capella from a different Wide Area Network
# or Availability Zone(e.g. your laptop).
options.apply_profile('wan_development')
cluster = Cluster.connect(f'couchbases://{endpoint}', options)

# Wait until the cluster is ready for use.
cluster.wait_until_ready(timedelta(seconds=35))
```

Note, the client certificate for connecting to a Capella cluster is included in the SDK installation.

```python
# Update this to your cluster
username = "Administrator"
password = "password"
bucket_name = "travel-sample"
# User Input ends here.

# Connect options - authentication
auth = PasswordAuthenticator(
    username,
    password,
)

# Get a reference to our cluster
# NOTE: For non-TLS/SSL connection use 'couchbase://<your-ip-address>' instead
cluster = Cluster.connect('couchbases://your-ip', ClusterOptions(auth))

# Wait until the cluster is ready for use.
cluster.wait_until_ready(timedelta(seconds=5))
```

`wait_until_ready` is an optional call, but it is good practice to use it. Making connections, and opening resources such as buckets, is asynchronous — that is, the `cluster.bucket` call (below) returns immediately and proceeds in the background. `waitUntilReady` ensures that the bucket resource is fully loaded before proceeding.

For a deeper look at connection options, read [Managing Connections](../howtos/managing-connections.md).

> [!IMPORTANT]
> The connection code for getting started uses the Administrator password that you were given during set up. In any production app you should create a role restricted to the permissions needed for your app — more on this in [the Security documentation](../concept-docs/best-practices.md#roles-and-rbac).

### [](#opening-a-bucket)Opening a Bucket

Following successful authentication, open the bucket with:

```python
# get a reference to our bucket
cb = cluster.bucket(bucket_name)
```

**Collections** allow documents to be grouped by purpose or theme, according to a specified **scope** — see data modeling, [below](#data-modeling). Here we will use the `airport` collection within the `inventory` scope from `travel-sample` bucket as an example.

```python
cb_coll = cb.scope("inventory").collection("airline")
```

## [](#create-read-update-delete)Create, Read, Update, Delete

Couchbase documents are organized into buckets, scopes, and collections. [CRUD operations](https://en.wikipedia.org/wiki/CRUD) — Create, Read, Update, Delete — can be performed upon documents in a collection.

### [](#insert-create-and-upsert)Insert (Create) and Upsert

`insert` and `upsert` will both create a new document. The difference between the two is that if a document with that key already exists, the `insert` operation will fail, while the `upsert` operation will succeed, replacing the content.

Here is a function to wrap upsert:

```python


def upsert_document(doc):
    print("\nUpsert CAS: ")
    try:
        # key will equal: "airline_8091"
        key = doc["type"] + "_" + str(doc["id"])
        result = cb_coll.upsert(key, doc)
        print(result.cas)
    except Exception as e:
        print(e)
```

We'll create a new document…​

Creating a new document

```python
airline = {
    "type": "airline",
    "id": 8091,
    "callsign": "CBS",
    "iata": None,
    "icao": None,
    "name": "Couchbase Airways",
}
```

… And call our wrapper function

Upserting the document

```python
upsert_document(airline)
```

### [](#get-read)Get (Read)

The `get` method reads a document from a collection.

```python
# get document function


def get_airline_by_key(key):
    print("\nGet Result: ")
    try:
        result = cb_coll.get(key)
        print(result.content_as[str])
    except Exception as e:
        print(e)
```

### [](#replace-update-and-overloads)Replace (Update) and Overloads

The replace method updates the value of an existing document

```python
# Replace document with CAS
result = collection.get("document-key")
doc = result.content_as[dict]
doc["bar"] = "baz"
opts = ReplaceOptions(cas=result.cas)
result = collection.replace("document-key", doc, opts)
```

When you replace a document, it's usually good practice to use [optimistic locking](../howtos/kv-operations.md#optimistic-locking), as in the above example, using CAS. Otherwise, changes might get lost if two people change the same document at the same time.

### [](#remove-delete)Remove (Delete)

The remove method deletes a document from a collection:

```python
# remove document with options
result = collection.remove(
    "document-key",
    RemoveOptions(
        cas=12345,
        durability=ServerDurability(
            Durability.MAJORITY)))
```

Like `replace`, `remove` also optionally takes the CAS value if you want to make sure you are only removing the document if it hasn't changed since you last fetched it.

## [](#data-modeling)Data Modeling

Documents are organized into collections — collections of documents that belong together. You get to decide what it means to "belong." Developers usually put documents of the same type in the same collection.

For example, imagine you have two types of documents: customers and invoices. You could put the customer documents in a collection called `customers`, and the invoice documents in a collection called `invoices`.

Each document belongs to exactly one collection. A document's ID is unique _within_ the collection.

Different scopes can hold collections with different names. There is no relationship between collections in different scopes. Each collection belongs to just one scope and a collection's name is unique within the scope.

More details can be found on the [Data Model page](../concept-docs/data-model.md).

## [](#what-next)What Next?

### [](#help-and-troubleshooting)Help and Troubleshooting

* [Troubleshooting common network problems](../howtos/troubleshooting-cloud-connections.md).
* [Help forum](https://www.couchbase.com/forums/c/python-sdk/10).
* [Discord channel](https://discord.com/channels/915294689681362954/1217642561645318194).
* Read the [error handling page](../howtos/error-handling.md).
* [Get help from Couchbase iQ](../../../cloud/get-started/capella-iq/get-started-with-iq.md#generate-sdk-code-preview).

### [](#next-steps)Next Steps

* [Learn more about the Data Service](../concept-docs/data-durability-acid-transactions.md).
* [Discover SQL++](../concept-docs/querying-your-data.md) — our SQL-family querying language.
* Explore some of the [third party integrations](../project-docs/third-party-integrations.md) with Couchbase and the Python SDK, across the Python ecosystem.