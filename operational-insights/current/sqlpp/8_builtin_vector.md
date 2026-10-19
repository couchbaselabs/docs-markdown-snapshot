---
title: Vector Functions
description: Learn more about the vector search functions available in {sqlppea}.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/sqlpp/pages/8_builtin_vector.adoc
  xref: xref:enterprise-analytics:sqlpp:8_builtin_vector.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/sqlpp/8_builtin_vector.html)

# Vector Functions

> Learn more about the vector search functions available in {sqlppea}. 

Operational Insights vector functions compute a distance, or similarity, value between a stored vector field and a query vector. SQL++ for Operational Insights provides 2 kinds of vector functions:

* **K-nearest neighbor (KNN)** functions compute the exact distance between a pair of vectors. A query that calls one without a matching `VTREE` index applies it to every record in the collection in turn, which scans the whole collection. Use KNN functions when no compatible index exists, or when you need an exact result rather than an approximation.
* **Approximate nearest neighbor (ANN)** functions use a `VTREE` vector index to prune the search to a subset of clusters, trading a small amount of recall for query speed. For more information about creating a `VTREE` index, see [CREATE a Vector Index](5%5Fddl%5Fvector%5Findex.md).

The examples in this topic use an `Entertainment.Movie` collection, containing movie records with an `embedding` field. This example field is a 384-dimensional array of floating point numbers derived by embedding each movie's title and overview.

## [](#cosine%5Fsimilarity)cosine\_similarity

Computes the exact cosine similarity between `vector1` and `vector2`. Unlike a distance function, a higher `cosine_similarity` value indicates a closer match.

### [](#syntax)Syntax

```SQL++
 cosine_similarity(vector1, vector2)
```

### [](#arguments)Arguments

* `vector1` is the first vector, expressed as an array of floating point numbers.
* `vector2` is the second vector, expressed as an array of floating point numbers.

### [](#return-value)Return Value

* A floating point number between -1 and 1 representing the cosine similarity between `vector1` and `vector2`.
* `missing`, if either vector argument is `missing`.
* `null`, if either vector argument is `null`.
* An empty result, with a warning, if either vector argument has the wrong (non-numeric) data type, or the 2 vectors have mismatched dimensions.

### [](#example)Example

```SQL++
 USE Entertainment;

 LET qvec = [ /* 384-dimensional float array */ ];

 FROM Movie mov
 LET sim = cosine_similarity(mov.embedding, qvec)
 SELECT mov.id, mov.title, mov.release_date, sim
 ORDER BY sim DESC
 LIMIT 50;
```

## [](#dot%5Fproduct)dot\_product

Computes the dot product between `vector1` and `vector2`.

### [](#syntax-2)Syntax

```SQL++
 dot_product(vector1, vector2)
```

### [](#arguments-2)Arguments

* `vector1` is the first vector, expressed as an array of floating point numbers.
* `vector2` is the second vector, expressed as an array of floating point numbers.

### [](#return-value-2)Return Value

* A floating point number representing the dot product of `vector1` and `vector2`.
* `missing`, if either vector argument is `missing`.
* `null`, if either vector argument is `null`.
* An empty result, with a warning, if either vector argument has the wrong (non-numeric) data type, or the 2 vectors have mismatched dimensions.

### [](#example-2)Example

```SQL++
 USE Entertainment;

 LET qvec = [ /* 384-dimensional float array */ ];

 FROM Movie mov
 LET dist = dot_product(mov.embedding, qvec)
 SELECT mov.id, mov.title, mov.release_date, dist
 ORDER BY dist
 LIMIT 50;
```

## [](#euclidean%5Fdistance)euclidean\_distance

Computes the Euclidean, or L2, distance between `vector1` and `vector2`.

### [](#syntax-3)Syntax

```SQL++
 euclidean_distance(vector1, vector2)
```

### [](#arguments-3)Arguments

* `vector1` is the first vector, expressed as an array of floating point numbers.
* `vector2` is the second vector, expressed as an array of floating point numbers.

### [](#return-value-3)Return Value

* A floating point number representing the Euclidean distance between `vector1` and `vector2`.
* `missing`, if either vector argument is `missing`.
* `null`, if either vector argument is `null`.
* An empty result, with a warning, if either vector argument has the wrong (non-numeric) data type, or the 2 vectors have mismatched dimensions.

### [](#example-3)Example

```SQL++
 USE Entertainment;

 LET qvec = [ /* 384-dimensional float array */ ];

 FROM Movie mov
 LET dist = euclidean_distance(mov.embedding, qvec)
 SELECT mov.id, mov.title, mov.release_date, dist
 ORDER BY dist
 LIMIT 50;
```

## [](#euclidean%5Fsquared%5Fdistance)euclidean\_squared\_distance

Computes the squared Euclidean, or L2 squared, distance between `vector1` and `vector2`. Squared Euclidean distance omits the final square root calculation, so it's cheaper to compute than `euclidean_distance` while preserving the same distance ordering.

### [](#syntax-4)Syntax

```SQL++
 euclidean_squared_distance(vector1, vector2)
```

### [](#arguments-4)Arguments

* `vector1` is the first vector, expressed as an array of floating point numbers.
* `vector2` is the second vector, expressed as an array of floating point numbers.

### [](#return-value-4)Return Value

* A floating point number representing the squared Euclidean distance between `vector1` and `vector2`.
* `missing`, if either vector argument is `missing`.
* `null`, if either vector argument is `null`.
* An empty result, with a warning, if either vector argument has the wrong (non-numeric) data type, or the 2 vectors have mismatched dimensions.

### [](#example-4)Example

```SQL++
 USE Entertainment;

 LET qvec = [ /* 384-dimensional float array */ ];

 FROM Movie mov
 LET dist = euclidean_squared_distance(mov.embedding, qvec)
 SELECT mov.id, mov.title, mov.release_date, dist
 ORDER BY dist
 LIMIT 50;
```

## [](#vector%5Fdistance)vector\_distance

Computes the exact distance between `vector1` and `vector2`. Use `vector_distance` for an exact K-nearest neighbor (KNN) result, or when no applicable `VTREE` index exists.

### [](#syntax-5)Syntax

```SQL++
 vector_distance(vector1, vector2, distance_function)
```

### [](#arguments-5)Arguments

* `vector1` is the first vector, expressed as an array of floating point numbers.
* `vector2` is the second vector, expressed as an array of floating point numbers.
* `distance_function` is a string specifying the distance metric: `cosine`, `dot`, `l2` or `euclidean`, or `l2_squared` or `euclidean_squared`.

### [](#return-value-5)Return Value

* A floating point number representing the exact distance between `vector1` and `vector2`, according to `distance_function`.
* `missing`, if either vector argument is `missing`.
* `null`, if either vector argument is `null`.
* An error, if `distance_function` is invalid.
* An empty result, with a warning, if either vector argument has the wrong (non-numeric) data type, or the 2 vectors have mismatched dimensions.

### [](#example-5)Example

Find the exact 50 nearest movies to a given query vector by cosine distance, without using an index.

```SQL++
 USE Entertainment;

 LET qvec = [ /* 384-dimensional float array */ ];

 FROM Movie mov
 LET dist = vector_distance(mov.embedding, qvec, "cosine")
 SELECT mov.id, mov.title, mov.release_date, dist
 ORDER BY dist
 LIMIT 50;
```

## [](#ann%5Fdistance)ann\_distance

Computes the approximate distance between `vector_field` and `query_vector` when an eligible `VTREE` index exists and applies to the query. Otherwise, computes the exact distance. `APPROX_VECTOR_DISTANCE` is an alias for `ANN_DISTANCE`.

### [](#syntax-6)Syntax

```SQL++
 ann_distance(vector_field, query_vector, distance_function)
 ann_distance(vector_field, query_vector, distance_function, min_probe_fraction)
 ann_distance(vector_field, query_vector, distance_function, min_probe_fraction, k_multiplier)
```

### [](#arguments-6)Arguments

* `vector_field` is a reference to the vector field to search. It must match the vector field declared when the index was created.
* `query_vector` is the query vector, expressed as an array of floating point numbers.
* `distance_function` is a string specifying the distance metric. It must match the `similarity` parameter used when a `VTREE` index was created in order for the index to be used. Otherwise, the query falls back to exact KNN evaluation. SQL++ for Operational Insights supports `dot` similarity only for normalized embeddings in this release.
* `min_probe_fraction` is optional. It's a float ranging from 0.0 to 1.0 that sets the fraction of the epsilon-narrowed shortlist of leaf-level candidates to probe. If you omit this argument, or pass `0`, Operational Insights uses the index's default probe behavior.  
  
**Default**: `0.75`
* `k_multiplier` is optional. It's an integer that sets how many candidates, expressed as `k` times this multiplier, the ANN operator retrieves from each storage partition before final ranking. If you omit this argument, Operational Insights uses the default multiplier.  
  
**Default**: `1`

### [](#return-value-6)Return Value

* A floating point number representing the distance between `vector_field` and `query_vector`, according to `distance_function`.
* `missing`, if either vector argument is `missing`.
* `null`, if either vector argument is `null`.
* An error, if `distance_function` is invalid.
* An empty result, with a warning, if either vector argument has the wrong (non-numeric) data type, or the 2 vectors have mismatched dimensions.
* If no eligible `VTREE` index exists on `vector_field`, or the query is not shaped to use one, SQL++ for Operational Insights evaluates the query as an exact KNN scan instead.

### [](#example-6)Example

Find the 50 movies with an embedding closest to a given query vector, using cosine distance and the index's default probe settings.

```SQL++
 USE Entertainment;

 LET qvec = [ /* 384-dimensional float array */ ];

 FROM Movie mov
 LET dist = ann_distance(mov.embedding, qvec, "cosine")
 SELECT mov.id, mov.title, mov.release_date, dist
 ORDER BY dist
 LIMIT 50;
```

Trade off slower performance for higher recall by probing an extra 20% of the VTREE search's candidate cluster shortlist and doubling the number of candidates retrieved from each storage partition before performing the final ranking.

```SQL++
 USE Entertainment;

 LET qvec = [ /* 384-dimensional float array */ ];

 FROM Movie mov
 LET dist = ann_distance(mov.embedding, qvec, "cosine", 0.2, 2)
 SELECT mov.id, mov.title, mov.release_date, dist
 ORDER BY dist
 LIMIT 50;
```

## [](#approx%5Fvector%5Fdistance)approx\_vector\_distance

An alias for `ann_distance`. Both names accept the same arguments and return the same result.

### [](#syntax-7)Syntax

```SQL++
 approx_vector_distance(vector_field, query_vector, distance_function)
 approx_vector_distance(vector_field, query_vector, distance_function, min_probe_fraction)
 approx_vector_distance(vector_field, query_vector, distance_function, min_probe_fraction, k_multiplier)
```

## [](#isvector)isvector

Returns whether `vec` is a usable vector, meaning a non-empty array whose elements are all numeric values, of a given length when you specify `dimension`. A record whose vector field satisfies `isvector` is eligible to be indexed with a `VTREE` index. `IS_VECTOR` is an alias for `ISVECTOR`.

### [](#syntax-8)Syntax

```SQL++
 isvector(vec)
 isvector(vec, dimension)
```

### [](#arguments-7)Arguments

* `vec` is any value to test.
* `dimension` is optional. It's an integer specifying the required number of elements.

### [](#return-value-7)Return Value

* `true`, if `vec` is an array whose elements are all numeric values, and, when you specify `dimension`, it has exactly that many elements.
* `false`, if `vec` is a non-`null`, non-`missing` value that's not an array, is an empty array, or contains a non-numeric element. `false` also results when you specify `dimension` and the element count does not match.
* `missing`, if either argument is `missing`.
* `null`, if either argument is `null`.
* An error, if `dimension` is not a numeric value.

### [](#example-7)Example

```SQL++
 isvector([0.2, 0.1, 0.4, 0.3], 4)   -- true
 isvector([0.2, 0.1, 0.3], 4)        -- false, wrong dimension
 isvector([0.2, 0.1, "s", 0.3], 4)   -- false, a string element is not numeric
 isvector([])                        -- false, an empty array is not a vector
```

## [](#see-also)See Also

* [CREATE a Vector Index](5%5Fddl%5Fvector%5Findex.md)