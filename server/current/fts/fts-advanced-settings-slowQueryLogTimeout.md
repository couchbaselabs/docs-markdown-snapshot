---
title: slowQueryLogTimeout
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/fts/pages/fts-advanced-settings-slowQueryLogTimeout.adoc
  xref: xref:server:fts:fts-advanced-settings-slowQueryLogTimeout.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/fts/fts-advanced-settings-slowQueryLogTimeout.html)

# slowQueryLogTimeout

The `slowQueryLogTimeout` setting controls the logging of the queries in the FTS server logs.

The default value for the `slowQueryLogTimeout` setting is **5 seconds**.

Every query for which the execution time is more than the value set in the `slowQueryLogTimeout` setting,will be logged in the FTS server logs and the slow-query server stats.

## [](#example)Example

```console
curl -XPUT -H "Content-type:application/json" http://username:password@<ip>:8094/api/managerOptions \-d '{
    "slowQueryLogTimeout": "10"
}
```