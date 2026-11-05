---
title: Ports Used by FTS
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/fts/pages/fts-architecture-ports-used.adoc
  xref: xref:7.6@server:fts:fts-architecture-ports-used.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/fts/fts-architecture-ports-used.html)

# Ports Used by FTS

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

The following table lists the FTS port details:

__Table 1\. FTS Ports__
| Port name                              | Default port number(un / encrypted) | Description                                                                                                         | Node-to-node | Client-to-node | XDCR (cluster-to-cluster) |
| -------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------ | -------------- | ------------------------- |
| fts\_http\_port / fts\_ssl\_port       | 8094 / 18094                        | Search Service REST/HTTP traffic                                                                                    | No           | Yes            | No                        |
| fts\_grpc\_port / fts\_grpc\_ssl\_port | 8094 / 18094                        | Search Service gRPC port used for [scatter-gather](fts-architecture-scatter-gather.md) operations between FTS nodes | Yes          | No             | No                        |