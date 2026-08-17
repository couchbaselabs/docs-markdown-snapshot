---
title: Database Configuration
description: Using Sync Gateway's Admin REST API to configure and manage databases
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/configuration-schema-database.adoc
  xref: xref:3.0@sync-gateway::configuration-schema-database.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/configuration-schema-database.html)

# Database Configuration

> Using Sync Gateway's Admin REST API to configure and manage databases  

_Related topics_: [Overview](configuration-overview.md) | [Bootstrap](configuration-schema-bootstrap.md) | Database | [Database Security](#configuration-schema-db-security&.adoc#8212;​page}) | [Access Control](configuration-schema-access-control.md) | [Import](configuration-schema-import-filter.md) | [Inter-Sync Gateway Replication](configuration-schema-isgr.md)

> [!IMPORTANT]
> Pre-3.0 Legacy Configuration Equivalents
> 
> This content describes configuration for Sync Gateway 3.0 and higher — for legacy configuration, see: [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

## [](#introduction)Introduction

From _Sync Gateway_ 3.0 you can use the Admin REST API to provision persistent configuration changes. This content introduces the [Create Database](#lbl-create-db) and [Configure Database](#lbl-configure-db) endpoints for convenience — see [Database Configuration](rest-api-admin.md#/Database%5FConfiguration/) for a full description of the endpoints available.

## [](#lbl-create-db)Create Database

PUT {url}/{dbname}/

Use this method to create a new Sync Gateway database.

The database name is taken from the URL path. Pass the required database configuration settings as a JSON object in the request body.

{
    "name": "todo_db"
    "bucket": "todo_app"
}

By default the created database is brought online immediately, **unless** you include `"offline": true` in the configuration.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect

### [](#parameters)Parameters

| Type     | Name                                          | Description                                                                 | Schema                                  |
| -------- | --------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------- |
| **Path** | **db** _required_                             | Database name                                                               | string                                  |
| **Body** | **database configuration details** _optional_ | Provision the database configuration details as JSON object in request body | [Database\_model](#%5Fdatabase%5Fmodel) |

### [](#responses)Responses

| HTTP Code | Description                                       | Schema     |
| --------- | ------------------------------------------------- | ---------- |
| **201**   | 201 - OK - Create Operation successful            | No Content |
| **401**   | 401 - Unauthorized - Error validating credentials | No Content |

### [](#example)Example

Example 1\. Create database

Here we create a new sync gateway database.

* Curl
* HTTP

```bash
curl --location --request PUT 'http://127.0.0.1:4985/traveldb/' \ (1)
--header 'Authorization: Basic c3luY19nYXRld2F5OnBhc3N3b3Jk' \ (2)
--header 'Content-Type: application/json' \
--data-raw '{
"bucket": "todo", (3)
"num_index_replicas": 0}'
```

```http
PUT /traveldb/ HTTP/1.1 (1)
Host: 127.0.0.1:4985
Authorization: Basic c3luY19nYXRld2F5OnBhc3N3b3Jk (2)
Content-Type: application/json
Content-Length: 44

{
"bucket": "todo", (3)
"num_index_replicas": 0}
```

| **1** | Here we create a sync gateway database called traveldb                                                     |
| ----- | ---------------------------------------------------------------------------------------------------------- |
| **2** | Note we are using Basic Authentication here to authenticate against an existing Couchbase Server RBAC user |
| **3** | Here we point to the Couchbase Server bucket called todo                                                   |

## [](#lbl-configure-db)Configure Database

PUT {url}/{db}/_config

Use this endpoint to update the configuration of an existing Sync Gateway database.

Provide the database name in the URL path. Provide the required database configuration settings as a JSON object in the request body.

By default the updated database is brought online immediately, **unless** you include `"offline": true` in the configuration.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect
* Sync Gateway Application

### [](#parameters-2)Parameters

| Type     | Name                                          | Description                                                                 | Schema                                  |
| -------- | --------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------- |
| **Path** | **db** _required_                             | Database name                                                               | string                                  |
| **Body** | **database configuration details** _optional_ | Provision the database configuration details as JSON object in request body | [Database\_model](#%5Fdatabase%5Fmodel) |

### [](#responses-2)Responses

| HTTP Code | Description                                       | Schema     |
| --------- | ------------------------------------------------- | ---------- |
| **200**   | 200 - OK - Operation successful                   | No Content |
| **401**   | 401 - Unauthorized - Error validating credentials | No Content |

### [](#example-2)Example

Example 2\. Configure database

Here we configure an existing sync gateway database.

* Curl
* HTTP

```bash
curl --location --request PUT 'http://127.0.0.1:4985/traveldb/_config/' \ (1)
--header 'Authorization: Basic c3luY19nYXRld2F5OnBhc3N3b3Jk' \ (2)
--header 'Content-Type: application/json' \
--data-raw '{
  "enable_shared_bucket_access": true,
  "import_docs": true
}' (3)
```

```http
PUT /traveldb/_config/ HTTP/1.1  (1)
Host: 127.0.0.1:4985
Authorization: Basic c3luY19nYXRld2F5OnBhc3N3b3Jk  (2)
Content-Type: application/json
Content-Length: 120

{
"enable_shared_bucket_access": true,
"import_docs": true
} (3)
```

| **1** | Here we choose to configure (\_config) a sync gateway database called traveldb                             |
| ----- | ---------------------------------------------------------------------------------------------------------- |
| **2** | Note we are using Basic Authentication here to authenticate against an existing Couchbase Server RBAC user |
| **3** | Here we toggle a couple of database properties                                                             |

## [](#%5Fdatabase)Schema

This section shows Sync Gateway's database configuration settings in schema format for convenience in constructing JSON models for use in the Admin REST API.

The configuration settings described here are provisioned through the [Database Configuration](rest-api-admin.md#/Database%5FConfiguration/) endpoints.

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
* [Database](#)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)