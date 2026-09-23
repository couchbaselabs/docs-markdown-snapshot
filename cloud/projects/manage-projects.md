---
title: Manage Projects
description: Create and manage projects to organize and allow access to Couchbase clusters.
pubDate: 2026-09-23T04:31:20.427Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/projects/pages/manage-projects.adoc
  xref: xref:cloud:projects:manage-projects.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/projects/manage-projects.html)

# Manage Projects

> Create and manage projects to organize and allow access to Couchbase clusters. 

The purpose of a project is to organize and manage access to groups of Couchbase [clusters](../clusters/databases.md). For more information about projects, see [Projects Overview](projects.md).

## [](#prerequisites)Prerequisites

* To view a project, you must have a [project role](project-roles.md) for that project.
* To create a project, you must have either the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) or [Project Creator](../organizations/organization-user-roles.md#organization-role-project-creator) roles.
* To change the name of a project, you must have the [Project Owner](project-roles.md#project-owner-role) role for the project you want to rename.
* To delete a project, you must have the [Project Owner](project-roles.md#project-owner-role) role for the project you want to delete.

> [!NOTE]
> Users with the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) role automatically have a [Project Owner](project-roles.md#project-owner-role) role for all projects in their organization.

## [](#view-projects-in-the-capella-ui)View Projects in the Capella UI

To view projects in your organization:

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **Projects**.

Capella displays in table format, a summary of all projects of which you're a member. The project summary displays the following fields for each project:

| Field             | Description                                                                                                                |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Name**          | The name of the project.                                                                                                   |
| **Created By**    | The name of the user who created the project.                                                                              |
| **Date Created**  | The date the project was created.                                                                                          |
| **Clusters**      | The number of clusters in the project.                                                                                     |
| **App Services**  | The number of App Services that the project is running.                                                                    |
| **Collaborators** | The number of users who can access the project. For more information, see [Manage Project Users](manage-project-users.md). |

## [](#create-project)Create a Project

To create a project:

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **Projects**.
3. Click **Create Project**.
4. Enter a name for your project.
5. Click **Create a Project**.
6. Open the new project by clicking on its name.  
Since there are not yet any clusters in the new project, you'll see an option to [create a cluster](../clusters/create-database.md).

## [](#rename-a-project)Rename a Project

To rename a project:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Projects**.
  2. Use the project breadcrumb to find a project.
2. Select the project you want to rename.
3. Go to **Settings** **General**.
4. Change the **Project Name** field.
5. Click **Save**.

## [](#delete-project)Delete a Project

> [!WARNING]
> Deleting a project is a permanent action and cannot be reversed.

To delete a project:

1. [Delete all the clusters](../clusters/delete-database.md) in the project.  
Capella does not allow the deletion of a project if it contains clusters.
2. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Projects**.
  2. Use the project breadcrumb to find a project.
3. Select the project you want to delete.
4. Go to **Settings** **General**.
5. Click **Delete Project**.
6. Confirm that you want to delete the project.
7. Click **Delete Project**.

## [](#see-also)See Also

* [Manage Project Users](manage-project-users.md)
* [Project Roles](project-roles.md)
* [Manage Users](../organizations/manage-organization-users.md)
* [Organization Roles](../organizations/organization-user-roles.md)