---
title: disableFileTransferRebalance
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/fts/pages/fts-advanced-settings-disable-file-transfer-rebalance.adoc
  xref: xref:server:fts:fts-advanced-settings-disable-file-transfer-rebalance.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/fts/fts-advanced-settings-disable-file-transfer-rebalance.html)

# disableFileTransferRebalance

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