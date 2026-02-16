[View original HTML](/couchbase-lite/3.2/csharp/working-with-vector-search.html)

> Use Vector Search with Full Text Search and Query. 

## [](#use-vector-search)Use Vector Search

To configure a project to use vector search, follow the [installation instructions](gs-install.md) to add the Vector Search extension.

|  | You must install Couchbase Lite to use the Vector Search extension. |
|  | ------------------------------------------------------------------- |

## [](#create-a-vector-index)Create a Vector Index

This method shows how you can create a vector index using the Couchbase Lite Vector Search extension.

```csharp
            // Create a vector index configuration for indexing 3 dimensional vectors embedded
            // in the documents' key named "vector" using 2 centroids. The config is customized
            // to use Cosine distance metric, no vector encoding, min training size 100,
            // max training size 200, and number of probes 8.
            var config = new VectorIndexConfiguration("vector", 3, 2)
            {
                DistanceMetric = DistanceMetric.Cosine,
                Encoding = VectorEncoding.None(),
                MinTrainingSize = 100,
                MaxTrainingSize = 200,
                NumProbes = 8
            };
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

You can use the following methods to generate vectors in Couchbase Lite:

1. You can call a Machine Learning(ML) model, and embed the generated vectors inside the documents.
2. You can use the `prediction()` function to generate vectors to be indexed for each document at the indexing time.
3. You can use Lazy Vector Index (lazy index) to generate vectors asynchronously from remote ML models that may not always be reachable or functioning, skipping or scheduling retries for those specific cases.

Below are example configurations of the previously mentioned methods.

### [](#create-a-vector-index-with-embeddings)Create a Vector Index with Embeddings

This method shows you how to create a Vector Index with embeddings.

```csharp
            // Create a vector index configuration for indexing 3 dimensional vectors embedded
            // in the documents' key named "vector" using 2 centroids.
            var config = new VectorIndexConfiguration("color", 3, 100);

            // Create a vector index named "color_index" using the configuration
            var collection = database.GetCollection("colors");
            collection.CreateIndex("colors_index", config);
```

1. First, create the standard configuration, setting up an expression, number of dimensions and number of centroids for the vector embedding.
2. Next, create a vector index, `colors_index`, on a collection and pass it the configuration.

### [](#create-vector-index-embeddings-from-a-predictive-model)Create Vector Index Embeddings from a Predictive Model

This method generates vectors to be indexed for each document at the index time by using the `prediction()` function. The key difference to note is that the `config` object uses the output of the `prediction()` function as the `expression` parameter to generate the vector index.

```csharp
            // Register the predictive model named "ColorModel".
            Database.Prediction.RegisterModel("ColorModel", new ColorModel());

            // Create a vector index configuration with an expression using the prediction
            // function to get the vectors from the registered predictive model.
            var expression = "prediction(ColorModel, {\"colorInput\": color}).vector";
            var config = new VectorIndexConfiguration(expression, 3, 100);

            // Create a vector index from the configuration
            var collection = database.GetCollection("colors");
            collection.CreateIndex("colors_index", config);
```

The section `{\"colorInput\": color}).vector` is broken down into the following components:

1. `colorInput` is derived from a document property to be used in the prediction function.
2. `vector` serves as a key to the result dictionary.
3. Therefore `{\"colorInput\": color}).vector` shows that `colorInput` is an input to the color model provided by the documents with `.vector` being the key used in the dictionary outputted by the `prediction()` function.

|  | You can use less storage by using the prediction() function as the encoded vectors will only be stored in the index. However, the index time will be longer as vector embedding generation is occurring at run time. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#create-a-lazy-vector-index)Create a Lazy Vector Index

Lazy indexing is an alternate approach to using the standard predictive model with regular vector indexes which handle the indexing process automatically. You can use lazy indexing to use a ML model that is not available locally on the device and to create vector indexes without having vector embeddings in the documents.

```csharp
            // Creating a lazy vector index is the same as creating a normal one, except
            // with the IsLazy property set to true
            var config = new VectorIndexConfiguration("vector", 3, 2)
            {
                IsLazy = true
            };
```

You can enable lazy vector indexing by setting the `isLazy` property to `true` in your vector index configuration.

|  | Lazy Vector Indexing is opt-in functionality, the isLazy property is set to false by default. |
|  | --------------------------------------------------------------------------------------------- |

### [](#updating-the-lazy-index)Updating the Lazy Index

Below is an example of how you can update your lazy index.

```csharp
            // Retrieve the index you wish to update
            var index = collection.GetIndex("index-name");

            // Start an update on it (in this case, limit to 50 entries at a time)
            var updater = index.BeginUpdate(50);

            // If updater is null, that means there are no more entries to process
            while (updater != null) {
                using (updater) {
                    // Otherwise, the updater will contain a list of data that needs embeddings generated
                    int i = 0;
                    foreach (var entry in updater) {
                        // The type of entry will depend on what you have set as your index.
                        // In this example, we will assume it was set to a string property.
                        // Let's also assume that if an embedding is not applicable, this
                        // pseudo function returns null
                        try {
                            var embedding = await GenerateEmbedding((string)entry);
                            if (embedding == null) {
                                // No embedding applicable.  Calling SetVector will null will
                                // cause the underlying document to NOT be indexed
                                updater.SetVector(i, null);
                            } else {
                                // Yes this if/else is unneeded, and only to demonstrate the
                                // effect of setting null in SetVector
                                updater.SetVector(i, embedding);
                            }
                        } catch (Exception) {
                            // Bad connection?  Corrupted over the wire?  Something bad happened
                            // and the embedding cannot be generated at the moment.  So skip
                            // this entry.  The next time BeginUpdate is called, it will be considered again
                            updater.SkipVector(i);
                        }
                    }

                    // This writes the vectors to the index.  Disposing it without calling this
                    // will throw out the results without saving.  You MUST have either set or
                    // skipped all the entries inside of the updater or this call will throw an exception.
                    updater.Finish();
                }

                // Ready for the next batch!
                updater = index.BeginUpdate(50);
            }
```

You procedurally update the vectors in the index by looping through the vectors in batches until you reach the value of the `LIMIT` parameter.

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

### [](#approx%5Fvector%5Fdistancevector-expr-target-vector-metric-nprobes-accurate)`APPROX_VECTOR_DISTANCE(vector-expr, target-vector, [metric], [nprobes], [accurate])`

|  | If you use a different distance metric in the APPROX\_VECTOR\_DISTANCE() function from the one configured in the index, you will receive an error when compiling the query. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| Parameter     | Is Required                | Description                                                                                                                                                                                                                                                                                                                  |
| ------------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| vector-expr   | ![yes](../_images/yes.png) | The expression returning a vector (NOT Index Name). Must match the expression specified in the vector index exactly.                                                                                                                                                                                                         |
| target-vector | ![yes](../_images/yes.png) | The target vector.                                                                                                                                                                                                                                                                                                           |
| metric        | ![no](../_images/no.png)   | Values : "EUCLIDEAN\_SQUARED", “L2\_SQUARED”, “EUCLIDEAN”, “L2”, ”COSINE”, “DOT”. If not specified, the metric set in the vector index is used. If specified, the metric must match with the metric set in the vector index. This optional parameter allows multiple indexes to be attached to the same field in a document. |
| nprobes       | ![no](../_images/no.png)   | Number of buckets to search for the nearby vectors. If not specified, the nprobes set in the vector index is used.                                                                                                                                                                                                           |
| accurate      | ![no](../_images/no.png)   | If not present, false will be used, which means that the quantized/encoded vectors in the index will be used for calculating the distance. IMPORTANT: Only accurate = false is supported                                                                                                                                     |

This function returns the approximate distance between a given vector, typically generated from your ML model, and an array of vectors with size equal to the `LIMIT` parameter, collected by a SQL++ query using `APPROX_VECTOR_DISTANCE()`.

Below are examples of valid and invalid use of Hybrid Search.

```csharp
            // Combining vector search logic with other logic makes a hybrid query
            var sql = """
                      SELECT color 
                      FROM colors 
                      WHERE APPROX_VECTOR_DISTANCE(vector, $vector) < 0.5 AND group = 'group1'
                      LIMIT 10
                      """;

            var query = database.CreateQuery(sql);

            // Setting the vector ommitted for brevity (see other examples)
```

You can see a combination of SQL++ and the `APPROX_VECTOR_DISTANCE()` function to form a hybrid query. The key difference between an invalid and valid hybrid query is that you cannot use `OR` with the `WHERE` clause as it is not supported.

The example below showcases the necessity of the `LIMIT` clause.

```csharp
            // To avoid an accidental resource intensive exhaustive search of the
            // database, a LIMIT clause it required for non-hybrid vector search
            // queries

            // This will work
            var sql = "SELECT id, color, approx_vector_distance(vector, $vector) " +
                      "FROM _default.colors " +
                      "LIMIT 8";

            var query = database.CreateQuery(sql);

            // This will not
            sql = "SELECT id, color, approx_vector_distance(vector, $vector) " +
                      "FROM _default.colors ";

            query = database.CreateQuery(sql);
```

The `LIMIT` clause is required for all non-hybrid Vector Search queries to prevent accidental, exhaustive, slow, and resource intensive searches of the database.

### [](#hybrid-vector-search-with-full-text-match)Hybrid Vector Search with Full Text Match

Below is an example of using Hybrid Search with the Full Text `match()` function.

```csharp
            // The following shows using Full Text Search and Vector Search
            // in the same query.  Note that this example doesn't show
            // setting up the full text index 'desc-index'.
            var sql = """
                      SELECT color 
                      FROM colors 
                      WHERE MATCH(desc-index, $text) AND group = 'group1'
                      ORDER BY APPROX_VECTOR_DISTANCE(vector, $vector)
                      """;

            var query = database.CreateQuery(sql);
```

## [](#see-also)See Also

* [Installation Instructions](gs-install.md)
* [Vector Search](vector-search.md)
* [Full Text Search](fts.md)