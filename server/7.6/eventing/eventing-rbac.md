---
title: Eventing Role-Based Access Control (RBAC)
description: Full Administrators or users with proper <em>Role-Based Access
  Control</em> (RBAC) roles can create and manage Eventing Functions.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/eventing/pages/eventing-rbac.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/eventing/eventing-rbac.html)

# Eventing Role-Based Access Control (RBAC)

> Full Administrators or users with proper _Role-Based Access Control_ (RBAC) roles can create and manage Eventing Functions. 

## [](#description)Description: What is RBAC

Couchbase provides _Role-Based Access Control_ (RBAC), in which access privileges are assigned to fixed roles, which are in turn assigned to users, (each of which may be an administrator or an application) either _directly_; or _indirectly_, by means of _user-groups_.

Couchbase Server Enterprise Edition provides RBAC with multiple roles for finer access control. Community Edition provides multiple users that can be assigned to a limited set of roles. There are three fixed roles in the community edition of Couchbase providing coarser access control: Bucket Full Access (`bucket_full_access[*]`), Admin (`admin`), and Read Only Admin (`ro_admin`).

A Couchbase-Server _role_ permits one or more _resources_ to be accessed according to defined _privileges_. Roles can be assigned to individual users, and to groups, by means of either the UI or the REST API.

For a complete list of roles, see [Roles](../learn/security/roles.md). Note that most roles can be assigned only on the _Enterprise Edition_ of Couchbase Server: on the _Community Edition_ of Couchbase Server, only the `bucket_full_access`, `admin`, and `ro_admin` roles can be assigned.

For more information, see [Authorization](../learn/security/authorization-overview.md), and [Manage Users, Groups, and Roles](../manage/manage-security/manage-users-and-roles.md).

## [](#function-scope)Function Scope

A bucket.scope combination is used for identifying functions belonging to the same group.

Only the "Eventing Full Admin" role and also the "Full Admin" role can set the bucket.scope to **\*.\***; all other Eventing non-privileged users need to define a **Function Scope** for their Eventing functions that references an existing resource of bucket.scope. This provides role-based isolation of Eventing functions between non-privileged users

> [!CAUTION]
> Changing the access role (i.e., by revoking write permissions) could impact deployed eventing functions that have been assigned to this role.  
> _This may result in the function being undeployed._  
> In this case, redeploy the function with the correctly assigned role to allow access.

Typically, you should set Function Scope to the bucket.scope that holds the collection that is the source of your mutations to your Eventing Function. This best practice ensures that you _do not_ inadvertently cause an Eventing Function to undeploy by removing a **Function Scope** pointing to a resource that is not required for the function to run.

> [!NOTE]
> A user can be assigned multiple "Eventing/Manage Scope Function" RBAC roles. If any of these roles match an existing Eventing Function’s **Function Scope**, then that user can manage, modify, or delete the Eventing Function even if it was created or imported by someone else.

## [](#privileged-users)Privileged Users

If a user role of either "Full Admin" or "Eventing Full Admin", then by default this user has all the necessary access to every resource in a cluster required to run the Eventing Service and create and manage Eventing Functions.

When creating an Eventing Function, either of these roles can set the **Function Scope** to **\*.\***; no other RBAC role is allowed to use this **Function Scope**.

> [!NOTE]
> When upgrading to 7.1, all Eventing Functions are assumed to be running as a privileged user and have their **Function Scope** set to **\*.\*** to ensure continuity of your Eventing Functions.

### [](#full-admin-v-eventing-full-admin)Full Admin v. Eventing Full Admin

Prior to 7.0.0, Eventing always runs as "Full Admin". This blocked some use cases and adoption as this role allowed creation of new users and the ability to escalate privilege sets. The "Eventing Full Admin" role introduced in 7.0 simply removes the capability of creating users and assigning/modifying RBAC credentials, thus providing a bit more security.

For the Function Scope or RBAC grouping, we will use the 'bulk.data' assuming you have the role of either "Full Admin" or "Eventing Full Admin". For standard or non-privileged users, refer to Role-Based Access Control.

## [](#eventing-and-rbac-for-non-privileged-users)Eventing and RBAC for Non-privileged Users

> [!NOTE]
> If a user role of either "Full Admin" or "Eventing Full Admin", then this user, by default, has all the necessary access privileges to every resource in a cluster required to run the Eventing Service and create and manage Eventing Functions.

_In RBAC, although you can assign rolls directly to a **USER**, it is generally more flexible to define a **GROUP** and then assign that group or set of roles to a **USER**. This allows reusing a **GROUP** across multiple users._

## [](#minimal-eventing-rbac-role)Minimal Eventing RBAC role

The following minimal resources are required for a non-privileged user to access the Eventing Service and create and manage Eventing Functions.

* Data Reader

  * Eventing Storage keyspace or Scratchpad
* Data Writer

  * Eventing Storage keyspace or Scratchpad
* Data DCP reader

  * Mutation Source
* Eventing / Manage Scope Function

  * bucket.scope or bucket.

## [](#minimal-eventing-rbac-role-example)Minimal Eventing RBAC role example

* Access the Couchbase Web Console > Security and Select "ADD GROUP".  
![rbac min add add group](_images/rbac_min_add_add_group.png)
* Configure the group as follows:

  * `Data Reader` and `Data Writer` are required for the Eventing Storage or scratchpad.
  * `Data DCP Reader` is required to fetch the mutations from DCP.  
  > [!NOTE]  
  > this item was defined as `bulk.data` which would allow building Evening functions that can listen to any collection under `bulk.data`.  
  ![rbac min a](_images/rbac_min_a.png)  
  The final item required is defining the **Function Scope** under "Eventing / Manage Scope Function". Since we will be listing to mutations in a collection under `bulk.data`, it makes sense to use this as our grouping.  
  ![rbac min b](_images/rbac_min_b.png)
* Hit **Save** to store the GROUP to the system.
* Access the Couchbase Web Console > Security and Select "ADD USER".  
![rbac min add add user](_images/rbac_min_add_add_user.png)
* Associate the GROUP to the user so the user can inherit all the roles in the group.  
![rbac min c](_images/rbac_min_c.png)
* Add your password and verify it in the lower two boxes
* Hit **Save** to store the USER to the system.
* Access the Couchbase Web Console > Security
* Select GROUPS on the right, you should see your definition for GROUP `eventing_min`.  
![rbac min groups](_images/rbac_min_groups.png)
* Select USERS on the right, you should see your definition for USER `user_min`.  
![rbac min users](_images/rbac_min_users.png)

## [](#beyond-a-minimal-eventing-rbac-role)Beyond a Minimal Eventing RBAC role

You may consider adding

* Data Reader

  * Mutation Source
* Data Writer

  * Mutation Source
* Data Monitor

  * Mutation Source
  * Eventing Storage keyspace or Scratchpad

If you have any Bindings in your Eventing Function of type `Bucket Alias`, you will need to have one or more additional settings if not already allowed.

* Data Reader

  * Bucket Alias
* Data Writer

  * Bucket Alias

If you plan to use SQL++ consider adding at lease SELECT privileges

* Query & Index / Query Select

  * Mutation Source

## [](#multi-tenancy-in-eventing)Multi-tenancy in Eventing

The "Function Scope" in an Eventing Function works with the RBAC selection in "Eventing / Manage Scope Function" to limit access to between tenants in both the UI and the REST API.

A tenant might be based on company departments such as administration, sales, production and support.

Below we have two tenants example (an admin and a limited user) and four Eventing Functions each with a different **Function Scope**. We logged into the UI with either an Eventing Full Admin" or "Full Admin" role, and thus we can access all the Eventing Functions.

![rbac admin view](_images/rbac_admin_view.png) 

Now log out of the UI console and log back in as a non-privileged user, (for example, we use the USER `user_min` as defined above). Because of the privileges defined, we are only allowed access to Eventing Functions that have a **Function Scope** of `bulk.data`.

![rbac user view](_images/rbac_user_view.png)