---
title: Create a Kafka Pipeline Link
pubDate: 2026-08-25T04:30:40.250Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sources/pages/remote-kafka.adoc
  xref: xref:analytics:sources:remote-kafka.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/sources/remote-kafka.html)

# Create a Kafka Pipeline Link

> To continuously update a Capella Analytics collection with a data stream from a Kafka pipeline, you create a remote link. 

After you create a remote link, you must create one or more collections to receive the data.

## [](#reqs)Requirements

Your Capella Analytics account must have either the [Project Owner](../admin/auth/auth-ui.md#project-owner-role) or [Project Manager](../admin/auth/auth-ui.md#project-cluster-manager-role) role to be able to create a link and its associated collection. In addition, you must also have the necessary credentials to read data from the Kafka topic or topics you want to stream into Capella Analytics.

To connect to a Kafka data streaming service, you provide the broker URL or URLs and the authentication type to use with its credentials. For data that's in a format other than JSON, you also provide the schema registry to use and its details.

Capella Analytics supports Confluent Cloud Kafka and Amazon Managed Streaming for Apache Kafka (Amazon MSK) as Kafka sources. When a Debezium connector populates topics, Capella Analytics also supports Oracle and SQL Server as upstream CDC sources. See [Stream CDC Data from Oracle](debezium-oracle.md) and [Stream CDC Data from SQL Server](debezium-sqlserver.md).

* Confluent Cloud Kafka
* Amazon MSK

---

* **Broker URL** or a comma-separated list of URLs.
* **Authentication Type** and its credentials:

  * Plain
  * SCRAM-SHA-256
  * SCRAM-SHA-512
  * OAuth

  * API Key
  * API Key Secret
  * TLS 1.2 or higher encryption

  * API Key
  * API Key Secret
  * TLS 1.2 or later encryption (optional)

  * API Key
  * API Key Secret
  * TLS 1.2 or later encryption (optional)

  * Client ID
  * Client Secret
  * Token Endpoint URL
  * Scope (optional)
  * Logical Cluster (optional)
  * Identity Pool ID (optional)
  * TLS 1.2 or higher encryption
* **Schema Registry Details** for data in non-JSON format:

  * Schema Registry URL
  * Registry API Key
  * Registry API Key Secret  
  For more information, see the [Confluent Cloud documentation](https://docs.confluent.io/cloud/current/get-started/confluent-cloud-basics.html).

---

* **Broker URL** or a comma-separated list of URLs.
* **Authentication Type** and its credentials:

  * SCRAM\_SHA\_512
  * AWS Identity and Access Management (IAM)

  * API Key
  * API Key Secret
  * TLS 1.2 or higher encryption (optional)

  * TLS 1.2 or later encryption (optional)
  * The MSK cluster must have IAM enabled.
  * You must have AWS IAM credentials for the MSK cluster.
* **Schema Registry Details** for data in non-JSON format:

  * AWS Region
  * Schema Registry Name (optional)
  * Access Key ID
  * Access Key Secret
  * Session Token  
  For more information, see the [Amazon Managed Streaming for Apache Kafka documentation](https://docs.aws.amazon.com/msk/latest/developerguide/operations.html).

## [](#create-a-link-to-a-kafka-pipeline)Create a Link to a Kafka Pipeline

To create a link to a Kafka pipeline:

1. In the Capella UI, select the **Capella Analytics** tab.
2. Click a cluster name. The workbench opens.
3. Use the explorer to review the existing databases, scopes, and collections. If you want to set up a database and scope to organize data received from this new source, you can do that now. See [Manage Databases](manage-databases.md) and [Manage Scopes](manage-scopes.md).
4. Select **Create** **Data Link**. The **Create Link for <cluster name> Cluster** dialog opens.
5. Select either **Confluent Cloud/Platform** or **Amazon MSK**.
6. Review the list of prerequisites that appear after select the data source to make sure you have all the necessary information and have configured your Kafka source. Then click **Continue**
7. In the **Link Name** field, enter a name for the link.  
The name must start with a letter (A-Z, a-z) and contain only upper- and lowercase letters, numbers (0-9), and underscore (\_) or dash (-) characters.
8. Supply the **Broker URL** or a comma-separated list of URLs.
9. Select an **Authentication Type** and then supply the credentials. See the [requirements](#reqs) for Confluent Cloud Kafka or Amazon MSK.
10. TLS encryption is optional for some authentication types. To leave data unencrypted, clear **TLS Enabled**.
11. If the data is in a format other than JSON, supply **Schema Registry Details**.
12. Click **Save & Continue**. Capella Analytics creates the link and adds it to the **Links** section of the explorer. The next step is to create a collection to receive the data. Click **Create Linked Collection** to begin creating the collection, or click **Complete Later** to start the next step later. See [Create a Kafka Pipeline Collection](kafka-collection.md).

## [](#see-also)See Also

* [Delete a Collection or Link](delete-entity.md)
* [Stream Data from Remote Sources](manage-remote.md)
* [Access and Organize Data in Capella Analytics Services](database-objects.md)