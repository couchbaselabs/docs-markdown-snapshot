---
title: bleveMaxResultWindow
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/fts/pages/fts-advanced-settings-bleveMaxResultWindow.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:fts:fts-advanced-settings-bleveMaxResultWindow.adoc[]
---

[View original HTML](/server/current/fts/fts-advanced-settings-bleveMaxResultWindow.html)

# bleveMaxResultWindow

The default value of the `bleveMaxResultWindow` setting is **10000**. However, users can change this value if they want to view more records in the result.

The `bleveMaxResultWindow` setting controls the maximum number of results a query can obtain, which helps limit the max results, thereby limiting the resource usage. It may also increase.

## [](#example)Example

```console
curl -XPUT -H "Content-type:application/json" http://username:password@<ip>:8094/api/managerOptions \-d '{
    "bleveMaxResultWindow": "10000"
}
```