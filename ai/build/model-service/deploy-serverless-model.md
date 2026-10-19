---
title: Deploy Serverless LLMs and Embedding Models
description: Deploy Large Language Models (LLMs) and embedding models as
  serverless models that Capella serves from Amazon Bedrock and bills per token.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase AI Data Plane
    version: ""
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/build/pages/model-service/deploy-serverless-model.adoc
  xref: xref:ai:build:model-service/deploy-serverless-model.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/build/model-service/deploy-serverless-model.html)

# Deploy Serverless LLMs and Embedding Models

> Deploy Large Language Models (LLMs) and embedding models as serverless models that Capella serves from Amazon Bedrock and bills per token. 

A serverless model has no GPU compute for you to choose or manage. In each deployment request, you choose 1 region and up to 10 models, and Capella deploys each model separately. You can deploy LLMs and embedding models together in the same request.

To compare the capabilities of serverless and provisioned models, see [Compare Serving Modes](model-service.md#compare).

> [!NOTE]
> You cannot edit or turn off a serverless model after you deploy it. To change a model's configuration, such as its caching settings, [delete the model](#delete) and deploy it again.

## [](#prerequisites)Prerequisites

* Your user account has the [Organization Owner](../../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) role.
* If you want to deploy a serverless LLM that uses semantic caching, you must already have a healthy serverless embedding model in the same region where you're deploying your LLM. You cannot use a provisioned embedding model, or an embedding model that you're deploying at the same time as your LLM.

## [](#deploy)Deploy Serverless Models

1. From your organization, go to **AI Data Plane** **Models**.
2. Click **Deploy New Model**.
3. Under **Serving Mode**, choose **Serverless**.
4. In the **Region** list, choose the AWS region where you're deploying your model.  
The **Model Catalog** stays empty until you choose a region, because model availability and rates differ by region.  
> [!NOTE]  
> Deploying a model to a region for the first time can take between 5 and 10 minutes. Capella needs this time to deploy an AI gateway for your organization in that region. This is a one-time operation per region, so any models you deploy following the first are immediately available.
5. In the **Model Catalog** section, select up to 10 models.  
To see the full catalog, click **View All Models**. In the **All Models** panel, you can filter by **Model Provider** and **Type**, or search by model name.  
A model is unavailable if the chosen region does not offer it, or if you already deployed it in that region. If you change the region after choosing your models, Capella removes any selected models that the new region does not offer.  
After selecting models in the **All Models** panel, click **Use Selected Models**.
6. (Optional for LLMs) In the **Value Adds** section, you can enable caching for your chosen LLMs.  
The caching configuration you choose applies to every LLM in this deployment request.

  1. Choose a caching type:

    * [Standard Caching](configure-value-adds.md#standard-cache)
    * [Semantic Caching](configure-value-adds.md#semantic-cache)
    * [Standard and Semantic Caching](configure-value-adds.md#both-cache)
  2. (Optional) Select [Conversational Caching](configure-value-adds.md#conv-cache).
  3. If you chose semantic caching, choose the **Embedding Model** to use.  
  Only serverless embedding models that are healthy in your chosen region are available.
  4. (Optional) Expand the advanced options to set **Cache Expiry (TTL in seconds)**. If you're using semantic caching, you can also set **Score Threshold**, **Vector Dimensions**, and **Vector Similarity**.  
For more information about caching options, see [Caching](configure-value-adds.md#caching).
7. Review the **Summary** and **Estimated Costs**.

**Estimated Costs** shows the input and output rates for your selected models, in Capella credits per 1 million tokens. Rates vary by model and region. To see the rates for each model, click **See individual model costs**.  
For more information about billing, see [Serverless Model Billing](../../../cloud/billing/billing.md#model-service-serverless).
8. Click **Deploy Model**.  
Each model in your request deploys independently and starts with a `Pending` status. A model's status changes to `Deploying`, and then to `Healthy` when it's ready to use.

## [](#view)View Your Serverless Models

The **Serverless** tab on the **Models** page lists your serverless models with the following columns:

* **Model**
* **Region**
* **Status**
* **Created**
* **Requests & Tokens**, which shows request and token counts for the model for the current billing cycle.

To see further details about a model, expand its row. These details include **API Keys**, **Value Adds**, **Model ID**, and **Model Endpoint** information.

## [](#access)Set Up Access to a Serverless Model

To call a serverless model, you need a Model Service API key for the model's region. The API key works for all models you deploy to that region.

If a healthy model has no API key, its **Requests & Tokens** column shows **Set Up Access**. Click **Set Up Access**, or open the actions menu on the model's row and click **Add API Key**. The **Generate API Key** panel opens with the model's region selected.

For more information about API keys, see [Generate Model Service API Keys](../../api-guide/api-start.md#generate-model-keys).

## [](#delete)Delete a Serverless Model

You cannot delete a model if:

* An AI Function uses the model.  
Remove the association from the AI Function first. For more information, see [Use Couchbase AI Data Plane AI Functions](../ai-functions.md).
* It's an embedding model that a serverless LLM uses for semantic caching.  
Delete the LLM first, then delete the embedding model. To find the LLMs that use the embedding model, look on the **Serverless** tab for LLMs in the same region whose **Value Adds** include semantic caching.

> [!NOTE]
> When you delete the last serverless or provisioned model in a region, and no AI Functions use that region's AI gateway, Capella removes the gateway. You cannot deploy a serverless model in that region until Capella finishes removing the gateway.

To delete a serverless model:

1. From your organization, go to **AI Data Plane** **Models**.
2. Click the **Serverless** tab.
3. On the row of the model you want to delete, open the actions menu and click **Delete**.  
The confirmation names the model and its region. If you deployed the same model in several regions, verify the region before you continue.
4. Enter `delete` and click **Delete Model**.

The model shows a `Destroying` status until Capella removes it.

## [](#next-steps)Next Steps

* [Generate Model Service API Keys](../../api-guide/api-start.md#generate-model-keys)
* [Use AI Functions with your serverless LLMs](../ai-functions.md)