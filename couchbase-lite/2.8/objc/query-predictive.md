---
title: Predictive Query
description: Couchbase mobile database predictive query concepts
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/objc/pages/query-predictive.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@couchbase-lite:objc:query-predictive.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/objc/query-predictive.html)

# Predictive Query

> Description — _Couchbase mobile database predictive query concepts_  

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

### [](#integrate-the-model)Integrate the Model

To integrate a model with Couchbase Lite, you must implement the `PredictiveModel` interface which has only one function called `predict()`.

```objc
// `myMLModel` is a fake implementation
// this would be the implementation of the ml model you have chosen
@interface myMLModel : NSObject

+ (NSDictionary*)predictImage: (NSData*)data;

@end

@interface ImageClassifierModel : NSObject <CBLPredictiveModel>

- (nullable CBLDictionary*) predict: (CBLDictionary*)input;

@end

@implementation ImageClassifierModel

- (nullable CBLDictionary*) predict: (CBLDictionary*)input; {
    CBLBlob* blob = [input blobForKey:@"photo"];

    NSData* imageData = blob.content;
    // `myMLModel` is a fake implementation
    // this would be the implementation of the ml model you have chosen
    NSDictionary* modelOutput = [myMLModel predictImage:imageData];

    CBLMutableDictionary* output = [[CBLMutableDictionary alloc] initWithData: modelOutput];
    return output; (1)
}

@end
```

| **1** | The predict(input) -> output method provides the input and expects the result of using the machine learning model. The input and output of the predictive model is a DictionaryObject. Therefore, the supported data type will be constrained by the data type that the DictionaryObject supports. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#register-the-model)Register the Model

To register the model you must create a new instance and pass it to the `Database.prediction.registerModel` static method.

```objc
ImageClassifierModel* model = [[ImageClassifierModel alloc] init];
[[CBLDatabase prediction] registerModel:model withName:@"ImageClassifier"];
```

### [](#create-an-index)Create an Index

Creating an index for a predictive query is highly recommended. By computing the predictions during writes and building a prediction index, you can significantly improve the speed of prediction queries (which would otherwise have to be computed during reads).

There are two types of indexes for predictive queries:

* [Value Index](#value-index)
* [Predictive Index](#predictive-index)

#### [](#value-index)Value Index

The code below creates a value index from the "label" value of the prediction result. When documents are added or updated, the index will call the prediction function to update the label value in the index.

```objc
CBLQueryExpression* input = [CBLQueryExpression dictionary: @{@"photo":[CBLQueryExpression property:@"photo"]}];
CBLQueryPredictionFunction* prediction = [CBLQueryFunction predictionUsingModel:@"ImageClassifier" input:input];

CBLValueIndex* index = [CBLIndexBuilder valueIndexWithItems:@[[CBLValueIndexItem expression:[prediction property:@"label"]]]];
[database createIndex:index withName:@"value-index-image-classifier" error:&error];
```

#### [](#predictive-index)Predictive Index

Predictive Index is a new index type used for predictive query. The Predictive Index is different from the value index in that the Predictive Index caches the predictive result and creates the value index from the cached predictive result when the predictive results values are specified.

The code below creates a predictive index from the "label" value of the prediction result.

```objc
CBLQueryExpression* input = [CBLQueryExpression dictionary:@{@"photo":[CBLQueryExpression property:@"photo"]}];

CBLPredictiveIndex* index = [CBLIndexBuilder predictiveIndexWithModel:@"ImageClassifier" input:input properties:nil];
[database createIndex:index withName:@"predictive-index-image-classifier" error:&error];
```

### [](#run-a-prediction-query)Run a Prediction Query

The code below creates a query that calls the prediction function to return the "label" value for the first 10 results in the database.

```objc
CBLQueryExpression* input = [CBLQueryExpression dictionary: @{@"photo":[CBLQueryExpression property:@"photo"]}];
CBLQueryPredictionFunction* prediction = [CBLQueryFunction predictionUsingModel:@"ImageClassifier" input:input]; (1)

CBLQueryExpression* condition = [[[prediction property:@"label"] equalTo:[CBLQueryExpression string:@"car"]]
                                 andExpression:[[prediction property:@"probablity"] greaterThanOrEqualTo:[CBLQueryExpression double:0.8]]];
CBLQuery* query = [CBLQueryBuilder select: @[[CBLQuerySelectResult all]]
                                     from: [CBLQueryDataSource database:database]
                                    where: condition];

// Run the query.
CBLQueryResultSet *result = [query execute:&error];
NSLog(@"Number of rows :: %lu", (unsigned long)[[result allResults] count]);
```

| **1** | The PredictiveModel.predict() method returns a constructed Prediction Function object which can be used further to specify a property value extracted from the output dictionary of the PredictiveModel.predict() function. The null value returned by the prediction method will be interpreted as MISSING value in queries. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#unregister-the-model)Unregister the Model

To unregister the model you must call the `Database.prediction.unregisterModel` static method.

```objc
[[CBLDatabase prediction] unregisterModelWithName:@"ImageClassifier"];
```

### [](#integrate-a-model-with-coremlpredictivemodel-ios-only)Integrate a Model with CoreMLPredictiveModel (iOS only)

`CoreMLPredictiveModel` is a Core ML based implementation of the `PredictiveModel` protocol that facilitates the integration of Core ML models with Couchbase Lite.

The following example describes how to load a Core ML model using `CoreMLPredictiveModel`. All other steps (register, indexing, query, unregister) are the same as with a model that is integrated using your own `PredictiveModel` implementation.

```objc
// Load MLModel from `ImageClassifier.mlmodel`
NSURL* modelURL = [[NSBundle mainBundle] URLForResource:@"ImageClassifier" withExtension:@"mlmodel"];
NSURL* compiledModelURL = [MLModel compileModelAtURL:modelURL error:&error];
MLModel* model = [MLModel modelWithContentsOfURL:compiledModelURL error:&error];
CBLCoreMLPredictiveModel* predictiveModel = [[CBLCoreMLPredictiveModel alloc] initWithMLModel:model];

// Register model
[[CBLDatabase prediction] registerModel:predictiveModel withName:@"ImageClassifier"];
```