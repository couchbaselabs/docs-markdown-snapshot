---
title: Manage Project Users
pubDate: 2026-09-23T04:31:20.427Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/projects/pages/manage-project-users.adoc
  xref: xref:cloud:projects:manage-project-users.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/projects/manage-project-users.html)

# Manage Project Users

> Manage the collaborators of a project to control access to Couchbase clusters. 

In Couchbase Capella, project collaborators are users in an organization who have been added to a project and given a project role. Project roles control a user's access level to any cluster in a project and what actions they can take. For more information about project roles, see [Project Roles](project-roles.md).

## [](#prerequisites)Prerequisites

* To view a project's collaborators, you must have a [project role](project-roles.md) for that project.
* To add collaborators to a project, you must have the [Project Owner](project-roles.md#project-owner-role) role for that project.
* To change a user's project role, you must have the [Project Owner](project-roles.md#project-owner-role) role for that project.
* To delete a user from a project, you must have the [Project Owner](project-roles.md#project-owner-role) role for that project.

> [!NOTE]
> Users with the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) role automatically have a [Project Owner](project-roles.md#project-owner-role) role for all projects in their organization. You cannot remove the [Project Owner](project-roles.md#project-owner-role) role from a user with the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) role.

## [](#view-project-users-in-the-capella-ui)View Project Users in the Capella UI

To view your project's users:

1. Select your project's name.
2. Go to **Collaborators**.  
Capella shows a [summary](#project-users-summary) of all users who are part of the current project.
3. To find a specific user, do 1 of the following:

  * Use the search bar to find the user by **Name** or **Email**.
  * Use the default filters to narrow the list of users by:

    * [Organization Roles](../organizations/organization-user-roles.md)
    * [Project Roles](project-roles.md)

### [](#project-users-summary)Project Collaborators Summary

The **Collaborators** tab shows a list of all the users assigned a role for the current project. This includes the following information:

| Field                  | Description                                                                   |
| ---------------------- | ----------------------------------------------------------------------------- |
| **Name**               | The name of the user and their email address.                                 |
| **Organization Roles** | The user's [organization roles](../organizations/organization-user-roles.md). |
| **Project Roles**      | The user's [project roles](project-roles.md).                                 |
| **SSO Groups**         | The user's [SSO groups](../organizations/ui-auth/capella-ui-auth.md).         |

## [](#add-users-to-project)Add Users to a New or Existing Project

> [!NOTE]
> By default, you add SSO users to projects using [teams](../organizations/ui-auth/manage-role-mapping.md). Only when a realm has [group mapping turned off](../organizations/ui-auth/manage-identity-providers.md#group-mapping), can you invite and manage SSO users using the procedures on this page.

To add users to a new or existing project:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Projects**.
  2. Use the project breadcrumb to find a project.
2. Select the project where you want to add a user.
3. Go to **Collaborators**.
4. Click **Add Collaborators**.
5. In the **Collaborators** list, select the users in the current organization that you want to add to the project.  
If a user is not a member of your organization, [invite them](../organizations/manage-organization-users.md#invite-organization-users) to your organization to add them to a project.  
> [!TIP]  
> Selected users get the same project roles.
6. Select the project roles you want to assign to the user.
7. Click **Add**.

## [](#change-a-users-project-role)Change a User's Project Role

To change a user's project role:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Projects**.
  2. Use the project breadcrumb to find a project.
2. Select the project where you want to change a user's project role.
3. Go to **Collaborators**.
4. Click the name of the user whose project role you want to change.
5. Click **Edit Project Roles**.
6. From the list of project roles, select the roles to assign to the selected user. Deselect the roles that you do not want to assign to the selected user.
7. Click **Save**.

## [](#remove-users-from-project)Remove a User (or Yourself) from a Project

> [!IMPORTANT]
> You cannot fully remove a user from a project if they have the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) role, since they automatically retain [Project Owner](project-roles.md#project-owner-role) access. However, you can remove any other project roles assigned to them.

To remove a user from a project:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Projects**.
  2. Use the project breadcrumb to find a project.
2. Select the project where you want to remove a user.
3. Go to **Collaborators**.
4. Click the name of the user you want to remove.
5. Click **Remove User from Project**.
6. Confirm that you want to delete the user and click **Remove User from Project**.

## [](#see-also)See Also

* [Project Roles](project-roles.md)
* [Manage Projects](manage-projects.md)
* [Manage Users](../organizations/manage-organization-users.md)
* [Organization Roles](../organizations/organization-user-roles.md)