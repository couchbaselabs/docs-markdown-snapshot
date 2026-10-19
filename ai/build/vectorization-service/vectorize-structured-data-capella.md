---
title: Vectorize Structured Data from Capella
description: Use a Data from Capella Workflow to automatically generate
  embedding vectors from JSON data in your Capella operational cluster. Use
  embedding vectors for similarity searches on your data.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase AI Data Plane
    version: ""
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/build/pages/vectorization-service/vectorize-structured-data-capella.adoc
  xref: xref:ai:build:vectorization-service/vectorize-structured-data-capella.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/build/vectorization-service/vectorize-structured-data-capella.html)

# Vectorize Structured Data from Capella

> Use a Data from Capella Workflow to automatically generate embedding vectors from JSON data in your Capella operational cluster. Use embedding vectors for similarity searches on your data. 

The Vectorization Service automatically creates a [Vector Search index](../../../cloud/vector-search/vector-search.md) for your embeddings - letting you get started right away with Vector Search. You can use Vector Search to support Retrieval Augmented Generation (RAG) in your applications, or for other vector similarity use cases.

Your data must already be extracted, filtered, and chunked in preparation for generating embeddings.

To generate your embeddings, you can use a model [hosted by the AI Data Plane Model Service](../model-service/deploy-embed-model.md), [OpenAI](https://openai.com/), or [Amazon Bedrock](https://aws.amazon.com/bedrock/). The AI Data Plane stores the generated vector embeddings and Vector Search index in an operational cluster.

## [](#prerequisites)Prerequisites

* You have data available in JSON format inside a Capella operational cluster. If your data is not yet in JSON format, see [Process and Vectorize Unstructured Data](vectorize-unstructured-data.md).
* If you want to use a model hosted on the AI Data Plane, you must have:

  * Deployed an AI Data Plane embedding model. For more information, see [Deploy a Provisioned Embedding Model](../model-service/deploy-embed-model.md).
  * Your model's **API Key ID** and **API Key Token**. For more information about API keys for AI Data Plane models, see [Get Started with the Couchbase AI Data Plane APIs](../../api-guide/api-start.md).
* If you want to use a model hosted by OpenAI, you have your OpenAI API Key. For more information about how to find your OpenAI API Key, see [the OpenAI Help Center](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key).
* If you want to use an Amazon Bedrock model, you need a short-term Amazon Bedrock API key. For more information, see [Add an Amazon Bedrock API Key](../../admin/manage-ai-integrations.md#add-bedrock).
* You have deployed an operational cluster that has the following:

  * Couchbase Server version 8.0 or later.
  * The Search Service and Eventing Service running on at least 1 Service Group. For more information, see [Services and Service Groups](../../../cloud/clusters/databases.md#couchbase-services).
  * A bucket that can store the Vector Search index and any generated vector embeddings.  
  Use any bucket settings you would prefer for your particular use case. For more information, see [Manage Buckets](../../../cloud/clusters/data-service/manage-buckets.md).

## [](#procedure)Procedure

To create a new Data from Capella workflow and process your JSON data from a Capella operational cluster:

1. Go to **AI Data Plane** **Workflows**.
2. Click **Create New Workflow**.
3. Click **Data from Capella**.
4. In the **Workflow Name** field, enter a name to identify your Data from Capella Workflow, or accept the automatically generated name.  
Workflow names can be a maximum of 128 characters and can include letters (A-Z, a-z), numbers (0-9), dashes (-), and underscores (\_).
5. Click **Setup Workflow**.
6. Under **Data Source**, in the **Cluster** list, select the operational cluster where your data is stored. Your cluster must meet the criteria in the [Prerequisites](#prerequisites) to appear in the list.
7. Use the **Bucket**, **Scope**, and **Collection** lists to set where your data is stored on your operational cluster.
8. [Configure Your Source Fields](#configure-data).
9. Choose whether to **Create HyperScale Vector Index (now)** or **Create HyperScale Vector Index (later)**.
10. [Choose Your Embedding Model](#choose-embedding).
11. Verify your workflow configuration.
12. Click **Run Workflow**.

> [!CAUTION]
> Do not delete or modify the metadata scope, collections, or Eventing functions created by your new Workflow. If you modify or delete the metadata or functions, you must delete your Workflow and create a new one.

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

You can choose to use an embedding model [hosted by the AI Data Plane Model Service](../model-service/deploy-embed-model.md), hosted by OpenAI, or hosted by Amazon Bedrock to vectorize your data.

* Use an AI Data Plane Model
* Use an OpenAI Model
* Use an AWS Bedrock Model

To use an AI Data Plane Model:

1. Select **Capella Model** as your model source.
2. Select the specific Capella embedding model you want to use in this workflow.
3. Upload or manually enter your embedding model's **API Key ID** and **API Key Token**. For more information about API keys for AI Data Plane models, see [Get Started with the Couchbase AI Data Plane APIs](../../api-guide/api-start.md).
4. (Optional) Choose whether to set up **Private Networking** for your AI Data Plane embedding model. For more information about Private Networking for the Couchbase AI Data Plane, see [Add an AWS PrivateLink Connection](../../security/add-aws-privatelink.md).
5. Click **Next**.
6. Continue with the rest of the [Procedure](#procedure).

To use an OpenAI model:

1. Select **OpenAI** as your model source.
2. Select the specific OpenAI model you want to use in this workflow.
3. (Optional) To use a new OpenAI API key, click **Add New OpenAI API Key**.

  1. Enter a name to identify your API Key in Capella.
  2. Enter your **Secret Access Key** from OpenAI.
  3. Click **Add Key**.
4. Select the OpenAI API Key you want to use.
5. Click **Next**.
6. Continue with the rest of the [Procedure](#procedure).  
> [!NOTE]  
> Workflows do not use the OpenAI Batch API.

Before you begin, generate a short-term Amazon Bedrock API key and add it to the Couchbase AI Data Plane integrations. For more information, see [Add an Amazon Bedrock API Key](../../admin/manage-ai-integrations.md#add-bedrock).

To use an AWS Bedrock model:

1. Select **AWS Bedrock** as your model source.
2. Select the **Bedrock Model** type you want to use in this workflow.
3. Select the model's **Dimensions**.
4. (Optional) To use a new Amazon Bedrock credential, click **Add New Bedrock Credentials**.

  1. Enter a name to identify your key in the AI Data Plane.
  2. Select the AWS region where you generated your short-term key.
  3. Enter your short-term Amazon Bedrock API key. The key must start with `bedrock-api-key-`.
  4. Click **Add Credentials**.
5. Select the Bedrock credential you want to use.
6. (Optional) Choose whether to set up private networking for your AWS Bedrock model. To enable private networking, your cluster and credential must be in the same region.  
> [!NOTE]  
> * You can change the **AWS Region** for an Amazon Bedrock credential only if it's not associated with an active workflow that has private networking enabled. For more information, see [Edit an API Key or Credential](../../admin/manage-ai-integrations.md#edit-integration).  
> * Workflows that use the same cluster reuse the same private endpoint automatically. Other clusters, even in the same region, need their own private endpoint.  
If you do not set up private networking, your data traverses the public Internet with TLS encryption. You cannot enable private networking after creating a workflow; you must delete the original workflow and recreate it with private networking enabled.  
Capella bills your account for AWS PrivateLink when you have private endpoints enabled. For more information, see [Private Endpoints Billing](../../../cloud/billing/billing.md#private-endpoints).
7. Click **Next**.
8. Continue with the rest of the [Procedure](#procedure).

## [](#next-steps)Next Steps

The AI Data Plane UI shows the documents that have been processed by your Data from Capella Workflow. You can click the **Failed** icon to view error information for failed documents.

Data from AI Data Plane Workflows for Capella data display with a **Capella** Type.

For more information about Workflow statuses, see [Workflow Statuses](data-processing.md#status).

You can also:

* [Deploy a Provisioned Embedding Model](../model-service/deploy-embed-model.md)
* [Deploy a Provisioned Large Language Model (LLM)](../model-service/deploy-llm-model.md)
* [Integrate an Agent with the Agent Catalog](../integrate-agent-with-catalog.md)
* [Process and Vectorize Unstructured Data](vectorize-unstructured-data.md)
* [Troubleshoot a Workflow](troubleshoot-vectorization.md)