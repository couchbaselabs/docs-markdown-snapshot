---
title: Index Service API
description: The Index Service REST APIs provide configuration options for the
  Index Service.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/rest-index-service.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:rest-api:rest-index-service.adoc[]
---

[View original HTML](/server/current/rest-api/rest-index-service.html)

# Index Service API

> The Index Service REST APIs provide configuration options for the Index Service. 

## [](#apis-in-this-section)APIs in this Section

For a list of the methods and URIs covered in these pages, see the tables below.

By default, the Index REST APIs below listen on port `9102`, or `19102` for secure access. Note that the GSI Settings API listens on port `8091`, or `18091` for secure access.

### [](#gsi-settings)GSI Settings

| HTTP Method | URI               | Documented at                                    |
| ----------- | ----------------- | ------------------------------------------------ |
| GET         | /settings/indexes | [Retrieve GSI Settings](get-settings-indexes.md) |
| POST        | /settings/indexes | [Set GSI Settings](post-settings-indexes.md)     |

### [](#index-statistics)Index Statistics

| HTTP Method | URI                              | Documented at                                                                  |
| ----------- | -------------------------------- | ------------------------------------------------------------------------------ |
| GET         | /api/v1/stats                    | [Get Node Statistics](../index-rest-stats/index.md#get%5Fnode%5Fstats)         |
| GET         | /api/v1/stats/{keyspace}         | [Get Keyspace Statistics](../index-rest-stats/index.md#get%5Fkeyspace%5Fstats) |
| GET         | /api/v1/stats/{keyspace}/{index} | [Get Index Statistics](../index-rest-stats/index.md#get%5Findex%5Fstats)       |

### [](#index-settings)Index Settings

| HTTP Method | URI       | Documented at                                                             |
| ----------- | --------- | ------------------------------------------------------------------------- |
| GET         | /settings | [Retrieve Index Settings](../index-rest-settings/index.md#get%5Fsettings) |
| POST        | /settings | [Update Index Settings](../index-rest-settings/index.md#post%5Fsettings)  |