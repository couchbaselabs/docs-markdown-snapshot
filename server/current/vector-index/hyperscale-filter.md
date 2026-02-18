---
title: Use Scalar Columns to Filter Hyperscale Vector Index Scans
description: You can reduce the number of vectors for a query that uses a
  Hyperscale Vector index by adding scalar values.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/vector-index/pages/hyperscale-filter.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/vector-index/hyperscale-filter.html)

# Use Scalar Columns to Filter Hyperscale Vector Index Scans

> You can reduce the number of vectors for a query that uses a Hyperscale Vector index by adding scalar values. A Hyperscale Vector index has a single column that indexes the vector. However, you can include scalar values in the index that you can use to filter the vector search. The index stores these included values along with the vector, but they’re not indexed. 

In your queries that use a Hyperscale Vector index, you add the included scalar values as predicates in the `WHERE` clause. During the index scan, Couchbase Server uses the included scalar values to filter out vectors that do not meet the filter restriction. If the filter matches the entry, Couchbase Server performs the more expensive vector comparison operation to determine the distance between the vector value and the search vector.

## [](#creating-a-hyperscale-vector-index-with-included-scalar-values)Creating a Hyperscale Vector Index with Included Scalar Values

When you create a Hyperscale Vector index, you can add scalar values to the index using the `INCLUDE` clause in the `CREATE VECTOR INDEX` statement.

The following example creates a new Hyperscale Vector index for the `embedding-vector-dot` vector column from the [Hyperscale Vector Index Query Example](hyperscale-vector-index.md#query-example). It also includes the `brightness` key from the document.

```sqlpp
CREATE VECTOR INDEX `color_desc_hyperscale_brightness` 
       ON `vector-sample`.`color`.`rgb`(`embedding_vector_dot` VECTOR)
       INCLUDE (`brightness`)
       WITH { "dimension":1536, "similarity":"L2", "description":"IVF8,SQ4" }
```

This example is the same as the example from [Create Hyperscale Vector Index Example](hyperscale-vector-index.md#examples), except that it adds the `INCLUDE` clause to add the `brightness` key.

## [](#querying-a-hyperscale-vector-index-with-included-scalar-values)Querying a Hyperscale Vector Index with Included Scalar Values

When you query a Hyperscale Vector index, you can use the included scalar values as predicates in the `WHERE` clause of your query. Couchbase Server uses the predicates to filter the results before performing the vector comparison.

The following example performs the same query as the example from [Query with a Hyperscale Vector Index](hyperscale-vector-index.md#query-with-a-hyperscale-vector-index), but adds the `brightness` key as a predicate in the `WHERE` clause:

```sqlpp
WITH question_vec AS (
        SELECT RAW couchbase_search_query.knn[0].vector  
        FROM `vector-sample`.`color`.`rgb-questions` 
        WHERE meta().id = "#87CEEB")
SELECT b.color, b.description, b.brightness
       FROM `vector-sample`.`color`.`rgb` AS b
       WHERE b.brightness > 170.0
       ORDER BY APPROX_VECTOR_DISTANCE(b.embedding_vector_dot, 
       question_vec[0], "l2", 4)  LIMIT 3;
```

The result of running the query is:

```json
[{
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
        "brightness": 188.077
    },
    {
        "color": "light sky blue",
        "description": "Light sky blue is a soft and delicate color that evokes 
                        a sense of tranquility and peace. It is a shade of blue 
                        that is reminiscent of a clear, sunny day with a few fluffy 
                        clouds scattered across the sky. This color is often 
                        associated with feelings of serenity and relaxation, making 
                        it a popular choice for bedrooms and spa-like environments. 
                        The lightness of this shade adds a touch of freshness and 
                        purity, making it a perfect color for creating a calming 
                        and inviting atmosphere.",
        "brightness": 189.787
    },
    {
        "color": "pale turquoise",
        "description": "Pale turquoise is a delicate and soothing color that can be 
                       described as a soft blend of blue and green. It has a calming 
                       effect and can evoke feelings of tranquility and serenity. The 
                       color is often associated with the ocean and can bring to mind 
                       images of clear, tropical waters. It has a gentle and subtle 
                       quality, making it a popular choice for creating a peaceful and 
                       serene atmosphere.",
        "brightness": 219.163
    }
]
```

Querying with the `brightness` attribute changes makes `sky blue` the top result compared to the results from the example in [Query with a Hyperscale Vector Index](hyperscale-vector-index.md#query-with-a-hyperscale-vector-index). The restriction can also make the query faster. On a laptop running a three-node cluster in Docker containers, the query ran in 43 ms versus 219 ms for the query without the filter.