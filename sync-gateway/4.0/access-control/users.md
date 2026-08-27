---
title: Users
description: About Sync Gateway <em>users</em> and their role in secure
  cloud-to-edge enterprise data synchronization.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/access-control/pages/users.adoc
  xref: xref:4.0@sync-gateway:access-control:users.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/4.0/access-control/users.html)

# Users

> About Sync Gateway _users_ and their role in secure cloud-to-edge enterprise data synchronization.  
> Here we introduce the concept of _users_ and their role in assuring secure access control within _Sync Gateway_.

_Related Concepts_: [Access Control Model](access-control-model.md) | [Channels](channels.md) | [Roles](roles.md) | [Sync Function](sync-function/sync-function.md) | [Users](users.md)

## [](#concept)Concept

Users are one of the cornerstone concepts of access control. You can restrict document access to specific users and-or to users with specific roles.

As an entity a _user_ comprises a name, password, list of [Roles](roles.md) and a list of [Channels](channels.md).

## [](#lbl-sgw-users)Sync Gateway Users

Sync Gateway users and roles have no relationship to [Couchbase Server's _RBAC (Role-based Access Control) users_](#lbl-rbac-users). They are created and operate solely within the _Sync Gateway_ ecosphere to govern access to replication data and to the Public API.

Granting access to a channel in Couchbase Sync Gateway allows users to access all documents assigned to that channel, which are part of specific collections. If granting users access to admin channels statically, it is necessary to specify both the corresponding collection and channel.

Users can also be assigned to zero or more [Roles](roles.md). A user inherits the channel access of all roles it belongs to. This is very much like Unix groups, except that roles do not form a hierarchy.

Sync Gateway user credentials can be used to authenticate access to the Public API; RBAC users are required for access to other API.

## [](#lbl-rbac-users)RBAC Users

Couchbase Server _RBAC user_ credentials are required to authenticate and authorize access to the Admin and Metrics API. You will need to create these users on Couchbase server in order to enable access — see: [Create RBAC users](../start-here/get-started-prepare.md#step-2create-rbac-user) for how to and [Security Authorization Overview](../../../server/current/learn/security/authorization-overview.md) for more on RBAC user authentication.

## [](#process)Process

A user must be created on Sync Gateway before it can be granted access to documents.

You create and-or manage users using the following options — as shown in [Example 1](#ex-create-users):

* Admin REST API  
Users are created via the Sync Gateway [Admin REST API](../rest-api/rest-api-admin.md).
* OIDC  
Configure _OIDC_ authentication to auto-register a user following successful validation of an ID Token — [User Authentication](../security/authentication-users.md).
* Static Configuration (Pre 3.0):  
Users can be statically configured within the Sync Gateway Configuration File — see: [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md).  
**Note**, to use this option in version 3.x users must run Sync Gateway with the `disable_persistent_config` flag set to `true`.

Example 1\. How to Create Users

Admin REST API

> [!NOTE]
> This is the default recommended option starting 3.0\.

Create a new user by sending a POST request to the Admin Rest Api `_user` endpoint ([{db}/\_user/{name}](../rest-api/rest-api-admin.md#tag/Database-Security/operation/put%5Fdb-%5Fuser-name)). Update existing users by sending a PUT instead; in this case include the user name at the end of the url.

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

To continue using legacy Pre-3.0 configuration you should start _Sync Gateway_ with [disable\_persistent\_config](../configuration/configuration-properties-legacy.md#disable%5Fpersistent%5Fconfig) set `true` either in the configuration file or in [Command Line Options](../deploy/command-line-options.md).

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

| **1** | [databases.$db.users](../configuration/configuration-schema-database.md#database-users) |
| ----- | --------------------------------------------------------------------------------------- |
| **2** | Here we add the Edge1 user                                                              |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](sync-function/sync-function.md)
* [Import filter](../sync/import-processing.md)

###### [](#-3)

Reference material …​

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)