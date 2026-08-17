---
title: Select Data with Queries
description: These guides explain how to read data with a SQL++ query.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/guides/pages/query.adoc
  xref: xref:cloud:guides:query.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/guides/query.html)

# Select Data with Queries

These guides explain how to read data with a SQL++ query. The SQL++ query language enables you to retrieve a document by inspecting its contents to see if it matches a certain criterion. Key-value operations are quicker, but querying documents allows for richer search capabilities — for example, "Give me all likes and followed users located in the US", versus "Give me a user with the ID e3d882a4".

## Read Data and Return Results

To read data from a data source using SQL++, you must use a selection query; in other words, a query using the `SELECT` statement.

* [Read Data and Return Results](select.md)

## Query Across Relationships

You can use a join to read objects from one data source, combine them with corresponding objects from another data source, and return the joined objects.

* [Query Across Relationships](join.md)

## Nest and Unnest Documents

SQL++ provides syntax which enables you to nest (create) or unnest (flatten) arrays of embedded documents in a query.

* [Nest and Unnest Documents](nest-unnest.md)

## Grouping and Aggregation

You can use aggregate functions to perform calculations over multiple values. Grouping enables you to display the results in groups.

* [Calculate Aggregates and Group Results](group-agg.md)

## Prepared Statements

If you need to execute certain SQL++ statements repeatedly, you can use placeholder parameters and prepared statements to optimize query reuse.

* [Prepare Statements for Reuse](prep-statements.md)