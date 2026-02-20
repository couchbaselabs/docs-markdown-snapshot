---
title: Capella AI Services Release Notes
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/reference/pages/release-notes.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:ai:reference:release-notes.adoc[]
---

[View original HTML](/ai/reference/release-notes.html)

# Capella AI Services Release Notes

## [](#november-2025-changelog)November 2025 Changelog

* We’re excited to announce that Capella AI Services is now available.  
Hosted with AWS, Capella AI Services includes the following:

  * Data Processing Service  
  The Data Processing Service provides no-code, automated RAG ETL pipelines to prepare your enterprise data for agentic applications. Deploy fully managed workflows to ingest, preprocess, and vectorize unstructured data, such as PDF and DOCX, directly from your sources into a vector index.  
  Use workflows to accelerate your RAG application deployments by eliminating complex ETL development and management.  
  For more information, see [Process Your Data For Capella AI Services](../build/vectorization-service/data-processing.md).
  * Model Service  
  The Model Service is a managed inference service for deploying leading open source LLMs and embedding models. Available models include Llama 3, NVIDIA Nemotron, Mistral, and more.  
  Backed by NVIDIA Enterprise AI, this service delivers high performance and a low total cost of ownership (TCO). Colocate your models and data within Capella to achieve optimal response times and eliminate the security risks associated with sending data to external inference providers.  
  Value-added features include a built-in cache, content safety guardrails, and automated performance optimizations.  
  For more information, see [Deploy Models with the Capella Model Service](../build/model-service/model-service.md).
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
  For more information, see [Use Capella AI Functions](../build/ai-functions.md).
  * Agent Catalog  
  Agent Catalog provides a database-native, centralized catalog for all your agent components. Use it as a governed store where every tool, prompt, and piece of ground-truth data can live, evolve, and scale to simplify agent development and management.  
  For more information, see [Integrate an Agent with the Agent Catalog](../build/integrate-agent-with-catalog.md).