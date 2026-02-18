---
title: Manage AI Integration Settings
description: Use the Capella UI to manage settings for your integrations between
  an operational database, Capella AI Services, and OpenAI or Amazon S3.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/admin/pages/manage-ai-integrations.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/ai/admin/manage-ai-integrations.html)

# Manage AI Integration Settings

> Use the Capella UI to manage settings for your integrations between an operational database, Capella AI Services, and OpenAI or Amazon S3\. 

* Use **Amazon S3** to load data into Capella.
* Use **OpenAI** as a foundation model for your AI applications. Add Retrieval-Augmented Generation (RAG) to your applications through your Capella operational database and get more accurate responses.

Other integrations are available. Use the available filters or search for a supported Capella AI Services integration, to explore the full AI ecosystem available in Capella.

You can directly manage your OpenAI API keys or Amazon S3 bucket credentials from the **AI Services > Integrations** page. The **Integrations** page lets you see available integrations, and your current API keys or credentials. You can [edit your API keys or credentials](#edit-integration) or [delete them](#delete-integration) from your organization. Reuse your credentials across workflows to save time during workflow configuration.

You can add multiple OpenAI API keys or Amazon S3 bucket connections to Capella at once. For more information about how to add a new OpenAI model or Amazon S3 bucket connection to Capella, see [Vectorize Structured Data from Amazon S3](../build/vectorization-service/vectorize-structured-data-s3.md) or [Process and Vectorize Unstructured Data](../build/vectorization-service/vectorize-unstructured-data.md).

## [](#prerequisites)Prerequisites

* You have an OpenAI API key or credentials for an Amazon S3 bucket.
* You have logged in to the Couchbase Capella UI.

## [](#edit-integration)Edit an OpenAI API Key or Amazon S3 Credentials

To edit an API Key or credentials in your organization or cluster:

1. From your organization, go to **AI Services** **Integrations**.
2. Search for what you want to edit:

  * **Amazon S3** credentials
  * **OpenAI** API keys
3. Click **Manage Credentials**.
4. Next to the API key or credentials you want to edit, under **Actions**, click **Edit**.
5. Update the API key or Amazon S3 credentials
6. Click **Save API Key** or **Save Credentials**.

## [](#delete-integration)Delete an OpenAI API Key or Amazon S3 Credentials

To delete an API key or Amazon S3 credentials from your organization:

1. From your organization, go to **AI Services** **Integrations**.
2. Search for what you want to edit:

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