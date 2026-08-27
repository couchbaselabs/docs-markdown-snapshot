---
title: enableVerboseLogging
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/fts/pages/fts-advanced-settings-enableVerboseLogging.adoc
  xref: xref:7.6@server:fts:fts-advanced-settings-enableVerboseLogging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/fts/fts-advanced-settings-enableVerboseLogging.html)

# enableVerboseLogging

The `enableVerboseLogging` setting enables collecting additional logs for debugging purpose.

Enabling this setting periodically adds more statistics whenever user runs the `/api/stats` endpoint for periodic stats collection.

## [](#example)Example

```console
curl -XPUT -H "Content-type:application/json" http://username:password@<ip>:8094/api/managerOptions \-d '{
    "enableVerboseLogging": "true"
}
```