[View original HTML](/server/7.2/fts/fts-architecture-ports-used.html)

The following table lists the FTS port details:

__Table 1\. FTS Ports__
| Port name                              | Default port number(un / encrypted) | Description                                                                                                         | Node-to-node | Client-to-node | XDCR (cluster-to-cluster) |
| -------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------ | -------------- | ------------------------- |
| fts\_http\_port / fts\_ssl\_port       | 8094 / 18094                        | Search Service REST/HTTP traffic                                                                                    | No           | Yes            | No                        |
| fts\_grpc\_port / fts\_grpc\_ssl\_port | 8094 / 18094                        | Search Service gRPC port used for [scatter-gather](fts-architecture-scatter-gather.md) operations between FTS nodes | Yes          | No             | No                        |