---
title: Setting Storage Thread Allocations
description: Couchbase Server has several settings that let you change how it
  allocates and uses threads for storage across the entire cluster.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/rest-api/pages/rest-reader-writer-thread-config.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/rest-api/rest-reader-writer-thread-config.html)

# Setting Storage Thread Allocations

> Couchbase Server has several settings that let you change how it allocates and uses threads for storage across the entire cluster. 

## [](#http-method-and-uri)HTTP method and URI

Get Global Thread Settings

```url
GET /pools/default/settings/memcached/global
```

Set Global Thread Allocations

```none
POST /pools/default/settings/memcached/global
```

## [](#description)Description

Couchbase Server lets you set the number of threads per node for reading, writing, NonIO, and AuxIO thread pools. You can also change the number of threads that Magma buckets use for writing data to disk. Increasing thread allocation can improve performance on systems with a large number of CPU cores. For example, more writer threads can optimize durable write performance. For more information, see [Durability](../learn/data/durability.md). However, allocating too many threads can reduce performance on nodes with limited resources. Test any changes to thread allocation before applying them to production systems.

## [](#getting-current-thread-settings)Getting Current Thread Settings

To get the current global thread settings for Couchbase Server, send a GET request to the `/pools/default/settings/memcached/global` endpoint.

### [](#get-curl-syntax)curl Syntax

```bash
curl -X GET http[s]://{host}:{port}/pools/default/settings/memcached/global
     -u $USER:$PASSWORD
```

#### [](#path-parameters)Path Parameters

`host`

Hostname or IP address of a Couchbase Server.

`port`

Port number for the REST API. Defaults are 8091 for unencrypted and 18901 for encrypted connections.

`$USER`

The name of a user who has at least 1 of the roles listed in [Required Privileges](#required-privileges-get).

`$PASSWORD`

The password for the user.

### [](#required-privileges-get)Required Privileges

Your account must have at least 1 of the following roles to make a GET request from this endpoint:

* [Full Admin](../learn/security/roles.md#full-admin)
* [Cluster Admin](../learn/security/roles.md#cluster-admin)
* [External User Security Admin](../learn/security/roles.md#external-user-security-admin)
* [Local User Security Admin](../learn/security/roles.md#local-user-security-admin)

### [](#responses)Responses

200 OK

The request was successful. Returns a JSON object containing the current global thread settings that have been set explicitly.

400 Bad Request

The request could not be understood. Also returns a JSON object containing an error message.

### [](#example)Example

The following example shows how to get the current global thread settings for Couchbase Server:

```bash
curl -X GET -u Administrator:password \
http://localhost:8091/pools/default/settings/memcached/global | jq
```

If successful, the call returns a JSON object containing the any overrides to the default global thread settings:

```json
{
  "magma_flusher_thread_percentage": 30,
  "num_storage_threads": 25
}
```

## [](#setting-global-thread-allocations)Setting Global Thread Allocations

To set the global thread allocations for Couchbase Server, send a `POST` to the `/pools/default/settings/memcached/global` endpoint.

### [](#curl-syntax)curl Syntax

```bash
curl -X POST http[s]://{host}:{port}/pools/default/settings/memcached/global
  [-d num_reader_threads=<integer>]
  [-d num_writer_threads=<integer>]
  [-d num_nonio_threads=<integer>]
  [-d num_auxio_threads=<integer>]
  [-d num_storage_threads=<integer>]
  [-d magma_flusher_thread_percentage=<integer>]
  -u $USER:$PASSWORD
```

#### [](#path-parameters-2)Path Parameters

`host`

Hostname or IP address of a Couchbase Server.

`port`

Port number for the REST API. Defaults are 8091 for unencrypted and 18901 for encrypted connections.

`$USER`

The name of a user who has at least 1 of the roles listed in [Required Privileges](#required-privileges-put).

`$PASSWORD`

The password for the user.

#### [](#parameters)Parameters

(optional) Sets the number of threads Couchbase Server uses to read data.

`num_writer_threads`

(optional) Sets the number of threads Couchbase Server uses to write data.

`num_nonio_threads`

(optional) Sets the number of NonIO threads to be used by Couchbase Server. The NonIO thread pool runs in-memory tasks. For example, the durability timeout task uses these threads. Valid values are:

* An integer from `1` to `64`: sets the number of threads.
* `default`: Couchbase Server calculates and applies an appropriate number of threads.

`num_auxio_threads`

(optional) Sets the number of AuxIO threads to be used by Couchbase Server. The AuxIO thread pool runs auxiliary I/O tasks — for example, the access log task. Valid values are:

* An integer from `1` to `64`: sets the number of threads.
* `default`: Couchbase Server determines the number of threads.

`num_storage_threads`

(optional) Sets the number of threads the Magma storage engine can use when compacting and writing data to disk. This thread pool is divided into 2 types of threads: flusher threads and compactor threads. For more information, see [Magma Flushing and Compaction Threads](../learn/buckets-memory-and-storage/storage-settings.md#magma-flushing-and-compaction-threads).

The default value is `20`.

`magma_flusher_thread_percentage`

(optional) Sets the percentage of Magma storage engine threads to allocate to flushing compacted data to disk. The remaining threads in the thread pool are allocated to compacting data. For example, if you set `num_storage_threads` to `20` and set `magma_flusher_thread_percentage` to `50`, Couchbase Server uses `10` threads to flush data and `10` threads to compact data. For more information, see [Magma Flushing and Compaction Threads](../learn/buckets-memory-and-storage/storage-settings.md#magma-flushing-and-compaction-threads).

Valid values for this setting are integers from `0` to `100`.

The default setting is `20` which allocates 20% of threads to flushing data.

> [!NOTE]
> `num_storage_threads` and `magma_flusher_thread_percentage` are advanced settings. Contact Couchbase Support before making changes to them. Support can help you determine the best settings for your workload and hardware.

### [](#required-privileges-put)Required Privileges

Your account must have at least 1 of the following roles to make a POST request to this endpoint:

* [Full Admin](../learn/security/roles.md#full-admin)
* [Cluster Admin](../learn/security/roles.md#cluster-admin)

### [](#responses)Responses

202 Accepted

The request was successful. This result also returns a JSON object containing all non-default thread settings.

400 Bad Request

The request had errors or invalid values. This result also returns a JSON object containing an error message.

Success returns an object whose values confirm the settings that have been made.

### [](#examples)Examples

To set the numbers of reader, writer, NonIO, and AuxIO threads for Couchbase Server, use the `POST /pools/default/settings/memcached/global` http method and endpoint as follows:

```bash
curl -X POST -u Administrator:password \
http://localhost:8091/pools/default/settings/memcached/global \
-d num_reader_threads=12 \
-d num_writer_threads=8 \
-d num_nonio_threads=6 \
-d num_auxio_threads=6 | jq
```

This sets the number of `reader` threads to `12`, the number of `writer` threads to `8`, and the numbers of `NonIO` and `AuxIO` threads each to `6`. If successful, the call returns an object that confirms the settings you specified:

```json
{
  "num_reader_threads": 12,
  "num_writer_threads": 8,
  "num_auxio_threads": 6,
  "num_nonio_threads": 6
}
```

The following example increases the Magma storage engine’s thread pool to 30 threads and allocates 25% of the threads to flushing data to disk:

```bash
curl -X POST -u Administrator:password \
     http://localhost:8091/pools/default/settings/memcached/global \
     -d num_storage_threads=30 \
     -d magma_flusher_thread_percentage=25 | jq
```

If successful, the call returns an object confirming your new settings:

```json
{
  "magma_flusher_thread_percentage": 25,
  "num_storage_threads": 30
}
```

## [](#see-also)See Also

* [Durability](../learn/data/durability.md)
* [Threading](../learn/buckets-memory-and-storage/storage-settings.md#threading)