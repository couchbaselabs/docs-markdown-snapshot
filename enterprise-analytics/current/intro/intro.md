[View original HTML](/enterprise-analytics/current/intro/intro.html)

> Enterprise Analytics is a self-managed, JSON-native NoSQL analytical database. It serves to unify data from diverse sources, allowing for the execution of complex analytical queries and the extraction of timely insights. 

Enterprise Analytics harnesses the power of NoSQL for analytics. It integrates seamlessly with both Couchbase Server and the Couchbase Capella cloud platform, enabling the creation of real-time, adaptive applications.

Traditionally, analyzing JSON data in NoSQL databases requires complex transformations, like flattening, to prepare it for analytics, causing delays and hindering real-time insights. Enterprise Analytics eliminates these ETL complexities by using a unifying JSON data model with schema flexibility. This allows data to fluidly evolve at its source without requiring manual schema or transformation management. This facilitates a Zero ETL environment, leading to faster time to insight, reduced costs, and increased agility.

![architecture](_images/architecture.png) 

Figure 1\. Enterprise Analytics Architecture

Enterprise Analytics offers the following features:

* A column-oriented, Log-Structured Merge (LSM) tree–based storage engine delivers scalable analytic performance and capacity for customers with self-managed on-premises or cloud deployments. The LSM tree architecture provides high write throughput for fast data ingestion, while columnar storage accelerates analytical queries by accessing only the necessary columns.
* A shared-nothing compute and shared-object storage architecture that allows customers to scale compute resources independently of storage.
* An enhanced MPP-based query engine enables scalable, real-time analytical query computation.
* A cost-based optimizer improves query execution without requiring user intervention. Using a sample-based approach, it quickly estimates data statistics from a small subset of the data, enabling it to identify the lowest-cost query plan without scanning the entire dataset.
* Zero ETL for incoming data, with real-time ingestion capabilities powered by Confluent Kafka, that provide the ability to connect, capture, and extract data from nearly any database or application. One can optionally modify the target JSON structure of the incoming data while in transit, for example, to omit or modify its fields.
* Data Lakehouse capabilities that enable direct querying from supported [object storage](../install/supported-platform.md#supported-object-storage-solutions), with support for formats including JSON, Parquet, Avro, CSV, TSV, and Delta tables, providing the ability for queries to combine external data with other data in Enterprise Analytics.
* A SQL++ based path for writing the results of a query back to the Couchbase Operational data service to support adaptive applications.
* A tabular view facility that provides native SQL-based support for Tableau, PowerBI and Apache Superset for building business reports, visualizations, and dashboards.

|  | Analytics SDKs Analytics SDKs for the Java, Node.js, and Python platforms are available [here](#home:ROOT:analytics-sdk.adoc). |
|  | ------------------------------------------------------------------------------------------------------------------------------ |

## [](#next-steps)Next Steps

* [Do a Quick Install](do-a-quick-install.md)
* [Set up a Cluster](../manage/manage-nodes/create-cluster.md#set-up-a-new-cluster)
* [Configure Enterprise Analytics](../manage/manage-nodes/create-cluster.md#configure-couchbase-server)
* [Connecting to Data Sources](connecting-to-data-sources.md)