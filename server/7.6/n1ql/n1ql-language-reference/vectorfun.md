---
title: Vector Functions
description: Vector functions enable you to work with vector values.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/n1ql/pages/n1ql-language-reference/vectorfun.adoc
  xref: xref:7.6@server:n1ql:n1ql-language-reference/vectorfun.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/n1ql/n1ql-language-reference/vectorfun.html)

# Vector Functions

> Vector functions enable you to work with vector values. 

Vector functions are supported in Couchbase Server 7.6.6 and later.

## [](#vector%5Fdistance)VECTOR\_DISTANCE(`vec`, `queryvec`, `metric`)

### [](#description)Description

Finds the exact distance between a provided vector and the content of a specified field that contains vector embeddings.

### [](#arguments)Arguments

vec

The name of a field that contains vectors. The field must contain an array of 32-bit floating point numbers.

queryvec

An array of 32-bit floating point numbers representing the vector value to search for in the vector field. The array must have the same dimensions as the vector field.

metric

A string representing the distance metric to use when comparing the vectors.

| COSINE                         | [Cosine Similarity](#cosine)                     |
| ------------------------------ | ------------------------------------------------ |
| DOT                            | [Dot Product](#dot)                              |
| L2 EUCLIDEAN                   | [Euclidean Distance](#euclidean)                 |
| L2\_SQUARED EUCLIDEAN\_SQUARED | [Euclidean Squared Distance](#euclidean-squared) |

### [](#return-value)Return Value

Returns a numeric value representing the vector distance. If the vector value is missing, returns MISSING. If the vector value is null, returns NULL.

### [](#examples)Examples

VECTOR\_DISTANCE() Example

The following query finds the exact vector distance between a query vector and three different embedded vectors.

Query

```sqlpp
WITH data AS ([
  {"vector": [1, 2, 3, 4], "similarity": "identical"},
  {"vector": [1, 2, 3, 5], "similarity": "close"},
  {"vector": [6, 7, 8, 9], "similarity": "distant"}
])
SELECT
  similarity,
  VECTOR_DISTANCE(vector, [1, 2, 3, 4], "COSINE") AS cosine,
  VECTOR_DISTANCE(vector, [1, 2, 3, 4], "DOT") AS dot,
  VECTOR_DISTANCE(vector, [1, 2, 3, 4], "L2") AS l2,
  VECTOR_DISTANCE(vector, [1, 2, 3, 4], "L2_SQUARED") AS l2_squared
FROM data;
```

The results show how the distance changes as the similarity decreases.

Results

```json
[
    {
        "similarity": "identical",
        "cosine": 0,
        "dot": -30,
        "l2": 0,
        "l2_squared": 0
    },
    {
        "similarity": "close",
        "cosine": 0.00600091145203363,
        "dot": -34,
        "l2": 1,
        "l2_squared": 1
    },
    {
        "similarity": "distant",
        "cosine": 0.0369131753138463,
        "dot": -80,
        "l2": 10,
        "l2_squared": 100
    }
]
```

## [](#vector%5Fsimilarity)Vector Similarity Metrics

You use metrics (also known as distance functions) to find similar vectors. When you use a vector function, you must specify which metric to use to compare vectors. Each metric works best for certain applications and types of data.

Couchbase Server supports four metrics:

### [](#euclidean)Euclidean Distance

Euclidean Distance (also known as L2) calculates the geometric distance between two vectors by finding the distance between the individual dimensions in the vectors. This method is most sensitive to the distance between the vectors in space, rather than their alignment. It's also sensitive to the scale of the vectors, where the length of one vector versus the other affects the relationship between the vectors. Use this method when the actual distance of the vectors and their magnitudes are important. This method is useful if the distance between vectors represents a real-world value.

> [!NOTE]
> When you select Euclidean Distance or L2 as the metric for a vector index, Couchbase Server internally uses the [Euclidean Squared Distance](#euclidean-squared) metric (explained in the next section) to perform vector comparisons. This approach improves performance because it avoids performing a computationally expensive square root operation. Vector searches using the Euclidean Squared metric return the same relevant vectors and ranking of results as Euclidean Distance. If your query materializes or projects the actual distance between vectors, Couchbase Server calculates the actual Euclidean Distance. For example, if your query returns the distance between vectors as a column, Couchbase Server calculates the square root of the Euclidean Squared distance to return the actual Euclidean Distance.

### [](#euclidean-squared)Euclidean Squared Distance

Euclidean Squared Distance (also known as L2 Squared or L22) is similar to Euclidean Distance. However, it does not take the square root of the sum distances between the vectors:

Euclidean Distance Formula

\\(L2(x, y) = \\sqrt{\\sum\_{i=1}^n (x\_i - y\_i)^2}\\)

Euclidean Squared Distance Formula

\\(L2^2(x, y) = \\sum\_{i=1}^n (x\_i - y\_i)^2\\)

Because it does not take the square root of the sums, Euclidean Squared Distance is faster to calculate than Euclidean Distance. However, it does not represent the actual distance between the vectors. The results of a vector search using L2 Squared as a metric always returns the same rankings that an L2 search returns. In cases where the dimensions of the vectors represent real-world values, L2 is more intuitive to use because it returns the actual distance between the vectors.

Use this method when you need higher performance than Euclidean Distance. It's better in cases when comparing literal distances is less important than performance and where having the ranking of search results is sufficient.

### [](#dot)Dot Product

This metric finds related vectors by comparing the magnitude (length) and alignment of the vectors. Here, the proximity of the vectors in space is less important than whether they point in a similar direction and have the a similar magnitude. Vectors that point in similar directions (have a low angle between them) and have similar magnitude are strongly associated with each other. This method uses the similarity of the vectors' magnitudes to rank their relation.

Use this method for tasks where ranking confidence is key. The magnitude of the vectors is important when determining the strength of the relationship.

### [](#cosine)Cosine Similarity

This metric is similar to the dot product. However, it normalizes the vectors (making them the same length) during comparison. Normalization means their magnitudes are not taken into account, just their alignment. This normalization makes this method better for comparing textual data because it's less sensitive to the length of the data. The magnitude of a vector generated by some text embedding models depend on the length of the source text. Normalizing vector magnitudes emphasizes the semantic meaning when performing comparisons. Therefore, Cosine Similarity can find the semantic relationship between a short question and a long article that's relevant to answering it.

Use this method when you're performing searches that rely on semantic meaning.