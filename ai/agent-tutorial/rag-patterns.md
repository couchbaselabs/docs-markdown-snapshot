---
title: About RAG Blueprints
description: Learn about common RAG (Retrieval-Augmented Generation) patterns
  and how they are applied in knowledge bases, support, and search.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/agent-tutorial/pages/rag-patterns.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:ai:agent-tutorial:rag-patterns.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/agent-tutorial/rag-patterns.html)

# About RAG Blueprints

> Learn about common RAG (Retrieval-Augmented Generation) patterns and how they are applied in knowledge bases, support, and search. 

## [](#whats-rag)What's RAG?

Retrieval-Augmented Generation (RAG) is a technique that combines a Large Language Model (LLM) with an external knowledge source. Instead of relying only on an LLM's training data, RAG retrieves relevant information from a database, document store, or [search index](../../cloud/vector-index/vectors-and-indexes-overview.md) and injects it into the LLM's prompt.

RAG allows an LLM to:

* Answer questions with up-to-date information.
* Provide domain-specific knowledge, such as company policies, or product manuals.
* Reduce hallucinations by grounding responses in real data.

> [!TIP]
> Capella AI Services offers a guided workflow to get you started with RAG. For more information and to view the interactive tutorials, go to **AI Services** **Offerings** in the Capella UI.
> 
> You can also use notebooks and sample code hosted on Google Colab and GitHub to get you started with a prebuilt agentic app in your choice of agent framework:
> 
> * Colab: [LangGraph](https://colab.research.google.com/github/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/flight%5Fsearch%5Fagent%5Flangraph/flight%5Fsearch%5Fagent%5Ftutorial.ipynb) | [LangChain](https://colab.research.google.com/github/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/hotel%5Fsearch%5Fagent%5Flangchain/hotel%5Fsearch%5Fagent%5Ftutorial.ipynb) | [LlamaIndex](https://colab.research.google.com/github/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/landmark%5Fsearch%5Fagent%5Fllamaindex/landmark%5Fsearch%5Fagent%5Ftutorial.ipynb)
> * GitHub: [LangGraph](https://github.com/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/flight%5Fsearch%5Fagent%5Flangraph/flight%5Fsearch%5Fagent%5Ftutorial.ipynb) | [LangChain](https://github.com/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/hotel%5Fsearch%5Fagent%5Flangchain/hotel%5Fsearch%5Fagent%5Ftutorial.ipynb) | [LlamaIndex](https://github.com/couchbase-examples/agent-catalog-quickstart/blob/main/notebooks/landmark%5Fsearch%5Fagent%5Fllamaindex/landmark%5Fsearch%5Fagent%5Ftutorial.ipynb)

## [](#rag-blueprints)RAG Blueprints

While every RAG system is unique, most fall into common patterns, or blueprints. These blueprints describe how RAG is applied in different contexts, such as:

* [Knowledge bases, for internal or external documentation](#knowledge-base).
* [Customer support assistants](#customer-support).
* [Search and discovery tools](#search).

By understanding these blueprints, you can design your own RAG-powered applications more effectively.

### [](#knowledge-base)RAG Blueprint 1: Knowledge Base Assistant

In this blueprint, a RAG agent gives accurate answers from searching a large set of documents. These documents could be in the form of:

* Company wikis
* User manuals
* Research papers

You could use this kind of RAG blueprint to build apps for an internal employee knowledge base, a technical documentation search, or other research assistant.

The typical logic flow in this RAG blueprint is:

1. The user asks a question.
2. The system retrieves the most relevant documents or passages from the document set.
3. The retrieved text is injected into the LLM's prompt.
4. The LLM generates a grounded answer, citing or summarizing the sources.

![Diagram](_images/diag-ad5b92fc90727632ea2d8e9cc6a993a3518a4910.svg) 

#### [](#overall-system-considerations)Overall System Considerations

When designing an application that uses this kind of RAG blueprint, make sure to consider:

Document chunking strategy

If a document is not chunked properly, you might lose context or semantic meaning from your content, or you might exceed token limits on your LLM.

Your chunking strategy should suit the structure of your documents, including the specific formatting features, while also efficiently returning results.

For more information about configuring chunking in a Capella AI Services Workflow, see [Chunking](../build/vectorization-service/data-processing.md#chunking).

Embedding quality

If you use low-dimension embeddings for your RAG system, your retrieval results might not be accurate - but high-quality, high dimension embeddings cost more to store and take more time to search.

Source attribution

When retrieving documents through RAG, it's important for your agent to cite its sources and return them in results.

This can also help make debugging your agent code easier.

Managing document index updates

As your documents change or update, you need to make sure that the index, or the collection of embeddings and metadata you use for retrieval, stays in sync. To keep your content and your index in sync, you should:

* Set up regular reindexing to get new or updated documents.
* Make sure outdated content or documents are removed from your index.

#### [](#specific-blueprint-configuration-settings)Specific Blueprint Configuration Settings

When configuring your workflow and supporting systems for this blueprint, keep in mind the following configuration guidance:

Top K

The Top K value controls how many chunks your system retrieves from documents to try and answer a query.

Keep the Top K value for a knowledge base assistant higher if your queries tend to be more broad or your documents are more scattered.

A higher Top K value on your LLM keeps the model from missing important supporting information. Higher Top K values can also cause you to lose more focused answers.

Try to find a good balance between precision and capturing relevant information. For example, you might consider setting your Top K value somewhere around 5-12.

Embedding Model

For the best results, make sure that you use the same model for generating embeddings and retrieving them from your RAG system. You can use a different, main LLM for the rest of your app.

This is even more important if your document set is expected to change often, and you need to generate embeddings regularly.

For a knowledge base assistant, consider using an embedding model like `nv-embedqa-mistral-7b-v2`.

In general, choose a richer model that gives better semantic embeddings, or higher recall scores, or a model that's tuned to your specific use case. Better semantics helps connect information across the chunks in your documents.

For more information about how to deploy an embedding model on Capella, like `nv-embedqa-mistral-7b-v2`, see [Deploy an Embedding Model](../build/model-service/deploy-embed-model.md).

Similarity Metric

You should consider normalizing your vectors and use cosine similarity as your similarity metric. Cosine similarity offers the best directional alignment between a query and document chunks.

For more information about how to set the similarity metric for your vectors in Capella, see:

* [Create a Search Vector Index in Quick Mode](../../cloud/vector-search/create-vector-search-index-ui.md)
* [Create a HyperScale Vector Index with the Capella UI](../../cloud/vector-index/hyperscale-vector-index.md#create-index)
* [Create a Composite Vector Index with the Capella UI](../../cloud/vector-index/composite-vector-index.md#create-index)

### [](#customer-support)RAG Blueprint 2: Customer Support Assistant

In this blueprint, a RAG agent helps users resolve issues by combining documentation with conversational guidance.

You could use this kind of RAG blueprint to build a product support chatbot, an IT helpdesk assistant, or help with triage in customer service.

The typical logic flow in this RAG blueprint is:

1. The user describes a problem in natural language.
2. The system retrieves relevant troubleshooting steps or FAQs.
3. The LLM uses both the retrieved content and conversation history to guide the user.
4. Optionally, the system can escalate to a human agent if needed.

![Diagram](_images/diag-b44dcf34cb6604cfae7dae6172babc2622e3dc97.svg) 

#### [](#overall-system-considerations-2)Overall System Considerations

When designing an application that uses this kind of RAG blueprint, make sure to consider:

Handling ambiguity or incomplete queries

Users might provide ambiguous or incomplete information in their initial query. In a customer support scenario, you need to figure out how your app should ask clarifying questions to give the best response.

You may want your LLM to generate clarifying questions based on few-shot examples, or based on the knowledge available from its initial query.

After generating a clarifying question, you also need to figure out how to incorporate that context into the agent's memory to try and generate another response - whether that's another question or a final answer.

Escalation rules

In a customer support RAG app, you want your agent to know when to hand off to a human. Generally, an agent should complete a hand off when:

* The user specifically requests it.
* The user has shown escalating frustration.
* The user asks a question outside the agent's scope.
* The agent fails to determine the user's intent.
* The agent has encountered technical problems.

Make sure that your handoff passes over all available information gathered by the AI agent to the human agent.

Guardrails

Guardrails are especially important in a customer support scenario. You must make sure that the app does not provide unsafe, incorrect, or otherwise harmful information or instructions to the user.

You might want your guardrails to filter unsafe or biased content from user queries. You could also want to make sure that no sensitive information from your app's available resources, such as information that could personally identify a customer, gets returned in responses.

Guardrails could be as simple as keyword or semantic filtering, or as complex as contextual grounding checks and AI-powered moderation.

For more information about how to configure guardrails on a model deployed on Capella, see [Configure Guardrails and Security](../build/model-service/configure-guardrails-security.md).

#### [](#specific-blueprint-configuration-settings-2)Specific Blueprint Configuration Settings

When configuring your workflow and supporting systems for this blueprint, keep in mind the following configuration guidance:

Top K

The Top K value controls how many chunks your system retrieves from documents to try and answer a query.

Keep the Top K value for a customer support assistant much lower than a knowledge base assistant or search and discovery tool.

In this use case, you want focused, short answers with minimal surrounding info.

For example, you might consider setting your Top K value somewhere around 3.

Embedding Model

For the best results, make sure that you use the same model for generating embeddings and retrieving them from your RAG system. You can use a different, main LLM for the rest of your app.

This is even more important if your document set is expected to change often, and you need to do a lot of embedding.

For a customer support assistant, consider using an embedding model like `nv-embedqa-e5-v5`.

You can choose a smaller model for this use case to save and support better scaling on query volumes, since you need shorter, predictable responses.

For more information about how to deploy an embedding model on Capella, like `nv-embedqa-e5-v5`, see [Deploy an Embedding Model](../build/model-service/deploy-embed-model.md).

Similarity Metric

Use cosine similarity to get the best directional, conceptual alignment between a query and a chunk.

For more information about how to set the similarity metric for your vectors in Capella, see:

* [Create a Search Vector Index in Quick Mode](../../cloud/vector-search/create-vector-search-index-ui.md)
* [Create a HyperScale Vector Index with the Capella UI](../../cloud/vector-index/hyperscale-vector-index.md#create-index)
* [Create a Composite Vector Index with the Capella UI](../../cloud/vector-index/composite-vector-index.md#create-index)

### [](#search)RAG Blueprint 3: Search and Discovery

In this blueprint, a RAG agent helps users explore large collections of information with natural language, rather than limited keyword searches.

You could use this kind of RAG blueprint to run an enterprise search across internal files, create a research discovery platform or media and news aggregator.

The typical logic flow in this RAG blueprint is:

1. The user enters a query in natural language.
2. The system retrieves relevant documents, articles, or data.
3. The LLM summarizes, ranks, or clusters the results.
4. The user can continue to refine the query conversationally.

![Diagram](_images/diag-9f29fe99811468806c00449022d9e85eb976111d.svg) 

#### [](#overall-system-considerations-3)Overall System Considerations

When designing an application that uses this kind of RAG blueprint, make sure to consider:

Balancing recall and precision

Based on the specifics of your search agent, you need to balance finding enough results for a query with finding the right results.

More exhaustive searches use more resources, as you compare a greater number of embeddings. This more precise search might be necessary for queries that require highly accurate results, such as in a medical research context.

For a search query that's more focused on brainstorming or answering a more complex question, it might be better to return more results, to make sure you do not leave anything out.

Result transparency

A search agent needs to present more than a single answer. Presenting users with a set of relevant results provides a better user experience. It also makes it easier to refine search results and get to the most relevant result.

Consider adding confidence scoring, or highlighting matching terms or sections in results for even more transparency.

Supporting conversational refinement

A search agent should allow users to continue to refine a search conversationally. The context window of the LLM should support iteration and keep the context of the conversation while running a search.

Follow-up questions from the LLM, if a query was ambiguous, or clarifications from the user, should all be kept in context and updating filtering or sorting on results. Consider adding indications in your app to show users how their conversation affects the search results.

#### [](#specific-blueprint-configuration-settings-3)Specific Blueprint Configuration Settings

When configuring your workflow and supporting systems for this blueprint, keep in mind the following configuration guidance:

Top K

The Top K value controls how many chunks your system retrieves from documents to try and answer a query.

Keep the Top K value for a search and discovery tool high.

In this use case, you want as many options as possible, and for the LLM to be quite exploratory.

Try a Top K value of 20-30.

Embedding Model

For the best results, make sure that you use the same model for generating embeddings and retrieving them from your RAG system. You can use a different, main LLM for the rest of your app.

This is even more important if your document set is expected to change often, and you need to do a lot of embedding.

For a search and discovery tool, consider using an embedding model like `arctic-embed-l`.

You want a larger, more capable model to handle the number of vectors and the size of the dataset for this use case.

For more information about how to deploy an embedding model on Capella, like `arctic-embed-l`, see [Deploy an Embedding Model](../build/model-service/deploy-embed-model.md).

Similarity Metric

Use dot product similarity for a search and discovery agent to get the fastest performance when comparing your vectors.

For more information about how to set the similarity metric for your vectors in Capella, see:

* [Create a Search Vector Index in Quick Mode](../../cloud/vector-search/create-vector-search-index-ui.md)
* [Create a HyperScale Vector Index with the Capella UI](../../cloud/vector-index/hyperscale-vector-index.md#create-index)
* [Create a Composite Vector Index with the Capella UI](../../cloud/vector-index/composite-vector-index.md#create-index)

## [](#combining-rag-blueprints)Combining RAG Blueprints

RAG blueprints are not rigid categories. Any blueprint is a pattern that you can adapt to your specific use case.

In many cases, your application might combine elements from multiple blueprints:

* A support assistant may use a knowledge base for answers and a search interface for escalation.
* A research tool may combine search and discovery with a knowledge base of curated papers.

The key is that RAG allows your app to stay grounded in real data, while still benefiting from the reasoning and flexibility of an LLM.

## [](#see-also)See Also

* [About Agentic Apps](about-agentic-app.md)
* [Plan Your Agentic App](plan-agentic-app.md)
* [Capella AI Services](../get-started/intro.md)
* [Integrate an Agent with the Agent Catalog](../build/integrate-agent-with-catalog.md)