---
title: What&#8217;s SQL++ for Analytics?
description: An introduction to Couchbase Analytics.
editUrl: https://github.com/couchbase/docs-analytics/edit/release/7.2/modules/analytics/pages/1_intro.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/analytics/1_intro.html)

# What&#8217;s SQL++ for Analytics?

This document is intended as a reference guide to the full syntax and semantics of the SQL++ for Analytics Query Language, a SQL-inspired language for working with semistructured data. SQL++ for Analytics is a Couchbase implementation, focused on parallel data analysis, of an emerging SQL-for-JSON query language specification called SQL++. SQL++ for Analytics has much in common with SQL, but there are differences due to the data model that this language is designed to serve. (SQL was designed in the 1970s to interact with the flat, schematic world of relational databases, while SQL++ for Analytics is designed for the nested, schemaless or schema-optional world of modern NoSQL systems.) In particular, SQL++ for Analytics is intended for working with the JSON data model.

In what follows, we detail the features of the SQL++ for Analytics language in a grammar-guided manner: we list and briefly explain each of the productions in the SQL++ for Analytics grammar, offering examples (and results) for clarity.

> [!NOTE]
> For further information on SQL++, see _SQL++ For SQL Users: A Tutorial_ by Don Chamberlin, which is available from Couchbase [here](https://www.couchbase.com/analytics-data).