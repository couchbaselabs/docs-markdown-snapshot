---
title: How to Assign Users to Roles
description: How to assign a Sync Gateway <em>User</em> one or more roles for
  secure access control in cloud-to-edge enterprise data synchronization.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.1/modules/ROOT/pages/access-control-how-assign-users-to-roles.adoc
  xref: xref:3.1@sync-gateway::access-control-how-assign-users-to-roles.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.1/access-control-how-assign-users-to-roles.html)

# How to Assign Users to Roles

> How to assign a Sync Gateway _User_ one or more roles for secure access control in cloud-to-edge enterprise data synchronization.  
> Sync Gateway _Users_ and _Roles_ are a key part of a flexible approach to data routing and access control.

_Related topics_: [Create Role](access-control-how-create-roles.md) | [Create User](access-control-how-create-users.md) | Add Role to User | [Allow Access](access-control-how-control-document-access.md) | [Verify Access](access-control-how-verify-access.md) | [Write Access](#access-control-how-write-access.adoc)

## [](#process)Process

You can assign (or remove) users to (or from) roles using any of the following mechanisms:

* Admin REST API  
Assign a user to a role via the [Admin REST API](rest-api-admin.md)
* Configuration Properties file (Pre v3.x+)  
Roles can be configured within using the DB section — see: [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md).  
> [!IMPORTANT]  
> Persistent Configuration is enabled by default from 3.0.  
>  
> To continue using legacy Pre-3.0 configuration you should start _Sync Gateway_ with [disable-persistent-config](configuration-properties-legacy.md#disable%5Fpersistent%5Fconfig) set `true` either in the configuration file or in [Command Line Options](command-line-options.md).
* Sync Function  
Programmatically assign users to roles.

Removing a role effectively revokes access to the channel that role is associated with. This may mean users will lose access to required documents.

Example 1\. Assign user to role

Admin REST API

> [!NOTE]
> The recommended method from 3.0

Assign a user to a role by sending a PUT request to the Admin REST API `_user` endpoint ([/{db}/\_user/{name}](rest-api-admin.md#/user/post\%5F%5Fdb%5F%5F%5Fuser%5Fname%5F) ).

Specify the roles to be assigned in the `admin_roles` array.

```bash
$ curl -vX PUT "http://localhost:4985/mydatabase/_user/{user}" -H (1)
"accept: application/json" -H "Content-Type: application/json" -d
'{ "admin_roles": ["Edge1"]}' (2)
```

| **1** | {user} is the user name to be updated, e.g. "Edge1User"             |
| ----- | ------------------------------------------------------------------- |
| **2** | Include the role that the user is to be assigned to in admin\_roles |

See also: [/{db}/\_role/{name}](rest-api-admin.md#/role/put%5F%5Fdb%5F%5F%5Frole%5F%5Fname%5F)

Sync Function

You can also use the Sync Function's [role()](sync-function-api-role-cmd.md) function to assign users to roles programmatically.

In this use case, where role assignment is done dynamically via the sync function, the role(s) to which user is assigned can be identified in two ways:

* By document content — the role can be derived or specified as a property within the document body.
* By user defined XATTR (3.0+) — the role can be specified within a special user-defined XATTR associated with the document — see: [Use XATTRs for Access Grants](access-control-how-use-xattrs-for-access-grants.md)

Note that both role and user must already exist. Nonexistent roles don't cause an error, but have no effect on the user's access privileges.

```javascript
role ("Edge1User", "role:Edge1");
role ("Edge2User", "role:Edge2":);
```

File-based Configuration Properties

Persistent Configuration is enabled by default from 3.0.

To continue using legacy Pre-3.0 configuration you should start _Sync Gateway_ with [disable-persistent-config](configuration-properties-legacy.md#disable%5Fpersistent%5Fconfig) set `true` either in the configuration file or in [Command Line Options](command-line-options.md).

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

| **1** | Within users find the user you want to assign to a role                                                                                                                                            |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Add the role the user is to be assigned to in admin\_roles — see: [databases.$db.users.$user.admin\_roles](configuration-properties-legacy.md#databases-this%5Fdb-users-this%5Fuser-admin%5Froles) |

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