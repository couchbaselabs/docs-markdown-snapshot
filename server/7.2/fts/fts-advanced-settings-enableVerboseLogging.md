---
title: enableVerboseLogging
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-advanced-settings-enableVerboseLogging.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:fts:fts-advanced-settings-enableVerboseLogging.adoc[]
---

[View original HTML](/server/7.2/fts/fts-advanced-settings-enableVerboseLogging.html)

# enableVerboseLogging

The `enableVerboseLogging` setting enables collecting additional logs for debugging purpose.

Enabling this setting periodically adds more statistics whenever user runs the `/api/stats` endpoint for periodic stats collection.

## [](#example)Example

```console
curl -XPUT -H "Content-type:application/json" http://username:password@<ip>:8094/api/managerOptions \-d '{
    "enableVerboseLogging": "true"
}
```