---
title: Memory and Storage
description: Couchbase-Server memory and storage can be managed by means of the REST API.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/rest-memory-and-storage.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/rest-api/rest-memory-and-storage.html)

# Memory and Storage

## [](#apis-in-this-section)APIs in this Section

Using the REST API, _memory quotas_ can be allocated to services, and the current allocations retrieved. During cluster initialization, the _on-disk paths_ for services can be specified on a _per node_ basis.

_Reader and writer threads_ can be configured, to ensure that disk access is highly performant.

Additionally, _compaction_ can be managed: this is used by Couchbase Server to relocate on-disk data; so as to ensure the data’s closest-possible proximity, and thereby reclaim fragments of unused disk-space. The periodic compaction of a bucket’s data helps to ensure the ongoing efficiency of both reads and writes.

Administrators can initiate the compaction of a single bucket’s data at any time, and can cancel such compaction if and when necessary. The REST APIs that support this are described in [Performing Compaction Manually](rest-compact-post.md).

Additionally, settings are provided whereby compaction is triggered _automatically_, according to a specified configuration and schedule. This _auto-compaction_ can be achieved in two ways:

* _Globally_, meaning that all buckets in the cluster are compacted according to the same configuration and schedule — with the exception of those buckets for which these default settings are deliberately overridden. The REST APIs that support global auto-compaction are described in [Auto-Compaction: Global](rest-autocompact-global.md).
* _Per bucket_, meaning that a specified bucket is automatically compacted according to a different configuration and schedule than those established as the global defaults. The REST APIs that support per-bucket auto-compaction are described in [Auto-Compaction: Per Bucket](rest-autocompact-per-bucket.md).

The methods and URIs covered in this section are listed in the table below.

| HTTP Method | URI                                                                      | Documented at                                                      |
| ----------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| POST        | /nodes/self/controller/settings                                          | [Initializing a Node](rest-initialize-node.md)                     |
| POST        | /pools/default                                                           | [Configuring Memory](rest-configure-memory.md)                     |
| POST        | /pools/default/settings/memcached/global                                 | [Setting Thread Allocations](rest-reader-writer-thread-config.md)  |
| GET         | /nodes/self                                                              | [Getting Storage Information](rest-getting-storage-information.md) |
| POST        | /pools/default/buckets/\[bucket-name\]/controller/compactBucket          | [Performing Compaction Manually](rest-compact-post.md)             |
| POST        | /pools/default/buckets/\[bucket-name\]/controller/cancelBucketCompaction | [Performing Compaction Manually](rest-compact-post.md)             |
| GET         | /settings/autoCompaction                                                 | [Auto-Compaction: Global](rest-autocompact-global.md)              |
| POST        | /controller/setAutoCompaction                                            | [Auto-Compaction: Global](rest-autocompact-global.md)              |
| GET         | /pools/default/buckets/\[bucket-name\]                                   | [Auto-Compaction: Per Bucket](rest-autocompact-per-bucket.md)      |
| POST        | /pools/default/buckets/\[bucket-name\]                                   | [Auto-Compaction: Per Bucket](rest-autocompact-per-bucket.md)      |