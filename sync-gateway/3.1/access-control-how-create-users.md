---
title: How to Create a User
description: How to create a Sync Gateway user for secure access control in
  cloud-to-edge enterprise data synchronization.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.1/modules/ROOT/pages/access-control-how-create-users.adoc
  xref: xref:3.1@sync-gateway::access-control-how-create-users.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.1/access-control-how-create-users.html)

# How to Create a User

> How to create a Sync Gateway user for secure access control in cloud-to-edge enterprise data synchronization.  
> Sync Gateway _users_ are a key part of a flexible approach to data routing and access control.

_Related topics_: [Create Role](access-control-how-create-roles.md) | Create User | [Add Role to User](access-control-how-assign-users-to-roles.md) | [Allow Access](access-control-how-control-document-access.md) | [Verify Access](access-control-how-verify-access.md) | [Write Access](#access-control-how-write-access.adoc)

## [](#process)Process

A user must be created on Sync Gateway before it can be granted access to documents.

You create and-or manage users using the following options — as shown in [Example 1](#ex-create-users):

* Admin REST API  
Users are created via the Sync Gateway [Admin REST API](rest-api-admin.md).
* OIDC  
Configure _OIDC_ authentication to auto-register a user following successful validation of an ID Token — [User Authentication](authentication-users.md).
* Static Configuration (Pre 3.0):  
Users can be statically configured within the Sync Gateway Configuration File — see: [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md).  
**Note**, to use this option in version 3.x users must run Sync Gateway with the `disable_persistent_config` flag set to `true`.

Example 1\. How to Create Users

Admin REST API

> [!NOTE]
> This is the default recommended option starting 3.0\.

Create a new user by sending a POST request to the Admin Rest Api `_user` endpoint ([{db}/\_user/{name}](rest-api-admin.md#/user/put%5F%5Fdb%5F%5F%5Fuser%5F%5Fname%5F)). Update existing users by sending a PUT instead; in this case include the user name at the end of the url.

The user credentials (**username**/**password**) are passed in the request body.

```bash
$ curl -vX POST "http://localhost:4985/mydatabase/_user/" -H
"accept: application/json" -H "Content-Type: application/json" -d
'{"name": "Edge1User", "password": "pass"}' (1)

$ curl -vX PUT "http://localhost:4985/mydatabase/_user/Edge1User" -H
"accept: application/json" -H "Content-Type: application/json" -d
'{"name": "Edge1User", "admin_channels": ["RandomChannel"]}' (2)
```

| **1** | Add new user "Edge1User", no admin\_channels or role is specified here. |
| ----- | ----------------------------------------------------------------------- |
| **2** | Update existing user "Edge1User" and add admin\_channels data           |

OIDC

```bash
curl --location --request PUT 'http://localhost:4985/ourdb/_config' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
  oidc: {
    providers: {
      google_implicit: {
        issuer:https://accounts.google.com,
        client_id:yourclientid-uso.apps.googleusercontent.com,
        register:true (1)
      },
    },
  }
}'
```

| **1** | Use register=true to automatically create a Sync Gateway user on successful completion of validation. |
| ----- | ----------------------------------------------------------------------------------------------------- |

File-based Configuration Properties File

Persistent Configuration is enabled by default from 3.0.

To continue using legacy Pre-3.0 configuration you should start _Sync Gateway_ with [disable-persistent-config](configuration-properties-legacy.md#disable%5Fpersistent%5Fconfig) set `true` either in the configuration file or in [Command Line Options](command-line-options.md).

Create users by hardcoding their credentials in the Configuration Properties file. This method is convenient for testing and to get started.  
Use the Admin REST API for production system changes.

```json
{
  "databases": {
    "mydatabase": {
      "users": { (1)
        "GUEST": {"disabled": true},
        "Edge1User": {"password": "pass", (2)
                      "admin_channels": ["RandomChannel"]},
      }
    }
  }
}
```

| **1** | [databases.$db.users](configuration-schema-database.md#database-users) |
| ----- | ---------------------------------------------------------------------- |
| **2** | Here we add the Edge1 user                                             |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](#sync-function-overview.adoc)
* [Import filter](import-processing.md)
* [Access Control](configuration-schema-access-control.md)
* [Add/Update Sync Function](#rest-api-admin.html#/Access%5FControl/update%5Fsync%5Ffunction)
* [Sync Function Overview](#sync-function-overview.adoc)

###### [](#-3)

Reference material …​

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)