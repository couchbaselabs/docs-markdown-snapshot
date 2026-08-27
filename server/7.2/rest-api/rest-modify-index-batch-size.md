---
title: Modify Index Batch Size
description: The REST API supports modification of the batch size whereby the
  relocation and rebuilding of indexes, during rebalance, is maintained at a
  high level of performance.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/rest-modify-index-batch-size.adoc
  xref: xref:7.2@server:rest-api:rest-modify-index-batch-size.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/rest-api/rest-modify-index-batch-size.html)

# Modify Index Batch Size

> The REST API supports modification of the batch size whereby the relocation and rebuilding of indexes, during rebalance, is maintained at a high level of performance. 

## [](#http-method-and-uri)HTTP Method and URI

POST /settings

## [](#description)Description

Establishes the _batch size_, which is used for index rebuilding and metadata transfer, during rebalance. This is the maximum number of indexes that will be moved concurrently in the cluster. Either the Full Admin or the Cluster Admin role is required.

## [](#curl-syntax)Curl Syntax

curl -X POST http://<node-ip-address-or-domain-name>:<port-number>/settings
  -u <username>:<password>
  -d '{"indexer.rebalance.transferBatchSize":<integer>}'

The port number must be either `9102` or `19102`, which are those of the `indexer_http_port` and `indexer_https_port` respectively. The `integer` should be a small integer that corresponds to the batch size to be established. The default is `3`.

The change automatically propagates to all Index-Service nodes, and will be remembered across node and cluster restarts.

## [](#responses)Responses

Success returns `200 OK`. Failure to authenticate returns `401 Unauthorized`. An incorrectly specified URI returns `404 Object Not Found`.

Failure correctly to specify the key `"indexer.rebalance.transferBatchSize"` generates no error, and returns `200 OK`.

## [](#example)Example

The following call establishes the batch size as `7`:

curl -v -X POST http://localhost:9102/settings -u Administrator:password \
-d '{"indexer.rebalance.transferBatchSize":7}'

If successful, the call returns `200 OK` and no object.

## [](#see-also)See Also

An overview of rebalance as it affects the Index Service, including an overview of _smart batching_, is provided in [Index Service](../learn/clusters-and-availability/rebalance.md#rebalancing-the-index-service). For information on Couchbase-Server ports, see [Couchbase Server Ports](../install/install-ports.md).