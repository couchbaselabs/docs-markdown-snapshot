---
title: SQL++ for Mobile&#8201;&#8212;&#8201;Differences from Querybuilder
description: Differences between Couchbase Lite's Querybuilder and SQL++ for Mobile
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.1/modules/swift/pages/query-n1ql-mobile-querybuilder-diffs.adoc
  xref: xref:couchbase-lite:swift:query-n1ql-mobile-querybuilder-diffs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/swift/query-n1ql-mobile-querybuilder-diffs.html)

# SQL++ for Mobile&#8201;&#8212;&#8201;Differences from Querybuilder

> Description — _Differences between Couchbase Lite's Querybuilder and SQL++ for Mobile_  
> Related Content — [Predictive Queries](querybuilder.md#lbl-predquery) | [Live Queries](query-live.md) | [Indexing](indexing.md)

Couchbase Lite's SQL++ for Mobile supports all QueryBuilder features, except _Predictive Query_ and _Index_.  
See [Table 1](#tbl-qbldr-diffs) for the features supported by SQL++ but not by QueryBuilder.

__Table 1\. QueryBuilder Differences__
| Category                   | Components                                                                             |
| -------------------------- | -------------------------------------------------------------------------------------- |
| Conditional Operator       | CASE(WHEN …​ THEN …​ ELSE ..)                                                          |
| Array Functions            | ARRAY\_AGG ARRAY\_AVG ARRAY\_COUNT ARRAY\_IFNULL ARRAY\_MAX ARRAY\_MIN ARRAY\_SUM      |
| Conditional Functions      | IFMISSING IFMISSINGORNULL IFNULL MISSINGIF NULLIF Match Functions DIV IDIV ROUND\_EVEN |
| Pattern Matching Functions | REGEXP\_CONTAINS REGEXP\_LIKE REGEXP\_POSITION REGEXP\_REPLACE                         |
| Type Checking Functions    | ISARRAY ISATOM ISBOOLEAN ISNUMBER ISOBJECT ISSTRING TYPE                               |
| Type Conversion Functions  | TOARRAY TOATOM TOBOOLEAN TONUMBER TOOBJECT TOSTRING                                    |

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

.

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.