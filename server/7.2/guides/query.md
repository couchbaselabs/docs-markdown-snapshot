---
title: Selection Queries
description: These guides explain how to read data with a SQL++ query.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/guides/pages/query.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/guides/query.html)

# Selection Queries

These guides explain how to read data with a SQL++ query. The SQL++ query language enables you to retrieve a document by inspecting its contents to see if it matches a certain criterion. Key-value operations are quicker, but querying documents allows for richer search capabilities — for example, "Give me all likes and followed users located in the US", versus "Give me a user with the ID e3d882a4".

This page is for Couchbase Server.

## Selecting Data with Queries

To read data from a data source using SQL++, you must use a selection query; in other words, a query using the `SELECT` statement.

* [Selecting Data](select.md)

## Querying Across Relationships

You can use a join to read objects from one data source, combine them with corresponding objects from another data source, and return the joined objects.

* [Querying Across Relationships](join.md)

## Nesting and Unnesting Documents

SQL++ provides syntax which enables you to nest (create) or unnest (flatten) arrays of embedded documents in a query.

* [Nesting and Unnesting Documents](nest-unnest.md)

## Grouping and Aggregation

You can use aggregate functions to perform calculations over multiple values. Grouping enables you to display the results in groups.

* [Grouping and Aggregation](group-agg.md)