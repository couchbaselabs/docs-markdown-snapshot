---
title: Develop with the Agent Memory SDK
description: Use the Couchbase Agent Memory Python SDK to add persistent memory
  to your AI agent application.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/build/pages/agent-memory/develop-agent-mem.adoc
pubDate: 2026-07-20T13:54:32.914Z
link: xref:ai:build:agent-memory/develop-agent-mem.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/build/agent-memory/develop-agent-mem.html)

# Develop with the Agent Memory SDK

> Use the Couchbase Agent Memory Python SDK to add persistent memory to your AI agent application. 

This page builds on the quickstart in [Get Started with Agent Memory](get-started-agent-mem.md) and covers the SDK patterns you need for production agent applications: updating memories, cross-session search, TTL management, annotations, async processing, and framework integration.

## [](#prerequisites)Prerequisites

* You have a running Agent Memory server. For setup instructions, see [Get Started with Agent Memory](get-started-agent-mem.md) or [Deploy Agent Memory for Production](deploy-agent-mem-prod.md).
* You have installed the [Agent Memory Python SDK](https://pypi.org/project/couchbase-agent-memory/):  
```console  
pip install couchbase-agent-memory  
```
* You have installed [Python 3.12](https://www.python.org/downloads/) or later.

## [](#initialize-the-client)Initialize the Client

Create an `AgentMemoryClient` pointing at your running server. Use it as a context manager so connections are cleaned up automatically:

```python
from agentmemory import AgentMemoryClient

with AgentMemoryClient(base_url="http://localhost:8080") as client:
    health = client.health_ping()
    print(f"Server status: {health.overall_status.value}")
```

> [!NOTE]
> If your server has OIDC authentication enabled, pass your JWT bearer token: `AgentMemoryClient(base_url="https://your-server", token="your-jwt-token")`. For more information, see [Configure Agent Memory Authentication](config-agent-mem-auth.md).

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
    created_at=datetime(2025, 1, 15, 10, 30, tzinfo=timezone.utc),
)
```

If `created_at` is omitted, the block inherits the server's `ingested_at` timestamp.

### [](#synchronous-vs-asynchronous-processing)Synchronous vs Asynchronous Processing

By default, `add_memory()` uses `async_processing=True` and returns immediately while embedding generation runs in the background. Agent Memory stores blocks at once, making them readable as soon as the call returns, but they do not appear in search results until their status reaches `ready`.

To wait until embeddings are ready before the call returns, for example in tests or when you need to search right after writing, set `async_processing=False`:

```python
response = session.add_memory(
    facts=["User prefers email notifications."],
    async_processing=False,  # Block until embedding is ready
)
print(f"Block IDs: {response.block_ids}")
```

### [](#asynchronous-processing-limits)Asynchronous Processing Limits

When using the default asynchronous processing mode, be aware of the following limits:

Per-block token limit

Agent Memory rejects blocks exceeding the `AGENTMEMORY_PER_REQUEST_TOKEN_LIMIT` before they enter the extraction queue. The request still returns HTTP `201`, but the response includes `rejected_count` and `rejected_details` fields identifying the dropped blocks and the reason for rejection.

Queue capacity

When the extraction queue is full, the server returns HTTP `429` with a `Retry-After` header. Wait for the indicated cooloff period before retrying.

Extraction failures

If async extraction fails after 3 retries, the block is permanently marked `extraction_failed`. Blocks in this state are stored but excluded from semantic search results. To retry a permanently failed block, use the update endpoint with `async_processing=True`. Track permanent failures with the `agentmemory_async_batch_permanent_failures_total` server metric. On server restart, blocks with a `fail_count` less than `3` are automatically re-queued for extraction.

## [](#search-memory)Search Memory

Use `search_memory()` to retrieve memory blocks from a session.

When you pass a `query`, the server embeds the query text and returns blocks ranked by semantic similarity, which is useful for surfacing relevant context before an agent responds. Semantic search returns at most `relevant_k` results (default `10`) with no pagination; to retrieve more blocks, pass `relevant_k` in `filters`.

When you omit `query`, the server runs a SQL++ lookup and returns all matching blocks unranked. You can use this for auditing stored memory, exporting a session's history, or feeding all blocks into a prompt. Filter-only searches are not subject to the `relevant_k` cap.

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
> A block's content type is fixed at creation. You cannot update a fact block with a message payload, or vice versa.

## [](#manage-ttl)Manage TTL

Memory blocks can expire automatically. Set TTL at different levels:

* Per block: pass the `memory_block_ttl` (seconds) SDK parameter to `add_memory()` or `update_memory()`.
* Per session: pass the `memory_blocks_ttl` SDK parameter when creating a session. New blocks in that session inherit this TTL.
* Globally: configure the `AGENTMEMORY_MEMORY_BLOCK_TTL` environment variable on the server. For more information, see [Agent Memory Environment Variable Reference](config-agent-mem-env.md).

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

Annotations are searchable key-value tags you can add to sessions and blocks. Use them to filter search results or partition memory by intent, channel, or any other dimension.

> [!TIP]
> Define a small, consistent vocabulary of annotation keys at design time. For example, `topic`, `source`, `importance`, or `locale` and set them at ingestion. Annotation keys cannot contain hyphens (`-`), dots (`.`), or spaces. Annotation matching is exact string comparison, not semantic. Inconsistent or free-text values produce inconsistent search results.

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
    filters={"session_ids": "all", "annotations": {"topic": "onboarding"}},
)
```

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

| Category                 | Exception                                                                       | Strategy                                                                   |
| ------------------------ | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Transient infrastructure | ServiceUnavailableError (database), UpstreamError (model service), TimeoutError | Retry with exponential backoff and jitter, capped at a reasonable ceiling. |
| Capacity                 | RateLimitError (429), ServiceUnavailableError (memory pressure, 503)            | Honor e.retry\_after before retrying. Do not retry immediately.            |
| Bad request              | ValidationError                                                                 | Do not retry. Fix the request.                                             |
| Logical error            | NotFoundError, ConflictError                                                    | Do not retry. Fix the application logic.                                   |
| Authentication           | AuthenticationError                                                             | Do not retry. Obtain a fresh token or correct credentials.                 |

> [!TIP]
> For the complete request and response schemas for every endpoint, see the interactive API reference at `/docs` on your running server.

## [](#integrate-with-agent-frameworks)Integrate with Agent Frameworks

The SDK ships ready-made notebook examples for popular agent frameworks. Each builds a travel assistant that persists memory across conversations.

| Framework                                        | Description                                                         |
| ------------------------------------------------ | ------------------------------------------------------------------- |
| [LangGraph](https://www.langchain.com/langgraph) | Stateful graph-based agent with cross-session memory recall.        |
| [CrewAI](https://crewai.com/)                    | Multi-agent crew where each agent shares a persistent memory layer. |
| [LlamaIndex](https://www.llamaindex.ai/)         | RAG agent backed by Agent Memory for context retrieval.             |
| [Strands Agents](https://strandsagents.com/)     | Tool-use agent with memory-backed conversation continuity.          |

Notebooks are available in the SDK repository under `examples/notebooks/`.

The core pattern is the same regardless of framework:

1. Initialize an `AgentMemoryClient` pointing at your server.
2. On each agent turn, call `session.search_memory()` to retrieve relevant context and inject it into the prompt.
3. After each turn, call `session.add_memory()` to persist the exchange.

## [](#next-steps)Next Steps

* [Deploy Agent Memory for Production](deploy-agent-mem-prod.md)
* [Agent Memory Environment Variable Reference](config-agent-mem-env.md)
* [Configure Agent Memory Authentication](config-agent-mem-auth.md)