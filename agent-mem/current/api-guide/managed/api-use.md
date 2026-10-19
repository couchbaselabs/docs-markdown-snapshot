---
title: Make an API Call with the Agent Memory APIs
description: How to make an API call with the Couchbase Capella APIs for Agent Memory.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase Agent Memory
    version: "1.1"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-agentmemory/edit/release/1.1/modules/api-guide/pages/managed/api-use.adoc
  xref: xref:agent-mem:api-guide:managed/api-use.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/agent-mem/current/api-guide/managed/api-use.html)

# Make an API Call with the Agent Memory APIs

> How to make an API call with the Couchbase Capella APIs for Agent Memory. 

This page is for Agent Memory in Capella. It covers the Agent Memory features in the Management API, and the Agent Memory API. For more information about the Management API for Capella Operational features, see [Make an API Call with the Capella Operational Management API](../../../../cloud/management-api-guide/management-api-use.md).

Agent Memory in Capella has different APIs that you can use. You can:

* [Make an API call with the Management API](#management-api-call) to manage **Agent Memory Servers** and **Agent Memory API Keys**.
* [Make an API call with the Agent Memory API](#agent-memory-api-call) to store and retrieve memory on your Agent Memory server.

## [](#management-api-call)Make an API Call with the Management API

Use the Management API to manage your Agent Memory servers and Agent Memory API keys.

### [](#prerequisites)Prerequisites

* You have [created an API key](#api-guide:api-start.adoc#generate-keys).

  * The API key must have all the organization roles, project access, and project roles required to carry out the API call. In the [Management API reference](../../../../cloud/management-api-reference/index.md), each endpoint description lists the roles that are needed.
  * The API key is not expired.
  * You added your connection IP address to your API key's allowed IP addresses.
  * You saved the API key token when you created it.

### [](#make-an-api-call)Make an API Call

You can use a client such as [cURL](https://curl.se) or a native SDK call to make an API call with the Management API.

To make an API call:

1. Use the following base URL:  
https://cloudapi.cloud.couchbase.com
2. Pass your API key as a Bearer token using the HTTP `Authorization` header.
3. If a request body is required, pass it in JSON format.

Alternatively, you can use a client such as [Insomnia](https://insomnia.rest) or [Postman](https://www.postman.com) to explore the details of the REST API, generate code samples, and so on. The Management API uses an [OpenAPI](https://swagger.io/resources/open-api) v3 specification. To download the Management API specification, go to the [Management API Reference](../../../../cloud/management-api-reference/index.md) and click **Download**.

### [](#examples)Examples

The following examples show different operations you can complete with the Management API:

* [Get an Agent Memory Server's Endpoint](#get-agent-memory-server-example)
* [Create an Agent Memory API Key](#create-agent-memory-key-example)

#### [](#get-agent-memory-server-example)Get an Agent Memory Server's Endpoint

The following [GET](../../../../cloud/management-api-reference/index.md#tag/AI-Agent-Memory-Servers/operation/getAgentMemoryServer) request gets the details of an Agent Memory server.

* `$ORG_ID` is the organization ID.
* `$PROJECT_ID` is the project ID.
* `$CLUSTER_ID` is the ID of the operational cluster that the Agent Memory server connects to.
* `$SERVER_ID` is the Agent Memory server ID.
* `$TOKEN` is the API key token.

HTTP Request

```sh
curl "https://cloudapi.cloud.couchbase.com/v4/organizations/$ORG_ID/projects/$PROJECT_ID/clusters/$CLUSTER_ID/aiServices/agentMemoryServers/$SERVER_ID" \
   -H "Authorization: Bearer $TOKEN"
```

The response is a JSON object similar to the following:

HTTP Response

```json
{
  "id": "<SERVER_ID>",
  "name": "support-bot-memory",
  "description": "Agent memory store for the support bot",
  "tenantId": "<ORG_ID>",
  "projectId": "<PROJECT_ID>",
  "clusterId": "<CLUSTER_ID>",
  "config": {
    "nodeConfig": {
      "instanceType": "small",
      "nodeCount": 3,
      "provider": "aws",
      "region": "us-east-1"
    },
    "bucket": "agent-memory",
    "memoryBlockTTL": 604800,
    "embedding": {
      "integrationId": "<INTEGRATION_ID>",
      "model": "text-embedding-3-small"
    },
    "llm": {
      "integrationId": "<INTEGRATION_ID>",
      "model": "gpt-4o-mini"
    },
    "semanticExtraction": {
      "enabled": true
    },
    "advancedConfig": {
      "summaryTokenLimit": 700,
      "processingBatchSize": 5,
      "maxRequestsPerMinute": 1500,
      "maxTokensPerMinute": 125000,
      "maxConcurrentTasks": 100,
      "perRequestTokenLimit": 4096,
      "idleSleepSeconds": 0.5,
      "queueMaxSize": 10000,
      "maxFailCount": 3,
      "taskTimeoutSeconds": 90
    }
  },
  "network": {
    "endpoint": "<AGENT_MEMORY_SERVER_ENDPOINT_STRING>"
  },
  "status": "healthy",
  "audit": {
    "createdBy": "<USER_ID>",
    "createdAt": "2026-07-15T10:30:00Z",
    "modifiedBy": "<USER_ID>",
    "modifiedAt": "2026-07-16T08:00:00Z",
    "version": 2
  }
}
```

The response includes the Agent Memory server's endpoint in the `network.endpoint` field. Use the endpoint as the base URL for the Agent Memory API.

#### [](#create-agent-memory-key-example)Create an Agent Memory API Key

The following [POST](../../../../cloud/management-api-reference/index.md#tag/AI-Agent-Memory-API-Keys/operation/createAgentMemoryApiKey) request creates an Agent Memory API key with read and write access, which expires after 30 days.

* `$ORG_ID` is the organization ID.
* `$PROJECT_ID` is the project ID.
* `$CLUSTER_ID` is the ID of the operational cluster that the Agent Memory server connects to.
* `$SERVER_ID` is the Agent Memory server ID.
* `$TOKEN` is the API key token.

HTTP Request

```sh
curl "https://cloudapi.cloud.couchbase.com/v4/organizations/$ORG_ID/projects/$PROJECT_ID/clusters/$CLUSTER_ID/aiServices/agentMemoryServers/$SERVER_ID/apiKeys" \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json" \
   -d '{
  "name": "my-agent-key",
  "description": "API key for my AI agent",
  "expiry": 30,
  "accessPolicy": {
    "roles": ["ams_rw"]
  }
}'
```

The response is a JSON object similar to the following:

HTTP Response

```json
{
  "id": "<API_KEY_ID>",
  "name": "my-agent-key",
  "description": "API key for my AI agent",
  "apiKeySecret": "<API_KEY_TOKEN>",
  "expiry": 30,
  "accessPolicy": {
    "roles": ["ams_rw"]
  }
}
```

The response includes the Agent Memory API key token in the `apiKeySecret` field.

> [!WARNING]
> The Management API returns the Agent Memory API key token only once, when you create the API key. Save the API key token in a secure location.

## [](#agent-memory-api-call)Make an API Call with the Agent Memory API

Use the Agent Memory API to store and retrieve memory on your Agent Memory server.

### [](#prerequisites-2)Prerequisites

To make an API call with the Agent Memory API, you have:

* [Created an Agent Memory API key](api-start.md#generate-agent-memory-keys).

  * The API key must have the access level required to carry out the API call. For more information, see [Access Levels](api-intro.md#access-level).
  * The API key is not expired.
  * You saved the API key token when you created it, as it cannot be retrieved later.
* Copied your Agent Memory server endpoint.
* Added the required IP addresses to the list of allowed IP addresses for your Agent Memory server. For more information, see [Add Allowed IP Addresses](api-start.md#add-agent-memory-ips).

### [](#make-an-api-call-2)Make an API Call

You can use a client such as [curl](https://curl.se) to make an API call with the Agent Memory API.

To make an API call with the Agent Memory API:

1. Use your Agent Memory server endpoint as the base URL:  
```text  
https://<HOST_ID>.svc.ai.cloud.couchbase.com/ams/<SERVER_ID>/  
```
2. Pass the Agent Memory API key token as a Bearer token using the HTTP `Authorization` header.
3. If the endpoint requires a request body, pass it in JSON format.

Alternatively, you can use a client such as [Insomnia](https://insomnia.rest) or [Postman](https://www.postman.com) to explore the details of the REST API. The Agent Memory API uses an [OpenAPI](https://swagger.io/resources/open-api) v3 specification. To download the Agent Memory API specification, go to the [Agent Memory API Reference](../../agent-memory-api-reference/rest-api.md) and click **Download**.

### [](#examples-2)Examples

The following examples show how to store memory with the Agent Memory API. Run them in order, because each example uses the user or session created in the previous one:

1. [Create a User](#create-user-example)
2. [Create a Session](#create-session-example)
3. [Add Memory Blocks](#add-memory-example)

> [!NOTE]
> The API key for these examples needs the Write (`ams_rw`) or Admin (`ams_admin`) access level.

#### [](#create-user-example)Create a User

The following [POST](../../agent-memory-api-reference/rest-api.md#tag/Users/operation/create%5Fuser%5Fusers%5Fpost) request creates a user. You choose the `user_id`, which must be unique.

* `$ENDPOINT_STRING` is the base URL. This is the [Agent Memory server endpoint](api-start.md#agent-memory-endpoint).
* `$TOKEN` is your [Agent Memory API key](api-start.md#agent-memory-keys) token, used as the Bearer token.

HTTP Request

```sh
curl "$ENDPOINT_STRING/users" \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json" \
   -d '{
  "user_id": "user_123",
  "name": "John Doe"
}'
```

The response is a JSON object similar to the following:

HTTP Response

```json
{
  "id": "user_123",
  "name": "John Doe",
  "sessions": [],
  "metadata": {}
}
```

The response includes the user ID. You can use the user ID for any further API calls in which `{USER_ID}` is a path parameter.

#### [](#create-session-example)Create a Session

The following [POST](../../agent-memory-api-reference/rest-api.md#tag/Sessions/operation/create%5Fsession%5Fusers<em>user%5Fid</em>sessions%5Fpost) request creates a session for the user. You choose the `session_id`, which must be unique for the user.

* `$ENDPOINT_STRING` is the base URL. This is the [Agent Memory server endpoint](api-start.md#agent-memory-endpoint).
* `$TOKEN` is your [Agent Memory API key](api-start.md#agent-memory-keys) token, used as the Bearer token.

HTTP Request

```sh
curl "$ENDPOINT_STRING/users/user_123/sessions" \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json" \
   -d '{
  "session_id": "session_456"
}'
```

The response is a JSON object similar to the following:

HTTP Response

```json
{
  "user_id": "user_123",
  "session_id": "session_456",
  "start_time": "2026-09-24 14:30:00.123456",
  "end_time": null,
  "annotations": {},
  "metadata": {},
  "blocks_ttl": null
}
```

The response includes the session ID. You can use the session ID for any further API calls in which `{SESSION_ID}` is a path parameter.

#### [](#add-memory-example)Add Memory Blocks

The following [POST](../../agent-memory-api-reference/rest-api.md#tag/Memory/operation/add%5Fmemory%5Fusers<em>user%5Fid</em>sessions<em>session%5Fid</em>memory%5Fpost) request adds 2 facts to the session as memory blocks.

The request sets `async_processing` to `false`, so Agent Memory processes the memory blocks before it returns a response. You can then search the memory blocks.

* `$ENDPOINT_STRING` is the base URL. This is the [Agent Memory server endpoint](api-start.md#agent-memory-endpoint).
* `$TOKEN` is your [Agent Memory API key](api-start.md#agent-memory-keys) token, used as the Bearer token.

HTTP Request

```sh
curl "$ENDPOINT_STRING/users/user_123/sessions/session_456/memory" \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json" \
   -d '{
  "facts": [
    "User prefers email notifications",
    "User is allergic to peanuts"
  ],
  "async_processing": false
}'
```

The response is a JSON object similar to the following:

HTTP Response

```json
{
  "message": "Successfully added 2 memory block(s).",
  "accepted_count": 2,
  "block_ids": [
    "<BLOCK_ID_1>",
    "<BLOCK_ID_2>"
  ],
  "rejected_count": 0,
  "rejected_details": null
}
```

The response includes the ID of each memory block that Agent Memory added.

## [](#next-steps)Next Steps

* For more information about the Agent Memory APIs, see [Agent Memory APIs for Managed Deployments](api-intro.md).
* For a full reference guide of the Management API, see [Couchbase Capella Management API Reference](../../../../cloud/management-api-reference/index.md).
* For a full reference guide of the Agent Memory API, see [Agent Memory API Reference](../../agent-memory-api-reference/rest-api.md).
* For a reference of the Management API and Agent Memory API errors, see [The Agent Memory API Errors](api-errors.md).