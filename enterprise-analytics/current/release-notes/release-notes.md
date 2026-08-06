---
title: Enterprise Analytics Release Notes
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/release-notes/pages/release-notes.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:enterprise-analytics:release-notes:release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/release-notes/release-notes.html)

# Enterprise Analytics Release Notes

## [](#release-2-2-1-july-2026)Release 2.2.1 (July 2026)

Enterprise Analytics 2.2.1, released in July 2026, is a maintenance release that resolves the following issues.

### [](#issues-and-improvements)Issues and Improvements

The following table lists resolved issues and improvements included in this release:

| Category                                  | Topic                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                       | Issue                                                         |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Storage & Connectivity                    | S3 batch delete Content-MD5 support                                                                                                                                                                                                                                                         | Enterprise Analytics failed to connect to S3-compatible stores that require the legacy Content-MD5 header on batch delete requests, such as Huawei OBS. Batch delete requests now include this header.                                                                            | [MB-72785](https://jira.issues.couchbase.com/browse/MB-72785) |
| Azure client ID applied to storage client | On Azure deployments that use a user-assigned managed identity, the configured blobStorageAzureClientId value was not passed to the underlying blob storage client, which then authenticated with the wrong identity. The client ID now passes through to the storage client's credentials. | [MB-72853](https://jira.issues.couchbase.com/browse/MB-72853)                                                                                                                                                                                                                     |                                                               |
| Connectivity validation errors surfaced   | Blob storage connectivity validation failures returned only a generic exit status 1 error from POST /settings/analytics, hiding the actual cause. The API response now includes the detailed validation error, making misconfigurations easier to diagnose.                                 | [MB-72859](https://jira.issues.couchbase.com/browse/MB-72859)                                                                                                                                                                                                                     |                                                               |
| Query Engine & Indexes                    | Query hang with nested filter predicates                                                                                                                                                                                                                                                    | A query using UNNEST over nested arrays combined with a column filter predicate could hang indefinitely instead of returning results. Column filter evaluation is now corrected so these queries return results.                                                                  | [MB-72388](https://jira.issues.couchbase.com/browse/MB-72388) |
| Data Processing                           | Column count accounting for meta fields                                                                                                                                                                                                                                                     | Ingestion did not account for columns contributed by document metadata when it estimated the column count for a page, including columns added by xattrs in the DCP stream. This under-accounting could cause a page overflow. Column counting now includes these metadata fields. | [MB-72946](https://jira.issues.couchbase.com/browse/MB-72946) |
| Option to include xattrs during ingestion | Enterprise Analytics always ingested extended attributes (xattrs), with no option to exclude them. xattr ingestion is now optional and disabled by default, controlled via a new service-level configuration dcpIngestXattrs.                                                               | [MB-72948](https://jira.issues.couchbase.com/browse/MB-72948)                                                                                                                                                                                                                     |                                                               |

## [](#release-2-2-june-2026)Release 2.2 (June 2026)

Enterprise Analytics 2.2, released in June 2026, introduces the following new features:

* Google Cloud Storage Support  
Google Cloud Storage (GCS) is now supported as both an underlying storage layer for deployments and as an external data source. You can query files stored in GCS directly using external collections, and export processed results back to GCS using the COPY TO statement.  
For more information, see [Google Cloud Storage](../manage/manage-nodes/google-cloud-storage.md), [Query Data in Google Cloud Storage](../sources/external-gcs.md), and [COPY TO External Data Store Statements](../sqlpp/5%5Fdml%5Fcopy%5Fto%5Fexternal.md).
* Apache Iceberg Support  
Enterprise Analytics now supports read-only access to Apache Iceberg. You can register supported catalogs — such as AWS Glue and BigLake Metastore — and directly query Iceberg table data stored in external object storage using external collections.  
For more information, see [Apache Iceberg Support](../sqlpp/5%5Fddl%5Ficeberg.md).
* Data Streaming from Oracle and SQL Server  
Enterprise Analytics now streams continuous, row-level data changes from Oracle and SQL Server databases directly into your collections. Powered by Kafka links and Debezium connectors, this integration captures operational updates in real time with full CDC fidelity.  
For more information, see [Stream CDC Data from Oracle](../sources/debezium-oracle.md) and [Stream CDC Data from SQL Server](../sources/debezium-sqlserver.md).
* SQL++ UPDATE Statement  
Enterprise Analytics introduces the `UPDATE` statement, which enables you to modify documents in standalone and remote collections. The statement supports updating scalar values, nested fields, and array elements, and accepts a `WHERE` clause to filter the documents to update.  
For more information, see [UPDATE Statement](#sqlpp:5%5Fdml%5Fupdate.adoc).
* Index Advisor  
The Index Advisor analyzes SQL++ queries and recommends secondary indexes that can improve query execution performance.  
For more information, see [Index Advisor](#sqlpp:5c%5Findex-advisor.adoc).
* Index-Only Query Plans  
Enterprise Analytics now supports index-only query plans, allowing the query engine to serve requests entirely from index data when a covered index is available, accelerating response times by eliminating the need to fetch the underlying records.  
For more information, see [Using Indexes](../sqlpp/7%5Fusing%5Findex.md).
* JWT Authentication  
Enterprise Analytics adds support for JSON Web Token (JWT) authentication. JWT tokens can be used to authenticate REST API calls and query requests, including tokens issued by external identity providers. External users can also be granted Enterprise Analytics RBAC roles without requiring a local Couchbase account.  
For more information, see [Configure JWT Authentication](../manage/manage-security/configure-jwt.md).
* Asynchronous REST API  
Enterprise Analytics now supports asynchronous query execution, allowing you to submit long-running queries without blocking application workflows. Applications can send requests asynchronously, poll for execution status, and retrieve the final results in a subsequent REST API call.  
For more information, see [Analytics Service REST API](../analytics-rest-service/index.md).

## [](#issues-and-improvements-2)Issues and Improvements

The following table lists resolved issues and improvements included in this release.

| Category                                                               | Topic                                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                | Issue                                                         |
| ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Storage & Connectivity                                                 | GCS and S3 HTTP connection settings not honored                                                                                                                                                                                                                                                           | Cloud HTTP connection idle timeout and maximum lifetime settings were not applied to GCS and S3 clients. Connection behavior now correctly reflects the configured values. | [MB-71767](https://jira.issues.couchbase.com/browse/MB-71767) |
| Static credential rotation after driver restart                        | Updated static credentials were not applied until the driver was restarted. Credential rotation now takes effect without requiring a restart.                                                                                                                                                             | [MB-71496](https://jira.issues.couchbase.com/browse/MB-71496)                                                                                                              |                                                               |
| Azure hierarchical namespace validation                                | Azure Blob Storage connection validation now correctly checks whether the hierarchical namespace is compatibly configured before allowing link creation.                                                                                                                                                  | [MB-71432](https://jira.issues.couchbase.com/browse/MB-71432)                                                                                                              |                                                               |
| Parquet COPY INTO failure for Azure Blob Storage                       | COPY INTO for Parquet files stored in Azure Blob Storage failed with an internal error. The statement now executes correctly against Azure Blob Storage.                                                                                                                                                  | [MB-71164](https://jira.issues.couchbase.com/browse/MB-71164)                                                                                                              |                                                               |
| Cloud storage settings visible without restart                         | Updates to cloud storage settings were not reflected in node diagnostics output until the driver was restarted. Diagnostic output now reflects configuration changes without requiring a restart.                                                                                                         | [MB-72234](https://jira.issues.couchbase.com/browse/MB-72234)                                                                                                              |                                                               |
| S3-compatible storage change detection mode configurable               | External links to S3-compatible storage that do not support ETags could fail because the default change detection mode (server) requires ETag support. The changeDetectionMode property is now configurable on S3 external links, allowing it to be set to none for storage systems without ETag support. | [MB-71726](https://jira.issues.couchbase.com/browse/MB-71726)                                                                                                              |                                                               |
| Parquet inputStream and changeDetectionMode properties available in UI | The inputStream and changeDetectionMode Parquet properties were configurable via the REST API but were not available in the Enterprise Analytics UI during link creation. Both properties are now included in the UI.                                                                                     | [MB-72281](https://jira.issues.couchbase.com/browse/MB-72281)                                                                                                              |                                                               |
| Query Engine & Indexes                                                 | LEFT JOIN alias in correlated NOT EXISTS                                                                                                                                                                                                                                                                  | A NullPointerException could occur when a LEFT JOIN alias was referenced inside a correlated NOT EXISTS clause. The query now executes correctly.                          | [MB-71638](https://jira.issues.couchbase.com/browse/MB-71638) |
| Plan instability on predicate switch                                   | Switching between equivalent predicates could produce different query plans for the same query. Plans are now stable for equivalent predicate forms.                                                                                                                                                      | [MB-71042](https://jira.issues.couchbase.com/browse/MB-71042)                                                                                                              |                                                               |
| Cost-based optimizer secondary index costing                           | The cost-based optimizer could fall back to a full data scan instead of using available secondary indexes. Index costing has been corrected to prevent unnecessary scan fallback.                                                                                                                         | [MB-71010](https://jira.issues.couchbase.com/browse/MB-71010)                                                                                                              |                                                               |
| B-tree and Array index intersection                                    | B-tree and Array indexes were not intersected during query planning, preventing optimal use of multiple indexes. Index intersection is now applied correctly.                                                                                                                                             | [MB-70981](https://jira.issues.couchbase.com/browse/MB-70981)                                                                                                              |                                                               |
| Cluster Management                                                     | Link stuck in inconsistent state after drop                                                                                                                                                                                                                                                               | A link could become permanently stuck in an inconsistent state (error CBAS0096) after DROP LINK was issued on a running link. Link lifecycle handling has been corrected.  | [MB-71946](https://jira.issues.couchbase.com/browse/MB-71946) |
| Recovery loop on KV collection recreate                                | Recreating a KV collection could trigger a recovery loop due to inconsistent partition state. The restart logic now handles this case correctly.                                                                                                                                                          | [MB-71707](https://jira.issues.couchbase.com/browse/MB-71707)                                                                                                              |                                                               |
| DCP ingestion state lost on resume                                     | Resuming DCP ingestion after a restart could fail because the DCP state was not found. Ingestion state is now correctly preserved and restored across restarts.                                                                                                                                           | [MB-71382](https://jira.issues.couchbase.com/browse/MB-71382)                                                                                                              |                                                               |
| Kafka collection metadata cleanup on drop                              | Dropping a Kafka-linked collection did not fully remove the associated metadata, leaving stale entries. Metadata is now fully cleaned up when a collection is dropped.                                                                                                                                    | [MB-71333](https://jira.issues.couchbase.com/browse/MB-71333)                                                                                                              |                                                               |
| Partition reassignment timing during node recovery                     | Partitions could be reassigned before the required access token expiry interval elapsed during node recovery, causing access errors. Partition reassignment now waits for the interval to elapse before proceeding.                                                                                       | [MB-71274](https://jira.issues.couchbase.com/browse/MB-71274)                                                                                                              |                                                               |
| Data Processing                                                        | Multi-byte characters corrupted in CSV output                                                                                                                                                                                                                                                             | Multi-byte and emoji characters were corrupted in CSV query output. Character encoding is now handled correctly in CSV output.                                             | [MB-71405](https://jira.issues.couchbase.com/browse/MB-71405) |
| COPY TO fails with INTERVAL type columns                               | A COPY TO statement that included a column of INTERVAL type caused an internal error. The type is now handled correctly.                                                                                                                                                                                  | [MB-71111](https://jira.issues.couchbase.com/browse/MB-71111)                                                                                                              |                                                               |

## [](#known-issues)Known Issues

The following issues are known to affect Enterprise Analytics 2.2.

### [](#query-engine)Query Engine

**Scan Consistency Client Hangs** ([MB-72484](https://jira.issues.couchbase.com/browse/MB-72484))

`request_plus` scan consistency queries hang or time out in Enterprise Analytics.

**Root Cause:** `DcpStateTracker` uses the IO device count instead of the storage partition count to determine when the dataset state is complete. On Enterprise Analytics, a node with 2 IO devices may host 8 storage partitions. The partition count never matches the IO device count, so the `seqno` is never reported as complete, causing `request_plus` queries to hang indefinitely.

**Symptoms:**

* `request_plus` queries time out or hang without returning results.
* Enterprise Analytics returns a scan wait timeout error.

**Workaround:**No workaround available.

### [](#apache-iceberg-support)Apache Iceberg Support

**Iceberg Discovery Functions Return Internal Error Instead of Specific Error Messages** ([MB-72418](https://jira.issues.couchbase.com/browse/MB-72418))

Certain errors encountered during Iceberg catalog discovery return a generic internal error instead of a specific error message.

**Root Cause:**Iceberg data source functions do not handle all error types correctly.

**Symptoms:**

* `list_iceberg_catalogs()`, `list_iceberg_namespaces()`, `list_iceberg_tables()`, or `list_iceberg_snapshots()` returns `Internal Error` when an error occurs.

**Workaround:**No workaround available. To identify the underlying error, check `analytics_info.log` for the statement targeting the relevant data source function — the error is logged there. Alternatively, collect logs and share with Couchbase Support.

**`list_iceberg_catalogs()` Returns `namespace` Instead of `catalog` as the Field Name** ([MB-72486](https://jira.issues.couchbase.com/browse/MB-72486))

`list_iceberg_catalogs()` returns the catalog name under the field `namespace` instead of `catalog`.

**Root Cause:**The data source function uses an incorrect field name for the catalog identifier. Only the data source function is affected; the list catalogs REST API returns the correct field name.

**Symptoms:**

* `list_iceberg_catalogs()` returns `{"namespace": "myCatalogName"}` instead of `{"catalog": "myCatalogName"}`.

**Workaround:**Use the list catalogs REST API, which returns the correct field name.

### [](#storage-connectivity)Storage & Connectivity

**GCS Link `applicationDefaultCredentials` Accepts a String Instead of a Boolean** ([MB-72371](https://jira.issues.couchbase.com/browse/MB-72371))

The `applicationDefaultCredentials` parameter for GCS links accepts only the string `"true"`, not a JSON `boolean`.

**Root Cause:** `applicationDefaultCredentials` is modeled and validated as a string, rather than a `boolean`. This is inconsistent with other `boolean` link parameters, such as `disableSslVerify`.

**Symptoms:**

* Setting `applicationDefaultCredentials` to `false` returns `INVALID_PARAM_VALUE_ALLOWED_VALUE`.
* Application Default Credentials cannot be explicitly disabled by setting the parameter to `false`.

**Workaround:**Omit `applicationDefaultCredentials` from the request body to disable Application Default Credentials.

**Unique Identifiers Used as Field Names Cause Schema Growth and Memory Errors** ([MB-72487](https://jira.issues.couchbase.com/browse/MB-72487))

Schemas grow without bound when unique identifiers, such as UUID or transaction ID values, are used as JSON field names.

**Root Cause:**Each unique field name creates a new column in the column storage layer. Thousands of unique field names cause the schema to grow to thousands of columns, leading to OutOfMemory errors and slow merge operations.

**Symptoms:**

* OutOfMemory errors occur during ingestion.
* Ingestion pipeline performance degrades.
* Memory usage increases, approaching the memory quota.

**Workaround:**Avoid using unique identifiers as JSON field names. Store unique identifiers as field values instead.

### [](#data-formats)Data Formats

**Avro Format Treats `NULL` Values as `MISSING`** ([MB-72320](https://jira.issues.couchbase.com/browse/MB-72320))

When Enterprise Analytics reads Avro files, fields with `null` values are omitted from results instead of returning `null`.

**Root Cause:**The Avro parser handles `NULL` values as `MISSING`, causing null fields to be absent from query results.

**Symptoms:**

* Fields expected to return `null` are absent from query results.

**Workaround:**Use `IFMISSING()` to convert missing fields back to `null`:

```SQL++
SELECT IFMISSING(nullableField, null) AS nullableField FROM myCollection;
```

## [](#release-2-1-november-2025)Release 2.1 (November 2025)

Enterprise Analytics 2.1, a self-managed version, was released in November 2025\. This release contains the following features:

* Microsoft Azure Support for Enterprise Analytics

  * Enterprise Analytics expands deployment flexibility by introducing native support for Microsoft Azure. Customers can now use Azure Blob Storage as the storage layer for their deployments.  
  For more information, see [Azure Blob Storage](../manage/manage-nodes/azure-blob-storage.md).
  * External collections now support Azure Blob Storage. This feature allows external query access, enabling direct querying of data files residing in external object storage, without requiring data movement.  
  For more information, see [Set Up an External Data Source](../sources/manage-external.md).
  * The COPY TO statement can now write processed data back to Azure Blob Storage.  
  For more information, see [COPY TO External Data Store Statements](../sqlpp/5%5Fdml%5Fcopy%5Fto%5Fexternal.md).
* Unlimited column support  
Enterprise Analytics removes previous constraints on schema width by introducing unlimited column support.  
For more information, see [View Metadata for a Collection](../sources/manage-collections.md#view-metadata-for-a-collection).
* Data transformation during ingestion  
Enterprise Analytics introduces the ability to perform lightweight data transformations directly during ingestion using SQL++ User-Defined Functions (UDFs).  
For more information, see [User-Defined Functions](../sqlpp/9%5Fudf.md).

## [](#release-2-0-august-2025)Release 2.0 (August 2025)

Couchbase is pleased to announce the launch of Enterprise Analytics, our robust data management solution that enables developers and data platform teams to create responsive analytic applications that adapt to rapidly changing data needs. Enterprise Analytics delivers the powerful capabilities seen in our cloud offering, Capella Analytics (formerly Capella Columnar), but in a new form that's optimized for on-premise and self-managed deployments.

Enterprise Analytics 2.0 includes the following features:

* A column-oriented, Log-Structured Merge (LSM) tree based storage engine built to deliver scalable analytic performance and capacity in customers' on-premise and/or self-managed environments. Enterprise Analytics has a shared-nothing compute and shared-object storage architecture that allows customers to scale compute resources independently of storage.
* An enhanced MPP-based query engine, enabling scalable, real-time analytical query computation.
* A [cost-based query optimizer](../sqlpp/5b%5Fcbo.md) for improved query planning without user intervention.
* A [SQL++](../sqlpp/5%5Fdml%5Fcopy%5Fto%5Fkv.md) based path for writing the results of a query back to the Couchbase Operational data service to support adaptive applications.
* [Zero ETL](../sources/remote-kafka.md) for incoming data, with real-time ingestion capabilities powered by Confluent Kafka, that provide the ability to connect, capture, and extract data from nearly any database or application.
* Data Lakehouse capabilities that enable direct [querying from Amazon S3 and S3-compatible storage](../sources/manage-external.md), with support for formats including JSON, Parquet, Avro, CSV, TSV, and Delta tables, providing the ability for queries to combine external data with other data in Enterprise Analytics.
* Native SQL-based support for [Tableau, PowerBI, and Apache Superset](../query/bi.md) for building business reports, visualizations, and dashboards.