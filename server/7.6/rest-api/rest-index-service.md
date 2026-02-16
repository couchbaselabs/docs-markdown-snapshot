[View original HTML](/server/7.6/rest-api/rest-index-service.html)

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