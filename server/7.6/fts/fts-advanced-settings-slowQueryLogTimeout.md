---
title: slowQueryLogTimeout
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/fts/pages/fts-advanced-settings-slowQueryLogTimeout.adoc
  xref: xref:7.6@server:fts:fts-advanced-settings-slowQueryLogTimeout.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/fts/fts-advanced-settings-slowQueryLogTimeout.html)

# slowQueryLogTimeout

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

The `slowQueryLogTimeout` setting controls the logging of the queries in the FTS server logs.

The default value for the `slowQueryLogTimeout` setting is **5 seconds**.

Every query for which the execution time is more than the value set in the `slowQueryLogTimeout` setting,will be logged in the FTS server logs and the slow-query server stats.

## [](#example)Example

```console
curl -XPUT -H "Content-type:application/json" http://username:password@<ip>:8094/api/managerOptions \-d '{
    "slowQueryLogTimeout": "10"
}
```