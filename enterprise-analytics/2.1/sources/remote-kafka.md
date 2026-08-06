---
title: Create a Kafka Pipeline Link
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sources/pages/remote-kafka.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:2.1@enterprise-analytics:sources:remote-kafka.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/sources/remote-kafka.html)

# Create a Kafka Pipeline Link

> To continuously update an Enterprise Analytics collection with a data stream from a Kafka pipeline, you create a remote link. 

After you create a remote link, you must create 1 or more collections to receive the data.

## [](#reqs)Requirements

Your Enterprise Analytics account must have the `**Enterprise Analytics Access**` role along with specific privileges to be able to create a link and its associated collection. In addition, you must also have the necessary credentials to read data from the Kafka topic or topics you want to stream into Enterprise Analytics.

To connect to a Kafka data streaming service, you provide the broker URL or URLs and the authentication type to use with its credentials. For data that's in a format other than JSON, you also provide the schema registry to use and its details.

Enterprise Analytics supports Confluent Cloud Kafka as Kafka sources:

* Confluent Cloud Kafka

---

* **Broker URL** or a comma-separated list of URLs.
* **Authentication Type** and its credentials:

  * Plain
  * SCRAM-SHA-256
  * SCRAM-SHA-512

  * API Key
  * API Key Secret
  * TLS 1.2 or higher encryption

  * API Key
  * API Key Secret
  * TLS 1.2 or later encryption (optional)

  * API Key
  * API Key Secret
  * TLS 1.2 or later encryption (optional)
* **Schema Registry Details** for data in non-JSON format:

  * Schema Registry URL
  * Registry API Key
  * Registry API Key Secret  
  For more information, see the [Confluent Cloud documentation](https://docs.confluent.io/cloud/current/get-started/confluent-cloud-basics.html).

## [](#create-a-link-to-a-kafka-pipeline)Create a Link to a Kafka Pipeline

To create a link to a Kafka pipeline:

1. In the UI, select the **Workbench** tab.
2. Click **\+ new link**.
3. In the **Link Name** field, enter a name for the link.  
The name must start with a letter (A-Z, a-z) and contain only upper- and lowercase letters, numbers (0-9), and underscore (\_) or dash (-) characters.
4. In the **Link Type** field, select **Kafka**.  
> [!NOTE]  
> The **Vendor** field is populated with **Confluent** by default.
5. In the **Bootstrap Servers** field, enter the URL of the bootstrap server.  
> [!NOTE]  
> If there are multiple URLs, separate them with commas.
6. In the **Authentication** field, select 1 of the options.
7. TLS encryption is optional for some authentication types. To leave data unencrypted, clear TLS Enabled.
8. Select **Custom Schema registry** so that collections associated with this link can handle schema types other than JSON.
9. Click **Save**.

See [Create a Kafka Pipeline Collection](kafka-collection.md).

## [](#see-also)See Also

* [Delete a Collection or Link](delete-entity.md)
* [Stream Data from Remote Sources](manage-remote.md)
* [Access and Organize Data in Enterprise Analytics](database-objects.md)