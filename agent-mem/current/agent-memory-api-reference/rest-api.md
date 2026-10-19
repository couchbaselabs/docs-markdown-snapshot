---
title: Agent Memory API Reference
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase Agent Memory
    version: "1.1"
antora:
  editUrl: https://github.com/couchbaselabs/docs-agentmemory/edit/release/1.1/modules/agent-memory-api-reference/pages/rest-api.adoc
  xref: xref:agent-mem:agent-memory-api-reference:rest-api.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/agent-mem/current/agent-memory-api-reference/rest-api.html)

# Agent Memory API Reference

* Core concepts
* Semantic extraction
* Authentication
* Authorization
* Request and response format
* Rate limiting and ingestion
* Memory Management
  * Users
    * postCreate User
    * getList Users
    * getGet User
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
  * Prompts
    * postCreate Prompt
    * getList Prompts
    * getGet Prompt
    * putUpdate Prompt
    * delPurge Prompt
    * getList Prompt Versions
    * putArchive Prompt
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

# AgentMemory API (1.1.0)

Download OpenAPI specification:

AgentMemory is a persistent, semantic memory service for AI agents. It stores conversation history, extracted facts, and vector embeddings, enabling agents to recall relevant past context across sessions and conversations.

## [](#section/Core-concepts)Core concepts

AgentMemory organizes data in a three-level hierarchy:

* **User** \- a persistent identity (human end-user, agent instance, or service account) that owns one or more sessions. A user must exist before sessions or memory can be created.
* **Session** \- a scoped conversation context owned by a user. The session is the default boundary for semantic search - results are drawn from the current session unless the request explicitly expands scope. Sessions can be ended to prevent further writes.
* **Memory block** \- the atomic unit of stored knowledge. Each block holds either a **chat message** (a user-turn and assistant-turn exchange) or a **fact** (a standalone declarative string). Blocks are independently addressable and retrievable.

## [](#section/Semantic-extraction)Semantic extraction

When a memory block is written, AgentMemory generates its vector embedding before responding, so every block is searchable as soon as the write returns. The optional LLM-generated summary and contexts are produced separately, by default asynchronously in the background. Search returns blocks in any `status`: a `processing` or `extraction_failed` block has no summary or contexts yet, only its raw content.

## [](#section/Authentication)Authentication

Authentication is optional and controlled by the `OIDC_AUTH_ENABLED` server configuration. When enabled, all endpoints except `GET /health` and `GET /metrics` require a valid JWT Bearer token issued by the configured OIDC provider.

Include the token in every request: `Authorization: Bearer <token>`

Tokens are validated against the provider's JWKS endpoint. A `401` response indicates a missing, malformed, or expired token.

## [](#section/Authorization)Authorization

Role-based authorization is a separate switch, `AGENTMEMORY_AUTHZ_ENABLED`, off by default. When it is off, any valid token reaches every endpoint. When it is on, the token's roles claim must carry at least one of three ranked roles:

| Role       | Grants                                                               |
| ---------- | -------------------------------------------------------------------- |
| ams\_ro    | Reads: search, get, list, and the /health/\* diagnostics             |
| ams\_rw    | Everything ams\_ro does, plus user, session, and memory mutations    |
| ams\_admin | Everything, plus GET /users, prompt mutations, and GET /logs/collect |

Ranks are cumulative, so a single role is enough - `ams_admin` does not also need the lower two. Roles the server does not recognize are ignored rather than rejected, so unrelated realm roles in the same claim are harmless. A token carrying none of the three is denied on every non-public endpoint.

A `403` response means the token was valid but its rank was below what the endpoint requires; the response body names the role needed, for example `Insufficient permissions. Required role: ams_rw or higher`.

## [](#section/Request-and-response-format)Request and response format

All request and response bodies use `application/json`. All timestamps are ISO 8601 strings in UTC. Errors are returned as a JSON object with an `error` code, a human-readable `message`, and an optional `details` field.

## [](#section/Rate-limiting-and-ingestion)Rate limiting and ingestion

Memory block ingestion is accepted immediately, but semantic extraction (embedding generation and summarization) is rate-limited by the configured model provider. If the extraction queue reaches capacity, ingestion requests return `503` with a `retry_after_seconds` field.

## [](#tag/Users)Users

Create and manage user identities. A **user** is the top-level entity in the AgentMemory hierarchy - every session and memory block is owned by a user.

The `user_id` is application-defined and must be unique across the deployment. Use your application's native user identifier (UUID, account ID, or similar) as `user_id` to avoid maintaining a separate mapping table.

Deleting a user is a **cascade operation** \- it permanently removes all sessions and memory blocks associated with that user. There is no soft-delete or recovery.

## [](#tag/Users/operation/create%5Fuser%5Fusers%5Fpost)Create User 

Create a new user with the specified ID, name, and optional metadata. The `user_id` must be unique — attempting to create a user with an existing ID returns a conflict error.

##### Authorizations:

_HTTPBearer_

##### Request Body schema: application/json

required

| user\_idrequired | string (User Id) Unique user ID. Must not be blank. A duplicate returns 409.                                              |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------- |
| namerequired     | string (Name) Display name. Must not be blank.                                                                            |
| metadata         | Metadata (object) or Metadata (null) (Metadata) Free-form JSON stored with the user. GET /users can filter on its values. |

### Responses

**201** 

Successful Response

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**409** 

The resource already exists, is archived, or is busy.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

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
* 401
* 403
* 409
* 422
* 500
* 503

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

## [](#tag/Users/operation/list%5Fusers%5Fusers%5Fget)List Users 

Retrieve users, optionally filtered by `name` and/or `metadata`, paginated. Criteria are combined with AND logic and match on exact equality — no wildcards. Returns an empty list if no users match, or if no users exist.

##### Authorizations:

_HTTPBearer_

##### query Parameters

| name     | Name (string) or Name (null) (Name) Filter by exact user name                                                                                                |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| metadata | Array of Metadata (strings) or Metadata (null) (Metadata) Filter by metadata, as repeated key=value params. Values are matched as strings on exact equality. |
| limit    | integer (Limit) \[ 1 .. 500 \] Default: 50                                                                                                                   |
| offset   | integer (Offset) \>= 0 Default: 0                                                                                                                            |

### Responses

**200** 

Successful Response

**400** 

The request was rejected before it reached the database.

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

get/users

AgentMemory server

http://{host}/users

### Response samples 

* 200
* 400
* 401
* 403
* 422
* 500
* 503

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
* "count": 0,
* "total": 0,
* "limit": 1,
* "offset": 0
}`

## [](#tag/Users/operation/get%5Fuser%5Fusers%5F%5Fuser%5Fid%5F%5Fget)Get User 

Retrieve a single user by ID. Responds with 404 if no such user exists. Filtered lookup lives on the List Users endpoint.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| user\_idrequired | string (User Id) Unique identifier for the user |
| ---------------- | ----------------------------------------------- |

### Responses

**200** 

Successful Response

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**404** 

No such resource. The message names the id that was looked up.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

get/users/{user\_id}

AgentMemory server

http://{host}/users/{user\_id}

### Response samples 

* 200
* 401
* 403
* 404
* 422
* 500
* 503

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

## [](#tag/Users/operation/update%5Fuser%5Fusers%5F%5Fuser%5Fid%5F%5Fput)Update User 

Update an existing user's `name` and/or `metadata`. At least one field must be provided. Omitted fields retain their existing values.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| user\_idrequired | string (User Id) Unique identifier for the user |
| ---------------- | ----------------------------------------------- |

##### Request Body schema: application/json

required

| name     | Name (string) or Name (null) (Name) New display name. Omit to keep the current one.                                                                                        |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| metadata | Metadata (object) or Metadata (null) (Metadata) Replaces the whole metadata object (no merge). Omit to keep the current one. At least one of name or metadata is required. |

### Responses

**200** 

Successful Response

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**404** 

No such resource. The message names the id that was looked up.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

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
* 401
* 403
* 404
* 422
* 500
* 503

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

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**404** 

No such resource. The message names the id that was looked up.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

delete/users/{user\_id}

AgentMemory server

http://{host}/users/{user\_id}

### Response samples 

* 401
* 403
* 404
* 422
* 500
* 503

Content type

application/json

Example

AUTHENTICATION\_REQUIREDTOKEN\_EXPIREDINVALID\_TOKENTOKEN\_VALIDATION\_FAILEDAUTHENTICATION\_REQUIRED

Copy

`{
* "error": "AUTHENTICATION_REQUIRED",
* "message": "Authentication required"
}`

## [](#tag/Users/operation/modify%5Fttl%5Fusers%5F%5Fuser%5Fid%5F%5Fttl%5Fput)Update Memory Block TTL 

Update the time-to-live (TTL) for memory blocks belonging to a user. Optionally scope the update to one session, or to specific block IDs within that session (block\_ids requires session\_id). Every targeted session must already be ended; open sessions are rejected before any block is retimed.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| user\_idrequired | string (User Id) Unique identifier for the user |
| ---------------- | ----------------------------------------------- |

##### Request Body schema: application/json

required

| session\_id      | Session Id (string) or Session Id (null) (Session Id) Session to retime. Omit to retime every session the user owns. Every targeted session must already be ended. |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| block\_ids       | Array of Block Ids (strings) or Block Ids (null) (Block Ids) Retime only these blocks. Requires session\_id, and every ID must belong to that session.             |
| new\_ttlrequired | integer (New Ttl) \>= 0 New TTL in seconds, counted from this call. 0 removes the expiry so the blocks never expire.                                               |

### Responses

**200** 

Successful Response

**400** 

The request was rejected before it reached the database.

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**404** 

No such resource. The message names the id that was looked up.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

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
* 400
* 401
* 403
* 404
* 422
* 500
* 503

Content type

application/json

Copy

`null`

## [](#tag/Users/operation/list%5Fuser%5Fsessions%5Fusers%5F%5Fuser%5Fid%5F%5Fsessions%5Fget)List User Sessions 

Retrieve a user's sessions, including lifecycle state and annotations, paginated. Returns an empty list if the user has no sessions.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| user\_idrequired | string (User Id) Unique identifier for the user |
| ---------------- | ----------------------------------------------- |

##### query Parameters

| limit  | integer (Limit) \[ 1 .. 500 \] Default: 50 |
| ------ | ------------------------------------------ |
| offset | integer (Offset) \>= 0 Default: 0          |

### Responses

**200** 

Successful Response

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**404** 

No such resource. The message names the id that was looked up.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

get/users/{user\_id}/sessions

AgentMemory server

http://{host}/users/{user\_id}/sessions

### Response samples 

* 200
* 401
* 403
* 404
* 422
* 500
* 503

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
* "count": 0,
* "total": 0,
* "limit": 1,
* "offset": 0
}`

## [](#tag/Sessions)Sessions

Create and manage conversation sessions. A **session** scopes memory blocks and defines the default retrieval boundary for semantic search.

Sessions have a two-state lifecycle:

* **Open** (default) - memory can be added, updated, searched, and deleted.
* **Ended** \- the session is read-only; no new memory blocks can be added. Call `POST /users/{user_id}/sessions/{session_id}/end` to end a session.

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

| session\_idrequired | string (Session Id) Session ID, unique per user. Must not be blank. A duplicate returns 409.                                                                                                                                                                                                |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| annotations         | Annotations (object) or Annotations (null) (Annotations) String key/value labels stored with the session.                                                                                                                                                                                   |
| metadata            | Metadata (object) or Metadata (null) (Metadata) Free-form JSON stored with the session.                                                                                                                                                                                                     |
| memory\_blocks\_ttl | Memory Blocks Ttl (integer) or Memory Blocks Ttl (null) (Memory Blocks Ttl) Default TTL in seconds for blocks added to this session without their own memory\_block\_ttl. Omit or 0 for no session default: blocks then use AGENTMEMORY\_MEMORY\_BLOCK\_TTL if set, otherwise never expire. |

### Responses

**201** 

Successful Response

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**404** 

No such resource. The message names the id that was looked up.

**409** 

The resource already exists, is archived, or is busy.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

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
* 401
* 403
* 404
* 409
* 422
* 500
* 503

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

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**404** 

No such resource. The message names the id that was looked up.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

get/users/{user\_id}/sessions/{session\_id}

AgentMemory server

http://{host}/users/{user\_id}/sessions/{session\_id}

### Response samples 

* 200
* 401
* 403
* 404
* 422
* 500
* 503

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

| annotations | Annotations (object) or Annotations (null) (Annotations) Replaces all session annotations (no merge). Omit to keep them. Must not be an empty object. |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| metadata    | Metadata (object) or Metadata (null) (Metadata) Replaces all session metadata (no merge). Omit to keep it. Must not be an empty object.               |

### Responses

**200** 

Successful Response

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**404** 

No such resource. The message names the id that was looked up.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

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
* 401
* 403
* 404
* 422
* 500
* 503

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

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**404** 

No such resource. The message names the id that was looked up.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

delete/users/{user\_id}/sessions/{session\_id}

AgentMemory server

http://{host}/users/{user\_id}/sessions/{session\_id}

### Response samples 

* 401
* 403
* 404
* 422
* 500
* 503

Content type

application/json

Example

AUTHENTICATION\_REQUIREDTOKEN\_EXPIREDINVALID\_TOKENTOKEN\_VALIDATION\_FAILEDAUTHENTICATION\_REQUIRED

Copy

`{
* "error": "AUTHENTICATION_REQUIRED",
* "message": "Authentication required"
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

**400** 

The request was rejected before it reached the database.

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**404** 

No such resource. The message names the id that was looked up.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

post/users/{user\_id}/sessions/{session\_id}/end

AgentMemory server

http://{host}/users/{user\_id}/sessions/{session\_id}/end

### Response samples 

* 200
* 400
* 401
* 403
* 404
* 422
* 500
* 503

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

Add, retrieve, update, and search memory blocks. A **memory block** is the atomic unit of knowledge - each block holds either a chat message exchange or a standalone fact, and is automatically processed for semantic search.

**Adding memory** \- Submit messages or facts in a single request. Semantic extraction runs asynchronously by default; blocks are readable and searchable immediately, and their extracted facts appear once extraction completes.

**Searching memory** \- Provide a natural-language query to retrieve semantically similar blocks. Search is session-scoped by default. Set `filters.session_ids` to `"all"` to search across all sessions for a user. Blocks still being processed are returned with their raw content.

**TTL and expiry** \- Memory blocks carry an optional time-to-live in seconds. TTL can be set per-block, per-session, or globally via server configuration.

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

| messages           | Array of Messages (objects) or Messages (null) (Messages) Chat exchanges to store, one block per message. Send exactly one of messages or facts.                                                                                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| facts              | Array of Facts (strings) or Facts (null) (Facts) Facts to store, one block per fact. Each must be non-blank. Send exactly one of messages or facts.                                                                                                                                              |
| annotations        | Annotations (object) or Annotations (null) (Annotations) Keys must match ^\[a-zA-Z\_\]\[a-zA-Z0-9\_\]\*$ (letters, digits, underscore; not starting with a digit): each key becomes an index field and a query identifier. Values are free-form strings.                                         |
| created\_at        | Created At (string) or Created At (null) (Created At) ISO 8601 timestamp indicating when the data was originally created. Defaults to the ingestion time if not provided.                                                                                                                        |
| async\_processing  | boolean (Async Processing) Default: true If true, returns once blocks are stored with status processing, and LLM extraction runs in the background. If false, extraction finishes before the response. Embeddings are always generated before the response, so blocks are searchable either way. |
| memory\_block\_ttl | Memory Block Ttl (integer) or Memory Block Ttl (null) (Memory Block Ttl) TTL in seconds for the new blocks; 0 means never expire. Omit to use the session's blocks\_ttl, then AGENTMEMORY\_MEMORY\_BLOCK\_TTL, otherwise no expiry.                                                              |
| context\_required  | Context Required (boolean) or Context Required (null) (Context Required) Whether to run LLM extraction (summary and contexts). Omit to use AGENTMEMORY\_EXTRACT\_SEMANTIC (default true).                                                                                                        |
| prompt\_id         | Prompt Id (string) or Prompt Id (null) (Prompt Id) Registry prompt\_id to use for extraction. Must already exist (and not be archived) - an unresolvable prompt\_id rejects the whole call before any work is done.                                                                              |
| prompt\_vid        | Prompt Vid (integer) or Prompt Vid (null) (Prompt Vid) Pin extraction to this exact immutable registry version of prompt\_id, rather than late-binding to whatever prompt\_id currently says. Requires prompt\_id to also be provided in the same call - rejected otherwise.                     |

### Responses

**201** 

Successful Response

**400** 

The request was rejected before it reached the database. For MEMORY\_BLOCK\_TOO\_LARGE, `details.limit` names the limit that was hit and nothing was stored.

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**404** 

No such resource. The message names the id that was looked up.

**409** 

The resource already exists, is archived, or is busy.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**429** 

The async processing queue is full. Retry-After is set and `details` carries the queue depth to back off on.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**502** 

The model service returned an error or could not be reached.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

**504** 

The model service did not respond in time.

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
* "context_required": true,
* "prompt_id": "support_tickets",
* "prompt_vid": 1
}`

### Response samples 

* 201
* 400
* 401
* 403
* 404
* 409
* 422
* 429
* 500
* 502
* 503
* 504

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

| block\_idsrequired | Array of Block Ids (strings) or "all" (string) (Block Ids) Block IDs to delete, or "all" for every block in the session. |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ |

### Responses

**200** 

Successful Response

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**404** 

No such resource. The message names the id that was looked up.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

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
* 401
* 403
* 404
* 422
* 500
* 503

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "deleted_count": 0,
* "failed_count": 0,
* "failed_block_ids": [ ]
}`

## [](#tag/Memory/operation/update%5Fmemory%5Fusers%5F%5Fuser%5Fid%5F%5Fsessions%5F%5Fsession%5Fid%5F%5Fmemory%5F%5Fblock%5Fid%5F%5Fput)Update Memory Block 

Update the content, annotations, or TTL of an existing memory block. Providing a new message or fact triggers re-extraction (new embedding and summary). Changing `prompt_id` or `prompt_vid` also triggers re-extraction. Omitted fields retain their existing values. To retry a block with `status: extraction_failed`, resend its `message` or `fact`: that re-runs extraction and resets `fail_count`. `async_processing` only controls whether that extraction runs in the background. If the block does not exist or has expired due to TTL, responds with 404.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| user\_idrequired    | string (User Id) Unique identifier for the user          |
| ------------------- | -------------------------------------------------------- |
| session\_idrequired | string (Session Id) Unique identifier for the session    |
| block\_idrequired   | string (Block Id) Unique identifier for the memory block |

##### Request Body schema: application/json

required

| message            | ChatMessage (object) or null New content for a message block. Rejected on a fact block. Re-embeds the block and re-runs extraction.                                                                                                                                                                                                               |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| fact               | Fact (string) or Fact (null) (Fact) New content for a fact block. Rejected on a message block. Re-embeds the block and re-runs extraction.                                                                                                                                                                                                        |
| annotations        | Annotations (object) or Annotations (null) (Annotations) New annotations to overwrite existing ones. If None, existing annotations are preserved. Keys must match ^\[a-zA-Z\_\]\[a-zA-Z0-9\_\]\*$ (letters, digits, underscore; not starting with a digit): each key becomes an index field and a query identifier. Values are free-form strings. |
| memory\_block\_ttl | Memory Block Ttl (integer) or Memory Block Ttl (null) (Memory Block Ttl) New TTL in seconds. If None, existing TTL is preserved.                                                                                                                                                                                                                  |
| async\_processing  | boolean (Async Processing) Default: false If True, semantic extraction runs in background via queue.                                                                                                                                                                                                                                              |
| context\_required  | Context Required (boolean) or Context Required (null) (Context Required) Whether semantic extraction is required. If None, uses environment variable.                                                                                                                                                                                             |
| prompt\_id         | Prompt Id (string) or Prompt Id (null) (Prompt Id) Omit to inherit the block's existing prompt\_id/prompt\_vid. Pass the literal string "default" to explicitly clear both to None. Pass a real prompt\_id to switch - must already exist (and not be archived).                                                                                  |
| prompt\_vid        | Prompt Vid (integer) or Prompt Vid (null) (Prompt Vid) Pin extraction to this exact immutable registry version of prompt\_id. Requires a real prompt\_id in this same call - rejected if prompt\_id is omitted or is 'default'.                                                                                                                   |

### Responses

**200** 

Successful Response

**400** 

The request was rejected before it reached the database. For MEMORY\_BLOCK\_TOO\_LARGE, `details.limit` names the limit that was hit and nothing was stored.

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**404** 

No such resource. The message names the id that was looked up.

**409** 

The resource already exists, is archived, or is busy.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**429** 

The async processing queue is full. Retry-After is set and `details` carries the queue depth to back off on.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**502** 

The model service returned an error or could not be reached.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

**504** 

The model service did not respond in time.

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
* "context_required": true,
* "prompt_id": "support_tickets",
* "prompt_vid": 1
}`

### Response samples 

* 200
* 400
* 401
* 403
* 404
* 409
* 422
* 429
* 500
* 502
* 503
* 504

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
  * "prompt_id": "string",
  * "prompt_vid": 0,
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

Retrieve memory blocks using semantic similarity and/or filters. Provide a natural-language `query` to rank blocks by relevance, or use `filters` alone for deterministic retrieval. Search is session-scoped by default — set `filters.session_ids` to `"all"` to search across all sessions for the user. Blocks still being processed are included and carry their raw content until extraction finishes.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| user\_idrequired    | string (User Id) Unique identifier for the user       |
| ------------------- | ----------------------------------------------------- |
| session\_idrequired | string (Session Id) Unique identifier for the session |

##### Request Body schema: application/json

required

| query   | Query (string) or Query (null) (Query) Natural-language text to rank blocks by semantic similarity. Omit to retrieve by filters only. |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| filters | FilterOptions (object) or null Scope and filters. Omit to search the current session with defaults.                                   |

### Responses

**200** 

Successful Response

**400** 

The request was rejected before it reached the database.

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**404** 

No such resource. The message names the id that was looked up.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**502** 

The model service returned an error or could not be reached.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

**504** 

The model service did not respond in time.

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
  * "annotation_filter_mode": "pre",
  * "order_by": "ingested_at",
  * "prompt_id": "support_tickets",
  * "prompt_vid": 1  
}
}`

### Response samples 

* 200
* 400
* 401
* 403
* 404
* 422
* 500
* 502
* 503
* 504

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
    * "prompt_id": "string",
    * "prompt_vid": 0,
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

**400** 

The request was rejected before it reached the database.

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**404** 

No such resource. The message names the id that was looked up.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

get/users/{user\_id}/memory

AgentMemory server

http://{host}/users/{user\_id}/memory

### Response samples 

* 200
* 400
* 401
* 403
* 404
* 422
* 500
* 503

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
    * "prompt_id": "string",
    * "prompt_vid": 0,
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

## [](#tag/Prompts)Prompts

Manage the custom extraction prompt registry. A **prompt** is a named, versioned block of extraction instructions that `add_memory`/`update_memory` can reference by `prompt_id` to customize what gets extracted from a memory block, without touching the locked output schema.

`prompt_id` is the only identifier - fixed at creation, no renaming. Every update to `prompt` text appends to an audit-only version history; there is no rollback endpoint.

## [](#tag/Prompts/operation/create%5Fprompt%5Fprompts%5Fpost)Create Prompt 

Register a new named custom extraction prompt. `prompt_id` must be globally unique -- a duplicate, or a previously archived `prompt_id`, returns a conflict error. A previously purged `prompt_id` is genuinely gone and can be freely re-registered.

##### Authorizations:

_HTTPBearer_

##### Request Body schema: application/json

required

prompt\_id

required

string (Prompt Id) <= 128 characters ^\[a-zA-Z0-9\_-\]+$

Only letters, digits, underscores, and hyphens - avoids collision with the internal prompt:::: key encoding. Max 128 characters. Cannot be one of the reserved sentinel values: \['default'\]. 

prompt

required

string (Prompt) <= 4000 characters 

Max 4000 characters (\~1000 tokens) - keeps custom instructions well within any model's context budget alongside real block content.

description

required

string (Description) <= 200 characters 

Short, human-written summary of what this prompt is for - shown in GET /prompts list results for discoverability. No fixed template required; aim for something like the example.

annotations

Annotations (object) or Annotations (null) (Annotations) 

String key/value labels. Not versioned.

### Responses

**201** 

Successful Response

**400** 

The request was rejected before it reached the database.

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**409** 

The resource already exists, is archived, or is busy.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

post/prompts

AgentMemory server

http://{host}/prompts

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "prompt_id": "support_tickets",
* "prompt": "Focus on product issues, error codes, and resolution steps.",
* "description": "Use for support ticket extraction - focuses on product issues and resolution steps",
* "annotations": {
  * "category": "tickets",
  * "team": "support"  
}
}`

### Response samples 

* 201
* 400
* 401
* 403
* 409
* 422
* 500
* 503

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "prompt_id": "string",
* "prompt": "string",
* "description": "string",
* "annotations": {
  * "property1": "string",
  * "property2": "string"  
},
* "current_vid": 0,
* "version_count": 0,
* "last_updated_at": "string",
* "archived": false
}`

## [](#tag/Prompts/operation/list%5Fprompts%5Fprompts%5Fget)List Prompts 

List registered prompts (lean head-doc shape, no version history), paginated. Archived prompts are included, flagged via `archived`.

##### Authorizations:

_HTTPBearer_

##### query Parameters

| limit  | integer (Limit) \[ 1 .. 1000 \] Default: 100 |
| ------ | -------------------------------------------- |
| offset | integer (Offset) \>= 0 Default: 0            |

### Responses

**200** 

Successful Response

**400** 

The request was rejected before it reached the database.

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

get/prompts

AgentMemory server

http://{host}/prompts

### Response samples 

* 200
* 400
* 401
* 403
* 422
* 500
* 503

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "prompts": [
  * {
    * "prompt_id": "string",
    * "prompt": "string",
    * "description": "string",
    * "annotations": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "current_vid": 0,
    * "version_count": 0,
    * "last_updated_at": "string",
    * "archived": false  
  }  
],
* "count": 0,
* "total": 0,
* "limit": 1,
* "offset": 0
}`

## [](#tag/Prompts/operation/get%5Fprompt%5Fprompts%5F%5Fprompt%5Fid%5F%5Fget)Get Prompt 

Retrieve a prompt's current state, or (if `vid` is given) a single historical version's text along with whether it's archived and whether it's the current version. Use GET .../versions for the full history.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| prompt\_idrequired | string (Prompt Id) ^\[a-zA-Z0-9\_-\]+$ Unique identifier for the prompt |
| ------------------ | ----------------------------------------------------------------------- |

##### query Parameters

| vid | integer (Vid) \>= 0 If given, retrieve this specific version instead. |
| --- | --------------------------------------------------------------------- |

### Responses

**200** 

Successful Response

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**404** 

No such resource. The message names the id that was looked up.

**409** 

The resource already exists, is archived, or is busy.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

get/prompts/{prompt\_id}

AgentMemory server

http://{host}/prompts/{prompt\_id}

### Response samples 

* 200
* 401
* 403
* 404
* 409
* 422
* 500
* 503

Content type

application/json

Example

PromptPromptVersionPrompt

Copy

 Expand all  Collapse all 

`{
* "prompt_id": "string",
* "prompt": "string",
* "description": "string",
* "annotations": {
  * "property1": "string",
  * "property2": "string"  
},
* "current_vid": 0,
* "version_count": 0,
* "last_updated_at": "string",
* "archived": false
}`

## [](#tag/Prompts/operation/update%5Fprompt%5Fprompts%5F%5Fprompt%5Fid%5F%5Fput)Update Prompt 

Update a prompt. Providing `prompt` creates a new, immutable version; `description`/`annotations` are updated in place and never versioned. Omitting a field preserves its existing value. Returns a conflict error if the prompt has been archived.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| prompt\_idrequired | string (Prompt Id) ^\[a-zA-Z0-9\_-\]+$ Unique identifier for the prompt |
| ------------------ | ----------------------------------------------------------------------- |

##### Request Body schema: application/json

required

| prompt      | Prompt (string) or Prompt (null) (Prompt) Max 4000 characters (\~1000 tokens). Omit to preserve the existing text (no new version created).                                                   |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| description | Description (string) or Description (null) (Description) Omit to preserve the existing description. Never versioned (same as annotations) - updating it does not create a new prompt version. |
| annotations | Annotations (object) or Annotations (null) (Annotations) Replaces all annotations (no merge). Omit to keep them. Never versioned.                                                             |

### Responses

**200** 

Successful Response

**400** 

The request was rejected before it reached the database.

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**404** 

No such resource. The message names the id that was looked up.

**409** 

The resource already exists, is archived, or is busy.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

put/prompts/{prompt\_id}

AgentMemory server

http://{host}/prompts/{prompt\_id}

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "prompt": "Focus on billing disputes and refund policy exceptions.",
* "description": "Use for billing-dispute extraction - refunds and exceptions",
* "annotations": {
  * "team": "billing"  
}
}`

### Response samples 

* 200
* 400
* 401
* 403
* 404
* 409
* 422
* 500
* 503

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "prompt_id": "string",
* "prompt": "string",
* "description": "string",
* "annotations": {
  * "property1": "string",
  * "property2": "string"  
},
* "current_vid": 0,
* "version_count": 0,
* "last_updated_at": "string",
* "archived": false
}`

## [](#tag/Prompts/operation/purge%5Fprompt%5Fprompts%5F%5Fprompt%5Fid%5F%5Fdelete)Purge Prompt 

Permanently delete a prompt (`vid=all`) or a single version of it (`vid=<int>`). Irreversible. `vid=all` removes the prompt and its entire history and frees prompt\_id for re-registration; memory blocks still queued against it fall back to the default extraction behavior. `vid=<int>` removes just that one version, leaving the rest of the history untouched.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| prompt\_idrequired | string (Prompt Id) ^\[a-zA-Z0-9\_-\]+$ Unique identifier for the prompt |
| ------------------ | ----------------------------------------------------------------------- |

##### query Parameters

| vidrequired | string (Vid) "all" for the whole prompt, or a version number for just that one version. Required -- there is no default -- so a caller can never silently escalate to the wrong scope by omitting it. |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**204** 

Successful Response

**400** 

The request was rejected before it reached the database.

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**404** 

No such resource. The message names the id that was looked up.

**409** 

The resource already exists, is archived, or is busy.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

delete/prompts/{prompt\_id}

AgentMemory server

http://{host}/prompts/{prompt\_id}

### Response samples 

* 400
* 401
* 403
* 404
* 409
* 422
* 500
* 503

Content type

application/json

Copy

`{
* "error": "INVALID_REQUEST",
* "message": "Invalid request"
}`

## [](#tag/Prompts/operation/list%5Fprompt%5Fversions%5Fprompts%5F%5Fprompt%5Fid%5F%5Fversions%5Fget)List Prompt Versions 

List a prompt's version history, paginated. Each item indicates whether that specific version is archived and whether it's the current version. Returns a not-found error if prompt\_id doesn't exist.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| prompt\_idrequired | string (Prompt Id) ^\[a-zA-Z0-9\_-\]+$ Unique identifier for the prompt |
| ------------------ | ----------------------------------------------------------------------- |

##### query Parameters

| limit  | integer (Limit) \[ 1 .. 1000 \] Default: 100 |
| ------ | -------------------------------------------- |
| offset | integer (Offset) \>= 0 Default: 0            |

### Responses

**200** 

Successful Response

**400** 

The request was rejected before it reached the database.

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**404** 

No such resource. The message names the id that was looked up.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

get/prompts/{prompt\_id}/versions

AgentMemory server

http://{host}/prompts/{prompt\_id}/versions

### Response samples 

* 200
* 400
* 401
* 403
* 404
* 422
* 500
* 503

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "versions": [
  * {
    * "prompt_id": "string",
    * "vid": 0,
    * "prompt": "string",
    * "updated_at": "string",
    * "archived": false,
    * "is_current": false  
  }  
],
* "count": 0,
* "total": 0,
* "limit": 1,
* "offset": 0
}`

## [](#tag/Prompts/operation/archive%5Fprompt%5Fprompts%5F%5Fprompt%5Fid%5F%5Farchive%5Fput)Archive Prompt 

Archive a prompt (`vid=all`) or a single version of it (`vid=<int>`) without deleting it -- content and history are retained. `vid=all` blocks all new references and permanently reserves prompt\_id against reuse; `vid=<int>` blocks only new references pinned to that exact version. Anything already in progress resolves normally either way.

##### Authorizations:

_HTTPBearer_

##### path Parameters

| prompt\_idrequired | string (Prompt Id) ^\[a-zA-Z0-9\_-\]+$ Unique identifier for the prompt |
| ------------------ | ----------------------------------------------------------------------- |

##### query Parameters

| vidrequired | string (Vid) "all" for the whole prompt, or a version number for just that one version. Required -- there is no default -- so a caller can never silently escalate to the wrong scope by omitting it. |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**204** 

Successful Response

**400** 

The request was rejected before it reached the database.

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**404** 

No such resource. The message names the id that was looked up.

**409** 

The resource already exists, is archived, or is busy.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

put/prompts/{prompt\_id}/archive

AgentMemory server

http://{host}/prompts/{prompt\_id}/archive

### Response samples 

* 400
* 401
* 403
* 404
* 409
* 422
* 500
* 503

Content type

application/json

Copy

`{
* "error": "INVALID_REQUEST",
* "message": "Invalid request"
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

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

get/health/couchbase

AgentMemory server

http://{host}/health/couchbase

### Response samples 

* 200
* 401
* 403
* 500
* 503

Content type

application/json

Copy

`{
* "status": "healthy"
}`

## [](#tag/Health/operation/check%5Fmodels%5Fhealth%5Fhealth%5Fmodels%5Fget)Check Model Service Health 

Check reachability and status of the configured embedding and LLM model services. `status` is `healthy` when both models are healthy, `degraded` when either is rate limited, and `unhealthy` when either is in any other state, in which case memory routes that need that model return 503.

##### Authorizations:

_HTTPBearer_

### Responses

**200** 

Successful Response

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

get/health/models

AgentMemory server

http://{host}/health/models

### Response samples 

* 200
* 401
* 403

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

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

get/health/async-batch-processor

AgentMemory server

http://{host}/health/async-batch-processor

### Response samples 

* 200
* 401
* 403

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

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

get/health/async-batch-processor-stats

AgentMemory server

http://{host}/health/async-batch-processor-stats

### Response samples 

* 200
* 401
* 403

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

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

get/health/memory

AgentMemory server

http://{host}/health/memory

### Response samples 

* 200
* 401
* 403

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

The request was rejected before it reached the database.

**401** 

No bearer token was supplied, or the token is expired, malformed, or an ID token rather than an access token.

**403** 

The token carries no AMS role, or one below this route's minimum tier. The body names the tier the route requires.

**422** 

Request validation failed. `details.fields` lists the offending fields.

**500** 

The operation failed inside the server. Retrying will not help; quote `request_id` when reporting it. DATABASE\_ERROR carries `details` naming the bucket, scope, collection, keyspace or index that no longer exists.

**503** 

A backing service is unavailable, or the IdP cannot be reached to validate the token. Retry-After may be set.

get/logs/collect

AgentMemory server

http://{host}/logs/collect

### Response samples 

* 200
* 400
* 401
* 403
* 422
* 500
* 503

Content type

application/json

Copy

`null`