---
title: Manage Organization Users
pubDate: 2026-09-23T04:31:20.427Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/organizations/pages/manage-organization-users.adoc
  xref: xref:cloud:organizations:manage-organization-users.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/organizations/manage-organization-users.html)

# Manage Organization Users

> Invite users to an organization and manage their roles within the organization. 

## [](#prerequisites)Prerequisites

You must have the [Organization Owner](organization-user-roles.md#organization-role-organization-owner) role to:

* Add users to your organization.
* Change a user's organization role.
* Remove someone other than yourself from an organization.
* Remove 1 or more SSO users from an organization through the [realm in the Capella UI](#remove-user-sso) or through your identity provider.

> [!IMPORTANT]
> An organization must have at least 1 user with the [Organization Owner](organization-user-roles.md#organization-role-organization-owner) role at all times. If you're the only [Organization Owner](organization-user-roles.md#organization-role-organization-owner) user, you cannot edit your own role until you grant the [Organization Owner](organization-user-roles.md#organization-role-organization-owner) role to at least 1 other user.

## [](#view-organization-users-in-the-capella-ui)View Organization Users in the Capella UI

To view your organization's users:

1. In the navigation breadcrumbs in the Capella UI, click your organization's name.
2. Go to **People**.  
Capella shows a [summary](#user-summary) of all users who are part of the organization.
3. To find a specific user, do 1 of the following:

  * Use the search bar to find the user by **Name** or **Email**.
  * Use the default filters to narrow the list of users by:

    * Email Status (Verified or Pending)
    * MFA Status (Enabled or Disabled)
    * [Roles](organization-user-roles.md)
    * [Teams](ui-auth/manage-role-mapping.md#access-teams)

### [](#user-summary)Users Summary

The **People** tab shows a summary of all users that are part of the organization. This includes the following information about each user:

| Field            | Description                                                                                                                                                                                                                                                                                      |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Name**         | The name and email address of the user. Data in this column is in ascending alphabetical order by default. Click the header to change this to descending alphabetical order.                                                                                                                     |
| **Email Status** | The invitation status of the user. **Verified**: The invitee has accepted the invitation. **Pending**: The invitee has not yet accepted the invitation.                                                                                                                                          |
| **Roles**        | The organization roles assigned to the account: [Organization Owner](organization-user-roles.md#organization-role-organization-owner) [Project Creator](organization-user-roles.md#organization-role-project-creator) [Organization Member](organization-user-roles.md#organization-role-member) |

## [](#invite-organization-users)Add/Invite Users to an Organization

> [!IMPORTANT]
> Social Sign In and Single Sign-On (SSO)
> 
> People you invite to an organization can sign in using third-party accounts such as Google or GitHub if they're associated with the same email address used for Capella.
> 
> When using SSO with your organization, make sure only authorized SSO users can access your organization by only inviting Organization Owners. Configure all other users using your SSO provider.
> 
> Users with SSO do not need an invitation and can sign in using the organization's realm name.
> 
> For more information, see [Sign in to Capella with SSO](ui-auth/sign-in-with-sso.md).

To add users to an organization:

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **People**.
3. Click **Invite People**.
4. Enter the user's email address, where they will receive an invitation to log into Capella.
5. Select 1 or more [organization roles](organization-user-roles.md) for the user.
6. Click **Invite**.

After you add a user, Capella sends an email to invite them to join the organization. An invited user is shown in the **People** tab with a status of **Pending** until they accept their invitation. Once they accept the invitation, their status shows **Verified**.

A pending user cannot access anything in the organization until they accept the invitation and configure their account.

> [!CAUTION]
> Invitations expire after 24 hours.

## [](#resend-invite)Resend or Cancel a User's Invitation

If a user did not receive their invitation before it expired, you have the option to resend the invitation.

To resend or cancel a user's invitation:

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **People**.
3. Click the name of the user you want to re-invite or cancel their invitation, and do 1 of the following:

  * To resend the invite, click **Resend Invite**.
  * To cancel the invite, click **Remove User**.

    1. Confirm that you want to remove the user and click **Remove**.

## [](#change-user)Change a User's Organization Role

> [!WARNING]
> If you remove the Organization Owner role from a user, they also lose the [Project Owner](../projects/project-roles.md#project-owner-role) role for all projects in their organization. They keep their other project roles.

To change a user's organization role:

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **People**.
3. Click the name of the user whose role you want to change.
4. Under **Organizational Roles**, click **Edit Organizational Roles**.
5. From the list of [organization roles](organization-user-roles.md), select the roles that you want to add to the current user. Deselect the roles you want to remove.
6. Click **Save**.

## [](#remove-user)Remove a User (or Yourself) from an Organization

To remove SSO users, see [Remove SSO Users](#remove-user-sso).

> [!WARNING]
> Removing a user from an organization removes all organization roles assigned to this user and removes their access to all projects contained in that organization.

To remove yourself or another non-SSO user from an organization:

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **People**.
3. Click the name of the user you want to remove from the organization.  
This can be yourself if you're removing yourself from the organization.
4. Under **Remove User**, click **Remove User**.
5. Confirm you want to remove this user and click **Remove**.

### [](#remove-user-sso)Remove SSO Users

As well as removing SSO users from Capella using your identity provider, [Organization Owners](organization-user-roles.md#organization-role-organization-owner) can also remove them using the Capella UI. To remove SSO users from Capella using the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **Settings** **SSO**.
3. In the listing for your realm, click **More Options (⋮)** **Manage SSO Users**.
4. Select 1 or more users to remove.
5. Click **Delete**.
6. Confirm your user selection for removal and click **Delete User(s)**.

## [](#see-also)See Also

* [Manage Organizations](manage-organizations.md)
* [Organization Roles](organization-user-roles.md)
* [Manage Project Users](../projects/manage-project-users.md)
* [Project Roles](../projects/project-roles.md)