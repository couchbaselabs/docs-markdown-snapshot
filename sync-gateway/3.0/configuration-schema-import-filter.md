---
title: Import Filter Configuration
description: Using Sync Gateway's Admin REST API and the Import Filter function
  to configure access
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/configuration-schema-import-filter.adoc
  xref: xref:3.0@sync-gateway::configuration-schema-import-filter.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/configuration-schema-import-filter.html)

# Import Filter Configuration

> [!IMPORTANT]
> Pre-3.0 Legacy Configuration Equivalents
> 
> This content describes configuration for Sync Gateway 3.0 and higher — for legacy configuration, see: [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

## [](#upsert-import-filter-function)Upsert Import Filter Function

https:://{sgw-uri}/{db}/_config/import_filter

Use this convenience endpoint to add or update the `import_filter` Javascript function for an existing Sync Gateway database.

See the 'Model' below for more info

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect

See: [Import filter](import-filter.md) for more.

## [](#parameters)Parameters

| Type     | Name                          | Description                                       | Schema                                               |
| -------- | ----------------------------- | ------------------------------------------------- | ---------------------------------------------------- |
| **Path** | **db** _required_             | Database name                                     | string                                               |
| **Body** | **import\_filter** _required_ | The Javascipt code for the import filter function | [Import\_filter\_model](#%5Fimport%5Ffilter%5Fmodel) |

## [](#responses)Responses

| HTTP Code | Description                                       | Schema                                               |
| --------- | ------------------------------------------------- | ---------------------------------------------------- |
| **200**   | OK                                                | [Import\_filter\_model](#%5Fimport%5Ffilter%5Fmodel) |
| **401**   | 401 - Unauthorized - Error validating credentials | No Content                                           |

## [](#%5FImport%5Ffilter)Schema

This section shows Sync Gateway's import control configuration settings in schema format for convenience in constructing JSON models for use in the Admin REST API.

The configuration settings described here are provisioned through the [Access Control](rest-api-admin.md#/Access%5FControl) endpoints.

### [](#%5Fimport%5Ffilter%5Fmodel)Import\_filter\_model

The `import_filter` controls whether a document written to the Couchbase Server bucket should be made available to Couchbase Mobile clients (that is, whether it ought to be imported).

You should provision the filter as a Javascript function in the request body of a call to the Admin Rest API endpoint `put {db}/_config/import_filter`.

Set the header's content type to `content-Type: application/javascript`.

The function takes the document body as parameter and is expected to return a boolean to indicate whether the document should be imported.

If you do not provide a filter function then no filter will be applied and ALL documents will be imported.

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
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](#)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)