---
title: Access Control How-To
description: How to implement Sync Gateway access controls using Configuration
  File, Admin REST API and-or the Sync Function to manage documents, users,
  roles and channels
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/access-control/pages/access-control-how.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/sync-gateway/current/access-control/access-control-how.html)

# Access Control How-To

> How to implement Sync Gateway access controls using Configuration File, Admin REST API and-or the Sync Function to manage documents, users, roles and channels  
> The sync function API provides several methods that you can use to validate and control user access to databases and documents.

_Related Topics_: [Concepts](access-control-concepts.md) | [How-to](access-control-how.md) | [Sync Function](sync-function/sync-function.md) | [Use XATTRs for Access Grants](access-control-how-use-xattrs-for-access-grants.md)

## [](#introduction)Introduction

This topic will show how to use the various [Access Control Concepts](access-control-concepts.md) to provide effective and secure document distribution and control.

## [](#mechanism)Mechanism

There are a number of ways in which you can control document distribution and user access, both statically a dynamically; these are itemized in [Ways to configure access](#lst1) and illustrated in [Example 1](#img-channel-access).

Ways to configure access

* Legacy Pre 3.0: Use the [Legacy Configuration Properties](../configuration/configuration-properties-legacy.md) file’s [admin\_user\_channels](../configuration/configuration-properties-legacy.md#databases-user-admin-channels)
* Dynamically

  * At the time of user creation with Admin REST Endpoint [{db}/\_user/{name}](../rest-api/rest-api-admin.md#tag/Database-Security/operation/put%5Fdb-%5Fuser-name) using `admin_channel`
  * Using the Sync Function’s [access()](sync-function/sync-function-api-access-cmd.md).

Example 1\. Control Points

![channel access grant all](../_images/channel-access-grant-all.png) 

| **1** | Documents are assigned to channel using the Sync Function’s [channel()](sync-function/sync-function-api-channel-cmd.md) API. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------- |
| **2** | User and-or roles are granted access to channels by one of the means defined in [Ways to configure access](#lst1)            |

## [](#lbl-acc-ctl-users)Create Users

### [](#process)Process

A user must be created on Sync Gateway before it can be granted access to documents.

You create and-or manage users using the following options — as shown in [Example 2](#ex-create-users):

* Admin REST API  
Users are created via the Sync Gateway [Admin REST API](../rest-api/rest-api-admin.md).
* OIDC  
Configure _OIDC_ authentication to auto-register a user following successful validation of an ID Token — [User Authentication](../security/authentication-users.md).
* Static Configuration (Pre 3.0):  
Users can be statically configured within the Sync Gateway Configuration File — see: [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md).  
**Note**, to use this option in version 3.x users must run Sync Gateway with the `disable_persistent_config` flag set to `true`.

Example 2\. How to Create Users

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

## [](#lbl-acc-ctl-roles-create)Create Roles

_Related Concepts_: [Roles](roles.md)

### [](#provisioning)Provisioning

The creation of roles is optional. It depends on the use case whether there is a need to logically group users.

You can create and-or manage roles using the following options

* Admin REST API:  
Roles are created via the Sync Gateway Admin REST API — see: [Admin REST API](../rest-api/rest-api-admin.md).
* File-based Configuration Properties \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

**Note** To use this option in v3.x, you must use the `-disable_persistent_config` CLI option.  
Configure roles in the [Legacy Configuration Properties](../configuration/configuration-properties-legacy.md) file.

**Note** that removing a role effectively revokes access to the channel that role is associated with and may mean users will lose access to required documents.

Example 3\. How to Create a Role

* Admin REST API
* File-based Configuration Properties

> [!NOTE]
> This is the default recommended option starting 3.0..

Create a new role using the [/{db}/\_role/](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Security/operation/post%5Fdb-%5Frole-) endpoint.

```bash
$ curl -vX POST "http://localhost:4985/mydatabase/_roles/" -H
"accept: application/json" -H "Content-Type: application/json" -d
'{"name": "Edge1", "collection_acces": {"scopename": {"collectionname": {"admin_channels": ["channel1", "channel3"]]}}}}' (1)
```

| **1** | Here we add the Edge1 role which grants channel access to channel1 and channel3 in scope scopename and collection collectionname. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------- |

Create roles by hardcoding them in the [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md). This method is convenient for testing and to get started. It is recommended to use the **REST API** for production systems.

```json
{
  "databases": {
    "mydatabase": {
      "roles": { (1)
        "Edge1": {
          "collection_access": {
            "scopename": {
              "collectionname": {
                "admin_channels": ["channel1", "channel3"] (2)
              }
            }
          }
	},
        "Edge2": {"admin_channels": ["channel2", "channel3"]},
        "GUEST": {"disabled": true}
      }
    }
  }
}
```

| **1** | [databases.$db.users](../configuration/configuration-schema-database.md#database-users) |
| ----- | --------------------------------------------------------------------------------------- |
| **2** | Here we add the Edge1 role.                                                             |

## [](#lbl-acc-ctl-roles-add)Assign Users to Roles

### [](#process-2)Process

You can assign (or remove) users to (or from) roles using any of the following mechanisms:

* Admin REST API  
Assign a user to a role via the [Admin REST API](../rest-api/rest-api-admin.md)
* Configuration Properties file (Pre v3.x+)  
Roles can be configured within using the DB section — see: [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md).  
> [!IMPORTANT]  
> Persistent Configuration is enabled by default from 3.0.  
>  
> To continue using legacy Pre-3.0 configuration you should start _Sync Gateway_ with [disable\_persistent\_config](../configuration/configuration-properties-legacy.md#disable%5Fpersistent%5Fconfig) set `true` either in the configuration file or in [Command Line Options](../deploy/command-line-options.md).
* Sync Function  
Programmatically assign users to roles.

Removing a role effectively revokes access to the channel that role is associated with. This may mean users will lose access to required documents.

Example 4\. Assign user to role

Admin REST API

> [!NOTE]
> The recommended method from 3.0

Assign a user to a role by sending a PUT request to the Admin REST API `_user` endpoint ([/{db}/\_user/{name}](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Security/operation/put%5Fdb-%5Fuser-name) ).

Specify the roles to be assigned in the `admin_roles` array.

```bash
$ curl -vX PUT "http://localhost:4985/mydatabase/_user/{user}" -H (1)
"accept: application/json" -H "Content-Type: application/json" -d
'{ "admin_roles": ["Edge1"]}' (2)
```

| **1** | {user} is the user name to be updated, e.g. "Edge1User"             |
| ----- | ------------------------------------------------------------------- |
| **2** | Include the role that the user is to be assigned to in admin\_roles |

See also: [/{db}/\_role/{name}](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Security/operation/put%5Fdb-%5Frole-name)

Sync Function

You can also use the Sync Function’s [role()](sync-function/sync-function-api-role-cmd.md) function to assign users to roles programmatically.

In this use case, where role assignment is done dynamically via the sync function, the role(s) to which user is assigned can be identified in two ways:

* By document content — the role can be derived or specified as a property within the document body.
* By user defined XATTR (3.0+) — the role can be specified within a special user-defined XATTR associated with the document — see: [Use XATTRs for Access Grants](access-control-how-use-xattrs-for-access-grants.md)

Note that both role and user must already exist. Nonexistent roles don’t cause an error, but have no effect on the user’s access privileges.

```javascript
role ("Edge1User", "role:Edge1");
role ("Edge2User", "role:Edge2":);
```

File-based Configuration Properties

Persistent Configuration is enabled by default from 3.0.

To continue using legacy Pre-3.0 configuration you should start _Sync Gateway_ with [disable\_persistent\_config](../configuration/configuration-properties-legacy.md#disable%5Fpersistent%5Fconfig) set `true` either in the configuration file or in [Command Line Options](../deploy/command-line-options.md).

Add the role the user is to be assigned to in the configuration file. This method is convenient for testing and to get started. Use the **Admin REST API** for production systems.

```json
{
  "databases": {
    "mydatabase": {
      "users": { (1)
        "GUEST": {"disabled": true},
        "Edge1User": {"password": "pass", "admin_roles": ["Edge1"], (2)
                      "admin_channels": ["RandomChannel"]},
        "Edge2User": {"password": "pass", "admin_roles": ["Edge2"]}
      }
    }
  }
}
```

| **1** | Within users find the user you want to assign to a role                                                                                                                                                             |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Add the role the user is to be assigned to in admin\_roles — see: [databases.$db.users.$user.admin\_roles](../configuration/configuration-properties-legacy.md#databases-this%5Fdb-users-this%5Fuser-admin%5Froles) |

## [](#lbl-control-document-access)Control Document Access

_Related Concepts_: [Access control Model](access-control-model.md) | [Channels](channels.md) | [Users](users.md) | [Roles](roles.md)

### [](#lbl-read-access)Read Access Control

Channels form the core of the Sync Gateway Access Control model.

Every document in the database is assigned a list of channels it is distributed to. Every user (or role) is granted access to a list of channels — as shown in [Example 5](#ex-read-access).

Channels can be user-defined or they can be system channels (like the public, all-docs, wildcard)

This dual-purpose is reflected in the way you use channels:

* By granting a user (or role) access to a channel, you are imposing access control. Users can only access documents that are channels that they have been granted access to.
* By assigning a document to a channel you are imposing document routing and data segregation

You grant roles and-or users access to channels using:

* Admin REST API  
Using `admin_channels` property inside the `collection_access` property using the admin REST API endpoint — see [/{db}/\_user/{name}](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Security/operation/put%5Fdb-%5Fuser-name)
* Dynamically via Sync Function  
Programmatically within the sync function using the exposed helper function access() — see [Sync Function API](sync-function/sync-function-api.md)
* Configuration File (pre 3.0)  
Using the appropriate `admin_channels` property in the [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md).  
**Note:** This option is disabled by default in 3.0; to use it, set the `disable_persistent_config` CLI or configuration file property flag to `true` and provide a full configuration

Example 5\. Allow Access

* Admin REST API
* Sync Function
* File-base Configuration Properties

Add a channel to an existing user by sending a PUT request to the Admin REST API `_role` endpoint ([/{db}/\_role/{name}](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Security/operation/put%5Fdb-%5Frole-name) ).

Specify the roles to be assigned in the `admin_channels` array.

```bash
$ curl -vX PUT "http://localhost:4985/mydatabase/_user/{user}" -H (1)
"accept: application/json" -H "Content-Type: application/json" -d
'{"collection_access": {"scopename": { "collectionname": {"admin_channels": ["Channel1","Channel3"]}}}}' (2)
```

| **1** | {user} is the user name to be updated, e.g. "Edge1User"                                                 |
| ----- | ------------------------------------------------------------------------------------------------------- |
| **2** | Here we add _Channel1_ and _Channel3_ to the user inside scope scopename and collection collectionname. |

You can also use the Sync Function’s [access()](sync-function/sync-function-api-access-cmd.md) function to allow channel access to roles and-or users programmatically.

In the case where channel assignment is done dynamically via the sync function, the channel(s) to which user/role is assigned is identified in two ways:

* The user/role can be derived or specified as a property within the document body. In this case, the document content itself is used to govern access and routing
* From 3.0, the role can be specified within a special user-defined XATTR associated with the document — see: [Use XATTRs for Access Grants](access-control-how-use-xattrs-for-access-grants.md).

* Version 3.x
* All Versions

Here we are using a specific XATTR to determine which users need access to the document’s contents — for more on how to configure ths see [Use XATTRs for Access Grants](access-control-how-use-xattrs-for-access-grants.md).

```javascript
function (doc, oldDoc, meta) { (1)

  if (meta.xattrs.channelXattr === undefined) (2)
    {
      console.log("no user_xattr_key defined")
      channel(null)
    } else {
      channel(meta.xattrs.channelXattr) (3)


    }

  // Further processing as required ../
```

| **1** | The meta parameter exposes the user defined user\_xattr\_key if defined. The item takes the name configured for the database |
| ----- | ---------------------------------------------------------------------------------------------------------------------------- |
| **2** | Access the meta parameter object to check an xattr exists on this document                                                   |
| **3** | Use the content of the xattr to define the channels setting for this document                                                |

Here we are using the document content (`type`) to determine which users need access to the document’s contents.

```javascript
function (doc, olddoc) {

  // user logic

  if (doc.type=="type1") {
    access("Edge1User", "channel1") (1)
  } else if (doc.type="type2") {
    access("role:Edge2", "channel2") (2)
  } else {
    access("Edge1User", "Edge2User", "channel3")
  }

  // user logic
}
```

| **1** | Here we add access to channel _channel1_ to the user _Edge1User_                                                                                                                                                                                       |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | The access() function can also operate on roles. If a user name string begins with role: then the remainder of the string is interpreted as a role name. **NOTE** There’s no ambiguity here, because : is an illegal character in a user or role name. |
| **3** | Here we allow access to the channel _channel2_ for the role _Edge2_                                                                                                                                                                                    |

Add a channel to a user in the configuration file. This method is convenient for testing and to get started. Use the **Admin REST API** for production systems.

```json
{
  "databases": {
    "mydatabase": {
      "users": {
        "GUEST": {"disabled": true},
        "Edge1User": {
          "password": "pass",
          "admin_roles": ["Edge1"],
          "collection_access": {
            "scopename": {
              "collectionname": {
                "admin_channels": ["Channel1","Channel3","RandomChannel"] (1)
              }
            }
          }
        }
      },
      "roles": {
        "Edge1": {
          "collection_access": {
	    "scopename": {
	      "collectionname": {
		"admin_channels": ["channel1","channel3"]
	      }
	    }
	  }
	},
	"Edge2": {
          "collection_access": {
	    "scopename": {
	      "collectionname": {
                "admin_channels": ["channel2","channel3","SkyChannel"]} (2)
	      }
	    }
	  }
	},
      }
    }
  }
}
```

| **1** | Here we have added the channels _channel1_ and \`_channel3_ to the user _Edge1User_ [databases.$db.users.$user.collection\_access.$scopename.$collectionname.admin\_channels](../configuration/configuration-schema-database.md#database-users-this%5Fuser-admin%5Fchannels)           |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Here we have added the channels _channel2_, _channel3_ and _SkyChannel_ to the role _Edge2_ [databases.$db.users.$user.$collection\_access.$scopename.$collectionname.$admin\_channels](../configuration/configuration-schema-database.md#database-roles-this%5Frole-admin%5Fchannels) |

### [](#lbl-write-access)Write Access Control

Channels enforce read access control to the documents. Any user who has access to a document can update the document.

Write access can be enforced at a document property level by implementing suitable logic within the Sync Function, using its helper functions to control the users allowed to make document updates and deletions — as shown in [Example 6](#ex-check-write-access).

You can build user validation into your Sync Function. For example, you can require that the user making the change has a specific name, role or channel access — as shown in [Example 7](#ex-helper-functions). Do this using any combination of: [requireUser()](sync-function/sync-function-api-require-user-cmd.md), [requireRole()](sync-function/sync-function-api-require-role-cmd.md) or [requireAccess()](sync-function/sync-function-api-require-access-cmd.md).

Note that when sending a change to Sync Gateway through the Admin REST API, the Sync Function executes with admin privileges. Calls to `requireUser`, `requireAccess` and `requireRole` will be no-ops, and will always appear successful.

Example 6\. Check Write Access

This example shows Sync Function logic that allows only the document owner to make changes. It does so by requiring that the current user is the one recorded as an owner on the old document.

* Version 3.x
* All Versions

This example makes use of channel data stored in XATTRS, an option introduced in 3.0 — see [Use XATTRs for Access Grants](access-control-how-use-xattrs-for-access-grants.md) for more on this topic.

```javascript
function (doc, oldDoc, meta) { (1)
  if (oldDoc) {
    requireUser(oldDoc.owner); (2)
  }
  if (meta.xattr.channelxattr) {
    requireAccess(meta.xattr.channelxattr); (3)
  } else
    {
      throw("No channel access granted") (4)
    }
}
```

| **1** | Note the additional, optional, meta argument, which gives acsess to XATTR objects.                                                                  |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | If the user making the change is not an owner of the pre-change document, an exception is thrown and the update is rejected with an error.          |
| **3** | Here we check the designated XATTR for the document channel(s) and require the user making the change to have access to on or more of the channels. |
| **4** | If the XATTR is not set we throw an exception.                                                                                                      |

This example makes use of document contents to store channel data.

```javascript
function (doc, oldDoc) {
  if (oldDoc) {
    requireUser(oldDoc.owner); (1)
  }
  if (olddoc.channels) {
    requireAccess(olddoc.channels); (2)
  } else
    {
      throw("No channel access defined or granted") (3)
    }
}
```

| **1** | If the user making the change is not an owner of the pre-change document, an exception is thrown and the update is rejected with an error.                     |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Here we check the designated document content for the document channel(s) and require the user making the change to have access to on or more of the channels. |
| **3** | If the olddoc.channels value is not set we throw an exception.                                                                                                 |

Example 7\. Helper Function examples

Here we show various ways to use some of the Sync Function API’s helper functions:

```javascript
requireUser("snej") (1)

requireUser(["snej", "jchris", "tleyden"]) (2)

requireRole("admin") (3)

requireRole(["admin", "old-timer"]) (4)

requireAccess("events")  (5)

requireAccess(["events", "messages"]) (6)
```

| **1** | throw an error if username is not "snej"                               |
| ----- | ---------------------------------------------------------------------- |
| **2** | throw if username is not in the list                                   |
| **3** | throw an error unless the user has the "admin" role                    |
| **4** | throw an error unless the user has one of those roles                  |
| **5** | throw an error unless the user has access to read the "events" channel |
| **6** | throw an error unless the can read one of these channels               |

## [](#lbl-verify-access)Verify Access

Related Concepts

[Access control Model](access-control-model.md)

### [](#purpose)Purpose

Use the Admin REST API to see the:

* Channels a user has access to
* Channels a role has access to
* Channels a document is assigned to

### [](#context)Context

The `all_channels` property of a user account determines the channels a user can access. Its value is derived from the union of:

* The user’s `admin_channels` property, which is set using the Admin REST API.
* The channels the user has been granted access to by [access()](sync-function/sync-function-api-access-cmd.md) calls from sync functions invoked for current revisions of documents.
* The `all_channels` properties of any roles the user belongs to. These are themselves computed using the above rules.

### [](#process-3)Process

* Users
* Roles
* Document

Send a get request to the [/{db}/\_user/{name}](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Security/operation/get%5Fdb-%5Fuser-name) endpoint

```bash
curl http://localhost:4985/db/_user/pupshaw
```

The [output](#ex-output) shows that the user `pupshaw` has access to the following channels:

| **1** | all through its own admin\_channels setting for the default collection.                    |
| ----- | ------------------------------------------------------------------------------------------ |
| **2** | collectionAChannel through its own admin\_channels setting for the collection collectionA. |
| **3** | hoopy through the froods role’s admin\_channels setting in the default collection.         |

```json
{
    "admin_channels": [
        "all" (1)
    ],
    "collection_access": {
        "scopeA": {
	    "collectionA": {
		"admin_channels": [
		    "collectionAChannel" (2)
		],
		"all_channels": [
		    "collectionAChannel"
		]
	    }
	}
    },
    "admin_roles": [
        "froods"
    ],
    "all_channels": [
        "all",
        "hoopy" (3)
    ],
    "name": "pupshaw",
    "roles": [
        "froods"
    ]
}
```

Send a get request to the [/{db}/\_role/{name}](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Security/operation/get%5Fdb-%5Frole-name) endpoint

```bash
curl http://localhost:4985/db/_role/frood
```

The output shows that the role `froods` has access to the following channels:

| **1** | hoopy through its role’s admin\_channels setting for the default collection.           |
| ----- | -------------------------------------------------------------------------------------- |
| **2** | collectionA through its role’s admin\_channels setting for the collection collectionA. |

```json
{
    "name": "froods",
    "collection_access": {
        "scopeA": {
	    "collectionA": {
		"admin_channels": [
		    "collectionAChannel" (1)
		],
		"all_channels": [
		    "collectionAChannel"
		]
	    }
	}
    },
    "admin_channels": [
        "hoopy" (2)
    ],
    "admin_roles": [
        "froods"
    ],
    "all_channels": [
        "hoopy" (3)
    ]
}
```

Send a get request to the [/{keyspace}/\_alldocs](../rest-api/rest%5Fapi%5Fadmin.md#tag/Document/operation/get%5Fkeyspace-%5Fall%5Fdocs) endpoint

```bash
curl http://localhost:4985/ourdb/_all_docs?channels=true&keys=[ourdoc]" -H "accept: application/json"
```

| **1** | The [output](#ex-outdoc) shows that the document ourdoc is assigned to the channels: all and hoopyThat assignment to hoopy is what makes it available to our froods role and therefore to our user pupshaw. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

```json
{
  "id": "ourdoc",
  "key": "ourdoc",
  "value": {
      "channels": [ (1)
          "short",
          "hoopy"
      ],
      "rev": "1-86effb929acbf953905dd0e3974f6051"
  }
}
```

## [](#lbl-xattrs)Use Extended Attributes (XATTRS)

_Related Concepts_: [Access control Model](access-control-model.md) | [Control Document Access](access-control-how-control-document-access.md)

### [](#why-use-xattrs)Why use XATTRS

XATTRs can be used to hold data used for document routing and access control \[[2](#%5Ffootnotedef%5F2 "View footnote.")\]. When retrieved by the Sync Function, this data can be used to drive access grants. This approach has a few benefits:

* It provide an added level of security, users can no longer identify the channels and users a document is available to by reading its contents, because the information is in metadata that is inaccessible to them
* Separation of concerns. By separating access grant metadata from document contents, changes to access grants will not create a new document revision that is subsequently pushed to a client

Sync Gateway exposes a single user-definable XATTR for this purpose. Learn how to configure it in [Configuration](#lbl-config) and how to use it in [Setting](#lbl-set) and [Use XATTRs in a Sync Function](#lbl-using).

### [](#lbl-config)Configuration

Name the XATTR (see: [user\_xattr\_key](../configuration/configuration-schema-database.md#databases-this%5Fdb-user%5Fxattr%5Fkey)) to be used for channel routing by defining it using the Admin REST API’s [Database Configuration](../configuration/configuration-schema-database.md) — see: [Example 8](#ex-config).

The actual value of this XATTR can be anything that enables the Sync Function to make an appropriate access grant. Its data type can be string, array, object — any valid JSON that meets the required use case.

Example 8\. Define the User Extended Attribute Key

This example uses the Admin REST API to specify the required XATTR name as `channelXattr` on the database `hotels`.

* CURL
* HTTP

```json
curl -X POST 'http://localhost:4985/hotels/_config' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "user_xattr_key": "channelXattr" (1)
    }
}'
```

```http
POST /hotels/_config HTTP/1.1
Host: http://localhost:4985
Accept: application/json
Content-Type: application/json
Content-Length: 999

{
  “user_xattr_key”: “channelXattr” (1)
}
```

| **1** | Here _channelXattr_ is set as the name of the XATTR designated to hold channel routing information. |
| ----- | --------------------------------------------------------------------------------------------------- |

### [](#lbl-set)Setting

You can set and maintain the value of the XATTR using a Couchbase Server SDK API. You cannot set it using the Sync Gateway REST API.

For an example of setting the value of the XATTR using the C# SDK, see [Example 9](#ex-cbs-metadata-setting), this can be easily translated to any of the available SDK languages. See [Example 10](#ex-cbs-metadata) for an example of the metadata model.

Example 9\. Set XATTR using Couchbase Server SDK

```C#
using System;
using System.Threading.Tasks;
using Couchbase;
using Couchbase.KeyValue; (1)


namespace examples
{

    class Program
    {
        static async Task Main(string[] args)
        {
            // Set scope - cluster, bucket and collection
            var cluster =
                    await Cluster.ConnectAsync(
                                    "couchbase://localhost",
                                    "Administrator",
                                    "password");


            var bucket = await cluster.BucketAsync("travel-sample");
            var collection = bucket.DefaultCollection();

            // Set required  user_xattr_key name and value
            var our_user_xattr_key_name = "channelXattr"; (2)
            String[] channelXattrValue =
                {"channel1","channel3", "useradmin" }; (3)

            var ourDocumentType = "hotel";
            var documentKey = "";

            // Find our documents and get their ids
            var queryResult =
               await cluster.QueryAsync<dynamic>(
                   "select meta().id from `travel-sample`.`_default`.`_default` h where h.type = $1",
                        new Couchbase.Query.QueryOptions().Parameter(ourDocumentType)); (4)
            await foreach (var row in queryResult)
            {
                documentKey = row.id;
                Console.WriteLine("Working with document id: {0} ",
                                    documentKey);

                // Check if the document has an existing
                // user_xattr_key and update or insert new value
                var result =
                    await collection.LookupInAsync(
                            documentKey,
                            specs => specs.Exists(
                                path: our_user_xattr_key_name,
                                isXattr: true)
                            ); (5)

                if (result.Exists(0))
                {
                    // Update xattr for retrieved Id
                    await collection.MutateInAsync(
                            documentKey,
                            specs => specs.Upsert(
                                path: our_user_xattr_key_name, (6)
                                value: channelXattrValue, (7)
                                isXattr: true)); (8)

                    Console.Write("Updated Existing user_xattr_key: {0} to this value: {1}\n",
                        our_user_xattr_key_name,
                        string.Join(", ", channelXattrValue));

                }
                else
                {
                    // Insert xattr for retrieved id
                    await collection.MutateInAsync(
                            documentKey,
                            specs => specs.Insert(
                                path: our_user_xattr_key_name, (9)
                                value: channelXattrValue, (10)
                                isXattr: true)); (11)

                    Console.Write("Inserted New user_xattr_key: {0} with value {1}\n",
                        our_user_xattr_key_name,
                        string.Join(", ", channelXattrValue));

                }

            }
            Console.WriteLine("Completed Changes\n");
        }
    }
}
```

| **1**  | This is required to make the MutateInSpec class available, providing access to sub-documents, of which metadata is a special class |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| **2**  | This string’s value is what we want this document’s XATTR to be called                                                             |
| **3**  | This array contains the channels we want to include as the XATTR value                                                             |
| **4**  | Here we get all documents that we want to set the XATTR on (type = 'hotel' in this instance)                                       |
| **5**  | Check if the XATTR has been defined yet                                                                                            |
| **6**  | Update the XATTR — specify the item to update                                                                                      |
| **7**  | Update the XATTR — set the required value                                                                                          |
| **8**  | Update the XATTR — specify the item is an XATTR                                                                                    |
| **9**  | Insert the XATTR — specify the item to add (channelXattr)                                                                          |
| **10** | Insert the XATTR — set the required value using channelXattrValue                                                                  |
| **11** | Insert the XATTR — specify the item is an XATTR                                                                                    |

Running the code produces the following output:

```bash
Working with document id: 1000
Updated Existing user_xattr_key:
  channelXattr to this value: channel1, channel3, useradmin

Working with document id: 1001
Inserted New user_xattr_key:
  channelXattr with this value: channel1, channel3, useradmin

Completed Changes
```

Example 10\. Metadata on Couchbase Server document

```json
{
  "meta": { (1)
    "id": "1000",
    "rev": "7-1680c88cbce700000000000002000006",
    "expiration": 0,
    "flags": 33554438,
    "type": "json"
  },
  "xattrs": { (2)
    "channelXattr": [ (3)
      "channel1",
      "channel3",
      "useradmin"
    ]
  }
}
```

| **1** | This is the Fixed (or System) metadata                                                                                                                                                                                                |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | This is the User metadata, where you can define extended attributes                                                                                                                                                                   |
| **3** | Here _channelXattr_ is the name of the designated xattr holding the channel routing information to be passed to the Sync Function. You will set the value of the xattr using the SDK API when the document is created and-or updated. |

For more on Couchbase Server metadata and extended attributes — see Couchbase Server topics: [Metadata](../../../server/current/learn/data/data.md#metadata) | [Extended Attributes](../../../server/current/learn/data/extended-attributes-fundamentals.md)

### [](#lbl-using)Use XATTRs in a Sync Function

The designated XATTR is exposed to the [Sync Function](sync-function/sync-function.md) as an additional argument `meta.xattrs.<xattr name>`

Example 11\. Sync Function Arguments

```javascript
function (doc, oldDoc, meta) { (1)

  if (meta.xattrs.channelXattr === undefined) (2)
    {
      console.log("no user_xattr_key defined")
      channel(null)
    } else {
      channel(meta.xattrs.channelXattr) (3)


    }

  // Further processing as required ../
```

| **1** | The meta parameter exposes the user defined user\_xattr\_key if defined. The item takes the name configured for the database |
| ----- | ---------------------------------------------------------------------------------------------------------------------------- |
| **2** | Access the meta parameter object to check an xattr exists on this document                                                   |
| **3** | Use the content of the xattr to define the channels setting for this document                                                |

See: [Sync Function](sync-function/sync-function.md) topic for more information.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](sync-function/sync-function.md)
* [Import filter](../sync/import-processing.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Add/Update Sync Function](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-sync)
* [Sync Function Overview](sync-function/sync-function.md)

###### [](#-3)

Reference material …​

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)

---

[1](#%5Ffootnoteref%5F1). Prior to Release 3.0 

[2](#%5Ffootnoteref%5F2). From release 3.0