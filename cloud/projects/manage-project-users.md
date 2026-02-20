---
title: Manage Project Users
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/projects/pages/manage-project-users.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:projects:manage-project-users.adoc[]
---

[View original HTML](/cloud/projects/manage-project-users.html)

# Manage Project Users

> Manage the collaborators of a project to control access to Couchbase clusters. 

In Couchbase Capella, project collaborators are users in an organization who have been added to a project and given a project role. Project roles control a user’s access level to any cluster in a project and what actions they can take. For more information about project roles, see [Project Roles](project-roles.md).

## [](#accessing-project-users-in-the-capella-ui)Accessing Project Users in the Capella UI

You can view and manage project collaborators on the **Projects** tab in the main navigation by clicking the name of a project you want to manage. With the project open, click the **Collaborators** tab. Capella shows a summary of all collaborators who are part of the current project.

You can only see the summary if you’re a project collaborator. If you’re a [Project Owner](project-roles.md#project-owner-role), you can also see an option to invite collaborators to the project.

> [!NOTE]
> Users with the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) organization role automatically have a [Project Owner](project-roles.md#project-owner-role) role for all projects in their organization, which means they can also access collaborator information for all projects.

### [](#project-users-summary)Project Collaborators Summary

The **Collaborators** tab shows a list of all the collaborators assigned a role for the current project.

This includes the following information:

| Field                  | Description                                                                   |
| ---------------------- | ----------------------------------------------------------------------------- |
| **Name**               | The name of the user and their email address.                                 |
| **Organization Roles** | The user’s [organization roles](../organizations/organization-user-roles.md). |
| **Project Roles**      | The user’s [project roles](project-roles.md).                                 |
| **SSO Groups**         | The user’s [SSO groups](../organizations/ui-auth/capella-ui-auth.md).         |

## [](#add-users-to-project)Add Users to an Existing Project

> [!NOTE]
> By default, you add SSO users to projects using [teams](../organizations/ui-auth/manage-role-mapping.md). Only when a realm has [group mapping turned off](../organizations/ui-auth/manage-identity-providers.md#group-mapping), can you invite and manage SSO users using the procedures on this page.

After you create a project, you can add collaborators. To add a collaborator, you must have the [Project Owner](project-roles.md#project-owner-role) project role. If you created a project, then you automatically have this role.

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Projects**.
  2. Use the project breadcrumb to find a project.
2. Select the project where you want to add a collaborator.
3. Go to **Collaborators**.  
Capella opens the [Project Collaborators summary](#project-users-summary).
4. Click **Add Collaborators**.  
Capella opens the **Add Collaborators** page.
5. In the **Collaborators** list, select the people in the current organization that you want to add to the project.  
If a user isn’t a member of your organization, [invite them](../organizations/manage-organization-users.md#invite-organization-users) to your organization to add them to a project.  
> [!TIP]  
> Selected users get the same project roles.
6. Click the tile for each project role you want to assign to your selected users.
7. To add the selected users to the project and assign the selected roles, click **Add**.  
Capella notifies you after it adds the new collaborators to the project.

## [](#change-a-users-project-role)Change a User’s Project Role

To change a user’s project role, you must have the [Project Owner](project-roles.md#project-owner-role) project role for the project.

If you created a project, you automatically have this role.

> [!IMPORTANT]
> Users with the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) role have [Project Owner](project-roles.md#project-owner-role) roles for all projects in their organization. You cannot remove the [Project Owner](project-roles.md#project-owner-role) role from a user with the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) role.

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Projects**.
  2. Use the project breadcrumb to find a project.
2. Select the project where you want to add a collaborator.
3. Go to **Collaborators**.  
Capella opens the [Project Collaborators summary](#project-users-summary).
4. Click the name of the user whose project role you want to change.  
Capella opens the user’s collaborator information page.
5. Click **Edit Project Roles**.
6. From the list of project roles, select the roles to assign to the selected user. Deselect the roles that you don’t want to assign to the selected user.
7. To apply your changes, click **Save**.

## [](#remove-users-from-project)Remove a User (or Yourself) from a Project

> [!IMPORTANT]
> You can’t remove a user from a project if they have the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) user role. If you remove a user with the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) role, you can remove their other project roles. The user keeps their [Project Owner](project-roles.md#project-owner-role) access.

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Projects**.
  2. Use the project breadcrumb to find a project.
2. Select the project where you want to add a collaborator.
3. Go to **Collaborators**.  
Capella opens the [Project Collaborators summary](#project-users-summary).
4. Click the name of the user you want to remove.  
Capella opens the user’s collaborator information page.
5. Click **Remove User from Project**.  
Capella opens the **Remove User from Project** dialog.
6. To confirm that you want to delete the user, click **Remove User from Project**.  
Capella notifies you after the user is removed from the project.

## [](#see-also)See Also

* [Project Roles](project-roles.md)
* [Manage Projects](manage-projects.md)
* [Manage Users](../organizations/manage-organization-users.md)
* [Organization Roles](../organizations/organization-user-roles.md)