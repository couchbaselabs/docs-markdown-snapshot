---
title: Predictive Query&#8201;&#8212;&#8201;Working with Queries
description: Couchbase Lite database data querying concepts -- predictive query
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/android/pages/query-predictive.adoc
  xref: xref:2.8@couchbase-lite:android:query-predictive.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/android/query-predictive.html)

# Predictive Query&#8201;&#8212;&#8201;Working with Queries

> Description — _Couchbase Lite database data querying concepts — predictive query_  
> Related Content — [Indexing](../../current/android/indexing.md) | [Live Query](../../current/android/query-live.md) | [Queries](../../current/android/querybuilder.md)

## [](#overview)Overview

> [!IMPORTANT]
> Enterprise Edition only
> 
> Predictive Query is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature.

Predictive Query enables Couchbase Lite queries to use machine learning, by providing query functions that can process document data (properties or blobs) via trained ML models.

Let's consider an image classifier model that takes a picture as input and outputs a label and probability.

![predictive diagram](../_images/predictive-diagram.png) 

To run a predictive query with a model as the one shown above, you must implement the following steps.

1. [Integrate the Model](#integrate-the-model)
2. [Register the Model](#register-the-model)
3. [Create an Index (Optional)](#create-an-index)
4. [Run a Prediction Query](#run-a-prediction-query)
5. [Unregister the Model](#unregister-the-model)

## [](#integrate-the-model)Integrate the Model

To integrate a model with Couchbase Lite, you must implement the `PredictiveModel` interface which has only one function called `predict()`.

```Java
// `tensorFlowModel` is a fake implementation
// this would be the implementation of the ml model you have chosen
class ImageClassifierModel implements PredictiveModel {
    @Override
    public Dictionary predict(@NonNull Dictionary input) {
        Blob blob = input.getBlob("photo");
        if (blob == null) { return null; }

        // `tensorFlowModel` is a fake implementation
        // this would be the implementation of the ml model you have chosen
        return new MutableDictionary(TensorFlowModel.predictImage(blob.getContent())); (1)
    }
}

class TensorFlowModel {
    public static Map<String, Object> predictImage(byte[] data) {
        return null;
    }
}
```

| **1** | The predict(input) -> output method provides the input and expects the result of using the machine learning model. The input and output of the predictive model is a DictionaryObject. Therefore, the supported data type will be constrained by the data type that the DictionaryObject supports. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#register-the-model)Register the Model

To register the model you must create a new instance and pass it to the `Database.prediction.registerModel` static method.

```Java
Database.prediction.registerModel("ImageClassifier", new ImageClassifierModel());
```

## [](#create-an-index)Create an Index

Creating an index for a predictive query is highly recommended. By computing the predictions during writes and building a prediction index, you can significantly improve the speed of prediction queries (which would otherwise have to be computed during reads).

There are two types of indexes for predictive queries:

* [Value Index](#value-index)
* [Predictive Index](#predictive-index)

### [](#value-index)Value Index

The code below creates a value index from the "label" value of the prediction result. When documents are added or updated, the index will call the prediction function to update the label value in the index.

```Java
ValueIndex index = IndexBuilder.valueIndex(ValueIndexItem.expression(Expression.property("label")));
database.createIndex("value-index-image-classifier", index);
```

### [](#predictive-index)Predictive Index

Predictive Index is a new index type used for predictive query. The Predictive Index is different from the value index in that the Predictive Index caches the predictive result and creates the value index from the cached predictive result when the predictive results values are specified.

The code below creates a predictive index from the "label" value of the prediction result.

```Java
Map<String, Object> inputMap = new HashMap<>();
inputMap.put("numbers", Expression.property("photo"));
Expression input = Expression.map(inputMap);

PredictiveIndex index = IndexBuilder.predictiveIndex("ImageClassifier", input, null);
database.createIndex("predictive-index-image-classifier", index);
```

## [](#run-a-prediction-query)Run a Prediction Query

The code below creates a query that calls the prediction function to return the "label" value for the first 10 results in the database.

```Java
Map<String, Object> inputProperties = new HashMap<>();
inputProperties.put("photo", Expression.property("photo"));
Expression input = Expression.map(inputProperties);
PredictionFunction prediction = PredictiveModel.predict("ImageClassifier", input); (1)

Query query = QueryBuilder
    .select(SelectResult.all())
    .from(DataSource.database(database))
    .where(Expression.property("label").equalTo(Expression.string("car"))
        .and(Expression.property("probability").greaterThanOrEqualTo(Expression.doubleValue(0.8))));

// Run the query.
ResultSet result = query.execute();
Log.d(TAG, "Number of rows: " + result.allResults().size());
```

| **1** | The PredictiveModel.predict() method returns a constructed Prediction Function object which can be used further to specify a property value extracted from the output dictionary of the PredictiveModel.predict() function. The null value returned by the prediction method will be interpreted as MISSING value in queries. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#unregister-the-model)Unregister the Model

To unregister the model you must call the `Database.prediction.unregisterModel` static method.

```Java
Database.prediction.unregisterModel("ImageClassifier");
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Queries](../../current/android/querybuilder.md)
* [Live Query](../../current/android/query-live.md)
* [Predictive Query](#couchbase-lite:android:query-predictive.adoc)
* [Full Text Search](../../current/android/fts.md)

###### [](#-2)

Learn more . . .

* [Databases](../../current/android/database.md)
* [Documents](../../current/android/document.md)
* [Blobs](../../current/android/blob.md)

###### [](#-3)

Dive Deeper . . .

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)