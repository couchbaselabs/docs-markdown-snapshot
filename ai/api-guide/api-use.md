---
title: Make an API Call with Capella AI Services APIs
description: How to make an API call with the Couchbase AI Services APIs.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/api-guide/pages/api-use.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:ai:api-guide:api-use.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/api-guide/api-use.html)

# Make an API Call with Capella AI Services APIs

> How to make an API call with the Couchbase AI Services APIs. 

This page is for Capella AI Services. It covers the AI Services features in the Management API, and the Model Service API. For more information about the Management API for Capella Operational features, see [Make an API Call with the Capella Operational Management API](../../cloud/management-api-guide/management-api-use.md).

Capella AI Services has different APIs that you can use. You can:

1. [Make an API call with the Management API](#management-api-call) to manage **Provider** integrations, **Workflows**, AI **Models**, and **Model Service API Keys**.
2. [Make an API call with Model Service API](#model-api-call) to send inference requests to your embedding models or Large Language Models (LLMs) and receive outputs.

## [](#management-api-call)Make an API Call with the Management API

Use the Management API to manage your AI Services.

### [](#prerequisites)Prerequisites

* You have [created an API key](api-start.md#generate-keys).

  * The API key must have all the organization roles, project access, and project roles required to carry out the API call. In the [Management API reference](../../cloud/management-api-reference/index.md), each endpoint description lists the roles that are needed.
  * The API key is not expired.
  * You added your connection IP address to your API key's allowed IP addresses.
  * You saved the API key token when you created it.

### [](#make-an-api-call)Make an API Call

You can use a client such as [cURL](https://curl.se) or a native SDK call to make an API call with the Management API.

To make an API call:

1. Use the following base URL:  
```text  
https://cloudapi.cloud.couchbase.com  
```
2. Pass your API key as a Bearer token using the HTTP `Authorization` header.
3. If a request body is required, pass it in JSON format.

Alternatively, you can use a client such as [Insomnia](https://insomnia.rest) or [Postman](https://www.postman.com) to explore the details of the REST API, generate code samples, and so on. The Management API uses an [OpenAPI](https://swagger.io/resources/open-api) v3 specification. To download the Management API specification, go to the [Management API Reference](../../cloud/management-api-reference/index.md) and click **Download**.

### [](#examples)Examples

The following examples show different operations you can complete with the Management API:

* [List an API Key's Organizations](#list-org-example)
* [List Deployed Models in an Organization](#list-model-example)
* [Get a Model's Connection String](#get-model-string-example)
* [Create Model Service API Key for a Region](#create-model-key-example)

#### [](#list-org-example)List an API Key's Organizations

The following [GET](../../cloud/management-api-reference/index.md#tag/Organizations/operation/getOrganizationByID) request lists all of the organizations available to the provided API key.

* `$TOKEN` is the API key token.

HTTP Request

```sh
curl "https://cloudapi.cloud.couchbase.com/v4/organizations" \
   -H "Authorization: Bearer $TOKEN"
```

The response is a JSON object similar to the following. In this case, the provided API key is able to access a single organization.

HTTP Response

```json
{
  "data": [
    {
      "audit": {
        "createdAt": "2025-10-02T16:34:44.604521691Z",
        "createdBy": "<USER_ID",
        "modifiedAt": "2025-10-02T16:34:44.604521691Z",
        "modifiedBy": "<USER_ID>",
        "version": 1
      },
      "description": "",
      "id": "<ORGID>",
      "name": "My Organization",
      "preferences": {
        "sessionDuration": 7200
      }
    }
  ]
}
```

The response includes the organization ID. You can use the organization ID for any further API calls in which `{organization}` is a path parameter.

#### [](#list-model-example)List Deployed Models in an Organization

The following [GET](../../cloud/management-api-reference/index.md#tag/Models-%28AI-Services%29/operation/listModels) request lists all of the deployed models available to the provided API key within the specified organization.

* `$ORGID` is the organization ID.
* `$TOKEN` is the API key token.

HTTP Request

```sh
curl "https://cloudapi.cloud.couchbase.com/v4/organizations/$ORGID/aiServices/models
   -H "Authorization: Bearer $TOKEN"
```

The response is a JSON object similar to the following.

HTTP Response

```json
{
    "cursor": {
        "hrefs": {
            "first": "https://cloudapi.cloud.couchbase.com/v4/organizations/<ORGID>/aiServices/models?page=1&perPage=10",
            "last": "https://cloudapi.cloud.couchbase.com/v4/organizations/<ORGID>/aiServices/models?page=1&perPage=10",
            "next": "https://cloudapi.cloud.couchbase.com/v4/organizations/<ORGID>/aiServices/models?page=0&perPage=10",
            "previous": ""
        },
        "pages": {
            "last": 1,
            "next": 0,
            "page": 1,
            "perPage": 10,
            "previous": 0,
            "totalItems": 2
        }
    },
    "data": [
        {
            "model": {
                "actions": [
                    "pause",
                    "destroy",
                    "edit"
                ],
                "cloudConfig": {
                    "compute": {
                        "cpu": 4,
                        "gpuMemory": 48
                    },
                    "provider": "aws",
                    "region": "us-east-1"
                },
                "config": {
                    "catalogModelName": "mistralai/mistral-7b-instruct-v0.3",
                    "provider": "mistral",
                    "type": "text-generation"
                },
                "connectionString": "https://<MODEL_STRING_ID>.ai.couchbase.com",
                "id": "<MODELID",
                "name": "model-1",
                "status": "healthy"
            }
        },
        {
            "model": {
                "actions": [
                    "pause",
                    "destroy",
                    "edit"
                ],
                "cloudConfig": {
                    "compute": {
                        "cpu": 4,
                        "gpuMemory": 24
                    },
                    "provider": "aws",
                    "region": "us-east-1"
                },
                "config": {
                    "catalogModelName": "nvidia/llama-3.2-nv-embedqa-1b-v2",
                    "dimensions": 2048,
                    "provider": "nvidia",
                    "type": "embedding-generation"
                },
                "connectionString": "https://<MODEL_STRING_ID>.ai.couchbase.com",
                "id": "<MODELID>",
                "name": "model-2",
                "status": "healthy"
            }
        }
    ]
}
```

This response contains details about all the models, including their model type and respective `{connectionString}` URL.

#### [](#get-model-string-example)Get a Model's Connection String

The following [GET](../../cloud/management-api-reference/index.md#tag/Models-%28AI-Services%29/operation/getConnectionString) request retrieves details about a specific model's connection string. This connection string is the base URL required to use the Model Service API for this specific model.

* `$ORGID` is the organization ID.
* `$MODELID` is the model ID.
* `$TOKEN` is the API key token.

HTTP Request

```sh
curl "https://cloudapi.cloud.couchbase.com/v4/organizations/$ORGID/aiServices/models/$MODELID/connectionString" \
   -H "Authorization: Bearer $TOKEN"
```

The response is a JSON object similar to the following.

HTTP Response

```json
{
    "connectionString": "https://<MODEL_STRING_ID>.ai.couchbase.com"
}
```

#### [](#create-model-key-example)Create Model Service API Key for a Region

The following [POST](../../cloud/management-api-reference/index.md#tag/Model-Services-API-Keys-%28AI-Services%29/operation/createModelAPIKey) request creates a Model Service API Key for an AWS region within the specified organization. You need this Model Service API Key to access the Model Service API and use your AI model.

* `$ORGID` is the organization ID.
* `$TOKEN` is the API key token.

HTTP Request

```sh
curl "https://cloudapi.cloud.couchbase.com/v4/organizations/$ORGID/aiServices/models/apiKeys" \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json" \
   -d '{
    "name": "model-api-key",
  "description": "API key for LLM",
  "expiry": 180,
  "allowedCIDRs": ["<ALLOWED_IP>"],
  "region": "us-east-1"
  }'
```

The response is an JSON similar to the following.

HTTP Response

```text
{
    "id": "<API-KEY-ID>",
    "token": "<API-KEY-TOKEN>"
}
```

## [](#model-api-call)Make an API Call with the Model Service API

Use the Model Service API to provide inference requests to your hosted models.

### [](#prerequisites-2)Prerequisites

To make an API call with the Model Service API, you need:

* [A Model Service API key](#model-service-key).
* [The model connection string](#model-connection-string).

#### [](#model-service-key)Model Service API Key

A Model Service API key is only used for the Model Service API. Organizational API keys created for the Management API have different access and will not work for the Model Service API.

To use a Model Service API key to make a call to the Model Service API:

* Configure it with the same region as your AI model.
* Use a key that has not expired.
* Add the IP address you want to connect from to your API key's allowed IP addresses.
* Save the API key token when you create it, as it cannot be retrieved later.

To create an API key for the Model Service API, see [Generate Model Service API Keys](api-start.md#generate-model-keys).

#### [](#model-connection-string)Model Connection String

The Model Service API uses a model's **Model Endpoint** as its base URL. This is also known as the model connection string in the Management API. The model connection string is unique to every AI model you deploy.

To get your model connection string:

1. Go to **AI Services** **Models**.
2. Find your model and copy the **Model Endpoint**.

To get your model connection string using the Management API, see [Get a Model's Connection String](#get-model-string-example).

### [](#make-an-api-call-2)Make an API Call

You can use a client such as [cURL](https://curl.se) or a native SDK call to make an API call with the Model Service API.

To make an API call with the Model Service API and a specific model:

1. Use your model's connection string as the base URL:  
```text  
https://<MODEL_STRING_ID>.ai.couchbase.com  
```
2. Pass the Model Service API key as a Bearer token using the HTTP `Authorization` header.
3. If a request body is required, pass it in JSON format.

Alternatively, you can use a client such as [Insomnia](https://insomnia.rest) or [Postman](https://www.postman.com) to explore the details of the REST API, generate code samples, and so on. The Model Service API uses an [OpenAPI](https://swagger.io/resources/open-api) v3 specification. To download the Model Service API specification, go to the [Model Service API Reference](../model-service-api-reference/rest-api.md) and click **Download**.

### [](#examples-2)Examples

The following examples show different operations you can complete with the Model Service API:

* [Create Chat Conversation](#create-model-chat)

#### [](#create-model-chat)Create Chat Conversation

The following [POST](../model-service-api-reference/rest-api.md#tag/Chat/operation/createChatCompletion) request creates a model response for a given chat conversation with your specified LLM. To use your model, you need a Model Service API key in the same region as the model, along with its unique model connection string.

* `$MODEL_STRING` is the base URL. This is the [model connection string](#model-connection-string), also known as **Model Endpoint** in the Capella UI.
* `$TOKEN` is the Model Service API key token.

HTTP Request

```sh
curl "$MODEL_STRING/v1/chat/completions \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json" \
   -d '{
  "messages": [
    {
      "role": "user",
      "content": "What is Couchbase all about? Write a N1QL query to get top 250 documents in a sorted list of scope, inventory and collection, airlines"
    }
  ],
  "model": "meta-llama/Llama-3.1-8B-Instruct",
  "stream": false,
  "max_tokens": 100
}
```

The response is an JSON similar to the following.

HTTP Response

```text
{
    "id": "<CHATID>",
    "object": "chat.completion",
    "created": 1759451545,
    "model": "mistralai/mistral-7b-instruct-v0.3",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "Couchbase is a NoSQL document-oriented database that can be used for building fast and resilient applications, offering features like data durability, real-time insights, and flexible data modeling. It supports various programming languages and APIs, including N1QL (SQL-likequery language).\n\nIn your case, you want to retrieve the top 250 documents from a scope, inventory, and collection named \"airlines\" in a sorted order. Assuming you have"
            },
            "finish_reason": "length"
        }
    ],
    "usage": {
        "prompt_tokens": 38,
        "completion_tokens": 100,
        "total_tokens": 138
    }
}
```

## [](#next-steps)Next Steps

* For a full reference guide of the Management API, see [Management API Reference](../../cloud/management-api-reference/index.md).
* For a full reference guide of the Model Service API, see [Inference API Reference](../model-service-api-reference/rest-api.md).
* For a reference of the Management API errors, see [Management API Error Messages ](api-errors.md#management-api-errors).
* For a reference of the AI Services Model Service API errors, see [Model Service API Error Messages ](api-errors.md#model-api-errors).