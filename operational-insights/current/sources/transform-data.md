---
title: Transform Data
description: Operational Insights can apply lightweight transformations to data
  as it's ingested into a remote collection, before the data is stored.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/sources/pages/transform-data.adoc
  xref: xref:enterprise-analytics:sources:transform-data.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/sources/transform-data.html)

# Transform Data

> Operational Insights can apply lightweight transformations to data as it's ingested into a remote collection, before the data is stored. 

You do this by creating a `TRANSFORM FUNCTION` — a specialized SQL++ user-defined function (UDF) that receives each incoming document and returns the transformed version to be stored. Common transformations include renaming or excluding fields, flattening nested structures, converting data types, and deriving new fields from existing ones.

Once you've created a `TRANSFORM FUNCTION`, you apply it to a remote collection using the `APPLY FUNCTION` clause of the `CREATE COLLECTION` statement, so that Operational Insights transforms each document automatically as it arrives, before storing it.

For the full syntax, requirements, and examples, see [Transform Functions](../sqlpp/9a%5Ftransform-functions.md).

## [](#see-also)See Also

* [Transform Functions](../sqlpp/9a%5Ftransform-functions.md)
* [Stream Data from Remote Sources](manage-remote.md)
* [CREATE a Remote Collection](../sqlpp/5%5Fddl%5Fremote.md)