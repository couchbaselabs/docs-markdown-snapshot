[View original HTML](/cloud/organizations/manage-organization-users.html)

> Invite users to an organization and manage their roles within the organization. 

## [](#view-organization-users-in-the-capella-ui)View Organization Users in the Capella UI

View and manage the users in an organization using the **People** tab. A summary of all users is displayed in a table format.

### [](#users-summary)Users Summary

The **People** tab shows a summary of all users that are part of the organization. This summary includes the following information about each user:

Name

The name and email address of the user. Data in this column is in ascending alphabetical order by default. Click the header to change this to descending alphabetical order.

Email Status

The invitation status of the user.

* **Verified**: The invitee has accepted the invitation.
* **Pending**: The invitee has not yet accepted the invitation.

Roles

The organization roles assigned to the account:

* [Organization Owner](organization-user-roles.md#organization-role-organization-owner)
* [Project Creator](organization-user-roles.md#organization-role-project-creator)
* [Organization Member](organization-user-roles.md#organization-role-member)

## [](#invite-organization-users)Add/Invite Users to an Organization

|  | Social Sign In and Single Sign-On (SSO) People you invite to an organization can sign in using third-party accounts such as Google or GitHub if they’re associated with the same email address used for Capella. When using SSO with your organization, make sure only authorized SSO users can access your organization by only inviting Organization Owners. Configure all other users using your SSO provider. Users with SSO do not need an invitation and can sign in using the organization’s realm name. For more information, see [Sign in to Capella with SSO](ui-auth/sign-in-with-sso.md). |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

To add users to your organization, you must have the [Organization Owner](organization-user-roles.md#organization-role-organization-owner) role. You must also have the email address of the person you plan to invite.

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **People**.
3. Click **Invite People**.  
On the **Invite People** page, configure the following:  
People  
Enter the user’s email address, where they will receive an invitation to log into Capella.  
Organization Roles  
Choose one or more [organization roles](organization-user-roles.md) for the user.
4. To confirm and send the invitation, click **Invite**.  
After you add a user, Capella sends an email to invite them to join the organization. An invited user is shown in the **People** tab with a status of **Pending** until they accept their invitation. Once they accept the invitation, their status shows **Verified**.  
A pending user cannot access anything in the organization until they accept the invitation and configure their account. Invitations expire after 24 hours.

## [](#resend-invite)Resend or Cancel a User’s Invitation

If a user did not receive their invitation before it expired, you have the option to resend the invitation.

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **People**.
3. Click the name of the user you want to re-invite or cancel.
4. Under the Resend Invite section, click **Resend Invite**.

Alternatively, if you do not want to add the user to your organization, you can cancel their invitation.

1. Under the **Remove User** section click **Remove User**.
2. To confirm that you want to remove the user, click **Remove**.

## [](#change-user)Change a User’s Organization Role

To change a user’s organization role, you must have the [Organization Owner](organization-user-roles.md#organization-role-organization-owner) organization role.

|  | An organization must have at least one user with the [Organization Owner](organization-user-roles.md#organization-role-organization-owner) role at all times. If you are the only [Organization Owner](organization-user-roles.md#organization-role-organization-owner) user, you cannot edit your own role until you grant the [Organization Owner](organization-user-roles.md#organization-role-organization-owner) role to at least one other user. If you remove the Organization Owner role from a user, they also lose the [Project Owner](../projects/project-roles.md#project-owner-role) role for all projects in their organization. They keep their other project roles. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **People**.
3. Click the name of the user whose role you want to change,
4. Under the **Role** section, click **Edit Organizational Role**.
5. From the list of [organization roles](organization-user-roles.md), select the roles that you want to add to the current user. Clear the roles you want to remove.
6. To confirm your changes, click **Update**.

## [](#remove-user)Remove a User (or Yourself) from an Organization

|  | Organization Owners can remove one or more SSO users from an organization through the [realm in the Capella UI](#remove-user-sso), or through their identity provider. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

|  | Removing a user from an organization removes all organization roles assigned to this user and removes their access to all projects contained in that organization. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

Use this procedure to remove either yourself or another non-SSO user from an organization. To remove someone other than yourself from an organization, you must have [Organization Owner](organization-user-roles.md) privileges. An organization must have at least one user with the [Organization Owner](organization-user-roles.md#organization-role-organization-owner) role at all times.

If you’re the only [Organization Owner](organization-user-roles.md#organization-role-organization-owner) user, you cannot leave the organization until you grant the [Organization Owner](organization-user-roles.md#organization-role-organization-owner) role to at least one other user.

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **People**.
3. Click the name of the user you want to remove from the organization.  
This can be yourself if you’re removing yourself from the organization.
4. Under the **Remove User** section click **Remove User**.
5. Review and confirm your user selection for removal. Click **Remove**.

### [](#remove-user-sso)Remove One or More SSO Users

As well as removing SSO users from Capella using your identify provider, [Organization Owners](organization-user-roles.md#organization-role-organization-owner) can also remove them using the Capella UI. To remove SSO users from Capella using the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **Settings** **SSO**.
3. In the listing for your realm, click **More Options (⋮)** **Manage SSO Users**.
4. Select one or more users to remove.
5. Click **Delete**.
6. Review and confirm your user selection for removal. Click **Delete User(s)**

## [](#see-also)See Also

* [Manage Organizations](manage-organizations.md)
* [Organization Roles](organization-user-roles.md)
* [Manage Project Users](../projects/manage-project-users.md)
* [Project Roles](../projects/project-roles.md)