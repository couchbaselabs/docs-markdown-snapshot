---
title: Configure Embedding Model Performance
description: The AI Data Plane Model Service offers options to tweak the
  performance of your embedding model.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/build/pages/model-service/configure-embed-performance.adoc
  xref: xref:ai:build:model-service/configure-embed-performance.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/build/model-service/configure-embed-performance.html)

# Configure Embedding Model Performance

> The AI Data Plane Model Service offers options to tweak the performance of your embedding model. 

The following performance settings are available when deploying an embedding model:

* [Dimensions](#dimensions)
* [Async Processing](#async-processing)

## [](#dimensions)Dimensions

In embedding models, dimensions are the length of the numerical vectors used to represent text content. These vectors capture semantic meaning, allowing AI systems to identify similarities between content. A higher number of dimensions provides richer and more detailed representations, but also increases resource costs. The ideal number of dimensions is a trade-off between performance, accuracy, and computational resources.

When choosing the number of dimensions for your embedding model, consider the following factors:

Use Case

The specific requirements of your application influence the ideal number of dimensions. Higher dimensions can capture more nuanced semantic relationships, improving performance in complex tasks like semantic search and sentiment analysis. Lower dimensions capture more generalized patterns and lose some subtle contextual details.

Resources

Higher dimensions require more storage and computational resources. Selecting smaller dimensions can reduce resource consumption and improve computational efficiency, but lose some accuracy.

You cannot customize the number of vector dimensions on all embedding models available through the Model Service.

You cannot change the number of dimensions after deploying an embedding model.

## [](#async-processing)Async Processing

Asynchronous processing can help improve throughput and efficiency during periods of high demand or when processing large volumes of data. Rather than processing embedding requests right away, asynchronous processing allows embedding jobs to be queued and processed when system capacity becomes available. By enabling Async Processing, you can maximize resource utilization and reduce wait times for embedding jobs that do not require immediate results.

Async Processing is beneficial when you need high throughput for batch operations, such as processing large batches of documents for embedding or handling spikes in embedding requests from multiple users or applications. Async Processing is less suitable for real-time applications that need immediate results, such as embedding user queries for semantic search or live chatbot responses.

You can toggle Async Processing on or off during or after deployment of an embedding model.

## [](#see-also)See Also

* [Deploy an Embedding Model](deploy-embed-model.md)
* [Process and Vectorize Unstructured Data](../vectorization-service/vectorize-unstructured-data.md)
* [Vectorize Structured Data from Capella](../vectorization-service/vectorize-structured-data-capella.md)
* [Vectorize Structured Data from Amazon S3](../vectorization-service/vectorize-structured-data-s3.md)