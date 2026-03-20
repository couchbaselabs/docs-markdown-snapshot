---
title: bleveMaxResultWindow
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-advanced-settings-bleveMaxResultWindow.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:fts:fts-advanced-settings-bleveMaxResultWindow.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-advanced-settings-bleveMaxResultWindow.html)

# bleveMaxResultWindow

The default value of the `bleveMaxResultWindow` setting is **10000**. However, users can change this value if they want to view more records in the result.

The `bleveMaxResultWindow` setting controls the maximum number of results a query can obtain, which helps limit the max results, thereby limiting the resource usage. It may also increase.

## [](#example)Example

```console
curl -XPUT -H "Content-type:application/json" http://username:password@<ip>:8094/api/managerOptions \-d '{
    "bleveMaxResultWindow": "10000"
}
```