---
title: Make an API Call with the Agent Memory API
description: How to make an API call with the Agent Memory API on a self-managed
  Agent Memory server.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase Agent Memory
    version: "1.0"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-agentmemory/edit/release/1.0/modules/api-guide/pages/self-managed/api-use.adoc
  xref: xref:1.0@agent-mem:api-guide:self-managed/api-use.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/agent-mem/1.0/api-guide/self-managed/api-use.html)

# Make an API Call with the Agent Memory API

> How to make an API call with the Agent Memory API on a self-managed Agent Memory server. 

This page is for self-managed Agent Memory.

Use the Agent Memory API to store and retrieve memory for your AI agents on your Agent Memory server.

## [](#prerequisites)Prerequisites

To make an API call with the Agent Memory API, you need:

* [The base URL of your Agent Memory server](api-intro.md#agent-memory-base-url).
* [An access token](api-intro.md#agent-memory-auth), if your Agent Memory server uses authentication.

## [](#make-an-api-call)Make an API Call

You can use a client such as [curl](https://curl.se) to make an API call with the Agent Memory API.

To make an API call with the Agent Memory API:

1. Use the hostname and port of your Agent Memory server as the base URL:  
```text  
http://<HOST>:<PORT>  
```
2. If your Agent Memory server uses authentication, pass the access token as a Bearer token using the HTTP `Authorization` header.
3. If the endpoint requires a request body, pass it in JSON format.

Alternatively, you can use a client such as [Insomnia](https://insomnia.rest) or [Postman](https://www.postman.com) to explore the details of the REST API. The Agent Memory API uses an [OpenAPI](https://swagger.io/resources/open-api) v3 specification. To download the Agent Memory API specification, go to the [Agent Memory API Reference](../../agent-memory-api-reference/rest-api.md) and click **Download**.

## [](#examples)Examples

The following examples show how to store memory with the Agent Memory API. Run them in order, because each example uses the user or session created in the previous one:

1. [Create a User](#create-user-example)
2. [Create a Session](#create-session-example)
3. [Add Memory Blocks](#add-memory-example)

If your Agent Memory server does not use authentication, remove the `Authorization` header from each example.

### [](#create-user-example)Create a User

The following [POST](../../agent-memory-api-reference/rest-api.md#tag/Users/operation/create%5Fuser%5Fusers%5Fpost) request creates a user. You choose the `user_id`, which must be unique.

* `$BASE_URL` is the base URL. This is the [hostname and port of your Agent Memory server](api-intro.md#agent-memory-base-url).
* `$TOKEN` is your [access token](api-intro.md#agent-memory-auth), used as the Bearer token.

HTTP Request

```sh
curl "$BASE_URL/users" \
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

### [](#create-session-example)Create a Session

The following [POST](../../agent-memory-api-reference/rest-api.md#tag/Sessions/operation/create%5Fsession%5Fusers<em>user%5Fid</em>sessions%5Fpost) request creates a session for the user. You choose the `session_id`, which must be unique for the user.

* `$BASE_URL` is the base URL. This is the [hostname and port of your Agent Memory server](api-intro.md#agent-memory-base-url).
* `$TOKEN` is your [access token](api-intro.md#agent-memory-auth), used as the Bearer token.

HTTP Request

```sh
curl "$BASE_URL/users/user_123/sessions" \
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

### [](#add-memory-example)Add Memory Blocks

The following [POST](../../agent-memory-api-reference/rest-api.md#tag/Memory/operation/add%5Fmemory%5Fusers<em>user%5Fid</em>sessions<em>session%5Fid</em>memory%5Fpost) request adds 2 facts to the session as memory blocks.

The request sets `async_processing` to `false`, so Agent Memory processes the memory blocks before it returns a response. You can then search the memory blocks immediately.

* `$BASE_URL` is the base URL. This is the [hostname and port of your Agent Memory server](api-intro.md#agent-memory-base-url).
* `$TOKEN` is your [access token](api-intro.md#agent-memory-auth), used as the Bearer token.

HTTP Request

```sh
curl "$BASE_URL/users/user_123/sessions/session_456/memory" \
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

* For more information about the Agent Memory API, see [Agent Memory API for Self-Managed Deployments](api-intro.md).
* For a full reference guide, see [Agent Memory API Reference](../../agent-memory-api-reference/rest-api.md).
* For an error reference, see [The Agent Memory API Errors](api-errors.md).