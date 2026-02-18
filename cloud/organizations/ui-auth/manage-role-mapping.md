---
title: Map User Roles
description: After adding federated and SSO authentication to your organization,
  you can map IdP groups to permission sets.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/organizations/pages/ui-auth/manage-role-mapping.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/organizations/ui-auth/manage-role-mapping.html)

# Map User Roles

> After adding federated and SSO authentication to your organization, you can map IdP groups to permission sets. 

_Teams_ map user groups from your identity provider (IdP) to permissions sets in Capella. A team’s members are the users of the SSO (IdP) groups you’ve mapped to it. You assign teams a set of [project and organization roles](../organization-projects-overview.md) and any [projects](../../projects/projects.md) you need their members to access.

This page walks you through the process of creating and configuring a team.

## [](#role-mapping)Role Mapping

Role mapping defines an SSO user’s level of access to Capella. You can add one or more SSO (IdP) groups to one or more teams to provision users with access to an organization’s projects and clusters.

* Capella applies role mapping on user sign in.
* Capella compares the SSO groups to the role mappings defined for your organization.

  * If you’ve defined role mappings for an SSO group so that they’re part of one or more teams, those team permissions apply to all users in that SSO group.
  * If you haven’t defined role mappings for an SSO group, Capella assigns those users to the [default team](#default-teams).
  * If you remove an SSO user from all SSO groups that are mapped to a team, Capella assigns that user to the [default team](#default-teams).  
  > [!TIP]  
  > For example, imagine a user belonging to an SSO group named `dev`. In Capella, you’ve role mapped the `dev` SSO group to the `Developers` team. If you remove that user from the `dev` SSO group, Capella removes their `Developers` team roles when they next sign in. Instead, they’re given the team roles as configured by the default team set by the Realm.

### [](#default-teams)Default Team

When you create an organization, Capella automatically creates "My First Team". This is the default team unless you choose another team for that purpose. The default team is what each SSO user is assigned to unless otherwise specified. "My First Team" members have the [Organization Member](../organization-user-roles.md#organization-role-member) role. They don’t have any project or SSO group mapping unless otherwise specified. You can’t delete any team set as the default team.

## [](#access-teams)Access Teams in the Capella UI

> [!IMPORTANT]
> Permissions Required
> 
> All members of an organization can view team information.

To manage teams for SSO, you first need to open the **Teams** page.

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **Teams**.

The **Teams** page lists any existing teams in your organization.

\+ If you added a realm and linked it with your IdP, "My First Team" is one of the options. Clicking a team listed on the **Teams** page opens its details and provides the controls needed to manage it.

## [](#create-a-team)Create a Team

> [!IMPORTANT]
> Prerequisites
> 
> * You must have the [Organization Owner](../organization-user-roles.md#organization-role-organization-owner) role to create a team.
> * A realm must exist before mapping SSO groups to a team. If you haven’t yet created a realm, see [Add SSO Authentication](add-sso-auth.md).
> * You must turn on group mapping in your realm to add SSO group mappings to a team.

1. On the [Teams page](#access-teams), click **Create Team**.
2. On the **Create Team** page, complete the following fields:

  1. **Team Name**: Enter your desired team name.
  2. **SSO Groups**: Enter the user groups from your IdP that you would like to map to this team. You must separate multiple SSO groups by a comma.

    1. _Okta_: Enter the group name as it’s shown in Okta into the **SSO Groups** text area.
    2. _Azure AD_: Enter the group’s object ID into the **SSO Groups** text area instead of the group’s name.  
      > [!TIP]  
      > Using the Azure portal, you can find a group’s object ID by clicking **Azure Active Directory** **Groups** **GROUP\_NAME**. Or, you can use Microsoft Graph Powershell to search for a group’s display name: `Get-MgGroup -ConsistencyLevel eventual -Search '"DisplayName:GROUP_NAME"'`. The output includes the group ID (`Id`).
    3. _Ping_: Enter the group name as it’s shown in Ping into the **SSO Groups** text area.
    4. _CyberArk_: Enter the group name as it’s shown in CyberArk into the **SSO Groups** text area.
    5. _Google Workspace_: Enter the group name as it’s shown in Google Workspace into the **SSO Groups** text area.
    6. _OneLogin_: Enter the group name as it’s shown in OneLogin into the **SSO Groups** text area.
  3. **Organization Roles**: Select one or more [organization roles](../organization-user-roles.md) that you would like all team members to have.
3. Add projects to the team you’re creating:

  1. Click **Add Project to Team**.
  2. **Project**: Choose a project in the organization you want all team members to access.
  3. **Project Roles**: For this project, choose the [project roles](../../projects/project-roles.md) you want all members of this team to have.
  4. Click **Add Project**.
4. Click **Create Team**.

## [](#edit-a-team)Edit a Team

> [!IMPORTANT]
> Permissions Required
> 
> You must have the [Organization Owner](../organization-user-roles.md#organization-role-organization-owner) role to edit a team.

You can change the following team settings:

| Option                 | Actions                                                                                                                                                 | Considerations                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Team Name**          | [Rename a Team](#rename-a-team)                                                                                                                         | You can rename a team at any time.                                                                                                                                                                                                                                                                                                                                          |
| **SSO Groups**         | [Add an SSO Group](#add-an-sso-group) [Remove an SSO Group](#remove-an-sso-group)                                                                       | You can add or remove SSO (IdP) groups to or from a team as needed. Removing an SSO group from a team doesn’t delete its users. If the SSO group you removed isn’t mapped to another team, Capella assigns it to the [default team](#default-teams) and its associated permissions. Any changes you make to user permissions are applied as users sign in, not immediately. |
| **Organization Roles** | [Edit Organization Roles](#edit-organization-roles)                                                                                                     | You can add one or more organization roles to a team. Assigned organization roles apply to all team members. Any changes you make to user permissions are applied as users sign in, not immediately.                                                                                                                                                                        |
| **Projects**           | [Add Access to a Project](#add-access-to-a-project) [Edit Project Roles](#edit-project-roles) [Remove Access to a Project](#remove-access-to-a-project) | You can give a team access to multiple projects in an organization and assign project roles on a project-by-project basis. Assigned project roles apply to all team members. Any changes you make to user permissions are applied as users sign in, not immediately.                                                                                                        |

### [](#rename-a-team)Rename a Team

1. On the [**Teams** page](#access-teams), click the name of the team you’re renaming.  
The team page in question opens to the **General** page.
2. Inside the **Name of Team** field, replace the text with the name you want.
3. Click **Apply**.

### [](#add-an-sso-group)Add an SSO Group

> [!IMPORTANT]
> A realm must exist before mapping SSO groups to a team. If you haven’t yet created a realm, see [Add SSO Authentication](add-sso-auth.md).

1. On the [**Teams** page](#access-teams), click the name of the team you’re editing.  
The team page in question opens to the **General** page.
2. Enter the SSO groups from your IdP that you would like to map to this team into the **SSO Groups** field. You must separate multiple SSO groups by a comma.

  1. _Okta_: Enter the group name as it’s shown in Okta into the **SSO Groups** text area.
  2. _Azure AD_: Enter the group’s [**object ID**](#object-id) into the **SSO Groups** text area instead of the group’s name.
  3. _Ping_: Enter the group name as it’s shown in Ping into the **SSO Groups** text area.
  4. _CyberArk_: Enter the group name as it’s shown in CyberArk into the **SSO Groups** text area.
  5. _Google Workspace_: Enter the group name as it’s shown in Google Workspace into the **SSO Groups** text area.
  6. _OneLogin_: Enter the group name as it’s shown in OneLogin into the **SSO Groups** text area.
3. Click **Apply**.

### [](#remove-an-sso-group)Remove an SSO Group

> [!CAUTION]
> This action revokes the current team privileges from all SSO users within the removed SSO group. If you remove an SSO group that isn’t mapped to another team, Capella assigns it to the default team.

1. On the [**Teams** page](#access-teams), click the name of the team you’re editing.  
The team page in question opens to the **General** page.
2. Within the **SSO Groups** field, click the Close icon  in the SSO group you’re removing from the team.
3. Click **Apply**.

### [](#edit-organization-roles)Edit Organization Roles

1. On the [**Teams** page](#access-teams), click the name of the team you’re editing.  
The team page in question opens to the **General** page.
2. In the navigation pane, click **Organization Roles**.  
The **Organization Roles** page lists all the organization roles assigned to the current team.
3. Click each Capella organization role you want to assign to the team. Clicking a selected organization role removes it.
4. Click **Apply**.

### [](#add-access-to-a-project)Add Access to a Project

1. On the [**Teams** page](#access-teams), click the name of the team you’re editing.  
The team page in question opens to the **General** page.
2. On the navigation pane, click **Projects**.  
The **Projects** page lists all of the projects assigned to the current team.
3. Click **Add Project to Team**.  
This action displays the **Add Project** dialog.
4. Use the **Project** drop-down menu to select the project from the organization you’re adding.
5. Use the **Roles** drop-down menu to choose which project roles to apply to the whole team for the chosen project.
6. Click **Add Project**.

### [](#edit-project-roles)Edit Project Roles

1. On the [**Teams** page](#access-teams), click the name of the team you’re editing.  
The team page in question opens to the General tab.
2. On the navigation pane, click **Projects**.  
The **Projects** page lists all of the projects assigned to the current team.
3. On the same row as the project you want to change the team’s access to, click Edit icon .  
The action displays the **Project Role** dialog.
4. Click each Capella project role you’re assigning to the team for the selected project. Clicking an already chosen project role removes it.
5. Click **Apply**.

### [](#remove-access-to-a-project)Remove Access to a Project

1. On the [**Teams** page](#access-teams), click the name of the team you’re editing.  
The team page in question opens to the **General** page.
2. On the navigation pane, click **Projects**.  
The **Projects** page lists all of the projects assigned to the current team.
3. On the same row as the project you want to remove the team’s access to, click the Trash icon .  
The action displays the **Remove Project From team** dialog.
4. Type `delete` into the provided text area.
5. Click **Remove**.

## [](#delete-a-team)Delete a Team

> [!IMPORTANT]
> Permissions Required
> 
> You must have the [Organization Owner](../organization-user-roles.md#organization-role-organization-owner) role to create a team.

> [!CAUTION]
> Deleting a team removes that team’s permissions from users in its mapped SSO groups. If an SSO user of a deleted team isn’t mapped to another team, Capella assigns them the [default team](#default-teams), and they get its associated role mappings.

1. On the [**Teams** page](#access-teams), click the name of the team you’re deleting.  
The team page in question opens to the **General** page.
2. Click **Delete Team**.  
This action displays the **Delete Team** dialog.
3. Type `delete` into the provided text area.
4. Click **Delete**.

## [](#next-steps)Next Steps

* [Sign in to Capella with SSO](sign-in-with-sso.md)
* [Manage Identity Providers](manage-identity-providers.md)