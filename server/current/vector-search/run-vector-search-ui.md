[View original HTML](/server/current/vector-search/run-vector-search-ui.html)

> Run a Vector Search query from the Couchbase Server Web Console to preview and test the search results from a Search Vector Index. 

For more information about how the Search Service scores documents in search results, see [Scoring for Search Queries](#run-searches.adoc#scoring).

|  | You cannot use Vector Search on Windows platforms. You can use Vector Search on Linux from Couchbase Server version 7.6.0 and MacOS from version 7.6.2. You can still use other features of the [Search Service](../search/search.md). |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* You have a bucket with scopes and collections in your cluster. For more information about how to create a bucket, see [Create a Bucket](../manage/manage-buckets/create-bucket.md).
* Your user account has the **Search Admin** or **Search Reader** role.
* You have created a Search Vector Index.  
For more information about how to create a Search Vector Index, see [Create a Search Vector Index with the Server Web Console](create-vector-search-index-ui.md).

|  | You can download a sample dataset to use with the procedure or examples on this page: [Download color\_data\_2vectors.zip](https://cbc-remote-execution-examples-prod.s3.amazonaws.com/color%5Fdata%5F2vectors.zip) To get the best results with using the sample data with the examples in this documentation, [import the sample files](../guides/load.md) from the dataset into your database with the following settings: Use a bucket called vector-sample. Use a scope called color. Use a collection called rgb for rgb.json. To set your document keys, use the value of the id field from each JSON document. For the best results, consider using the sample Search Vector Index from [Create a Search Vector Index with the Server Web Console](create-vector-search-index-ui.md#example) or [Create a Search Vector Index with the REST API and curl/HTTP](create-vector-search-index-rest-api.md#example). |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To run a Vector Search with the Couchbase Server Web Console:

1. Go to **Search**.
2. Click the index where you want to run a search.
3. In the **Search this index** field, enter a search query.
4. Press Enter or click **Search**.

### [](#similarity)Example: Running a Simple Vector Similarity Query

For example, the following query searches for the top 2 vectors similar to the vector `[ 0, 0, 128 ]` in the `colorvect_l2` field:

```json
{
    "fields": ["*"], 
    "knn": [
      {
        "k": 2, 
        "field": "colorvect_l2", 
        "vector": [ 0, 0, 128 ]
      }
    ]
}
```

The Search query is only a Vector Search query. It only returns the `k` number of similar vectors.

When running a hybrid Search query, the Search Service combines the Vector search results from a `knn` object with the traditional `query` object by using an `OR` function. If the same documents match the `knn` and `query` objects, the Search Service ranks those documents higher in search results.

The document for the color `navy` should be the first result, followed by a similar color.

### [](#hybrid)Example: Running a Simple Hybrid Search Query

The following hybrid Search query searches for the top vector similar to the vector `[ 0, 0, 128 ]` in the `colorvect_l2` field. It also runs a [Numeric Range Query](../search/search-request-params.md#numeric-range-queries) on the `brightness` field to only return colors that have a brightness value between `70` and `80`:

```json
{
    "fields": ["*"], 
    "query": { 
      "min": 70,
      "max": 80,
      "inclusive_min": false,
      "inclusive_max": true,
      "field": "brightness"
    }, 
    "knn": [
      {
        "k": 1, 
        "field": "colorvect_l2", 
        "vector": [ 0, 0, 128 ]
      }
    ]
}
```

The Search Service combines the Vector search results from a `knn` object with the traditional `query` object by using an `OR` function. If the same documents match the `knn` and `query` objects, the Search Service ranks those documents higher in search results.

The document for the color `navy` should be the first result, followed by colors that are similar and match the `brightness` field query.

|  | If you want to run a hybrid Search query on a large, partitioned Search index and your cluster is on Couchbase Server version 8.0 or later, use the bm25 scoring model for your Search index. For more information, see [Set Search Index Advanced Settings](../search/set-advanced-settings.md). |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#large)Example: Running a Semantic Search Query with a Large Embedding Vector

The following query searches for matches to a large embedding vector, generated by the [OpenAI embedding model](https://platform.openai.com/docs/guides/embeddings), `text-embedding-ada-002-v2`.

|  | You can find generated embedding vectors for each color’s description field in rgb.json. |
|  | ---------------------------------------------------------------------------------------- |

This query should return the document for the color `navy`, based on a generated embedding vector for:

What is a classic, refined hue that exudes elegance and is often linked to power and stability?

The following shows part of the sample Search query:

```json
{
    "fields": ["*"],
    "knn": [
      {
        "field": "embedding_vector_dot",
        "k": 3,
        "vector": [
          0.024032991379499435,
          -0.009131478145718575,
          0.013961897231638432,
          -0.024734394624829292,
          -0.020605377852916718,
          0.006739427801221609,
          -0.012539239600300789,
          0.0063192471861839294,
          0.000004374724539957242,
          -0.030252983793616295,
          -0.010944539681077003,
          -0.0012845275923609734,
          0.0059850881807506084,
          -0.006388725712895393,
          -0.016304319724440575,
          0.03046472743153572,
          0.029988301917910576,
          -0.013121536932885647,
          0.01815708354115486,
          -0.011096730828285217,
          -0.0423753522336483,
          -0.0023523480631411076,
          -0.00022332418302539736,
          -0.0024681459181010723,
          -0.02911485731601715,
```

|  | Due to the size of the embedding vector, only part of the full query is being displayed in the documentation. Click **View** to view and copy the entire Vector Search query payload. Make sure you remove the lines for // tag::partial\[\] and // end::partial\[\]. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#base64)Example: Running a Semantic Search Query with a base64 Encoded String

If your cluster is running Couchbase Server version 7.6.2 or later, you can use vectors encoded as base64 strings with Vector Search. For example, the following document describes the color `navy`, with base64 encoded strings in the `embedding_vector_dot` and `colorvect_l2` fields instead of arrays:

```json
{
    "id": "#000080",
    "color": "navy",
    "brightness": 14.592,
    "colorvect_l2": "AACA",
    "wheel_pos": "other",
    "verbs": [
        "deep",
        "rich",
        "sophisticated"
    ],
    "description": "Navy is a deep, rich color that exudes sophistication. It is a dark shade of blue that is often associated with authority, stability, and elegance. Navy is a versatile color that can be both bold and understated, making it a popular choice in fashion and interior design. It is a timeless color that never goes out of style and adds a touch of sophistication to any look or space.",
    "embedding_model": "text-embedding-ada-002-v2",
    "embedding_vector_dot": "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"
},
```

The following query uses a base64 encoded string for the same query as [Running a Semantic Search Query with a Large Embedding Vector](#large) to return the document for `navy`:

```json
{
    "fields": ["*"],
    "knn": [
      {
        "field": "embedding_vector_dot",
        "k": 3,
        "vector_base64": "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"
      }
    ]
}
```

|  | You can use base64 encoded strings in your Vector Search queries only if your documents use base64 encoded strings, indexed with the **vector\_base64** field data type. You cannot search for and return vectors you indexed as arrays with the **vector** field data type by using a Search query with a base64 encoded string. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#next-steps)Next Steps

If you do not get the search results you were expecting, you can change the [JSON payload for your Search query](../search/search-request-params.md).

You can also [customize your Search index](../search/customize-index.md) with additional features.

Either of the example queries on this page can also be used with the [REST API](run-vector-search-rest-api.md) to run a search.