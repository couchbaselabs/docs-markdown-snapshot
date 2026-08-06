---
title: How to Create a Role
description: How to create a Sync Gateway <em>Role</em> for secure access
  control in cloud-to-edge enterprise data synchronization.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.1/modules/access-control/pages/access-control-how-create-roles.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:sync-gateway:access-control:access-control-how-create-roles.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/access-control/access-control-how-create-roles.html)

# How to Create a Role

> How to create a Sync Gateway _Role_ for secure access control in cloud-to-edge enterprise data synchronization.  
> Sync Gateway _Roles_ are a key part of a flexible approach to data routing and access control.

_Related topics_: [Create Role](access-control-how-create-roles.md) | [Create User](access-control-how-create-users.md) | [Add Role to User](access-control-how-assign-users-to-roles.md) | [Allow Access](access-control-how-control-document-access.md) | [Verify Access](access-control-how-verify-access.md) | [Write Access](access-control-how-control-document-access.md)

_Related Concepts_: [Roles](roles.md)

## [](#provisioning)Provisioning

The creation of roles is optional. It depends on the use case whether there is a need to logically group users.

You can create and-or manage roles using the following options

* Admin REST API:  
Roles are created via the Sync Gateway Admin REST API — see: [Admin REST API](../rest-api/rest-api-admin.md).
* File-based Configuration Properties \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

**Note** To use this option in v3.x, you must use the `-disable_persistent_config` CLI option.  
Configure roles in the [Legacy Configuration Properties](../configuration/configuration-properties-legacy.md) file.

**Note** that removing a role effectively revokes access to the channel that role is associated with and may mean users will lose access to required documents.

Example 1\. How to Create a Role

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

:include-related!

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