---
title: disableFileTransferRebalance
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/fts/pages/fts-advanced-settings-disable-file-transfer-rebalance.adoc
  xref: xref:7.6@server:fts:fts-advanced-settings-disable-file-transfer-rebalance.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/fts/fts-advanced-settings-disable-file-transfer-rebalance.html)

# disableFileTransferRebalance

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

FTS index partitions are copied between nodes instead of regenerating them from scratch, to facilitate faster rebalancing.

As an alternative, the index partitions can be generated from scratch during rebalancing. To set this mode of operation, the following command can be executed to disable the file transfer balance mode.

Disable file transfer rebalance

```console
curl -XPUT -H "Content-type:application/json" \
http://<Administrator>:<pwd>@<node>:8094/api/managerOptions \
 -d '{"disableFileTransferRebalance": "true"}'
```

To re-enable file transfer rebalance, use the following commmand:

Enable file transfer rebalance

```console
curl -XPUT -H "Content-type:application/json" \
http://<Administrator>:<pwd>@<node>:8094/api/managerOptions \
 -d '{"disableFileTransferRebalance": "false"}'
```