---
title: maxReplicasAllowed
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/fts/pages/fts-advanced-settings-maxReplicasAllowed.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:fts:fts-advanced-settings-maxReplicasAllowed.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/fts/fts-advanced-settings-maxReplicasAllowed.html)

# maxReplicasAllowed

The `maxReplicasAllowed` setting is the maximum number of copies of primary index partitions that the index can support.

The default limit value of this is **3**.

## [](#example)Example

```console
curl -XPUT -H "Content-type:application/json" http://username:password@<ip>:8094/api/managerOptions \-d '{
    "maxReplicasAllowed": "2"
}
```