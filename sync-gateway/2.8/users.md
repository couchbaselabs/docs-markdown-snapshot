---
title: Users
description: About Sync Gateway <em>users</em> and their role in secure
  cloud-to-edge enterprise data synchronization.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/users.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@sync-gateway::users.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/users.html)

# Users

> About Sync Gateway _users_ and their role in secure cloud-to-edge enterprise data synchronization.  
> Here we introduce the concept of _users_ and their role in assuring secure access control within _Sync Gateway_.

_Related concepts topics_: **Users** | [Roles](../current/access-control/roles.md) | [Channels](../current/access-control/channels.md) | [Revisions](../current/manage/revisions.md) | [Tombstones](../current/manage/managing-tombstones.md)

## [](#introduction)Introduction

Users are one of the cornerstone concepts behind _Sync Gateway_'s access control feature.

You can authorize users and control their access to your database by creating user accounts and assigning roles to users. This topic focuses on how to authorize users to be able to access the Sync Gateway and their remote databases.

## [](#creating)Creating

The user must be created on Sync Gateway before it can be used for authentication — see also: [User Authentication](../current/security/authentication-users.md).

> [!NOTE]
> Sync Gateway users and roles have no relationship to Couchbase Server’s [RBAC (Role-base Access Control) users](../../server/current/learn/security/authorization-overview.md).

You create Users through either the [Admin REST API](../current/rest-api/rest-api-admin.md) or [Configuration Properties](../current/configuration/configuration-properties-legacy.md).

Admin REST API

Create a new user by sending a PUT request to [/{db}/\_user/{name}](../current/rest-api/rest-api-admin.md#/user/put%5F%5Fdb%5F%5F%5Fuser<em>name%5F) or by sending a POST request to [/{db}/\_user](../current/rest-api/rest-api-admin.md#/user/post\</em>db%5F%5F%5Fuser%5F), where `db` is the configured name of the database and `name` is the user name.

The user credentials (**username**/**password**) are passed in the request body.

```bash
$ curl -vX POST "http://localhost:4985/mydatabase/_user/" -H "accept: application/json" -H "Content-Type: application/json" -d '{"name": "john", "password": "pass"}'
```

The Admin REST API is for administrator use only, and hence is **not** accessible from the clients directly. To allow users to sign up, it is recommended to have an app server sitting alongside Sync Gateway that performs the user validation, creates a new user on this API and then returns the response to the application.

Additionally, this API can be used in conjunction with a 3rd party server for the authentication process (see [Custom authentication](authentication-users.md#custom-authentication)).

Lastly, Sync Gateway supports [OpenID Connect authentication](authentication-users.md#openid-connect). In this case, Sync Gateway can automatically create users for successfully authenticated users that don’t have an already existing user in Sync Gateway.

Configuration file

Create users by hardcoding their credentials in the [Configuration Properties](../current/configuration/configuration-properties-legacy.md). This method is convenient for testing and to get started, otherwise it is generally recommended to use the **Admin REST API** for a programmatic behavior.

```json
{
  "databases": {
    "mydatabase": {
      "users": { (1)
        "GUEST": {"disabled": true},
        "john": {"password": "pass"}
      }
    }
  }
}
```

| **1** | [databases.$db.users](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-users) |
| ----- | ------------------------------------------------------------------------------------------------------------ |

## [](#related-content)Related Content

###### [](#)

Learn more …​

* [Sync Function](../current/access-control/sync-function/sync-function.md)
* [Import filter](../current/sync/import-processing.md)

###### [](#-2)

Reference material …​

* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)