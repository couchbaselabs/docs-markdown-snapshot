[View original HTML](/ai/build/vectorization-service/data-processing.html)

> Use Capella AI Services Workflows to prepare, process, and vectorize text for use with other Capella AI Services. 

The following Workflows are available through Capella AI Services:

* **Unstructured Data from S3**: Use when your data is not yet in JSON format and is stored inside an Amazon S3 bucket.
* **Structured Data from External Sources**: Use when your data has already been pre-processed and stored in JSON format on an Amazon S3 bucket.
* **Data from Capella**: Use when your data has already been pre-processed and stored in a Capella operational cluster.

|  | All Workflows require an embedding model to generate vectors. You can use an embedding model [hosted by the Capella Model Service](../model-service/deploy-embed-model.md) or [OpenAI](https://openai.com/). |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

You must configure specific [data preprocessing options](#data-preprocess) when using an Unstructured Data Workflow. Keep the [Unstructured Data Processing Limitations](#limitations) in mind when processing unstructured data.

## [](#vectorization)Vectorization

Using the Data Processing Service, Capella AI Services preprocesses and chunks your data, removing elements to reduce your signal-to-noise ratio and converting data into JSON. It uses the Vectorization Service to take processed JSON data and generate vector embeddings.

Vectors are a numerical representation of complex unstructured data. They distill this complex data into an array of floating-point values called dimensions. The dimensions in vectors capture features of the data in a way that makes them easy to compare mathematically.

For more information about vectors, see [About Vectors](../../../cloud/vector-index/vectors-and-indexes-overview.md#about-vectors) and [Embedding Vectors](../../../cloud/vector-index/vectors-and-indexes-overview.md#embedding-vectors).

Workflows create dedicated metadata collections and [Eventing functions](../../../cloud/eventing/eventing-overview.md) on your chosen Capella operational cluster:

* A Workflow’s metadata is stored in collections inside the `vectorization-meta-data` scope.
* Every Workflow creates 2 Eventing functions:

  * `vec_ctr_$WORKFLOW_ID`
  * `vec_wkr_$WORKFLOW_ID`

|  | Do not modify or delete the Workflows metadata scope, its collections, or the Eventing functions. If you delete or modify the scope, collections, or Eventing functions, you must delete your Workflow and create a new one. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#data-preprocess)Data Preprocessing Options

When using an Unstructured Data Workflow, you can configure data preprocessing options to control and fine-tune your data before generating vector embeddings.

You can configure the following options:

* (Optional) [Page ranges to include from documents](#page-range)
* (Optional) [Specific document elements to remove](#layout-exclusions)
* (Optional) [Optical Character Recognition (OCR)](#ocr) for processing text from images or PDFs
* [How the Workflow creates chunks from your documents](#chunking)

### [](#page-range)Page Range

You can set an inclusive range of pages for any documents processed through your Workflow.

Capella ignores any content on document pages not included in this range.

### [](#layout-exclusions)Layout Exclusions

You can choose specific document elements to remove from processing through your Workflow.

These specific elements of unstructured documents can add noise to your vectorization process, and do not include meaningful semantic content. Remove these elements to improve the signal-to-noise ratio, and reduce the storage and processing requirements for vectorizing your data.

You can remove the following document elements from processing through an Unstructured Data Workflow:

* Tables
* Footers
* Document titles and section headers

By default, your Unstructured Data Workflow enables **Exclude Footer** and **Exclude Header**.

### [](#ocr)Optical Character Recognition (OCR)

You can enable OCR to extract text from JPEGs, PNGs, and PDFs.

If you do not have images or PDF files in your data, you do not need to enable OCR.

### [](#chunking)Chunking

You can configure how your Unstructured Data Workflow chunks, or divides your documents into smaller segments. Chunks make it easier for a model to search and retrieve only the relevant information from your documents.

You can choose a chunking strategy, maximum chunk size, and chunk overlap.

Chunks can be set to a minimum of 256 and a maximum of 8192 tokens.

If you choose to set a chunk overlap, your Unstructured Data Workflow makes sure 0-4 tokens overlap between chunks.

#### [](#chunking-strategies)Chunking Strategies

The following chunking strategies are available in Capella AI Services:

| Chunking Strategy                       | Semantic Preservation                                                                                                                                                                                                                                                                                              | Common Use Cases                                                                                           |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| [FIXED\_TOKEN\_SPLITTER](#fixed-chunk)  | Low semantic preservation that ignores document structure and can break natural semantic boundaries.                                                                                                                                                                                                               | Generic document collections Machine learning training data Log files Web crawled content                  |
| [PARAGRAPH\_SPLITTER](#paragraph-chunk) | High semantic preservation by preserving the broader contextual reasoning and narrative flow.                                                                                                                                                                                                                      | Academic papers Long-form articles Research reports Narrative texts                                        |
| [RECURSIVE\_SPLITTER](#recursive-chunk) | Medium-to-high semantic preservation that preserves meaning within chunks, particularly for highly structured or hierarchical documents.                                                                                                                                                                           | Long reports or research papers Legal documents Technical documentation Books or articles                  |
| [SEMANTIC\_SPLITTER](#semantic-chunk)   | High semantic preservation that preserves semantic meaning within chunks, by comparing text segments for semantic similarity and creating new chunks at logical breaks. Content is separated into chunks based on themes, rather than just structural elements, making comprehensive information retrieval easier. | Complex legal documents Technical documentation or manuals Long reports or research papers Narrative texts |
| [SENTENCE\_SPLITTER](#sentence-chunk)   | High semantic preservation by preserving precise context in sentences, but may struggle with inter-sentence references.                                                                                                                                                                                            | Structured reports Concise articles Scientific abstracts Customer support transcripts                      |

Fixed-length (text) chunking

Divides text into uniform chunks based on the chosen maximum chunk size. This method can help with consistent processing across large documentation sets, even when individual sections vary greatly in length. However, it can break semantic units and is unsuitable for preserving semantic coherence.

For example, you could split a document into chunks of 100 tokens, regardless of whether the chunk ends mid-sentence or across paragraphs. This option is useful for summarizing and searching extensive log files.

Paragraph chunking

Divides text into full paragraphs. This method preserves paragraph integrity and can maintain context within logical text units.

For example, paragraph chunking might break a document into chunks where each has several paragraphs, maintaining the semantic integrity of each chunk while keeping the size manageable. However, there can be variation in chunk sizes since paragraphs can vary greatly in length. Preserving context and reasoning within each paragraph is useful for applications like finding information in large, complex documents.

Recursive chunking

Divides text into increasingly smaller segments based on document structure and semantic units. This method preserves document hierarchy by splitting at natural boundaries like paragraphs, sentences, and then words using a top-down approach.

For example, recursive chunking might break a document first into paragraphs. If a paragraph exceeds the chunk size, it moves to the next level by breaking it into sentences. This process continues down to individual words if necessary. This hierarchical approach maintains context between chunks while keeping individual segments at a manageable size for processing. This approach is useful for applications that need to understand document structure and relationships, such as legal documents.

Semantic chunking

Divides text into smaller, self-contained units based on meaning and context. This method uses embedding models to create mathematical representations of text segments, comparing their semantic similarity to find logical breaks for new chunks.

Semantic chunking makes sure each chunk conveys a unified idea and preserves coherent context for RAG applications. It uses a specific algorithm that requires a specific chunk size and a chunk overlap, to help determine where to create breaks in the content.

Semantic chunking is the default option for Capella AI Services, as it can provide the best results.

Sentence chunking

Divides text into full sentences, ensuring each chunk contains a complete thought. This method helps preserve the logical flow of information by splitting natural sentence boundaries.

For example, sentence-level chunking breaks a document into chunks that contain 1 complete sentence, maintaining the semantic integrity of each chunk while keeping the size manageable. This approach allows for precise retrieval of specific details, which is crucial for applications like accurate customer support responses.

## [](#limitations)Unstructured Data Processing Limitations

Unstructured Data Workflows have the following file size or file number limitations:

| Limitation                                   | Value         |
| -------------------------------------------- | ------------- |
| Maximum file size                            | 100 MB        |
| Maximum number of files allowed per Workflow | 10,000        |
| Maximum image size                           | 32,767 pixels |

## [](#status)Workflow Statuses

A Capella AI Services Workflow can have 1 of the following statuses:

| State          | Description                                                                                                                                                                                                                                                |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Deploying      | The resources for this Workflow are currently being deployed on AI services.                                                                                                                                                                               |
| Deploy Failed  | The required resources for this Workflow failed to deploy. You can delete this Workflow and try to deploy a new one.                                                                                                                                       |
| Pending        | The deployment process for the Workflow is taking longer than expected.                                                                                                                                                                                    |
| Running        | The Workflow is currently processing documents. You can stop the Workflow while it’s running by going to **More Options (⋮)** **Stop Workflow** on the Workflows page.                                                                                     |
| Completed      | The Workflow has finished processing documents. A Workflow can change to the Completed state even if it’s only processed a single document. You can rerun the Workflow by going to going to **More Options (⋮)** **Rerun Workflow** on the Workflows page. |
| Failed         | The Workflow failed during processing. Click to view more information about the error. You can rerun the Workflow by going to going to **More Options (⋮)** **Rerun Workflow** on the Workflows page.                                                      |
| Stopping       | The Workflow is currently finishing processing any currently ingested documents and preparing to stop.                                                                                                                                                     |
| Stopped        | The Workflow has stopped processing documents. You can rerun the Workflow by going to going to **More Options (⋮)** **Rerun Workflow** on the Workflows page.                                                                                              |
| Stop Failed    | An error occurred while stopping the Workflow. Contact [Couchbase Capella Support](../../../cloud/support/manage-support.md) to delete the Workflow.                                                                                                       |
| Destroying     | The Workflow’s resources are being deleted.                                                                                                                                                                                                                |
| Destroy Failed | An error occurred while deleting the Workflow. Contact [Couchbase Capella Support](../../../cloud/support/manage-support.md).                                                                                                                              |

## [](#workflow-billing)Workflow Billing

For information about how Couchbase bills you according to your Workflow usage, see [Workflow Billing](../../../cloud/billing/billing.md#workflows).

## [](#see-also)See Also

* [Process and Vectorize Unstructured Data](vectorize-unstructured-data.md)
* [Vectorize Structured Data from Capella](vectorize-structured-data-capella.md)
* [Vectorize Structured Data from Amazon S3](vectorize-structured-data-s3.md)
* [Troubleshoot a Workflow](troubleshoot-vectorization.md)