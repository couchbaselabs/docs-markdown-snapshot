---
title: Roles
description: About Sync Gateway <em>Roles</em> and their part in secure
  cloud-to-edge enterprise data synchronization.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/roles.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@sync-gateway::roles.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/roles.html)

# Roles

> About Sync Gateway _Roles_ and their part in secure cloud-to-edge enterprise data synchronization.  
> Here we introduce the concept of _Roles_ and the part they play in assuring secure access control within _Sync Gateway_.

_Related concepts topics_: [Users](../current/access-control/users.md) | Roles | [Channels](../current/access-control/channels.md) | [Revisions](../current/manage/revisions.md) | [Tombstones](../current/manage/managing-tombstones.md)

## [](#introduction)Introduction

Roles are named collections of channels — see [Channels](../current/access-control/channels.md).

A _User_ account can be assigned to zero or more roles. A user inherits the channel access of all roles it belongs to. This is very much like Unix groups, except that roles do not form a hierarchy.

## [](#assigning)Assigning

You access roles through the Admin REST API much like users are accessed, through URLs of the form [/{db}/\_role/{name}](../current/rest-api/rest-api-admin.md#/role). Role resources have a subset of the properties that users do: `name`, `admin_channels`, `all_channels`.

Roles have a separate namespace from users, so it’s legal to have a user and a role with the same name.

Admin REST API

You can assign a role to a user by sending a PUT request to [/{db}/\_user/{name}](../current/rest-api/rest-api-admin.md#/user/put%5F%5Fdb%5F%5F%5Fuser%5F%5Fname%5F) where `db` is the configured name of the database and `name` is the user name.

The roles to assign to the user are specified in the `admin_roles` array.

```bash
$ curl -vX POST "http://localhost:4985/mydatabase/_user/" -H "accept: application/json" -H "Content-Type: application/json" -d '{"name": "john", "password": "pass", "admin_roles": ["foo"]}'
```

Configuration file

A user can also be assigned to a role in the configuration file. This method is convenient for testing and to get started, otherwise it is generally recommended to use the **Admin REST API** for a programmatic behavior.

```json
{
  "databases": {
    "mydatabase": {
      "users": { (1)
        "GUEST": {"disabled": true},
        "john": {"password": "pass", "admin_roles": ["foo"]}
      }
    }
  }
}
```

| **1** | [databases.$db.users.$user.admin\_roles](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-users-this%5Fuser-admin%5Froles) |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#related-content)Related Content

###### [](#)

Learn more …​

* [Sync Function](../current/access-control/sync-function/sync-function.md)
* [Import filter](../current/sync/import-processing.md)
* [Inter-Sync Gateway Replication](../current/sync/sync-inter-syncgateway-overview.md)
* [Sync with Couchbase Server](../current/sync/sync-with-couchbase-server.md)

###### [](#-2)

Reference material …​

* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)