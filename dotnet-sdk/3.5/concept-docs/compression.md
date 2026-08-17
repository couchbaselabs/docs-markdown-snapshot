---
title: Compression
description: In response to increasing volumes of data being sent over the wire,
  Couchbase Data Platform provides data compression between the SDK and
  Couchbase Server.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/release/3.5/modules/concept-docs/pages/compression.adoc
  xref: xref:3.5@dotnet-sdk:concept-docs:compression.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/3.5/concept-docs/compression.html)

# Compression

> In response to increasing volumes of data being sent over the wire, Couchbase Data Platform provides data compression between the SDK and Couchbase Server. 

> [!NOTE]
> From version 3.5.2, the .NET SDK provides compression by using [Snappier](https://www.nuget.org/packages/Snappier), a performance-focused C# port of [Snappy](https://github.com/google/snappy). This was previously opt-in only via installing the corresponding [Couchbase.Extensions](https://www.nuget.org/packages/Couchbase.Extensions.Compression.Snappier/1.0.0-beta.1) package.

## [](#overview)Overview

Documents may already be stored compressed with Snappy on the server. New documents may be passed from client applications to the server in compressed form, saving around 40% in bandwidth (depending on the document content and size), and also transmission time. Register a Snappy plugin for the SDK to use compression for requests and responses, using the `WithSnappyCompression()` extension method, then these operations take place automatically after the SDK negotiates the capability with the server.

For SDKs with Snappy compression enabled, documents will be automatically compressed if compression is not turned `Off` in [Couchbase Server](../../../server/7.6/learn/buckets-memory-and-storage/compression.md#compression-modes) (see [below](#minimum-size)).

## [](#usage-and-customization)Usage and Customization

Starting with .NET SDK v3.5.2, Snappier compression is enabled in the `ClusterOptions` using the `WithSnappyCompression()` extension method.

You can disable compression or customize certain settings, both via `ClusterOptions` or Connection String parameters:

```csharp
// ConnectionString parameters
var connectionString = "couchbases://cb.<your-endpoint>.cloud.couchbase.com:18091?compression=true&compression_min_size=512&compression_min_ratio=0.82";
// for development on local cluster, use: couchbase://localhost:8091

// ClusterOptions parameters
var clusterOptions = new ClusterOptions
{
    Compression = true,
    CompressionMinRatio = 0.82f, // Float value between 1 and 0.
    CompressionMinSize = 512 // Integer value represented in bytes.
}.WithSnappyCompression();

// Connect
clusterOptions.WithConnectionString(connectionString);
clusterOptions.WithCredentials("Administrator", "password");

var cluster = await Cluster.ConnectAsync(clusterOptions).ConfigureAwait(false);
```

Please refer to the [API Documentation](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.ClusterOptions.html#Couchbase%5FClusterOptions%5FCompression) for details on `CompressionMinRatio` and `CompressionMinSize`.

### [](#advanced-bring-your-own-compression)Advanced: Bring Your Own Compression

You can provide the SDK with your own implementation of Snappy compression/decompression by implementing the `ICompressionAlgorithm` interface, and passing it through your `ClusterOptions` with:

```csharp
clusterOptions.WithCompressionAlgorithm(myCompressionImplementation);

// See Couchbase.Compression.Snappier.Internal.SnappierCompression for details on how Snappier implements the interface.
```

> [!CAUTION]
> Even when compression is turned `Off` server-side, Couchbase Server will decompress documents in memory, and store them recompressed on disk (using Snappy) [see server compression docs](../../../server/7.6/learn/buckets-memory-and-storage/compression.md#compression-modes).
> 
> It is therefore not recommended to implement a different compression algorithm from Snappy as this may very well cause data corruption.

## [](#limits)Limits

The document must be below 20MiB in size in both compressed and uncompressed form. Compression is available in Couchbase Capella, and in the Enterprise Edition of self-managed Couchbase Server.

> [!TIP]
> This size limit is enforced by Couchbase Server; in practice it will affect very few users, as most JSON documents are considerably smaller. A compressed doument of just under 20MB, which is greater than 20,971,520 bytes (20 MiB) when uncompressed, will be rejected by the server as follows:
> 
> * Couchbase Server decompresses the document to check that it is valid JSON, and is correctly compressed with _Snappy_, and at this point measures it against `max data size` (20 MiB).
> * If the decompressed value's size exceeds this limit, the mutation is failed with a "too big" error code (E2BIG code 3).
> 
> Therefore, where necessary, enforce document size limits in your application on _uncompressed_ documents.

## [](#operating-modes-server-side)Operating Modes (Server-side)

The three modes in which compression can be used — "off", "passive", and "active" — are configured per bucket in the configuration settings on the cluster.

__Table 1\. Compression Operating Modes__
|                                                                       | **OFF**                              | **PASSIVE**                  | **ACTIVE**                                                                                  |
| --------------------------------------------------------------------- | ------------------------------------ | ---------------------------- | ------------------------------------------------------------------------------------------- |
| Negotiating SNAPPY                                                    | ignore                               | acknowledge                  | acknowledge                                                                                 |
| Sending compressed data when SNAPPY feature **enabled**               | \-                                   | accept                       | accept                                                                                      |
| Sending compressed data when SNAPPY feature **disabled**              | reject as invalid                    | reject as invalid            | reject as invalid                                                                           |
| Receiving data which were previously compressed on the server         | server inflates and sends plain data | server sends compressed data | server sends compressed data                                                                |
| Receiving data which were **not** previously compressed on the server | server sends plain data              | server sends plain data      | server might send compressed data (the compression is done in the background on the server) |

## [](#compression-for-net-sdk-3-4-10-to-3-5-1)Compression for .NET SDK 3.4.10 to 3.5.1

[Snappier](https://github.com/brantburnett/Snappier) is integrated with the [.NET Couchbase.Extensions Library](https://github.com/couchbaselabs/Couchbase.Extensions). Since [.NET SDK 3.4.10](../project-docs/sdk-release-notes.md#version-3-4-10), the .NET SDK has been able to work with external Snappy libraries as the setting for the Server flag `SnappyEverywhere` is now supported.

Install Snappier with the [.NET Couchbase.Extensions](https://github.com/couchbaselabs/Couchbase.Extensions) Library.