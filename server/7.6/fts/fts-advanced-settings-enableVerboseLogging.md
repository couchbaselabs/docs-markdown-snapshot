---
title: enableVerboseLogging
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/fts/pages/fts-advanced-settings-enableVerboseLogging.adoc
  xref: xref:7.6@server:fts:fts-advanced-settings-enableVerboseLogging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/fts/fts-advanced-settings-enableVerboseLogging.html)

# enableVerboseLogging

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

The `enableVerboseLogging` setting enables collecting additional logs for debugging purpose.

Enabling this setting periodically adds more statistics whenever user runs the `/api/stats` endpoint for periodic stats collection.

## [](#example)Example

```console
curl -XPUT -H "Content-type:application/json" http://username:password@<ip>:8094/api/managerOptions \-d '{
    "enableVerboseLogging": "true"
}
```