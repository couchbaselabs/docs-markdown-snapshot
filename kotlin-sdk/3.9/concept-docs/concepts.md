---
title: Concepts Guides
description: A discursive look at the features exposed by the Couchbase Java SDK.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/temp/3.9/modules/concept-docs/pages/concepts.adoc
  xref: xref:3.9@kotlin-sdk:concept-docs:concepts.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/kotlin-sdk/3.9/concept-docs/concepts.html)

# Concepts Guides

> A discursive look at the features exposed by the Couchbase Java SDK. 

The Couchbase SDK docs aim to be practical, and example-led, to get you working with any of our features as quickly as possible. At some point during your journey through these Howto docs, you may feel the need for a deeper dive into certain topics. This section contains discussion-style expansions of key Couchbase features, which go beyond the dry, bare-bones reference of the API docs, and aim to give a clear understanding of the chosen topic.

* [Buckets & Clusters](buckets-and-clusters.md)
* [Collections & Scope](collections.md)
* [Compression](compression.md)
* [Data Model](data-model.md)

  * [Documents (includes discussion of Counters)](documents.md)
  * [Non-json Docs](nonjson.md)
  * [Sub-Documents](subdocument-operations.md)
  * [XATTR & Virtual XATTR](xattr.md)
* [Errors, Exceptions, and Diagnostics](errors.md)

  * [Health Check](health-check.md)
  * [Tracing](response-time-observability.md)
* [Failure Considerations & Durability](durability-replication-failure-considerations.md)
* [Field Level Encryption](encryption.md)
* [Services - choosing the right one](data-services.md)

  * [Analytics](analytics-for-sdk-users.md)
  * [Full Text Search](full-text-search-overview.md)
  * [MapReduce Views](understanding-views.md)
  * [SQL++ Query](n1ql-query.md)
* [User Management](sdk-user-management-overview.md)

  * [Cert Auth](certificate-based-authentication.md)
  * [RBAC](rbac.md)