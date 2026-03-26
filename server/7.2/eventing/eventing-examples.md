---
title: "Examples: Using the Eventing Service"
description: This page contains examples of how to use the Eventing Service,
  using the Couchbase Web Console.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/eventing/pages/eventing-examples.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.2@server:eventing:eventing-examples.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/eventing/eventing-examples.html)

# Examples: Using the Eventing Service

> This page contains examples of how to use the Eventing Service, using the Couchbase Web Console. 

## [](#examples-step-by-step)Step by Step Examples

**Detailed Examples**: These tutorial-like guides are ideal for a novice to learn the basics of the Eventing Service, via complete detailed step by step start-to-finish instructions.

| [Data Enrichment](eventing-example-data-enrichment.md)  | [Cascade Delete](eventing-examples-cascade-delete.md)                | [Document Expiry](eventing-examples-docexpiry.md)                        |
| ------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| [Delete v Expiry](eventing-examples-delete-v-expiry.md) | [Document Archival](eventing-examples-docarchive.md)                 | [Cancel or Overwrite Timer](eventing-examples-cancel-overwrite-timer.md) |
| [Recurring Timer](eventing-examples-recurring-timer.md) | [External REST via cURL GET](eventing-examples-rest-via-curl-get.md) | [Risk Assessment](eventing-examples-high-risk.md)                        |

## [](#examples-scriptlets)Scriptlets or Terse Examples

**Basic KV Eventing Functions**: The following Scriptlets are essentially stand alone Eventing Functions examples, and introduce more use cases. Here we assume the reader has a good understanding of the Eventing System and requires little guidance.

| [basicBucketOps](eventing-handler-basicBucketOps.md)                   | [basicCurlGet](eventing-handler-curl-get.md)                         | [basicCurlPost](eventing-handler-curl-post.md)                               |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| [simpleTimer](eventing-handler-simpleTimer.md)                         | [cascadeKvDeleteWithDoc](eventing-handler-cascadeKvDeleteWithDoc.md) | [redactSharedData](eventing-handler-redactSharedData.md)                     |
| [simpleFlatten](eventing-handler-simpleFlatten.md)                     | [fixEmailDomains](eventing-handler-fixEmailDomains.md)               | [keepLastN](eventing-handler-keepLastN.md)                                   |
| [docControlledSelfExpiry](eventing-handler-docControlledSelfExpiry.md) | [shippingNotifier](eventing-handler-shippingNotifier.md)             | [ConvertBucketToCollections](eventing-handler-ConvertBucketToCollections.md) |

**Basic SQL++ Eventing Functions**: The following Scriptlets demonstrate using SQL++ or the Query Service from within an Eventing Function.

| [basicN1qlSelectStmt](eventing-handler-basicN1qlSelectStmt.md) | [basicN1qlPreparedSelectStmt](eventing-handler-basicN1qlPreparedSelectStmt.md) |  |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------ |  |

**Generic Manipulation Eventing Functions** The following Scriptlets are more advanced use cases which focus on mutating documents without knowledge of the document's schema.

| [dateToEpochConversion](eventing-handler-dateToEpochConversion.md) | [deepCloneAndModify](eventing-handler-deepCloneAndModify.md)   | [removeObjectStubs](eventing-handler-removeObjectStubs.md) |
| ------------------------------------------------------------------ | -------------------------------------------------------------- | ---------------------------------------------------------- |
| [removeNullsAndEmptys](eventing-handler-removeNullsAndEmptys.md)   | [genericRename](eventing-handler-genericRename.md)             | [genericFlatten](eventing-handler-genericFlatten.md)       |
| [convertXMLtoJSON](eventing-handler-convertXMLtoJSON.md)           | [convertAdvXMLtoJSON](eventing-handler-convertAdvXMLtoJSON.md) |                                                            |

**Advanced Accessor Eventing Functions**: The following Scriptlets demonstrate using Advanced Bucket Accessors (introduced in version 6.6.1) which allow the use of CAS, ability to set expirations (or TTLs) and the use of distributed atomic counters to increment or decrement counts.

| [advancedGetOp](eventing-handler-advancedGetOp.md)                                      | [advancedGetOpWithCache](eventing-handler-advancedGetOpWithCache.md)   | [advancedInsertOp](eventing-handler-advancedInsertOp.md)    |
| --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------- |
| [advancedUpsertOp](eventing-handler-advancedUpsertOp.md)                                | [advancedReplaceOp](eventing-handler-advancedReplaceOp.md)             | [advancedDeleteOp](eventing-handler-advancedDeleteOp.md)    |
| [advancedIncrementOp](eventing-handler-advancedIncrementOp.md)                          | [advancedDecrementOp](eventing-handler-advancedDecrementOp.md)         | [advancedKeepLastN](eventing-handler-advanced-keepLastN.md) |
| [advancedDocControlledSelfExpiry](eventing-handler-advanced-docControlledSelfExpiry.md) | [multiCollectionEventing](eventing-handler-multiCollectionEventing.md) |                                                             |

**Binary Document Support**: The following Scriptlets demonstrate support for binary documents in Eventing. Only a Function with "language compatibility" of 6.6.2 or above in its settings will pass binary documents to the OnUpdate(doc,meta) handler.

| [basicBinaryKV](eventing-handler-basicBinaryKV.md) | [advancedBinaryKV](eventing-handler-advancedBinaryKV.md) |  |
| -------------------------------------------------- | -------------------------------------------------------- |  |

**Performance Eventing Functions** The following Scriptlets are performance oriented and/or benchmarks.

| [fasterToLocalString](eventing-handler-fasterToLocalString.md) |  |  |
| -------------------------------------------------------------- |  |  |