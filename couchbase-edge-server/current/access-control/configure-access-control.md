---
title: Configure Access Control
description: Configure fine-grained read and write permissions for downstream
  edge clients in Couchbase Edge Server at the database, scope, and collection
  level.
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.1/modules/access-control/pages/configure-access-control.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:couchbase-edge-server:access-control:configure-access-control.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-edge-server/current/access-control/configure-access-control.html)

# Configure Access Control

Configure fine-grained access control to define which collections each edge client user can read from or write to.

## [](#prerequisites)Prerequisites

* Couchbase Edge Server {version} or later.
* A users file configured for your deployment. See [Authentication](../configuration/authentication.md).
* Users must authenticate using Basic Auth or mTLS client certificates.

## [](#enable-access-control-on-a-database)Enable Access Control on a Database

Access control enforcement is opt-in and is configured at the server level. Set `enable_user_access_control` to `true` in the top-level server configuration.

```json
{
  "enable_user_access_control": true,
  "databases": {
    "mydb": { }
  }
}
```

When this property is not set or is set to `false`, all configured users have unrestricted read and write access to all collections in all databases.

## [](#define-user-access-permissions)Define User Access Permissions

Access permissions are defined in the users file using the `access` property. Each entry maps a keyspace pattern to an array of permitted operations.

```json
{
  "$schema": "…/users_schema.json",
  "appUser": {
    "access": {
      "travel.*": ["read"],
      "travel.inventory.hotels": ["write"],
      "travel.inventory.landmarks": ["read", "write"],
      "sales": ["read"]
    },
    "password": "<<bcrypt password>>"
  },
  "admin": {
    "roles": ["admin"],
    "password": "<<bcrypt password>>"
  }
}
```

In this example:

* `appUser` has read access to all collections in the `travel` database.
* `appUser` has write-only access to the `hotels` collection in the `travel.inventory` scope.
* `appUser` has read and write access to the `landmarks` collection in the `travel.inventory` scope.
* `appUser` has read access to the `_default._default` collection of the `sales` database.
* `admin` has unrestricted access to all databases as an admin role user.

> [!NOTE]
> The `password` field is optional when using mTLS certificate-based authentication. If provided, it is ignored for mTLS users.

## [](#keyspace-pattern-reference)Keyspace Pattern Reference

__Table 1\. Keyspace Pattern Syntax__
| Pattern                                              | Target                                                    |
| ---------------------------------------------------- | --------------------------------------------------------- |
| database.scope.collection                            | A specific collection within a specific scope.            |
| database.scope.\*                                    | All collections within a specific scope.                  |
| database.\*                                          | All collections within the database, including \_default. |
| database                                             | The \_default.\_default collection of the database.       |
| database.\_default.collection or database.collection | A named collection within the \_default scope.            |

## [](#next-steps)Next Steps

* To restrict which named queries a user can execute, see [configuration:configure-query-access.adoc](#configuration:configure-query-access.adoc).
* To review how Couchbase Edge Server enforces access control across REST operations, see [configuration:fine-grained-access-control.adoc](#configuration:fine-grained-access-control.adoc).