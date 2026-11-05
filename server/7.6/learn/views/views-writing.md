---
title: Writing MapReduce Views
description: During the view creation process, the output structure, field
  order, content, and any summary or grouping information desired in the view is
  defined.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/learn/pages/views/views-writing.adoc
  xref: xref:7.6@server:learn:views/views-writing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/learn/views/views-writing.html)

# Writing MapReduce Views

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

> During the view creation process, the output structure, field order, content, and any summary or grouping information desired in the view is defined. 

The fundamentals of a view are straightforward. A view creates a perspective on the data stored in Couchbase buckets in a format that can be used to represent the data in a specific way, define and filter the information, and provide a basis for searching or querying the data in the database based on the content.

Views achieve this by defining an output structure that translates the stored JSON object data into a JSON array or object across two components, the key and the value. This definition is performed through the specification of two separate functions written in JavaScript. The view definition is divided into two parts, a map function and a reduce function:

* Map functions
* Reduce functions