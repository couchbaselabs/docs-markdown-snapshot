---
title: The Data Model
description: Couchbase's use of JSON as a storage format allows powerful search
  and query over documents.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-c/edit/release/3.3/modules/concept-docs/pages/data-model.adoc
  xref: xref:c-sdk:concept-docs:data-model.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/c-sdk/current/concept-docs/data-model.html)

# The Data Model

> Couchbase's use of JSON as a storage format allows powerful search and query over documents. Several data structures are supported by the other SDKs, including map, list, queue, and set. 

The power to search, query, and easily work with data in Couchbase, comes from the choice of JSON as a storage format. Non-JSON storage is supported — see the [Binary Storage Documentation](nonjson.md) — including UTF-8 strings, raw sequences of bytes, and language specific serializations, however, only JSON is supported by [Query](n1ql-query.md).

In Couchbase, JSON's key-value structure allows the storage of collection data structures such as lists, maps, sets and queues. JSON's tree-like structure allows operations against [specific paths in the Document](subdocument-operations.md), and efficient support for these data structures. The data structure API is not available in the C SDK, but the sub-document API (which the data structure feature uses) can be used to attain the same results with the same performance profile. The best way to inter-operate with data structures as provided by other Couchbase SDKs is to use either full-document operations or sub-document operations.