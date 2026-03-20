---
title: Hello World
description: Install, connect, try. A quick start guide to get you up and
  running with Couchbase and the Scala SDK.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.10/modules/hello-world/pages/start-using-sdk.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.10@scala-sdk:hello-world:start-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/3.10/hello-world/start-using-sdk.html)

# Hello World

> Install, connect, try. A quick start guide to get you up and running with Couchbase and the Scala SDK. 

> [!NOTE]
> From 3.9.0 on, all Couchbase JVM SDKs have an aligned version number to make it easier to users to track changes. So the version has jumped from 1.8.x to 3.9.x.

Couchbase has a simple interface for creating and modifying records in a document, based upon the **collection** into which the documents are organized. You can read more about data modeling [below](#data-modeling), but first let’s look at those data operations, and installing the Scala SDK.

Upsert with a Unique ID

```scala
val docId = UUID.randomUUID().toString
collection.upsert(docId, json) match {
  case Success(result)    =>
  case Failure(exception) => println("Error: " + exception)
}
```

`upsert` inserts (creates) the document if it does not exist, or replaces it if it does. We’ll explore creating and retrieving data records in more detail [below](#create-read-update-delete)(and touch lightly upon a little of Scala’s functional programming approach as we go), after walking through a quick installation.

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

* The Scala SDK is tested against LTS versions of Oracle JDK and OpenJDK — see the [compatibility docs](../project-docs/compatibility.md#jdk-compat).
* The Couchbase Scala SDK 3.10 Client supports Scala 2.12, 2.13, and 3.3 through 3.7 (inclusive).

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

More details of the installation process are in the [full installation guide](../project-docs/sdk-full-installation.md). In most cases, given the above prerequisites, it’s a simple matter of the following for your favorite build tool:

* Scala Build Tool (SBT)
* Gradle
* Maven

```sbt
libraryDependencies += "com.couchbase.client" %% "scala-client" % "3.10.1"
```

This will automatically use the correct build for your Scala version.

For Scala 2.13 or Scala 3.3 through 3.7, include the following in your `build.gradle`:

```groovy
dependencies {
    compile group: 'com.couchbase.client', name: 'scala-client_3', version: '3.10.1'
}
```

For Scala 2.12, refer to the full [Installation page](../project-docs/sdk-full-installation.md).

For Scala 2.13 or Scala 3.3 through 3.7, include the following in your Maven `pom.xml`:

```xml
<dependencies>
    <dependency>
        <groupId>com.couchbase.client</groupId>
        <artifactId>scala-client_3</artifactId>
        <version>3.10.1</version>
    </dependency>
</dependencies>
```

For Scala 2.12, refer to the full [Installation page](../project-docs/sdk-full-installation.md).

### [](#ide-plugins)IDE Plugins

To make development easier, Couchbase plugins are available for VSCode and the IntelliJ family of IDEs and editors. For links and more information on these and other integrations across the Scala ecosystem, check out the [Integrations & Ecosystem](../project-docs/third-party-integrations.md) page.

### [](#grab-the-code)Grab the Code

If you’re all set up and in a real hurry, just grab this code sample and add in your Capella details.

Complete Hello World code sample \[**Click to open or collapse the listing**\] 

/*
 * Copyright (c) 2024 Couchbase, Inc.
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
import com.couchbase.client.scala.durability.Durability
import com.couchbase.client.scala.env.{
  ClusterEnvironment,
  SecurityConfig,
  TimeoutConfig
}
import com.couchbase.client.scala.json.{JsonObject, JsonObjectSafe}
import com.couchbase.client.scala.kv.ReplaceOptions
import com.couchbase.client.scala.{Cluster, ClusterOptions}
import io.netty.handler.ssl.util.InsecureTrustManagerFactory

import java.nio.file.Path
import java.util.UUID
import scala.concurrent.duration._
import scala.util.{Failure, Success, Try}
// end::imports[]

object Cloud {
  def main(args: Array[String]): Unit = {
    // tag::connect[]
    // Update this to your cluster
    val endpoint = "cb.<your-endpoint>.cloud.couchbase.com"
    val username = "username"
    val password = "Password!123"
    val bucketName = "travel-sample"

    val env = ClusterEnvironment.builder
      .securityConfig(
        SecurityConfig()
          .enableTls(true)
      )
      // Sets a pre-configured profile called "wan-development" to help avoid latency issues
      // when accessing Capella from a different Wide Area Network
      // or Availability Zone (e.g. your laptop).
      .applyProfile(ClusterEnvironment.WanDevelopmentProfile)
      .build
      .get

    val cluster = Cluster
      .connect(
        "couchbases://" + endpoint,
        ClusterOptions
          .create(username, password)
          .environment(env)
      )
      .get
    // end::connect[]

    // tag::bucket[]
    val bucket = cluster.bucket(bucketName)
    bucket.waitUntilReady(30.seconds).get
    // end::bucket[]

    // tag::collection[]
    val collection = bucket.scope("inventory").collection("airport")
    // end::collection[]

    // tag::json[]
    val json = JsonObject("status" -> "awesome")
    // end::json[]

    // tag::upsert[]
    val docId = UUID.randomUUID().toString
    collection.upsert(docId, json) match {
      case Success(result)    =>
      case Failure(exception) => println("Error: " + exception)
    }
    // end::upsert[]

    // tag::get[]
    // Get a document
    collection.get(docId) match {
      case Success(result) =>
        // Convert the content to a JsonObjectSafe
        result.contentAs[JsonObjectSafe] match {
          case Success(json) =>
            // Pull out the JSON's status field, if it exists
            json.str("status") match {
              case Success(hello) => println(s"Couchbase is $hello")
              case _              => println("Field 'status' did not exist")
            }
          case Failure(err) => println("Error decoding result: " + err)
        }
      case Failure(err) => println("Error getting document: " + err)
    }
    // end::get[]

    def getFor() {
      // tag::get-for[]
      val result: Try[String] = for {
        result <- collection.get(docId)
        json <- result.contentAs[JsonObjectSafe]
        status <- json.str("status")
      } yield status

      result match {
        case Success(status) => println(s"Couchbase is $status")
        case Failure(err)    => println("Error: " + err)
      }
      // end::get-for[]
    }

    def getMap() {
      // tag::get-map[]
      val result: Try[String] = collection
        .get(docId)
        .flatMap(_.contentAs[JsonObjectSafe])
        .flatMap(_.str("status"))

      result match {
        case Success(status) => println(s"Couchbase is $status")
        case Failure(err)    => println("Error: " + err)
      }
      // end::get-map[]
    }

    def replaceOptions() {
      // tag::replace-options[]
      collection.replace(
        docId,
        json,
        ReplaceOptions()
          .expiry(10.seconds)
          .durability(Durability.Majority)
      ) match {
        case Success(status) =>
        case Failure(err)    => println("Error: " + err)
      }
      // end::replace-options[]
    }

    def replaceNamed() {
      // tag::replace-named[]
      collection.replace(docId, json, durability = Durability.Majority) match {
        case Success(status) =>
        case Failure(err)    => println("Error: " + err)
      }
      // end::replace-named[]
    }
  }
}

Otherwise, read on as we introduce the CRUD API and connection to Capella or self-managed Couchbase Server.

> [!TIP]
> There’s a **View** link to the complete sample code on GitHub above each of the snippets on these SDK pages, and a **Copy** icon to grab just the snippet shown.

## [](#connect-to-your-database)Connect to your Database

Connect to your Couchbase Capella operational cluster (or your local Couchbase Cluster, if you are trying out self-managed Couchbase).

* Couchbase Capella
* Self-Managed Couchbase Server
* Cloud Native Gateway (CNG)

```scala
// Update this to your cluster
val endpoint = "cb.<your-endpoint>.cloud.couchbase.com"
val username = "username"
val password = "Password!123"
val bucketName = "travel-sample"

val env = ClusterEnvironment.builder
  .securityConfig(
    SecurityConfig()
      .enableTls(true)
  )
  // Sets a pre-configured profile called "wan-development" to help avoid latency issues
  // when accessing Capella from a different Wide Area Network
  // or Availability Zone (e.g. your laptop).
  .applyProfile(ClusterEnvironment.WanDevelopmentProfile)
  .build
  .get

val cluster = Cluster
  .connect(
    "couchbases://" + endpoint,
    ClusterOptions
      .create(username, password)
      .environment(env)
  )
  .get
```

Note, the client certificate for connecting to a Capella cluster is included in the SDK installation.

```scala
// Update this to your cluster
val username = "Administrator"
val password = "password"
val bucketName = "travel-sample"

val env = ClusterEnvironment.builder
  // You should uncomment this if running in a production environment.
  // .securityConfig(
  //   SecurityConfig()
  //     .enableTls(true)
  // )
  .build
  .get

val cluster = Cluster
  .connect(
    // For a secure cluster connection, use `couchbases://<your-cluster-ip>` instead.
    "couchbase://localhost",
    ClusterOptions
      .create(username, password)
      .environment(env)
  )
  .get
```

Couchbase’s large number of ports across the URLs of many services can be proxied by using a `couchbase2://` endpoint as the connection string — currently only compatible with recent versions of [Couchbase Autonomous Operator](../../../operator/current/concept-cloud-native-gateway.md):

```scala
.connect(
  "couchbase2://10.12.14.16",
  ClusterOptions
    .create(username, password)
    .environment(env)
)
```

Read more on the [Connections](../howtos/managing-connections.md#cloud-native-gateway) page.

The `ClusterEnvironment.builder` is covered more fully on the [Client Settings](../ref/client-settings.md#the-environment-builder) page.

> [!NOTE]
> `Cluster.connect` returns a `Try[Cluster]`, as the Scala client uses functional error handling and does not throw exceptions. You’ll see examples later of how to better handle a `Try`, but for simplicity here we’ll assume the operation succeeded and get the result as a `Cluster` using `.get`.

For a deeper look at connection options, read [Managing Connections](../howtos/managing-connections.md).

> [!TIP]
> The connection code for getting started uses the Administrator password that you were given during set up. In any production app you should create a role restricted to the permissions needed for your app — more on this in [the Security documentation](../concept-docs/best-practices.md#roles-and-rbac).

### [](#opening-a-bucket)Opening a Bucket

Following successful authentication, open the bucket with:

```scala
val bucket = cluster.bucket(bucketName)
bucket.waitUntilReady(30.seconds).get
```

`waitUntilReady` is an optional call, but it is good practice to use it. Opening resources such as buckets is asynchronous — that is, the `cluster.bucket` call returns immediately and proceeds in the background. `waitUntilReady` ensures that the bucket resource is fully loaded before proceeding. If not present, then the first key-value (KV) operation on the bucket will wait for it to be ready. As with the earlier `Cluster.connect`, we use `.get` on the result here for simplicity.

**Collections** allow documents to be grouped by purpose or theme, according to a specified **scope** — see data modeling, [below](#data-modeling). Here we will use the `airport` collection within the `inventory` scope from `travel-sample` bucket as an example.

```scala
val collection = bucket.scope("inventory").collection("airport")
```

## [](#create-read-update-delete)Create, Read, Update, Delete

Couchbase documents are organized into buckets, scopes, and collections. [CRUD operations](https://en.wikipedia.org/wiki/CRUD) — Create, Read, Update, Delete — can be performed upon documents in a collection.

### [](#json)JSON

We’ll create a snippet of JSON to work with, using the client’s own JSON library, but you can read about the Scala SDK’s support for other JSON libraries on the [JSON Libraries](../howtos/json.md) page.

```scala
val json = JsonObject("status" -> "awesome")
```

### [](#insert-create-and-upsert)Insert (Create) and Upsert

`insert` and `upsert` will both create a new document. The difference between the two is that if a document with that key already exists, the `insert` operation will fail, while the `upsert` operation will succeed, replacing the content.

We need to provide a unique ID as the key, and we’ll use a UUID here:

Creating a new document

```scala
val docId = UUID.randomUUID().toString
collection.upsert(docId, json) match {
  case Success(result)    =>
  case Failure(exception) => println("Error: " + exception)
}
```

### [](#get-read)Get (Read)

The `get` method reads a document from a collection.

As mentioned above, the Scala SDK will not throw exceptions. Instead, methods that can error — such as the `upsert` above — will return a Scala `Try` result, which can either be a `Success` containing the result, or a `Failure` containing a _Throwable_ exception. The easiest way to handle a single operation is with pattern matching, as shown above.

Now let’s get the data back (this example will look a little messy due the nested handling of multiple `Try` results, but we’ll see how to clean it up shortly):

```scala
// Get a document
collection.get(docId) match {
  case Success(result) =>
    // Convert the content to a JsonObjectSafe
    result.contentAs[JsonObjectSafe] match {
      case Success(json) =>
        // Pull out the JSON's status field, if it exists
        json.str("status") match {
          case Success(hello) => println(s"Couchbase is $hello")
          case _              => println("Field 'status' did not exist")
        }
      case Failure(err) => println("Error decoding result: " + err)
    }
  case Failure(err) => println("Error getting document: " + err)
}
```

Here we’re fetching the value for the key `docId`, converting that value to a `JsonObjectSafe`(a simple wrapper around `JsonObject` that returns `Try` results — see [JsonObjectSafe](../howtos/json.md#error-handling-and-jsonobjectsafe) for details), and then accessing the value of the **status** key as a String.

#### [](#better-error-handling)Better Error Handling

All three of these operations could fail, so there’s quite a lot of error handling code here to do something quite simple. One way to improve on this is by using `flatMap`, like this:

```scala
val result: Try[String] = collection
  .get(docId)
  .flatMap(_.contentAs[JsonObjectSafe])
  .flatMap(_.str("status"))

result match {
  case Success(status) => println(s"Couchbase is $status")
  case Failure(err)    => println("Error: " + err)
}
```

Alternatively, you can use a for-comprehension, like so:

```scala
val result: Try[String] = for {
  result <- collection.get(docId)
  json <- result.contentAs[JsonObjectSafe]
  status <- json.str("status")
} yield status

result match {
  case Success(status) => println(s"Couchbase is $status")
  case Failure(err)    => println("Error: " + err)
}
```

Either of these methods will stop on the first failed operation. So the final returned `Try` contains either a) `Success` and the result of the final operation, indicating that everything was successful, or b) `Failure` with the error returned by the first failing operation.

### [](#replace-update-and-overloads)Replace (Update) and Overloads

You’ll notice that most operations in the Scala SDK have two overloads. One will take an Options builder, which provides all possible options that operation takes. For instance:

The replace method updates the value of an existing document

```scala
collection.replace(
  docId,
  json,
  ReplaceOptions()
    .expiry(10.seconds)
    .durability(Durability.Majority)
) match {
  case Success(status) =>
  case Failure(err)    => println("Error: " + err)
}
```

These options blocks are implemented as Scala case classes: they are immutable data objects that return a copy of themselves on each change.

The other overload is provided purely for convenience. It takes named arguments instead of an Options object, and provides only the most commonly used options:

```scala
collection.replace(docId, json, durability = Durability.Majority) match {
  case Success(status) =>
  case Failure(err)    => println("Error: " + err)
}
```

> [!CAUTION]
> When you replace a document, it’s usually good practice to use [optimistic locking](../howtos/kv-operations.md#optimistic-locking). Otherwise, changes might get lost if two people change the same document at the same time.

### [](#remove-delete)Remove (Delete)

The remove method deletes a document from a collection:

```scala
collection.remove("document-key") match {
  case Success(result) => println("Document removed successfully")
  case Failure(err: DocumentNotFoundException) =>
    println("The document does not exist")
  case Failure(err) => println("Error: " + err)
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
* [Help forum](https://www.couchbase.com/forums/c/scala-sdk/37).
* [Discord channel](https://discord.com/channels/915294689681362954/1217642561645318194).
* Read the [error handling page](../howtos/error-handling.md).
* [Get help from Couchbase iQ](../../../cloud/get-started/capella-iq/get-started-with-iq.md#generate-sdk-code-preview).

### [](#next-steps)Next Steps

* [Learn more about the Data Service](../concept-docs/data-durability-acid-transactions.md).
* [Discover SQL++](../concept-docs/querying-your-data.md) — our SQL-family querying language.
* Explore some of the [third party integrations](../project-docs/third-party-integrations.md) with Couchbase and the Scala SDK, across the Scala ecosystem.