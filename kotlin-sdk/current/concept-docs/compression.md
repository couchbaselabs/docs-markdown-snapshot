---
title: Compression
description: In response to increasing volumes of data being sent over the wire,
  Couchbase Data Platform provides data compression between the SDK and
  Couchbase Server.
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/temp/3.11/modules/concept-docs/pages/compression.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:kotlin-sdk:concept-docs:compression.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/kotlin-sdk/current/concept-docs/compression.html)

# Compression

> In response to increasing volumes of data being sent over the wire, Couchbase Data Platform provides data compression between the SDK and Couchbase Server. 

## [](#overview)Overview

Documents may already be stored compressed with Snappy on the server. New documents may be passed from client applications to the server in compressed form, saving around 40% in bandwidth (depending on the document content and size), and also transmission time. These operations take place automatically, after the SDK negotiates the capability with the server, and do not require any changes on the client side.

For SDKs with Snappy compression enabled, documents will be automatically compressed if the [Couchbase Server](#7.1@server:learn:buckets-memory-and-storage/compression.adoc#compression-modes) is not set to `Off` for Compression see [see below](#minimum-size). Instructions to disable compression can be found at [the bottom of the page](#threshold).

## [](#limits)Limits

The document must be below 20MiB in size in both compressed and uncompressed form. Compression is only available in the Enterprise Edition of Couchbase Data Platform.

> [!TIP]
> This size limit is enforced by Couchbase Server; in practice it will affect very few users, as most JSON documents are considerably smaller. A compressed doument of just under 20MB, which is greater than 20,971,520 bytes (20 MiB) when uncompressed, will be rejected by the server as follows:
> 
> * Couchbase Server decompresses the document to check that it is valid JSON, and is correctly compressed with _Snappy_, and at this point measures it against `max data size` (20 MiB).
> * If the decompressed value's size exceeds this limit, the mutation is failed with a "too big" error code (E2BIG code 3).
> 
> Therefore, where necessary, enforce document size limits in your application on _uncompressed_ documents.

## [](#operating-modes)Operating Modes

The three modes in which compression can be used, "off", "passive" and "active", are configured per bucket in the configuration settings on the cluster.

__Table 1\. Compression Operating Modes__
|                                                                       | **OFF**                              | **PASSIVE**                  | **ACTIVE**                                                                                  |
| --------------------------------------------------------------------- | ------------------------------------ | ---------------------------- | ------------------------------------------------------------------------------------------- |
| Negotiating SNAPPY                                                    | ignore                               | acknowledge                  | acknowledge                                                                                 |
| Sending compressed data when SNAPPY feature **enabled**               | \-                                   | accept                       | accept                                                                                      |
| Sending compressed data when SNAPPY feature **disabled**              | reject as invalid                    | reject as invalid            | reject as invalid                                                                           |
| Receiving data which were previously compressed on the server         | server inflates and sends plain data | server sends compressed data | server sends compressed data                                                                |
| Receiving data which were **not** previously compressed on the server | server sends plain data              | server sends plain data      | server might send compressed data (the compression is done in the background on the server) |

## [](#acceptance-guarantee)Acceptance Guarantee

The server may change compression settings for the bucket at any time, but it is guaranteed that once the socket negotiates compression, the server will never reject compressed data, even if the bucket setting has been changed.

## [](#minimum-size)Minimum Size

While the tiniest of documents will not be reduced in size by compressing, there is another category of slightly larger documents in whose case the time overhead of compressing and decompressing outweighs the slight advantage of marginally reduced transmission time from client to server or back.

To safeguard against the case of several thousand documents stealing CPU time to barely discernable advantage, a threshold for minimum doument size to compress is set in the SDK, with a sensible default value - that value can be seen for your chosen SDK in its API documentation (32 bytes), and you can override this to disable compression of smaller ones:

```java
ClusterEnvironment env = ClusterEnvironment
    .builder()
    // start compressing at 1024 bytes
    .compressionConfig(CompressionConfig.minSize(1024))
    .build();
```

The `CompressionConfig` also allows you to disable compression completely or tune the ratio of when a compressed document (compared to the size of the uncompressed) should be sent over the wire.