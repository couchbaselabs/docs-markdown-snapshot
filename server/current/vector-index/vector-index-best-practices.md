---
title: Hyperscale and Composite Vector Index Best Practices
description: When creating and querying Hyperscale and Composite Vector indexes,
  you have several options to set that can affect the speed and accuracy of your
  results.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/vector-index/pages/vector-index-best-practices.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:vector-index:vector-index-best-practices.adoc[]
---

[View original HTML](/server/current/vector-index/vector-index-best-practices.html)

# Hyperscale and Composite Vector Index Best Practices

> When creating and querying Hyperscale and Composite Vector indexes, you have several options to set that can affect the speed and accuracy of your results. Couchbase has tested vector indexes to determine how index creation and query settings affect the performance of Hyperscale and Composite Vector indexes. The following sections describe the results of the testing and recommendations based on these results. 

> [!NOTE]
> Most of the tests were performed using the Hyperscale Vector index. However, many of the results also apply to Composite Vector indexes where the two index types share the same settings.

## [](#tune-index-creation)Tune Index Creation

When you create a Hyperscale Vector index, you can set the parameters in the following list. Each has the potential to affect the performance of creating the index and the speed and accuracy of queries that use the index. For more information about these parameters:

* For Composite Vector index, see the [WITH Clause](../n1ql/n1ql-language-reference/createindex.md#index-with) in the [CREATE INDEX](../n1ql/n1ql-language-reference/createindex.md) page of the SQL++ for Query Reference.
* For Hyperscale Vector index, see [WITH Clause](../n1ql/n1ql-language-reference/createvectorindex.md#index-with) in the [CREATE VECTOR INDEX](../n1ql/n1ql-language-reference/createvectorindex.md) page of the SQL++ for Query Reference.

### [](#nlist)nList

The `nList` setting controls the number of clusters (centroids) in the index. You set the `nList` by supplying a value after the `IVF` in the `description` parameter when you create your index. This value affects the accuracy of the index and the speed of queries that use it. The `nList` setting defaults to the number of vectors in the dataset divided by 1000.

For Composite Vector indexes, tests show that increasing `nList` beyond the default does not affect the build time of the index. However, it does improve the queries per second (QPS) that the index can handle. It also lowers the latency of queries that use the index.

Hyperscale Vector indexes tend to perform better with larger centroids (smaller `nList` values). This performance gain has to be balanced against the possibility of increased disk I/O due to centroids having more vectors associated with them.

**Recommendation:** The best practice for the `nList` depends on your vector index type:

* If you find that your Composite Vector index query throughput and latency is not meeting your needs, you can try rebuilding the index with a larger `nList` value.
* For Hyperscale Vector indexes, decrease the `nList` value if your working dataset fits into the bucket’s memory quota. You can also try decreasing the `nList` value if you have fast storage such as NVME connected to a high-speed PCIe interface.

### [](#train%5Flist)train\_list

The `train_list` setting controls the number of vectors that Couchbase Server considers when searching for centroids in the dataset. You set it using the `train_list` argument in the `WITH` clause when you create your index. The default value depends on the size of the dataset:

* If there are less than 10,000 vectors, Couchbase Server samples all of the vectors.
* If there are 10,000 or more vectors, Couchbase Server samples the number of vectors divided by 10 or 10 times the number of centroids, whichever is larger. Couchbase Server limits the trainlist to a maximum of 1 million vectors.

Tests show that increasing the `trainlist` improves QPS and reduces latency, but slightly increases memory usage for the index.

**Recommendation:** if you find that increasing the `nList` does not improve your query performance, you can try increasing the `train_list` value.

The following example demonstrates how to set the `train_list` value when creating a Hyperscale Vector index:

```sqlpp
CREATE VECTOR INDEX `squad-context-index`
ON  `demo`.`squad`.`context`(`vector` VECTOR)
       WITH {  "dimension":384, "similarity":"L2", 
               "description":"IVF,SQ8", 
               "train_list":15000};
```

### [](#partitions)Partitions

The number of partitions the index controls how the index is split among logical shards. This setting affects the scalability, memory distribution, and parallelism of the index. You set this value using the `PARTITION BY` clause in the `CREATE [VECTOR] INDEX` statement. See [Index Partitioning](../n1ql/n1ql-language-reference/index-partitioning.md) for more information about partitioning indexes.

Tests show that increasing the number of partitions linearly reduces both the time it takes to build and train the index and index’s memory use. These changes do not affect the QPS or latency of queries that use the index.

**Recommendation:** if the length of time it takes to build the index or the amount of memory the index uses is a concern, you can try increasing the number of partitions.

### [](#replicas)Replicas

The number of replicas you set affects the fault tolerance, query throughput, and memory footprint of the index. You set this value using the `num_replicas` key in the `WITH` clause when you create or alter your index.

Tests show that increasing the number of replicas linearly increases the QPS and linearly reduces the latency of queries that use the index. However, it also linearly increases the memory footprint of the index. Adding replicas does not affect the time it takes to build the index.

**Recommendation:** if you find that your query throughput or latency is not meeting your needs, you can try increasing the number of replicas for the index if you can afford the additional memory usage.

### [](#quantization)Quantization

Vector indexes always use quantization to compress the vectors they index. Couchbase Server supports two quantization methods: [scalar quantization (SQ)](vectors-and-indexes-overview.md#sq) and [product quantization (PQ)](vectors-and-indexes-overview.md#pq). You set the quantization method using the `description` parameter in the `WITH` clause when you create your index.

Couchbase tested different quantization settings using datasets that differed in size and number of dimensions. The results of these tests appear in the following table:

| Dataset                    | Index Type | Quantization Setting | Build Time               | Memory Use        | Recall Accuracy | QPS            | Latency        |
| -------------------------- | ---------- | -------------------- | ------------------------ | ----------------- | --------------- | -------------- | -------------- |
| 100 million 128 dimensions | Hyperscale | SQ8                  | Lowest                   | Highest           | Best            | Best           | Best           |
| 5 million, 1536 dimensions | Composite  | PQ32x8               | Slightly higher than SQ8 | 75% less than SQ8 | lower than SQ8  | Lower than SQ8 | Lower than SQ8 |

> [!NOTE]
> Couchbase also tested Hyperscale Vector indexes containing 1 billion vectors with 128 dimensions using SQ4 quantization. The results showed acceptable recall accuracy and similar performance to SQ8 on smaller datasets.

**Recommendations:**

* SQ8 provides the best balance between memory use and recall for lower dimensional datasets.
* If you have a low-dimensional dataset that’s in the range of a billion vectors, consider using SQ4 quantization.
* Use PQ for higher-dimensional datasets if you want to reduce memory use and are willing to accept less accurate recall, decreased QPS, and increased latency.

## [](#tune-queries)Tune Queries

When querying a Hyperscale Vector index, you can set several parameters in the `APPROX_VECTOR_DISTANCE` function that affect the performance of the query. The following list describes the parameters you can set in the function:

### [](#nprobes)nProbes

`nProbes` sets the number of centroids in the Hyperscale Vector index to search for similar vectors. You optionally set this value as the fourth parameter in the `APPROX_VECTOR_DISTANCE` function call in your query. The default value for this value is 1, which only searches for similar vectors in the centroid that’s closest to the search vector.

Tests show that increasing `nProbes` beyond the default improves the accuracy of results non-linearly (larger values show diminishing improvements). However, it caused a linear decrease in QPS and increase in latency.

**Recommendation:** if you find that your query recall is not meeting your needs, you can try increasing the `nProbes` value. However, increasing this value reduces QPS and increases latency.

### [](#reranking)Reranking

A query can perform a reranking phase after a vector search. This reranking phase reorders the results by comparing the full vector values of the results to the search vector. See [Hyperscale Vector Index Reranking and Full Vector Persistence](hyperscale-reranking.md) for more information about how reranking works. This setting is off by default. You can enable it by passing `TRUE` as the fifth parameter in the `APPROX_VECTOR_DISTANCE` function call in your query.

Testing shows that enabling reranking improves the accuracy of recall in limited cases and decreases QPS.

**Recommendation:** if you find recall accuracy is not meeting your needs and you’re using SQ4 or PQ128x8 or below quantization, try enabling reranking. You must have your index set to persist the full vector value, which increases memory use.

If you do not enable reranking, consider preventing the persistence of the full vector value in the index to reduce memory and disk use. See [Preventing Vector Persistence](hyperscale-reranking.md#prevent-vector-persistence) to learn how to turn off full vector persistence.

## [](#recall-accuracy)Determine Recall Rate

To understand how well your index and queries are performing, you can determine the recall of your queries. To do this, compare the results of running a query using the `APPROX_VECTOR_DISTANCE` function to the results of running the same query using the `VECTOR_DISTANCE` function. The `VECTOR_DISTANCE` function performs a brute-force full vector comparison, so it returns the most accurate results. Based on the results of this comparison, you can decide whether you need to adjust your index or query settings to improve recall accuracy.

> [!IMPORTANT]
> The `VECTOR_DISTANCE` function is expensive to run because it compares all vectors in the dataset. You should only use it on a testing system with a smaller dataset.

For example, suppose you run the following query against a Hyperscale Vector index:

```sqlpp
WITH question_vec AS (
        SELECT RAW couchbase_search_query.knn[0].vector 
        FROM `vector-sample`.`color`.`rgb-questions` 
        WHERE meta().id = "#87CEEB"
    ), 
colors AS (
    SELECT b.color
    FROM `vector-sample`.`color`.`rgb` AS b
    ORDER BY APPROX_VECTOR_DISTANCE(b.embedding_vector_dot, question_vec[0], "l2")
    LIMIT 10 )
SELECT RAW colors;
```

The results of running this query against the RGB sample dataset are:

```json
[
    [{
            "color": "pale turquoise"
        },
        {
            "color": "slate blue"
        },
        {
            "color": "cadet blue"
        },
        {
            "color": "teal"
        },
        {
            "color": "snow"
        },
        {
            "color": "medium turquoise"
        },
        {
            "color": "slate gray"
        },
        {
            "color": "grey"
        },
        {
            "color": "medium slate blue"
        },
        {
            "color": "linen"
        }
    ]
]
```

You can then run the same query using the `VECTOR_DISTANCE` function to get the most accurate results. The following example uses the `VECTOR_DISTANCE` function instead of the `APPROX_VECTOR_DISTANCE` function:

```sqlpp
WITH question_vec AS (
        SELECT RAW couchbase_search_query.knn[0].vector 
        FROM `vector-sample`.`color`.`rgb-questions` 
        WHERE meta().id = "#87CEEB"
    ), 
colors AS (
    SELECT b.color
    FROM `vector-sample`.`color`.`rgb` AS b
    ORDER BY VECTOR_DISTANCE(b.embedding_vector_dot, question_vec[0], "l2")
    LIMIT 10 )
SELECT RAW colors;
```

Running the query returns the following results:

```json
[
    [{
            "color": "deep sky blue"
        },
        {
            "color": "sky blue"
        },
        {
            "color": "light sky blue"
        },
        {
            "color": "pale turquoise"
        },
        {
            "color": "blue"
        },
        {
            "color": "slate blue"
        },
        {
            "color": "light cyan"
        },
        {
            "color": "cadet blue"
        },
        {
            "color": "light blue"
        },
        {
            "color": "medium blue"
        }
    ]
]
```

You can see the results of the two queries share few common results. You can perform a more complex query that determines the common results between the two queries and calculates the recall rate. The following example executes both of the previous queries as subqueries, then finds the intersection of the results. It calculates the recall rate based on the 10 results the queries return (called the recall@10 due to the sample size):

```sqlpp
-- Get the vector for the question
WITH question_vec AS (
    SELECT RAW couchbase_search_query.knn[0].vector
    FROM `vector-sample`.`color`.`rgb-questions`
    WHERE meta().id = "#87CEEB"
),
-- Exact Search results
GroundTruthResults AS (
    SELECT b.color
    FROM `vector-sample`.`color`.`rgb` AS b
    ORDER BY VECTOR_DISTANCE(b.embedding_vector_dot,
    question_vec[0], "l2") LIMIT 10
),
-- Approximate Search results
ApproximateResults AS (
    SELECT b.color
    FROM `vector-sample`.`color`.`rgb` AS b
    ORDER BY APPROX_VECTOR_DISTANCE(b.embedding_vector_dot,
    question_vec[0], "l2") LIMIT 10
)
SELECT
    -- List the stats based on the merges in the following clauses
    COUNT(DISTINCT gr.color) AS total_returned_items,
    ARRAY_AGG(intersection_results) AS matching_color_list,
    COUNT(DISTINCT intersection_results.color) AS matching_color_count,
    (COUNT(DISTINCT intersection_results.color) * 100.0 / COUNT(DISTINCT gr.color)) AS recall_percentage
FROM
    GroundTruthResults AS gr
LEFT JOIN
    ApproximateResults AS ar ON gr.color = ar.color
LEFT JOIN
    -- Use INTERSECT SELECT to find the shared members of the two result sets
    (SELECT t1.color FROM GroundTruthResults AS t1 INTERSECT SELECT t2.color FROM ApproximateResults AS t2) AS intersection_results
    ON gr.color = intersection_results.color;
```

The result of running the recall rate query is:

```json
[{
    "total_returned_items": 10,
    "matching_color_list": [{
            "color": "cadet blue"
        },
        {
            "color": "pale turquoise"
        },
        {
            "color": "slate blue"
        }
    ],
    "matching_color_count": 3,
    "recall_percentage": 30
}]
```

The recall rate shown in the example is 30%, which indicates poor results.

A low recall rate means you need to perform some tuning to improve the recall accuracy of the query or the index. One way to improve the recall accuracy is to increase the `nProbes` value in the `APPROX_VECTOR_DISTANCE` function call. It increases the number of centroids the query searches for similar vectors. See [nProbes](#nprobes) for more information about this setting. The following example shows how to increase this value to `4` in the approximate vector query:

```sqlpp
WITH question_vec AS (
        SELECT RAW couchbase_search_query.knn[0].vector 
        FROM `vector-sample`.`color`.`rgb-questions` 
        WHERE meta().id = "#87CEEB"
    ), 
colors AS (
    SELECT b.color
    FROM `vector-sample`.`color`.`rgb` AS b
    ORDER BY APPROX_VECTOR_DISTANCE(b.embedding_vector_dot, question_vec[0], "l2", 4)
    LIMIT 10 )
SELECT RAW colors;
```

The results of running the tuned query are:

```json
[
    [{
            "color": "deep sky blue"
        },
        {
            "color": "sky blue"
        },
        {
            "color": "light sky blue"
        },
        {
            "color": "pale turquoise"
        },
        {
            "color": "light cyan"
        },
        {
            "color": "slate blue"
        },
        {
            "color": "blue"
        },
        {
            "color": "cadet blue"
        },
        {
            "color": "light blue"
        },
        {
            "color": "medium blue"
        }
    ]
]
```

The results look more similar to the results of the exact query. To verify, you can re-run the recall rate query using the new `nProbes` value. The following example shows the recall rate query with the `APPROX_VECTOR_DISTANCE` function call updated with the new `nProbes` value:

```sqlpp
-- Get the vector for the question
WITH question_vec AS (
    SELECT RAW couchbase_search_query.knn[0].vector
    FROM `vector-sample`.`color`.`rgb-questions`
    WHERE meta().id = "#87CEEB"
),
-- Exact Search results
GroundTruthResults AS (
    SELECT b.color
    FROM `vector-sample`.`color`.`rgb` AS b
    ORDER BY VECTOR_DISTANCE(b.embedding_vector_dot,
    question_vec[0], "l2") LIMIT 10
),
-- Approximate Search results, this timw with nProbes set to 4:
ApproximateResults AS (
    SELECT b.color
    FROM `vector-sample`.`color`.`rgb` AS b
    ORDER BY APPROX_VECTOR_DISTANCE(b.embedding_vector_dot,
    question_vec[0], "l2", 4) LIMIT 10
)
SELECT
    -- List the stats based on the merges in the following clauses
    COUNT(DISTINCT gr.color) AS total_returned_items,
    ARRAY_AGG(intersection_results) AS matching_color_list,
    COUNT(DISTINCT intersection_results.color) AS matching_color_count,
    (COUNT(DISTINCT intersection_results.color) * 100.0 / COUNT(DISTINCT gr.color)) AS recall_percentage
FROM
    GroundTruthResults AS gr
LEFT JOIN
    ApproximateResults AS ar ON gr.color = ar.color
LEFT JOIN
    -- Use INTERSECT SELECT to find the shared members of the two result sets
    (SELECT t1.color FROM GroundTruthResults AS t1 INTERSECT SELECT t2.color FROM ApproximateResults AS t2) AS intersection_results
    ON gr.color = intersection_results.color;
```

The results of this update are:

```json
[{
    "total_returned_items": 10,
    "matching_color_list": [{
            "color": "blue"
        },
        {
            "color": "cadet blue"
        },
        {
            "color": "deep sky blue"
        },
        {
            "color": "light blue"
        },
        {
            "color": "light cyan"
        },
        {
            "color": "light sky blue"
        },
        {
            "color": "medium blue"
        },
        {
            "color": "pale turquoise"
        },
        {
            "color": "sky blue"
        },
        {
            "color": "slate blue"
        }
    ],
    "matching_color_count": 10,
    "recall_percentage": 100
}]
```

The new recall rate is 100%, which means the result of the change makes the `APPROX_VECTOR_DISTANCE` function as accurate as the `VECTOR_DISTANCE` function. This means the query calling `APPROX_VECTOR_DISTANCE` is now returning the most accurate results possible.