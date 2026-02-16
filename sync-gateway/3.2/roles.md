[View original HTML](/sync-gateway/3.2/roles.html)

> About Sync Gateway _Roles_ and their part in secure cloud-to-edge enterprise data synchronization.  
> Here we introduce the concept of _Roles_ and the part they play in assuring secure access control within _Sync Gateway_.

_Related Concepts_: [Access Control Model](access-control-model.md) | [Channels](channels.md) | Roles | [Sync Function](#sync-function-overview.adoc) | [Users](users.md)

## [](#concept)Concept

Roles are named collections of [Channels](channels.md). They enable the grouping together of [Users](users.md) with similar characteristics, which makes the management of large user populations easier.

A Role and a user assigned to a role is granted to access to a channel, which is associated with a specific collection. The user can then access all documents assigned to that channel. When granting user access to admin channels statically, the user must specify the collection and corresponding channel.

As an entity, roles comprise a name and a list of channels.

Any user associated with a role inherits the right to access any of the channels in the role’s list. This provides a convenient way to associate multiple channels with multiple users.

|  | Roles have a separate namespace from users, so it’s possible to have a user and a role with the same name. |
|  | ---------------------------------------------------------------------------------------------------------- |

## [](#provisioning)Provisioning

The creation of roles is optional. It depends on the use case whether there is a need to logically group users.

You can create and-or manage roles using the following options

* Admin REST API:  
Roles are created via the Sync Gateway Admin REST API — see: [Admin REST API](rest-api-admin.md).
* File-based Configuration Properties \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

**Note** To use this option in v3.x, you must use the `-disable_persistent_config` CLI option.  
Configure roles in the [Legacy Configuration Properties](configuration-properties-legacy.md) file.

**Note** that removing a role effectively revokes access to the channel that role is associated with and may mean users will lose access to required documents.

Example 1\. How to Create a Role

* Admin REST API
* File-based Configuration Properties

Create a new role using the [/{db}/\_role/](rest%5Fapi%5Fadmin.md#tag/Database-Security/operation/post%5Fdb-%5Frole-) endpoint.

```bash
$ curl -vX POST "http://localhost:4985/mydatabase/_roles/" -H
"accept: application/json" -H "Content-Type: application/json" -d
'{"name":"Edge1","collection_access":{"scopename":{"collectionname":{"admin_channels":["channel1","channel3"]}}}}' (1)
```

| **1** | Here you add the Edge1 role which grants channel access to channel1 and channel3 in scope scopename and collection collectionname. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------- |

Create roles by hardcoding them in the [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md). This method is convenient for testing and to get started. It is recommended to use the [/{db}/\_role/](rest%5Fapi%5Fadmin.md#tag/Database-Security/operation/post%5Fdb-%5Frole-) for production systems.

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
        "Edge2": {
          "collection_access": {
            "anotherscopename": {
              "anothercollectionname": {
                "admin_channels": ["channel2", "channel3"]
              }
            }
          }
        },
        "GUEST": {"disabled": true}
      }
    }
  }
}
```

| **1** | [databases.$db.users](configuration-schema-database.md#database-users) |
| ----- | ---------------------------------------------------------------------- |
| **2** | Here we add the Edge1 role.                                            |

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

---

[1](#%5Ffootnoteref%5F1). Prior to Release 3.0