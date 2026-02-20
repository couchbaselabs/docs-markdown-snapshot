---
title: Start Using the Kotlin SDK
description: A Kotlin application running on the JVM can use the Couchbase
  Kotlin SDK to access a Couchbase cluster.
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/temp/1.4/modules/hello-world/pages/start-using-sdk.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:1.4@kotlin-sdk:hello-world:start-using-sdk.adoc[]
---

[View original HTML](/kotlin-sdk/1.4/hello-world/start-using-sdk.html)

# Start Using the Kotlin SDK

> A Kotlin application running on the JVM can use the Couchbase Kotlin SDK to access a Couchbase cluster. 

The Couchbase Kotlin SDK is built on top of the same high performance I/O core as the Couchbase Java SDK. It provides idiomatic Kotlin features like default arguments, suspend functions, and tasteful DSLs.

## [](#prerequisites)Before You Start

* You should know [how to set up a new Kotlin project using Gradle](https://kotlinlang.org/docs/gradle.html) (or [using Maven](https://kotlinlang.org/docs/maven.html)). The SDK requires Kotlin 1.6.20 or later.
* You will need Java 8 or later. We recommend running the latest Java LTS version with the highest patch version available.

## [](#installing-the-sdk)Installing the SDK

All stable versions of the SDK are [available on Maven Central](https://central.sonatype.com/artifact/com.couchbase.client/kotlin-client/1.4.9).

You can use your favorite dependency management tool to include the SDK in your project.

* Gradle (Kotlin)
* Gradle (Groovy)
* Maven

```kotlin
implementation("com.couchbase.client:kotlin-client:1.4.9")
```

```groovy
implementation "com.couchbase.client:kotlin-client:1.4.9"
```

```xml
<dependency>
  <groupId>com.couchbase.client</groupId>
  <artifactId>kotlin-client</artifactId>
  <version>1.4.9</version>
</dependency>
```

## [](#using-a-snapshot-version-optional)Using a Snapshot Version (optional)

Couchbase publishes pre-release snapshot artifacts to the Sonatype OSS Snapshot Repository. If you wish to use a snapshot version, you’ll need to tell your build tool about this repository.

* Gradle (Kotlin)
* Gradle (Groovy)
* Maven

`**build.gradle.kts**`

```kotlin
repositories {
    mavenCentral()

    maven {
        url = uri("https://oss.sonatype.org/content/repositories/snapshots")
        mavenContent { snapshotsOnly() }
    }
}
```

`**build.gradle**`

```groovy
repositories {
    mavenCentral()

    maven {
        url "https://oss.sonatype.org/content/repositories/snapshots"
        mavenContent { snapshotsOnly() }
    }
}
```

`**pom.xml**`

```xml
<repositories>
  <repository>
    <id>sonatype-snapshots</id>
    <url>https://oss.sonatype.org/content/repositories/snapshots</url>
    <releases><enabled>false</enabled></releases>
    <snapshots><enabled>true</enabled></snapshots>
  </repository>
</repositories>
```

## [](#hello-couchbase)Hello Couchbase

Here’s an example that shows how to execute a SQL++ (formerly N1QL) query and get a document from the Key Value (KV) service.

* Couchbase Capella
* Local Couchbase Server

This version of the example assumes you are connecting to a [Couchbase Capella](https://docs.couchbase.com/cloud/index.html) free tier operational cluster, which has the `travel-sample` bucket installed by default.

(If you’re not using Couchbase Capella, click the **Local Couchbase Server** tab above.)

Before running the example:

* Replace the `address` variable with the address of your Capella cluster.
* Replace the `username` and `password` arguments with credentials for a cluster user that can read the `travel-sample` bucket.

```kotlin
import com.couchbase.client.kotlin.Cluster
import com.couchbase.client.kotlin.query.execute
import kotlinx.coroutines.runBlocking
import kotlin.time.Duration.Companion.seconds

fun main() {
    // Replace with your cluster address.
    val address = "--your-cluster--.cloud.couchbase.com"

    val cluster = Cluster.connect(
        connectionString = "couchbases://$address", (1)
        username = "username", // Replace with credentials
        password = "password", // of a database user account.
    )

    try {
        runBlocking {
            val collection = cluster
                .bucket("travel-sample")
                .waitUntilReady(10.seconds)
                .defaultCollection()

            // Execute a N1QL query
            val queryResult = cluster
                .query("select * from `travel-sample` limit 3")
                .execute()
            queryResult.rows.forEach { println(it) }
            println(queryResult.metadata)

            // Get a document from the K/V service
            val getResult = collection.get("airline_10")
            println(getResult)
            println(getResult.contentAs<Map<String, Any?>>())
        }
    } finally {
        runBlocking { cluster.disconnect() }
    }
}
```

| **1** | For Capella, the connection string starts with couchbases:// (note the final 's') to enable a secure connection with TLS. |
| ----- | ------------------------------------------------------------------------------------------------------------------------- |

This version of the example assumes you are connecting to a single-node Couchbase Server cluster running on your local computer.

Before running the example:

* Install the `travel-sample` [sample bucket](../../../server/7.6/manage/manage-settings/install-sample-buckets.md).
* Replace the `username` and `password` arguments with credentials for a cluster user that can read the `travel-sample` bucket. You can use the administrator credentials you chose when setting up the cluster.

```kotlin
import com.couchbase.client.kotlin.Cluster
import com.couchbase.client.kotlin.query.execute
import kotlinx.coroutines.runBlocking
import kotlin.time.Duration.Companion.seconds

fun main() {
    val cluster = Cluster.connect(
        connectionString = "couchbase://127.0.0.1",
        username = "username", // Replace with credentials
        password = "password", // of a database user account.
    )

    try {
        runBlocking {
            val collection = cluster
                .bucket("travel-sample")
                .waitUntilReady(10.seconds)
                .defaultCollection()

            // Execute a N1QL query
            val queryResult = cluster
                .query("select * from `travel-sample` limit 3")
                .execute()
            queryResult.rows.forEach { println(it) }
            println(queryResult.metadata)

            // Get a document from the K/V service
            val getResult = collection.get("airline_10")
            println(getResult)
            println(getResult.contentAs<Map<String, Any?>>())
        }
    } finally {
        runBlocking { cluster.disconnect() }
    }
}
```

## [](#additional-resources)Additional Resources

To see more documentation, select a chapter from the navigation sidebar on the left.

Join us on the [Couchbase Discord server](https://discord.com/invite/sQ5qbPZuTh) and the [Couchbase Forum](https://forums.couchbase.com/c/kotlin-sdk/40).

The [Couchbase Playground](https://couchbase.live) has Kotlin examples you can edit and run in your web browser.

There are more [code samples on GitHub](https://github.com/couchbase/couchbase-jvm-clients/tree/master/kotlin-client/src/main/kotlin/com/couchbase/client/kotlin/samples).

The API reference is [here](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client/).

Couchbase welcomes community contributions to the Kotlin SDK. The source code is available on [GitHub](https://github.com/couchbase/couchbase-jvm-clients).