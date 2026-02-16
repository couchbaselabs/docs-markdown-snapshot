[View original HTML](/server/7.6/fts/fts-advanced-settings-disable-file-transfer-rebalance.html)

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