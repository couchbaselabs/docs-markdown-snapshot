---
title: How to Verify Access
description: How to verify Sync Gateway access to data in cloud-to-edge
  enterprise data synchronization.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.1/modules/ROOT/pages/access-control-how-verify-access.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.1@sync-gateway::access-control-how-verify-access.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.1/access-control-how-verify-access.html)

# How to Verify Access

> How to verify Sync Gateway access to data in cloud-to-edge enterprise data synchronization.  

_Related topics_: [Create Role](access-control-how-create-roles.md) | [Create User](access-control-how-create-users.md) | [Add Role to User](access-control-how-assign-users-to-roles.md) | [Allow Access](access-control-how-control-document-access.md) | Verify Access | [Write Access](#access-control-how-write-access.adoc)

Related Concepts

[Access control Model](access-control-model.md)

## [](#purpose)Purpose

Use the Admin REST API to see the:

* Channels a user has access to
* Channels a role has access to
* Channels a document is assigned to

## [](#context)Context

The `all_channels` property of a user account determines the channels a user can access. Its value is derived from the union of:

* The user’s `admin_channels` property, which is set using the Admin REST API.
* The channels the user has been granted access to by [access()](sync-function-api-access-cmd.md) calls from sync functions invoked for current revisions of documents.
* The `all_channels` properties of any roles the user belongs to. These are themselves computed using the above rules.

## [](#process)Process

* Users
* Roles
* Document

Send a get request to the [/{db}/\_user/{name}](rest-api-admin.md#/user/post\%5F%5Fdb%5F%5F%5Fuser%5Fname%5F) endpoint

```bash
curl http://localhost:4985/db/_user/pupshaw
```

The [output](#ex-output) shows that the user `pupshaw` has access to the following channels:

| **1** | all through its own admin\_channels setting             |
| ----- | ------------------------------------------------------- |
| **2** | hoopy through the froods role’s admin\_channels setting |

```json
{
    "admin_channels": [
        "all" (1)
    ],
    "admin_roles": [
        "froods"
    ],
    "all_channels": [
        "all",
        "hoopy" (2)
    ],
    "name": "pupshaw",
    "roles": [
        "froods"
    ]
}
```

Send a get request to the [/{db}/\_role/](rest-api-admin.md#/role/get%5F%5Fdb%5F%5F%5Frole%5F%5Fname%5F) endpoint

```bash
curl http://localhost:4985/db/_role/frood
```

The output shows that the role `froods` has access to the following channels:

| **1** | hoopy through its role’s admin\_channels setting |
| ----- | ------------------------------------------------ |

```json
{
    "name": "froods",
    "admin_channels": [
        "hoopy" (1)
    ],
    "admin_roles": [
        "froods"
    ],
    "all_channels": [
        "hoopy" (2)
    ]
}
```

Send a get request to the [/{db}/\_alldocs](rest-api-admin.md#/database/get%5F%5Fdb%5F%5F%5Fall%5Fdocs) endpoint

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