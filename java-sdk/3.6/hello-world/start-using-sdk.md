---
title: Start Using the Java SDK
description: A quick start guide to get you up and running with Couchbase and the Java SDK.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-java/edit/temp/3.6/modules/hello-world/pages/start-using-sdk.adoc
  xref: xref:3.6@java-sdk:hello-world:start-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.6/hello-world/start-using-sdk.html)

# Start Using the Java SDK

> A quick start guide to get you up and running with Couchbase and the Java SDK. 

The Couchbase Java client allows applications to access a Couchbase cluster. It offers synchronous APIs as well as reactive and asynchronous equivalents to maximize flexibility and performance.

In this guide, you will learn:

* How to [connect to Couchbase Capella or Couchbase Server](#connect).
* How to [add and retrieve Documents](#add-and-retrieve-documents).
* How to [lookup documents](#sql-lookup) with the [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) query language.

## [](#hello-couchbase)Hello Couchbase

We will go through the code sample step by step, but for those in a hurry, here's the complete code:

* Couchbase Capella Sample
* Local Couchbase Server

If you are connecting to [Couchbase Capella](https://docs.couchbase.com/cloud/index.html), you'll need to know the endpoint address, as well as a username and password.

This example requires the Travel Sample Bucket. The Couchbase Capella free tier version comes with this bucket, and its Query indexes, loaded and ready.

```java
import com.couchbase.client.java.*;
import com.couchbase.client.java.kv.*;
import com.couchbase.client.java.json.*;
import com.couchbase.client.java.query.*;

import java.time.Duration;

public class StartUsingCapella {
  // Update these variables to point to your Couchbase Capella instance and credentials.
  static String connectionString = "couchbases://cb.<your-endpoint-here>.cloud.couchbase.com";
  static String username = "username";
  static String password = "Password!123";
  static String bucketName = "travel-sample";

  public static void main(String... args) {
    Cluster cluster = Cluster.connect(
        connectionString,
        ClusterOptions.clusterOptions(username, password).environment(env -> {
          // Sets a pre-configured profile called "wan-development" to help avoid
          // latency issues when accessing Capella from a different Wide Area Network
          // or Availability Zone (e.g. your laptop).
          env.applyProfile("wan-development");
        })
    );

    // Get a bucket reference
    Bucket bucket = cluster.bucket(bucketName);
    bucket.waitUntilReady(Duration.ofSeconds(10));

    // Get a user-defined collection reference
    Scope scope = bucket.scope("tenant_agent_00");
    Collection collection = scope.collection("users");

    // Upsert Document
    MutationResult upsertResult = collection.upsert(
        "my-document",
        JsonObject.create().put("name", "mike")
    );

    // Get Document
    GetResult getResult = collection.get("my-document");
    String name = getResult.contentAsObject().getString("name");
    System.out.println(name); // name == "mike"

    // Call the query() method on the scope object and store the result.
    Scope inventoryScope = bucket.scope("inventory");
    QueryResult result = inventoryScope.query("SELECT * FROM airline WHERE id = 10;");

    // Return the result rows with the rowsAsObject() method and print to the terminal.
    System.out.println(result.rowsAsObject());
  }
}
```

Before running this example, you will need to install the Travel Sample Bucket using either the [Web interface](../../../server/7.6/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui)or the [command line](../../../server/7.6/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-cli).

```java
import com.couchbase.client.java.*;
import com.couchbase.client.java.kv.*;
import com.couchbase.client.java.json.*;
import com.couchbase.client.java.query.*;

import java.time.Duration;

public class StartUsing {
  // Update these variables to point to your Couchbase Server instance and credentials.
  static String connectionString = "couchbase://127.0.0.1";
  static String username = "Administrator";
  static String password = "password";
  static String bucketName = "travel-sample";

  public static void main(String... args) {
    Cluster cluster = Cluster.connect(
        connectionString,
        ClusterOptions.clusterOptions(username, password).environment(env -> {
          // Customize client settings by calling methods on the "env" variable.
        })
    );

    // get a bucket reference
    Bucket bucket = cluster.bucket(bucketName);
    bucket.waitUntilReady(Duration.ofSeconds(10));

    // get a user-defined collection reference
    Scope scope = bucket.scope("tenant_agent_00");
    Collection collection = scope.collection("users");

    // Upsert Document
    MutationResult upsertResult = collection.upsert(
        "my-document",
        JsonObject.create().put("name", "mike")
    );

    // Get Document
    GetResult getResult = collection.get("my-document");
    String name = getResult.contentAsObject().getString("name");
    System.out.println(name); // name == "mike"

    // Call the query() method on the scope object and store the result.
    Scope inventoryScope = bucket.scope("inventory");
    QueryResult result = inventoryScope.query("SELECT * FROM airline WHERE id = 10;");

    // Return the result rows with the rowsAsObject() method and print to the terminal.
    System.out.println(result.rowsAsObject());
  }
}
```

## [](#quick-installation)Quick Installation

We recommend running the latest Java LTS version (i.e. at the time of writing JDK 21) with the highest patch version available. Couchbase publishes all stable artifacts to [Maven Central](https://central.sonatype.com/namespace/com.couchbase.client).

The latest version (as of April 2024) is [3.6.2](https://central.sonatype.com/artifact/com.couchbase.client/java-client/3.6.2/jar).

You can use your favorite dependency management tool to install the SDK.

* Maven
* Gradle

```xml
<dependencies>
    <dependency>
        <groupId>com.couchbase.client</groupId>
        <artifactId>java-client</artifactId>
        <version>3.6.2</version>
    </dependency>
</dependencies>
```

```groovy
implementation 'com.couchbase.client:java-client:3.6.2'
```

See the [installation page](../project-docs/sdk-full-installation.md) for more detailed instructions.

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
> Couchbase Server uses [Role Based Access Control (RBAC)](../../../server/7.6/learn/security/roles.md) to control access to resources. In this guide we suggest using the **Full Admin** role created during setup of your local Couchbase Server cluster. For production client code, you will want to use more appropriate, restrictive settings.

## [](#step-by-step)Step by Step

Here are all the imports needed to run the sample code:

```java
import com.couchbase.client.java.*;
import com.couchbase.client.java.kv.*;
import com.couchbase.client.java.json.*;
import com.couchbase.client.java.query.*;

import java.time.Duration;
```

If you haven't already, create an empty class and add a `main()` method.

```java
public class YourClassName {
    public static void main(String... args) {}
}
```

Make sure to replace `YourClassName` with your own class name.

Above the `main()` method, add the following variables and update them accordingly:

* Couchbase Capella
* Local Couchbase Server

```java
// Update these variables to point to your Couchbase Capella instance and credentials.
static String connectionString = "couchbases://cb.<your-endpoint-here>.cloud.couchbase.com";
static String username = "username";
static String password = "Password!123";
static String bucketName = "travel-sample";
```

```java
// Update these variables to point to your Couchbase Server instance and credentials.
static String connectionString = "couchbase://127.0.0.1";
static String username = "Administrator";
static String password = "password";
static String bucketName = "travel-sample";
```

In the following sections we will populate the `main()` method.

### [](#connect)Connect

Connect to your cluster by calling the `Cluster.connect()` method and pass it your connection details. The basic connection details that you'll need are given below — for more background information, see [Managing Connections](../howtos/managing-connections.md).

* Couchbase Capella
* Local Couchbase Server

From version 3.3, the Java SDK includes Capella's standard Certificate Authority (CA) certificates by default, so you don't need any additional configuration. Capella requires TLS, which you can enable by using a connection string that starts with `couchbases://` (note the final 's').

This example shows how to connect and customize the [Cluster Environment](../howtos/managing-connections.md#cluster-environment) settings.

```java
Cluster cluster = Cluster.connect(
    connectionString,
    ClusterOptions.clusterOptions(username, password).environment(env -> {
      // Sets a pre-configured profile called "wan-development" to help avoid
      // latency issues when accessing Capella from a different Wide Area Network
      // or Availability Zone (e.g. your laptop).
      env.applyProfile("wan-development");
    })
);
```

When accessing Capella from a different Wide Area Network or Availability Zone, you may experience latency issues with the default connection settings. SDK 3.4 introduces a `wan-development` Configuration Profile, which provides pre-configured timeout settings suitable for working in high latency environments. Basic usage is shown in the example above, but if you want to learn more see [Constrained Network Environments](../ref/client-settings.md#constrained-network-environments).

> [!CAUTION]
> The Configuration Profiles feature is currently a [Volatile API](../../current/project-docs/compatibility.md#interface-stability) and may be subject to change.

For developing locally on the same machine as Couchbase Server, your connection string can be `couchbase://127.0.0.1` as shown here. For production deployments, you will want to enable TLS by using `couchbases://` (note the final 's') instead of `couchbase://`.

This example shows how to connect and customize the [Cluster Environment](../howtos/managing-connections.md#cluster-environment) settings.

```java
Cluster cluster = Cluster.connect(
    connectionString,
    ClusterOptions.clusterOptions(username, password).environment(env -> {
      // Customize client settings by calling methods on the "env" variable.
    })
);
```

> [!TIP]
> Simpler Connection
> 
> There's also a simpler version of `Cluster.connect()` for when you don't need to customize the cluster environment:
> 
> ```java
> // Alternatively, connect without customizing the cluster envionrment.
> Cluster cluster = Cluster.connect(connectionString, username, password);
> ```

Now that you have a `Cluster`, add this code snippet to access your `Bucket`:

```java
// Get a bucket reference
Bucket bucket = cluster.bucket(bucketName);
bucket.waitUntilReady(Duration.ofSeconds(10));
```

### [](#add-and-retrieve-documents)Add and Retrieve Documents

The Java SDK supports full integration with the [Collections](../../../server/7.6/learn/data/scopes-and-collections.md) feature introduced in Couchbase Server 7.0\. **Collections** allow documents to be grouped by purpose or theme, according to a specified **Scope**.

Here we refer to the `users` collection within the `tenant_agent_00` scope from the Travel Sample bucket as an example, but you may replace this with your own data.

```java
// Get a user-defined collection reference
Scope scope = bucket.scope("tenant_agent_00");
Collection collection = scope.collection("users");
```

[Data operations](../howtos/kv-operations.md), like storing and retrieving documents, can be done using simple methods on the `Collection` class such as `Collection.get()` and `Collection.upsert()`.

Add the following code to create a new document and retrieve it:

```java
// Upsert Document
MutationResult upsertResult = collection.upsert(
    "my-document",
    JsonObject.create().put("name", "mike")
);

// Get Document
GetResult getResult = collection.get("my-document");
String name = getResult.contentAsObject().getString("name");
System.out.println(name); // name == "mike"
```

### [](#sql-lookup)SQL++ Lookup

Couchbase SQL++ queries can be performed at the `Cluster` or `Scope` level by invoking `Cluster.query()` or `Scope.query()`.

Cluster level queries require you to specify the fully qualified keyspace each time (e.g. `travel-sample.inventory.airline`). However, with a Scope level query you only need to specify the Collection name — which in this case is `airline`:

```java
// Call the query() method on the scope object and store the result.
Scope inventoryScope = bucket.scope("inventory");
QueryResult result = inventoryScope.query("SELECT * FROM airline WHERE id = 10;");

// Return the result rows with the rowsAsObject() method and print to the terminal.
System.out.println(result.rowsAsObject());
```

You can learn more about SQL++ queries on the [Query](../howtos/n1ql-queries-with-sdk.md) page.

### [](#execute)Execute!

Now that you've completed all the steps, run the example via your IDE or through the command line. You should expect to see the following output:

```console
mike
[{"airline":{"country":"United States","iata":"Q5","name":"40-Mile Air","callsign":"MILE-AIR","icao":"MLA","id":10,"type":"airline"}}]
```

## [](#next-steps)Next Steps

Now you're up and running, try one of the following:

* Our [Travel Sample Application](sample-application.md) demonstrates all the basics you need to know;
* Explore [Data Operations](../howtos/kv-operations.md) against a document database;
* Or [Query](../howtos/n1ql-queries-with-sdk.md) with our SQL++ query language;
* Or read up on [which service fits your use case](../concept-docs/data-services.md).

### [](#additional-resources)Additional Resources

The API reference is generated for each release and the latest can be found [here](http://docs.couchbase.com/sdk-api/couchbase-java-client/). Older API references are linked from their respective sections in the [Release Notes](../project-docs/sdk-release-notes.md).

Couchbase welcomes community contributions to the Java SDK. The Java SDK source code is available on [GitHub](https://github.com/couchbaselabs/couchbase-jvm-clients).

If you are planning to use Spring Data Couchbase, see the [notes on version compatibility](../project-docs/compatibility.md#spring-compat).

### [](#troubleshooting)Troubleshooting

* Couchbase Server is designed to work in the same WAN or availability zone as the client application. If you're running the SDK on your laptop against a Capella cluster, see further information on:

  * Notes on [Constrained Network Environments](../ref/client-settings.md#constrained-network-environments).
  * [Network Requirements](../project-docs/compatibility.md#network-requirements).
  * If you have a consumer-grade router which has problems with DNS-SRV records review our [Troubleshooting Guide](../howtos/troubleshooting-cloud-connections.md#troubleshooting-host-not-found).
* Our [community forum](https://forums.couchbase.com/c/java-sdk/5) is a great source of help.