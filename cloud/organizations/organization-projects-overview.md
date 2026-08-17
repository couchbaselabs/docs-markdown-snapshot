---
title: Manage Organizations and Access
description: All clusters in Couchbase Capella are grouped into organizations and projects.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/organizations/pages/organization-projects-overview.adoc
  xref: xref:cloud:organizations:organization-projects-overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/organizations/organization-projects-overview.html)

# Manage Organizations and Access

> All clusters in Couchbase Capella are grouped into organizations and projects. You can add projects to organizations to group related clusters together. Use organization roles and project roles to control your users' access. 

## [](#overview)About the Capella Hierarchy

Couchbase Capella uses an organizational hierarchy to help you keep all of your data organized and securely accessible. At the top of the hierarchy is an organization. Everything you do in Capella, from creating a cluster to managing billing, happens inside the scope of an organization.

All projects exist inside an organization. Use projects to group and manage clusters inside Capella. For example, you could use projects to create separate environments for production and development or group your clusters by application:

![svg](_images/svg-bcd99104982501c0344b0d6ac0be33b676870671.svg) 

### [](#organization-access)About Organizations

Add users to an organization by sending them invitations. Users can create a new Capella account when they receive an invitation to an organization. Users can join organizations with an existing Capella account.

When you create a new Capella account without an invitation to an existing organization, Capella automatically creates a new organization for you, named `My Organization`.

All users in an organization are assigned 1 or more organization roles. Use organization roles to control user access and privileges inside an organization for the Capella UI. Organization roles set whether a user can create a new project, invite new users, or view billing information in the UI.

For example, if a user has the [Organization Member](organization-user-roles.md#organization-role-member) role, they cannot manage API keys or view billing information in the Capella UI.

For more information about the available organization roles in Capella, see [Organization Roles](organization-user-roles.md).

### [](#switching-between-organizations)Switching Between Organizations

You can navigate between the organizations associated with your user account using the navigation breadcrumbs in the Capella UI. Click your organization name to return to your organization-specific settings, clusters, and other options. Expand the organization breadcrumb to search for and switch to another organization.

### [](#project-access)About Projects

Create projects inside an organization to organize clusters and control user access to clusters.

Add a user to a project as a collaborator to set project roles and control their privileges for clusters inside that project. Project roles can set whether a user can read and write data on clusters, only read data, or only configure and delete clusters.

For example, if a user only has the [Cluster Manager](../projects/project-roles.md#project-cluster-manager-role) project role, they cannot use the **Data Tools** tab to access and modify data for clusters in that project.

If that same user had the [Data Writer](../projects/project-roles.md#project-cluster-data-reader-writer) project role in the same project, they could use the **Data Tools** tab to access and modify data on clusters in that project.

For more information about the available project roles in Capella, see [Project Roles](../projects/project-roles.md).

### [](#switching-between-projects)Switching Between Projects

You can navigate between the projects you have access to in your organization using the navigation breadcrumbs in the Capella UI. Click your current project name to return to the options and settings available in your current project. Expand the projects breadcrumb to search for and switch to another project.

## [](#database-access)About Cluster Access Credentials and Programmatic Access

Control programmatic and application-level access to data for each cluster using [cluster access credentials](../clusters/manage-database-users.md). Capella offers [basic access credentials](../clusters/cluster-rbac.md#basic-access-credentials) with predefined read, write, or read/write permissions, and [advanced access credentials](../clusters/cluster-rbac.md#advanced-access-credentials) with fine-grained privileges and reusable access roles for more precise access control. You can choose specific [buckets, scopes, and collections](../clusters/data-service/about-buckets-scopes-collections.md) for your cluster access credentials to limit access to data.

Only the [Project Owner](../projects/project-roles.md#project-owner-role) role can create cluster access credentials for their projects.