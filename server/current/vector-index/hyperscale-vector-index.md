---
title: Vector Search Using Hyperscale Vector Indexes
description: Hyperscale Vector Indexes are optimized to index a single vector
  column. They offer the highest performance of any index when it comes to
  vector data.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/vector-index/pages/hyperscale-vector-index.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:vector-index:hyperscale-vector-index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/vector-index/hyperscale-vector-index.html)

# Vector Search Using Hyperscale Vector Indexes

> Hyperscale Vector Indexes are optimized to index a single vector column. They offer the highest performance of any index when it comes to vector data. They can scale up to a billion documents containing vectors with a large number of dimensions. 

Because they provide the best performance, consider testing a Hyperscale Vector index for your application before resorting to the other types of indexes. If you find their performance does not meet your needs, then test using a Composite Vector Index or a Search Vector Index.

## [](#how-the-hyperscale-vector-index-works)How the Hyperscale Vector Index Works

The Hyperscale Vector Index primarily relies on data stored in an optimized format on disk. By relying on disk storage, they have lower memory requirements than other index types.

You add a single vector column to a Hyperscale Vector Index. The vector value can be an array of floating point values. You can nest the array in another array as long as you use an [UNNEST clause](../n1ql/n1ql-language-reference/unnest.md) to extract it from the containing array. You can also store the vector in a BASE64 string.

## [](#prerequisites)Prerequisites

Hyperscale Vector Indexes have the following requirements:

* You must have the Index Service enabled on at least one node in your cluster. For more information about how to deploy a new node and Services on your database, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* Your account must have the [Query Manage Index](../learn/security/roles.md#query-manage-index) or an administrator role to be able to create an index.
* You must have a bucket your database. For more information about how to create a bucket, see [Create a Bucket](../manage/manage-buckets/create-bucket.md).
* You have documents in a collection that contain one or more vector embeddings. You can add a single vector to a Hyperscale Vector Index. If your documents contain multiple embedded vectors, you can create multiple indexes — one for each vector attribute.  
Embeddings can be an array of floating point numbers or a base64 encoded string. Couchbase Server does not embed vectors itself. You must use an external embedding model to embed vectors into your data and add them to your documents.
* The vectors you add to an index must contain the same number of dimensions. Also the values in the vector must be 32-bit floating point numbers. If a vector does not meet both of these requirements, the vector index treats it as a NULL value and the document is not added to the index.
* You must know the number of dimensions the vector contains. The embedding model you use to embed the vectors may determine this value for you. For example, OpenAI API’s `text-embedding-ada-002` embedding model creates vectors that have 1536 dimensions.
* You must decide whether you want to use the default distance metric and quantization for your index. By default, a Hyperscale Vector index uses the [Euclidean distance squared](vectors-and-indexes-overview.md#euclidean-squared) metric and [Scalar Quantization (SQ)](vectors-and-indexes-overview.md#sq) with 8 bits per vector dimension (`SQ8`). The metrics affect how the index compares vectors. The quantization determines how much memory your index uses and the amount of processing Couchbase Server must perform to train and search them. See [Vector Similarity Metrics](vectors-and-indexes-overview.md#vector%5Fsimilarity) and [Quantization](vectors-and-indexes-overview.md#quantization) for more information.

### [](#examples-on-this-page)Examples on this Page

You can download a sample dataset to use with the procedure or examples on this page:

[Download color\_data\_2vectors.zip](https://cbc-remote-execution-examples-prod.s3.amazonaws.com/color%5Fdata%5F2vectors.zip)

To get the best results with using the sample data with the examples in this documentation, [import the sample files](../guides/load.md) from the dataset into your database with the following settings:

* Use a bucket called `vector-sample`.
* Use a scope called `color`.
* Use a collection called `rgb` for `rgb.json`.
* To set your document keys, use the value of the `id` field from each JSON document.

## [](#create-index)Create a Hyperscale Vector Index

Use the `CREATE VECTOR INDEX` statement to create a Hyperscale Vector Index. This statement is similar to the `CREATE INDEX` statement that you use to create Global Secondary Indexes (GSI). See [Create Indexes](../guides/create-index.md) for an overview of creating indexes. You must also supply a `WITH` clause to set some additional information about the vector column that the Hyperscale index needs.

The following syntax shows the minimum required parameters to create a Hyperscale Vector index:

```sqlpp
CREATE VECTOR INDEX `<index_name>`
       ON `<collection>`(`<key_name>` VECTOR)
       WITH {"dimension": <dimensions>,
             "similarity": <similarity_metric>,
             "description": <centroids_and_quantization>
        };
```

> [!NOTE]
> This syntax for the `CREATE VECTOR INDEX` shows the minimum required parameters to get you started. For the full syntax, see [CREATE VECTOR INDEX](../n1ql/n1ql-language-reference/createvectorindex.md) in the SQL++ for Query Reference.

The parameters in this statement are:

* `index_name` is a string that sets the name of the index.
* `collection` is the path of the collection to index.
* `key_name` is the name of the key containing the vector that you want to index. The key value must be an array of floating point numbers or a base64 encoded string.
* `dimensions` The number of dimensions in the vector as an integer. The embedded model you use to embed the vectors determines the number of dimensions in the vector.
* `similarity_metric` is a string that sets the distance metric to use when comparing vectors during index creation.  
Couchbase Server uses the following strings to represent the distance metrics:

  * `COSINE`: [Cosine Similarity](vectors-and-indexes-overview.md#cosine)
  * `DOT`: [Dot Product](vectors-and-indexes-overview.md#dot)
  * `L2` or `EUCLIDEAN`: [Euclidean Distance](vectors-and-indexes-overview.md#euclidean)
  * `L2_SQUARED` or `EUCLIDEAN_SQUARED`: [Euclidean Squared Distance](vectors-and-indexes-overview.md#euclidean-squared)  
For the greatest accuracy, use the distance metric you plan to use to query the data.
* `centroids_and_quantization` is a string containing the settings for the quantization and index algorithms. See [Quantization and Centroid Settings](#algo%5Fsettings) in the next section for more information.

### [](#algo%5Fsettings)Quantization and Centroid Settings

When creating an index that includes a vector field, you choose settings that affect how the index processes vectors. The parameter named `description` is the primary setting that controls the quantization and the number of centroids Couchbase Server to create the index. Using it, you control how the index subdivides the dataset to improve performance and how it quantizes vectors to reduce memory and processing requirements.

The `description` parameter is a string in the following format:

```ebnf
description ::= '"' 'IVF' number-of-centroids? ',' ('SQ' sq-settings | 'PQ' pq-settings) '"'
```

The following sections describe the settings for centroids and quantization.

#### [](#number-of-centroids)Number of Centroids

Hyperscale Vector index uses several algorithms to organize its data to improve its performance. One of these algorithms, [Inverted File (IVF)](vectors-and-indexes-overview.md#IVF), has a setting you can adjust to control how it subdivides the dataset. The other algorithms that Hyperscale Vector index uses do not have settings you can adjust.

The key setting for IVF is the number of centroids it allocates for the index. This setting controls how large the centroids are. Larger centroids have more vectors associated with them.

You can have Couchbase Server choose a number of centroids for you by not providing a value after the `IVF` in your `description` parameter. It sets the number of centroids to the number of vectors in the dataset divided by 1000.

You can manually set the number of centroids for the index by adding an integer value after the `IVF` in the `description` parameter. The number of centroids you set manually must be less than the number of vectors in the dataset.

Hyperscale Vector indexes perform better with larger centroids (fewer centroids in the index). They use algorithms to skip vectors that are far away from the search vector, making searches faster even with more vectors per centroid. Having fewer centroids can also speed up the index training process because Couchbase Server has to identify fewer data clusters. However, having more vectors per centroid can result in more disk I/O during searches because each centroid has more data associated with it.

When choosing the number of centroids for your index, consider the following guidelines:

* If the majority of your working data set fits into the bucket’s memory quota, choose a smaller number of centroids for the index. Having more of the working data set in memory reduces disk I/O during searches, making searches faster. Another option is to have the fastest possible storage such as a fast NVME connected to a high-speed PCIe interface.
* If your working data set is much larger than the bucket’s memory quota, choose a larger number of centroids for the index. This setting reduces the number of vectors associated with each centroid, which can reduce disk I/O during searches.

You may need to experiment with different numbers of centroids to find the best setting for your dataset and queries.

See [nList](vector-index-best-practices.md#nlist) for more guidance on choosing the number of centroids for the index.

#### [](#quantization-setting)Quantization Setting

Hyperscale Vector index always uses quantization to reduce the size of vectors stored in the index. You must choose whether the index uses [Scalar Quantization (SQ)](vectors-and-indexes-overview.md#sq) or [Product Quantization (PQ)](vectors-and-indexes-overview.md#pq). See [Quantization](vector-index-best-practices.md#quantization) for guidance on choosing the quantization method for the index.

You select the quantization by adding a comma followed by either `PQ` or `SQ` to the `description` parameter after the IVF setting in the `description` value.

Each quantization method has additional settings explained in the following sections.

##### [](#sq-settings)SQ Settings

For SQ, you set the number of bits the SQ algorithm uses for the bin index value, or the number of bits it uses to store the centroid for each bin. The values for SQ that Couchbase Server supports are:

| Setting | Effect                                                                           |
| ------- | -------------------------------------------------------------------------------- |
| SQ4     | SQ uses a 4-bit index value splitting each vector dimension into 16 subspaces.   |
| SQ6     | SQ uses a 6-bit index value splitting each vector dimension into 64 subspaces.   |
| SQ8     | SQ uses an 8-bit index value splitting each vector dimension into 256 subspaces. |

See [Scalar Quantization](vectors-and-indexes-overview.md#sq) for more information about how SQ works.

##### [](#pq-settings)PQ Settings

If you choose to use PQ in your index, you must set two values:

* The number of subquantizers (number of subspaces PQ splits the vector’s dimensions into) to use. This value must be a divisor of the number of dimensions in the vector. For example, if your vector has 99 dimensions, you can only use the values 3, 9, 11, 33, and 99 for the subquantizers. Using any other value returns an error.
* The number of bits in the centroid’s index value. This value sets the number centroids to find in each subspace. For example, setting this value to 8 has PQ store the index for the centroids in a byte. This results in SQ using 256 centroids per subspace.  
The number of centroids you set using this value must be less than the number of vectors in the dataset. For example, if you choose 32 for the centroid index size, your dataset must have at least 4,294,967,296 vectors in it.

The larger you set either of these values, the more accurate the index’s search results are. The trade-off is that your index is larger, as it has to store data for more centroids. A smaller value results in a smaller index that returns less accurate results.

The format for the PQ settings is:

```ebnf
pq-settings ::= 'PQ' subquantizers 'x' number-of-bits
```

For example, `PQ32x8` has PQ break the vector’s dimensions into 32 subspaces, each of which has 256 centroids. See [Product Quantization](vectors-and-indexes-overview.md#pq) for more information about how PQ works.

#### [](#algorithm-settings-examples)Algorithm Settings Examples

The following table shows several `description` values along with an explanation.

| Setting       | Effect                                                                                                                                                                                                                                                  |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IVF,SQ8       | Couchbase Server chooses the number of centroids the IVF algorithm uses. The index uses Scalar Quantization with an 8-bit index, meaning it breaks each of the vector’s dimensions into 256 bins.                                                       |
| IVF1024,PQ8x8 | IVF uses 1024 centroids to divide the dataset. The index uses Product Quantization. PQ breaks the vector space into 8 subspaces, each of which uses 8-bits to represent centroids in the subspace. This settings means each subspace has 256 centroids. |

### [](#examples)Create Hyperscale Vector Index Example

The examples in this section use a dataset that contains information about colors including a text description of the color. There’s also a field named `couchbase_search_query.knn.vector` that contains an embedded vector for the color description.

You can download a sample dataset to use with the procedure or examples on this page:

[Download color\_data\_2vectors.zip](https://cbc-remote-execution-examples-prod.s3.amazonaws.com/color%5Fdata%5F2vectors.zip)

To get the best results with using the sample data with the examples in this documentation, [import the sample files](../guides/load.md) from the dataset into your database with the following settings:

* Use a bucket called `vector-sample`.
* Use a scope called `color`.
* Use a collection called `rgb` for `rgb.json`.
* To set your document keys, use the value of the `id` field from each JSON document.

The following query returns a sample document from the data in the `vector-sample.color.rgb` collection, truncating the embedded vector to 4 values to make the result readable:

```sqlpp
SELECT 
  d.id,
  d.color,
  d.brightness,
  d.description,
  ARRAY_CONCAT(
    d.embedding_vector_dot[0:4], 
    ["..."]
  ) AS embedding_vector_dot
FROM `vector-sample`.`color`.`rgb` AS d
WHERE d.id = "#87CEEB";
```

The result of running the query is:

```json
[{
    "id": "#87CEEB",
    "color": "sky blue",
    "brightness": 188.077,
    "description": "Sky blue is a calming and serene color that evokes feelings of 
                    tranquility. It is a light shade of blue that resembles the color 
                    of the sky on a clear day. The color is often associated with 
                    peace, relaxation, and a sense of openness. It can also represent 
                    a sense of freedom and endless possibilities, as the sky seems 
                    to stretch on forever. Sky blue is a refreshing and soothing color 
                    that can bring a sense of calmness to any space.",
    "embedding_vector_dot": [
        0.015966663137078285,
        0.018097303807735443,
        -0.005783640779554844,
        -0.020661966875195503,
        "..."
    ]
}]
```

The following example creates an Hyperscale vector index for the vector column named `embedding-vector-dot`.

```sqlpp
CREATE VECTOR INDEX `color_desc_hyperscale` 
       ON `vector-sample`.`color`.`rgb`(`embedding_vector_dot` VECTOR)
       WITH { "dimension":1536, "similarity":"L2", "description":"IVF8,SQ4" }
```

The key pieces of this example are:

* The `CREATE VECTOR INDEX` statement creates a Hyperscale Vector index. This differs from the `CREATE INDEX` statement used to create a Global Secondary Index (GSI).
* The `WITH` clause defines several settings specific to Hyperscale Vector indexes:

  * It uses the Euclidean distance (`l2`) similarity function when locating centroids. This function has high accuracy, which matters in a dataset with only 153 documents.
  * Also, because the dataset is so small, the example sets the `description` to `IVF8,SQ4`. This value has the [inverted file algorithm](vectors-and-indexes-overview.md#IVF) use just 8 centroids. It also uses 4-bit [scalar quantization](vectors-and-indexes-overview.md#sq). These settings limit the fragmentation of the small dataset.

In most cases, you’ll not use these settings in a production environment.

## [](#query-with-a-hyperscale-vector-index)Query with a Hyperscale Vector Index

To use your Hyperscale Vector index, use the `SELECT` statement with an `ORDER BY` clause containing a call to the [APPROX\_VECTOR\_DISTANCE()](../n1ql/n1ql-language-reference/vectorfun.md#approx%5Fvector%5Fdistance) function. The query selects the Hyperscale Vector index when this function includes the vector key that the index covers.

A typical query looks like this:

```sqlpp
SELECT <fields>
       FROM <collection>
       ORDER BY APPROX_VECTOR_DISTANCE(
                <collection-vector-column>,
                <search-vector-value>,
                <distance-metric>,
                <centroids-to-probe>,
                <rerank>,
                <topNScan>
        ) LIMIT <number-of-results>;
```

The `APPROX_VECTOR_DISTANCE` parameters shown in the example are:

* `collection-vector-column` is the name of the key containing the vector in the collection.
* `search-vector-value` is the vector value to search for in the collection column. It can be an array of floating point numbers or a base64 encoded string.
* `distance-metric` is the distance metric to use when comparing the vectors. This value should match the distance metric you used when you created the index.
* `centroids-to-probe` is an optional integer value that sets the number of centroids to probe for matching vectors. By default, the vector search only probes a single centroid.
* `rerank` is an optional Boolean that can only be used when `centroids-to-probe` is specified. It specifies whether the function should use full vectors to achieve better results. For more information, see [Hyperscale Vector Index Reranking and Full Vector Persistence](hyperscale-reranking.md).
* `topNScan` is an optional positive integer that can only be used when `centroids-to-probe` and `rerank` are specified. If specified, it sets the number of records to scan.

Also use a `LIMIT` clause to return just the number of results you need. The query pushes the `LIMIT` clause down into the index scan so that the scan ends after finding the number of matches you need.

> [!NOTE]
> You can also call the function [VECTOR\_DISTANCE()](../n1ql/n1ql-language-reference/vectorfun.md#vector%5Fdistance) to find similar vectors. However, this function does not use the Hyperscale Vector index to perform the vector search. Instead, it performs a brute-force search for similar vectors. It’s useful to measure the recall of your Hyperscale Vector index. See [Determine Recall Rate](vector-index-best-practices.md#recall-accuracy) for more information about measuring recall.

### [](#query-example)Hyperscale Vector Index Query Example

You must supply a vector value in your query that Couchbase Server can compare to the vectors in the index. In actual use, your application generates a vector for the query value using the same embedding model it used to embed the vectors in your documents.

To avoid the complication of calling an embedding model, this example uses embedded vectors in the `rgb_questions.json` file that’s included in `color_data_2vectors.zip`. For this example, the contents of this file are loaded into a collection named `vector-sample.color.rgb-questions`. This collection contains a `question` attribute which is a search prompt for a particular color. The `couchbase_search_query.knn.vector` attribute contains the embedded vector for the `question` attribute. The following query lists several attributes from a document in the collection. It truncates the `couchbase_search_query.knn.vector` attribute to just the first 4 dimensions of the vector for readability:

```sqlpp
SELECT 
  d.id,
  d.question,
  d.wanted_similar_color_from_search,
  ARRAY_CONCAT(
    d.couchbase_search_query.knn[0].vector[0:4], 
    ["..."]
  ) AS vector
FROM `vector-sample`.`color`.`rgb-questions` AS d
WHERE d.id = "#87CEEB";
```

The output of the query looks like this:

```json
[{
    "id": "#87CEEB",
    "question": "What is the color that is often linked to feelings of peace and 
                tranquility, and is reminiscent of the clear sky on a calm day?",
    "wanted_similar_color_from_search": "sky blue",
    "vector": [
        0.024399276822805405,
        -0.006973916664719582,
        0.025191623717546463,
        -0.02188388630747795,
        "..."
    ]
}]
```

To use the embedded vector, you need to include the `couchbase_search_query.knn.vector` attribute in your query’s `SELECT` statement. You can either directly copy and paste the entire array into your query or use a subquery to retrieve it from the `vector-sample.color.rgb-questions` collection. The following example uses a subquery to get the vector, and also includes the `wanted_similar_color_from_search` attribute in the output which shows you the color that the query should return.

```sqlpp
WITH question_vec AS (
        SELECT RAW couchbase_search_query.knn[0].vector  
        FROM `vector-sample`.`color`.`rgb-questions` 
        WHERE meta().id = "#87CEEB"),
    question_answer AS (
        SELECT wanted_similar_color_from_search
        FROM `vector-sample`.`color`.`rgb-questions` 
        WHERE meta().id = "#87CEEB")
SELECT b.color, b.description, q.wanted_similar_color_from_search  
       FROM `vector-sample`.`color`.`rgb` AS b, question_answer as q
       ORDER BY APPROX_VECTOR_DISTANCE(b.embedding_vector_dot, 
       question_vec[0], "l2", 4)  LIMIT 3;
```

In this example, the `APPROX_VECTOR_DISTANCE` function compares the vector in the `couchbase_search_query.knn.vector` attribute to the vectors in the index. The parameters the example passes to this function are:

* The `embedding-vector-dot` is the name of the indexed vector key in the collection.
* The `couchbase_search_query.knn[0].vector` is the vector search value to compare to the vectors in the index. This value is the result of the subquery that gets the vector from the `rgb-questions` collection.
* `l2` is the distance metric to use.
* `4` is the number of centroids to probe for matching vectors. This value defaults to `1`. This example sets this value to `4` because the dataset is small. In a small dataset, it’s more likely that relevant vectors are not associated with the same centroid. This parameter broadens the search beyond a single centroid to find more relevant vectors. If you re-run the query with the default value of `1`, you’ll see that the results are less relevant.

The result of running the query is:

```json
[{
        "color": "deep sky blue",
        "description": "Deep sky blue is a calming and refreshing color that evokes 
                        feelings of tranquility and peace. It is a shade of blue 
                        that resembles the clear, open sky on a sunny day. This 
                        color is often associated with serenity and relaxation, 
                        making it a popular choice for interior design and clothing. 
                        Its cool and calming nature makes it a perfect color for 
                        creating a peaceful and serene atmosphere.",
        "wanted_similar_color_from_search": "sky blue"
    },
    {
        "color": "sky blue",
        "description": "Sky blue is a calming and serene color that evokes feelings of 
                        tranquility. It is a light shade of blue that resembles the 
                        color of the sky on a clear day. The color is often associated 
                        with peace, relaxation, and a sense of openness. It can also 
                        represent a sense of freedom and endless possibilities, as the 
                        sky seems to stretch on forever. Sky blue is a refreshing and 
                        soothing color that can bring a sense of calmness to any space.",
        "wanted_similar_color_from_search": "sky blue"
    },
    {
        "color": "light sky blue",
        "description": "Light sky blue is a soft and delicate color that evokes a sense of 
                        tranquility and peace. It is a shade of blue that is reminiscent 
                        of a clear, sunny day with a few fluffy clouds scattered across the 
                        sky. This color is often associated with feelings of serenity and 
                        relaxation, making it a popular choice for bedrooms and spa-like 
                        environments. The lightness of this shade adds a touch of freshness 
                        and purity, making it a perfect color for creating a calming and 
                        inviting atmosphere.",
        "wanted_similar_color_from_search": "sky blue"
    }
]
```

The second result, `sky blue`, matches the `wanted_similar_color_from_search` attribute as the most relevant color to the question posed in the `question` attribute. All of the results are still relevant to the question.

### [](#getting-the-vector-distance)Getting the Vector Distance

You can use the `APPROX_VECTOR_DISTANCE` function as a predicate to return the distance between the search vector and the vectors in the index. You may want to get this value when the distance is meaningful, such as when it represents a real-world measurement.

The following example returns the distance between the search vector and the vectors in the index by adding an alias for the results of the `APPROX_VECTOR_DISTANCE` function in the `SELECT` statement as well as the `ORDER BY` clause:

```sqlpp
WITH question_vec AS (
        SELECT RAW couchbase_search_query.knn[0].vector  
        FROM `vector-sample`.`color`.`rgb-questions` 
        WHERE meta().id = "#87CEEB"),
    question_answer AS (
        SELECT wanted_similar_color_from_search
        FROM `vector-sample`.`color`.`rgb-questions` 
        WHERE meta().id = "#87CEEB")
SELECT b.color, b.description, q.wanted_similar_color_from_search, approx_distance  
       FROM `vector-sample`.`color`.`rgb` AS b, question_answer as q, 
       APPROX_VECTOR_DISTANCE(b.embedding_vector_dot, question_vec[0], "l2", 4) 
       as approx_distance
       ORDER BY approx_distance  LIMIT 3;
```

The result of running the query is:

```json
[{
        "color": "deep sky blue",
        "description": "Deep sky blue is a calming and refreshing color that 
                        evokes feelings of tranquility and peace. It is a shade 
                        of blue that resembles the clear, open sky on a sunny 
                        day. This color is often associated with serenity and 
                        relaxation, making it a popular choice for interior 
                        design and clothing. Its cool and calming nature makes 
                        it a perfect color for creating a peaceful and serene 
                        atmosphere.",
        "wanted_similar_color_from_search": "sky blue",
        "approx_distance": 0.5202313646339596
    },
    {
        "color": "sky blue",
        "description": "Sky blue is a calming and serene color that evokes 
                        feelings of tranquility. It is a light shade of blue 
                        that resembles the color of the sky on a clear day. 
                        The color is often associated with peace, relaxation, 
                        and a sense of openness. It can also represent a sense 
                        of freedom and endless possibilities, as the sky seems 
                        to stretch on forever. Sky blue is a refreshing and 
                        soothing color that can bring a sense of calmness to 
                        any space.",
        "wanted_similar_color_from_search": "sky blue",
        "approx_distance": 0.5205406483903239
    },
    {
        "color": "light sky blue",
        "description": "Light sky blue is a soft and delicate color that evokes 
                        a sense of tranquility and peace. It is a shade of blue 
                        that is reminiscent of a clear, sunny day with a few 
                        fluffy clouds scattered across the sky. This color is 
                        often associated with feelings of serenity and 
                        relaxation, making it a popular choice for bedrooms and 
                        spa-like environments. The lightness of this shade adds 
                        a touch of freshness and purity, making it a perfect 
                        color for creating a calming and inviting atmosphere.",
        "wanted_similar_color_from_search": "sky blue",
        "approx_distance": 0.5315537216573907
    }
]
```