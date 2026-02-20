---
title: maxFeedsPerDCPAgent
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/fts/pages/fts-advanced-settings-maxFeedsPerDCPAgent.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:fts:fts-advanced-settings-maxFeedsPerDCPAgent.adoc[]
---

[View original HTML](/server/7.6/fts/fts-advanced-settings-maxFeedsPerDCPAgent.html)

# maxFeedsPerDCPAgent

The `maxFeedsPerDCPAgent` setting refers to the number of index partitions a single physical connection to KV will handle. This setting controls the sharing of feed Agent or the underlying connection per feed of various index partitions belonging to the same bucket.

The default value for the `maxFeedsPerDCPAgent` setting is **6**.

You can get the maximum indexing throughput by setting the `maxFeedsPerDCPAgent` value to 1\. However, it results in higher resource utilization.

## [](#example)Example

```console
curl -XPUT -H "Content-type:application/json" http://username:password@<ip>:8094/api/managerOptions \-d '{
    "maxFeedsPerDCPAgent": "10"
}
```