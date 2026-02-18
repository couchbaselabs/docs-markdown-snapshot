---
title: Deploy an Embedding Model
description: Use the Capella Model Service to deploy embedding models for vectorizing text.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/build/pages/model-service/deploy-embed-model.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/ai/build/model-service/deploy-embed-model.html)

# Deploy an Embedding Model

> Use the Capella Model Service to deploy embedding models for vectorizing text. 

An embedding model vectorizes text into numerical vectors that capture their semantic meaning, allowing AI systems to identify similarities between content. You can use embedding models you deploy through the Capella Model Service with [Capella AI Services Workflows](../vectorization-service/data-processing.md).

## [](#prerequisites)Prerequisites

* To deploy a model, you must have the [Organization Owner](../../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) role.

## [](#procedure)Procedure

1. From your organization, go to **AI Services** **Models**.
2. Click **Deploy New Model**.
3. Choose an embedding model to deploy:

  1. Click **View All Models**.
  2. Click **Type:All** and deselect the **LLM, Text to Text** option, or use the search bar to find a specific embedding model.
  3. Click the model you want to deploy.
  4. Click **Use Selected Model**.
4. Enter a name for the embedding model that you’re deploying.
5. Choose the AWS region where you want to deploy the model.
6. Choose the compute and GPU size configuration to run the model.  
The minimum supported compute size available for the model in your chosen region is the default.
7. (Optional) Apply advanced configuration options:  
> [!CAUTION]  
> If you change or enable any advanced configurations, such as value adds or security features, after deployment, your existing Model Service API keys will stop working, and you must create a new API key. For more information, see [Value Adds and Security Features](../../api-guide/api-start.md#value-adds).  
Dimensions  
When available, you can configure your embedding model to generate vectors with more or fewer dimensions by adjusting the **Dimensions** setting.  
You cannot change this setting after you deploy the embedding model.  
For more information, see [Configure Embedding Model Performance](configure-embed-performance.md#dimensions).  
Async Processing  
Increase throughput by processing jobs asynchronously when system capacity becomes available. This allows tasks to be queued and handled as resources permit, improving overall efficiency.  
For more information, see [Configure Embedding Model Performance](configure-embed-performance.md#async-processing).
8. Click **Deploy Model**.

## [](#next-steps)Next Steps

The **Models** page opens with your model in a deploying state. Once the model has finished deploying, you can view the model details and manage the model by expanding its listing on the **Models** page.

To create API keys for your deployed model, see [Generate Model Service API Keys](../../api-guide/api-start.md#generate-model-keys).

You can also:

* [Process and Vectorize Unstructured Data](../vectorization-service/vectorize-unstructured-data.md)
* [Vectorize Structured Data from Capella](../vectorization-service/vectorize-structured-data-capella.md)
* [Vectorize Structured Data from Amazon S3](../vectorization-service/vectorize-structured-data-s3.md)
* [Deploy a Large Language Model (LLM)](deploy-llm-model.md)