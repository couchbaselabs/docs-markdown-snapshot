[View original HTML](/analytics/release-notes/release-notes.html)

## [](#october-2025-changelog)October 2025 Changelog

* Unlimited Columns Support  
Capella Analytics now supports an unlimited number of columns ensuring the flexibility to handle extremely wide schemas for analytical workloads.  
For more information, see [View Metadata for a Collection](../sources/manage-collections.md#view-metadata-for-a-collection).
* Data Transformation During Ingestion  
Capella Analytics introduces lightweight transformation of data during ingestion using SQL++ user-defined functions (UDFs). This enables direct manipulation of incoming data with minimal latency.  
For more information, see [User-Defined Functions](../sqlpp/9%5Fudf.md).
* Support for Heterogeneous Indexes  
Capella Analytics now supports heterogeneous indexes. Indexes no longer require a single data type to be declared in the `CREATE INDEX` statement. Mixing heterogeneous fields with schema-declared fields in index definitions is not supported.  
For more information, see [Indexes](../sqlpp/7%5Fusing%5Findex.md).
* New Built-in Functions  
Capella Analytics introduces three new built-in functions: `sha1_hex` and `sha1_base64` for hashing text, and `from_base` for converting a number string from a given base (radix) into a standard decimal big integer value.  
For more information, see [String Functions](../sqlpp/8%5Fbuiltin%5Fstr.md)

## [](#august-2025-changelog)August 2025 Changelog

Effective today, Capella Columnar has been formally rebranded as Capella Analytics. All relevant documentation and product references have been updated to reflect this change.

## [](#may-2025-changelog)May 2025 Changelog

* Enhanced Data Export with CSV and Parquet  
Capella Analytics now supports exporting query results to external data stores in CSV and Parquet formats using the COPY TO statement.  
This expands upon the existing JSON export capability.  
For more information, see [COPY TO External Data Store Statements](../sqlpp/5%5Fdml%5Fcopy%5Fto%5Fexternal.md).
* TRUNCATE COLLECTION  
Capella Analytics introduces the TRUNCATE COLLECTION statement for a collection, providing a fast and efficient method to remove all data.  
For more information, see [TRUNCATE Statements](../sqlpp/5%5Fdml%5Ftruncate.md).
* Improved Conditional Functions Behavior  
Capella Analytics has updated the behavior of some of its conditional functions such as NULLIF.  
When comparing against a null or missing second argument, these functions consistently return the first argument, aligning with standard SQL behavior.  
For more information, see [Conditional Functions](../sqlpp/8%5Fbuiltin%5Fcond.md).

## [](#march-2025-changelog)March 2025 Changelog

* Expanded AWS region availability  
Capella Analytics supports 2 new AWS regions:

  * Europe (Stockholm)
  * Asia-Pacific (Tokyo)  
For a list of all AWS regions that Capella Analytics now supports, see [Amazon Web Services (AWS)](../reference/aws.md#supported-regions).
* Google Cloud Storage (GCS) Support  
Capella Analytics is now available in select Google Cloud regions, supporting Compute-Optimized (C4A) instances featuring Arm based Axion processors and Titanium SSDs. This integration enhances high-performance analytics capabilities for enterprises leveraging cloud infrastructure, enabling faster insights with greater efficiency.  
For more information, see [Google Cloud Platform (GCP)](../reference/gcp.md).
* DynamoDB Support  
Capella Analytics now supports data ingestion from DynamoDB using the MOLO17 Gluesync connector.  
For more information, see [Create a Collection for a Kafka Data Link](../sources/kafka-collection.md#create-a-collection-for-a-kafka-data-link).
* Ordered Columns  
Capella Analytics now supports ordered columns, ensuring that it preserves the column order specified in the user’s SELECT statement. This aligns with standard SQL behavior, providing consistency and predictability in query results.  
For more information, see [Select Clauses](../sqlpp/3%5Fquery.md#Select%5Fclauses).
* Server RBAC  
We are excited to introduce fine-grained access control in Capella Analytics using a robust roles and privileges model that enables granular, programmatic, and application-level data access on clusters. Access Control Accounts now secure automated and service-to-service interactions without being tied to individual users, while UI tools like the Workbench continue to use separate controls. This update reinforces least privilege principles, improves compliance, and streamlines auditing for enhanced security.  
For more information, see [Create an Access Control Account](../admin/auth/auth-data.md#create-an-access-control-account).

## [](#january-2025-changelog)January 2025 Changelog

* Delta Lake  
Delta Lake is an open-source storage framework that enables building a format agnostic Lakehouse architecture. With this support, Capella Analytics provides read-only access to Delta Lake tables in Amazon S3.  
For more information, see [CREATE an External Collection](../sqlpp/5%5Fddl%5Fexternal.md).
* Apache Superset  
Apache SuperSet is a modern platform for data exploration and visualization. Capella Analytics now includes support for Superset as an additional business intelligence (BI) tool.  
For more information, see [Use Business Intelligence Tools](../query/bi.md).

## [](#november-2024-changelog)November 2024 Changelog

* Visualize Query Results with iQ Insights  
After running a query, you can use iQ Insights to generate a variety of relevant graphs and charts with the help of AI. Use iQ insights to better understand your data and gain more insights from your query results.  
iQ Insights is available to use with both Capella Operational and Capella Analytics clusters.  
For more information, see [Explore Results with iQ Insights](../query/iq-insights.md).

## [](#october-2024-changelog)October 2024 Changelog

* We’re pleased to announce the launch of Capella Analytics SDKs, offering programmatic access to the Capella Analytics service. Capella Analytics SDKs are initially available for the Java, Node.js, and Python platforms, and are tailored to the APIs offered by the Capella Analytics service.

| Capella Analytics SDK         | Documentation                                                     | Quickstart Example                                                                          | SDK API Reference                                                                                         |
| ----------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Java Capella Analytics SDK    | [Docs](../../java-columnar-sdk/current/hello-world/overview.md)   | [Java Getting Started](../../java-columnar-sdk/current/hello-world/start-using-sdk.md)      | [Java Capella Analytics API Reference](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client) |
| Node.js Capella Analytics SDK | [Docs](../../nodejs-columnar-sdk/current/hello-world/overview.md) | [Node.js Getting Started](../../nodejs-columnar-sdk/current/hello-world/start-using-sdk.md) | [Node.js Capella Analytics API Reference](https://docs.couchbase.com/sdk-api/columnar-nodejs-client/)     |
| Python Capella Analytics SDK  | [Docs](../../python-columnar-sdk/current/hello-world/overview.md) | [Python Getting Started](../../python-columnar-sdk/current/hello-world/start-using-sdk.md)  | [Python Capella Analytics API Reference](https://docs.couchbase.com/sdk-api/columnar-python-client/)      |

## [](#august-2024-changelog)August 2024 Changelog

* We’re pleased to announce the launch of Capella Analytics, a new offering designed to enable developers and data platform teams to build responsive analytic applications that can adapt to rapidly changing data needs. Capella Analytics is a NoSQL first analytics database as a service (Online Analytical Processing or OLAP).  
Capella Analytics offers the following features:

  * A column-oriented, Log-Structured Merge (LSM) plus B-tree structured storage engine built to expand the analytic performance and capacity of Capella. Capella Analytics has a shared-nothing compute and shared object storage architecture. Customers can scale compute resources independently of storage.
  * An enhanced MPP-based computation engine, allowing for real-time calculations regardless of data size.
  * Supports cost based optimization for faster and accurate results.
  * Ability to write back results of the query to Couchbase Operational data service using a simple SQL++ query.
  * Zero ETL and real-time ingestion capabilities powered by Confluent Kafka and Amazon Manage Streaming for [Apache Kafka](../sources/remote-kafka.md) (MSK), which provide the ability to connect, capture, and extract data from nearly any database or application. This process also transforms the extracted data into developer-friendly JSON while in transit.
  * File-based reads, imports and exports for data stored in AWS S3 including JSON, Parquet, Avro, CSV, and other text formats.
  * Data Lakehouse by querying directly from S3 and combining it with the data in Capella Analytics.
  * Conversational coding using [Capella iQ](../query/iq.md), to allow developers to use the power of a large language model (LLM) for SQL++ development.
  * Native support for [Tableau and PowerBI](../query/bi.md) for building reports, visualizations, and dashboards.