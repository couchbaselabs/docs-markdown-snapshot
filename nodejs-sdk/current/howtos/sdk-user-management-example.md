---
title: User Management
description: The Node.js SDK lets you create <em>users</em>, assign them
  <em>roles</em> and associated <em>privileges</em>, and remove them from the
  system.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.7/modules/howtos/pages/sdk-user-management-example.adoc
  xref: xref:nodejs-sdk:howtos:sdk-user-management-example.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/current/howtos/sdk-user-management-example.html)

# User Management

> The Node.js SDK lets you create _users_, assign them _roles_ and associated _privileges_, and remove them from the system. 

## [](#user-management-apis)User-Management APIs

Users who have been assigned the **Admin** role for the cluster are able to create, edit, and remove users. The Node.js SDK provides APIs to support these activities. A high-level summary of the APIs can be found in [User-Management](../concept-docs/sdk-user-management-overview.md), and details of all options in the [UserManager API docs](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/UserManager.html).

## [](#using-the-usermanager-api)Using the UserManager API

The most common uses of the `UserManager` API are creating and listing users:

Creating Users

```javascript
Unresolved include directive in modules/howtos/pages/sdk-user-management-example.adoc - include::example$user-manager.js[]
```

Listing Users

```javascript
Unresolved include directive in modules/howtos/pages/sdk-user-management-example.adoc - include::example$user-manager.js[]
```

Using a user created in the SDK to access data:

```javascript
Unresolved include directive in modules/howtos/pages/sdk-user-management-example.adoc - include::example$user-manager.js[]
```

## [](#further-reading)Further Reading

The SDK also contains management APIs for dealing with [Cluster resources](provisioning-cluster-resources.md).