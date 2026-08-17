---
title: Index Service API
description: The Index service REST API provides configuration options for the
  Index service.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/rest-index-service.adoc
  xref: xref:7.2@server:rest-api:rest-index-service.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/rest-api/rest-index-service.html)

# Index Service API

> The Index service REST API provides configuration options for the Index service. 

## [](#apis-in-this-section)APIs in this Section

The REST API allows Index-Service indexes to be created and managed. For a list of the methods and URIs covered in these pages, see the table below.

| HTTP Method | URI                              | Documented at                                                            |
| ----------- | -------------------------------- | ------------------------------------------------------------------------ |
| GET         | /settings/indexes                | [Retrieve GSI Settings](get-settings-indexes.md)                         |
| POST        | /settings/indexes                | [Set GSI Settings](post-settings-indexes.md)                             |
| GET         | /api/v1/stats                    | [Get Node Statistics](rest-index-stats.md#%5Fget%5Fnode%5Fstats)         |
| GET         | /api/v1/stats/{keyspace}         | [Get Keyspace Statistics](rest-index-stats.md#%5Fget%5Fkeyspace%5Fstats) |
| GET         | /api/v1/stats/{keyspace}/{index} | [Get Index Statistics](rest-index-stats.md#%5Fget%5Findex%5Fstats)       |