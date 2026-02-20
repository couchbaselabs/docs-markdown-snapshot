---
title: disableFileTransferRebalance
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-advanced-settings-disable-file-transfer-rebalance.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:fts:fts-advanced-settings-disable-file-transfer-rebalance.adoc[]
---

[View original HTML](/server/7.2/fts/fts-advanced-settings-disable-file-transfer-rebalance.html)

# disableFileTransferRebalance

FTS index partitions are copied between nodes instead of regenerating them from scratch, to facilitate faster rebalancing.

As an alternative, the index partitions can be generated from scratch during rebalancing. To set this mode of operation, the following command can be executed to disable the file transfer balance mode.

Disable file transfer rebalance

```console
curl -XPUT -H "Content-type:application/json" \
http://<Administrator>:<pwd>@<node>:8094/api/managerOptions \
 -d '{"disableFileTransferRebalance": "true"}'
```

To re-enable file transfer rebalance, use the following command:

Enable file transfer rebalance

```console
curl -XPUT -H "Content-type:application/json" \
http://<Administrator>:<pwd>@<node>:8094/api/managerOptions \
 -d '{"disableFileTransferRebalance": "false"}'
```