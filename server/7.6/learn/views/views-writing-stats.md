---
title: Built-in _stats Function
description: The built-in <code>_stats</code> reduce function produces
  statistical calculations for the input data.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/learn/pages/views/views-writing-stats.adoc
  xref: xref:7.6@server:learn:views/views-writing-stats.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/learn/views/views-writing-stats.html)

# Built-in _stats Function

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

> The built-in `_stats` reduce function produces statistical calculations for the input data. 

As with the `_sum` function, the corresponding value in the emit call should be a number. The generated statistics include the sum, count, minimum ( `min` ), maximum ( `max` ) and sum squared ( `sumsqr` ) of the input rows.

For example, using the sales data, a slightly truncated output at group level one shows the same fields in the output value for each of the reduced output rows.

{
   "rows" : [
      {
         "value" : {
            "count" : 3,
            "min" : 7000,
            "sumsqr" : 699000000,
            "max" : 19000,
            "sum" : 43000
         },
         "key" : [
            "Adam"
         ]
      },
      {
         "value" : {
            "count" : 3,
            "min" : 5000,
            "sumsqr" : 594000000,
            "max" : 20000,
            "sum" : 38000
         },
         "key" : [
            "James"
         ]
      },
      {
         "value" : {
            "count" : 3,
            "min" : 3000,
            "sumsqr" : 542000000,
            "max" : 22000,
            "sum" : 32000
         },
         "key" : [
            "John"
         ]
      }
   ]
}