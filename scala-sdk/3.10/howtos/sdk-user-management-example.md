---
title: User Management
description: The Java SDK lets you create <em>users</em>, assign them
  <em>roles</em> and associated <em>privileges</em>, and remove them from the
  system.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.10/modules/howtos/pages/sdk-user-management-example.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.10@scala-sdk:howtos:sdk-user-management-example.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/3.10/howtos/sdk-user-management-example.html)

# User Management

> The Java SDK lets you create _users_, assign them _roles_ and associated _privileges_, and remove them from the system. 

## [](#user-management-apis)User-Management APIs

Users who have been assigned the **Admin** role for the cluster are able to create, edit, and remove users. The Java SDK provides APIs to support these activities. A high-level summary of the APIs can be found in [User-Management](#concept-docs:sdk-user-management-overview.adoc), and details of all options in the [UserManager API docs](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/manager/user/UserManager.html).

## [](#using-the-usermanager-api)Using the UserManager API

The most common uses of the `UserManager` API are creating and listing users:

Creating Users

```java
Unresolved include directive in modules/howtos/pages/sdk-user-management-example.adoc - include::devguide:example$scala/UserManagementExample.java[]
```

Listing Users

```java
Unresolved include directive in modules/howtos/pages/sdk-user-management-example.adoc - include::devguide:example$scala/UserManagementExample.java[]
```

Using a user created in the SDK to access data:

```java
Unresolved include directive in modules/howtos/pages/sdk-user-management-example.adoc - include::devguide:example$scala/UserManagementExample.java[]
```

## [](#further-reading)Further Reading

The SDK also contains management APIs for dealing with [Cluster resources](provisioning-cluster-resources.md).