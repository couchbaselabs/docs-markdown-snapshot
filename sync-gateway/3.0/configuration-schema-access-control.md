---
title: Access Control Configuration
description: Using Sync Gateway's Admin REST API and the Sync function to configure access
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/configuration-schema-access-control.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.0@sync-gateway::configuration-schema-access-control.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/configuration-schema-access-control.html)

# Access Control Configuration

> [!IMPORTANT]
> Pre-3.0 Legacy Configuration Equivalents
> 
> This content describes configuration for Sync Gateway 3.0 and higher — for legacy configuration, see: [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

## [](#upsert-sync-function)Upsert Sync Function

The sync function is crucial to the security of your application. It is in charge of data validation, access control and routing. The function executes every time a new revision/update is made to a document.

https:://{sgw-uri}/{db}/_config/sync

Use this convenience endpoint to add or update the `Sync` function for an existing Sync Gateway database

See the 'Model' below for more info

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect

Use this convenience endpoint to add or update the `Sync` function for an existing Sync Gateway database

See the 'Model' below for more info

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect

For more on the Sync Function and access control see: [Sync Function Overview](sync-function-overview.md)

## [](#parameters)Parameters

| Type     | Name                         | Description                              | Schema                          |
| -------- | ---------------------------- | ---------------------------------------- | ------------------------------- |
| **Path** | **db** _required_            | Database name                            | string                          |
| **Body** | **sync function** _required_ | The Javascipt code for the sync function | [Sync\_model](#%5Fsync%5Fmodel) |

| Type     | Name                         | Description                              | Schema                          |
| -------- | ---------------------------- | ---------------------------------------- | ------------------------------- |
| **Path** | **db** _required_            | Database name                            | string                          |
| **Body** | **sync function** _required_ | The Javascipt code for the sync function | [Sync\_model](#%5Fsync%5Fmodel) |

## [](#responses)Responses

| HTTP Code | Description                                       | Schema                          |
| --------- | ------------------------------------------------- | ------------------------------- |
| **200**   | OK                                                | [Sync\_model](#%5Fsync%5Fmodel) |
| **401**   | 401 - Unauthorized - Error validating credentials | No Content                      |

| HTTP Code | Description                                       | Schema                          |
| --------- | ------------------------------------------------- | ------------------------------- |
| **200**   | OK                                                | [Sync\_model](#%5Fsync%5Fmodel) |
| **401**   | 401 - Unauthorized - Error validating credentials | No Content                      |

## [](#%5Fsync%5Ffunction)Schema

This section shows Sync Gateway’s access control configuration settings in schema format for convenience in constructing JSON models for use in the Admin REST API.

The configuration settings described here are provisioned through the [Access Control](rest-api-admin.md#/Access%5FControl) endpoints.

### [](#%5Fsync%5Fmodel)Sync\_model

The `sync` property is a Javascript function that determines which users can access which documents.

This JavaScript function is provisioned using the Admin Rest API Endpoint `put /{db}/_config/sync`

Add the function as plain javascript in the request body, with the `content-Type: application/javascript` header.

_Type_ : string

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](configuration-schema-bootstrap.md)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](#)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)