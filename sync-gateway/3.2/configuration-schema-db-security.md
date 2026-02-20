---
title: Database Security
description: Using Sync Gateway's Admin REST API to configure users and roles
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.2/modules/ROOT/pages/configuration-schema-db-security.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:3.2@sync-gateway::configuration-schema-db-security.adoc[]
---

[View original HTML](/sync-gateway/3.2/configuration-schema-db-security.html)

# Database Security

> Using Sync Gateway’s Admin REST API to configure users and roles  

_Related topics_: [Overview](configuration-overview.md) | [Bootstrap](configuration-schema-bootstrap.md) | [Database](configuration-schema-database.md) | [Database Security](#configuration-schema-db-security&.adoc#8212;​page}) | [Access Control](configuration-schema-access-control.md) | [Import](configuration-schema-import-filter.md) | [Inter-Sync Gateway Replication](configuration-schema-isgr.md)

> [!IMPORTANT]
> Pre-3.0 Legacy Configuration Equivalents
> 
> This content describes configuration for Sync Gateway 3.0 and higher — for legacy configuration, see: [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

## [](#introduction)Introduction

Use the Admin REST API `_user` and `_role` endpoints to provision and manage Sync Gateway users through persistent configuration changes.

This page introduces the [Create or Update a Role](#put%5Fdb-%5Frole-name) and [Create or Update a User](#put%5Fdb-%5Fuser-name) endpoints for convenience — see [Database Security](rest%5Fapi%5Fadmin.md#tag/Database-Security) for a full description of the endpoints available.

It also includes a JSON-data model, you can use to build your request bodies. See: [Schema](#lbl-schema)

## [](#lbl-upsert-role)Create or Update a Role

PUT /{db}/_role/{name}

For detailed parameters and response information, see: [/{db}/\_role/](rest%5Fapi%5Fadmin.md#tag/Database-Security/operation/post%5Fdb-%5Frole-)

### [](#example-using-named-collections)Example using Named collections

* Curl
* HTTP

```bash
curl --location --request PUT 'http://127.0.0.1:4985/travel25/_role/newrole' \ (1)
--header 'Authorization: Basic c3luY19nYXRld2F5OnBhc3N3b3Jk' \ (2)
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "newrole",
    "collection_access": {
      "scopename": {
          "collectionname": {
               "admin_channels": ["newrolechannel"]
          }
      }
   }
}'
```

```bash
PUT /travel25/_role/newrole HTTP/1.1 (1)
Host: 127.0.0.1:4985
Authorization: Basic c3luY19nYXRld2F5OnBhc3N3b3Jk (2)
Content-Type: application/json
Content-Length: 134

{
    "name": "newrole",
    "collection_access": {
      "scopename": {
          "collectionname": {
               "admin_channels": ["newrolechannel"]
          }
      }
   }
}
```

| **1** | Add role newrole to the travel25 database and the scopename scope and collectionname collection |
| ----- | ----------------------------------------------------------------------------------------------- |
| **2** | Note we are using Basic Auth to authenticate to an existing RBAC user                           |

### [](#example-using-default-collections)Example using Default collections

* Curl
* HTTP

```bash
curl --location --request PUT 'http://127.0.0.1:4985/travel25/_role/newrole' \ (1)
--header 'Authorization: Basic c3luY19nYXRld2F5OnBhc3N3b3Jk' \ (2)
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "newrole",
    "collection_access": {
      "_default": {
          "_default": {
               "admin_channels": ["newrolechannel"]
          }
      }
   }
}'
```

```bash
PUT /travel25/_role/newrole HTTP/1.1 (1)
Host: 127.0.0.1:4985
Authorization: Basic c3luY19nYXRld2F5OnBhc3N3b3Jk (2)
Content-Type: application/json
Content-Length: 132

{
    "name": "newrole",
    "collection_access": {
      "_default": {
          "_default": {
               "admin_channels": ["newrolechannel"]
          }
      }
   }
}
```

| **1** | Add role newrole to the travel25 database using the \_default scope and collection |
| ----- | ---------------------------------------------------------------------------------- |
| **2** | Note we are using Basic Auth to authenticate to an existing RBAC user              |

For complete role management operations, see: [/{db}/\_role/](rest%5Fapi%5Fadmin.md#tag/Database-Security/operation/post%5Fdb-%5Frole-)\[Role management API Reference\]

## [](#lbl-upsert-user)Create or Update a User

PUT /{db}/_user/{username} **(1)**

| **1** | where {db} is the Sync Gateway database and {username} is the name for the new user |
| ----- | ----------------------------------------------------------------------------------- |

For detailed parameters and response information, see: [{db}/\_user/{name}](rest-api-admin.md#tag/Database-Security/operation/put%5Fdb-%5Fuser-name)\[Create User\] or [/{db}/\_user/{name}](rest%5Fapi%5Fadmin.md#tag/Database-Security/operation/put%5Fdb-%5Fuser-name)\[Update User\]

### [](#example-using-named-collections-2)Example using Named collections

* Curl
* HTTP

```bash
curl --location --request PUT 'http://127.0.0.1:4985/travel25/_user/newuser' \ (1)
--header 'Authorization: Basic c3luY19nYXRld2F5OnBhc3N3b3Jk' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "newuser",
    "password": "pass",
    "collection_access": {
      "scopename": {
          "collectionname": {
               "admin_channels": ["newuserchannel"]
          }
      }
   }
}'
```

```bash
PUT /travel25/_user/newuser HTTP/1.1 (1)
Host: 127.0.0.1:4985
Authorization: Basic c3luY19nYXRld2F5OnBhc3N3b3Jk
Content-Type: application/json
Content-Length: 154

{
    "name": "newuser",
    "password": "pass",
    "collection_access": {
      "scopename": {
          "collectionname": {
               "admin_channels": ["newuserchannel"]
          }
      }
   }
}
```

| **1** | Add user newuser to the travel25 database with access to scopename.collectionname |
| ----- | --------------------------------------------------------------------------------- |

### [](#example-using-default-collections-2)Example using Default collections

* Curl
* HTTP

```bash
curl --location --request PUT 'http://127.0.0.1:4985/travel25/_user/newuser' \ (1)
--header 'Authorization: Basic c3luY19nYXRld2F5OnBhc3N3b3Jk' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "newuser",
    "password": "pass",
    "collection_access": {
      "_default": {
          "_default": {
               "admin_channels": ["newuserchannel"]
          }
      }
   }
}'
```

```bash
PUT /travel25/_user/newuser HTTP/1.1 (1)
Host: 127.0.0.1:4985
Authorization: Basic c3luY19nYXRld2F5OnBhc3N3b3Jk
Content-Type: application/json
Content-Length: 152

{
    "name": "newuser",
    "password": "pass",
    "collection_access": {
      "_default": {
          "_default": {
            "admin_channels": ["newuserchannel"]
        }
      }
   }
}
```

| **1** | Add user newuser to the travel25 database using the default scope and collection |
| ----- | -------------------------------------------------------------------------------- |

For complete user management operations, see: [/{db}/\_user/{name}](rest%5Fapi%5Fadmin.md#tag/Database-Security/operation/put%5Fdb-%5Fuser-name)\[User management API Reference\]

## [](#lbl-schema)Schema

This section shows Sync Gateway’s database security configuration settings in schema format for convenience in constructing JSON models for use in the Admin REST API.

The configuration settings described here are provisioned through the Admin REST API — see as shown in [Database Security](rest%5Fapi%5Fadmin.md#tag/Database-Security).

### [](#Role2)Role


{
   [admin_channels](#admin%5Fchannels): ["string"...],
   [all_channels](#all%5Fchannels): ["string"...],
   [collection_access](#collection%5Faccess): {
      [{scopename...}](#collection%5Faccess-{scopename}): {
         [{collectionname...}](#collection%5Faccess-{scopename}-{collectionname}): {
            [admin_channels](#collection%5Faccess-{scopename}-{collectionname}-admin%5Fchannels): ["string"...],
            [all_channels](#collection%5Faccess-{scopename}-{collectionname}-all%5Fchannels): ["string"...],
            [jwt_channels](#collection%5Faccess-{scopename}-{collectionname}-jwt%5Fchannels): ["string"...],
            [jwt_last_updated](#collection%5Faccess-{scopename}-{collectionname}-jwt%5Flast%5Fupdated): "string"
         }
      }
   },
   [name](#name): "string"
}

#### `admin_channels`

Type

array

Description

A list of channels to explicitly grant to the role for the default collection. See `collection_access` for channels in named collections.

#### `all_channels`

Type

array (readOnly)

Description

All the channels that the role has been granted access to for the default collection.

These channels could have been assigned by the Sync function or using the `admin_channels` property.

#### `collection_access`

Type

object

Description

A set of access grants by scope and collection for a specific collection.

#### `collection_access.{scopename…​}`

Type

object

Description

An object keyed by scope, containing a set of collections.

#### `collection_access.{scopename…​}.{collectionname…​}`

Type

object

Description

An object keyed by collection name, defines access collections in this scope.

#### `collection_access.{scopename…​}.{collectionname…​}.admin_channels`

Type

array

Description

A list of channels to explicitly grant to the user in this collection.

#### `collection_access.{scopename…​}.{collectionname…​}.all_channels`

Type

array (readOnly)

Description

All the channels that the user has been granted access to in this collection.

Access could have been granted through the sync function, roles, or explicitly on the user under the `admin_channels` property.

#### `collection_access.{scopename…​}.{collectionname…​}.jwt_channels`

Type

array (readOnly)

Description

The channels that the user has been granted access to through channels\_claim for this collection.

#### `collection_access.{scopename…​}.{collectionname…​}.jwt_last_updated`

Type

string (readOnly)

Description

The last time that the user's JWT channels were updated for this collection.

#### `name`

Type

string

Description

The name of the role.

Role names can only have alphanumeric ASCII characters and underscores.

### [](#User2)User


{
   [admin_channels](#admin%5Fchannels): ["string"...],
   [admin_roles](#admin%5Froles): ["string"...],
   [all_channels](#all%5Fchannels): ["string"...],
   [collection_access](#collection%5Faccess): {
      [{scopename...}](#collection%5Faccess-{scopename}): {
         [{collectionname...}](#collection%5Faccess-{scopename}-{collectionname}): {
            [admin_channels](#collection%5Faccess-{scopename}-{collectionname}-admin%5Fchannels): ["string"...],
            [all_channels](#collection%5Faccess-{scopename}-{collectionname}-all%5Fchannels): ["string"...],
            [jwt_channels](#collection%5Faccess-{scopename}-{collectionname}-jwt%5Fchannels): ["string"...],
            [jwt_last_updated](#collection%5Faccess-{scopename}-{collectionname}-jwt%5Flast%5Fupdated): "string"
         }
      }
   },
   [disabled](#disabled): false,
   [email](#email): "string",
   [jwt_channels](#jwt%5Fchannels): ["string"...],
   [jwt_issuer](#jwt%5Fissuer): "string",
   [jwt_last_updated](#jwt%5Flast%5Fupdated): "string",
   [jwt_roles](#jwt%5Froles): ["string"...],
   [name](#name): "string",
   [password](#password): "string",
   [roles](#roles): ["string"...]
}

#### `admin_channels`

Type

array

Description

A list of channels to explicitly grant to the user for the default collection. See `collection_access` for channels in named collections.

#### `admin_roles`

Type

array

Description

A list of roles to explicitly grant to the user.

#### `all_channels`

Type

array (readOnly)

Description

All the channels that the user has been granted access to for the default collection. See `collection_access` for channels in named collections.

Access could have been granted through the sync function, roles, or explicitly on the user under the `admin_channels` property.

#### `collection_access`

Type

object

Description

A set of access grants by scope and collection for a specific collection.

#### `collection_access.{scopename…​}`

Type

object

Description

An object keyed by scope, containing a set of collections.

#### `collection_access.{scopename…​}.{collectionname…​}`

Type

object

Description

An object keyed by collection name, defines access collections in this scope.

#### `collection_access.{scopename…​}.{collectionname…​}.admin_channels`

Type

array

Description

A list of channels to explicitly grant to the user in this collection.

#### `collection_access.{scopename…​}.{collectionname…​}.all_channels`

Type

array (readOnly)

Description

All the channels that the user has been granted access to in this collection.

Access could have been granted through the sync function, roles, or explicitly on the user under the `admin_channels` property.

#### `collection_access.{scopename…​}.{collectionname…​}.jwt_channels`

Type

array (readOnly)

Description

The channels that the user has been granted access to through channels\_claim for this collection.

#### `collection_access.{scopename…​}.{collectionname…​}.jwt_last_updated`

Type

string (readOnly)

Description

The last time that the user's JWT channels were updated for this collection.

#### `disabled`

Type

boolean

Description

If true, the user will not be able to login to the account as it is disabled.

#### `email`

Type

string

Description

The email address of the user.

#### `jwt_channels`

Type

array (readOnly)

Description

The channels that the user has been granted access to through channels\_claim for the default collection.

#### `jwt_issuer`

Type

string (readOnly)

Description

The issuer of the last JSON Web Token that the user last used to sign in.

#### `jwt_last_updated`

Type

string (readOnly)

Description

The last time that the user's JWT roles/channels were updated.

#### `jwt_roles`

Type

array (readOnly)

Description

The roles that the user has been added to through roles\_claim.

#### `name`

Type

string

Description

The name of the user.

User names can only have alphanumeric ASCII characters and underscores.

#### `password`

Type

string

Description

The password of the user.

Mandatory. unless `allow_empty_password` is `true` in the database configs.

#### `roles`

Type

array (readOnly)

Description

All the roles that the user has been granted access to.

Access could have been granted through the sync function, roles\_claim, or explicitly on the user under the `admin_roles` property.

## [](#HTTP%5FError)Errors

This section shows possible error responses returned by the Admin REST API.

| Property              |                        | Schema |
| --------------------- | ---------------------- | ------ |
| **error** _required_  | The error name.        | String |
| **reason** _required_ | The error description. | String |

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