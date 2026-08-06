---
title: Process and Vectorize Unstructured Data
description: Use an Couchbase AI Data Plane Unstructured Data Workflow to
  automatically preprocess data for a Retrieval Augmented Generation (RAG)
  application or other use cases inside Capella.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/build/pages/vectorization-service/vectorize-unstructured-data.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:ai:build:vectorization-service/vectorize-unstructured-data.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/build/vectorization-service/vectorize-unstructured-data.html)

# Process and Vectorize Unstructured Data

> Use an Couchbase AI Data Plane Unstructured Data Workflow to automatically preprocess data for a Retrieval Augmented Generation (RAG) application or other use cases inside Capella. Convert your data into JSON from PDFs, JPGs, PNGs, and DOCX files and generate vector embeddings, all in one Workflow. 

> [!IMPORTANT]
> The Couchbase AI Data Plane can convert only JPG and PNG images of text to JSON data. Images that do not contain text cannot be converted by a Workflow. Make sure image files do not exceed the [maximum image file size](data-processing.md#limitations).

Workflows use your choice of embedding model to generate JSON data and vector embeddings, along with a [Vector Search index](../../../cloud/vector-search/vector-search.md), based on data stored in an Amazon S3 bucket. To generate your embeddings, you can use a model [hosted by the AI Data Plane Model Service](../model-service/deploy-embed-model.md), [OpenAI](https://openai.com/), or [Amazon Bedrock](https://aws.amazon.com/bedrock/). The AI Data Plane stores the generated JSON data, vector embeddings, and Vector Search index in an operational cluster.

To process your data effectively, you must choose a chunking strategy for your text. For more information, see [Chunking](data-processing.md#chunking).

> [!NOTE]
> If you make any changes to the data inside your Amazon S3 bucket, such as adding or removing files, you must manually trigger the Unstructured Data Workflow again to process these changes.

## [](#prerequisites)Prerequisites

* You have an Amazon S3 bucket that contains data in 1 of the following formats: PDF, JPG, PNG, DOCX
* Your Amazon S3 bucket does not have more than 10,000 files or files larger than 100 MB.
* You have read-only credentials for your Amazon S3 bucket. For more information about AWS access keys, see [the AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id%5Fcredentials%5Faccess-keys.html).
* If you want to use a model hosted on the AI Data Plane, you must have:

  * Deployed an AI Data Plane embedding model. For more information, see [Deploy an Embedding Model](../model-service/deploy-embed-model.md).
  * Your model's **API Key ID** and **API Key Token**. For more information about API keys for AI Data Plane models, see [Get Started with the Couchbase AI Data Plane APIs](../../api-guide/api-start.md).
* If you want to use a model hosted by OpenAI, you have your OpenAI API Key. For more information about how to find your OpenAI API Key, see [the OpenAI Help Center](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key).
* If you want to use an Amazon Bedrock model, you need a short-term Amazon Bedrock API key. For more information, see [Add an Amazon Bedrock API Key](../../admin/manage-ai-integrations.md#add-bedrock).
* You know the chunking strategy you want to use to process your data. For more information, see [Chunking](data-processing.md#chunking).
* You have created an operational cluster in Capella that has the following:

  * Couchbase Server version 8.0 or later.
  * The Search Service and Eventing Service running on at least 1 Service Group. For more information, see [Services and Service Groups](../../../cloud/clusters/databases.md#couchbase-services).
  * A bucket that can store your Vector Search index and any generated vector embeddings.  
  Use any bucket settings you would prefer for your particular use case. For more information, see [Manage Buckets](../../../cloud/clusters/data-service/manage-buckets.md).

## [](#procedure)Procedure

To create a new Unstructured Data Workflow and process unstructured data in the AI Data Plane:

1. Go to **AI Data Plane** **Workflows**.
2. Click **Create New Workflow**.
3. Click **Unstructured Data from External sources**.
4. In the **Workflow Name** field, enter a name to identify your Unstructured Data Workflow, or accept the automatically generated name.  
Workflow names can be a maximum of 128 characters and can include letters (A-Z, a-z), numbers (0-9), dashes (-), and underscores (\_).
5. Click **Start Workflow**.
6. [Configure Your Amazon S3 Bucket](#configure-s3).
7. Choose whether to **Create HyperScale Vector Index (now)** or **Create HyperScale Vector Index (later)**.
8. Under **Destination Cluster**, in the **Destination Operational Cluster** list, select the cluster you configured in the [Prerequisites](#prerequisites).
9. Set the **Destination Bucket**, **Destination Scope**, and **Destination Collection** for your vector embeddings.
10. [Configure Your Data Preprocessing Settings](#configure-preprocess).
11. [Choose Your Embedding Model](#choose-embedding).
12. Verify your workflow configuration.
13. Click **Run Workflow**.

> [!CAUTION]
> Do not delete or modify the metadata scope, collections, or Eventing functions created by your new Workflow. If you modify or delete the metadata or functions, you must delete your Workflow and create a new one.

### [](#configure-s3)Configure Your Amazon S3 Bucket

Choose whether to use a new Amazon S3 bucket or choose an S3 bucket that you have already saved as an integration with the Couchbase AI Data Plane.

> [!TIP]
> You can manage your saved Amazon S3 bucket credentials from the [Integrations page](../../admin/manage-ai-integrations.md).

* New Amazon S3 Bucket
* Use Existing Amazon S3 Bucket

To configure a new Amazon S3 bucket:

1. Click **Add New S3 Bucket Integration**.
2. In the **Integration Name** field, enter a name to use to identify your credentials and make it easier to manage them from the [Integrations page](../../admin/manage-ai-integrations.md).
3. Enter the details and credentials for accessing your Amazon S3 bucket.  
It's recommended to use read-only credentials for your S3 bucket. Make sure you have your **Access Key ID** and its **Secret Access Key**.  
> [!TIP]  
> You can also choose to use temporary credentials, supported by a session token. For more information about configuring temporary credentials and session tokens, see [the AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id%5Fcredentials%5Ftemp%5Fuse-resources.html).
4. Click **Add Credentials**.
5. In the **S3 Bucket Integration** list, select your new S3 bucket.
6. Verify your **S3 Integration Summary**.
7. Continue with the rest of the [Procedure](#procedure).

To use an existing Amazon S3 bucket that you added to the AI Data Plane:

1. In the **S3 Bucket Integration** list, select the S3 bucket where your unstructured data is stored.
2. Verify your **S3 Integration Summary**.
3. Continue with the rest of the [Procedure](#procedure).

### [](#configure-preprocess)Configure Your Data Preprocessing Settings

Choose the specific settings for processing your unstructured data:

1. (Optional) To set a specific inclusive range of document pages to process in your Workflow, turn on **Include Page Range**.

  1. Using the **Start Page** and **End Page** fields, configure your inclusive page range.  
  The page range must be valid for all documents stored in your S3 bucket.
2. (Optional) In the **Layout Exclusions** list, select the specific page layout elements that you want to exclude from vectorization.  
For example, you could choose to exclude anything identified as a **Header** or **Footer** element from your workflow.
3. (Optional) If your documents include PNGs, JPGs, or PDFs, turn on **Enable OCR** to extract the text from these files.
4. Choose the chunking strategy, maximum chunk size, and chunk overlap for vectorizing your data.  
For more information about chunking strategies, see [Chunking](data-processing.md#chunking).
5. Click **Next**.
6. Continue with the rest of the [Procedure](#procedure).

### [](#choose-embedding)Choose Your Embedding Model

You can choose to use an embedding model [hosted by the AI Data Plane Model Service](../model-service/deploy-embed-model.md), hosted by OpenAI, or hosted by Amazon Bedrock to vectorize your data.

* Use an AI Data Plane Model
* Use an OpenAI Model
* Use an AWS Bedrock Model

To use an AI Data Plane Model:

1. Click **Capella Model**.
2. Select the name of the model you want to use in this workflow.
3. Upload or manually enter your embedding model's **API Key ID** and **API Key Token**. For more information about API keys for AI Data Plane models, see [Get Started with the Couchbase AI Data Plane APIs](../../api-guide/api-start.md).
4. (Optional) Choose whether to set up **Private Networking** for your AI Data Plane embedding model. For more information about Private Networking for the AI Data Plane, see [Add an AWS PrivateLink Connection](../../security/add-aws-privatelink.md).
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

Before you begin, generate a short-term Amazon Bedrock API key and add it to the Couchbase AI Data Plane integrations. For more information, see [Add an Amazon Bedrock API Key](../../admin/manage-ai-integrations.md#add-bedrock).

To use an AWS Bedrock model:

1. Click **AWS Bedrock Model**.
2. Add your **Bedrock Model ID**.  
Use a Bedrock embedding model ID, for example `amazon.titan-embed-text-v2:0`.
3. In the **Integrations Name** list, select the Bedrock API key you want to use.
4. Click **Next**.
5. Continue with the rest of the [Procedure](#procedure).

## [](#next-steps)Next Steps

The AI Data Plane UI shows the documents that have been processed by your Unstructured Data Workflow. You can click the **Failed** icon to view error information for failed documents.

Unstructured Data Workflows display with an **S3 - Unstructured** Type.

For more information about Workflow statuses, see [Workflow Statuses](data-processing.md#status).

You can also:

* [Deploy an Embedding Model](../model-service/deploy-embed-model.md)
* [Deploy a Large Language Model (LLM)](../model-service/deploy-llm-model.md)
* [Integrate an Agent with the Agent Catalog](../integrate-agent-with-catalog.md)
* [Vectorize Structured Data from Capella](vectorize-structured-data-capella.md)
* [Vectorize Structured Data from Amazon S3](vectorize-structured-data-s3.md)
* [Troubleshoot a Workflow](troubleshoot-vectorization.md)