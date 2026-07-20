---
title: Hello World
description: Install, connect, try. A quick start guide to get you up and
  running with Couchbase and the Java SDK.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.11/modules/hello-world/pages/start-using-sdk.adoc
pubDate: 2026-07-20T13:54:32.914Z
link: xref:java-sdk:hello-world:start-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/current/hello-world/start-using-sdk.html)

# Hello World

> Install, connect, try. A quick start guide to get you up and running with Couchbase and the Java SDK. 

Couchbase has a simple interface for creating and modifying records in a document, based upon the **collection** into which the documents are organized. You can read more about data modeling [below](#data-modeling), but first let's look at those data operations, and installing the Java SDK.

Upsert with Replication set to [Majority Durablity](../concept-docs/data-durability-acid-transactions.md#durable-writes):

```java
collection.upsert("my-document", JsonObject.create().put("doc", true),
    upsertOptions().durability(DurabilityLevel.MAJORITY));
```

`upsert` inserts (creates) the document if it does not exist, or replaces it if it does. We'll explore creating and retrieving data records in more detail [below](#create-read-update-delete)(and touch lightly upon a little of Java's functional programming approach as we go), after walking through a quick installation.

> [!TIP]
> This page walks you through a quick installation, and CRUD examples against the Data Service. Elsewhere in this section you can find a fully worked-through [Quickstart in Couchbase with Spring Boot and Java](sample-application.md) and, for those new to document (NoSQL) databases, our [Student Record Tutorial](student-record-developer-tutorial.md).

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

* The Java SDK is tested against LTS versions of Oracle JDK and OpenJDK — see the [compatibility docs](../project-docs/compatibility.md#jdk-compat).  
[OpenJDK 25 with HotSpot JVM](https://adoptium.net/) is recommended.

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

We recommend running the latest Java LTS version (i.e. at the time of writing JDK 25) with the highest patch version available. Couchbase publishes all stable artifacts to [Maven Central](https://central.sonatype.com/namespace/com.couchbase.client).

The latest version of 3.11.x is [3.11.3](https://central.sonatype.com/artifact/com.couchbase.client/java-client/3.11.3/jar).

More details of the installation process are in the [full installation guide](../project-docs/sdk-full-installation.md). In most cases, given the above prerequisites, use your favorite dependency management tool to install the SDK.

* Maven
* Gradle

```xml
<dependencies>
    <dependency>
        <groupId>com.couchbase.client</groupId>
        <artifactId>java-client</artifactId>
        <version>3.11.3</version>
    </dependency>
</dependencies>
```

```groovy
implementation 'com.couchbase.client:java-client:3.11.3'
```

### [](#ide-plugins)IDE Plugins

To make development easier, Couchbase plugins are available for VSCode and the IntelliJ family of IDEs and editors. For links and more information on these and other integrations across the Java ecosystem, check out the [3rd Party Integrations](../project-docs/third-party-integrations.md) page.

### [](#grab-the-code)Grab the Code

If you're all set up and in a real hurry, just grab this code sample and add in your Capella details.

Complete Hello World code sample \[**Click to open or collapse the listing**\] 

/*
 * Copyright (c) 2025 Couchbase, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// tag::imports[]
import com.couchbase.client.core.env.WanDevelopmentProfile;
import com.couchbase.client.core.error.CouchbaseException;
import com.couchbase.client.java.Bucket;
import com.couchbase.client.java.Cluster;
import com.couchbase.client.java.ClusterOptions;
import com.couchbase.client.java.Collection;
import com.couchbase.client.java.env.ClusterEnvironment;
import com.couchbase.client.java.json.JsonObject;
import com.couchbase.client.java.kv.GetResult;
import com.couchbase.client.java.kv.ReplaceOptions;

import java.time.Duration;
import java.util.UUID;

import static com.couchbase.client.core.msg.kv.DurabilityLevel.MAJORITY;
// end::imports[]

public class StartUsingCapella {
    public static void main(String[] args) {
        // tag::connect[]
        // Update this to your cluster
        String endpoint = "cb.<your-endpoint>.cloud.couchbase.com";
        String username = "username";
        String password = "Password!123";
        String bucketName = "travel-sample";

        ClusterEnvironment env = ClusterEnvironment.builder()
            .securityConfig(sc -> sc.enableTls(true))
            // Sets a pre-configured profile called "wan-development" to help avoid latency issues
            // when accessing Capella from a different Wide Area Network
            // or Availability Zone (e.g. your laptop).
            .applyProfile(new WanDevelopmentProfile().name())
            .build();

        Cluster cluster = Cluster.connect(
            "couchbases://" + endpoint,
            ClusterOptions.clusterOptions(username, password).environment(env)
        );
        // end::connect[]

        // tag::bucket[]
        Bucket bucket = cluster.bucket(bucketName);
        bucket.waitUntilReady(Duration.ofSeconds(30));
        // end::bucket[]

        // tag::collection[]
        Collection collection = bucket.scope("inventory").collection("airport");
        // end::collection[]

        // tag::json[]
        JsonObject json = JsonObject.create().put("status", "awesome");
        // end::json[]

        // tag::upsert[]
        String docId = UUID.randomUUID().toString();
        try {
            collection.upsert(docId, json);
        } catch (CouchbaseException e) {
            System.err.println("Error: " + e.getMessage());
        }
        // end::upsert[]

        // tag::get[]
        // Get a document
        try {
            GetResult result = collection.get(docId);
            JsonObject content = result.contentAsObject();
            String status = content.getString("status");
            System.out.println("Couchbase is " + status);
        } catch (Exception e) {
            System.err.println("Error getting document: " + e.getMessage());
        }
        // end::get[]

        // tag::get-for[]
        try {
            String status = collection.get(docId)
                .contentAsObject()
                .getString("status");
            System.out.println("Couchbase is " + status);
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
        // end::get-for[]

        // tag::replace-options[]
        try {
            collection.replace(
                docId,
                json,
                ReplaceOptions.replaceOptions()
                    .expiry(Duration.ofSeconds(10))
                    .durability(MAJORITY)
            );
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
        // end::replace-options[]

        // tag::replace-named[]
        try {
            collection.replace(
                docId,
                json,
                ReplaceOptions.replaceOptions()
                    .durability(MAJORITY)
            );
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
        // end::replace-named[]
    }
}

Otherwise, read on as we introduce the CRUD API and connection to Capella or self-managed Couchbase Server.

> [!TIP]
> There's a **View** link to the complete sample code on GitHub above each of the snippets on these SDK pages, and a **Copy** icon to grab just the snippet shown.

## [](#connect-to-your-database)Connect to your Database

Connect to your Couchbase Capella operational cluster (or your local Couchbase Cluster, if you are trying out self-managed Couchbase).

* Couchbase Capella
* Self-Managed Couchbase Server
* Cloud Native Gateway (CNG)
* Quarkus

```java
// Update this to your cluster
String endpoint = "cb.<your-endpoint>.cloud.couchbase.com";
String username = "username";
String password = "Password!123";
String bucketName = "travel-sample";

ClusterEnvironment env = ClusterEnvironment.builder()
    .securityConfig(sc -> sc.enableTls(true))
    // Sets a pre-configured profile called "wan-development" to help avoid latency issues
    // when accessing Capella from a different Wide Area Network
    // or Availability Zone (e.g. your laptop).
    .applyProfile(new WanDevelopmentProfile().name())
    .build();

Cluster cluster = Cluster.connect(
    "couchbases://" + endpoint,
    ClusterOptions.clusterOptions(username, password).environment(env)
);
```

```java
// Update these variables to point to your Couchbase Server instance and credentials.
static String connectionString = "couchbase://127.0.0.1";
static String username = "Administrator";
static String password = "password";
static String bucketName = "travel-sample";
```

```java
// Use the following code to connect to your cluster.
Cluster cluster = Cluster.connect(
    connectionString,
    ClusterOptions.clusterOptions(username, password).environment(env -> {
      // Customize client settings by calling methods on the "env" variable.
    })
);
```

Couchbase's large number of ports across the URLs of many services can be proxied by using a `couchbase2://` endpoint as the connection string — currently only compatible with recent versions of [Couchbase Autonomous Operator](#operator:ROOT:concept-cloud-native-gateway.adoc):

```scala
Cluster cluster = Cluster.connect(
  "couchbase2://10.12.14.16",
  ClusterOptions
    .create(username, password)
    .environment(env)
)
```

Read more on the [Connections](../howtos/managing-connections.md#cloud-native-gateway) page.

Our [Couchbase Quarkus Java Extension docs](../../../quarkus-extension/current/overview.md) cover installing and connecting with the Quarkus extension in detail, but if you already have Quarkus installed and a project ready (with `quarkus-couchbase` in your `pom.xml` or `build.gradle`), then your `src/main/resources/application.properties` file needs to contain:

```properties
quarkus.couchbase.connection-string=localhost
quarkus.couchbase.username=username
quarkus.couchbase.password=password
```

For a deeper look at connection options, read [Managing Connections](../howtos/managing-connections.md).

> [!TIP]
> The connection code for getting started uses the Administrator password that you were given during set up. In any production app you should create a role restricted to the permissions needed for your app — more on this in [the Security documentation](../concept-docs/best-practices.md#roles-and-rbac).

The `ClusterEnvironment.Builder` is covered more fully on the [Client Settings](../ref/client-settings.md#the-environment-builder) page.

> [!TIP]
> Simpler Connection
> 
> There's also a simpler version of `Cluster.connect()` for when you don't need to customize the cluster environment:
> 
> ```java
> // Alternatively, connect without customizing the cluster envionrment.
> Cluster cluster = Cluster.connect(connectionString, username, password);
> ```

### [](#opening-a-bucket)Opening a Bucket

Following successful authentication, open the bucket with:

```java
Bucket bucket = cluster.bucket(bucketName);
bucket.waitUntilReady(Duration.ofSeconds(30));
```

`waitUntilReady` is an optional call, but it is good practice to use it. Opening resources such as buckets is asynchronous — that is, the `cluster.bucket` call returns immediately and proceeds in the background. `waitUntilReady` ensures that the bucket resource is fully loaded before proceeding. If not present, then the first key-value (KV) operation on the bucket will wait for it to be ready. As with the earlier `Cluster.connect`, we use `.get` on the result here for simplicity.

**Collections** allow documents to be grouped by purpose or theme, according to a specified **scope** — see data modeling, [below](#data-modeling). Here we will use the `airport` collection within the `inventory` scope from `travel-sample` bucket as an example.

```java
Collection collection = bucket.scope("inventory").collection("airport");
```

## [](#create-read-update-delete)Create, Read, Update, Delete

Couchbase documents are organized into buckets, scopes, and collections. [CRUD operations](https://en.wikipedia.org/wiki/CRUD) — Create, Read, Update, Delete — can be performed upon documents in a collection.

### [](#json)JSON

We'll create a snippet of JSON to work with, using the client's own JSON library, but you can read about the Scala SDK's support for other JSON libraries on the [JSON Modelling](../howtos/json.md) page.

```java
JsonObject json = JsonObject.create().put("status", "awesome");
```

### [](#insert-create-and-upsert)Insert (Create) and Upsert

`insert` and `upsert` will both create a new document. The difference between the two is that if a document with that key already exists, the `insert` operation will fail, while the `upsert` operation will succeed, replacing the content.

We need to provide a unique ID as the key, and we'll use a UUID here:

Creating a new document

```java
String docId = UUID.randomUUID().toString();
try {
    collection.upsert(docId, json);
} catch (CouchbaseException e) {
    System.err.println("Error: " + e.getMessage());
}
```

### [](#get-read)Get (Read)

The `get` method reads a document from a collection.

Wrapping the method in a `Try` / `Catch` is a good way to handle exceptions:

```java
// Get a document
try {
    GetResult result = collection.get(docId);
    JsonObject content = result.contentAsObject();
    String status = content.getString("status");
    System.out.println("Couchbase is " + status);
} catch (Exception e) {
    System.err.println("Error getting document: " + e.getMessage());
}
```

### [](#replace-update-and-overloads)Replace (Update) and Overloads

The replace method updates the value of an existing document

```java
try {
    collection.replace(
        docId,
        json,
        ReplaceOptions.replaceOptions()
            .expiry(Duration.ofSeconds(10))
            .durability(MAJORITY)
    );
} catch (Exception e) {
    System.err.println("Error: " + e.getMessage());
}
```

> [!CAUTION]
> When you replace a document, it's usually good practice to use [optimistic locking](../howtos/kv-operations.md#optimistic-locking). Otherwise, changes might get lost if two people change the same document at the same time.

### [](#remove-delete)Remove (Delete)

The remove method deletes a document from a collection:

```java
try {
  collection.remove("my-document");
} catch (DocumentNotFoundException ex) {
  System.out.println("Document did not exist when trying to remove");
}
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
* [Help forum](https://www.couchbase.com/forums/c/java-sdk/5).
* [Discord channel](https://discord.com/channels/915294689681362954/1217642561645318194).
* Read the [error handling page](../howtos/error-handling.md).
* [Get help from Couchbase iQ](../../../cloud/get-started/capella-iq/get-started-with-iq.md#generate-sdk-code-preview).

### [](#next-steps)Next Steps

* [Learn more about the Data Service](../concept-docs/data-durability-acid-transactions.md).
* [Discover SQL++](../concept-docs/querying-your-data.md) — our SQL-family querying language.
* Explore some of the [third party integrations](../project-docs/third-party-integrations.md) with Couchbase and the Java SDK, across the Java ecosystem.