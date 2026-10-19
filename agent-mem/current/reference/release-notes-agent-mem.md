---
title: Agent Memory Release Notes
description: New features and changes in Couchbase Agent Memory for Managed and
  Self-Managed Agent Memory.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase Agent Memory
    version: "1.1"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-agentmemory/edit/release/1.1/modules/reference/pages/release-notes-agent-mem.adoc
  xref: xref:agent-mem:reference:release-notes-agent-mem.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/agent-mem/current/reference/release-notes-agent-mem.html)

# Agent Memory Release Notes

> New features and changes in Couchbase Agent Memory for Managed and Self-Managed Agent Memory. 

For changes to the Agent Memory API and the Capella Management API, see the API change logs for [Managed Agent Memory](../api-guide/managed/api-log.md) and [Self-Managed Agent Memory](../api-guide/self-managed/api-log.md).

## [](#october-2026)October 2026

### [](#october-2026-managed)Managed Agent Memory

Capella now offers a fully managed Agent Memory server, so AI agents can store and recall what users told them across sessions. Agent Memory extracts facts, embeds them, and makes them semantically searchable in your Capella operational cluster, with no memory infrastructure for you to host or maintain.

With Managed Agent Memory, you can:

* Deploy an Agent Memory server from the Capella UI or the Management API. For more information, see [Deploy Managed Agent Memory](../managed/deploy-agent-mem-managed.md).
* Authenticate with Agent Memory API keys, and allow requests from specific IP addresses. For more information, see [Control Access to Managed Agent Memory](../managed/access-agent-mem-managed.md).
* Monitor your server on a dashboard in Capella, and receive alerts through your existing Capella alert integrations. For more information, see [Monitor Managed Agent Memory](../managed/monitor-agent-mem-managed.md).

Managed Agent Memory is available on AWS in the US East (N. Virginia) and Europe (London) regions.

Managed Agent Memory runs Agent Memory 1.1.0 and includes all of its features. For more information, see [Agent Memory 1.1.0](#october-2026-release-1-1).

### [](#october-2026-release-1-1)Agent Memory 1.1.0

Agent Memory 1.1.0 is available for Self-Managed Agent Memory and adds the following features:

Multi-node scaling

Agent Memory can now run on multiple nodes, with automatic recovery if a node fails. For more information, see [Cluster Mode](../about-agent-mem.md#cluster-mode).

Annotation-based filtering

Agents can scope recall to a tenant, source, or channel. For more information, see [Use Annotations](../develop/develop-agent-mem.md#use-annotations).

Custom extraction prompts

Register your own extraction prompts to steer what each agent remembers. For more information, see [Customize Extraction and Summarization Prompts](../develop/customize-prompts-agent-mem.md).

Separate administrator and application roles

Give your agents only the access they need to store and search memory, and reserve administrative operations, such as managing custom prompts, for administrators. On Self-Managed Agent Memory, you assign roles through your identity provider. On Managed Agent Memory, you choose an access level for each API key. For more information, see [Configure RBAC for Self-Managed Agent Memory](../security/config-agent-mem-rbac.md) and [Control Access to Managed Agent Memory](../managed/access-agent-mem-managed.md).

Memory provider for Hermes Agent

You can now use Agent Memory as a memory provider for Hermes Agent. For more information, see [Agent Memory Plug-in for Hermes Agent](../develop/hermes-agent-mem.md).

## [](#june-2026)June 2026

### [](#june-2026-release-1-0)Agent Memory 1.0

Self-Managed Agent Memory is now available. Agent Memory gives your agents a persistent memory layer that stores conversation history, extracted facts, and vector embeddings in a Couchbase cluster.

For more information, see [Agent Memory for Persistent Memory Storage](../about-agent-mem.md).