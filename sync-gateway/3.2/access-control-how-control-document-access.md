---
title: Control Document Access
description: How to control read/write/delete access using Sync Gateway's Sync
  Function API to ensure secure access to data in cloud-to-edge enterprise data
  synchronization.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.2/modules/ROOT/pages/access-control-how-control-document-access.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/sync-gateway/3.2/access-control-how-control-document-access.html)

# Control Document Access

> How to control read/write/delete access using Sync Gateway’s Sync Function API to ensure secure access to data in cloud-to-edge enterprise data synchronization.  

_Related topics_: [Create Role](access-control-how-create-roles.md) | [Create User](access-control-how-create-users.md) | [Add Role to User](access-control-how-assign-users-to-roles.md) | Allow Access | [Verify Access](access-control-how-verify-access.md) | [Write Access](#access-control-how-write-access.adoc)

_Related Concepts_: [Access control Model](access-control-model.md) | [Channels](channels.md) | [Users](users.md) | [Roles](roles.md)

## [](#lbl-read-access)Read Access Control

Channels form the core of the Sync Gateway Access Control model.

Every document in the database is assigned a list of channels it is distributed to. Every user (or role) is granted access to a list of channels — as shown in [Example 1](#ex-read-access).

Channels can be user-defined or they can be system channels (like the public, all-docs, wildcard)

This dual-purpose is reflected in the way you use channels:

* By granting a user (or role) access to a channel, you are imposing access control. Users can only access documents that are channels that they have been granted access to.
* By assigning a document to a channel you are imposing document routing and data segregation

You grant roles and-or users access to channels using:

* Admin REST API  
Using `admin_channels` property inside the `collection_access` property using the admin REST API endpoint — see [/{db}/\_user/{name}](rest%5Fapi%5Fadmin.md#tag/Database-Security/operation/put%5Fdb-%5Fuser-name)
* Dynamically via Sync Function  
Programmatically within the sync function using the exposed helper function access() — see [Sync Function API](sync-function-api.md)
* Configuration File (pre 3.0)  
Using the appropriate `admin_channels` property in the [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md).  
**Note:** This option is disabled by default in 3.0; to use it, set the `disable_persistent_config` CLI or configuration file property flag to `true` and provide a full configuration

Example 1\. Allow Access

* Admin REST API
* Sync Function
* File-base Configuration Properties

Add a channel to an existing user by sending a PUT request to the Admin REST API `_role` endpoint ([/{db}/\_role/{name}](rest%5Fapi%5Fadmin.md#tag/Database-Security/operation/put%5Fdb-%5Frole-name) ).

Specify the roles to be assigned in the `admin_channels` array.

```bash
$ curl -vX PUT "http://localhost:4985/mydatabase/_user/{user}" -H (1)
"accept: application/json" -H "Content-Type: application/json" -d
'{"collection_access": {"scopename": { "collectionname": {"admin_channels": ["Channel1","Channel3"]}}}}' (2)
```

| **1** | {user} is the user name to be updated, e.g. "Edge1User"                                                 |
| ----- | ------------------------------------------------------------------------------------------------------- |
| **2** | Here we add _Channel1_ and _Channel3_ to the user inside scope scopename and collection collectionname. |

You can also use the Sync Function’s [access()](sync-function-api-access-cmd.md) function to allow channel access to roles and-or users programmatically.

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

| **1** | Here we have added the channels _channel1_ and \`_channel3_ to the user _Edge1User_ [databases.$db.users.$user.collection\_access.$scopename.$collectionname.admin\_channels](configuration-schema-database.md#database-users-this%5Fuser-admin%5Fchannels)           |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Here we have added the channels _channel2_, _channel3_ and _SkyChannel_ to the role _Edge2_ [databases.$db.users.$user.$collection\_access.$scopename.$collectionname.$admin\_channels](configuration-schema-database.md#database-roles-this%5Frole-admin%5Fchannels) |

## [](#lbl-write-access)Write Access Control

Channels enforce read access control to the documents. Any user who has access to a document can update the document.

Write access can be enforced at a document property level by implementing suitable logic within the Sync Function, using its helper functions to control the users allowed to make document updates and deletions — as shown in [Example 2](#ex-check-write-access).

You can build user validation into your Sync Function. For example, you can require that the user making the change has a specific name, role or channel access — as shown in [Example 3](#ex-helper-functions). Do this using any combination of: [requireUser()](sync-function-api-require-user-cmd.md), [requireRole()](sync-function-api-require-role-cmd.md) or [requireAccess()](sync-function-api-require-access-cmd.md).

Note that when sending a change to Sync Gateway through the Admin REST API, the Sync Function executes with admin privileges. Calls to `requireUser`, `requireAccess` and `requireRole` will be no-ops, and will always appear successful.

Example 2\. Check Write Access

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

Example 3\. Helper Function examples

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

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](#sync-function-overview.adoc)
* [Import filter](import-processing.md)
* [Access Control](configuration-schema-access-control.md)
* [Add/Update Sync Function](rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-sync)
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