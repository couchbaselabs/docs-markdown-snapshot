---
title: Hello World
description: Install, connect, try. A quick start guide to get you up and
  running with Couchbase and the Rust SDK.
editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/hello-world/pages/start-using-sdk.adoc
pubDate: 2026-03-13T03:41:17.220Z
link: xref:rust-sdk:hello-world:start-using-sdk.adoc[]
---

[View original HTML](/rust-sdk/current/hello-world/start-using-sdk.html)

# Hello World

> Install, connect, try. A quick start guide to get you up and running with Couchbase and the Rust SDK. 

Couchbase has a simple interface for creating and modifying records in a document, based upon the **collection** into which the documents are organized. You can read more about data modeling [below](#data-modeling), but first let’s look at those data operations, and installing the Rust SDK.

Upsert with a Unique ID

```rust
let result = collection
    .mutate_in(
        "customer123",
        &[MutateInSpec::upsert("email", "dougr96@hotmail.com", None)?],
        None,
    )
    .await;

match result {
    Ok(res) => {
        println!("Success!");
    }
    Err(e) => {
        println!("error: {e}")
    }
}
```

`upsert` inserts (creates) the document if it does not exist, or replaces it if it does. We’ll explore creating and retrieving data records in more detail [below](#create-read-update-delete)(and touch lightly upon a little of Rust’s functional programming approach as we go), after walking through a quick installation.

## [](#before-you-start)Before You Start

Couchbase Capella, our Database-as-a-Service, lets you get on with what matters, while we take care of the administration for you. Alternately, if you need to control every aspect of deployment — or just want to run the Server in a VM on your laptop — there are several self-managed options available:

* Couchbase Capella
* Self-Managed Couchbase Server

If you haven’t already got a cluster set up, the easiest route is to [sign up to Couchbase Capella and deploy a free tier cluster](https://cloud.couchbase.com/sign-up), then come back to this page. Make a note of the [endpoint](../../../cloud/get-started/connect.md) to connect to, and remember the credentials for the user that you set up.

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

For the example code below to run, you’ll need the username and password of the Administrator user that you create, and the IP address of at least one of the nodes of the cluster.

### [](#prerequisites)Prerequisites

* The Couchbase Rust SDK 1.0 Client is tested against Rust 1.90.

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

More details of the installation process are in the [full installation guide](../project-docs/sdk-full-installation.md). In most cases, given the above prerequisites, it’s a simple matter of the following:

```none
cargo add couchbase
```

### [](#ide-plugins)IDE Plugins

To make development easier, Couchbase plugins are available for VSCode and the IntelliJ family of IDEs and editors. For links and more information on these and other integrations across the Rust ecosystem, check out the [Integrations & Ecosystem](../project-docs/third-party-integrations.md) page.

### [](#grab-the-code)Grab the Code

If you’re all set up and in a real hurry, just grab this code sample and add in your Capella details.

Complete Hello World code sample \[**Click to open or collapse the listing**\] 

use crate::examples_error::ExamplesError;
use crate::timeout::timeout;
use couchbase::authenticator::{Authenticator, PasswordAuthenticator};
use couchbase::cluster::Cluster;
use couchbase::durability_level::DurabilityLevel;
use couchbase::logging_meter::LoggingMeter;
use couchbase::options::cluster_options::ClusterOptions;
use couchbase::options::kv_options::ReplaceOptions;
use couchbase::threshold_logging_tracer::ThresholdLoggingTracer;
use serde_json::json;
use std::time::Duration;
use tracing_subscriber::layer::SubscriberExt;
use tracing_subscriber::EnvFilter;
use tracing_subscriber::Layer;

pub async fn capella_sample() -> Result<(), ExamplesError> {
    // Set up logging
    let filter = EnvFilter::try_from_default_env()
        .unwrap_or_else(|_| EnvFilter::new("info"));

    let subscriber = tracing_subscriber::registry()
        .with(ThresholdLoggingTracer::new(None)) // Enables periodic slow-operation logging
        .with(LoggingMeter::new(None)) // Enables periodic logging of operation duration statistics
        .with(tracing_subscriber::fmt::layer().with_filter(filter));

    tracing::subscriber::set_global_default(subscriber)
        .expect("Failed to set global tracing subscriber");

    // tag::connect[]
    // Update this to your cluster
    let endpoint = "cb.<your-endpoint>.cloud.couchbase.com";
    let username = "<your-username>";
    let password = "<your-password>";
    let bucket_name = "travel-sample";

    let cluster_options = ClusterOptions::new(Authenticator::PasswordAuthenticator(
        PasswordAuthenticator::new(username.to_string(), password.to_string()),
    ));

    let cluster = timeout(
        Duration::from_secs(30),
        Cluster::connect(format!("couchbases://{endpoint}"), cluster_options),
    )
    .await
    .unwrap();
    // end::connect[]

    // tag::bucket[]
    let bucket = cluster.bucket(bucket_name);
    timeout(Duration::from_secs(30), bucket.wait_until_ready(None))
        .await
        .unwrap();
    // end::bucket[]

    // tag::collection[]
    let collection = bucket.scope("inventory").collection("airport");
    // end::collection[]

    // tag::json[]
    let doc = json!({"status": "awesome"});
    // end::json[]

    // tag::upsert[]
    let doc_id = uuid::Uuid::new_v4().to_string();
    timeout(
        Duration::from_millis(2500),
        collection.upsert(&doc_id, doc, None),
    )
    .await
    .unwrap();
    // end::upsert[]

    // tag::get[]
    let result = collection.get(&doc_id, None).await.unwrap();
    let value: serde_json::Value = result.content_as().unwrap();
    let status = value.get("status").unwrap();
    let status = status.as_str().unwrap();

    println!("Couchbase is ${status}");
    // end::get[]

    // tag::get-better-error-handling-propagate[]
    let get_result = collection.get(&doc_id, None).await?;
    let value: serde_json::Value = get_result.content_as()?;

    // value.get returns an Options, so we unwrap it here for simplicity.
    let status = value.get("status").unwrap();
    let status = status.as_str().unwrap();

    println!("Couchbase is ${status}");
    //end::get-better-error-handling-propagate[]

    // tag::get-better-error-handling[]
    match collection
        .get(&doc_id, None)
        .await
        .and_then(|result| result.content_as::<serde_json::Value>())
    {
        Ok(value) => {
            // We could convert the Option from `get` into a Result and include it in the function chain
            // above if we wanted to.
            let status = value.get("status").unwrap();
            let status = status.as_str().unwrap();

            println!("Couchbase is ${status}")
        }
        Err(e) => println!("Error: {e}"),
    };
    //end::get-better-error-handling[]

    // tag::replace-options[]
    timeout(
        Duration::from_millis(2500),
        collection.replace(
            &doc_id,
            value,
            ReplaceOptions::new()
                .expiry(Duration::from_secs(10))
                .durability_level(DurabilityLevel::MAJORITY),
        ),
    )
    .await
    .unwrap();
    // end::replace-options[]

    Ok(())
}

Otherwise, read on as we introduce the CRUD API and connection to Capella or self-managed Couchbase Server.

> [!TIP]
> There’s a **View** link to the complete sample code on GitHub above each of the snippets on these SDK pages, and a **Copy** icon to grab just the snippet shown.

## [](#connect-to-your-database)Connect to your Database

Connect to your Couchbase Capella operational cluster (or your local Couchbase Cluster, if you are trying out self-managed Couchbase).

* Couchbase Capella
* Self-Managed Couchbase Server

```rust
// Update this to your cluster
let endpoint = "cb.<your-endpoint>.cloud.couchbase.com";
let username = "<your-username>";
let password = "<your-password>";
let bucket_name = "travel-sample";

let cluster_options = ClusterOptions::new(Authenticator::PasswordAuthenticator(
    PasswordAuthenticator::new(username.to_string(), password.to_string()),
));

let cluster = timeout(
    Duration::from_secs(30),
    Cluster::connect(format!("couchbases://{endpoint}"), cluster_options),
)
.await
.unwrap();
```

Note, the client certificate for connecting to a Capella cluster is included in the SDK installation.

```rust
// Update this to your cluster
let username = "<your-username>";
let password = "<your-password>";
let bucket_name = "travel-sample";

let cluster = timeout(
    Duration::from_secs(60),
    Cluster::connect(
        // For a secure cluster connection, use `couchbases://<your-cluster-ip>` instead.
        "couchbase://localhost",
        ClusterOptions::new(Authenticator::PasswordAuthenticator(
            PasswordAuthenticator::new(username, password),
        )),
    ),
)
.await
.unwrap();
```

> [!NOTE]
> `Cluster.connect` returns a `Result<Cluster, Error>`. You’ll see examples later of how to better handle a `Result`, but for simplicity here we’ll assume the operation succeeded and get the result as a `Cluster` using `.unwrap`.

For a deeper look at connection options, read [Managing Connections](../howtos/managing-connections.md).

> [!TIP]
> The connection code for getting started uses the Administrator password that you were given during set up. In any production app you should create a role restricted to the permissions needed for your app — more on this in [the Security documentation](../concept-docs/best-practices.md#roles-and-rbac).

### [](#timeouts)Timeouts

Operations in the Rust SDK do not support timeouts in order to feel idiomatic to the Rust ecosystem. In the examples you will see that we use a `timeout` function, which is basic wrapper around `tokio::time::timeout`. To cancel an operation, be it from a timeout or any other reason, you can just drop the future that was returned and the SDK will internally release relevant resources.

### [](#opening-a-bucket)Opening a Bucket

Following successful authentication, open the bucket with:

```rust
let bucket = cluster.bucket(bucket_name);
timeout(Duration::from_secs(30), bucket.wait_until_ready(None))
    .await
    .unwrap();
```

`waitUntilReady` is an optional call, but it is good practice to use it. Opening resources such as buckets is asynchronous — that is, the `cluster.bucket` call returns immediately and proceeds in the background. `waitUntilReady` ensures that the bucket resource is fully loaded before proceeding. If not present, then the first key-value (KV) operation on the bucket will wait for it to be ready. As with the earlier `Cluster.connect`, we use `.unwrap` on the result here for simplicity.

**Collections** allow documents to be grouped by purpose or theme, according to a specified **scope** — see data modeling, [below](#data-modeling). Here we will use the `airport` collection within the `inventory` scope from `travel-sample` bucket as an example.

```rust
let collection = bucket.scope("inventory").collection("airport");
```

## [](#create-read-update-delete)Create, Read, Update, Delete

Couchbase documents are organized into buckets, scopes, and collections. [CRUD operations](https://en.wikipedia.org/wiki/CRUD) — Create, Read, Update, Delete — can be performed upon documents in a collection.

### [](#json)JSON

We’ll create a snippet of JSON to work with, using the `serde_json` JSON library, but you can use any library that can serialize to `serde::Serialize`. You can also use any value that is already serialized into a `Vec<u8>` using the `<operation_namne>_raw` set of functions.

```rust
let doc = json!({"status": "awesome"});
```

### [](#insert-create-and-upsert)Insert (Create) and Upsert

`insert` and `upsert` will both create a new document. The difference between the two is that if a document with that key already exists, the `insert` operation will fail, while the `upsert` operation will succeed, replacing the content.

We need to provide a unique ID as the key, and we’ll use a UUID here:

Creating a new document

```rust
let doc_id = uuid::Uuid::new_v4().to_string();
timeout(
    Duration::from_millis(2500),
    collection.upsert(&doc_id, doc, None),
)
.await
.unwrap();
```

### [](#get-read)Get (Read)

The `get` method reads a document from a collection.

Now let’s get the data back (this example does not follow best practices due to the use of `.unwrap`):

```rust
let result = collection.get(&doc_id, None).await.unwrap();
let value: serde_json::Value = result.content_as().unwrap();
let status = value.get("status").unwrap();
let status = status.as_str().unwrap();

println!("Couchbase is ${status}");
```

Here we’re fetching the value for the key `docId`, converting that value to a `serde_json::Value` (a generic JSON object), , and then accessing the value of the **status** key as a String.

#### [](#better-error-handling)Better Error Handling

There’s quite a lot of error handling code here to do something quite simple - both `get` and `content_as` can return an error. One way to handle this better is to use the `?` operator to propagate errors up to the caller, like this:

```rust
let get_result = collection.get(&doc_id, None).await?;
let value: serde_json::Value = get_result.content_as()?;

// value.get returns an Options, so we unwrap it here for simplicity.
let status = value.get("status").unwrap();
let status = status.as_str().unwrap();

println!("Couchbase is ${status}");
```

Another way to improve on this is by using `and_then`, like this:

```rust
match collection
    .get(&doc_id, None)
    .await
    .and_then(|result| result.content_as::<serde_json::Value>())
{
    Ok(value) => {
        // We could convert the Option from `get` into a Result and include it in the function chain
        // above if we wanted to.
        let status = value.get("status").unwrap();
        let status = status.as_str().unwrap();

        println!("Couchbase is ${status}")
    }
    Err(e) => println!("Error: {e}"),
};
```

### [](#replace-update-and-overloads)Replace (Update) and Overloads

You’ll notice that most operations in the Rust SDK have an `Options` parameter. For instance:

The replace method updates the value of an existing document

```rust
timeout(
    Duration::from_millis(2500),
    collection.replace(
        &doc_id,
        value,
        ReplaceOptions::new()
            .expiry(Duration::from_secs(10))
            .durability_level(DurabilityLevel::MAJORITY),
    ),
)
.await
.unwrap();
```

> [!CAUTION]
> When you replace a document, it’s usually good practice to use [optimistic locking](../howtos/kv-operations.md#optimistic-locking). Otherwise, changes might get lost if two people change the same document at the same time.

### [](#remove-delete)Remove (Delete)

The remove method deletes a document from a collection:

```rust
match collection.remove("document-key", None).await {
    Ok(_result) => {
        println!("Document remove successful");
    }
    Err(e) => {
        println!("Error: {e}");
    }
}
```

## [](#data-modeling)Data Modeling

Documents are organized into collections — collections of documents that belong together. You get to decide what it means to "belong." Developers usually put documents of the same type in the same collection.

For example, imagine you have two types of documents: customers and invoices. You could put the customer documents in a collection called `customers`, and the invoice documents in a collection called `invoices`.

Each document belongs to exactly one collection. A document’s ID is unique _within_ the collection.

Different scopes can hold collections with different names. There is no relationship between collections in different scopes. Each collection belongs to just one scope and a collection’s name is unique within the scope.

More details can be found on the [Data Model page](../concept-docs/data-model.md).

## [](#what-next)What Next?

### [](#help-and-troubleshooting)Help and Troubleshooting

* [Troubleshooting common network problems](../howtos/troubleshooting-cloud-connections.md).
* [Help forum](https://www.couchbase.com/forums/c/other-product/13).
* [Discord channel](https://discord.com/channels/915294689681362954/1217642561645318194).
* Read the [error handling page](../howtos/error-handling.md).
* [Get help from Couchbase iQ](../../../cloud/get-started/capella-iq/get-started-with-iq.md#generate-sdk-code-preview).

### [](#next-steps)Next Steps

* [Discover SQL++](../concept-docs/querying-your-data.md) — our SQL-family querying language.
* Explore some of the [third party integrations](../project-docs/third-party-integrations.md) with Couchbase and the Rust SDK, across the Rust ecosystem.