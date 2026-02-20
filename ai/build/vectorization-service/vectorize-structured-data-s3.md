---
title: Vectorize Structured Data from Amazon S3
description: Use a Capella Structured Data Workflow to automatically generate
  embedding vectors from JSON data in an Amazon S3 Bucket. Use embedding vectors
  for similarity searches on your data.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/build/pages/vectorization-service/vectorize-structured-data-s3.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:ai:build:vectorization-service/vectorize-structured-data-s3.adoc[]
---

[View original HTML](/ai/build/vectorization-service/vectorize-structured-data-s3.html)

# Vectorize Structured Data from Amazon S3

> Use a Capella Structured Data Workflow to automatically generate embedding vectors from JSON data in an Amazon S3 Bucket. Use embedding vectors for similarity searches on your data. 

The Vectorization Service automatically creates a [Vector Search index](../../../cloud/vector-search/vector-search.md) for your embeddings - letting you get started right away with Vector Search. You can use Vector Search to support Retrieval Augmented Generation (RAG) in your applications, or for other vector similarity use cases.

Your data must already be extracted, filtered, and chunked in preparation for generating embeddings. Data must be in **JSON**, **JSON List**, or **JSON Lines** format. If your data is not already in JSON format, see [Process and Vectorize Unstructured Data](vectorize-unstructured-data.md).

To generate your embeddings, you can use a model [hosted by the Capella Model Service](../model-service/deploy-embed-model.md) or [OpenAI](https://openai.com/). Capella stores the generated vector embeddings and Vector Search index in an operational cluster.

## [](#prerequisites)Prerequisites

* You have read-only credentials available for the Amazon S3 bucket where your data is stored. For more information about AWS access keys, see [the AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id%5Fcredentials%5Faccess-keys.html).
* If you want to use a model hosted on Capella, you must have:

  * Deployed a Capella embedding model. For more information, see [Deploy an Embedding Model](../model-service/deploy-embed-model.md).
  * Your model’s **API Key ID** and **API Key Token**. For more information about API keys for Capella models, see [Get Started with AI Services APIs](../../api-guide/api-start.md).
* If you want to use a model hosted by OpenAI, you have your OpenAI API Key. For more information about how to find your OpenAI API Key, see [the OpenAI Help Center](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key).
* You have deployed an operational cluster that has the following:

  * Couchbase Server version 8.0 or later.
  * The Search Service and Eventing Service running on at least 1 Service Group. For more information, see [Services and Service Groups](../../../cloud/clusters/databases.md#couchbase-services).
  * A bucket that can store the Vector Search index and any generated vector embeddings.  
  Use any bucket settings you would prefer for your particular use case. For more information, see [Manage Buckets](../../../cloud/clusters/data-service/manage-buckets.md).

## [](#procedure)Procedure

To create a new Structured Data workflow and process your JSON data:

1. Go to **AI Services** **Workflows**.
2. Click **Create New Workflow**.
3. Click **Structured Data from External sources**.
4. In the **Workflow Name** field, enter a name to identify your Structured Data Workflow, or accept the automatically generated name.  
Workflow names can be a maximum of 128 characters and can include letters (A-Z, a-z), numbers (0-9), dashes (-), and underscores (\_).
5. Click **Start Workflow**.
6. [Configure Your Amazon S3 Bucket](#configure-s3).
7. Do 1 of the following:

  1. To use an existing field in your data for your document ID values, click **Manually Enter Document ID Field** and provide your document ID field name.
  2. To automatically generate document IDs in a new field for all documents, click **Autogenerate ID Field**.
8. [Configure Your Source Fields](#configure-data).
9. Choose whether to **Create HyperScale Vector Index (now)** or **Create HyperScale Vector Index (later)**.
10. Under **Destination Cluster**, in the **Destination Operational Cluster** list, select the cluster you configured in the [Prerequisites](#prerequisites).
11. Set the **Destination Bucket**, **Destination Scope**, and **Destination Collection** for your vector embeddings.
12. [Choose Your Embedding Model](#choose-embedding).
13. Verify your workflow configuration.
14. Click **Run Workflow**.

> [!CAUTION]
> Do not delete or modify the metadata scope, collections, or Eventing functions created by your new Workflow. If you modify or delete the metadata or functions, you must delete your Workflow and create a new one.

### [](#configure-s3)Configure Your Amazon S3 Bucket

Choose whether to use a new Amazon S3 bucket or choose an S3 bucket that you have already saved as an integration with Capella AI Services.

> [!TIP]
> You can manage your saved Amazon S3 bucket credentials from the [Integrations page](../../admin/manage-ai-integrations.md).

* New Amazon S3 Bucket
* Use Existing Amazon S3 Bucket

To configure a new Amazon S3 bucket:

1. Click **Add New S3 Bucket Integration**.
2. In the **Integration Name** field, enter a name to use to identify your credentials and make it easier to manage them from the [Integrations page](../../admin/manage-ai-integrations.md).
3. Enter the details and credentials for accessing your Amazon S3 bucket.  
It’s recommended to use read-only credentials for your S3 bucket. Make sure you have your **Access Key ID** and its **Secret Access Key**.  
> [!TIP]  
> You can also choose to use temporary credentials, supported by a session token. For more information about configuring temporary credentials and session tokens, see [the AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id%5Fcredentials%5Ftemp%5Fuse-resources.html).
4. Click **Add Credentials**.
5. In the **S3 Bucket Integration** list, select your new S3 bucket.
6. In the **Select type of files** list, select the specific format for your JSON data.
7. Verify your **S3 Integration Summary**.
8. Continue with the rest of the [Procedure](#procedure).

To use an existing Amazon S3 bucket that you added to Capella AI Services:

1. In the **S3 Bucket Integration** list, select the S3 bucket where your structured data is stored.
2. In the **Select type of files** list, select the specific format for your JSON data.
3. Verify your **S3 Integration Summary**.
4. Continue with the rest of the [Procedure](#procedure).

### [](#configure-data)Configure Your Source Fields

You must configure whether the Vectorization Service should store all vectors generated from your documents in a single field, or create a custom source field mapping.

* Map all source fields to a single vector field
* Create custom source field mappings

To map all of the fields in your documents to a single vector field:

1. Click **Map all source fields to a single vector field**.
2. (Optional) Under **Vector Field**, enter a name for the field where you want to store your vectors.
3. Continue with the rest of the [Procedure](#procedure).

To create custom mappings and only vectorize specific fields from your documents:

1. Click **Create custom source field mappings**.
2. Under **Source Fields**, click the list.
3. Select every field from your source documents that you want to vectorize and store in a single field.
4. In the corresponding field under **Vector Field**, enter a name for the new vector field for your selected source field or fields.
5. (Optional) To map additional fields to another vector field, click **Add more mapping** and repeat Steps 2-4.
6. Continue with the rest of the [Procedure](#procedure).

### [](#choose-embedding)Choose Your Embedding Model

You can choose to use an embedding model [hosted by the Capella Model Service](../model-service/deploy-embed-model.md) or hosted by OpenAI to vectorize your data.

* Use a Capella Model
* Use an OpenAI Model

To use a Capella Model:

1. Click **Capella Model**.
2. Select the name of the model you want to use in this workflow.
3. Upload or manually enter your embedding model’s **API Key ID** and **API Key Token**. For more information about API keys for Capella models, see [Get Started with AI Services APIs](../../api-guide/api-start.md).
4. (Optional) Choose whether to set up **Private Networking** for your Capella embedding model. For more information about Private Networking for AI Services, see [Add an AWS PrivateLink Connection](../../security/add-aws-privatelink.md).
5. Click **Next**.
6. Continue with the rest of the [Procedure](#procedure).

To use an OpenAI model:

1. Click **External Model**.
2. In the **Choose OpenAI Model** list, select the specific OpenAI model you want to use in this workflow.
3. (Optional) To use a new OpenAI API key, click **Add New OpenAI API Key**.

  1. Enter a name to identify your API Key in Capella.
  2. Enter your **Secret Access Key** from OpenAI.
  3. Click **Add Key**.
4. In the **Integrations Name** list, select the OpenAI API Key you want to use.
5. Click **Next**.
6. Continue with the rest of the [Procedure](#procedure).  
> [!NOTE]  
> Workflows do not use the OpenAI Batch API.

## [](#next-steps)Next Steps

The Capella AI Services UI shows the documents that have been processed by your Structured Data Workflow. You can click the **Failed** icon to view error information for failed documents.

Structured Data Workflows display with an **S3 - Structured** Type.

For more information about Workflow statuses, see [Workflow Statuses](data-processing.md#status).

You can also:

* [Deploy an Embedding Model](../model-service/deploy-embed-model.md)
* [Deploy a Large Language Model (LLM)](../model-service/deploy-llm-model.md)
* [Integrate an Agent with the Agent Catalog](../integrate-agent-with-catalog.md)
* [Process and Vectorize Unstructured Data](vectorize-unstructured-data.md)
* [Troubleshoot a Workflow](troubleshoot-vectorization.md)