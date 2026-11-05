---
title: Index Service API
description: The Index service REST API provides configuration options for the
  Index service.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/rest-api/pages/rest-index-service.adoc
  xref: xref:7.6@server:rest-api:rest-index-service.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/rest-api/rest-index-service.html)

# Index Service API

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

> The Index service REST API provides configuration options for the Index service. 

## [](#apis-in-this-section)APIs in this Section

The REST API allows Index-Service indexes to be created and managed. For a list of the methods and URIs covered in these pages, see the table below.

| HTTP Method | URI                              | Documented at                                                                  |
| ----------- | -------------------------------- | ------------------------------------------------------------------------------ |
| GET         | /settings/indexes                | [Retrieve GSI Settings](get-settings-indexes.md)                               |
| POST        | /settings/indexes                | [Set GSI Settings](post-settings-indexes.md)                                   |
| GET         | /api/v1/stats                    | [Get Node Statistics](../index-rest-stats/index.md#get%5Fnode%5Fstats)         |
| GET         | /api/v1/stats/{keyspace}         | [Get Keyspace Statistics](../index-rest-stats/index.md#get%5Fkeyspace%5Fstats) |
| GET         | /api/v1/stats/{keyspace}/{index} | [Get Index Statistics](../index-rest-stats/index.md#get%5Findex%5Fstats)       |