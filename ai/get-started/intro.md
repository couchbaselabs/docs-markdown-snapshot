---
title: Couchbase AI Data Plane
description: The Couchbase AI Data Plane provides you with the tools to create,
  organize, and manage your agentic applications and data in a unified
  environment. Choose between self-managed deployments for use with Couchbase
  Server Enterprise Edition or fully managed solutions integrated with Couchbase
  Capella.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/get-started/pages/intro.adoc
pubDate: 2026-08-07T05:05:42.965Z
link: xref:ai:get-started:intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/get-started/intro.html)

# Couchbase AI Data Plane

# Couchbase AI Data Plane

The Couchbase AI Data Plane provides you with the tools to create, organize, and manage your agentic applications and data in a unified environment. Choose between self-managed deployments for use with [Couchbase Server Enterprise Edition](#server:get-started:why-couchbase.adoc) or fully managed solutions integrated with [Couchbase Capella](#cloud:get-started:intro.adc).

Get enterprise support by [licensing Couchbase AI Data Plane](https://www.couchbase.com/downloads/?family=ai-data-plane), and get access and support for [Couchbase Agent Memory](../build/agent-memory/about-agent-mem.md), [Couchbase Agent Catalog](../build/integrate-agent-with-catalog.md) and [Couchbase MCP Server](../../mcp-server/intro.md).

## Core Features

###  Model Service

Enterprise Support Only

Deploy and manage Large Language Models (LLMs) and embedding models in Capella to power your AI-driven applications. Or [bring your own model](../admin/manage-ai-integrations.md) using the provided OpenAI and Bedrock integrations.

[Learn more](../build/model-service/model-service.md)

###  Agent Catalog

Govern your agentic app development with the Couchbase Agent Catalog to help manage tools and prompts for your own custom AI agents, using your preferred Large Language Model (LLM) and agent framework.

[Learn more](../build/integrate-agent-with-catalog.md)

###  Agent Memory

Enterprise Support Only

Couchbase Agent Memory provides a unified, persistent memory layer for agentic applications. It allows secure storage and retrieval of information specific to each user, helping to maintain context across user sessions.

[Learn more](../build/agent-memory/about-agent-mem.md)

###  AI Functions

Use AI Functions to summarize text, classify content, detect sentiment, explain patterns, and more — all within your SQL++ queries.

[Learn more](../build/ai-functions.md)

###  MCP Server

Couchbase MCP Server is a Model Context Protocol (MCP) server implementation that lets LLMs directly interact with data stored in Couchbase clusters through a rich set of tools.

[Learn more](../../mcp-server/intro.md)

###  Data Processing Service

Enterprise Support Only

Use the Data Processing Service to vectorize your structured and unstructured data for use with other AI Data Plane features. Vectorize your [structured](../build/vectorization-service/vectorize-structured-data-capella.md) and [unstructured data](../build/vectorization-service/vectorize-unstructured-data.md).

## Start Building

###  Host an AI Model in the Couchbase AI Data Plane

Deploy an [embedding model](../build/model-service/deploy-embed-model.md) or [LLM](../build/model-service/deploy-llm-model.md) alongside your data.

###  Couchbase AI Data Plane Workflows

Use Couchbase AI Data Plane Workflows to prepare, process, and vectorize text for use with other AI Data Plane features. [Learn more](../build/vectorization-service/data-processing.md)

###  Build an Agent

Create an [agentic app](../agent-tutorial/about-agentic-app.md) using the [Agent Catalog](../build/integrate-agent-with-catalog.md) and use [Agent Tracer](../build/agent-tracer/agent-tracer.md) to monitor and observe agent activity.

###  Use the Couchbase AI Data Plane APIs

[Manage deployments with AI Data Plane APIs](../api-guide/api-intro.md).