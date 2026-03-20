---
title: Filtered Search Using Composite Vector Indexes
description: A Composite Vector index is a Global Secondary Index (GSI) with a
  single vector column that combines scalar queries with semantic search.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/vector-index/pages/composite-vector-index.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:vector-index:composite-vector-index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/vector-index/composite-vector-index.html)

# Filtered Search Using Composite Vector Indexes

> A Composite Vector index is a Global Secondary Index (GSI) with a single vector column that combines scalar queries with semantic search. The added vector column lets your application perform a query using both the index’s scalar, array, and object index entries to pre-filter the dataset before performing a vector similarity search. 

## [](#how-the-composite-vector-indexs-vector-column-works)How the Composite Vector Index’s Vector Column Works

The Composite Vector index’s single vector column enables semantic and similarity searches within your SQL++ queries. When creating the index, you use a `VECTOR` key attribute to identify the key that contains the embedded vectors.

When your query contains an embedded vector, the Index Service uses any non-vector predicates in the query to filter index entries. Then it performs a vector similarity search to locate semantically related vectors. Handling the non-vector predicates first reduces the number of vector similarity comparisons the Index Service must do to find similar vectors.

## [](#prerequisites)Prerequisites

* You must have the Index Service enabled on at least one node in your cluster. For more information about how to deploy a new node and Services on your database, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* You must have a bucket with scopes and collections in your database. For more information about how to create a bucket, see [Create a Bucket](../manage/manage-buckets/create-bucket.md).
* Your account must have the [Query Manage Index](../learn/security/roles.md#query-manage-index) or an administrator role to be able to create an index.
* You have documents in a collection that contain one or more vector embeddings. You can add a single vector to a Composite Vector index. If your documents contain multiple embedded vectors, you can create multiple indexes — one for each vector attribute.  
Embeddings can be an array of floating point numbers or a base64 encoded string. Couchbase Server does not embed vectors itself. You must use an external embedding model to embed vectors into your data and add them to your documents.
* You must know the number of dimensions the vector contains. The embedding model you use to embed the vectors may determine this value for you. For example, OpenAI API’s `text-embedding-ada-002` embedding model that embedded the sample data demonstrated later in this page creates vectors that have 1536 dimensions.
* You must decide what distance metric and quantization you want your index to use. The metrics affect how the index compares vectors. The quantization determines how much memory your index uses and the amount of processing Couchbase Server must perform to train and search them. See [Vector Similarity Metrics](vectors-and-indexes-overview.md#vector%5Fsimilarity) and [Quantization](vectors-and-indexes-overview.md#quantization) for more information.

### [](#examples-on-this-page)Examples on this Page

You can download a sample dataset to use with the procedure or examples on this page:

[Download color\_data\_2vectors.zip](https://cbc-remote-execution-examples-prod.s3.amazonaws.com/color%5Fdata%5F2vectors.zip)

To get the best results with using the sample data with the examples in this documentation, [import the sample files](../guides/load.md) from the dataset into your database with the following settings:

* Use a bucket called `vector-sample`.
* Use a scope called `color`.
* Use a collection called `rgb` for `rgb.json`.
* To set your document keys, use the value of the `id` field from each JSON document.

## [](#create-index)Create a Composite Vector Index

Creating a Composite Vector index is similar to creating a non-vector GSI index. See [Create Indexes](../guides/create-index.md) for an overview of creating indexes. In the `CREATE INDEX` statement to create the Composite Vector index, add the `VECTOR` key attribute after the vector’s key name to declare it as an embedded vector.

The index key that refers to a vector field may be the only index key. If there are multiple index keys, the index key referring to the vector field may be any of the index keys, including the leading index key.

You must also use the [WITH](../n1ql/n1ql-language-reference/createindex.md#index-with) clause to specify some additional information for the vector column. The format for this clause with the most commonly used parameters is:

```sqlpp
WITH {"dimension": <dimensions>,
      "similarity": <similarity_metric>,
      "description": <centroids_and_quantization>
     };
```

> [!NOTE]
> The `WITH` clause can contain other parameters that affect how the index processes vectors. For a full list of the parameters that affect a Composite Vector index, see [CREATE INDEX](../n1ql/n1ql-language-reference/createindex.md) in the SQL++ for Query Reference.

* `dimensions` is an integer value that sets the number of dimensions in the vector. This value is set by the embedded model you used to embed the vectors.
* `similarity_metric` is a string that sets the distance metric to use when comparing vectors during index creation.  
Couchbase Server uses the following strings to represent the distance metrics:

  * `COSINE`: [Cosine Similarity](vectors-and-indexes-overview.md#cosine)
  * `DOT`: [Dot Product](vectors-and-indexes-overview.md#dot)
  * `L2` or `EUCLIDEAN`: [Euclidean Distance](vectors-and-indexes-overview.md#euclidean)
  * `L2_SQUARED` or `EUCLIDEAN_SQUARED`: [Euclidean Squared Distance](vectors-and-indexes-overview.md#euclidean-squared)  
For the greatest accuracy, use the distance function you plan to use when querying vector data.
* `centroids_and_quantization` is a string containing the settings for the quantization and index algorithms. See [Quantization and Centroid Settings](#algo%5Fsettings) in the next section for more information.

### [](#algo%5Fsettings)Quantization and Centroid Settings

When creating an index that includes a vector field, you choose settings that affect how the index processes vectors. The parameter named `description` is the primary setting that controls the quantization and the number of centroids Couchbase Server to create the index. Using it, you control how the index subdivides the dataset to improve performance and how it quantizes vectors to reduce memory and processing requirements.

The `description` parameter is a string in the following format:

```ebnf
description ::= '"' 'IVF' number-of-centroids? ',' ('SQ' sq-settings | 'PQ' pq-settings) '"'
```

The following sections describe the settings for centroids and quantization.

#### [](#number-of-centroids)Number of Centroids

Composite Vector index uses several algorithms to organize its data to improve its performance. One of these algorithms, [Inverted File (IVF)](vectors-and-indexes-overview.md#IVF), has a setting you can adjust to control how it subdivides the dataset. The other algorithms that Composite Vector index uses do not have settings you can adjust.

The key setting for IVF is the number of centroids it allocates for the index. This setting controls how large the centroids are. Larger centroids have more vectors associated with them.

You can have Couchbase Server choose a number of centroids for you by not providing a value after the `IVF` in your `description` parameter. It sets the number of centroids to the number of vectors in the dataset divided by 1000.

You can manually set the number of centroids for the index by adding an integer value after the `IVF` in the `description` parameter. The number of centroids you set manually must be less than the number of vectors in the dataset.

The number of centroids affects the performance of your Composite Vector index index in two ways:

* If the index has fewer centroids, each centroid is larger (has more vectors associated with it). In this case, a vector search has to perform more comparisons, making the search slower. However, having fewer centroids decreases the processing required to train the index.
* A greater number of centroids results in a greater processing cost for training. This increase is due to the training process having to search for more data cluster to identify more centroids. However, it reduces the number of vectors associated with each centroid. This reduction makes search faster by limiting the number of vector comparisons during a search.

You may need to experiment with different numbers of centroids to find the best setting for your dataset and queries.

See [nList](vector-index-best-practices.md#nlist) for more guidance on choosing the number of centroids for the index.

#### [](#quantization-setting)Quantization Setting

Composite Vector index always uses quantization to reduce the size of vectors stored in the index. You must choose whether the index uses [Scalar Quantization (SQ)](vectors-and-indexes-overview.md#sq) or [Product Quantization (PQ)](vectors-and-indexes-overview.md#pq). See [Quantization](vector-index-best-practices.md#quantization) for guidance on choosing the quantization method for the index.

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

### [](#examples)Examples

The following examples show you how to create two Composite Vector index with a vector column using sample data. They both use the data from the `color_data_2vectors.zip` file mentioned earlier.

The following query gets a single document from the `rgb` collection in the `vector-sample` bucket’s `color` scope. It truncates the `embedding_vector_dot` attribute to the first four values to improve readability.

```sqlpp
SELECT RAW OBJECT_PUT(d, "embedding_vector_dot",
  ARRAY_CONCAT(d.embedding_vector_dot[0:4], ["..."])
)
FROM `vector-sample`.`color`.`rgb` AS d
USE KEYS ["#FFEFD5"];
```

The result of running this query is:

```json
[{
    "brightness": 240.82,
    "color": "papaya whip",
    "colorvect_l2": [
        255,
        239,
        213
    ],
    "description": "Papaya whip is a soft and mellow color that can be 
                   described as a light shade of peach or coral. It has 
                   a calming and soothing effect, similar to the tropical 
                   fruit it is named after. This color is perfect for 
                   creating a warm and inviting atmosphere, and it pairs 
                   well with other pastel shades or neutral tones. Papaya 
                   whip is a versatile color that can be used in both fashion 
                   and interior design, adding a touch of elegance and 
                   sophistication to any space.",
    "embedding_model": "text-embedding-ada-002-v2",
    "embedding_vector_dot": [
        -0.014644118957221508,
        0.017003899440169334,
        -0.013450744561851025,
        0.0021356006618589163,
        "..."
    ],
    "id": "#FFEFD5",
    "verbs": [
        "soften",
        "mellow",
        "lighten"
    ],
    "wheel_pos": "other"
}]
```

#### [](#index-the-rgb-values)Index the RGB Values

The `rgb.json` file’s `colorvect_l2` attribute defines an array containing the RGB values for the entry’s color. While this technically is not an embedded vector, you can still create a vector index column for this array. The following example creates a Composite Vector index for this attribute as an embedded vector as well as the color’s name and brightness.

```sqlpp
CREATE INDEX `color_vectors_idx` ON `vector-sample`.`color`.`rgb`
       (`colorvect_l2` VECTOR, color, brightness)
       WITH {  "dimension":3 , "similarity":"L2", "description":"IVF,SQ8"};
```

In this example:

* The number of dimensions is 3, because there are three values in the array containing the RGB value.
* The similarity function is `L2`. This function works well to find related vectors which are close by the search vector. In this example, finding similar colors depends more on proximity than the magnitude or alignment of the vectors. See [Vector Similarity](vectors-and-indexes-overview.md#vector%5Fsimilarity) for a comparison of similarity functions.
* The `description` lets Couchbase Server decide the number of centroids for the IVF algorithm. It also chooses to use Scalar Quantization with an 8-bit index, splitting each dimension into 256 bins. This setting does not actually save any space in the index, as each of the RGB dimensions are already 8-bit values. However, in this example, memory use is not a concern as the dataset is small.

The result of running example is:

```json
[
  {
    "id": "f572fa0b1c7358ee",
    "name": "color_vectors_idx",
    "state": "online"
  }
]
```

#### [](#create-a-composite-vector-index-using-the-embedded-vectors)Create a Composite Vector Index Using the Embedded Vectors

The `embedding_vector_dot` attribute contains the embedded vectors for the text in the `description` attribute. The data sample shown in [Examples](#examples) truncated this attribute to several values. The embedded vector contains 1536 dimensions.

The following example creates a Composite Vector index that indexes the embedded vectors in the `embedding_vector_dot` as well as indexing the scalar `color` that contains the color’s name and `brightness`.

```sqlpp
CREATE INDEX `color_desc_idx` ON `vector-sample`.`color`.`rgb` 
     (`embedding_vector_dot` VECTOR, color, brightness) 
     WITH { "dimension":1536, "similarity":"DOT", "description":" IVF,SQ8" }
```

This example uses the Dot Product similarity function. This function works better with the embedded text content than the Euclidean function used in the previous example. It also uses the same algorithms as the previous example — Couchbase Server chooses the number of centroids, and uses SQ quantization with 256 bins.

If successful, Couchbase Server responds with:

```json
[
  {
    "id": "c965205718c3e4c2",
    "name": "color_desc_idx",
    "state": "online"
  }
]
```

After Couchbase Server creates the index, it begins training it. Depending on your system, this training can take several seconds.

#### [](#create-a-composite-vector-index-with-a-scalar-leading-key)Create a Composite Vector Index with a Scalar Leading Key

If a Composite Vector index has multiple index keys, the leading index key may be a scalar field, rather than the vector field. This enables the Index Service to pre-filter using a scalar field. This is a key advantage that a Composite Vector index has over a Hyperscale Vector index with included scalar fields.

The following example creates a Composite Vector index that indexes the scalar `color` and brightness fields, as well as the embedded vectors in the `embedding_vector_dot` field.

```sqlpp
CREATE INDEX `color_name_idx` ON `vector-sample`.`color`.`rgb`
     (color, brightness, `embedding_vector_dot` VECTOR)
     WITH { "dimension":1536, "similarity":"DOT", "description":" IVF,SQ8" }
```

If successful, Couchbase Server responds with:

```json
[
  {
    "id": "45222612ffac4e98",
    "name": "color_name_idx",
    "state": "online"
  }
]
```

After Couchbase Server creates the index, it begins training it. Depending on your system, this training can take several seconds.

## [](#query-with-a-composite-vector-index)Query with a Composite Vector Index

You query embedded vector attributes to find similar vectors, and therefore similar semantic content. To find the most similar vectors, use an `ORDER BY` clause in your query to return the most relevant vectors first. In this clause, call one of two functions that actually performs the vector comparisons: `APPROX_VECTOR_DISTANCE` or `VECTOR_DISTANCE`. The first of these functions is faster, but less precise. The second is more precise, but slower. Which you choose depends on your use case.

To use your Composite Vector index, use the `SELECT` statement with an `ORDER BY` clause containing a call to the `APPROX_VECTOR_DISTANCE` function. This function selects the Composite Vector index when you query the vector key that the index covers.

You should use a `LIMIT` clause to return just the number of vectors you need. The query pushes the `LIMIT` clause down into the index scan so that the scan ends after finding the required number of matches.

You can also perform vector comparisons using the VECTOR\_DISTANCE function. This function does not select a Hyperscale Vector index or a Composite Vector Index, but performs a brute-force comparison.

### [](#query-rgb-values)Query RGB Values

Querying the RGB values in `rgb.colorvect_l2` requires a vector with only three values. You can just specify the vector by hand. The following example finds colors that are similar to gray, which has an RGB value of 128, 128, 128:

```sqlpp
SELECT b.color, b.colorvect_l2, b.brightness from `rgb` AS b
ORDER BY APPROX_VECTOR_DISTANCE(b.colorvect_l2,[128,128,128],"L2") 
LIMIT 5;
```

The query uses the `APPROX_VECTOR_DISTANCE` function to sort the results. You pass it the vector column to search, the vector to search for (in this case, the array `128, 128, 128`) and the distance function.

For the best accuracy, use the same distance function you specified when creating the Composite Vector index (in this case, `L2`). The query pushes the `LIMIT` clause down into the index scan, so once it finds the 5 entries that satisfy the query, it exits.

The top result is the entry for gray. The other results are all shades of gray:

```json
[{
        "color": "grey",
        "colorvect_l2": [
            128,
            128,
            128
        ],
        "brightness": 128
    },
    {
        "color": "slate gray",
        "colorvect_l2": [
            112,
            128,
            144
        ],
        "brightness": 125.04
    },
    {
        "color": "light slate gray",
        "colorvect_l2": [
            119,
            136,
            153
        ],
        "brightness": 132.855
    },
    {
        "color": "light gray",
        "colorvect_l2": [
            144,
            144,
            144
        ],
        "brightness": 144
    },
    {
        "color": "dim gray",
        "colorvect_l2": [
            105,
            105,
            105
        ],
        "brightness": 105
    }
]
```

You can also add other predicates to help reduce the workload of searching for similar vectors by excluding vectors. The following example searches for colors similar to gray which has an RGB value of 128, 128, 128 and have a brightness greater than 128:

```sqlpp
SELECT b.color, b.colorvect_l2, b.brightness from `rgb` AS b
WHERE b.brightness > 128 
ORDER BY APPROX_VECTOR_DISTANCE(b.colorvect_l2,[128,128,128],"L2") 
LIMIT 5;
```

The result of running this query are:

```json
[{
        "color": "light slate gray",
        "colorvect_l2": [
            119,
            136,
            153
        ],
        "brightness": 132.855
    },
    {
        "color": "light gray",
        "colorvect_l2": [
            144,
            144,
            144
        ],
        "brightness": 144
    },
    {
        "color": "cadet blue",
        "colorvect_l2": [
            95,
            158,
            160
        ],
        "brightness": 139.391
    },
    {
        "color": "rosy brown",
        "colorvect_l2": [
            188,
            143,
            143
        ],
        "brightness": 156.455
    },
    {
        "color": "dark sea green",
        "colorvect_l2": [
            143,
            188,
            143
        ],
        "brightness": 169.415
    }
]
```

### [](#query-the-embedded-vectors)Query the Embedded Vectors

To query the `color_desc_idx` Composite Vector index containing the embedded vector for the description attribute, you must supply a vector. In a production environment, your application calls the same embedding model it called to generate the embedded vectors in your documents to generate a vector for the query value.

For this example, you can use embedded vectors in the `rgb_questions.json` file that’s in the `color_data_2vectors.zip` file. This file contains a `question` attribute containing a search prompt for a particular color. The following query gets a single document from the `rgb_questions` collection in the `vector-sample` bucket’s `color` scope. It truncates the `couchbase_search_query.knn.vector` attribute to the first four values to improve readability.

```sqlpp
SELECT RAW OBJECT_PUT(d, "couchbase_search_query",
  OBJECT_PUT(d.couchbase_search_query, "knn",
    ARRAY OBJECT_PUT(k, "vector",
      ARRAY_CONCAT(k.vector[0:4], ["..."])
    )
    FOR k IN d.couchbase_search_query.knn END
  )
)
FROM `vector-sample`.`color`.`rgb-questions` AS d
USE KEYS ["#FFEFD5"];
```

The result of the query shows the content of one of the documents:

```json
[{
    "couchbase_search_query": {
        "fields": [
            "*"
        ],
        "knn": [{
            "field": "embedding_vector_dot",
            "k": 3,
            "vector": [
                0.005115953739732504,
                0.004331615287810564,
                0.014279481954872608,
                0.000619320897385478,
                "..."
            ]
        }],
        "query": {
            "match_none": {}
        },
        "sort": [
            "-_score"
        ]
    },
    "embedding_model": "text-embedding-ada-002-v2",
    "id": "#FFEFD5",
    "question": "What is the name of the color that is reminiscent of a tropical fruit and has a calming effect, often used in fashion and interior design?",
    "wanted_similar_color_from_search": "papaya whip"
}]
```

The `couchbase_search_query.knn.vector` attribute contains the embedded vector for the `question` attribute.

This example queries the `embedding_vector_dot` column. It appears here with most of the 1536 vectors omitted:

```sqlpp
SELECT b.color, b.description from `rgb` AS b 
order by APPROX_VECTOR_DISTANCE(b.embedding_vector_dot, 
[
            0.005115953739732504,
            0.004331615287810564,
            0.014279481954872608,
            /* long list of vector values omitted */
            -0.005022349301725626,
            0.002007648814469576,
            -0.03757078945636749
          ], "DOT")  LIMIT 3;
```

Click   **View** to see and copy the entire query with all the vectors.

Another option is to import the `rgb_questions.json` file into another collection in the `vector-sample` bucket’s `color` scope named `rgb-questions`. Then you can use a subquery to get the vectors for the question and use it in your query of the `rgb` collection’s `embedding_vector_dot` attribute:

```sqlpp
WITH question_vec AS (
        SELECT RAW couchbase_search_query.knn[0].vector  
        from `vector-sample`.`color`.`rgb-questions` 
        WHERE meta().id = "#FFEFD5")
SELECT b.color, b.description from `rgb` AS b 
order by APPROX_VECTOR_DISTANCE(b.embedding_vector_dot, 
question_vec[0], "DOT")  LIMIT 3;
```

In either case, the results of the query are the same:

```json
[
  {
    "color": "cantalope",
    "description": "The color cantaloupe is a soft and soothing shade that evokes feelings of calmness
    and relaxation. It is a refreshing hue that brings to mind the juicy and sweet fruit it is named
    after. This delicate color is a pale orange with hints of pink, giving it a subtle and gentle
    appearance. It is a perfect color for creating a peaceful and tranquil atmosphere."
  },
  {
    "color": "papaya whip",
    "description": "Papaya whip is a soft and mellow color that can be described as a light shade of
    peach or coral. It has a calming and soothing effect, similar to the tropical fruit it is named
    after. This color is perfect for creating a warm and inviting atmosphere, and it pairs well with
    other pastel shades or neutral tones. Papaya whip is a versatile color that can be used in both
    fashion and interior design, adding a touch of elegance and sophistication to any space."
  },
  {
    "color": "apricot",
    "description": "Apricot is a warm and inviting color, reminiscent of the soft glow of a sunset. It
    has the ability to soften the harshness of other colors and enliven any space it is used in. It is a
    delicate and soothing hue, perfect for creating a cozy and welcoming atmosphere."
  }
]
```

The second result, the color papaya whip, matches the `rgb_questions` collection’s `wanted_similar_color_from_search` attribute.

### [](#adding-a-scalar)Adding a Scalar

Using additional scalar fields in your search can improve your results and reduce the overhead of performing a vector search. For example, filtering on an additional scalar field reduces the number of vectors an index scan has to compare. Searching for scalar values requires less resources than vector searches.

The example that created the `color_desc_idx` index added fields in addition to the `embedding_vector_dot` vector field. The following example adds a filter based on the `brightness` field to reduce the number of vectors that get compared and also improve the results.

The version of the query that performs a subquery of the `rgb-questions` to get the vector value is:

```sqlpp
WITH question_vec AS (
        SELECT RAW couchbase_search_query.knn[0].vector  
        from `vector-sample`.`color`.`rgb-questions` 
        WHERE meta().id = "#FFEFD5")
SELECT b.color, b.description, b.brightness from `rgb` AS b 
WHERE b.brightness > 190.0
order by APPROX_VECTOR_DISTANCE(b.embedding_vector_dot, 
question_vec[0], "DOT")  LIMIT 3;
```

The truncated version of the query is:

```sqlpp
SELECT b.color, b.description from `rgb` AS b 
WHERE brightness > 190.0
ORDER BY APPROX_VECTOR_DISTANCE(b.embedding_vector_dot, 
[
            0.005115953739732504,
            0.004331615287810564,
            0.014279481954872608,
            /* long list of vector values omitted */
            -0.005022349301725626,
            0.002007648814469576,
            -0.03757078945636749
          ], "DOT")  LIMIT 3;
```

Click   **View** to see and copy the entire query with all the vectors.

The results show that this query moves the papaya whip entry to the top.

```json
[{
        "color": "papaya whip",
        "description": "Papaya whip is a soft and mellow color that can be described as a light shade of peach or coral. It has a calming and soothing effect, similar to the tropical fruit it is named after. This color is perfect for creating a warm and inviting atmosphere, and it pairs well with other pastel shades or neutral tones. Papaya whip is a versatile color that can be used in both fashion and interior design, adding a touch of elegance and sophistication to any space.",
        "brightness": 240.82
    },
    {
        "color": "pale turquoise",
        "description": "Pale turquoise is a delicate and soothing color that can be described as a soft blend of blue and green. It has a calming effect and can evoke feelings of tranquility and serenity. The color is often associated with the ocean and can bring to mind images of clear, tropical waters. It has a gentle and subtle quality, making it a popular choice for creating a peaceful and serene atmosphere.",
        "brightness": 219.163
    },
    {
        "color": "light green",
        "description": "Light green is a calming and refreshing color that evokes feelings of tranquility and new beginnings. It is a delicate shade that is often associated with nature and growth. The softness of this color can bring a sense of balance and harmony to any space, making it a popular choice for interior design. Light green is also known to have a rejuvenating effect, making it a perfect color for relaxation and self-care. Its gentle hue can bring a sense of peace and serenity to the mind, body, and soul.",
        "brightness": 199.178
    }
]
```