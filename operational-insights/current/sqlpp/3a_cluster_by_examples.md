---
title: CLUSTER BY Examples
description: Worked examples of the <code>CLUSTER BY</code> clause across
  different collection layouts, and combining <code>CLUSTER BY</code> with
  <code>GROUP BY</code>.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/sqlpp/pages/3a_cluster_by_examples.adoc
  xref: xref:enterprise-analytics:sqlpp:3a_cluster_by_examples.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/sqlpp/3a_cluster_by_examples.html)

# CLUSTER BY Examples

> Worked examples of the `CLUSTER BY` clause across different collection layouts, and combining `CLUSTER BY` with `GROUP BY`. For the `CLUSTER BY` syntax and `WITH` clause parameters, see [CLUSTER BY Clause](3%5Fquery.md#Cluster%5FBy%5Fclauses). 

The examples on this page cluster movies and their reviews by embedding similarity, using 3 different ways a collection can lay out movies, reviews, and their embeddings.

## [](#Design%5F1)Decomposed Collections

In this layout, movies and reviews are stored in 2 separate collections. Each movie has an embedding derived from its poster, and each review has an embedding derived from the text of the review.

movies

```json
{
    "name": "Avengers Endgame",
    "movie_year": "2019",
    "directors": ["Anthony Russo", "Joe Russo"],
    "movie_id": 2,
    "movie_poster": "image",
    "posterEmbedding": [1.9605, 4.4628, -1.7210]
}
```

movie\_reviews

```json
{
    "review": "The movie is filled with strong themes of nationalism and perseverance, making it a memorable movie.",
    "movie_id": 2,
    "review_id": 1,
    "author_id": "auth123",
    "reviewEmbedding": [-1.0164, 2.2702, -7.4882]
}
```

Cluster the reviews of movies released before 2020, and return each cluster's identifier, size, and member reviews.

```SQL++
 FROM movies m, movie_reviews r
 WHERE r.movie_id = m.movie_id AND m.movie_year < 2020
 CLUSTER BY r.reviewEmbedding AS sc
 CLUSTER AS rvc
 WITH {
     "clustering_algorithm": "K-Means",
     "dimension": [3],
     "num_clusters": 5,
     "similarity": "euclidean"
 }
 SELECT sc.cluster_id AS cid, ARRAY_COUNT(rvc) AS cnt, rvc;
```

Result:

[
    {
        "cid": 2,
        "cnt": 5,
        "rvc": [
            {
                "r": {
                    "review": "The movie is filled with strong themes of nationalism and perseverance, making it a memorable movie.",
                    "movie_id": 2,
                    "reviewEmbedding": [-1.0164, 2.2702, -7.4882]
                },
                "m": {
                    "name": "Avengers Endgame",
                    "movie_year": "2019",
                    "directors": ["Anthony Russo", "Joe Russo"],
                    "movie_id": 2,
                    "movie_poster": "image",
                    "posterEmbedding": [1.9605, 4.4628, -1.7210]
                }
            }
        ]
    }
]

## [](#Design%5F2)One Summary Embedding per Movie

In this layout, movies and reviews are stored in a single nested collection, with reviews stored as a nested array of review text. Each movie has 1 review embedding, derived from the entire array of review texts, in addition to its poster embedding. Use this layout to cluster movies by the similarity of their reviews as a whole, rather than by individual reviews.

movies

```json
{
    "name": "Avengers Endgame",
    "movie_year": "2019",
    "directors": ["Anthony Russo", "Joe Russo"],
    "reviews": ["an emotional Marvel movie with great sound track", "terrible movie"],
    "movie_poster": "image",
    "reviewEmbedding": [1.9061, 2.7604, 9.9142],
    "posterEmbedding": [1.9605, 4.4628, -1.7210]
}
```

Cluster movies released before 2020 by the similarity of their summarized reviews.

```SQL++
 FROM movies m
 WHERE m.movie_year < 2020
 CLUSTER BY m.reviewEmbedding AS sc
 CLUSTER AS movieCluster
 WITH {
     "clustering_algorithm": "K-Means",
     "dimension": [3],
     "num_clusters": 5,
     "similarity": "euclidean"
 }
 SELECT sc.cluster_id AS cid, ARRAY_COUNT(movieCluster) AS cnt, movieCluster;
```

Result:

[
    {
        "cid": 2,
        "cnt": 5,
        "movieCluster": [
            {
                "m": {
                    "name": "Avengers Endgame",
                    "movie_year": "2019",
                    "directors": ["Anthony Russo", "Joe Russo"],
                    "reviews": ["an emotional Marvel movie with great sound track", "terrible movie"],
                    "movie_poster": "image",
                    "reviewEmbedding": [1.9061, 2.7604, 9.9142],
                    "posterEmbedding": [1.9605, 4.4628, -1.7210]
                }
            }
        ]
    }
]

## [](#Design%5F3)Per-Review Embeddings

In this layout, movies and reviews are stored in a single nested collection, with reviews stored as a nested array of objects, each pairing a review's text with its own embedding.

movies

```json
{
    "name": "Avengers Endgame",
    "movie_year": "2019",
    "directors": ["Anthony Russo", "Joe Russo"],
    "reviews": [
        {
            "review": "an emotional Marvel movie with great sound track",
            "reviewEmbedding": [1.8065, 1.9672, 1.1618]
        },
        {
            "review": "terrible movie",
            "reviewEmbedding": [-4.6717, -3.8503, 2.2377]
        }
    ],
    "movie_poster": "image",
    "posterEmbedding": [1.9605, 4.4628, -1.7210]
}
```

Cluster individual reviews of movies released before 2020 by similarity, so that each cluster shows which movies received similar reviews.

```SQL++
 FROM movies m, m.reviews re
 WHERE m.movie_year < 2020
 CLUSTER BY re.reviewEmbedding AS sc
 CLUSTER AS rvc
 WITH {
     "clustering_algorithm": "K-Means",
     "dimension": [3],
     "num_clusters": 5,
     "similarity": "euclidean"
 }
 SELECT sc.cluster_id AS cid, ARRAY_COUNT(rvc) AS cnt, rvc;
```

Result:

[
    {
        "cid": 2,
        "cnt": 2,
        "rvc": [
            {
                "m": {
                    "name": "Avengers Endgame",
                    "movie_year": "2019",
                    "directors": ["Anthony Russo", "Joe Russo"],
                    "movie_poster": "image",
                    "posterEmbedding": [1.9605, 4.4628, -1.7210]
                },
                "re": {
                    "review": "an emotional Marvel movie with great sound track",
                    "reviewEmbedding": [1.8065, 1.9672, 1.1618]
                }
            }
        ]
    }
]

## [](#Combining%5Fcluster%5Fby%5Fand%5Fgroup%5Fby)Combining CLUSTER BY and GROUP BY

A query can contain only the `CLUSTER BY` or `GROUP BY` clause, not both. To combine them, cluster in a subquery, then group the subquery's results.

The following example, using the [decomposed collections](#Design%5F1) layout, clusters movie reviews by similarity, then groups the results by movie year, returning the cluster identifier, movie year, and names of the movies in each cluster.

```SQL++
 WITH mc AS (
     FROM movies m, movie_reviews r
     WHERE r.movie_id = m.movie_id
     CLUSTER BY r.reviewEmbedding AS sc
     CLUSTER AS rvc
     WITH {
         "clustering_algorithm": "K-Means",
         "dimension": [3],
         "num_clusters": 5,
         "similarity": "euclidean"
     }
     SELECT sc.cluster_id AS cid, rvc
 )
 FROM mc, mc.rvc AS rvc_i
 GROUP BY rvc_i.m.movie_year, mc.cid
 GROUP AS g
 SELECT mc.cid AS cid, rvc_i.m.movie_year AS year, (SELECT DISTINCT VALUE g.rvc_i.m.name FROM g) AS names;
```

Result:

[
    {
        "cid": 2,
        "year": "2019",
        "names": ["Avengers Endgame", "Terminator"]
    }
]

## [](#Without%5Fcluster%5Fas)Clustering Without CLUSTER AS

Cluster movie reviews by embedding similarity into 5 groups, and return each cluster's identifier and centroid, without retaining the individual reviews.

```SQL++
 FROM movies m, movie_reviews r
 WHERE r.movie_id = m.movie_id AND m.movie_year < 2020
 CLUSTER BY r.reviewEmbedding AS sc
 WITH {
     "clustering_algorithm": "K-Means",
     "dimension": [3],
     "num_clusters": 5,
     "similarity": "euclidean"
 }
 SELECT sc.cluster_id AS cid, sc.centroid;
```

Result:

[
    {
        "cid": 2,
        "centroid": [-1.2807952380952383, -0.8439857142857143, 0.6816]
    }
]

Without `CLUSTER AS`, the query can use only each cluster's `cluster_id` and `centroid`, not the individual records that made up the cluster.

## [](#Filtering%5Fclusters%5Fwith%5Fhaving)Filtering Clusters with HAVING

Cluster movie reviews by embedding similarity into 5 groups, then keep only the clusters that contain a review of a movie directed by a Russo brother. Return each matching cluster's identifier, size, and matching reviews.

```SQL++
 FROM movies m, movie_reviews r
 WHERE r.movie_id = m.movie_id AND m.movie_year < 2020
 CLUSTER BY r.reviewEmbedding AS sc
 CLUSTER AS rvc
 WITH {
     "clustering_algorithm": "K-Means",
     "dimension": [3],
     "num_clusters": 5,
     "similarity": "euclidean"
 }
 HAVING SOME x IN rvc SATISFIES (SOME d IN x.m.directors SATISFIES CONTAINS(d, "Russo"))
 SELECT sc.cluster_id AS cid,
        ARRAY_COUNT(rvc) AS cnt,
        (FROM rvc AS x
         WHERE SOME d IN x.m.directors SATISFIES CONTAINS(d, "Russo")
         SELECT x.m.name AS name, x.r.review_id AS review_id, x.r.review AS review
         ORDER BY review_id) AS russo_reviews
 ORDER BY cid;
```

Result:

[
    {
        "cid": 0,
        "cnt": 28,
        "russo_reviews": [
            {
                "name": "Avengers Endgame",
                "review_id": 4,
                "review": "Avengers Endgame handles grief and love with honesty and never feels manipulative."
            }
        ]
    }
]

The `HAVING` clause runs after clustering, and excludes any cluster whose records do not satisfy its condition, the same way it filters groups after `GROUP BY`.

## [](#see-also)See Also

* [CLUSTER BY Clause](3%5Fquery.md#Cluster%5FBy%5Fclauses)
* [GROUP BY Clause](3%5Fquery.md#Group%5FBy%5Fclauses)
* [HAVING Clause](3%5Fquery.md#Having%5Fclauses)