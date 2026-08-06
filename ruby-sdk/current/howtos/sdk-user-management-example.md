---
title: User Management
description: The Ruby SDK lets you create <em>users</em>, assign them
  <em>roles</em> and associated <em>privileges</em>, and remove them from the
  system.
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.8/modules/howtos/pages/sdk-user-management-example.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:ruby-sdk:howtos:sdk-user-management-example.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/current/howtos/sdk-user-management-example.html)

# User Management

> The Ruby SDK lets you create _users_, assign them _roles_ and associated _privileges_, and remove them from the system. 

## [](#user-management-apis)User-Management APIs

Users who have been assigned the **Admin** role for the cluster are able to create, edit, and remove users. The Ruby SDK provides APIs to support these activities. A high-level summary of the APIs can be found in [User-Management](../concept-docs/sdk-user-management-overview.md), and details of all options in the [UserManager API docs](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management/UserManager.html).

## [](#using-the-usermanager-api)Using the UserManager API

The most common uses of the `UserManager` API are creating and listing users:

Creating Users

```ruby
Unresolved include directive in modules/howtos/pages/sdk-user-management-example.adoc - include::example$managing_users.rb[]
```

Listing Users

```ruby
Unresolved include directive in modules/howtos/pages/sdk-user-management-example.adoc - include::example$managing_users.rb[]
```

Using a user created in the SDK to access data:

```ruby
Unresolved include directive in modules/howtos/pages/sdk-user-management-example.adoc - include::example$managing_users.rb[]
```

## [](#further-reading)Further Reading

The SDK also contains management APIs for dealing with [Cluster resources](provisioning-cluster-resources.md).