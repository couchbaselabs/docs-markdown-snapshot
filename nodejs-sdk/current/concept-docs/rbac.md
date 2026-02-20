---
title: RBAC
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.6/modules/concept-docs/pages/rbac.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:nodejs-sdk:concept-docs:rbac.adoc[]
---

[View original HTML](/nodejs-sdk/current/concept-docs/rbac.html)

# RBAC

> RBAC restrict resources on a Couchbase cluster to an identified user, allocated by role. 

## [](#users-resources-roles-and-privileges)Users, Resources, Roles, and Privileges

Couchbase Server Enterprise Edition uses _Role-Based Access Control_ for applications to restrict _resources_ on a Couchbase cluster to an identified _user_.

Each user who attempts resource-access is identified by means of the _credentials_ they pass to Couchbase Server, for purposes of _authentication_: these consist of a _username_ and (typically) a _password_. Once the user is authenticated, an _authorization_ process checks the _roles_ with which the user is associated. If one or more of these roles correspond to _privileges_ that permit the user-requested level of resource-access, access is duly granted; otherwise, it is denied.

Users who have been assigned the **Admin** role for the cluster are able to create, edit, and remove users. The SDK provides APIs to support these activities.

> [!NOTE]
> Introductory examples in the SDK documentation use the _Administrator_ user to ensure that developers can quickly get up and running; this _should not be used in production_. Elsewhere we use a general "user" which represents whichever permission levels are appropriate to your application.

## [](#further-information)Further Information

All aspects of the Couchbase RBAC system are covered in the section [Authorization](#7.1@server:learn:security/authorization-overview.adoc). Specifically, for information on:

* Adding _Users_ and assigning _roles_, by means of the Couchbase Web Console, see [Manage Users and Roles](#7.1@server:manage:manage-security/manage-users-and-roles.adoc).
* _Roles_ required for resource-access, and the privileges they entail, see [Roles](#7.1@server:learn:security/roles.adoc).
* _Resources_ controlled by Couchbase RBAC, see [Resources Under Access Control](#7.1@server:learn:security/resources-under-access-control.adoc).