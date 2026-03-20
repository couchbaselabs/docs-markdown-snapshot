---
title: Configure LLM Value Adds
description: Use Value Adds features to help you enhance the capabilities of
  your large language models (LLMs).
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/build/pages/model-service/configure-value-adds.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:ai:build:model-service/configure-value-adds.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/build/model-service/configure-value-adds.html)

# Configure LLM Value Adds

> Use Value Adds features to help you enhance the capabilities of your large language models (LLMs). 

The following Value Adds features are available when deploying large language models (LLMs) on the Capella Model Service:

* [Caching](#caching)
* [Async Processing](#async-processing)
* [Keyword Filtering](#keyword-filtering)

## [](#caching)Caching

When deploying a Capella-hosted LLM, you have caching options. Caching stores common prompt-response pairs in a Capella operational cluster. The model retrieves these pairs using exact or semantic methods.

Enabling caching improves your model’s response times and reduces costs by reducing calls to the LLM. You can also enable conversational caching to store chatbot sessions that add context and enhance conversational experiences.

> [!NOTE]
> For information about the billable costs of caching value adds, see [Manage Your Billing - AI Services](../../../cloud/billing/billing.md#model-service).

### [](#caching-expiry)Caching Expiry

The **Expiry** time to live (TTL) setting helps manage cache memory by automatically removing cached responses, embeddings, and conversation context after a specified time period. The default for this setting is `4000` seconds. You can enter a value between `3600` (1 hour) and `604800` (168 hours or 7 days).

### [](#caching-options)Caching Options

The following caching options are available when deploying LLMs:

| Caching Option                               | Example                                                                                                                                                                                                                                                               | Common Usage                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Standard Caching](#standard-cache)          | "What’s Python?" matches only "What’s Python?"                                                                                                                                                                                                                        | This method is effective for exact matches, but it does not help with prompts that vary even slightly. This makes standard caching less flexible for natural language interactions.                                                                                                                                                                                                           |
| [Semantic Caching](#semantic-cache)          | "What’s Python" might match "Tell me about Python" or "Explain Python"                                                                                                                                                                                                | This method provides higher cache hits and handles query variations and paraphrasing, making it better suited for natural language interactions. Semantic caching can increase costs because of its intensive computational and memory requirements and because it requires a dedicated embedding model.                                                                                      |
| [Standard and Semantic Caching](#both-cache) | When using standard cache (default or API-specified), "What’s Python?" matches only the exact phrase "What’s Python?". When using semantic cache (default or API-specified), it matches semantically similar queries like "Tell me about Python" or "Explain Python." | With the option of implementing 2 caching mechanisms, you can benefit from the speed and simplicity of standard caching for common cases, while providing the flexibility of semantic caching for more natural language interactions. Semantic caching can increase costs because of its intensive computational and memory requirements and because it requires a dedicated embedding model. |

Standard caching

Standard caching maintains an exact-match lookup: when the system receives a prompt, it checks if that exact prompt and parameter combination exists in the cache. If there is a match, the system returns the stored response immediately. If there is no match, the system calls the LLM, stores the new prompt-response pair in the cache, and returns it.

Semantic caching

Semantic caching uses vector embeddings to match similar meanings rather than exact matches. When the system receives a prompt, it converts the prompt into a vector representation using an embedding model and finds the closest semantic match in the cache. If there is a close semantic match, the system returns the stored response immediately. If there is no match, the system calls the LLM, stores the new prompt-response pair as vector representation, and returns it.

You can adjust the following semantic caching settings to tune the tradeoff between cache hit rate, response quality, and resource usage:

* **Score threshold**: The score threshold determines how closely a new prompt needs to match the prompts in the cache for it to be a match. A higher score threshold requires closer semantic similarity, resulting in more relevant but potentially fewer cache hits. A lower threshold allows more prompts to match cached results but may return less relevant responses.
* **Vector dimension**: The vector dimension defines the size of the vector embeddings used for semantic caching. Higher-dimensional vectors capture more nuanced semantic information but require more memory and computational resources. Lower-dimensional vectors are more efficient but may miss some semantic nuances.
* **Vector similarity**: The vector similarity metric defines how the system measures the closeness between vector embeddings. Similarity metrics include dot product, Euclidean norm, and cosine. Choosing the correct similarity metric affects how effective semantic caching is based on the nature of your prompts and the embedding model used.

You must [deploy an embedding model](deploy-embed-model.md) to use semantic caching.

Standard and semantic caching

Standard and semantic caching combines the benefits of standard and semantic caching into a single, unified cache that handles both caching options. When configuring the standard and semantic caching option, you set 1 of these strategies as the default that meets most of your caching needs. You can override the default and set a different caching mode as needed using the `X-cb-cache` API header with the following values:

* `standard`: Use standard caching for this request
* `semantic`: Use semantic caching for this request
* `none`: Bypass the cache and query the LLM directly for this request

For example, to use semantic caching for a specific request, include the `X-cb-cache` with the `semantic` value in the header of your API call:

```sh
curl "$MODEL_STRING/v1/chat/completions" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "X-cb-cache: semantic" \
  -d '{
  "messages": [
    {
      "role": "user",
      "content": "What is Couchbase all about? Write a SQL++ query to get top 250 documents in a sorted list of scope, inventory and collection, airlines"
    }
  ],
  "model": "meta-llama/Llama-3.1-8B-Instruct",
  "stream": false,
  "max_tokens": 100
}
```

Picking and choosing when to use a caching option allows for more flexibility and optimization for contrasting use cases.

You must [deploy an embedding model](deploy-embed-model.md) to use the combined standard and semantic cache.

Conversational caching

For advanced dialog systems and chatbot applications, you can enable conversational caching to store the context and state of ongoing conversations. This type of caching helps maintain conversational coherence and is critical to building smooth, responsive, and personalized chatbot experiences.

Conversational caching uses your chosen caching type.

### [](#considerations)Considerations

When configuring caching for your LLM, consider the following factors:

Performance needs

If your application requires low latency and fast response times, caching helps achieve these goals by reducing the number of calls to the LLM. Conversational caching is particularly beneficial for chatbot applications that require maintaining context across multiple interactions.

Cost savings

Caching reduces costs by minimizing the number of calls made to the LLM for frequently repeated prompts.

Resource constraints

Consider the computational and memory resources required for semantic caching.

## [](#async-processing)Async Processing

Asynchronous processing helps improve throughput and efficiency during periods of high demand or when processing large volumes of data. Rather than processing requests right away, asynchronous processing allows jobs to be queued and processed when system capacity becomes available. Enabling Async Processing maximizes resource utilization and reduces wait times for requests that do not require immediate results.

> [!NOTE]
> For information about the billable costs of Async Processing, see [Manage Your Billing - AI Services](../../../cloud/billing/billing.md#model-service).

Async Processing is beneficial when you need high throughput for batch operations, such as handling spikes in requests from multiple users or applications. Async Processing is less suitable for real-time applications that need immediate results, such as live chatbot responses.

You can toggle Async Processing on or off during or after deployment of a model.

### [](#considerations-2)Considerations

When configuring Async Processing for your LLM, consider the following factors:

Throughput requirements

If your application requires high throughput for batch operations or can tolerate some delay in processing, Async Processing improves efficiency and resource utilization.

Real-Time needs

If your application requires immediate results, such as real-time search or chatbot interactions, Async Processing may not be suitable. For these use cases, use synchronous processing.

## [](#keyword-filtering)Keyword Filtering

Keyword filtering uses whole-word blocking of keywords in LLM prompts and responses. Using this feature, you can define a list of keywords to block, helping to enforce content policies and improve the overall quality of interactions. For example, you could filter out the names of your competitors, explicit language, or other content you do not want in user prompts and responses.

When configuring an LLM to use keyword filtering, you must provide a string of case-sensitive comma separated keywords.

### [](#considerations-3)Considerations

When configuring keyword filtering for your LLM, consider the following factors:

Content policies

Make sure the selected keywords align with your organization’s content policies and ethical standards. Regularly review and update the keyword list to adapt to evolving language use and content standards.

User experience

Balance content moderation with user experience when selecting keywords. Overly broad or aggressive filtering may lead to unnecessary blocking of legitimate content, while lax filtering may allow inappropriate content to pass through. Test with representative queries to balance these factors.

## [](#see-also)See Also

* [Deploy a Large Language Model (LLM)](deploy-llm-model.md)
* [Configure LLM Performance](configure-llm-performance.md)
* [Configure Guardrails and Security](configure-guardrails-security.md)