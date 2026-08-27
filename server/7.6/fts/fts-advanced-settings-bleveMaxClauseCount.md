---
title: bleveMaxClauseCount
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/fts/pages/fts-advanced-settings-bleveMaxClauseCount.adoc
  xref: xref:7.6@server:fts:fts-advanced-settings-bleveMaxClauseCount.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/fts/fts-advanced-settings-bleveMaxClauseCount.html)

# bleveMaxClauseCount

The `bleveMaxClauseCount` setting limits the maximum number of query sub-clauses explicitly present in the search request or triggered internally from the search request.

Using this setting, users can restrict resource utilization, especially the memory usage for serving a query.

The default value of the `bleveMaxClauseCount` setting is **1024**.

The default limit might not be sufficient for queries like wildcard, regex, prefix, disjuncts, fuzzy, etc. So, users can fix the issue by specifying a higher value for the `bleveMaxClauseCount` setting. However, users must check the query patterns to make them more efficient and well-scoped.

## [](#example)Example

curl -XPUT -H "Content-type:application/json" http://username:password@<ip>:8094/api/managerOptions \-d '{
    "bleveMaxClauseCount": "10000"
}