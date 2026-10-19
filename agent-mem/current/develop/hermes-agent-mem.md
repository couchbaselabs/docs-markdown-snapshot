---
title: Agent Memory Plug-in for Hermes Agent
description: The Agent Memory plug-in adds persistent, semantic memory to Hermes
  Agent, recalling and capturing context automatically.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase Agent Memory
    version: "1.1"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-agentmemory/edit/release/1.1/modules/develop/pages/hermes-agent-mem.adoc
  xref: xref:agent-mem:develop:hermes-agent-mem.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/agent-mem/current/develop/hermes-agent-mem.html)

# Agent Memory Plug-in for Hermes Agent

> The Agent Memory plug-in adds persistent, semantic memory to Hermes Agent, recalling and capturing context automatically. 

[Hermes Agent](https://github.com/NousResearch/hermes-agent) is an open source autonomous AI agent built by Nous Research. Hermes' pluggable memory system lets you add Couchbase Agent Memory as a memory provider through the Couchbase Agent Memory plug-in. Once connected, the plug-in recalls and injects relevant memories into every turn and captures each exchange in the background, without slowing down Hermes. Captured exchanges go to your own Agent Memory server, not a third-party service.

To install the Agent Memory Plug-in for Hermes, see [Install the Agent Memory Plug-in for Hermes](install-hermes-agent-mem.md).

## [](#why-use-agent-memory-with-hermes)Why Use Agent Memory with Hermes?

Hermes has a built-in memory tool that saves notes to `MEMORY.md` and `USER.md`. It only captures what the model decides is worth saving, and those files are limited in size. For example, if you mention that your team calls your staging environment `preprod`, the model may not recognize it as worth saving. When the conversation ends, this information is gone.

The Agent Memory plug-in solves this with a persistent, semantic memory layer that captures every turn. In a later conversation about something else, you can ask Hermes about the staging environment, and it still calls it `preprod`. You never have to repeat it or paste the context back in.

## [](#the-memory-loop)The Memory Loop

The plug-in works at 3 points in every turn:

### [](#1-before-the-turn)1\. Before the Turn

When you send a message, Hermes uses the plug-in to recall memories relevant to the upcoming turn in the background and adds them to the context for that turn. With these memories, Hermes has the context it needs without the model calling any tool. Should the prefetch take too long, the conversation continues with the model able to call the search tool during the turn.

### [](#2-during-the-turn)2\. During the Turn

When the model responds, it can call the plug-in's tools to search, add, update, delete, or list memories directly. For more information about these tools, see [Tools Exposed to the Model](#tools).

> [!NOTE]
> Both automatic recall and tools are on for every turn.

### [](#3-after-the-turn)3\. After the Turn

After the model responds, the plug-in captures the exchange by sending it to Agent Memory in the background, without blocking the next turn. From this exchange, Agent Memory extracts facts, generates embeddings, and summarizes it. An extracted fact might be `user resides in London` or `user prefers Python`. The exchange can be recalled on the next turn. The extracted facts can be recalled once processing finishes, typically within seconds.

## [](#hermes-sessions)Hermes Sessions

Hermes sessions map directly onto Agent Memory sessions:

* Ending a Hermes session, either by running `/reset` or exiting the command-line interface (CLI), ends the corresponding Agent Memory session.
* `/resume` and `/branch` continue the correct Agent Memory session, and resuming a conversation whose session was already ended continues it under a new, linked session.
* By default, a search spans all of a user's sessions.

## [](#annotations)Annotations

The plug-in automatically annotates every memory it writes with context from Hermes:

| Annotation    | Values                                                                          | Meaning                                                                                                                         |
| ------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| source        | turn, agent                                                                     | turn marks an automatically captured conversation turn, and agent marks a fact the model stored explicitly through a tool call. |
| platform      | cli, or a gateway name such as telegram, discord, whatsapp, signal, api\_server | The Hermes surface the message arrived on.                                                                                      |
| agent         | profile name                                                                    | The active Hermes profile.                                                                                                      |
| user\_name    | free-form                                                                       | The sender's display name, as reported by the gateway.                                                                          |
| channel\_id   | free-form                                                                       | The gateway's chat or channel identifier.                                                                                       |
| channel\_type | dm, group, forum, channel, thread                                               | The kind of chat, as reported by the gateway.                                                                                   |

An annotation appears only when Hermes provides it, so a plain CLI chat typically carries only `platform`, `agent`, and `source`.

For more information, see [Narrow Recall for Every Search](install-hermes-agent-mem.md#annotations-and-recall-scoping).

## [](#hermes-built-in-memory)Hermes' Built-in Memory

Hermes uses a [built-in memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory) that stays active by default, and installing the Agent Memory plug-in does not automatically turn it off.

Running both systems together, the model can keep saving facts to the built-in memory it already knows, so those facts never reach Agent Memory. To have a single source of truth, you can turn off Hermes' built-in memory.

For more information, see [Install and Activate](install-hermes-agent-mem.md#install).

## [](#multi-user-support)Multi-User Support with Hermes Profiles

Hermes identifies the active user with a single `user_id`, but changing that value alone is not enough to isolate 2 people on the same machine. Hermes' built-in memory ties to the active Hermes profile, not to the plug-in's `user_id`. If you only switch the `user_id`, one person's built-in notes can leak into another person's conversations. Turning off built-in memory does not fix this either. Hermes also keeps session transcripts, `/resume`, and session search scoped per profile, and those cannot be disabled.

To run Hermes and maintain separation between people on a single machine, add 1 Hermes profile per person. A new profile is a fully separate home directory. It starts with no model configuration and no plug-in installed, so you need to set up both again for each profile.

For more information, see [Running Multiple Users](install-hermes-agent-mem.md#running-multiple-users).

## [](#tools)Tools Exposed to the Model

The Agent Memory plug-in provides the following tools to the model:

| Tool                | Arguments                                                                                                                                                                                                                | Purpose                                                                                                                                                                                        |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| agentmemory\_search | query, top\_k (default 10), since (optional recency window, for example 24h, 7d, 2w, 3mo), plus the optional recall facets described in [Narrow Recall for a Single Search](install-hermes-agent-mem.md#per-call-facets) | Semantically search the user's memory, optionally narrowed by recency or facet.                                                                                                                |
| agentmemory\_add    | content                                                                                                                                                                                                                  | Store a fact verbatim.                                                                                                                                                                         |
| agentmemory\_update | block\_id, content                                                                                                                                                                                                       | Replace a memory's content. If the memory's original session has already ended, this moves the content to a new block and returns its block\_id. Use that new block\_id for any further edits. |
| agentmemory\_delete | block\_id                                                                                                                                                                                                                | Delete a memory.                                                                                                                                                                               |
| agentmemory\_list   | limit (default 20, maximum 200)                                                                                                                                                                                          | List stored memories, most recent first.                                                                                                                                                       |

## [](#see-also)See Also

* [Install the Agent Memory Plug-in for Hermes](install-hermes-agent-mem.md)
* [Develop with the Agent Memory SDK](develop-agent-mem.md)
* [Agent Memory for Persistent Memory Storage](../about-agent-mem.md)