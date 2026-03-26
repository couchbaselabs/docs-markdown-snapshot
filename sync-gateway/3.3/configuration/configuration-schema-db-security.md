---
title: Database Security
description: Using Sync Gateway's Admin REST API to configure users and roles
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.3/modules/configuration/pages/configuration-schema-db-security.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.3@sync-gateway:configuration:configuration-schema-db-security.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.3/configuration/configuration-schema-db-security.html)

# Database Security

> Using Sync Gateway's Admin REST API to configure users and roles  

_Related topics_: [Overview](configuration-overview.md) | [Bootstrap](configuration-schema-bootstrap.md) | [Database](configuration-schema-database.md) | [Database Security](configuration-schema-db-security.md) | [Access Control](configuration-schema-access-control.md) | [Import](configuration-schema-import-filter.md) | [Inter-Sync Gateway Replication](configuration-schema-isgr.md)

> [!IMPORTANT]
> Pre-3.0 Legacy Configuration Equivalents
> 
> This content describes configuration for Sync Gateway 3.0 and higher — for legacy configuration, see: [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

## [](#introduction)Introduction

Use the Admin REST API `_user` and `_role` endpoints to provision and manage sync gateway users through persistent configuration changes.

This page introduces the [Create or Update a Role](#put%5Fdb-%5Frole-name) and [Create or Update a User](#put%5Fdb-%5Fuser-name) endpoints for convenience — see [Database Security](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Security) for a full description of the endpoints available.

It also includes a JSON-data model, you can use to build your request bodies. See: [Schema](#lbl-schema)

## [](#put%5Fdb-%5Frole-name)Upsert a role

PUT /{db}/_role/{name}

### [](#put%5Fdb-%5Frole-name-description)Description

If the role does not exist, create a new role otherwise update the existing role.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

Consumes

* application/json

Produces

* application/json

### [](#put%5Fdb-%5Frole-name-parameters)Parameters

#### [](#put%5Fdb-%5Frole-name-path)Path Parameters

| Name                | Description                                            | Schema |
| ------------------- | ------------------------------------------------------ | ------ |
| **db** _required_   | The name of the database to run the operation against. | String |
| **name** _required_ | The name of the role.                                  | String |

#### [](#put%5Fdb-%5Frole-name-body)Body Parameter

| Name                | Description                       | Schema         |
| ------------------- | --------------------------------- | -------------- |
| **Body** _optional_ | Properties associated with a role | [Role](#Role2) |

### [](#put%5Fdb-%5Frole-name-responses)Responses

| HTTP Code | Description                 | Schema                  |
| --------- | --------------------------- | ----------------------- |
| 200       | OK                          |                         |
| 201       | Created                     |                         |
| 404       | Resource could not be found | [Errors](#HTTP%5FError) |

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

| **1** | Add role newrole to the travel25 database               |
| ----- | ------------------------------------------------------- |
| **2** | Use Basic Auth to authenticate to an existing RBAC user |

## [](#put%5Fdb-%5Fuser-name)Upsert a user

PUT /{db}/_user/{name}

### [](#put%5Fdb-%5Fuser-name-description)Description

If the user does not exist, create a new user otherwise update the existing user.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

Consumes

* application/json

Produces

* application/json

### [](#put%5Fdb-%5Fuser-name-parameters)Parameters

#### [](#put%5Fdb-%5Fuser-name-path)Path Parameters

| Name                | Description                                            | Schema |
| ------------------- | ------------------------------------------------------ | ------ |
| **db** _required_   | The name of the database to run the operation against. | String |
| **name** _required_ | The name of the user.                                  | String |

#### [](#put%5Fdb-%5Fuser-name-body)Body Parameter

| Name                | Description                       | Schema         |
| ------------------- | --------------------------------- | -------------- |
| **Body** _optional_ | Properties associated with a user | [User](#User2) |

### [](#put%5Fdb-%5Fuser-name-responses)Responses

| HTTP Code | Description                         | Schema                  |
| --------- | ----------------------------------- | ----------------------- |
| 200       | Existing user modified successfully |                         |
| 201       | New user created                    |                         |
| 404       | Resource could not be found         | [Errors](#HTTP%5FError) |

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

This section shows Sync Gateway's database security configuration settings in schema format for convenience in constructing JSON models for use in the Admin REST API.

The configuration settings described here are provisioned through the Admin REST API — see as shown in [Database Security](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Security).

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

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](configuration-schema-bootstrap.md)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)