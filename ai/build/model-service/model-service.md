---
title: Deploy Models with the AI Data Plane Model Service
description: Deploy Large Language Models (LLMs) and embedding models in
  Capella, either as serverless models or as provisioned models.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase AI Data Plane
    version: ""
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/build/pages/model-service/model-service.adoc
  xref: xref:ai:build:model-service/model-service.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/build/model-service/model-service.html)

# Deploy Models with the AI Data Plane Model Service

> Deploy Large Language Models (LLMs) and embedding models in Capella, either as serverless models or as provisioned models. 

Use the AI Data Plane Model Service to deploy Large Language Models (LLMs) and embedding models for your AI applications. The following serving modes are available:

[Serverless](#serverless)

Capella serves the model from Amazon Bedrock and bills you for the tokens you use. You have no compute to choose or manage.

[Provisioned](#provisioned)

Capella runs the model with NVIDIA NIM on dedicated GPUs and bills you by the hour for the compute you choose.

You choose the serving mode when you deploy a model, and you can use both serving modes in the same organization.

For information about how Couchbase bills you for each serving mode, see [Model Service Billing](../../../cloud/billing/billing.md#model-service).

## [](#compare)Compare Serving Modes

The following table shows the primary differences between serverless and provisioned models:

|                                                          | Serverless                                                                                                                                  | Provisioned                                                                                      |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Infrastructure                                           | Amazon Bedrock, through an AI gateway that Capella deploys for your organization in each region you use.                                    | NVIDIA NIM on dedicated GPU compute.                                                             |
| Billing                                                  | Per input and output token, in Capella credits.                                                                                             | By the clock hour, based on the compute size and whether the model is on.                        |
| Regions                                                  | A subset of AWS regions that the Model Service supports.                                                                                    | All AWS regions that the Model Service supports.                                                 |
| Deployment options                                       | Choose a region and, for LLMs, optional caching. You cannot name a serverless deployment. Capella identifies it by its model ID and region. | Choose a name, compute and GPU size, and options such as quantization and optimization profiles. |
| Deployments of the same model                            | 1 per region in an organization.                                                                                                            | Multiple, each with its own name.                                                                |
| Value adds                                               | Caching (LLMs)                                                                                                                              | Caching (LLMs), async processing, and keyword filtering.                                         |
| Guardrails and jailbreak detection                       | Not available.                                                                                                                              | Available for LLMs.                                                                              |
| Changes after deployment                                 | Not available. To change a deployment, such as its caching settings, delete the model and deploy it again.                                  | Available.                                                                                       |
| Private networking                                       | Not available.                                                                                                                              | Available through AWS PrivateLink.                                                               |
| [Workflows](../vectorization-service/data-processing.md) | Not available.                                                                                                                              | Available.                                                                                       |
| [AI Functions](../ai-functions.md)                       | Available for LLMs.                                                                                                                         | Available for LLMs.                                                                              |

## [](#serverless)Serverless Models

Capella serves serverless models from Amazon Bedrock and bills you per token. To deploy a serverless model, see [Deploy Serverless LLMs and Embedding Models](deploy-serverless-model.md).

### [](#serverless-when-to-use)When to Use Serverless Models

Common use cases for serverless models include:

Exploring and prototyping with several models

Try several models at once without sizing or paying for idle compute. You can choose up to 10 models each time you deploy.

Applications with variable or unpredictable traffic

You pay for the tokens you use, so a model with little traffic can have lower costs.

Applications that need models from a wide range of providers

The serverless catalog includes LLMs and embedding models from providers such as Anthropic, Meta, Mistral AI, and Amazon.

Teams that want a simpler deployment

You choose only the model and a region. Capella manages the infrastructure, so you have no compute, GPU size, or performance settings to configure.

## [](#provisioned)Provisioned Models

Capella runs provisioned models with NVIDIA NIM on dedicated GPUs and bills you by the hour. To deploy a provisioned model, see [Deploy a Provisioned Large Language Model (LLM)](deploy-llm-model.md) or [Deploy a Provisioned Embedding Model](deploy-embed-model.md).

### [](#provisioned-when-to-use)When to Use Provisioned Models

Common use cases for provisioned models include:

Workloads that need dedicated capacity and consistent latency

Your model runs on GPUs that only your organization uses.

Applications that need content safety controls

Guardrails and jailbreak detection are available only on provisioned LLMs.

Applications that need private network access

You can connect to a provisioned model through AWS PrivateLink.

Vectorizing data with Workflows

Workflows can use only provisioned embedding models.

## [](#see-also)See Also

* [Deploy Serverless LLMs and Embedding Models](deploy-serverless-model.md)
* [Deploy a Provisioned Large Language Model (LLM)](deploy-llm-model.md)
* [Deploy a Provisioned Embedding Model](deploy-embed-model.md)
* [Configure LLM Value Adds](configure-value-adds.md)