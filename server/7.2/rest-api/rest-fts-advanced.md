---
title: Advanced
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/rest-fts-advanced.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:rest-api:rest-fts-advanced.adoc[]
---

[View original HTML](/server/7.2/rest-api/rest-fts-advanced.html)

# Advanced

## [](#index-partition-definition)Index Partition Definition

GET /api/pindex

Get information about an index partition.

**Permission Required**: cluster.bucket\[\].fts!read

**Role Required**: FTS-Searcher, FTS-Admin

Sample response

{
    "pindexes": {
        "myFirstIndex_6cc599ab7a85bf3b_0": {
            "indexName": "myFirstIndex",
            "indexParams": "",
            "indexType": "blackhole",
            "indexUUID": "6cc599ab7a85bf3b",
            "name": "myFirstIndex_6cc599ab7a85bf3b_0",
            "sourceName": "",
            "sourceParams": "",
            "sourcePartitions": "",
            "sourceType": "nil",
            "sourceUUID": "",
            "uuid": "2d9ecb8b574a9f6a"
        }
    },
    "status": "ok"
}

GET /api/pindex/{pindexName}

**Permission Required**: cluster.bucket\[`bucket_name`\].fts!read

**Role Required**: FTS-Searcher, FTS-Admin

## [](#index-partition-querying)Index Partition Querying

GET /api/pindex/{pindexName}/count

**Permission Required**: cluster.bucket\[`bucket_name`\].fts!read

**Role Required**: FTS-Searcher, FTS-Admin

POST /api/pindex/{pindexName}/query

**Permission Required**: cluster.bucket\[`bucket_name`\].fts!write

**Role Required**: FTS-Admin

## [](#fts-memory-quota)FTS Memory Quota

POST /pools/default

**Permission Required**: cluster.bucket\[`bucket_name`\].fts!manage

**Role Required**: FTS-Admin

Specify the `ftsMemoryQuota` parameter with an integer value (example: ftsMemoryQuota=512) to set the memory quota for the full text search (FTS) service.