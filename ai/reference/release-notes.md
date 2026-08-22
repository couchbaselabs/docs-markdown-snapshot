---
title: Couchbase AI Data Plane Release Notes
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/reference/pages/release-notes.adoc
  xref: xref:ai:reference:release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/reference/release-notes.html)

# Couchbase AI Data Plane Release Notes

## [](#june-2026-changelog)June 2026 Changelog

* We're excited to reintroduce Couchbase AI Services, now known as the **Couchbase AI Data Plane**.  
The Couchbase AI Data Plane is a unified data infrastructure layer for your production AI agents. Use it to give your agents persistent memory, governed data access, tool and prompt visibility, and fast context retrieval across cloud, self-managed, hybrid, edge, and air-gapped environments.  
As a part of this release, the AI Data Plane is introducing new features to help solve the problem of scattered agent data through:

  * **Agent Memory**: Use Couchbase Agent Memory to get a unified, persistent memory layer for your agentic applications. Store your users' conversation history, extracted facts, and vector embeddings to improve the personalization and user experience of your agents.  
  For more information, see [Agent Memory for Persistent Memory Storage](../build/agent-memory/about-agent-mem.md).
  * **MCP Server**: Use the Couchbase Model Context Protocol (MCP) Server to let LLMs interact directly with data stored in your Couchbase clusters. Use natural language querying to explore your cluster's setup and health, data models and schemas, directly query documents, or analyze query performance.  
  For more information, see [mcp-server::intro.adoc](#mcp-server::intro.adoc).  
The Couchbase AI Data Plane also includes:

  * **Agent Catalog**: Use Couchbase Agent Catalog for a database-native, centralized catalog for all your agent components. Use it as a governed store where every tool, prompt, and piece of ground-truth data can live, evolve, and scale to simplify agent development and management.  
  For more information, see [Integrate an Agent with the Agent Catalog](../build/integrate-agent-with-catalog.md).  
Use the Couchbase AI Data Plane wherever your agents are deployed, backed by either [Couchbase Server](../../home/server.md) or [Couchbase Capella](../../home/cloud.md). The AI Data Plane on Capella still includes the [Model Service](../build/model-service/model-service.md), [AI Functions](../build/ai-functions.md), and the [Data Processing Service](../build/vectorization-service/data-processing.md).

## [](#november-2025-changelog)November 2025 Changelog

* We're excited to announce that the AI Data Plane is now available.  
Hosted with AWS, the AI Data Plane includes the following:

  * Data Processing Service  
  The Data Processing Service provides no-code, automated RAG ETL pipelines to prepare your enterprise data for agentic applications. Deploy fully managed workflows to ingest, preprocess, and vectorize unstructured data, such as PDF and DOCX, directly from your sources into a vector index.  
  Use workflows to accelerate your RAG application deployments by eliminating complex ETL development and management.  
  For more information, see [Process Your Data For the Couchbase AI Data Plane](../build/vectorization-service/data-processing.md).
  * Model Service  
  The Model Service is a managed inference service for deploying leading open source LLMs and embedding models. Available models include Llama 3, NVIDIA Nemotron, Mistral, and more.  
  Backed by NVIDIA Enterprise AI, this service delivers high performance and a low total cost of ownership (TCO). Colocate your models and data within Capella to achieve optimal response times and eliminate the security risks associated with sending data to external inference providers.  
  Value-added features include a built-in cache, content safety guardrails, and automated performance optimizations.  
  For more information, see [Deploy Models with the AI Data Plane Model Service](../build/model-service/model-service.md).
  * AI Functions  
  AI Functions are pre-built and customizable task functions that utilize LLM capabilities to extract insights directly from your data using SQL++.  
  Pre-built task functions include:

    * Sentiment analysis
    * Summarization
    * Classification
    * Entity extraction
    * Grammar correction
    * Text generation
    * PII masking
    * Similarity scoring
    * Translation  
  A flexible completion function is also available for custom use cases.  
  Run these functions using a Capella-hosted model deployed through the [Model Service](../build/model-service/model-service.md) or an external inference provider of your choice.  
  For more information, see [Use Couchbase AI Data Plane AI Functions](../build/ai-functions.md).
  * Agent Catalog  
  Agent Catalog provides a database-native, centralized catalog for all your agent components. Use it as a governed store where every tool, prompt, and piece of ground-truth data can live, evolve, and scale to simplify agent development and management.  
  For more information, see [Integrate an Agent with the Agent Catalog](../build/integrate-agent-with-catalog.md).