---
title: Hyperscale Vector Index Reranking and Full Vector Persistence
description: You can enable reranking in queries using a Hyperscale Vector index
  to potentially improve the query results.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/vector-index/pages/hyperscale-reranking.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:vector-index:hyperscale-reranking.adoc[]
---

[View original HTML](/server/current/vector-index/hyperscale-reranking.html)

# Hyperscale Vector Index Reranking and Full Vector Persistence

> You can enable reranking in queries using a Hyperscale Vector index to potentially improve the query results. It uses non-quantized versions of the search and indexed vectors to return more accurate results. After the query locates similar vectors in the index, it performs a second round of comparisons using the full vector values stored in the index to reorder the results. This reranking can make the most relevant vectors to the search vector appear higher in the search results. 

## [](#enabling-reranking)Enabling Reranking

To enable reranking, your index must have a copy of the full vector value in addition to the quantized value. The `CREATE VECTOR INDEX` statement adds this copy of the full vector value to the index by default.

Queries do not perform reranking by default. To enable it, you must pass `TRUE` as the fifth parameter in the `APPROX_VECTOR_DISTANCE` function call in your query.

For example, the following query on the sample RGB dataset does not perform reranking:

```sqlpp
WITH question_vec AS (
        SELECT RAW couchbase_search_query.knn[0].vector  
        FROM `vector-sample`.`color`.`rgb-questions` 
        WHERE meta().id = "#FFFFE0")
    SELECT b.color, b.description, b.id
    FROM `vector-sample`.`color`.`rgb` AS b
    ORDER BY APPROX_VECTOR_DISTANCE(b.embedding_vector_dot, question_vec[0], "l2", 4)
    LIMIT 3;
```

The results of this query are:

```json
[{
        "color": "peach",
        "description": "Peach is a soft and warm color that can enliven any space. It has 
                       a delicate and gentle quality, like the softness of a peach's skin. 
                       This color can soften the harshness of other colors and bring a sense 
                       of warmth and comfort. It is a versatile color that can be both calming 
                       and invigorating, making it a popular choice in interior design. Peach 
                       is a color that evokes feelings of happiness and positivity, making it 
                       a perfect addition to any room.",
        "id": "#FF8C3C"
    },
    {
        "color": "apricot",
        "description": "Apricot is a warm and inviting color, reminiscent of the soft glow of 
                       a sunset. It has the ability to soften the harshness of other colors and 
                       enliven any space it is used in. It is a delicate and soothing hue, 
                       perfect for creating a cozy and welcoming atmosphere.",
        "id": "#FB8737"
    },
    {
        "color": "light yellow",
        "description": "Light yellow is a delicate and gentle color that can soften the overall 
                       tone of a room. It has a bright and cheerful quality that can brighten up 
                       any space. This color also has the ability to illuminate a room, making it 
                       feel more open and airy. Light yellow is a perfect choice for creating 
                       a warm and inviting atmosphere.",
        "id": "#FFFFE0"
    }
]
```

The color that’s most relevant to the search vector, `#FFFFE0` Light Yellow, is third in the results.

The following query enables reranking by passing `TRUE` as the fifth parameter in the `APPROX_VECTOR_DISTANCE` function call:

```sqlpp
WITH question_vec AS (
        SELECT RAW couchbase_search_query.knn[0].vector  
        FROM `vector-sample`.`color`.`rgb-questions` 
        WHERE meta().id = "#FFFFE0")
    SELECT b.color, b.description, b.id
    FROM `vector-sample`.`color`.`rgb` AS b
    ORDER BY APPROX_VECTOR_DISTANCE(b.embedding_vector_dot, question_vec[0], "l2", 4, TRUE)
    LIMIT 3;
```

The results of this query are:

```json
[{
        "color": "peach",
        "description": "Peach is a soft and warm color that can enliven any space. It has 
                       a delicate and gentle quality, like the softness of a peach's skin. 
                       This color can soften the harshness of other colors and bring a sense 
                       of warmth and comfort. It is a versatile color that can be both calming 
                       and invigorating, making it a popular choice in interior design. Peach 
                       is a color that evokes feelings of happiness and positivity, making it 
                       a perfect addition to any room.",
        "id": "#FF8C3C"
    },
    {
        "color": "light yellow",
        "description": "Light yellow is a delicate and gentle color that can soften the overall 
                       tone of a room. It has a bright and cheerful quality that can brighten up 
                       any space. This color also has the ability to illuminate a room, making it 
                       feel more open and airy. Light yellow is a perfect choice for creating a 
                       warm and inviting atmosphere.",
        "id": "#FFFFE0"
    },
    {
        "color": "apricot",
        "description": "Apricot is a warm and inviting color, reminiscent of the soft glow of a 
                       sunset. It has the ability to soften the harshness of other colors and 
                       enliven any space it is used in. It is a delicate and soothing hue, perfect 
                       for creating a cozy and welcoming atmosphere.",
        "id": "#FB8737"
    }
]
```

The result for Light Yellow improved from position 3 to position 2.

## [](#prevent-vector-persistence)Preventing Vector Persistence

Reranking can improve the accuracy of recall in some cases. However, it always decreases queries per second (QPS) when enabled. In many cases, you can achieve acceptable recall accuracy without reranking. See [Reranking](vector-index-best-practices.md#reranking) to learn in which cases reranking is useful.

Storing the full vector significantly increases the size of the index. If you do not plan to use reranking, you can save space in your index by having it not save the full vector value.

To prevent an index from persisting the full vector, set the `persist_full_vector` attribute to `False` in the `WITH` clause of the `CREATE VECTOR INDEX` statement you use to create it:

```sqlpp
WITH {  "dimension":<dimensions> ,
        "similarity":<similarity-function>,
        "description":<algorithm-settings>,
        "persist_full_vector":false
     };
```

The following example creates a Hyperscale Vector index from the example RGB dataset that does not persist the full vector value:

```sqlpp
CREATE VECTOR INDEX `color_desc_hyperscale_no_persist` 
       ON `vector-sample`.`color`.`rgb`(`embedding_vector_dot` VECTOR)
       WITH { "dimension":1536, "similarity":"L2", "description":"IVF8,SQ4", 
              "persist_full_vector": false};
```

The size of the resulting index is much smaller than the index that persists the full vector value (269KiB verses 1.17MiB).

The actual savings you see in your own indexes depends on the number of dimensions in your vectors.