---
title: Ports Used by FTS
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-architecture-ports-used.adoc
  xref: xref:7.2@server:fts:fts-architecture-ports-used.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-architecture-ports-used.html)

# Ports Used by FTS

The following table lists the FTS port details:

__Table 1\. FTS Ports__
| Port name                              | Default port number(un / encrypted) | Description                                                                                                         | Node-to-node | Client-to-node | XDCR (cluster-to-cluster) |
| -------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------ | -------------- | ------------------------- |
| fts\_http\_port / fts\_ssl\_port       | 8094 / 18094                        | Search Service REST/HTTP traffic                                                                                    | No           | Yes            | No                        |
| fts\_grpc\_port / fts\_grpc\_ssl\_port | 8094 / 18094                        | Search Service gRPC port used for [scatter-gather](fts-architecture-scatter-gather.md) operations between FTS nodes | Yes          | No             | No                        |