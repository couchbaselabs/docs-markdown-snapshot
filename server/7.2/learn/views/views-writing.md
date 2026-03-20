---
title: Writing MapReduce Views
description: During the view creation process, the output structure, field
  order, content, and any summary or grouping information desired in the view is
  defined.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/learn/pages/views/views-writing.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:learn:views/views-writing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/learn/views/views-writing.html)

# Writing MapReduce Views

> During the view creation process, the output structure, field order, content, and any summary or grouping information desired in the view is defined. 

The fundamentals of a view are straightforward. A view creates a perspective on the data stored in Couchbase buckets in a format that can be used to represent the data in a specific way, define and filter the information, and provide a basis for searching or querying the data in the database based on the content.

Views achieve this by defining an output structure that translates the stored JSON object data into a JSON array or object across two components, the key and the value. This definition is performed through the specification of two separate functions written in JavaScript. The view definition is divided into two parts, a map function and a reduce function:

* Map functions
* Reduce functions