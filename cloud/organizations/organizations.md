---
title: Organizations and Organization Users Overview
description: Use organizations and organization roles to manage users in Couchbase Capella.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/organizations/pages/organizations.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:organizations:organizations.adoc[]
---

[View original HTML](/cloud/organizations/organizations.html)

# Organizations and Organization Users Overview

> Use organizations and organization roles to manage users in Couchbase Capella. Organizations and organization roles are the first level of controlling access to your data in Capella. 

![svg](_images/svg-bcd99104982501c0344b0d6ac0be33b676870671.svg) 

## [](#organizations)Organizations

Organize and secure your data in Couchbase Capella by using an ordered hierarchy.

The hierarchy starts with an organization. Everything you do in Capella, from creating a cluster to managing your [billing](../billing/billing.md), happens inside an organization.

For more information about how to create, edit, and delete an organization in Capella, see [Manage Organizations](manage-organizations.md).

## [](#users)Organization Users

Add users to an organization or join an organization yourself using email invitations sent by Capella.

When you add a user to an organization, you can assign them 1 or more [organization roles](organization-user-roles.md) that control their access to features in the Capella UI.

When you [create your Capella account](../get-started/create-account.md) without an invitation to an existing organization, Capella automatically creates a new organization for you. In this organization, `My Organization`, your user account will have the [Organization Owner](organization-user-roles.md#organization-role-organization-owner) organization role. You can use this organization role to invite other users to `My Organization`.

Only users who have the [Organization Owner](organization-user-roles.md#organization-role-organization-owner) organization role can send email invitations to users.

> [!TIP]
> Use organization roles to give a user access to the Capella UI. Use [projects](../projects/projects.md) and [project roles](../projects/project-roles.md) to grant more specific privileges and access to clusters, data, and data tools. Use [cluster access credentials](../clusters/manage-database-users.md) to manage your programmatic and application-level access to a cluster’s data.

For more information about how to add, edit, and remove organization users, see [Manage Organization Users](manage-organization-users.md).

## [](#see-also)See Also

* [Manage Projects](../projects/manage-projects.md)
* [Manage Project Users](../projects/manage-project-users.md)
* [Manage Cluster Access Credentials](../clusters/manage-database-users.md)