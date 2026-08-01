---
title: Agent Memory API Reference
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/agent-memory-api-reference/pages/rest-api.adoc
pubDate: 2026-08-01T05:32:35.777Z
link: xref:ai:agent-memory-api-reference:rest-api.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/agent-memory-api-reference/rest-api.html)

# Agent Memory API Reference

* Core concepts
* Semantic extraction
* Authentication
* Request and response format
* Rate limiting and ingestion
* Memory Management
  * Users
    * getList Users
    * postCreate User
    * postSearch Users
    * putUpdate User
    * delDelete User
    * putUpdate Memory Block TTL
    * getList User Sessions
  * Sessions
    * postCreate Session
    * getGet Session
    * putUpdate Session
    * delDelete Session
    * postEnd Session
  * Memory
    * postAdd Memory Blocks
    * delDelete Memory Blocks
    * putUpdate Memory Block
    * postSearch Memory
    * getList Memory Blocks
* Observability
  * Health
    * getCheck Server Health
    * getCheck Database Health
    * getCheck Model Service Health
    * getCheck Extraction Queue Health
    * getGet Extraction Queue Statistics
    * getCheck Memory Pressure Status
  * Metrics
    * getScrape Prometheus Metrics
* Operations
  * Logs
    * getDownload Diagnostic Logs

[API docs by Redocly](https://redocly.com/redoc/)

# AgentMemory API (1.0.0)

Download OpenAPI specification:

AgentMemory is a persistent, semantic memory service for AI agents. It stores conversation history, extracted facts, and vector embeddings, enabling agents to recall relevant past context across sessions and conversations.

## [](#section/Core-concepts)Core concepts

AgentMemory organizes data in a three-level hierarchy:

* **User** — a persistent identity (human end-user, agent instance, or service account) that owns one or more sessions. A user must exist before sessions or memory can be created.
* **Session** — a scoped conversation context owned by a user. The session is the default boundary for semantic search — results are drawn from the current session unless the request explicitly expands scope. Sessions can be ended to prevent further writes.
* **Memory block** — the atomic unit of stored knowledge. Each block holds either a **chat message** (a user-turn and assistant-turn exchange) or a **fact** (a standalone declarative string). Blocks are independently addressable and retrievable.

## [](#section/Semantic-extraction)Semantic extraction

When a memory block is written, AgentMemory automatically generates a vector embedding and an optional LLM-generated summary. By default this happens asynchronously in the background. Blocks are immediately readable after ingestion but only participate in semantic search once their `status` reaches `ready`. Blocks with `status: processing` or `status: extraction_failed`are excluded from search results.

## [](#section/Authentication)Authentication

Authentication is optional and controlled by the `OIDC_AUTH_ENABLED` server configuration. When enabled, all endpoints except `GET /health` and `GET /metrics` require a valid JWT Bearer token issued by the configured OIDC provider.

Include the token in every request:

```
Authorization: Bearer <token>

```

Tokens are validated against the provider's JWKS endpoint. A `401` response indicates a missing, malformed, or expired token. A `403` response indicates a valid token with insufficient permissions.

## [](#section/Request-and-response-format)Request and response format

All request and response bodies use `application/json`. All timestamps are ISO 8601 strings in UTC. Errors are returned as a JSON object with an `error` code, a human-readable `message`, and an optional `details` field.

## [](#section/Rate-limiting-and-ingestion)Rate limiting and ingestion

Memory block ingestion is accepted immediately, but semantic extraction (embedding generation and summarization) is rate-limited by the configured model provider. If the extraction queue reaches capacity, ingestion requests return `503` with a `retry_after_seconds` field.

## [](#tag/Users)Users

Create and manage user identities. A **user** is the top-level entity in the AgentMemory hierarchy — every session and memory block is owned by a user.

The `user_id` is application-defined and must be unique across the deployment. Use your application's native user identifier (UUID, account ID, or similar) as `user_id` to avoid maintaining a separate mapping table.

Deleting a user is a **cascade operation** — it permanently removes all sessions and memory blocks associated with that user. There is no soft-delete or recovery.

## [](#tag/Users/operation/list%5Fusers%5Fusers%5Fget)List Users 

Retrieve all users. Returns an empty list if no users exist.

##### Authorizations:

_HTTPBearer_

### Responses

**200** 

Successful Response

get/users

AgentMemory server

http://{host}/users

### Response samples 

* 200

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "users": [
  * {
    * "id": "string",
    * "name": "string",
    * "sessions": [
      * "string"  
      ],
    * "metadata": { }  
  }  
],
* "count": 0
}`

## [](#tag/Users/operation/create%5Fuser%5Fusers%5Fpost)Create User 

Create a new user with the specified ID, name, and optional metadata. The `user_id` must be unique — attempting to create a user with an existing ID returns a conflict error.

##### Authorizations:

_HTTPBearer_

##### Request Body schema: application/json

required

| user\_idrequired | string (User Id)                                |
| ---------------- | ----------------------------------------------- |
| namerequired     | string (Name)                                   |
| metadata         | Metadata (object) or Metadata (null) (Metadata) |

### Responses

**201** 

Successful Response

**422** 

Validation Error

post/users

AgentMemory server

http://{host}/users

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "user_id": "user_123",
* "name": "John Doe",
* "metadata": {
  * "department": "Engineering",
  * "level": "senior",
  * "role": "developer"  
}
}`

### Response samples 

* 201
* 422

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "string",
* "name": "string",
* "sessions": [
  * "string"  
],
* "metadata": { }
}`

## [](#tag/Users/operation/search%5Fusers%5Fusers%5Fsearch%5Fpost)Search Users 

Find users matching the provided criteria (`user_id`, `name`, or `metadata`). Multiple criteria are combined with AND logic. At least one criterion must be provided.

##### Authorizations:

_HTTPBearer_

##### Request Body schema: application/json

required

| user\_id | User Id (string) or User Id (null) (User Id)    |
| -------- | ----------------------------------------------- |
| name     | Name (string) or Name (null) (Name)             |
| metadata | Metadata (object) or Metadata (null) (Metadata) |

### Responses

**200** 

Successful Response

**422** 

Validation Error

post/users/search

AgentMemory server

http://{host}/users/search

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "user_id": "user_123",
* "name": "John Doe",
* "metadata": {
  * "department": "Engineering"  
}
}`

### Response samples 

* 200
* 422

Content type

application/json

Example

UserResponse Search Users Users Search PostUser

Copy

 Expand all  Collapse all 

`{
* "id": "string",
* "name": "string",
* "sessions": [
  * "string"  
],
* "metadata": { }
}`

## [](#tag/Users/operation/update%5Fuser%5Fusers%5F%5Fuser%5Fid%5F%5Fput)Update User 

Update an existing user's `name` and/or `metadata`. At least one field must be provided. Omitted fields retain their existing values.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| user\_idrequired | string (User Id) Unique identifier for the user |
| ---------------- | ----------------------------------------------- |

##### Request Body schema: application/json

required

| name     | Name (string) or Name (null) (Name)             |
| -------- | ----------------------------------------------- |
| metadata | Metadata (object) or Metadata (null) (Metadata) |

### Responses

**200** 

Successful Response

**422** 

Validation Error

put/users/{user\_id}

AgentMemory server

http://{host}/users/{user\_id}

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "name": "Jane Smith",
* "metadata": {
  * "department": "Engineering",
  * "role": "senior_developer"  
}
}`

### Response samples 

* 200
* 422

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "string",
* "name": "string",
* "sessions": [
  * "string"  
],
* "metadata": { }
}`

## [](#tag/Users/operation/delete%5Fuser%5Fusers%5F%5Fuser%5Fid%5F%5Fdelete)Delete User 

Permanently delete a user and all associated sessions and memory blocks. This operation is irreversible — there is no soft-delete or recovery.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| user\_idrequired | string (User Id) Unique identifier for the user |
| ---------------- | ----------------------------------------------- |

### Responses

**204** 

Successful Response

**422** 

Validation Error

delete/users/{user\_id}

AgentMemory server

http://{host}/users/{user\_id}

### Response samples 

* 422

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "detail": [
  * {
    * "loc": [
      * "string"  
      ],
    * "msg": "string",
    * "type": "string",
    * "input": null,
    * "ctx": { }  
  }  
]
}`

## [](#tag/Users/operation/modify%5Fttl%5Fusers%5F%5Fuser%5Fid%5F%5Fttl%5Fput)Update Memory Block TTL 

Update the time-to-live (TTL) for memory blocks belonging to a user. Optionally scope the update to specific sessions or specific block IDs.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| user\_idrequired | string (User Id) Unique identifier for the user |
| ---------------- | ----------------------------------------------- |

##### Request Body schema: application/json

required

| session\_id      | Session Id (string) or Session Id (null) (Session Id)        |
| ---------------- | ------------------------------------------------------------ |
| block\_ids       | Array of Block Ids (strings) or Block Ids (null) (Block Ids) |
| new\_ttlrequired | integer (New Ttl) \>= 0                                      |

### Responses

**200** 

Successful Response

**422** 

Validation Error

put/users/{user\_id}/ttl

AgentMemory server

http://{host}/users/{user\_id}/ttl

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "session_id": "string",
* "block_ids": [
  * "string"  
],
* "new_ttl": 0
}`

### Response samples 

* 200
* 422

Content type

application/json

Copy

`null`

## [](#tag/Users/operation/list%5Fuser%5Fsessions%5Fusers%5F%5Fuser%5Fid%5F%5Fsessions%5Fget)List User Sessions 

Retrieve all sessions for a user, including lifecycle state and annotations. Returns an empty list if the user has no sessions.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| user\_idrequired | string (User Id) Unique identifier for the user |
| ---------------- | ----------------------------------------------- |

### Responses

**200** 

Successful Response

**422** 

Validation Error

get/users/{user\_id}/sessions

AgentMemory server

http://{host}/users/{user\_id}/sessions

### Response samples 

* 200
* 422

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "sessions": [
  * {
    * "user_id": "string",
    * "session_id": "string",
    * "start_time": "string",
    * "end_time": "string",
    * "annotations": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "metadata": { },
    * "blocks_ttl": 0  
  }  
],
* "count": 0
}`

## [](#tag/Sessions)Sessions

Create and manage conversation sessions. A **session** scopes memory blocks and defines the default retrieval boundary for semantic search.

Sessions have a two-state lifecycle:

* **Open** (default) — memory can be added, updated, searched, and deleted.
* **Ended** — the session is read-only; no new memory blocks can be added. Call `POST /users/{user_id}/sessions/{session_id}/end` to end a session.

Deleting a session cascades to all of its memory blocks.

## [](#tag/Sessions/operation/create%5Fsession%5Fusers%5F%5Fuser%5Fid%5F%5Fsessions%5Fpost)Create Session 

Create a new session for the specified user. The `session_id` must be unique per user — attempting to create a session with a duplicate ID returns a conflict error.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| user\_idrequired | string (User Id) Unique identifier for the user |
| ---------------- | ----------------------------------------------- |

##### Request Body schema: application/json

required

| session\_idrequired | string (Session Id)                                                         |
| ------------------- | --------------------------------------------------------------------------- |
| annotations         | Annotations (object) or Annotations (null) (Annotations)                    |
| metadata            | Metadata (object) or Metadata (null) (Metadata)                             |
| memory\_blocks\_ttl | Memory Blocks Ttl (integer) or Memory Blocks Ttl (null) (Memory Blocks Ttl) |

### Responses

**201** 

Successful Response

**422** 

Validation Error

post/users/{user\_id}/sessions

AgentMemory server

http://{host}/users/{user\_id}/sessions

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "session_id": "session_456",
* "annotations": {
  * "category": "technical",
  * "intent": "support"  
},
* "metadata": {
  * "platform": "ios",
  * "source": "web_chat"  
},
* "memory_blocks_ttl": 3600
}`

### Response samples 

* 201
* 422

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "user_id": "string",
* "session_id": "string",
* "start_time": "string",
* "end_time": "string",
* "annotations": {
  * "property1": "string",
  * "property2": "string"  
},
* "metadata": { },
* "blocks_ttl": 0
}`

## [](#tag/Sessions/operation/get%5Fsession%5Fusers%5F%5Fuser%5Fid%5F%5Fsessions%5F%5Fsession%5Fid%5F%5Fget)Get Session 

Retrieve a session by ID, including its lifecycle state, annotations, and metadata.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| user\_idrequired    | string (User Id) Unique identifier for the user       |
| ------------------- | ----------------------------------------------------- |
| session\_idrequired | string (Session Id) Unique identifier for the session |

### Responses

**200** 

Successful Response

**422** 

Validation Error

get/users/{user\_id}/sessions/{session\_id}

AgentMemory server

http://{host}/users/{user\_id}/sessions/{session\_id}

### Response samples 

* 200
* 422

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "user_id": "string",
* "session_id": "string",
* "start_time": "string",
* "end_time": "string",
* "annotations": {
  * "property1": "string",
  * "property2": "string"  
},
* "metadata": { },
* "blocks_ttl": 0
}`

## [](#tag/Sessions/operation/update%5Fsession%5Fusers%5F%5Fuser%5Fid%5F%5Fsessions%5F%5Fsession%5Fid%5F%5Fput)Update Session 

Update a session's annotations and/or metadata. At least one field must be provided. Omitted fields retain their existing values.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| user\_idrequired    | string (User Id) Unique identifier for the user       |
| ------------------- | ----------------------------------------------------- |
| session\_idrequired | string (Session Id) Unique identifier for the session |

##### Request Body schema: application/json

required

| annotations | Annotations (object) or Annotations (null) (Annotations) |
| ----------- | -------------------------------------------------------- |
| metadata    | Metadata (object) or Metadata (null) (Metadata)          |

### Responses

**200** 

Successful Response

**422** 

Validation Error

put/users/{user\_id}/sessions/{session\_id}

AgentMemory server

http://{host}/users/{user\_id}/sessions/{session\_id}

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "annotations": {
  * "intent": "support",
  * "status": "resolved"  
},
* "metadata": {
  * "duration": 1200,
  * "satisfaction": "high"  
}
}`

### Response samples 

* 200
* 422

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "user_id": "string",
* "session_id": "string",
* "start_time": "string",
* "end_time": "string",
* "annotations": {
  * "property1": "string",
  * "property2": "string"  
},
* "metadata": { },
* "blocks_ttl": 0
}`

## [](#tag/Sessions/operation/delete%5Fsession%5Fusers%5F%5Fuser%5Fid%5F%5Fsessions%5F%5Fsession%5Fid%5F%5Fdelete)Delete Session 

Permanently delete a session and all its memory blocks. This operation is irreversible.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| user\_idrequired    | string (User Id) Unique identifier for the user       |
| ------------------- | ----------------------------------------------------- |
| session\_idrequired | string (Session Id) Unique identifier for the session |

### Responses

**204** 

Successful Response

**422** 

Validation Error

delete/users/{user\_id}/sessions/{session\_id}

AgentMemory server

http://{host}/users/{user\_id}/sessions/{session\_id}

### Response samples 

* 422

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "detail": [
  * {
    * "loc": [
      * "string"  
      ],
    * "msg": "string",
    * "type": "string",
    * "input": null,
    * "ctx": { }  
  }  
]
}`

## [](#tag/Sessions/operation/end%5Fsession%5Fusers%5F%5Fuser%5Fid%5F%5Fsessions%5F%5Fsession%5Fid%5F%5Fend%5Fpost)End Session 

Mark a session as ended. Once ended, no new memory blocks can be added. Existing memory blocks remain readable and searchable. Returns the updated session with `end_time` set.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| user\_idrequired    | string (User Id) Unique identifier for the user       |
| ------------------- | ----------------------------------------------------- |
| session\_idrequired | string (Session Id) Unique identifier for the session |

### Responses

**200** 

Successful Response

**422** 

Validation Error

post/users/{user\_id}/sessions/{session\_id}/end

AgentMemory server

http://{host}/users/{user\_id}/sessions/{session\_id}/end

### Response samples 

* 200
* 422

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "user_id": "string",
* "session_id": "string",
* "start_time": "string",
* "end_time": "string",
* "annotations": {
  * "property1": "string",
  * "property2": "string"  
},
* "metadata": { },
* "blocks_ttl": 0
}`

## [](#tag/Memory)Memory

Add, retrieve, update, and search memory blocks. A **memory block** is the atomic unit of knowledge — each block holds either a chat message exchange or a standalone fact, and is automatically processed for semantic search.

**Adding memory** — Submit messages or facts in a single request. Semantic extraction runs asynchronously by default; blocks are readable immediately and become searchable once extraction completes.

**Searching memory** — Provide a natural-language query to retrieve semantically similar blocks. Search is session-scoped by default. Set `filters.session_ids` to `"all"` to search across all sessions for a user. Only `ready` blocks are returned.

**TTL and expiry** — Memory blocks carry an optional time-to-live in seconds. TTL can be set per-block, per-session, or globally via server configuration.

## [](#tag/Memory/operation/add%5Fmemory%5Fusers%5F%5Fuser%5Fid%5F%5Fsessions%5F%5Fsession%5Fid%5F%5Fmemory%5Fpost)Add Memory Blocks 

Add one or more memory blocks to the session. Each block holds either a chat message (user + assistant turn) or a fact (declarative string). Blocks are written immediately and queued for semantic extraction. The session must be open — ended sessions reject new blocks.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| user\_idrequired    | string (User Id) Unique identifier for the user       |
| ------------------- | ----------------------------------------------------- |
| session\_idrequired | string (Session Id) Unique identifier for the session |

##### Request Body schema: application/json

required

| messages           | Array of Messages (objects) or Messages (null) (Messages)                                                                                                 |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| facts              | Array of Facts (strings) or Facts (null) (Facts)                                                                                                          |
| annotations        | Annotations (object) or Annotations (null) (Annotations)                                                                                                  |
| created\_at        | Created At (string) or Created At (null) (Created At) ISO 8601 timestamp indicating when the data was originally created. Stored as null if not provided. |
| async\_processing  | boolean (Async Processing) Default: false                                                                                                                 |
| memory\_block\_ttl | Memory Block Ttl (integer) or Memory Block Ttl (null) (Memory Block Ttl)                                                                                  |
| context\_required  | Context Required (boolean) or Context Required (null) (Context Required)                                                                                  |

### Responses

**201** 

Successful Response

**422** 

Validation Error

post/users/{user\_id}/sessions/{session\_id}/memory

AgentMemory server

http://{host}/users/{user\_id}/sessions/{session\_id}/memory

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "messages": [
  * {
    * "assistant_content": "It's sunny and 72°F.",
    * "user_content": "What's the weather?"  
  }  
],
* "facts": [
  * "User prefers email notifications",
  * "User is allergic to peanuts"  
],
* "annotations": {
  * "category": "preferences",
  * "importance": "high"  
},
* "created_at": "2024-06-15T12:00:00",
* "async_processing": true,
* "memory_block_ttl": 3600,
* "context_required": true
}`

### Response samples 

* 201
* 422

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "message": "Successfully added 2 memory block(s)",
* "accepted_count": 2,
* "block_ids": [
  * "block-abc123",
  * "block-def456"  
],
* "rejected_count": 1,
* "rejected_details": {
  * "actual_tokens": 500,
  * "input_index": 0,
  * "per_request_token_limit": 400,
  * "reason": "memory block exceeds per-request token limit"  
}
}`

## [](#tag/Memory/operation/delete%5Fmemory%5Fusers%5F%5Fuser%5Fid%5F%5Fsessions%5F%5Fsession%5Fid%5F%5Fmemory%5Fdelete)Delete Memory Blocks 

Delete memory blocks by ID. Pass a list of block IDs to delete specific blocks, or `"all"` to delete every block in the session.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| user\_idrequired    | string (User Id) Unique identifier for the user       |
| ------------------- | ----------------------------------------------------- |
| session\_idrequired | string (Session Id) Unique identifier for the session |

##### Request Body schema: application/json

required

| block\_idsrequired | Array of Block Ids (strings) or "all" (string) (Block Ids) |
| ------------------ | ---------------------------------------------------------- |

### Responses

**200** 

Successful Response

**422** 

Validation Error

delete/users/{user\_id}/sessions/{session\_id}/memory

AgentMemory server

http://{host}/users/{user\_id}/sessions/{session\_id}/memory

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "block_ids": [
  * "string"  
]
}`

### Response samples 

* 200
* 422

Content type

application/json

Copy

`{
* "deleted_count": 0
}`

## [](#tag/Memory/operation/update%5Fmemory%5Fusers%5F%5Fuser%5Fid%5F%5Fsessions%5F%5Fsession%5Fid%5F%5Fmemory%5F%5Fblock%5Fid%5F%5Fput)Update Memory Block 

Update the content, annotations, or TTL of an existing memory block. Providing a new message or fact triggers re-extraction (new embedding and summary). Omitted fields retain their existing values. Use this endpoint to retry extraction on blocks with `status: extraction_failed` by setting `async_processing: true`. If the block does not exist or has expired due to TTL, responds with 404.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| user\_idrequired    | string (User Id) Unique identifier for the user          |
| ------------------- | -------------------------------------------------------- |
| session\_idrequired | string (Session Id) Unique identifier for the session    |
| block\_idrequired   | string (Block Id) Unique identifier for the memory block |

##### Request Body schema: application/json

required

| message            | ChatMessage (object) or null                                                                                                                          |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| fact               | Fact (string) or Fact (null) (Fact)                                                                                                                   |
| annotations        | Annotations (object) or Annotations (null) (Annotations) New annotations to overwrite existing ones. If None, existing annotations are preserved.     |
| memory\_block\_ttl | Memory Block Ttl (integer) or Memory Block Ttl (null) (Memory Block Ttl) New TTL in seconds. If None, existing TTL is preserved.                      |
| async\_processing  | boolean (Async Processing) Default: false If True, semantic extraction runs in background via queue.                                                  |
| context\_required  | Context Required (boolean) or Context Required (null) (Context Required) Whether semantic extraction is required. If None, uses environment variable. |

### Responses

**200** 

Successful Response

**422** 

Validation Error

put/users/{user\_id}/sessions/{session\_id}/memory/{block\_id}

AgentMemory server

http://{host}/users/{user\_id}/sessions/{session\_id}/memory/{block\_id}

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "message": {
  * "assistant_content": "Updated answer",
  * "user_content": "Updated question"  
},
* "fact": "Updated fact about the user",
* "annotations": {
  * "category": "updated",
  * "importance": "high"  
},
* "memory_block_ttl": 3600,
* "async_processing": true,
* "context_required": true
}`

### Response samples 

* 200
* 422

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "message": "Memory block updated successfully",
* "block": {
  * "block_id": "string",
  * "user_id": "string",
  * "session_id": "string",
  * "message": {
    * "user_content": "What's the weather today?",
    * "assistant_content": "It's sunny and 72°F."  
  },
  * "fact": "string",
  * "ingested_at": "string",
  * "created_at": "string",
  * "last_queued_at": "string",
  * "fail_count": 0,
  * "annotations": {
    * "property1": "string",
    * "property2": "string"  
  },
  * "summary": "string",
  * "contexts": [
    * "string"  
  ],
  * "status": "processing",
  * "rel_score": 0  
}
}`

## [](#tag/Memory/operation/search%5Fmemory%5Fusers%5F%5Fuser%5Fid%5F%5Fsessions%5F%5Fsession%5Fid%5F%5Fmemory%5Fsearch%5Fpost)Search Memory 

Retrieve memory blocks using semantic similarity and/or filters. Provide a natural-language `query` to rank blocks by relevance, or use `filters` alone for deterministic retrieval. Search is session-scoped by default — set `filters.session_ids` to `"all"` to search across all sessions for the user. Only `ready` blocks appear in results.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| user\_idrequired    | string (User Id) Unique identifier for the user       |
| ------------------- | ----------------------------------------------------- |
| session\_idrequired | string (Session Id) Unique identifier for the session |

##### Request Body schema: application/json

required

| query   | Query (string) or Query (null) (Query) |
| ------- | -------------------------------------- |
| filters | FilterOptions (object) or null         |

### Responses

**200** 

Successful Response

**422** 

Validation Error

post/users/{user\_id}/sessions/{session\_id}/memory/search

AgentMemory server

http://{host}/users/{user\_id}/sessions/{session\_id}/memory/search

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "query": "What are the user's preferences?",
* "filters": {
  * "start_time": "2025-12-22T00:00:00",
  * "end_time": "2025-12-22T23:59:59",
  * "created_start_time": "2025-12-22T00:00:00",
  * "created_end_time": "2025-12-22T23:59:59",
  * "session_ids": [
    * "session_123",
    * "session_456"  
  ],
  * "block_ids": [
    * "block_001",
    * "block_002"  
  ],
  * "relevant_k": 10,
  * "annotations": {
    * "importance": "high"  
  },
  * "order_by": "ingested_at"  
}
}`

### Response samples 

* 200
* 422

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "memory_blocks": [
  * {
    * "block_id": "string",
    * "user_id": "string",
    * "session_id": "string",
    * "message": {
      * "user_content": "What's the weather today?",
      * "assistant_content": "It's sunny and 72°F."  
      },
    * "fact": "string",
    * "ingested_at": "string",
    * "created_at": "string",
    * "last_queued_at": "string",
    * "fail_count": 0,
    * "annotations": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "summary": "string",
    * "contexts": [
      * "string"  
      ],
    * "status": "processing",
    * "rel_score": 0  
  }  
],
* "count": 0
}`

## [](#tag/Memory/operation/list%5Fmemories%5Fusers%5F%5Fuser%5Fid%5F%5Fmemory%5Fget)List Memory Blocks 

Paginated list of memory blocks for a user, ordered newest first. Use `session_ids` to scope results to specific sessions. Always specify `limit` and `offset` — unbounded requests on large datasets are slow.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| user\_idrequired | string (User Id) Unique identifier for the user |
| ---------------- | ----------------------------------------------- |

##### query Parameters

| session\_ids | Session Ids (string) or Session Ids (null) (Session Ids) Comma-separated session IDs to filter by, or 'all' for all sessions        |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| limit        | integer (Limit) \[ 1 .. 200 \] Default: 20 Maximum number of memory blocks to return (1–200)                                        |
| offset       | integer (Offset) \>= 0 Default: 0 Number of memory blocks to skip for pagination                                                    |
| order\_by    | string (Order By) Default: "ingested\_at" Enum: "ingested\_at" "created\_at" Field to order results by. Defaults to 'ingested\_at'. |

### Responses

**200** 

Successful Response

**422** 

Validation Error

get/users/{user\_id}/memory

AgentMemory server

http://{host}/users/{user\_id}/memory

### Response samples 

* 200
* 422

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "memory_blocks": [
  * {
    * "block_id": "string",
    * "user_id": "string",
    * "session_id": "string",
    * "message": {
      * "user_content": "What's the weather today?",
      * "assistant_content": "It's sunny and 72°F."  
      },
    * "fact": "string",
    * "ingested_at": "string",
    * "created_at": "string",
    * "last_queued_at": "string",
    * "fail_count": 0,
    * "annotations": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "summary": "string",
    * "contexts": [
      * "string"  
      ],
    * "status": "processing",
    * "rel_score": 0  
  }  
],
* "count": 0,
* "total": 0,
* "limit": 1,
* "offset": 0
}`

## [](#tag/Health)Health

Monitor the operational status of AgentMemory and its dependencies.

`GET /health` is a public endpoint suitable for load balancer health probes. All other health endpoints require authentication and provide deeper diagnostic detail about the database connection, model service availability, and the semantic extraction queue.

| Status    | Meaning                                         |
| --------- | ----------------------------------------------- |
| healthy   | Component is operating normally                 |
| degraded  | Component is reachable but not fully functional |
| unhealthy | Component is unreachable or critically impaired |

## [](#tag/Health/operation/health%5Fcheck%5Fhealth%5Fget)Check Server Health 

Return server health status, version, and uptime. Public endpoint — no authentication required.

### Responses

**200** 

Successful Response

get/health

AgentMemory server

http://{host}/health

### Response samples 

* 200

Content type

application/json

Copy

`{
* "status": "healthy",
* "version": "string",
* "uptime_seconds": 0
}`

## [](#tag/Health/operation/check%5Fcouchbase%5Fhealth%5Fhealth%5Fcouchbase%5Fget)Check Database Health 

Verify that AgentMemory can reach and query the Couchbase database.

##### Authorizations:

_HTTPBearer_

### Responses

**200** 

Successful Response

get/health/couchbase

AgentMemory server

http://{host}/health/couchbase

### Response samples 

* 200

Content type

application/json

Copy

`{
* "status": "healthy"
}`

## [](#tag/Health/operation/check%5Fmodels%5Fhealth%5Fhealth%5Fmodels%5Fget)Check Model Service Health 

Check reachability and status of the configured embedding and LLM model services.

##### Authorizations:

_HTTPBearer_

### Responses

**200** 

Successful Response

get/health/models

AgentMemory server

http://{host}/health/models

### Response samples 

* 200

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "status": "healthy",
* "embedding": {
  * "status": "string",
  * "model": "string",
  * "retry_after": 0  
},
* "llm": {
  * "status": "string",
  * "model": "string",
  * "retry_after": 0  
}
}`

## [](#tag/Health/operation/check%5Fasync%5Fbatch%5Fprocessor%5Fhealth%5Fhealth%5Fasync%5Fbatch%5Fprocessor%5Fget)Check Extraction Queue Health 

Return lightweight readiness status for the semantic extraction queue.

##### Authorizations:

_HTTPBearer_

### Responses

**200** 

Successful Response

get/health/async-batch-processor

AgentMemory server

http://{host}/health/async-batch-processor

### Response samples 

* 200

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "status": "string",
* "message": "string",
* "queue": {
  * "size": 0,
  * "queued_ids": 0,
  * "processing": 0,
  * "max_size": 0  
},
* "rate_budget": {
  * "available_requests": 0,
  * "available_tokens": 0,
  * "max_requests_per_minute": 0,
  * "max_tokens_per_minute": 0,
  * "per_request_token_limit": 0  
},
* "statistics": {
  * "total_enqueued": 0,
  * "total_recovered": 0,
  * "total_dispatched": 0,
  * "total_completed": 0,
  * "total_failed": 0,
  * "queue_full": 0,
  * "queue_duplicates": 0,
  * "queue_oversized": 0,
  * "recovery_duplicates": 0,
  * "active_tasks": 0,
  * "loop_running": true,
  * "dispatcher_alive": true  
},
* "loop_running": true,
* "dispatcher_alive": true
}`

## [](#tag/Health/operation/check%5Fasync%5Fbatch%5Fprocessor%5Fstats%5Fhealth%5Fasync%5Fbatch%5Fprocessor%5Fstats%5Fget)Get Extraction Queue Statistics 

Return detailed queue depth, model API rate budget, and cumulative throughput statistics for the semantic extraction queue.

##### Authorizations:

_HTTPBearer_

### Responses

**200** 

Successful Response

get/health/async-batch-processor-stats

AgentMemory server

http://{host}/health/async-batch-processor-stats

### Response samples 

* 200

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "status": "string",
* "message": "string",
* "queue": {
  * "size": 0,
  * "queued_ids": 0,
  * "processing": 0,
  * "max_size": 0  
},
* "rate_budget": {
  * "available_requests": 0,
  * "available_tokens": 0,
  * "max_requests_per_minute": 0,
  * "max_tokens_per_minute": 0,
  * "per_request_token_limit": 0  
},
* "statistics": {
  * "total_enqueued": 0,
  * "total_recovered": 0,
  * "total_dispatched": 0,
  * "total_completed": 0,
  * "total_failed": 0,
  * "queue_full": 0,
  * "queue_duplicates": 0,
  * "queue_oversized": 0,
  * "recovery_duplicates": 0,
  * "active_tasks": 0,
  * "loop_running": true,
  * "dispatcher_alive": true  
},
* "loop_running": true,
* "dispatcher_alive": true
}`

## [](#tag/Health/operation/check%5Fmemory%5Fhealth%5Fhealth%5Fmemory%5Fget)Check Memory Pressure Status 

Return current memory usage relative to the configured quota threshold. When usage exceeds the threshold, new ingestion requests are rejected until pressure subsides.

##### Authorizations:

_HTTPBearer_

### Responses

**200** 

Successful Response

get/health/memory

AgentMemory server

http://{host}/health/memory

### Response samples 

* 200

Content type

application/json

Copy

`{
* "status": "string",
* "message": "string",
* "accepting_requests": true,
* "usage_percent": 0,
* "threshold_percent": 0,
* "last_check": 0
}`

## [](#tag/Metrics)Metrics

Expose Prometheus-compatible metrics for monitoring and alerting. This endpoint is public and requires no authentication, making it suitable for Prometheus scrape targets and infrastructure monitoring tools.

## [](#tag/Metrics/operation/metrics%5Fmetrics%5Fget)Scrape Prometheus Metrics 

### Responses

**200** 

Successful Response

get/metrics

AgentMemory server

http://{host}/metrics

### Response samples 

* 200

Content type

application/json

Copy

`null`

## [](#tag/Logs)Logs

Download a ZIP archive of server logs and optional system diagnostics. Use this endpoint to collect diagnostic data for support requests or incident post-mortems. Requires authentication.

## [](#tag/Logs/operation/collect%5Flogs%5Flogs%5Fcollect%5Fget)Download Diagnostic Logs 

Download server logs and optional system diagnostics as a ZIP archive. Use `log_types` to select log categories and `start_time`/`end_time` to narrow the time range. Add `sys_commands` to include live system snapshots (CPU, memory, disk, network) in the archive. Include this archive in support requests and incident post-mortems.

##### Authorizations:

_HTTPBearer_

##### query Parameters

| start\_time   | Start Time (string) or Start Time (null) (Start Time) Include log lines at or after this timestamp                               |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| end\_time     | End Time (string) or End Time (null) (End Time) Include log lines at or before this timestamp                                    |
| log\_types    | Array of Log Types (strings) or Log Types (null) (Log Types) Log categories to include                                           |
| sys\_commands | Array of Sys Commands (strings) or Sys Commands (null) (Sys Commands) Optional system commands to run and include in the archive |

### Responses

**200** 

Successful Response

**400** 

Invalid request

**422** 

Validation Error

get/logs/collect

AgentMemory server

http://{host}/logs/collect

### Response samples 

* 200
* 400
* 422

Content type

application/json

Copy

`null`