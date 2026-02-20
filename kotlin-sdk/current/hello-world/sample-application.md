---
title: Quickstart in Couchbase with Kotlin and Ktor
description: Quickstart app to build a REST API using Couchbase Capella in
  Kotlin using Ktor.
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/release/3.9/modules/hello-world/pages/sample-application.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:kotlin-sdk:hello-world:sample-application.adoc[]
---

[View original HTML](/kotlin-sdk/current/hello-world/sample-application.html)

# Quickstart in Couchbase with Kotlin and Ktor

> Quickstart app to build a REST API using Couchbase Capella in Kotlin using Ktor. Discover how to connect to a Couchbase Capella cluster to create, read, update, and delete documents and how to write simple parametrized SQL++ queries. 

After you have navigated through [signing up to Capella](https://cloud.couchbase.com/sign-up), if Kotlin is entered as your chosen language, you will be pointed to a clonable quickstart app on GitHub. If you were not, you can still find it [here](https://developer.couchbase.com/tutorial-quickstart-kotlin-ktor).

Often, the first step developers take after creating their database is to create a REST API that can perform Create, Read, Update, and Delete (CRUD) operations for that database. The [quickstart project](https://developer.couchbase.com/tutorial-quickstart-kotlin-ktor/) is designed to teach you and give you a starter project (in Kotlin, using Ktor) to generate such a REST API. After you have loaded the travel-sample bucket in your database, you can run this application which is a REST API with Swagger documentation so that you can learn:

1. How to create, read, update, and delete documents using [Key-Value operations](#howto:kv-operations). KV operations are unique to Couchbase and provide super fast (under millisecond) operations.
2. How to write simple parametrized [SQL++ queries](#howtos:n1ql-queries-with-sdk.html) using the built-in travel-sample bucket.

This documentation — and a number of other useful developer tutorials — can be found on the [Couchbase Developer Portal](https://developer.couchbase.com/).

## [](#prerequisites)Prerequisites

To run this prebuilt project, you will need:

* A [Couchbase Capella](https://www.couchbase.com/products/capella/) cluster with the [travel-sample](../ref/travel-app-data-model.md) bucket loaded.  
To run this tutorial using a self-managed Couchbase cluster, please refer to the [Running Self Managed Couchbase Cluster](#running-self-managed-couchbase-cluster) section.
* A supported LTS JDK 17+ — see the [compatibility guide](../project-docs/compatibility.md#jdk-compat).  
> [!NOTE]  
> The application is tested with Java 17 and 21\. If you are using a different version of Java, please update the `pom.xml` file accordingly.
* The Travel Sample Bucket — pre-loaded in Capella Free Tier, or see [cloud:clusters:data-service/import-data-documents.adoc#import-sample-data](../../../cloud/clusters/data-service/import-data-documents.md#import-sample-data).
* [Maven 3.6.3+](https://maven.apache.org/install.html).

## [](#app-set-up)App Set-up

We will walk through the different steps required to get the application running:

1. Cloning Repo  
```console  
$ git clone https://github.com/couchbase-examples/kotlin-quickstart.git  
```
2. Navigate to the Project Directory  
```console  
$ cd kotlin-quickstart  
```
3. Install Dependencies  
The dependencies for the application are specified in the `pom.xml` file in the root folder. Dependencies can be installed through `mvn` the default package manager for Java.  
```console  
$ ./gradlew build -x test  
```

### [](#koin-module)Koin module

The quickstart code provides a `Koin` module that exports configuration, cluster, bucket, and scope beans to the application.

src/main/kotlin/com/couchbase/kotlin/quickstart/CouchbaseConfiguration.kt

```kotlin
// Creates a cluster bean
fun createCluster(configuration: CouchbaseConfiguration): Cluster {
  return Cluster.connect(
    connectionString = configuration.connectionString,
    username = configuration.username,
    password = configuration.password,
  )
}


// Creates a bucket bean
@ExperimentalTime
fun createBucket(cluster: Cluster, configuration: CouchbaseConfiguration): Bucket {
  val result : Bucket?
  runBlocking {
    result = cluster.bucket(configuration.bucket).waitUntilReady(10.seconds)
  }
  return result
}

// Creates a bucket scope bean
fun createScope(bucket: Bucket, configuration: CouchbaseConfiguration): Scope {
  return bucket.scope(configuration.scope)
}
```

Configured database objects like the bucket and scope must exist on the cluster prior to starting the application.

### [](#set-up-database-configuration)Set Up Database Configuration

To learn more about connecting to your Capella cluster, please follow the [instructions](https://docs.couchbase.com/cloud/get-started/connect.html). Specifically, you need to do the following:

1. Create the \[database credentials\](<https://docs.couchbase.com/cloud/clusters/manage-database-users.html>) to access the travel-sample bucket (Read and Write) used in the application.
2. [Allow access](https://docs.couchbase.com/cloud/clusters/allow-ip-address.html) to the Cluster from the IP on which the application is running.

All configuration for communication with the database is stored in the `src/main/resources/application.conf` file under the couchbase section:

couchbase {
    connectionString = "couchbases://yourassignedhostname.cloud.couchbase.com"
    username = "Administrator"
    password = "password"
    bucket = "travel-sample"
    scope = "inventory"
}

No The connection string expects the or couchbase:// part.

This includes the connection string, username, password, bucket and scope names. The default username is assumed to be `Administrator` and the default password is assumed to be `password`. These are different in your environment — even for testing against Capella — soyou will need to change them before running the application. The `couchbases://` part of the connection string — note the **s** — tells the SDK to connect using TLS, which is necessary for connecting over the public Internet to apella.

## [](#running-the-application)Running The Application

### [](#directly-on-machine)Directly on Machine

At this point, we have installed the dependencies, loaded the travel-sample data and configured the application with the credentials. The application is now ready and you can run it.

./gradlew run

### [](#using-docker)Using Docker

Build the Docker image

docker build -t couchbase-koltin-quickstart .

### [](#run-the-docker-image)Run the docker image

docker run -e DB_CONN_STR=<connection_string> -e DB_USERNAME=<user_with_read_write_permission_to_travel-sample_bucket> -e DB_PASSWORD=<password_for_user> -p 8080:8080 couchbase-koltin-quickstart

You can access the Application on `<http://0.0.0.0:8080>`.

### [](#verifying-the-application)Verifying the Application

Once the application starts, you can see the details of the application on the logs.

Unresolved include directive in modules/hello-world/pages/sample-application.adoc - include::swagger\_documentation.png\[\]

The application will run on port 8080 of your local machine (<http://0.0.0.0:8080>). You will find the Swagger documentation of the API if you go to the URL in your browser. Swagger documentation is used in this demo to showcase the different API end points and how they can be invoked.

## [](#data-model)Data Model

For this tutorial, we use three collections, airport, airline, and route, that contain sample airports, airlines and airline routes respectively. The route collection connects the airports and airlines as seen in the figure below. We use these connections in the quickstart to generate airports that are directly connected and airlines connecting to a destination airport. Note that these are just examples to highlight how you can use SQL++ queries to join the collections.

Unresolved include directive in modules/hello-world/pages/sample-application.adoc - include::travel\_sample\_data\_model.png\[\]

### [](#extending-api-by-adding-new-entity)Extending API by Adding New Entity

If you would like to add another entity to the APIs, these are the steps to follow:

1. Create the new entity (collection) in the Couchbase bucket. You can create the collection using the [SDK](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.1.8/kotlin-client/com.couchbase.client.kotlin.manager.collection/-collection-manager/index.html#2117033537%2FFunctions%2F1565675143) or via the [Couchbase Server interface](../../../cloud/n1ql/n1ql-language-reference/createcollection.md).
2. Define the routes in a file inside the `src/main/kotlin/com/couchbase/kotlin/quickstart/routes` folder similar to the existing routes.
3. Define the services in a new file inside the `src/main/kotlin/com/couchbase/kotlin/quickstart/services` folder similar to the existing services.
4. Define the repository for this collection inside a new file inside the `src/main/kotlin/com/couchbase/kotlin/quickstart/repositories` folder similar to the existing repositories.
5. Add the tests for the new routes in a new file in the `src/test/kotlin/com/couchbase/kotlin/quickstart` folder similar to the existing ones.

### [](#running-self-managed-couchbase-cluster)Running Self Managed Couchbase Cluster

If you are running this quickstart with a self managed Couchbase cluster, you may need to [load](../../../server/current/manage/manage-settings/install-sample-buckets.md) the travel-sample data bucket in your cluster and generate the credentials for the bucket.

You need to update the connection string and the credentials in the `src/main/resources/application.conf` file in the source folder.

### [](#swagger-documentation)Swagger Documentation

Swagger documentation provides a clear view of the API including endpoints, HTTP methods, request parameters, and response objects.

Click on an individual endpoint to expand it and see detailed information. This includes the endpoint’s description, possible response status codes, and the request parameters it accepts.

#### [](#trying-out-the-api)Trying Out the API

You can try out an API by clicking on the "Try it out" button next to the endpoints.

* **Parameters:** If an endpoint requires parameters, Swagger UI provides input boxes for you to fill in. This could include path parameters, query strings, headers, or the body of a `POST` / `PUT` request.
* **Execution:** Once you’ve inputted all the necessary parameters, you can click the "Execute" button to make a live API call. Swagger UI will send the request to the API and display the response directly in the documentation. This includes the response code, response headers, and response body.

#### [](#models)Models

Swagger documents the structure of request and response bodies using models. These models define the expected data structure using JSON schema and are extremely helpful in understanding what data to send and expect.