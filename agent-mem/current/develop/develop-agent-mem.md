---
title: Develop with the Agent Memory SDK
description: Use the Couchbase Agent Memory Python SDK to add persistent memory
  to your AI agent application.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase Agent Memory
    version: "1.1"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-agentmemory/edit/release/1.1/modules/develop/pages/develop-agent-mem.adoc
  xref: xref:agent-mem:develop:develop-agent-mem.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/agent-mem/current/develop/develop-agent-mem.html)

# Develop with the Agent Memory SDK

> Use the Couchbase Agent Memory Python SDK to add persistent memory to your AI agent application. 

This page builds on the quickstart for [Managed](../get-started/get-started-agent-mem-managed.md) or [Self-Managed](../get-started/get-started-agent-mem.md) Agent Memory, and covers the SDK patterns you need for production agent applications: updating memories, cross-session search, TTL management, annotations, async processing, and framework integration.

## [](#prerequisites)Prerequisites

* You have a running Agent Memory server. For setup instructions, see [Get Started with Managed Agent Memory](../get-started/get-started-agent-mem-managed.md) or [Get Started with Self-Managed Agent Memory](../get-started/get-started-agent-mem.md).
* You have installed the [Agent Memory Python SDK](https://pypi.org/project/couchbase-agent-memory/):  
```console  
pip install couchbase-agent-memory  
```
* You have installed [Python 3.12](https://www.python.org/downloads/) or later.

## [](#initialize-the-client)Initialize the Client

Create an `AgentMemoryClient` pointing at your running server. Use it as a context manager so connections are cleaned up automatically:

* Managed
* Self-Managed

Set `base_url` to your Agent Memory server endpoint and `token` to your Agent Memory API key token:

```python
from agentmemory import AgentMemoryClient

with AgentMemoryClient(
    base_url="<your-agent-memory-endpoint>",
    token="<your-api-key-token>",
) as client:
    health = client.health_ping()
    print(f"Server status: {health.overall_status.value}")
```

You can also set the token in the `AGENTMEMORY_JWT_TOKEN` environment variable instead of passing it to the constructor. For how to get your endpoint and API key, see [Allow Access and Connect](../managed/deploy-agent-mem-managed.md#connect).

Set `base_url` to your server's URL:

```python
from agentmemory import AgentMemoryClient

with AgentMemoryClient(base_url="http://localhost:8080") as client:
    health = client.health_ping()
    print(f"Server status: {health.overall_status.value}")
```

If your server has OIDC authentication enabled, pass your JWT bearer token: `AgentMemoryClient(base_url="https://your-server", token="your-jwt-token")`. For more information, see [Configure Authentication for Self-Managed Agent Memory](../security/config-agent-mem-auth.md).

## [](#store-memory)Store Memory

Memory blocks are always scoped to a session. Create a user and session first, then add messages or facts.

> [!NOTE]
> Use 1 Agent Memory user per application user identity and 1 session per conversation or workflow run. Reusing a shared user or session across all interactions contaminates search results with unrelated memory blocks and makes per-user data lifecycle management, including TTL and deletion, impossible.

```python
from agentmemory import AgentMemoryClient, ChatMessage

with AgentMemoryClient(base_url="http://localhost:8080") as client:
    user = client.create_user(user_id="agent-1", name="Support Bot")
    session = user.create_session(session_id="conv-100")

    # Store a conversation exchange
    session.add_memory(
        messages=[
            ChatMessage(
                user_content="My order hasn't arrived.",
                assistant_content="I'll look into that. What's your order number?",
            )
        ]
    )

    # Store a standalone fact
    session.add_memory(
        facts=["Customer is in the EU timezone."]
    )
```

> [!IMPORTANT]
> Submit `messages` and `facts` in separate `add_memory()` calls. Passing both in a single call raises `ValidationError`.

> [!TIP]
> You can pass multiple `ChatMessage` or fact objects in a single `add_memory()` call. Each item is stored as its own memory block, so passing a list is equivalent to making separate calls.

### [](#backfill-historical-data)Backfill Historical Data

Pass the optional `created_at` parameter to set a timestamp on the block. This is useful when importing historical conversations where you want `order_by="created_at"` in `list_memories()` to reflect original event times rather than ingestion times:

```python
from datetime import datetime, timezone

session.add_memory(
    messages=[
        ChatMessage(
            user_content="I'd like to cancel my subscription.",
            assistant_content="I can help with that.",
        )
    ],
    created_at=datetime(2025, 1, 15, 10, 30, tzinfo=timezone.utc).isoformat(),
)
```

If `created_at` is omitted, the block inherits the server's `ingested_at` timestamp.

### [](#synchronous-vs-asynchronous-processing)Synchronous vs Asynchronous Processing

To store a memory block, you call the `add_memory()` method. Adding a block includes 2 parts:

1. Generating its embedding.
2. Extracting semantic content to populate the `context` and `summary` fields.

Embedding generation always completes before `add_memory()` returns, no matter how you call it. A block's status is `processing` until extraction finishes. Once extraction finishes, the block's status moves to `ready`, with the `context` and `summary` fields populating. Both semantic and filter-only search return a `processing` block. The block includes only its raw `message` or `fact` content, not yet its extracted `context` or `summary`.

The `add_memory()` method accepts the `async_processing` parameter, which you use to control whether extraction finishes before the call returns.

`async_processing=True` (default)

`add_memory()` returns as soon as the embedding is ready, while extraction runs in the background.

`async_processing=False`

`add_memory()` returns only when extraction finishes. You might use this for testing, or other situations where you need the extracted `context` and `summary` before continuing.

For example, the following call waits for extraction to finish before printing the new block's ID:

```python
response = session.add_memory(
    facts=["User prefers email notifications."],
    async_processing=False,  # Block until extraction is ready
)
print(f"Block IDs: {response.block_ids}")
```

### [](#asynchronous-processing-limits)Asynchronous Processing Limits

When using the default asynchronous processing mode, be aware of the following limits:

Per-block token limit

Agent Memory rejects blocks exceeding the `AGENTMEMORY_PER_REQUEST_TOKEN_LIMIT` before they enter the extraction queue. If some blocks fit, the request returns HTTP `201`, and the response includes `rejected_count` and `rejected_details` fields identifying the dropped blocks and the reason for rejection. If every block in the request exceeds the limit, the request fails with HTTP `400` and the error code `MEMORY_BLOCK_TOO_LARGE`.

Queue capacity

When the extraction queue is full, the server returns HTTP `429` with a `Retry-After` header. Wait for the indicated cooloff period before retrying.

Extraction failures

If async extraction fails after 3 retries, the block is permanently marked `extraction_failed`. Blocks in this state are still returned by search, with their raw content but no extracted `context` or `summary`. To retry a permanently failed block, use the update endpoint with `async_processing=True`. Track permanent failures with the `agentmemory_async_batch_permanent_failures_total` server metric. On server restart, blocks with a `fail_count` less than `3` are automatically re-queued for extraction.

## [](#customize-extraction-with-prompts)Customize Extraction with Prompts

By default, `add_memory()` extracts and summarizes every block with the same fixed system prompt. Register a named prompt and reference it by `prompt_id` to steer what gets extracted for a specific use case, without changing the output structure:

```python
from agentmemory import ChatMessage

client.create_prompt(
    prompt_id="support_tickets",
    prompt="Focus on product issues, error codes, and resolution steps.",
    description="Use for support ticket extraction, focusing on product issues and resolution steps",
)

session.add_memory(
    messages=[
        ChatMessage(
            user_content="My order #123 hasn't shipped.",
            assistant_content="I'll look into that.",
        )
    ],
    prompt_id="support_tickets",
)
```

For more information about prompts, including registering, updating, pinning to a specific version, and archiving or purging a prompt, see [Customize Extraction and Summarization Prompts](customize-prompts-agent-mem.md).

## [](#search-memory)Search Memory

Use `search_memory()` to retrieve memory blocks from a session.

When you pass a `query`, the server embeds the query text and returns blocks ranked by semantic similarity, which is useful for surfacing relevant context before an agent responds. Semantic search returns at most `relevant_k` results (default `10`) with no pagination; to retrieve more blocks, pass `relevant_k` in `filters`.

When you omit `query`, the server runs a SQL++ lookup and returns matching blocks ordered newest-first, up to `relevant_k` (default `10`). You can use this for auditing stored memory, exporting a session's history, or feeding recent blocks into a prompt. To retrieve more, raise `relevant_k` in `filters`, or use `list_memories()` for paginated retrieval beyond that cap.

Both modes require the embedding service to be healthy. If the embedding service is unavailable, all `search_memory()` calls return HTTP `503`, including filter-only searches. Use `list_memories()` instead when you need retrieval that does not depend on the embedding service.

```python
# Semantic search — returns blocks ranked by relevance
results = session.search_memory(query="shipping delay")

# Unranked retrieval — returns all blocks in the current session
results = session.search_memory()
```

### [](#search-the-current-session)Search the Current Session

By default, search is scoped to the session you call it on:

```python
results = session.search_memory(query="shipping delay")

for block in results.memory_blocks:
    if block.fact:
        print(f"Fact: {block.fact} (score: {block.rel_score:.3f})")
    elif block.message:
        print(f"User: {block.message.user_content}")
```

### [](#search-across-all-sessions)Search Across All Sessions

> [!TIP]
> Cross-session search scans a larger corpus, which costs more and takes longer. Use it only when you need longitudinal context, such as tracking user preferences across all their conversations. When you use it, set `relevant_k` to the number of blocks you can fit in your downstream context window, not the API maximum.

Set `session_ids` to `"all"` to search every session belonging to a user:

```python
results = session.search_memory(
    query="payment preferences",
    filters={"session_ids": "all", "relevant_k": 20}
)
```

### [](#search-specific-sessions)Search Specific Sessions

Pass a list of session IDs to narrow the scope:

```python
results = session.search_memory(
    query="billing",
    filters={
        "session_ids": ["conv-100", "conv-101"],
        "annotations": {"topic": "payments"},
    }
)
```

### [](#search-by-custom-prompt)Search by Custom Prompt

Pass `prompt_id` (optionally with `prompt_vid`) in `filters` to restrict results to blocks extracted with a specific registered prompt:

```python
from libs.modules.dataclasses import FilterOptions

resp = session.get_memory(
    query="shipping delay",
    filters=FilterOptions(prompt_id="support_tickets"),
)
blocks = resp.memory_blocks if resp else []
    query="shipping delay",
    filters={"prompt_id": "support_tickets"},
)
```

In semantic search, this filter is applied after the top-`relevant_k` ranking cut, so a matching block that ranks outside `relevant_k` is not returned.

## [](#update-memory)Update Memory

To update an existing block's content, annotations, or TTL, the block must be in `ready` status. Calling `update_memory()` on a block still in `processing` raises an error. If you need to update a block immediately after creating it, add it with `async_processing=False` so it reaches `ready` first.

When you update `message` or `fact` content, the server regenerates the embedding and summary.

```python
# Update a fact and reset its TTL
resp = session.update_memory(
    block_id="block_abc",
    fact="Customer upgraded to premium plan.",
    annotations={"importance": "high"},
    memory_block_ttl=0,  # Make permanent
)
print(resp.block.fact)
```

> [!NOTE]
> Every `update_memory()` call must include at least 1 of `message`, `fact`, `annotations`, or `memory_block_ttl`. To update TTL on a single block without changing its content, pass only `memory_block_ttl`. `user.modify_ttl()` is a separate bulk operation that sets TTL across all blocks belonging to a user. For more information, see [Manage TTL](#manage-ttl).

> [!NOTE]
> Providing `annotations` replaces the block's entire annotation set, so include every key you want kept. Omit the parameter to leave existing annotations untouched.

> [!IMPORTANT]
> A block's content type is fixed at creation. You cannot update a fact block with a message payload, or vice versa.

## [](#manage-ttl)Manage TTL

Memory blocks can expire automatically. Set TTL at different levels:

* Per block: pass the `memory_block_ttl` (seconds) SDK parameter to `add_memory()` or `update_memory()`.
* Per session: pass the `memory_blocks_ttl` SDK parameter when creating a session. New blocks in that session inherit this TTL.
* Globally: configure the `AGENTMEMORY_MEMORY_BLOCK_TTL` environment variable on the server. For more information, see [Self-Managed Agent Memory Environment Variable Reference](../reference/config-agent-mem-env.md).

A value of `0` means no expiry. A block-level TTL overrides a session-level TTL, which overrides the global default.

```python
# Session where all blocks expire after 24 hours
session = user.create_session(
    session_id="ephemeral-session",
    memory_blocks_ttl=86400
)

# Override: make a specific block permanent
session.add_memory(
    facts=["Critical account note — do not expire."],
    memory_block_ttl=0,
)
```

You can also bulk-modify TTL for an existing user's blocks:

```python
# Change TTL for all blocks belonging to a user
user.modify_ttl(new_ttl=3600)

# Change TTL for blocks in a specific session
user.modify_ttl(new_ttl=3600, session_id="conv-100")

# Change TTL for specific blocks
user.modify_ttl(new_ttl=0, session_id="conv-100", block_ids=["block_1", "block_2"])
```

## [](#use-annotations)Use Annotations

You can add key-value annotations to sessions and to individual blocks. Block annotations are searchable. You can use them to filter search results or partition memory by intent, channel, or any other dimension. Session annotations are metadata on the session document only. They're not searched, and they're not copied onto blocks you add to that session.

> [!TIP]
> Define a small, consistent vocabulary of annotation keys at design time. Each distinct annotation key becomes a field in the Search index, so reuse this vocabulary instead of minting a new key per record. For example, `topic`, `source`, `importance`, or `locale`, set at ingestion. Annotation keys must contain only letters, digits, and underscores, and cannot start with a digit. Any other key is rejected with HTTP `422`. Annotation matching is an exact, case-sensitive string comparison, not semantic. Inconsistent or free-text values produce inconsistent search results.

```python
# Annotate a session using a consistent key vocabulary
session = user.create_session(
    session_id="conv-200",
    annotations={"topic": "onboarding", "source": "web"},
)

# Annotate individual blocks
session.add_memory(
    facts=["User completed onboarding."],
    annotations={"importance": "high", "locale": "en-US"},
)

# Filter search by annotation
results = session.search_memory(
    query="onboarding status",
    filters={"session_ids": "all", "annotations": {"importance": "high"}},
)
```

An `annotations` filter with multiple keys matches only blocks that satisfy every key. There's no OR form. For example, the following filter matches only blocks tagged with both `kind` and `env`:

```python
# Semantic search restricted to annotation matches
results = session.search_memory(
    query="pipeline failure",
    filters={
        "annotations": {"kind": "iac-change", "env": "prod"},
    },
)
```

### [](#control-annotation-filter-timing-in-semantic-search)Control Annotation Filter Timing in Semantic Search

In semantic search, `annotation_filter_mode` controls when the annotation filter applies relative to the relevance ranking. It has no effect unless you pass a `query` string to `search_memory()`.

`annotation_filter_mode` can have 1 of the following values:

`pre` (default)

Annotations pre-filter the candidate pool, restricting it before the search selects the top `relevant_k` results. The search still returns a matching block even if it ranks below `relevant_k` non-matching blocks.

`post`

Annotations post-filter the results, applying after the search selects the top `relevant_k`. The search selects the top `relevant_k` blocks first, so a matching block that ranks outside that set is already gone before the filter applies, and the search can return fewer than the matching blocks, or none.

For example, the following filter opts into the legacy `post` behavior:

```python
# Filter after the top-k cut instead of before it
results = session.search_memory(
    query="pipeline failure",
    filters={
        "annotations": {"kind": "iac-change"},
        "annotation_filter_mode": "post",
    },
)
```

Pre-filtering relies on the Search index. Annotation values larger than a few KB can exceed the index term limit and are excluded from pre-filtering. If you need to filter on values that large, set `annotation_filter_mode="post"`: post-filtering runs a plain SQL++ comparison and is not subject to the index term limit.

## [](#list-and-paginate-memories)List and Paginate Memories

Use `list_memories()` for deterministic, paginated retrieval without a search query:

```python
# List blocks in a session
page = session.list_memories(limit=50, offset=0, order_by="created_at")
print(f"Page: {page.count} of {page.total} blocks")

# List blocks across all sessions for a user
all_blocks = user.list_memories(limit=200)
```

`limit` accepts `1` to `200`. `order_by` accepts `"ingested_at"` (default) or `"created_at"`. When ordering by `"created_at"`, blocks ingested without an explicit `created_at` value sort last.

## [](#delete-memory)Delete Memory

```python
# Delete specific blocks
session.delete_memory(block_ids=["block_1", "block_2"])

# Delete all blocks in a session
session.delete_memory(block_ids="all")
```

Deleting a session or user cascades to all associated memory blocks.

## [](#use-the-async-client)Use the Async Client

For [asyncio](https://docs.python.org/3/library/asyncio.html)\-based applications, use `AsyncAgentMemoryClient`. It has the same API surface as the synchronous client:

```python
import asyncio
from agentmemory import AsyncAgentMemoryClient, ChatMessage

async def main():
    async with AsyncAgentMemoryClient(base_url="http://localhost:8080") as client:
        user = await client.create_user("agent-2", "Async Bot")
        session = await user.create_session("async-session-1")

        await session.add_memory(
            messages=[
                ChatMessage(
                    user_content="Hello",
                    assistant_content="Hi! How can I help?",
                )
            ]
        )

        results = await session.search_memory(query="greeting")
        for block in results.memory_blocks:
            print(block.message.assistant_content)

        await session.end()

asyncio.run(main())
```

> [!NOTE]
> Concurrent writes of different memory blocks to the same session, from multiple application instances, are safe, as Couchbase handles document-level atomicity. Read-modify-write operations on session annotations are not atomic at the API level. If 2 instances each read a session's annotations and append a key, 1 update can overwrite the other. Serialize these operations at the application layer using a single writer, a queue, or a distributed lock.

## [](#handle-errors)Handle Errors

The SDK raises typed exceptions that map to specific error categories, so you can decide whether to retry before acting.

| Category                 | Exception                                                                       | Strategy                                                                                                                                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Transient infrastructure | ServiceUnavailableError (database), UpstreamError (model service), TimeoutError | Retry with exponential backoff and jitter, capped at a reasonable ceiling.                                                                                                                                                        |
| Capacity                 | RateLimitError (429), ServiceUnavailableError (memory pressure, 503)            | Honor e.retry\_after before retrying. Do not retry immediately.                                                                                                                                                                   |
| Bad request              | ValidationError                                                                 | Do not retry. Fix the request.                                                                                                                                                                                                    |
| Logical error            | NotFoundError, ConflictError                                                    | Do not retry. Fix the application logic.                                                                                                                                                                                          |
| Authentication           | AuthenticationError                                                             | Do not retry. Obtain a fresh token or correct credentials. On Managed Agent Memory, every authentication failure returns the error code INVALID\_TOKEN, including an expired or deleted API key, or a key for a different server. |
| Authorization            | AuthorizationError                                                              | Do not retry. Use a token or API key with a higher role or access level.                                                                                                                                                          |

## [](#integrate-with-agent-frameworks)Integrate with Agent Frameworks

The SDK ships ready-made notebook examples for popular agent frameworks. Each builds a travel assistant that persists memory across conversations.

| Framework                                        | Description                                                         |
| ------------------------------------------------ | ------------------------------------------------------------------- |
| [LangGraph](https://www.langchain.com/langgraph) | Stateful graph-based agent with cross-session memory recall.        |
| [CrewAI](https://crewai.com/)                    | Multi-agent crew where each agent shares a persistent memory layer. |
| [LlamaIndex](https://www.llamaindex.ai/)         | RAG agent backed by Agent Memory for context retrieval.             |
| [Strands Agents](https://strandsagents.com/)     | Tool-use agent with memory-backed conversation continuity.          |

Notebooks for the frameworks shown in the table are available in the SDK repository under `examples/notebooks/`.

The core pattern is the same regardless of framework:

1. Initialize an `AgentMemoryClient` pointing at your server.
2. On each agent turn, call `session.search_memory()` to retrieve relevant context and inject it into the prompt.
3. After each turn, call `session.add_memory()` to persist the exchange.

## [](#next-steps)Next Steps

* [Customize Extraction and Summarization Prompts](customize-prompts-agent-mem.md)
* [Deploy Managed Agent Memory](../managed/deploy-agent-mem-managed.md)
* [Control Access to Managed Agent Memory](../managed/access-agent-mem-managed.md)
* [Monitor Managed Agent Memory](../managed/monitor-agent-mem-managed.md)
* [Deploy Self-Managed Agent Memory for Production](../self-managed/deploy-agent-mem-prod.md)
* [Self-Managed Agent Memory Environment Variable Reference](../reference/config-agent-mem-env.md)
* [Configure Authentication for Self-Managed Agent Memory](../security/config-agent-mem-auth.md)