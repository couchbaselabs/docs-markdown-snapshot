---
title: Vector Search Using Search Vector Indexes
description: Use Couchbase Server's Vector Search features to add fast and
  accurate semantic search to your applications.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/vector-search/pages/vector-search.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:vector-search:vector-search.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/vector-search/vector-search.html)

# Vector Search Using Search Vector Indexes

> Use Couchbase Server’s Vector Search features to add fast and accurate semantic search to your applications. 

> [!IMPORTANT]
> You cannot use Vector Search on Windows platforms. You can use Vector Search on Linux from Couchbase Server version 7.6.0 and MacOS from version 7.6.2.
> 
> You can still use other features of the [Search Service](../search/search.md).

## [](#about-vector-search)About Vector Search

Vector Search builds on Couchbase Server’s [Search Service](../search/search.md) to provide vector index support. You can use these new Search Vector Indexes for Retrieval Augmented Generation (RAG) with an existing Large Language Model (LLM).

Using Server’s Vector Search, an embedding model, and your chosen LLM, you can develop AI applications while giving context and up-to-date information from your own data.

You can develop applications that include:

* **Similarity search:** Search for documents, products, images, and more that are similar to a given query using vector embeddings. By using vector embeddings, you can search based on descriptions, rather than using specific keywords and get intuitive and relevant results across data types.
* **Semantic search**: Use natural language processing to deliver more accurate results based on an understanding of the intent and context behind a given search query, rather than simple keyword matches.
* **Generative AI:** Create new original content, such as text and images, based on a prompt or a vector search given to an LLM. Use generative AI to get tailored and dynamic responses across your applications.

Vector Search supports integrations with frameworks like [LangChain](https://python.langchain.com/docs/get%5Fstarted/introduction) to support AI application development. For more information about all frameworks and integrations supported by Vector Search and Server, see [Integrations, Connectors, and Tools](../third-party/integrations.md).

## [](#using-search-vector-indexes)Using Search Vector Indexes

To get started using Vector Search in Server:

1. **Store data**: Store the data you want to use for your search or AI project in a Server cluster.
2. **Generate embeddings**: Generate vector embeddings from your data with your preferred embedding model.
3. **Store your embeddings**: Store your vector embeddings in an array inside the documents in your Server cluster.
4. **Create a Search Vector Index**: Create an index to use your embeddings and identify similar documents with vector similarity.

In addition to supporting integrations with frameworks like LangChain and LlamaIndex, you can also use the API for an existing LLM and one of their embedding models to generate vector embeddings for your data. For example, the OpenAI `embeddings` endpoint can generate embeddings for a text string using a specified embedding model. You can then store that embedding as a new field in your documents. For more information about how to generate and obtain embeddings for text strings using the OpenAI API, see the [Embeddings documentation](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings).

> [!NOTE]
> When you create a Search Vector Index, the [dimension](../search/child-field-options-reference.md#dimension) of your data vector embeddings must match the dimension for any search query vectors. Otherwise, a Vector Search query fails to return any results.

For more information about how to create a Search Vector Index, see [Create a Search Vector Index with the Server Web Console](create-vector-search-index-ui.md) or [Create a Search Vector Index with the REST API and curl/HTTP](create-vector-search-index-rest-api.md).

For information about how to run a Vector Search query, see [Run A Vector Search with the Server Web Console](run-vector-search-ui.md) or [Run a Vector Search with the REST API and curl/HTTP](run-vector-search-rest-api.md).

## [](#see-also)See Also

* [Add Search to Your Application](../search/search.md)
* [Create a Search Vector Index with the Server Web Console](create-vector-search-index-ui.md)
* [Create a Search Vector Index with the REST API and curl/HTTP](create-vector-search-index-rest-api.md)
* [Run A Vector Search with the Server Web Console](run-vector-search-ui.md)
* [Run a Vector Search with the REST API and curl/HTTP](run-vector-search-rest-api.md)