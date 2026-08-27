---
title: Manage AI Integration Settings
description: Use the Capella UI to manage settings for your integrations between
  an operational database, the Couchbase AI Data Plane, and Amazon Bedrock,
  OpenAI, or Amazon S3.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/admin/pages/manage-ai-integrations.adoc
  xref: xref:ai:admin:manage-ai-integrations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/admin/manage-ai-integrations.html)

# Manage AI Integration Settings

> Use the Capella UI to manage settings for your integrations between an operational database, the Couchbase AI Data Plane, and Amazon Bedrock, OpenAI, or Amazon S3\. 

* Use **Amazon S3** to load data into the AI Data Plane.
* Use **OpenAI** as a foundation model for your AI applications. Add Retrieval-Augmented Generation (RAG) to your applications through your operational database and get more accurate responses.
* Use **Amazon Bedrock** as an embedding model provider for [Vectorization Workflows](../build/vectorization-service/data-processing.md).

Other integrations are available. Use the available filters or search for a supported AI Data Plane integration, to explore the full AI ecosystem available in the AI Data Plane.

You can directly manage your Amazon Bedrock API keys, OpenAI API keys, or Amazon S3 bucket credentials from the **AI Data Plane > Integrations** page. The **Integrations** page lets you see available integrations, and your current API keys or credentials. You can [edit your API keys or credentials](#edit-integration) or [delete them](#delete-integration) from your organization. Reuse your credentials across workflows to save time during workflow configuration.

You can add multiple OpenAI API keys or Amazon S3 bucket connections to the AI Data Plane at once. For more information about how to add a new OpenAI model or Amazon S3 bucket connection to the AI Data Plane, see [Vectorize Structured Data from Amazon S3](../build/vectorization-service/vectorize-structured-data-s3.md) or [Process and Vectorize Unstructured Data](../build/vectorization-service/vectorize-unstructured-data.md).

## [](#prerequisites)Prerequisites

* You have a short-term Amazon Bedrock API key, an OpenAI API key, or credentials for an Amazon S3 bucket.
* You have logged in to the Capella UI.

## [](#add-bedrock)Add an Amazon Bedrock API Key for Vectorization Workflows

Use a short-term Amazon Bedrock API key to connect Vectorization Workflows to an Amazon Bedrock embedding model in your AWS account.

> [!NOTE]
> When using Amazon Bedrock as an embedding model provider for Vectorization Workflows, you must use a short-term API key from AWS. If your key does not start with `bedrock-api-key-`, it's not a valid short-term key.

### [](#set-up-iam-permissions)Set Up IAM Permissions

Before generating a Bedrock API key, make sure the IAM role you use to generate it has permission to invoke your embedding model. As a minimum requirement, the role needs the `bedrock:InvokeModel` action scoped to the specific foundation model ARN. For guidance on setting up IAM permissions for Amazon Bedrock, see [Identity-based policy examples for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/security%5Fiam%5Fid-based-policy-examples.html) in the AWS documentation.

### [](#generate-a-short-term-key)Generate a Short-Term Key

Short-term Bedrock API keys inherit the duration of the IAM session used to generate them, up to a maximum of 12 hours. To minimize Workflow interruptions, generate your key using the maximum 12-hour session duration. Keys that use shorter durations are also valid, but they have a greater risk of expiring in the middle of a Workflow run and causing interruptions.

For more information about how to generate a short-term Bedrock API key, see [Amazon Bedrock API keys](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html) in the AWS documentation.

### [](#add-your-key-to-the-ai-data-plane)Add Your Key to the AI Data Plane

To add your Amazon Bedrock API key to the Couchbase AI Data Plane:

1. From your organization, go to **AI Data Plane** **Integrations**.
2. Find **Amazon Bedrock** in the list of integrations and click **Add Credentials**.
3. Click **Add Credentials**.
4. Enter a name to identify your key in the AI Data Plane.
5. Select the AWS region where you generated your short-term key.
6. Enter your short-term Amazon Bedrock API key. The key must start with `bedrock-api-key-`.
7. Click **Add Credentials**.

### [](#key-expiry-and-renewal)Key Expiry and Renewal

Short-term Bedrock API keys expire when the IAM session expires, up to a maximum of 12 hours. When a key expires, Workflows using it stop generating embeddings and fail with error messages indicating an AWS authentication error.

An existing workflow that fails due to API key expiration cannot automatically use updated API keys. To resume vectorization, you must:

1. Delete the existing Workflow that failed due to API key expiration.
2. Create a new Workflow using the integration that contains the updated API key.

## [](#edit-integration)Edit an API Key or Credentials

To edit an API key or credentials in your organization:

1. From your organization, go to **AI Data Plane** **Integrations**.
2. Search for what you want to edit:

  * **Amazon Bedrock** API keys
  * **Amazon S3** credentials
  * **OpenAI** API keys
3. Click **Manage Credentials**.
4. Next to the API key or credentials you want to edit, under **Actions**, click **Edit**.
5. Update the API key or Amazon S3 credentials
6. Click **Save API Key** or **Save Credentials**.

## [](#delete-integration)Delete an API Key or Credentials

To delete an API key or credentials from your organization:

1. From your organization, go to **AI Data Plane** **Integrations**.
2. Search for what you want to delete:

  * **Amazon Bedrock** API keys
  * **Amazon S3** credentials
  * **OpenAI** API keys
3. Click **Manage Credentials**.
4. to the API key or credentials you want to delete, under **Actions**, click **Delete**.
5. To confirm the deletion, enter `delete`.
6. Click **Delete API Key** or **Delete Credentials**.

## [](#see-also)See Also

* [Vectorize Structured Data from Amazon S3](../build/vectorization-service/vectorize-structured-data-s3.md)
* [Process and Vectorize Unstructured Data](../build/vectorization-service/vectorize-unstructured-data.md)
* [Deploy an Embedding Model](../build/model-service/deploy-embed-model.md)
* [Deploy a Large Language Model (LLM)](../build/model-service/deploy-llm-model.md)
* [Integrate an Agent with the Agent Catalog](../build/integrate-agent-with-catalog.md)