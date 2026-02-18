---
title: "Examples: Using the Eventing Service"
description: This page contains examples of how to use the Eventing Service with
  the Couchbase Web Console.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/eventing/pages/eventing-examples.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/eventing/eventing-examples.html)

# Examples: Using the Eventing Service

> This page contains examples of how to use the Eventing Service with the Couchbase Web Console. 

## [](#examples-step-by-step)Step-by-Step Examples

### [](#Couchbase-Eventing-Examples)Detailed Examples

The following tutorial-like guides have detailed start-to-finish instructions and are ideal for new users to learn the basics of the Eventing Service.

| [Data Enrichment](eventing-example-data-enrichment.md) | [Cascade Delete](eventing-examples-cascade-delete.md)                    | [Document Expiry](eventing-examples-docexpiry.md)       | [Delete v Expiry](eventing-examples-delete-v-expiry.md)              |
| ------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------- | -------------------------------------------------------------------- |
| [Document Archival](eventing-examples-docarchive.md)   | [Cancel or Overwrite Timer](eventing-examples-cancel-overwrite-timer.md) | [Recurring Timer](eventing-examples-recurring-timer.md) | [External REST via cURL GET](eventing-examples-rest-via-curl-get.md) |
| [Risk Assessment](eventing-examples-high-risk.md)      |                                                                          |                                                         |                                                                      |

## [](#examples-scriptlets)Scriptlets

### [](#examples-scriptlets-kv)Basic Accessor Eventing Functions

The following scriptlets are examples of standadlone Eventing Functions.

| [basicBucketOps](eventing-handler-basicBucketOps.md)                 | [basicCurlGet](eventing-handler-curl-get.md)                           | [basicCurlPost](eventing-handler-curl-post.md)           | [simpleTimer](eventing-handler-simpleTimer.md)                               |
| -------------------------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------- |
| [cascadeKvDeleteWithDoc](eventing-handler-cascadeKvDeleteWithDoc.md) | [redactSharedData](eventing-handler-redactSharedData.md)               | [simpleFlatten](eventing-handler-simpleFlatten.md)       | [fixEmailDomains](eventing-handler-fixEmailDomains.md)                       |
| [keepLastN](eventing-handler-keepLastN.md)                           | [docControlledSelfExpiry](eventing-handler-docControlledSelfExpiry.md) | [shippingNotifier](eventing-handler-shippingNotifier.md) | [convertBucketToCollections](eventing-handler-ConvertBucketToCollections.md) |

### [](#examples-scriptlets-n1ql)Basic SQL++ Eventing Functions

The following scriptlets demonstrate how to use SQL++ or the Query Service with an Eventing Function.

| [basicN1qlSelectStmt](eventing-handler-basicN1qlSelectStmt.md) | [basicN1qlPreparedSelectStmt](eventing-handler-basicN1qlPreparedSelectStmt.md) |  |  |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------ |  |  |

### [](#examples-scriptlets-generic)Generic Manipulation Eventing Functions

The following scriptlets are examples of advanced use cases that focus on mutating a document without knowing that document’s schema.

| [dateToEpochConversion](eventing-handler-dateToEpochConversion.md) | [deepCloneAndModify](eventing-handler-deepCloneAndModify.md) | [removeObjectStubs](eventing-handler-removeObjectStubs.md) | [removeNullsAndEmptys](eventing-handler-removeNullsAndEmptys.md) |
| ------------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------------------------------------------- | ---------------------------------------------------------------- |
| [genericRename](eventing-handler-genericRename.md)                 | [genericFlatten](eventing-handler-genericFlatten.md)         | [convertXMLtoJSON](eventing-handler-convertXMLtoJSON.md)   | [convertAdvXMLtoJSON](eventing-handler-convertAdvXMLtoJSON.md)   |

### [](#examples-scriptlets-advanced-accessors)Advanced Accessor Eventing Functions

The following scriptlets demonstrate how to use Advanced Keyspace Accessors, which allow you to:

* Use CAS
* Set expiry (TTL) dates
* Use distributed atomic counters to increment and decrement counts

| [advancedGetOp](eventing-handler-advancedGetOp.md)                 | [advancedGetOpWithCache](eventing-handler-advancedGetOpWithCache.md) | [advancedInsertOp](eventing-handler-advancedInsertOp.md)                                | [advancedUpsertOp](eventing-handler-advancedUpsertOp.md)               |
| ------------------------------------------------------------------ | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [advancedReplaceOp](eventing-handler-advancedReplaceOp.md)         | [advancedDeleteOp](eventing-handler-advancedDeleteOp.md)             | [advancedIncrementOp](eventing-handler-advancedIncrementOp.md)                          | [advancedDecrementOp](eventing-handler-advancedDecrementOp.md)         |
| [advancedTouchOp](eventing-handler-advancedTouchOp.md)             | [advancedKeepLastN](eventing-handler-advanced-keepLastN.md)          | [advancedDocControlledSelfExpiry](eventing-handler-advanced-docControlledSelfExpiry.md) | [multiCollectionEventing](eventing-handler-multiCollectionEventing.md) |
| [advancedSelfRecursion](eventing-handler-advancedSelfRecursion.md) | [advancedMutateInField](eventing-handler-advancedMutateInField.md)   | [advancedMutateInArray](eventing-handler-advancedMutateInArray.md)                      | [advancedLookupInField](eventing-handler-advancedLookupInOp.md)        |

### [](#examples-scriptlets-binary-documents)Binary Document Support

The following scriptlets demonstrate support for binary documents in Eventing.

Your Eventing Function must have a language compatibility setting of Couchbase Server version 6.6.2 or above to pass binary documents in its `OnUpdate(doc,meta)` handler.

| [basicBinaryKV](eventing-handler-basicBinaryKV.md) | [advancedBinaryKV](eventing-handler-advancedBinaryKV.md) |  |  |
| -------------------------------------------------- | -------------------------------------------------------- |  |  |

### [](#examples-scriptlets-performance)Performance Eventing Functions

The following scriptlets are examples of performance-oriented or benchmark Eventing Functions.

| [fasterToLocalString](eventing-handler-fasterToLocalString.md) |  |  |  |
| -------------------------------------------------------------- |  |  |  |