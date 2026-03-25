---
title: Database Security
description: Using Sync Gateway's Admin REST API to configure users and roles
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/configuration-schema-db-security.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.0@sync-gateway::configuration-schema-db-security.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/configuration-schema-db-security.html)

# Database Security

> Using Sync Gateway’s Admin REST API to configure users and roles  

_Related topics_: [Overview](configuration-overview.md) | [Bootstrap](configuration-schema-bootstrap.md) | [Database](configuration-schema-database.md) | [Database Security](#configuration-schema-db-security&.adoc#8212;​page}) | [Access Control](configuration-schema-access-control.md) | [Import](configuration-schema-import-filter.md) | [Inter-Sync Gateway Replication](configuration-schema-isgr.md)

> [!IMPORTANT]
> Pre-3.0 Legacy Configuration Equivalents
> 
> This content describes configuration for Sync Gateway 3.0 and higher — for legacy configuration, see: [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

## [](#introduction)Introduction

In 3.0 we use the Admin REST API `_user` and `_role` endpoints to provision and manage sync gateway users through persistent configuration changes.

This content introduces the [Create or Update a Role](#lbl-upsert-role) and [Create or Update a User](#lbl-upsert-user) endpoints for convenience — see [Database Security](rest-api-admin.md#/Database%5FSecurity) for a full description of the endpoints available.

It also includes a JSON-data model, you can use to build your request bodies. — see: [Schema](#lbl-schema)

## [](#lbl-upsert-role)Create or Update a Role

PUT /{db}/_role/{name}

Use this convenience endpoint to upsert a Sync Gateway role.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect
* Sync Gateway Application

### [](#parameters)Parameters

| Type     | Name                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Schema                          |
| -------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------- |
| **Path** | **db** _required_   | Database name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | string                          |
| **Path** | **name** _required_ | Role name, may contain any combination of the characters \[a-z A-Z 0-9 - + . @ %\], when creating a role any other characters must be percent encoded, see: <https://en.wikipedia.org/wiki/Percent-encoding>. When passing a role name in a URL path it must be escaped again using percent encoding for example if a role is created with the name "0\|59", the '|' character must first be percent-encoded resulting in "0%7C59". When using the same role name in a URL path it must be percent-encoded a second time resulting in "0%257C59" | string                          |
| **Body** | **role** _optional_ | The message body is a JSON document that contains the following objects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [Role\_model](#%5Frole%5Fmodel) |

### [](#responses)Responses

| HTTP Code | Description                                       | Schema     |
| --------- | ------------------------------------------------- | ---------- |
| **200**   | 200 - OK - Operation successful                   | No Content |
| **201**   | 201 - OK - Create Operation successful            | No Content |
| **401**   | 401 - Unauthorized - Error validating credentials | No Content |

### [](#example)Example

* Curl
* HTTP

```bash
curl --location --request PUT 'http://127.0.0.1:4985/travel25/_role/newrole' \ (1)
--header 'Authorization: Basic c3luY19nYXRld2F5OnBhc3N3b3Jk' \ (2)
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "newrole",
    "admin_channels": ["newrolechannel"]
}'
```

```bash
PUT /travel25/_role/newrole HTTP/1.1 (1)
Host: 127.0.0.1:4985
Authorization: Basic c3luY19nYXRld2F5OnBhc3N3b3Jk (2)
Content-Type: application/json
Content-Length: 67

{
    "name": "newrole",
    "admin_channels": ["newrolechannel"]
}
```

| **1** | Add role newrole to the travel25 database                             |
| ----- | --------------------------------------------------------------------- |
| **2** | Note we are using Basic Auth to authenticate to an existing RBAC user |

## [](#lbl-upsert-user)Create or Update a User

PUT /{db}/_user/{username} **(1)**

| **1** | where {db} is the Sync Gateway database and {username} is the name for the new user |
| ----- | ----------------------------------------------------------------------------------- |

Use this method to create or update a user

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect
* Sync Gateway Application

### [](#parameters-2)Parameters

| Type     | Name                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Schema                          |
| -------- | -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| **Path** | **db** _required_                      | Database name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | string                          |
| **Path** | **name** _required_                    | User’s name, may contain contain any combination of the characters \[a-z A-Z 0-9 - + . @ %\], when creating a user any other characters must be percent encoded, see: <https://en.wikipedia.org/wiki/Percent-encoding>. When passing a user name in a URL path it must be escaped again using percent encoding for example if a user is created with the name "0\|59", the '|' character must first be percent-encoded resulting in "0%7C59". When using the same user name in a URL path it must be percent-encoded a second time resulting in "0%257C59" | string                          |
| **Body** | **user configuration data** _optional_ | Provision the user configuration data in JSON format in the body                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | [User\_model](#%5Fuser%5Fmodel) |

### [](#responses-2)Responses

| HTTP Code | Description                                       | Schema     |
| --------- | ------------------------------------------------- | ---------- |
| **200**   | 200 - OK - Operation successful                   | No Content |
| **201**   | 201 - OK - Create Operation successful            | No Content |
| **401**   | 401 - Unauthorized - Error validating credentials | No Content |

### [](#example-2)Example

* Curl
* HTTP

```bash
curl --location --request PUT 'http://127.0.0.1:4985/travel25/_user/newuser' \ (1)
--header 'Authorization: Basic c3luY19nYXRld2F5OnBhc3N3b3Jk' \
--header 'Content-Type: application/json' \
--data-raw '{
    "password": "pass",
    "admin_channels": ["newrole"]
}
'
```

```bash
PUT /travel25/_user/newuser HTTP/1.1 (1)
Host: 127.0.0.1:4985
Authorization: Basic c3luY19nYXRld2F5OnBhc3N3b3Jk
Content-Type: application/json
Content-Length: 63

{
    "password": "pass",
    "admin_channels": ["newrole"]
}
```

| **1** | Add user newuser to the travel25 database |
| ----- | ----------------------------------------- |

## [](#lbl-schema)Schema

This section shows Sync Gateway’s database security configuration settings in schema format for convenience in constructing JSON models for use in the Admin REST API.

The configuration settings described here are provisioned through the Admin REST API — see as shown in [Database Security](rest-api-admin.md#/Database%5FSecurity).

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
* [Database Security](#)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)