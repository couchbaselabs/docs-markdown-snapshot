[View original HTML](/couchbase-lite/3.3/java/working-with-vector-search.html)

> Use Vector Search with Full Text Search and Query. 

## [](#use-vector-search)Use Vector Search

To configure a project to use vector search, follow the [installation instructions](gs-install.md) to add the Vector Search extension.

|  | You must install Couchbase Lite to use the Vector Search extension. |
|  | ------------------------------------------------------------------- |

## [](#create-a-vector-index)Create a Vector Index

This method shows how you can create a vector index using the Couchbase Lite Vector Search extension.

```java
        // create the configuration for a vector index named "vector"
        // with 3 dimensions, 100 centroids, no encoding, using cosine distance
        // with a max training size 5000 and amin training size 2500
        // no vector encoding and using COSINE distance measurement
        VectorIndexConfiguration config = new VectorIndexConfiguration("vector", 3L, 100L)
            .setEncoding(VectorEncoding.none())
            .setMetric(VectorIndexConfiguration.DistanceMetric.COSINE)
            .setNumProbes(8L)
            .setMinTrainingSize(2500L)
            .setMaxTrainingSize(5000L);
```

First, initialize the `config` object with the `VectorIndexConfiguration()` method with the following parameters:

* The expression of the data as a vector.
* The width or `dimensions` of the vector index is set to `3`.
* The amount of `centroids` is set to `100`. This means that there will be one hundred buckets with a single centroid each that gathers together similar vectors.

You can also alter some optional config settings such as `encoding`. From there, you create an index within a given collection, in this case `colors_index`, using the previously generated `config` object.

|  | The number of vectors, the width or dimensions of the vectors and the training size can incur high CPU and memory costs as the size of each variable increases. This is because the training vectors have to be resident on the machine. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#vector-index-configuration)Vector Index Configuration

The table below displays the different configurations you can modify within your `VectorIndexConfiguration()` function. For more information on specific configurations, see [Vector Search.](vector-search.md)

__Table 1\. Vector Index Configuration Options__
| Configuration Name   | Is Required                | Default Configuration                                                                                                                                              | Further Information                                                                                                                                                                                                                                                     |
| -------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Expression           | ![yes](../_images/yes.png) | No default                                                                                                                                                         | A SQL++ expression indicating where to get the vectors. A document property for embedded vectors or prediction() to call a registered Predictive model.                                                                                                                 |
| Number of Dimensions | ![yes](../_images/yes.png) | No default                                                                                                                                                         | 2-4096                                                                                                                                                                                                                                                                  |
| Number of Centroids  | ![yes](../_images/yes.png) | No default                                                                                                                                                         | 1-64000\. The general guideline is an approximate square root of the number of documents                                                                                                                                                                                |
| Distance Metric      | ![no](../_images/no.png)   | Squared Euclidean Distance (euclideanSquared)                                                                                                                      | You can set the following alternates as your Distance Metric: cosine (1 - Cosine similarity) Euclidean dot (negated dot product)                                                                                                                                        |
| Encoding             | ![no](../_images/no.png)   | Scalar Quantizer(SQ) or SQ-8 bits                                                                                                                                  | There are three possible configurations: None No compression, No data loss Scalar Quantizer (SQ) or SQ-8 bits (Default) Reduces the number of bits per dimension Product Quantizer (PQ) Reduces the number of dimensions and bits per dimension                         |
| Training Size        | ![no](../_images/no.png)   | The default values for both the minimum and maximum training size is zero. The training size is calculated based on the number of Centroids and the encoding type. | The guidelines for the minimum and maximum training size are as follows: The minimum training size is set to 25x the number of Centroids or 2 PQ’s bits when PQ is used The maximum training size is set to 256x the number of Centroids or 2 PQ’s bits when PQ is used |
| NumProbes            | ![no](../_images/no.png)   | The default value is 0\. The number of Probes is calculated based on the number of Centroids                                                                       | A guideline for setting a custom number of probes is at least 8 or 0.5% the number of Centroids                                                                                                                                                                         |
| isLazy               | ![no](../_images/no.png)   | False                                                                                                                                                              | Setting the value to true will enable lazy mode for the vector index                                                                                                                                                                                                    |

|  | Altering the default training sizes could be detrimental to the accuracy of returned results produced by the model and total computation time. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#generating-vectors)Generating Vectors

You can use two methods to generate vectors in Couchbase Lite:

1. You can call a Machine Learning(ML) model, and embed the generated vectors inside the documents.
2. You can use the `prediction()` function to generate vectors to be indexed for each document at the indexing time.
3. You can use Lazy Vector Index (lazy index) to generate vectors asynchronously from remote ML models that may not always be reachable or functioning, skipping or scheduling retries for those specific cases.

Below are example configurations of the previously mentioned methods.

### [](#create-a-vector-index-with-embeddings)Create a Vector Index with Embeddings

This method shows you how to create a Vector Index with embeddings.

```java
        // create a vector index named "colors_index"
        // in the collection "_default.colors"
        db.getCollection("colors").createIndex(
            "colors_index",
            new VectorIndexConfiguration("vector", 3L, 100L));
```

1. First, create the standard configuration, setting up an expression, number of dimensions and number of centroids for the vector embedding.
2. Next, create a vector index, `colors_index`, on a collection and pass it the configuration.

### [](#create-vector-index-embeddings-from-a-predictive-model)Create Vector Index Embeddings from a Predictive Model

This method generates vectors to be indexed for each document at the index time by using the `prediction()` function. The key difference to note is that the `config` object uses the output of the `prediction()` function as the `expression` parameter to generate the vector index.

```java
        // create a vector index with a simple predictive model
        Database.prediction.registerModel("ColorModel", colorModel);

        db.getCollection("colors").createIndex(
            "colors_pred_index",
            new VectorIndexConfiguration(
                "prediction(ColorModel, {'colorInput': color}).vector",
                3L, 100L));
```

|  | You can use less storage by using the prediction() function as the encoded vectors will only be stored in the index. However, the index time will be longer as vector embedding generation is occurring at run time. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#create-a-lazy-vector-index)Create a Lazy Vector Index

Lazy indexing is an alternate approach to using the standard predictive model with regular vector indexes which handle the indexing process automatically. You can use lazy indexing to use a ML model that is not available locally on the device and to create vector indexes without having vector embeddings in the documents.

```java
        db.getCollection("colors").createIndex(
            "colors_index",
            new VectorIndexConfiguration("color", 3L, 100L)
                .setLazy(true));
```

You can enable lazy vector indexing by setting the `isLazy` property to `true` in your vector index configuration.

|  | Lazy Vector Indexing is opt-in functionality, the isLazy property is set to false by default. |
|  | --------------------------------------------------------------------------------------------- |

### [](#updating-the-lazy-index)Updating the Lazy Index

Below is an example of how you can update your lazy index.

```java
        while (true) {
            try (IndexUpdater updater = col.getIndex("colors_index").beginUpdate(10)) {
                if (updater == null) { break; }
                for (int i = 0; i < updater.count(); i++) {
                    try {
                        // get the color swatch from the updater and send it to the remote model
                        List<Float> embedding = colorModel.getEmbedding(updater.getBlob(i));
                        updater.setVector(embedding, i);
                    }
                    catch (IOException e) {
                        // Bad connection? Corrupted over the wire? Something bad happened
                        // and the vector cannot be generated at the moment: skip it.
                        // The next time beginUpdate() is called, we'll try it again.
                        updater.skipVector(i);
                    }
                }
                // This writes the vectors to the index. You MUST either have set or skipped each
                // of the the vectors in the updater or this call will throw an exception.
                updater.finish();
            }
        }
```

You procedurally update the vectors in the index by looping through the vectors in batches until you reach the value of the `limit` parameter.

The update process follows the following sequence:

1. Get a value for the updater.

  1. If the there is no value for the vector, handle it. In this case, the vector will be skipped and considered the next time `beginUpdate()` is called.

|  | A key benefit of lazy indexing is that the indexing process continues if a vector fails to generate. For standard vector indexing, this will cause the affected documents to be dropped from the indexing process. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
2. Set the vector from the computed vector derived from the updater value and your ML model.

  1. If there is no value for the vector, this will result in the underlying document to not be indexed.
3. Once all vectors have completed the update loop, finish updating.

|  | updater.finish() will throw an error if any values inside the updater have not been set or skipped. |
|  | --------------------------------------------------------------------------------------------------- |

## [](#vector-search-sql-support)Vector Search SQL++ Support

Couchbase Lite currently supports Hybrid Vector Search and the `APPROX_VECTOR_DISTANCE()` function.

|  | Similar to the [Full Text Search](fts.md) match() function, the APPROX\_VECTOR\_DISTANCE() function and Hybrid Vector Search cannot use the OR expression with the other expressions in the related WHERE clause. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#use-hybrid-vector-search)Use Hybrid Vector Search

You can use Hybrid Vector Search (Hybrid Search) to perform vector search in conjunction with regular SQL++ queries. With Hybrid Search, you perform vector search on documents that have already been filtered based on criteria specified in the `WHERE` clause.

|  | A LIMIT clause is required for non-hybrid Vector Search, this avoids a slow, exhaustive unlimited search of all possible vectors. |
|  | --------------------------------------------------------------------------------------------------------------------------------- |

### [](#hybrid-vector-search-with-full-text-match)Hybrid Vector Search with Full Text Match

Below is an example of using Hybrid Search with the Full Text `match()` function.

```java
        // Create a hybrid vector search query with full-text's match() that
        // uses the the full-text index named "color_desc_index".
        Query query = db.createQuery(
            "SELECT meta().id, color"
                + " FROM _default.colors"
                + " WHERE MATCH(color_desc_index, $text)"
                + " ORDER BY APPROX_VECTOR_DISTANCE(vector, $vector)"
                + " LIMIT 8");
        Parameters params = new Parameters();
        params.setArray("vectorParam", new MutableArray(colorVector));
        query.setParameters(params);

        try (ResultSet rs = query.execute()) {
            // process results
        }
```

### [](#prediction-with-hybrid-vector-search)Prediction with Hybrid Vector Search

Below is an example of using Hybrid Search with an array of vectors generated by the `Prediction()` function at index time.

```java
        Query query = db.createQuery(
            "SELECT meta().id, color"
                + " FROM _default.colors"
                + " WHERE saturation > 0.5"
                + " ORDER BY APPROX_VECTOR_DISTANCE("
                + "    prediction(ColorModel, {'colorInput': color}).vector,"
                + "    $vectorParam)"
                + " LIMIT 8");
        Parameters params = new Parameters();
        params.setArray("vectorParam", new MutableArray(colorVector));
        query.setParameters(params);

        try (ResultSet rs = query.execute()) {
            // process results
        }
```

## [](#approx%5Fvector%5Fdistancevector-expr-target-vector-metric-nprobes-accurate)`APPROX_VECTOR_DISTANCE(vector-expr, target-vector, [metric], [nprobes], [accurate])`

|  | If you use a different distance metric in the APPROX\_VECTOR\_DISTANCE() function from the one configured in the index, you will receive an error when compiling the query. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| Parameter     | Is Required                | Description                                                                                                                                                                                                                                                                                                                  |
| ------------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| vector-expr   | ![yes](../_images/yes.png) | The expression returning a vector (NOT Index Name). Must match the expression specified in the vector index exactly.                                                                                                                                                                                                         |
| target-vector | ![yes](../_images/yes.png) | The target vector.                                                                                                                                                                                                                                                                                                           |
| metric        | ![no](../_images/no.png)   | Values : "EUCLIDEAN\_SQUARED", “L2\_SQUARED”, “EUCLIDEAN”, “L2”, ”COSINE”, “DOT”. If not specified, the metric set in the vector index is used. If specified, the metric must match with the metric set in the vector index. This optional parameter allows multiple indexes to be attached to the same field in a document. |
| nprobes       | ![no](../_images/no.png)   | Number of buckets to search for the nearby vectors. If not specified, the nprobes set in the vector index is used.                                                                                                                                                                                                           |
| accurate      | ![no](../_images/no.png)   | If not present, false will be used, which means that the quantized/encoded vectors in the index will be used for calculating the distance. IMPORTANT: Only accurate = false is supported                                                                                                                                     |

### [](#use-approx%5Fvector%5Fdistance)Use `APPROX_VECTOR_DISTANCE()`

```java
        // use APPROX_VECTOR_DISTANCE in a query WHERE clause
        Query query = db.createQuery(
            "SELECT meta().id, color"
                + " FROM _default.colors"
                + " WHERE APPROX_VECTOR_DISTANCE(vector, $vectorParam) < 0.5");
        Parameters params = new Parameters();
        params.setArray("vectorParam", new MutableArray(colorVector));
        query.setParameters(params);

        try (ResultSet rs = query.execute()) {
            // process results
        }
```

This function returns the approximate distance between a given vector, typically generated from your ML model, and an array of vectors with size equal to the `LIMIT` parameter, collected by a SQL++ query using `APPROX_VECTOR_DISTANCE()`.

### [](#prediction-with-approx%5Fvector%5Fdistance)Prediction with `APPROX_VECTOR_DISTANCE()`

Below is an example of using `APPROX_VECTOR_DISTANCE()` with an array of vectors generated by the `Prediction()` function at index time.

```java
        // use APPROX_VECTOR_DISTANCE with a predictive model
        Database.prediction.registerModel("ColorModel", colorModel);

        db.getCollection("colors").createIndex(
            "colors_pred_index",
            new VectorIndexConfiguration(
                "prediction(ColorModel, {'colorInput': color}).vector",
                3L, 100L));

        Query query = db.createQuery(
            "SELECT meta().id, color"
                + " FROM _default.colors"
                + " ORDER BY APPROX_VECTOR_DISTANCE("
                + "    prediction(ColorModel, {'colorInput': color}).vector,"
                + "    $vectorParam)"
                + " LIMIT 300");
        Parameters params = new Parameters();
        params.setArray("vectorParam", new MutableArray(colorVector));
        query.setParameters(params);

        try (ResultSet rs = query.execute()) {
            // process results
        }
```

## [](#see-also)See Also

* [Installation Instructions](gs-install.md)
* [Vector Search](vector-search.md)
* [Full Text Search](fts.md)