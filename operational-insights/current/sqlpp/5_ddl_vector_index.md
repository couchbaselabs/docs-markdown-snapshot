---
title: CREATE a Vector Index
description: Use a <code>CREATE</code> statement to create a vector index for
  approximate nearest neighbor (ANN) search on a remote or standalone
  collection.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/sqlpp/pages/5_ddl_vector_index.adoc
  xref: xref:enterprise-analytics:sqlpp:5_ddl_vector_index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/sqlpp/5_ddl_vector_index.html)

# CREATE a Vector Index

> Use a `CREATE` statement to create a vector index for approximate nearest neighbor (ANN) search on a remote or standalone collection. 

An Operational Insights vector index, of type `VTREE`, stores the embeddings from a single vector field and organizes them into a routing tree of leaf clusters. The query optimizer uses a `VTREE` index to accelerate approximate nearest neighbor (ANN) queries, pruning the search to a subset of clusters instead of scanning every record. For more information about the query-side functions that use this index, see [Vector Functions](8%5Fbuiltin%5Fvector.md).

An Operational Insights vector index covers only 1 vector field.

> [!IMPORTANT]
> Before you create a vector index on a collection, you must run `ANALYZE COLLECTION` on that collection to gather the samples the index build requires. Creating a vector index on a collection with no samples fails. For more information, see [Collecting Samples](5b%5Fcbo.md#Collecting%5Fsamples).

## [](#syntax)Syntax

**CreateVectorIndex EBNF** 

```EBNF
CreateVectorIndex ::= "CREATE" "INDEX" Identifier ("IF" "NOT" "EXISTS")?
                       "ON" QualifiedName
                       "(" VectorIndexField ")"
                       ("INCLUDE" "(" NestedField ( "," NestedField )* ")")?
                       ("TYPE" "VTREE")?
                       "WITH" ObjectConstructor
```

**CreateVectorIndex Diagram** 

!["CREATE" "INDEX" Identifier ("IF" "NOT" "EXISTS")? "ON" QualifiedName "(" VectorIndexField ")" ("INCLUDE" "(" NestedField ( "," NestedField )* ")")? ("TYPE" "VTREE")? "WITH" ObjectConstructor](_images/CreateVectorIndex.png) 

**Show VectorIndexField Diagram** 

![NestedField "VECTOR"](_images/VectorIndexField.png) 

VectorIndexField

**Show NestedField Diagram** 

![Identifier ( "." Identifier )*](_images/NestedField.png) 

NestedField

## [](#examples)Examples

The following example creates a vector index on the `review_vector_emb` field, specifying only the mandatory `dimension` and `similarity` parameters and omitting the optional `TYPE` clause:

```SQL++
 CREATE INDEX review_vector_idx
 ON products.ptype.product (review_vector_emb VECTOR)
 WITH {"dimension": 384, "similarity": "cosine"};
```

**Show additional examples** 

The following example creates a vector index and uses the `INCLUDE` clause to replicate the `rating` and `genre` fields in the index. A query that filters on `rating` or `genre` and orders by vector distance can then be served entirely from the index, without a lookup against the base collection.

```SQL++
 CREATE INDEX review_vector_idx
 ON products.ptype.product (review_vector_emb VECTOR)
 INCLUDE (rating, genre)
 TYPE VTREE
 WITH {"dimension": 384, "similarity": "cosine"};
```

The following example fine-tunes the index build and storage behavior by overriding the default settings for `train_list_fraction`, `quantization`, `epsilon`, and `num_clusters`:

```SQL++
 CREATE INDEX ix_vtree
 ON Entertainment.Movie (embedding VECTOR)
 INCLUDE (title, vote_average, revenue)
 TYPE VTREE
 WITH {
     "dimension": 384,
     "similarity": "cosine",
     "train_list_fraction": 0.2,
     "quantization": "SQ8",
     "epsilon": 0.25,
     "num_clusters": 1000
 };
```

You can drop a vector index the same way you drop any other index. For more information, see [DROP Statements](5%5Fddl%5Fdrop.md).

```SQL++
 DROP INDEX Entertainment.Movie.ix_vtree IF EXISTS;
```

## [](#arguments)Arguments

Identifier

For the `CREATE INDEX` statement, the first `Identifier` is the index name.

QualifiedName

The `QualifiedName` identifies the collection to build the index on.

VectorIndexField

The `VectorIndexField` consists of a `NestedField` that specifies the vector field to index, followed by the `VECTOR` keyword. The field must contain an array of floating point numbers with the dimensionality specified in the `WITH` clause. You can have only 1 vector field per vector index.

INCLUDE

The optional `INCLUDE` clause replicates the listed non-key fields directly in the vector index. When you omit `INCLUDE`, the index stores only the primary key and the vector field. Replicating fields in the index lets the query optimizer take ANN query paths that filter on those fields from within the closest leaf clusters, instead of looking up each candidate record in the base collection.

Unlike a standard index, do not specify a type for an `INCLUDE` field in a vector index. Specifying a type for an `INCLUDE` field causes a compilation error.

TYPE

The optional `TYPE` clause specifies the index type. `VTREE` is the only supported vector index type, and it's the default when you omit `TYPE`.

WITH

The `WITH` clause is mandatory for a vector index. Its `ObjectConstructor` represents an object containing key-value pairs, one for each parameter. You can define the following parameters:

| Name                              | Description                                                                                                                                                                                                                                           | Schema                                                            |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **dimension**Required             | The dimensionality of the vector field. This specifies the length of the vector arrays stored in the indexed field, such as 384 for a common sentence-transformer model.                                                                              | integer                                                           |
| **similarity**Required            | The distance or similarity metric used to train and query the index. Accepts one of the following string values: euclidean l2 euclidean\_squared l2\_squared cosine dot (supported only for normalized embeddings in this release)                    | enum: euclidean, l2, euclidean\_squared, l2\_squared, cosine, dot |
| **train\_list\_fraction**Optional | The decimal fraction of dataset records, ranging from 0.0 to 1.0, sampled to train the leaf centroid structure during index creation, such as 0.1 for 10% of the dataset. **Default**: 0.1                                                            | float                                                             |
| **quantization**Optional          | The scalar quantization applied to stored vectors to reduce index size and speed up distance computation, at the cost of a small reduction in recall. Accepts SQ4 (4-bit) or SQ8 (8-bit). **Default**: SQ8                                            | enum: SQ4, SQ8                                                    |
| **epsilon**Optional               | A fractional tolerance, greater than 0, that extends the search radius beyond the closest cluster boundary during index insertion and ANN query execution. A larger epsilon increases recall at the cost of visiting more clusters. **Default**: 0.75 | float                                                             |
| **num\_clusters**Optional         | The number of leaf clusters created in each storage partition. **Default**: the square root of the partition's cardinality.                                                                                                                           | integer                                                           |
| **seed**Optional                  | A seed value for the index build's random number generator. Set a specific value to reproduce the same exact index structure each time you create the index. **Default**: a random value, unless you specify one                                      | integer                                                           |

> [!NOTE]
> This parameter table, including the accepted `similarity` values and every default value, reflects the vector search design at the time of writing and is subject to change before general availability. If a record's vector field is `missing`, `null`, of the wrong type, or of the wrong dimensionality, Operational Insights excludes that record's embedding from the index and shows a warning, instead of failing the index build.

## [](#see-also)See Also

* [Vector Functions](8%5Fbuiltin%5Fvector.md)
* [Using Indexes](7%5Fusing%5Findex.md)
* [DROP Statements](5%5Fddl%5Fdrop.md)