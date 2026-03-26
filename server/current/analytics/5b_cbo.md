---
title: Cost-Based Optimizer for Analytics
description: The cost-based optimizer for Analytics uses samples to choose the
  optimal plan to execute a query.
editUrl: https://github.com/couchbase/docs-analytics/edit/release/8.0/modules/analytics/pages/5b_cbo.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:analytics:5b_cbo.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/analytics/5b_cbo.html)

# Cost-Based Optimizer for Analytics

The execution plan for a query involves many possible operations: scan, join, filter, and so on. When planning for a query's execution, there are usually several possible choices for each operation, including the use of different indexes or different join methods. Some of the choices will be faster and more efficient than others. The cost-based optimizer (CBO) aims to choose the most efficient option for each.

When generating an execution plan, the cost-based optimizer can do the following:

1. Index selection: the optimizer can select the optimal index for the query.
2. Join method: the optimizer can choose between nested-loop joins, hash joins, and hash broadcast joins. For hash joins, the optimizer can choose which side of the join should be the build side or the probe side.
3. Join enumeration: the optimizer can consider different join orders, and rewrite the query to use the optimal join order.

The cost-based optimizer for Analytics uses sample data taken randomly from each Analytics collection. At query planning time, the optimizer queries the samples, based on the query's single-collection predicates, in order to estimate the number of qualifying objects in each base collection for the query.

The optimizer uses these results to predict the cardinality of each predicate. It uses the cardinality to estimate the cost of different access paths, then compares the estimated cost of the alternatives in order to generate a query execution plan with the lowest expected cost.

## [](#Activation)Turning the Cost-Based Optimizer On or Off

The cost-based optimizer for Analytics is active by default. To turn it off or on, use the `compiler.cbo` configuration parameter.

Note that, in general, the `SET` statement only sets configuration parameters for the current query. It does not enable you to turn off the cost-based optimizer and leave it off permanently.

For more details, see [Cost-Based Optimizer Parameters](appendix%5F2%5Fparameters.md#CBO%5Fparameters).

## [](#Samples)Cost-Based Optimizer Samples

Before you can use the cost-based optimizer with a query, you must first gather the samples that it needs.

You must gather a sample from each Analytics collection that you want to query. You can only gather an optimizer sample from an Analytics collection, not from an Analytics view.

You must periodically refresh the sample for each collection, based on the collection's rate of change and how frequently you need to query each collection.

The query language provides ANALYZE statements which enable you to manage cost-based optimizer samples.

##### AnalyzeStmnt

![AnalyzeCollection | AnalyzeCollectionDrop](_images/diagrams/AnalyzeStmnt.png) 

## [](#Collecting%5Fsamples)Collecting Samples

The ANALYZE ANALYTICS COLLECTION statement collects a sample of randomly-selected records from the specified Analytics collection.

If no sample exists, executing this statement creates one. If one does currently exist, this statement resamples the target collection and replaces the previous sample.

##### AnalyzeCollection

!["ANALYZE" "ANALYTICS" "COLLECTION" QualifiedName ( "WITH" ObjectConstructor )?](_images/diagrams/AnalyzeCollection.png) 

The `QualifiedName` identifies the Analytics collection from which the samples are gathered. It consists of an optional Analytics scope name and the name of the Analytics collection. If no Analytics scope name is given, the Analytics collection is assumed to be in the scope defined by the immediately preceding USE statement, or the scope defined by the `query_context` parameter, or the `Default` Analytics scope, according to the rules for [Resolving Database Entities](appendix%5F3%5Fresolution.md#Resolving%5Fdatabase%5Fentities).

The optional `WITH` clause enables you to specify parameters for the optimizer samples. The `ObjectConstructor` represents an object containing key-value pairs, one for each parameter. The following parameters are available.

| Name                       | Description                                                                                                                                                                                 | Schema                   |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| **sample** _optional_      | Determines the size of the sample. May be one of the following string values: low — 1063 objects medium — 4 × 1063 objects high — 4 × 4 × 1063 objects The default setting is low.          | enum (low, medium, high) |
| **sample-seed** _optional_ | A number used to specify the initial seed for the random sampling process. If specified, the sampling is deterministic. If not specified, the sample is truly random — this is the default. | number                   |

The following example gathers optimizer statistics for the Analytics collection called `travel.route`.

Example

ANALYZE ANALYTICS COLLECTION travel.route;

The following example also gathers optimizer statistics for the Analytics collection called `travel.route`. In this case, the size of the sample is set to `medium`, and the initial seed for the random sampling process is set to `42`.

Example

ANALYZE ANALYTICS COLLECTION travel.route WITH {"sample": "medium", "sample-seed": 42};

## [](#Dropping%5Fsamples)Dropping Samples

The ANALYZE ANALYTICS COLLECTION …​ DROP STATISTICS statement drops samples for a named collection.

##### AnalyzeCollectionDrop

!["ANALYZE" "ANALYTICS" "COLLECTION" QualifiedName "DROP" "STATISTICS"](_images/diagrams/AnalyzeCollectionDrop.png) 

The `QualifiedName` identifies the Analytics collection from which the samples were gathered. It consists of an optional Analytics scope name and the name of the Analytics collection. If no Analytics scope name is given, the Analytics collection is assumed to be in the scope defined by the immediately preceding USE statement, or the scope defined by the `query_context` parameter, or the `Default` Analytics scope, according to the rules for [Resolving Database Entities](appendix%5F3%5Fresolution.md#Resolving%5Fdatabase%5Fentities).

The following example drops optimizer statistics for the Analytics collection called `travel.route`.

Example

ANALYZE ANALYTICS COLLECTION travel.route DROP STATISTICS;

## [](#Metadata)Sample Metadata

Metadata for cost-based optimizer samples can be found in the `` Metadata.`Index` `` collection, identified by `IndexStructure = "SAMPLE"`.

The Index catalog entry for a cost-based optimizer sample contains the following extra fields specific to samples:

* **SampleSeed**: The sample's seed.
* **SampleCardinalityTarget**: The sample's size.
* **SourceCardinality**: The total number of objects in the collection when it was sampled.
* **SourceAvgItemSize**: The average object size (in bytes) in the collection when it was sampled.

The last two attributes are used by the cost-based optimizer to estimate the costs of various query operators based on their input sizes.

## [](#Plans)Cost-Based Optimizer Query Plans

When you run an Analytics query, the cost-based optimizer adds extra information to the query plan.

For each operator, the plan includes an `operator-estimates` section, containing the following fields:

* **cardinality**: The estimated cardinality of the operator.
* **op-cost**: The estimated cost of the operator.
* **total-cost**: The estimated total cost up to the current operator.

For hash joins and hash broadcast joins, the plan includes the following field:

* **build-side**: Indicates the build side of the join. Always has the value `0` to indicate that the first input is the build side.

The `operator-estimates` section and the `build-side` field are also included in the visual query plan.

In the visual query plan, for hash joins and hash broadcast joins, the build side is displayed on the left side of the join and the probe side on the right, assuming that the plan direction is upward.

## [](#Settings)Cost-Based Optimizer Parameters and Hints

The Analytics service provides several compiler parameters which enable you to specify the behavior of the cost-based optimizer, as well as turning it on or off. See [Cost-Based Optimizer Parameters](appendix%5F2%5Fparameters.md#CBO%5Fparameters).

You can also supply hints to the optimizer within a specially-formatted hint comment. These enable you to specify the behavior of the cost-based optimizer within individual queries. See [Cost-Based Optimizer Hints](appendix%5F2%5Fparameters.md#CBO%5Fhints).

## [](#Related%5Flinks)Related Links

The [cost-based optimizer for the Query service](../n1ql/n1ql-language-reference/cost-based-optimizer.md) uses a mix of metadata and data statistics (histograms) to estimate the amount of processing (memory, CPU, network traffic, and I/O) needed for each operation. It considers the estimated cost of the alternatives in order to choose the query execution plan with the least expected cost.