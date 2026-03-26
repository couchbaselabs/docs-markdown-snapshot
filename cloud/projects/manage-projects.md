---
title: Manage Projects
description: Create and manage projects to organize and allow access to Couchbase clusters.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/projects/pages/manage-projects.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:cloud:projects:manage-projects.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/projects/manage-projects.html)

# Manage Projects

> Create and manage projects to organize and allow access to Couchbase clusters. 

The purpose of a _project_ is to organize and manage access to groups of Couchbase [clusters](../clusters/databases.md). For more information about projects, refer to [Projects Overview](projects.md).

## [](#accessing-projects-in-the-capella-ui)Accessing Projects in the Capella UI

Projects can be viewed and managed from the **Projects** tab in the main navigation. A summary of all projects — _of which you are a member_ — is displayed in table format.

> [!NOTE]
> Users with the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) organization role automatically have a [Project Owner](project-roles.md#project-owner-role) role for all projects in their organization, so they will see all the organization's projects listed in the project summary.

If your user has the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) or [Project Creator](../organizations/organization-user-roles.md#organization-role-project-creator) organization roles, you will see an option to create a project.

### [](#project-summary)Projects Summary

The **Projects** tab shows a summary of all the projects in the organization _where you are a member_. The summary is a table format, with a sortable name column and a row for each project.

The project summary displays the following fields for each project:

| Field             | Description                                             |
| ----------------- | ------------------------------------------------------- |
| **Name**          | The name of the project.                                |
| **Created By**    | The name of the user who created the project.           |
| **Date Created**  | The date the project was created.                       |
| **Clusters**      | The number of clusters in the project.                  |
| **App Services**  | The number of app services that the project is running. |
| **Collaborators** | The number of users who can access the project.         |

## [](#create-project)Create a Project

To create a project, you must have either the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) or [Project Creator](../organizations/organization-user-roles.md#organization-role-project-creator) organization roles.

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **Projects**.
3. Click **Create Project**.
4. Provide a name for the project.  
In the `Project Name` field, enter a name for your project.
5. Click **Create a Project**.  
The fly-out menu will close, and you will return to the project summary page.
6. Open the new project by clicking on its name.  
Since there are not yet any clusters in the new project, you will see an option to [create a cluster](../clusters/create-database.md).

## [](#rename-a-project)Rename a Project

To change the name of a project, you need the [Project Owner](project-roles.md#project-owner-role) role for the project in question.

> [!NOTE]
> Users with the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) organization role automatically have a [Project Owner](project-roles.md#project-owner-role) role for all projects in the organization, so they can also rename a project.

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Projects**.
  2. Use the project breadcrumb to find a project.
2. Select the project you want to rename.
3. Go to **Settings**.  
This displays an information page where you can edit the project name.
4. Change the **Project Name** field.
5. Click **Save**.  
A notification confirms that the project is renamed.

## [](#delete-project)Delete a Project

> [!WARNING]
> Deleting a project is a permanent action and cannot be reversed.

### [](#prerequisites)Prerequisites

* You have the [Project Owner](project-roles.md#project-owner-role) role for the project in question. Note that users with the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) organization role automatically have a [Project Owner](project-roles.md#project-owner-role) role for all projects in the organization, so they can also delete projects.
* You have [deleted all clusters](../clusters/delete-database.md) in the project. Capella does not allow the deletion of a project if it contains clusters.

### [](#procedure)Procedure

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Projects**.
  2. Use the project breadcrumb to find a project.
2. Select the project you want to delete.
3. Go to **Settings**.  
This opens the project settings page.
4. Click **Delete Project**.
5. Confirm that you want to delete the project.
6. Click **Delete Project**.

## [](#see-also)See Also

* [Manage Project Users](manage-project-users.md)
* [Project Roles](project-roles.md)
* [Manage Users](../organizations/manage-organization-users.md)
* [Organization Roles](../organizations/organization-user-roles.md)