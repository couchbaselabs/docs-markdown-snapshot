---
title: Migration
description: This section provides a step-by-step guide for migrating your data
  and applications to Couchbase Capella Analytics or Enterprise Analytics.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/migration/pages/migration-process.adoc
  xref: xref:2.0@enterprise-analytics:migration:migration-process.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/migration/migration-process.html)

# Migration

> This section provides a step-by-step guide for migrating your data and applications to Couchbase Capella Analytics or Enterprise Analytics. 

It covers the migration process, schema design, indexing strategies, query migration, security configuration, SDK updates, and integration with BI tools. Follow these instructions to make sure you have a smooth and efficient migration with minimal disruption to your existing workflows.

## [](#data-migration)Data Migration

You can migrate your data using 1 of the 3 migration paths.

### [](#capella-operational-analytics-service-to-capella-analytics)Capella Operational (Analytics Service) to Capella Analytics

1. Stream data hosted on a Couchbase Capella operational cluster to Capella Analytics using remote links.  
For more information, see [Stream Data from Couchbase Capella](../../../analytics/sources/remote-cb-capella.md).
2. Query data in external object storage by creating an external link and associating it with an external collection.  
For more information, see [Set Up an External Data Source](../../../analytics/sources/manage-external.md).
3. Perform migration within the same cloud provider region to minimize data transfer charges.  
For more information, see [Supported Cloud Providers](../../../analytics/reference/cloud-providers.md).

### [](#couchbase-server-analytics-service-to-capella-analytics)Couchbase Server (Analytics Service) to Capella Analytics

1. Stream data hosted on a Couchbase Server to Capella Analytics using remote links.  
For more information, see [Stream Data from Couchbase Server](../../../analytics/sources/remote-cb-server.md).
2. Query data in external object storage by creating an external link and associating it with an external collection.  
For more information, see [Set Up an External Data Source](../../../analytics/sources/manage-external.md).

### [](#couchbase-server-analytics-service-to-enterprise-analytics)Couchbase Server (Analytics Service) to Enterprise Analytics

1. Stream data hosted on a Couchbase Server to Enterprise Analytics using remote links.  
For more information, see [Stream Data from Couchbase Server](../../current/sources/remote-cb-server.md).
2. Query data in external object storage by creating an external link and associating it with an external collection.  
For more information, see [Set Up an External Data Source](../../current/sources/manage-external.md).

## [](#schema-design-naming-convention-and-bi-tools)Schema Design, Naming Convention, and BI tools

Before migrating your data and integrating BI tools, it's important to plan your schema design and query migration. This ensures optimal performance, compatibility, and a seamless transition to Capella Analytics or Enterprise Analytics. The complexity of schema design and query migration depends on several factors. Some factors are the structure of existing data, differences between Analytics Service and Capella Analytics or Enterprise Analytics environments, and specific requirements of your applications.

* Data Hierarchy
* Schema Conversion Guidelines
* Naming Convention
* BI Tools

Couchbase Server or Capella Operational

Couchbase stores data within a logical hierarchy of buckets, scopes, and collections. This enables separation between documents of different types.

For more information, see [Query Concepts](../../../server/current/n1ql/n1ql-intro/queriesandresults.md) and [Buckets, Scopes, and Collections](../../../cloud/clusters/data-service/about-buckets-scopes-collections.md).

Capella Analytics or Enterprise Analytics

Capella Analytics and Enterprise Analytics organizes entities into a hierarchy based on their levels. To fully qualify 1 of these database objects in your queries, prefix its entity identifier with those of its database and scope in the format `database_name.scope_name.database_object_name`.

For more information, see [Entities in Capella Analytics Services](../../../analytics/sqlpp/1a%5Fentities.md) and [Entities in Enterprise Analytics](../../current/sqlpp/1a%5Fentities.md).

Analytics Service

In Analytics Service for Capella Operational and Couchbase Server, an Analytics scope serves as the top-level entity. You can design these scopes to simulate the hierarchy of Data Service buckets and scopes. As a result, an Analytics scope can have 1 or 2 parts. This means an Analytics scope can either be a single `bucket_name` or a 2-part `bucket_name.scope_name`, mirroring the Data Service structure.

For more information, see [Data Definition Language (DDL)](../../../server/current/analytics/5%5Fddl.md).

It's important to understand how you can map data entities from Analytics Service to Capella Analytics or Enterprise Analytics. You can determine this mapping based on how the Analytics Service's scopes simulate the Data Service's bucket and scope hierarchy.

* 2-Part Analytics Service Scope:

If you reference an Analytics Service collection as `scope_name.collection_name` where the `scope_name` is a 2-part structure, it maps as follows in Capella Analytics or Enterprise Analytics:

* Database: `bucket_name`
* Scope: `scope_name`
* Collection: `collection_name`

For example, travel.inventory.airline

* Single-Part Analytics Service Scope:

If you reference an Analytics Service collection as `scope_name.collection_name` where the `scope_name` is a single part, it implies the Analytics Service scope simulates a Data Service scope within its default bucket and maps as follows in Capella or Enterprise Analytics:

* Database: default
* Scope: scope\_name
* Collection: collection\_name

For example inventory.airline,

* Unqualified Analytics Service Collection:

  1. If you reference an Analytics Service with any prefix, for example, airline, it resides in the Default Analytics Service Scope and maps as follows in Capella or Enterprise Analytics:

    1. Database: default
    2. Scope: default
    3. Collection: collection\_name (For example, airline)

Capella Analytics or Enterprise Analytics naming conventions allow migration without requiring immediate renaming of entities.

> [!NOTE]
> Couchbase Analytics bucket names permit periods (.) and percent symbols (%). However, Capella Analytics and Enterprise Analytics database and scope names explicitly forbid the use of the period (.) character.

For more information about requirements for Identifiers, see [Requirements for Identifiers](../sqlpp/1a%5Fentities.md#names).

Capella Analytics and Enterprise Analytics has connectivity to Business Intelligence tools for data visualization.

> [!NOTE]
> No changes are being made to JDBC and ODBC drivers

For more information about Business Intelligence tools, see [BI Tools](../query/bi.md).

## [](#indexing-strategy)Indexing Strategy

Capella Analytics and Enterprise Analytics may require fewer secondary indexes because of their architecture and enhanced query performance. If required, create, and optimize secondary indexes on the new cluster to make sure you get efficient query performance for your applications.

## [](#query-migration)Query Migration

SQL++ syntax is consistent between Analytics Service and Capella Analytics or Enterprise Analytics environments. As a result, you typically do not need to make fundamental changes to your query syntax during migration.

The main consideration during query migration is ensuring that namespaces are resolved correctly. If your data migration accurately maps data to the appropriate databases, scopes, and collections in Capella Analytics or Enterprise Analytics, existing queries automatically reference the correct entities. This typically removes the need to manually update query text for namespace changes.

User-Defined Functions (UDFs) will continue to work as long as their data references (namespaces) are properly mapped during migration. You do not need to make any changes if namespaces are resolved.

For example, if a collection in Analytics Service is located at Scope: default and Collection: airline, is migrated to Database: default, Scope: default, and Collection: airline in the target environment, no update to the query is required.

## [](#security-configuration)Security Configuration

You must design the security configuration to error or enhance the security posture of the Analytics Services system.

Capella Analytics offers a more granular Role-Based Access Control (RBAC) compared to Analytics Service. To use the Capella UI, you need an organization role and 1 or more project roles.

For more information, see [Assign Roles for UI Access](../../../analytics/admin/auth/auth-ui.md).

To use the Enterprise Analytics UI, you need the `**Enterprise Analytics Access**` role along with specific privileges. For more information, see [Role Based Access Control (RBAC)](../manage/manage-security/rbac-overview.md).

## [](#sdk-migration)SDK Migration

The new SDKs that are supported for migration are:

1. Java
2. .NET
3. Go
4. Node.js
5. Python

To use them, you must include the analytics libraries described later on and re-write the relevant code. Couchbase recommends that you set up a replica of the analytics application using the new SDKs to A/B test the old and new applications as shown in the following steps.

1. Update dependencies of your application to include new couchbase analytics SDK. For example, if you use Java, add `couchbase-analytics-java-client` library via Apache Maven, Gradle or manually.
2. Use the new Analytics connection management to connect to the new Capella Analytics or Enterprise Analytics endpoint.
3. Migrate rest of the code.

For more information, see [Migrate Code to Use the new Analytics SDK](#migratecodenewanalytics)

> [!NOTE]
> Differences include using async APIs or reactor compared to Java virtual threads.

### [](#migratecodenewanalytics)Migrate Code to Use the new Analytics SDK

You must update the rest of the code such as connection management and executing queries. For an example using Java SDKs, see the following:

* Update dependency
* Connection Management
* Execute Query
* Connection and Query Options
* Reactive and Async API
* Change all the import class paths
* Error handling

* Operational SDK  
```xml  
<dependency>  
    <groupId>com.couchbase.client</groupId>  
    <artifactId>java-client</artifactId>  
    <version>3.7.9</version>  
```
* Enterprise Analytics SDK  
Add the maven dependency to your pom.xml file.  
```xml  
<dependency>  
  <groupId>com.couchbase.client</groupId>  
  <artifactId>couchbase-analytics-java-client</artifactId>  
  <version>1.0.0</version> <!-- Use latest stable version -->  
</dependency>  
```

* Operational SDK  
```java  
Cluster cluster = Cluster.connect("couchbases://...","uname","pwd");  
```
* Enterprise Analytics SDK  
```java  
Cluster cluster = Cluster.newInstance(  
   "https://...",  
   Credential.of("uname","pwd");  
```

> [!NOTE]
> The URL begins with `https://` instead of `couchbases://`

* Operational SDK  
```java  
AnalyticsResult result = cluster.analyticsQuery(  
  "select * from airport limit 3");  
for (JsonObject row : result.rowsAsObject()) {  
  System.out.println("Found row: " + row);  
}  
```
* Enterprise Analytics SDK  
You can use 1 of the following to execute queries:

  * Buffered mode. Execute a query and buffer all result rows in client memory  
  ```java  
  QueryResult result = cluster.executeQuery(  
    "select * from Default.Default.orders");  
  result.rows().forEach(row ->  
    System.out.println("Got row: " + row));  
  ```
  * Streaming mode. Execute a query and process rows as they arrive from server.  
  ```java  
  cluster.executeStreamingQuery(  
    "select * from Default.Default.orders",  
    row -> System.out.println("Got row: " + row)  
  );  
  ```

* Operational SDK  
Options such as clientContextID, readonly and others.
* Enterprise Analytics SDK

* Operational SDK  
```java  
Mono<ReactiveAnalyticsResult> result = cluster  
  .reactive()  
  .analyticsQuery("select 1=1");  
result  
  .flatMapMany(ReactiveAnalyticsResult::rowsAsObject)  
  .subscribe(row -> System.out.println("Found row: " + row));  
```
* Enterprise Analytics SDK  
```java  
var reactor = ReactorQueryable.from(analyticsClusterOrScope);  
Mono<ReactorQueryResult> resultMono = reactor  
  .executeQuery(  
    "SELECT RAW i FROM ARRAY_RANGE(0, 10) as i");  
resultMono  
  .flatMapMany(ReactorQueryResult::rows)  
  .map(row -> row.as(Integer.class))  
  .doOnNext(System.out::println)  
  .blockLast();  
```

* Operational SDK  
```java  
import com.couchbase.client.java.Cluster;  
import com.couchbase.client.java.ClusterOptions;  
```
* Enterprise Analytics SDK  
```java  
import com.couchbase.analytics.client.java.Cluster;  
import com.couchbase.analytics.client.java.Credential;  
```

Update your error handling to catch an `AnalyticsException` (such as `AnalyticsTimeoutException`) instead of `ColumnarException`.

* Operational SDK  
```java  
try { } catch (CouchbaseException e)  
```
* Enterprise Analytics SDK  
```java  
try { } catch (AnalyticsException e)  
```

> [!NOTE]
> There are more exception handling classes such as `TimeoutException` which you will also need to refactor.

### [](#sparkpyspark-migration)Spark/PySpark Migration

If you use a spark connector, use the new analytics read format from the spark connector as mentioned in the following steps. NOTE: The connector `` jar` `` file remains the same and you need to update the library to the newest version.

1. Change spark/pyspark code to use the new read/write format:  
```python  
spark.read.format("couchbase.enterprise-analytics").load()  
```
2. Change the URL to point to the new analytics cluster. You do not need to make changes to the rest of the code to use the new analytics cluster via Spark or PySpark.