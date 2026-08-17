---
title: Start Using the Scala SDK
description: Get up and running quickly, installing the Couchbase Scala SDK, and
  running our Hello World example.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-scala/edit/temp/1.6/modules/hello-world/pages/start-using-sdk.adoc
  xref: xref:1.6@scala-sdk:hello-world:start-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/1.6/hello-world/start-using-sdk.html)

# Start Using the Scala SDK

> Get up and running quickly, installing the Couchbase Scala SDK, and running our Hello World example. 

The Couchbase Scala SDK allows Scala applications to access a Couchbase cluster.

## [](#hello-couchbase)Hello Couchbase

On this page we show you how to quickly get up and running — installing the Couchbase Scala SDK, and trying out the _Hello World_ code example against Couchbase Capella, or against a local Couchbase cluster.

We will go through the code sample step by step, but for those in a hurry to see it, here it is:

* Couchbase Capella Sample
* Local Couchbase Server

```scala
/*
 * Copyright (c) 2022 Couchbase, Inc.
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

object Cloud {
  def main(args: Array[String]): Unit = {
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

    val bucket = cluster.bucket(bucketName)
    bucket.waitUntilReady(30.seconds).get

    // get a reference to the default collection, required for Couchbase server 6.5 or earlier
    // val collection = bucket.defaultCollection

    val collection = bucket.scope("inventory").collection("airport")

    val json = JsonObject("status" -> "awesome")

    val docId = UUID.randomUUID().toString
    collection.upsert(docId, json) match {
      case Success(result)    =>
      case Failure(exception) => println("Error: " + exception)
    }

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

    def getFor() {
      val result: Try[String] = for {
        result <- collection.get(docId)
        json <- result.contentAs[JsonObjectSafe]
        status <- json.str("status")
      } yield status

      result match {
        case Success(status) => println(s"Couchbase is $status")
        case Failure(err)    => println("Error: " + err)
      }
    }

    def getMap() {
      val result: Try[String] = collection
        .get(docId)
        .flatMap(_.contentAs[JsonObjectSafe])
        .flatMap(_.str("status"))

      result match {
        case Success(status) => println(s"Couchbase is $status")
        case Failure(err)    => println("Error: " + err)
      }
    }

    def replaceOptions() {
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
    }

    def replaceNamed() {
      collection.replace(docId, json, durability = Durability.Majority) match {
        case Success(status) =>
        case Failure(err)    => println("Error: " + err)
      }
    }
  }
}
```

```scala
/*
 * Copyright (c) 2022 Couchbase, Inc.
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

object StartUsing {
  def main(args: Array[String]): Unit = {
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

    val bucket = cluster.bucket(bucketName)
    bucket.waitUntilReady(30.seconds).get

    val collection = bucket.defaultCollection

    val json = JsonObject("status" -> "awesome")

    val docId = UUID.randomUUID().toString
    collection.upsert(docId, json) match {
      case Success(result)    =>
      case Failure(exception) => println("Error: " + exception)
    }

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

    def getFor() {
      val result: Try[String] = for {
        result <- collection.get(docId)
        json <- result.contentAs[JsonObjectSafe]
        status <- json.str("status")
      } yield status

      result match {
        case Success(status) => println(s"Couchbase is $status")
        case Failure(err)    => println("Error: " + err)
      }
    }

    def getMap() {
      val result: Try[String] = collection
        .get(docId)
        .flatMap(_.contentAs[JsonObjectSafe])
        .flatMap(_.str("status"))

      result match {
        case Success(status) => println(s"Couchbase is $status")
        case Failure(err)    => println("Error: " + err)
      }
    }

    def replaceOptions() {
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
    }

    def replaceNamed() {
      collection.replace(docId, json, durability = Durability.Majority) match {
        case Success(status) =>
        case Failure(err)    => println("Error: " + err)
      }
    }
  }
}
```

The Couchbase Capella free tier version comes with the Travel Sample Bucket, and its Query indexes, loaded and ready.

## [](#quick-install)Quick Install

A more detailed guide in our [Installation page](../project-docs/sdk-full-installation.md) covers every supported platform, but this section should be enough to get up and running in most cases.

* SBT
* Gradle
* Maven

```sbt
libraryDependencies += "com.couchbase.client" %% "scala-client" % "1.6.2"
```

This will automatically use the Scala 2.12 or 2.13 builds, as appropriate for your SBT project.

It can be included in your `build.gradle` like this for 2.13:

```groovy
dependencies {
    compile group: 'com.couchbase.client', name: 'scala-client_2.13', version: '1.6.2'
}
```

For Scala 2.12, refer to the full [Installation page](../project-docs/sdk-full-installation.md).

It can be included in your Maven `pom.xml` like this for 2.13:

```xml
<dependencies>
    <dependency>
        <groupId>com.couchbase.client</groupId>
        <artifactId>scala-client_2.13</artifactId>
        <version>1.6.2</version>
    </dependency>
</dependencies>
```

For Scala 2.12, refer to the full [Installation page](../project-docs/sdk-full-installation.md).

## [](#prerequisites)Prerequisites

The following code samples assume:

* Couchbase Capella
* Local Couchbase Server

* You have signed up to [Couchbase Capella](https://cloud.couchbase.com/sign-up).
* You have created your own bucket, or loaded the Travel Sample dataset. Note, the Travel Sample dataset is installed automatically when deploying a Capella free tier cluster.
* A user is created with permissions to access the cluster (at least Application Access permissions). See the [Capella connection page](../../../cloud/get-started/run-first-queries.md#credentials) for more details.

> [!IMPORTANT]
> Couchbase Capella uses [Roles](../../../cloud/organizations/organization-projects-overview.md) to control user access to database resources. For the purposes of this guide, you can use the **Organization Owner** role automatically assigned to your account during installation of the Capella cluster. In a production scenario, we strongly recommend setting up users with more granular access roles as a best practice.

* [Couchbase Server](#7.6@server:getting-started/do-a-quick-install.adoc) is installed and accessible locally.
* You have created your own bucket, or loaded the Travel Sample dataset using the [Web interface](../../../server/7.6/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui).
* A user is created with permissions to access your cluster (at least Application Access permissions). See [Manage Users, Groups and Roles](../../../server/7.6/manage/manage-security/manage-users-and-roles.md) for more details.

> [!IMPORTANT]
> Couchbase Server uses [Role Based Access Control (RBAC)](../../../server/7.6/learn/security/roles.md) to control access to resources. In this guide we suggest using the **Full Admin** role created during setup of your local Couchbase Server cluster. For production client code, you will want to use more appropriate, restrictive settings.

## [](#step-by-step)Step by Step

Here's the above Hello World example, broken down into individual actions.

First pull in all the imports we'll be using:

```scala
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
```

### [](#connect)Connect

Now that you have the Scala client installed, try out the following to connect to a Couchbase cluster. The basic connection details that you'll need are given below — for more background information, refer to the [Managing Connections page](../howtos/managing-connections.md#connection-strings).

* Couchbase Capella
* Local Couchbase Server

You connect to a [Couchbase Capella](https://docs.couchbase.com/cloud/index.html) cluster the same as any other cluster, except that the use of TLS is mandatory, and the `couchbases://` connection string prefix should be used to allow DNS SRV lookup.

> [!IMPORTANT]
> As of Scala SDK version 1.3.0, the standard certificate required to connect to a Capella cluster is automatically included with no additional configuration.

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

When accessing Capella from a different Wide Area Network or Availability Zone, you may experience latency issues with the default connection settings. SDK 1.4 introduces a `wan-development` Configuration Profile, which provides pre-configured timeout settings suitable for working in high latency environments. Basic usage is shown in the example above, but if you want to learn more see [Constrained Network Environments](../ref/client-settings.md#constrained-network-environments).

> [!CAUTION]
> The Configuration Profiles feature is currently a [Volatile API](../../current/project-docs/compatibility.md#interface-stability) and may be subject to change.

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

For developing locally on the same machine as Couchbase Server, your URI can be `couchbase://localhost` as shown here. For production deployments, you will want to use a secure server, with `couchbases://`.

> [!NOTE]
> `Cluster.connect` returns a `Try[Cluster]`, as the Scala client uses functional error handling and does not throw exceptions. You'll see examples later of how to better handle a `Try`, but for simplicity here we'll assume the operation succeeded and get the result as a `Cluster` using `.get`.

Following successful authentication, the bucket can be opened:

```scala
val bucket = cluster.bucket(bucketName)
bucket.waitUntilReady(30.seconds).get
```

`waitUntilReady` is an optional call. Opening resources such as buckets is asynchronous — that is, the `cluster.bucket` call returns immediately and proceeds in the background. `waitUntilReady` ensures that the bucket resource is fully loaded before proceeding. If not present, then the first Key Value (KV) operation on the bucket will wait for it to be ready. As with `Cluster.connect`, we use `.get` on the result here for simplicity.

The Scala SDK supports full integration with the [Collections](../concept-docs/collections.md) feature introduced in Couchbase Server 7.0\. _Collections_ allow documents to be grouped by purpose or theme, according to a specified _Scope_. Here we will use the `users` collection within the `tenant_agent_00` scope from `travel-sample` bucket as an example.

```scala
// get a reference to the default collection, required for Couchbase server 6.5 or earlier
// val collection = bucket.defaultCollection

val collection = bucket.scope("inventory").collection("airport")
```

If you do not refer to a named collection, you can access the 'default collection', which includes all documents in a bucket, and is forwards and backwards compatible with all supported versions of Couchbase Server.

### [](#json)JSON

Now we can do some simple Key Value operations. First, let's create some JSON.

The Scala SDK directly supports several popular JSON libraries, including [uPickle/uJson](https://github.com/lihaoyi/upickle), [Circe](https://circe.github.io/circe/), [Play Json](https://github.com/playframework/play-json), [Jawn](https://github.com/typelevel/jawn), and [Json4s](https://github.com/json4s/json4s) (if you'd like to see your favorite supported, please let us know). In addition you can supply JSON encoded into a `String` or `Array[Byte]`, opening the door to any JSON library; [Jsoniter](https://jsoniter.com/) and [Jackson](https://github.com/FasterXML/jackson) have been tested this way, but any should work.

You can also directly encode and decode Scala case classes to and from the SDK.

To make things easy and to help get you started, the Scala SDK also bundles a home-grown small JSON library, which you are free to use instead of or alongside any of the other supported JSON libraries. The philosophy behind this library is to provide a very easy-to-use API and the fastest JSON implementation possible.

These options are described in detail [here](../howtos/json.md), but to get us started let's created some simple JSON using the built-in JsonObject library:

```scala
val json = JsonObject("status" -> "awesome")
```

### [](#key-value-operations)Key-Value Operations

And now let's upsert it into Couchbase (upsert is an operation that will insert the document if it does not exist, or replace it if it does). We need to provide a unique ID for the JSON, and we'll use a UUID here:

```scala
val docId = UUID.randomUUID().toString
collection.upsert(docId, json) match {
  case Success(result)    =>
  case Failure(exception) => println("Error: " + exception)
}
```

As mentioned above, the Scala SDK will not throw exceptions. Instead, methods that can error - such as the `upsert` above - will return a Scala `Try` result, which can either be a `Success` containing the result, or a `Failure` containing a _Throwable_ exception. The easiest way to handle a single operation is with pattern matching, as shown above.

Now let's get the data back (this example will look a little messy due the the nested handling of multiple `Try` results, but we'll see how to clean it up shortly):

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

Here we're fetching the value for the key `docId`, converting that value to a `JsonObjectSafe` (a simple wrapper around `JsonObject` that returns `Try` results - see [here](../howtos/json.md#error-handling-and-jsonobjectsafe) for details), and then accessing the value of the **status** key as a String.

### [](#better-error-handling)Better Error Handling

All three of these operations could fail, so there's quite a lot of error handling code here to do something quite simple. One way to improve on this is by using flatMap, like this:

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

### [](#overloads)Overloads

You'll notice that most operations in the Scala SDK have two overloads. One will take an Options builder, which provides all possible options that operation takes. For instance:

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

These options blocks are implemented as Scala case classes, e.g. they are immutable data objects that return a copy of themselves on each change.

The other overload is provided purely for convenience. It takes named arguments instead of an Options object, and provides only the most commonly used options:

```scala
collection.replace(docId, json, durability = Durability.Majority) match {
  case Success(status) =>
  case Failure(err)    => println("Error: " + err)
}
```

## [](#next-steps)Next Steps

Now you're up and running, try one of the following:

* Our [Travel Sample Application](sample-application.md) demonstrates all the basics you need to know;
* Explore [Key Value Operations](../howtos/kv-operations.md) (CRUD) against a document database;
* Or [Query](../howtos/n1ql-queries-with-sdk.md) with our SQL-based SQL++ query language;
* Try longer-running queries with our [Analytics Service](../howtos/analytics-using-sdk.md);
* A [Full Text Search](../howtos/full-text-searching-with-sdk.md);
* Or read up on [which service fits your use case](../concept-docs/data-services.md).

### [](#additional-resources)Additional Resources

The Scala SDK includes three APIs. The examples above show the simple blocking API, for simplicity, but you can also perform all operations in an async style using Scala `Future`, and a reactive style using Project Reactor `SMono` and `SFlux`. Please see [Choosing an API](../howtos/concurrent-async-apis.md) for more details.

The API reference is generated for each release and the latest can be found [here](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/index.html).

Couchbase welcomes community contributions to the Scala SDK. The SDK source code is available on [GitHub](https://github.com/couchbase/couchbase-jvm-clients).

### [](#troubleshooting)Troubleshooting

* Couchbase Server is designed to work in the same WAN or availability zone as the client application. If you're running the SDK on your laptop against a Capella cluster, see further information on:

  * Notes on [Constrained Network Environments](../ref/client-settings.md#constrained-network-environments).
  * [Network Requirements](../project-docs/compatibility.md#network-requirements).
  * If you have a consumer-grade router which has problems with DNS-SRV records review our [Troubleshooting Guide](../howtos/troubleshooting-cloud-connections.md#troubleshooting-host-not-found).
* Our [community forum](https://forums.couchbase.com/c/scala-sdk/37) is a great source of help.