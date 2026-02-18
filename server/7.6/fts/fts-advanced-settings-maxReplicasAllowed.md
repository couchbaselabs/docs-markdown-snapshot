---
title: maxReplicasAllowed
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/fts/pages/fts-advanced-settings-maxReplicasAllowed.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/fts/fts-advanced-settings-maxReplicasAllowed.html)

# maxReplicasAllowed

The `maxReplicasAllowed` setting is the maximum number of copies of primary index partitions that the index can support.

The default limit value of this is **3**.

## [](#example)Example

```console
curl -XPUT -H "Content-type:application/json" http://username:password@<ip>:8094/api/managerOptions \-d '{
    "maxReplicasAllowed": "2"
}
```