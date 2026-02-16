[View original HTML](/kotlin-sdk/current/hello-world/start-using-sdk.html)

> Install, connect, try. A quick start guide to get you up and running with Couchbase and the Kotlin SDK. 

Couchbase has a simple interface for creating and modifying records in a document, based upon the **collection** into which the documents are organized. You can read more about data modeling [below](#data-modeling), but first let’s look at those data operations, and installing the Kotlin SDK.

Upsert

```scala
collection.upsert(
    id = "alice",
    content = mapOf("favoriteColor" to "blue"),
)
```

`upsert` inserts (creates) the document if it does not exist, or replaces it if it does. We’ll explore creating and retrieving data records in more detail [below](#create-read-update-delete), after walking through a quick installation.

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

* The Kotlin SDK is tested against LTS versions of Oracle JDK and OpenJDK — see the [compatibility docs](../project-docs/compatibility.md#jdk-compat).
* The Couchbase Kotlin SDK 3.9 Client supports Kotlin 1.9.0 or later.

The code examples also assume:

* Couchbase Capella
* Self-Managed Couchbase Server

* You have signed up to [Couchbase Capella](https://cloud.couchbase.com/sign-up).
* You have created your own bucket, or loaded the Travel Sample dataset. Note, the Travel Sample dataset is installed automatically when deploying a Capella free tier cluster.
* A user is created with permissions to access the cluster (at least Application Access permissions). See the [Capella connection page](../../../cloud/get-started/run-first-queries.md#credentials) for more details.

|  | Couchbase Capella uses [Roles](../../../cloud/organizations/organization-projects-overview.md) to control user access to cluster resources. For the purposes of this guide, you can use the **Organization Owner** role automatically assigned to your account during installation of the Capella cluster. In production, Couchbase strongly recommends setting up users with more granular access roles as a best practice for data security. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

* [Couchbase Server](#8.0@server:getting-started/do-a-quick-install.adoc) is installed and accessible locally.
* You have created your own bucket, or loaded the Travel Sample dataset using the [Web interface](../../../server/current/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui).
* A user is created with permissions to access your cluster (at least Application Access permissions). See [Manage Users, Groups and Roles](../../../server/current/manage/manage-security/manage-users-and-roles.md) for more details.

|  | Couchbase Server uses [Role-Based Access Control (RBAC)](../../../server/current/learn/security/roles.md) to control access to cluster resources. In this guide we suggest using the **Full Admin** role created during setup of your local Couchbase Server cluster. In production, Couchbase strongly recommends setting up users with more granular access roles as a best practice for data security. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#installation)Installation

All stable versions of the SDK are [available on Maven Central](https://central.sonatype.com/artifact/com.couchbase.client/kotlin-client/{kotlin-current-version}).

More details of the installation process are in the [full installation guide](#project-docs:sdk-full-installation.adoc). You can use your favorite dependency management tool to include the SDK in your project:

* Gradle (Kotlin)
* Gradle (Groovy)
* Maven

```kotlin
implementation("com.couchbase.client:kotlin-client:{kotlin-current-version}")
```

```groovy
implementation "com.couchbase.client:kotlin-client:{kotlin-current-version}"
```

```xml
<dependency>
  <groupId>com.couchbase.client</groupId>
  <artifactId>kotlin-client</artifactId>
  <version>{kotlin-current-version}</version>
</dependency>
```

### [](#ide-plugins)IDE Plugins

To make development easier, Couchbase plugins are available for VSCode and the IntelliJ family of IDEs and editors. For links and more information on these and other integrations across the Kotlin ecosystem, check out the [project-docs:third-party-integrations.adoc](#project-docs:third-party-integrations.adoc) page.

### [](#grab-the-code)Grab the Code

If you’re all set up and in a real hurry, just grab this code sample and add in your Capella details.

Complete Hello World code sample \[**Click to open or collapse the listing**\] 

import com.couchbase.client.kotlin.Cluster
import com.couchbase.client.kotlin.query.execute
import kotlinx.coroutines.runBlocking
import kotlin.time.Duration.Companion.seconds

fun main() {
    // Replace with your cluster address.
    val address = "--your-cluster--.cloud.couchbase.com"

    val cluster = Cluster.connect(
        connectionString = "couchbases://$address", **(1)**
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

Otherwise, read on as we introduce the CRUD API and connection to Capella or self-managed Couchbase Server.

|  | There’s a **View** link to the complete sample code on GitHub above each of the snippets on these SDK pages, and a **Copy** icon to grab just the snippet shown. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#connect-to-your-database)Connect to your Database

Connect to your Couchbase Capella operational cluster (or your local Couchbase Cluster, if you are trying out self-managed Couchbase).

* Couchbase Capella
* Self-Managed Couchbase Server
* Cloud Native Gateway (CNG)

```scala
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

Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$scala/Cloud.scala[]
```

Note, the client certificate for connecting to a Capella cluster is included in the SDK installation.

```scala
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

Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$scala/StartUsing.scala[]
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

|  | Cluster.connect returns a Try\[Cluster\], as the Scala client uses functional error handling and does not throw exceptions. You’ll see examples later of how to better handle a Try, but for simplicity here we’ll assume the operation succeeded and get the result as a Cluster using .get. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

For a deeper look at connection options, read [Managing Connections](../howtos/managing-connections.md).

|  | The connection code for getting started uses the Administrator password that you were given during set up. In any production app you should create a role restricted to the permissions needed for your app — more on this in [the Security documentation](#concept-docs:best-practices.adoc#roles-and-rbac). |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#opening-a-bucket)Opening a Bucket

Following successful authentication, open the bucket with:

```scala
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

Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$scala/Cloud.scala[]
```

`waitUntilReady` is an optional call, but it is good practice to use it. Opening resources such as buckets is asynchronous — that is, the `cluster.bucket` call returns immediately and proceeds in the background. `waitUntilReady` ensures that the bucket resource is fully loaded before proceeding. If not present, then the first key-value (KV) operation on the bucket will wait for it to be ready. As with the earlier `Cluster.connect`, we use `.get` on the result here for simplicity.

**Collections** allow documents to be grouped by purpose or theme, according to a specified **scope** — see data modeling, [below](#data-modeling). Here we will use the `airport` collection within the `inventory` scope from `travel-sample` bucket as an example.

```scala
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

Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$scala/Cloud.scala[]
```

## [](#create-read-update-delete)Create, Read, Update, Delete

Couchbase documents are organized into buckets, scopes, and collections. [CRUD operations](https://en.wikipedia.org/wiki/CRUD) — Create, Read, Update, Delete — can be performed upon documents in a collection.

### [](#json)JSON

We’ll create a snippet of JSON to work with, using the client’s own JSON library, but you can read about the Scala SDK’s support for other JSON libraries on the [Working with JSON](../howtos/json.md) page.

```scala
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

Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$scala/Cloud.scala[]
```

### [](#insert-create-and-upsert)Insert (Create) and Upsert

`insert` and `upsert` will both create a new document. The difference between the two is that if a document with that key already exists, the `insert` operation will fail, while the `upsert` operation will succeed, replacing the content.

We need to provide a unique ID as the key, and we’ll use a UUID here:

Creating a new document

```scala
Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$scala/Cloud.scala[]
```

### [](#get-read)Get (Read)

The `get` method reads a document from a collection.

As mentioned above, the Scala SDK will not throw exceptions. Instead, methods that can error — such as the `upsert` above — will return a Scala `Try` result, which can either be a `Success` containing the result, or a `Failure` containing a _Throwable_ exception. The easiest way to handle a single operation is with pattern matching, as shown above.

Now let’s get the data back (this example will look a little messy due the nested handling of multiple `Try` results, but we’ll see how to clean it up shortly):

```scala
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

Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$scala/Cloud.scala[]
```

Here we’re fetching the value for the key `docId`, converting that value to a `JsonObjectSafe`(a simple wrapper around `JsonObject` that returns `Try` results — see [JsonObjectSafe](../howtos/json.md#error-handling-and-jsonobjectsafe) for details), and then accessing the value of the **status** key as a String.

#### [](#better-error-handling)Better Error Handling

All three of these operations could fail, so there’s quite a lot of error handling code here to do something quite simple. One way to improve on this is by using `flatMap`, like this:

```scala
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

Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$scala/Cloud.scala[]
```

Alternatively, you can use a for-comprehension, like so:

```scala
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

Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$scala/Cloud.scala[]
```

Either of these methods will stop on the first failed operation. So the final returned `Try` contains either a) `Success` and the result of the final operation, indicating that everything was successful, or b) `Failure` with the error returned by the first failing operation.

### [](#replace-update-and-overloads)Replace (Update) and Overloads

You’ll notice that most operations in the Scala SDK have two overloads. One will take an Options builder, which provides all possible options that operation takes. For instance:

The replace method updates the value of an existing document

```scala
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

Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$scala/Cloud.scala[]
```

These options blocks are implemented as Scala case classes: they are immutable data objects that return a copy of themselves on each change.

The other overload is provided purely for convenience. It takes named arguments instead of an Options object, and provides only the most commonly used options:

```scala
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

Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$scala/Cloud.scala[]
```

|  | When you replace a document, it’s usually good practice to use [optimistic locking](../howtos/kv-operations.md#optimistic-locking). Otherwise, changes might get lost if two people change the same document at the same time. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### [](#remove-delete)Remove (Delete)

The remove method deletes a document from a collection:

```scala
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

Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$scala/KvOperations.scala[]
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
* [Help forum](https://www.couchbase.com/forums/c/kotlin-sdk/40).
* [Discord channel](https://discord.com/channels/915294689681362954/1217642561645318194).
* Read the [error handling page](#howtos:error-handling.adoc).
* [Get help from Couchbase iQ](../../../cloud/get-started/capella-iq/get-started-with-iq.md#generate-sdk-code-preview).

### [](#next-steps)Next Steps

* [Learn more about the Data Service](../concept-docs/data-durability-acid-transactions.md).
* [Discover SQL++](#concept-docs:querying-your-data.adoc) — our SQL-family querying language.
* Explore some of the [third party integrations](#project-docs:third-party-integrations.adoc) with Couchbase and the Kotlin SDK, across the Kotlin ecosystem.

# [](#hello-world)Hello World

> Install, connect, try. A quick start guide to get you up and running with Couchbase and the Kotlin SDK. 

Couchbase has a simple interface for creating and modifying records in a document, based upon the **collection** into which the documents are organized. You can read more about data modeling [below](#data-modeling), but first let’s look at those data operations, and installing the Kotlin SDK.

Upsert with Replication set to [Majority Durablity](../concept-docs/data-durability-acid-transactions.md#durable-writes).

```kotlin
collection.upsert(
    id = "alice",
    content = mapOf("favoriteColor" to "blue"),
)
```

`upsert` inserts (creates) the document if it does not exist, or replaces it if it does. We’ll explore creating and retrieving data records in more detail [below](#create-read-update-delete)after walking through a quick installation.

|  | This page walks you through a quick installation, and CRUD examples against the Data Service. Elsewhere in this section you can find a fully worked-through [Quickstart in Couchbase with Kotlin and Ktor](sample-application.md) and, for those new to document (NoSQL) databases, our [Student Record Tutorial](student-record-developer-tutorial.md). |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#before-you-start-2)Before You Start

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

### [](#prerequisites-2)Prerequisites

* The Kotlin SDK is tested against LTS versions of Oracle JDK and OpenJDK — see the [compatibility docs](../project-docs/compatibility.md#jdk-compat).  
[OpenJDK 21 with HotSpot JVM](https://adoptium.net/) is recommended.

The code examples also assume:

* Couchbase Capella
* Self-Managed Couchbase Server

* You have signed up to [Couchbase Capella](https://cloud.couchbase.com/sign-up).
* You have created your own bucket, or loaded the Travel Sample dataset. Note, the Travel Sample dataset is installed automatically when deploying a Capella free tier cluster.
* A user is created with permissions to access the cluster (at least Application Access permissions). See the [Capella connection page](../../../cloud/get-started/run-first-queries.md#credentials) for more details.

|  | Couchbase Capella uses [Roles](../../../cloud/organizations/organization-projects-overview.md) to control user access to cluster resources. For the purposes of this guide, you can use the **Organization Owner** role automatically assigned to your account during installation of the Capella cluster. In production, Couchbase strongly recommends setting up users with more granular access roles as a best practice for data security. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

* [Couchbase Server](#8.0@server:getting-started/do-a-quick-install.adoc) is installed and accessible locally.
* You have created your own bucket, or loaded the Travel Sample dataset using the [Web interface](../../../server/current/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui).
* A user is created with permissions to access your cluster (at least Application Access permissions). See [Manage Users, Groups and Roles](../../../server/current/manage/manage-security/manage-users-and-roles.md) for more details.

|  | Couchbase Server uses [Role-Based Access Control (RBAC)](../../../server/current/learn/security/roles.md) to control access to cluster resources. In this guide we suggest using the **Full Admin** role created during setup of your local Couchbase Server cluster. In production, Couchbase strongly recommends setting up users with more granular access roles as a best practice for data security. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#installation-2)Installation

We recommend running the latest Java LTS version (at the time of writing, JDK 21) with the highest patch version available. Couchbase publishes all stable artifacts to [Maven Central](https://central.sonatype.com/namespace/com.couchbase.client).

The latest version of 3.9.x is [3.9.0](https://central.sonatype.com/artifact/com.couchbase.client/java-client/3.9.0/jar).

More details of the installation process are in the [full installation guide](#project-docs:sdk-full-installation.adoc). In most cases, given the above prerequisites, use your favorite dependency management tool to install the SDK.

* Gradle (Kotlin)
* Gradle (Groovy)
* Maven

```kotlin
implementation("com.couchbase.client:kotlin-client:{kotlin-current-version}")
```

```groovy
implementation "com.couchbase.client:kotlin-client:{kotlin-current-version}"
```

```xml
<dependency>
  <groupId>com.couchbase.client</groupId>
  <artifactId>kotlin-client</artifactId>
  <version>{kotlin-current-version}</version>
</dependency>
```

### [](#ide-plugins-2)IDE Plugins

To make development easier, Couchbase plugins are available for VSCode and the IntelliJ family of IDEs and editors. For links and more information on these and other integrations across the Kotlin ecosystem, check out the [project-docs:third-party-integrations.adoc](#project-docs:third-party-integrations.adoc) page.

### [](#grab-the-code-2)Grab the Code

If you’re all set up and in a real hurry, just grab this code sample and add in your Capella details.

Complete Hello World code sample \[**Click to open or collapse the listing**\] 

Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$StartUsingCapella.kt[]

Otherwise, read on as we introduce the CRUD API and connection to Capella or self-managed Couchbase Server.

|  | There’s a **View** link to the complete sample code on GitHub above each of the snippets on these SDK pages, and a **Copy** icon to grab just the snippet shown. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#connect-to-your-database-2)Connect to your Database

Connect to your Couchbase Capella operational cluster (or your local Couchbase Cluster, if you are trying out self-managed Couchbase).

* Couchbase Capella
* Self-Managed Couchbase Server
* Cloud Native Gateway (CNG)
* Quarkus

```kotlin
Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$StartUsingCapella.kt[]
```

```kotlin
Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$StartUsing.kt[]
```

```kotlin
Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$StartUsing.kt[]
```

Couchbase’s large number of ports across the URLs of many services can be proxied by using a `couchbase2://` endpoint as the connection string — currently only compatible with recent versions of [Couchbase Autonomous Operator](../../../operator/current/concept-cloud-native-gateway.md):

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

|  | The connection code for getting started uses the Administrator password that you were given during set up. In any production app you should create a role restricted to the permissions needed for your app — more on this in [the Security documentation](#concept-docs:best-practices.adoc#roles-and-rbac). |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

The `ClusterEnvironment.Builder` is covered more fully on the [Client Settings](../ref/client-settings.md#the-environment-builder) page.

|  | Simpler Connection There’s also a simpler version of Cluster.connect() for when you don’t need to customize the cluster environment: Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$SimpleConnect.kt\[\] |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#opening-a-bucket-2)Opening a Bucket

Following successful authentication, open the bucket with:

```kotlin
Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$StartUsingCapella.kt[]
```

`waitUntilReady` is an optional call, but it is good practice to use it. Opening resources such as buckets is asynchronous — that is, the `cluster.bucket` call returns immediately and proceeds in the background. `waitUntilReady` ensures that the bucket resource is fully loaded before proceeding. If not present, then the first key-value (KV) operation on the bucket will wait for it to be ready. As with the earlier `Cluster.connect`, we use `.get` on the result here for simplicity.

**Collections** allow documents to be grouped by purpose or theme, according to a specified **scope** — see data modeling, [below](#data-modeling). Here we will use the `airport` collection within the `inventory` scope from `travel-sample` bucket as an example.

```kotlin
Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$StartUsingCapella.kt[]
```

## [](#create-read-update-delete-2)Create, Read, Update, Delete

Couchbase documents are organized into buckets, scopes, and collections. [CRUD operations](https://en.wikipedia.org/wiki/CRUD) — Create, Read, Update, Delete — can be performed upon documents in a collection.

### [](#json-2)JSON

We’ll create a snippet of JSON to work with, using the client’s own JSON library, but you can read about the Scala SDK’s support for other JSON libraries on the [Working with JSON](../howtos/json.md) page.

```kotlin
Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$StartUsingCapella.kt[]
```

### [](#insert-create-and-upsert-2)Insert (Create) and Upsert

`insert` and `upsert` will both create a new document. The difference between the two is that if a document with that key already exists, the `insert` operation will fail, while the `upsert` operation will succeed, replacing the content.

We need to provide a unique ID as the key, and we’ll use a UUID here:

Creating a new document

```kotlin
Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$StartUsingCapella.kt[]
```

### [](#get-read-2)Get (Read)

The `get` method reads a document from a collection.

Wrapping the method in a `Try` / `Catch` is a good way to handle exceptions:

```kotlin
Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$StartUsingCapella.kt[]
```

### [](#replace-update-and-overloads-2)Replace (Update) and Overloads

The replace method updates the value of an existing document

```kotlin
Unresolved include directive in modules/hello-world/pages/start-using-sdk.adoc - include::devguide:example$StartUsingCapella.kt[]
```

|  | When you replace a document, it’s usually good practice to use [optimistic locking](../howtos/kv-operations.md#optimistic-locking). Otherwise, changes might get lost if two people change the same document at the same time. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### [](#remove-delete-2)Remove (Delete)

The remove method deletes a document from a collection:

```kotlin
try {
  collection.remove("my-document");
} catch (DocumentNotFoundException ex) {
  System.out.println("Document did not exist when trying to remove");
}
```

Like `replace`, `remove` also optionally takes the CAS value if you want to make sure you are only removing the document if it hasn’t changed since you last fetched it.

## [](#data-modeling-2)Data Modeling

Documents are organized into collections — collections of documents that belong together. You get to decide what it means to "belong." Developers usually put documents of the same type in the same collection.

For example, imagine you have two types of documents: customers and invoices. You could put the customer documents in a collection called `customers`, and the invoice documents in a collection called `invoices`.

Each document belongs to exactly one collection. A document’s ID is unique _within_ the collection.

Different scopes can hold collections with different names. There is no relationship between collections in different scopes. Each collection belongs to just one scope and a collection’s name is unique within the scope.

More details can be found on the [Data Model page](../concept-docs/data-model.md).

## [](#what-next-2)What Next?

### [](#help-and-troubleshooting-2)Help and Troubleshooting

* [Troubleshooting common network problems](../howtos/troubleshooting-cloud-connections.md).
* [Help forum](https://www.couchbase.com/forums/c/kotlin-sdk/40).
* [Discord channel](https://discord.com/channels/915294689681362954/1217642561645318194).
* Read the [error handling page](#howtos:error-handling.adoc).
* [Get help from Couchbase iQ](../../../cloud/get-started/capella-iq/get-started-with-iq.md#generate-sdk-code-preview).

### [](#next-steps-2)Next Steps

* [Learn more about the Data Service](../concept-docs/data-durability-acid-transactions.md).
* [Discover SQL++](#concept-docs:querying-your-data.adoc) — our SQL-family querying language.
* Explore some of the [third party integrations](#project-docs:third-party-integrations.adoc) with Couchbase and the Kotlin SDK, across the Kotlin ecosystem.

## [](#next-steps-3)Next Steps

Now you’re up and running, try one of the following:

* Our [Travel Sample Application](sample-application.md) demonstrates all the basics you need to know;
* Explore [Key Value Operations](../howtos/kv-operations.md) (CRUD) against a document database;
* Or [Query](#howtos:sqlpp-queries-with-sdk.adoc) with our SQL-based SQL++ query language;
* Try longer-running queries with our [Analytics Service](../howtos/analytics-using-sdk.md);
* A [Full Text Search](#howtos:full-text-searching-with-sdk.adoc);
* Or read up on [which service fits your use case](../concept-docs/data-services.md).

### [](#additional-resources)Additional Resources

The API reference is generated for each release and the latest can be found [here](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/index.html).

Couchbase welcomes community contributions to the Kotlin SDK. The SDK source code is available on [GitHub](https://github.com/couchbase/couchbase-jvm-clients).

### [](#troubleshooting)Troubleshooting

* Couchbase Server is designed to work in the same WAN or availability zone as the client application. If you’re running the SDK on your laptop against a Capella cluster, see further information on:

  * Notes on [Constrained Network Environments](../ref/client-settings.md#constrained-network-environments).
  * [Network Requirements](../project-docs/compatibility.md#network-requirements).
  * If you have a consumer-grade router which has problems with DNS-SRV records review our [Troubleshooting Guide](../howtos/troubleshooting-cloud-connections.md#troubleshooting-host-not-found).
* Our [community forum](https://www.couchbase.com/forums/c/java-sdk/5) is a great source of help.

|  | Connecting to Cloud Native Gateway, for Kubernetes or OpenShift Couchbase’s large number of ports across the URLs of many services can be proxied by using a couchbase2:// endpoint as the connection string — read more on the [Connections](../howtos/managing-connections.md#cloud-native-gateway) page. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |