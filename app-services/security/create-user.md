---
title: Create App Users
description: Creating and editing App Users for a synchronized application using
  the Capella UI
pubDate: 2026-08-19T04:43:28.923Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/security/create-user.adoc
  xref: xref:app-services::security/create-user.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/security/create-user.html)

# Create App Users

> Creating and editing App Users for a synchronized application using the Capella UI 

## [](#app-users)Concept

Users are one of the cornerstone concepts of access control. You can restrict document access to specific users and-or to users with specific [roles](create-app-role.md#app-roles).

As an entity, a _user_ comprises a name, password, list of roles and a list of [channels](channels.md). These channels are organised within a linked Collection to a given Scope within your App Endpoint.

### [](#lbl-sgw-users)App Services Users

They are created and operate solely within the App Services ecosphere to govern access to replication data and to the Public API.

Users granted access to a [channel](channels.md) can access all documents assigned to that channel.

Users can also be assigned to zero or more roles. A user inherits the channel access of all roles it belongs to. This is very much like Unix groups, except that roles do not form a hierarchy.

> [!IMPORTANT]
> App Users are now organized at the collection level instead of at the bucket level.

This page covers creating and managing local App Users. If you want to delegate authentication to an external identity provider instead (for example, Google or Azure AD), see [Set Up an Authentication Provider](set-up-authentication-provider.md).

In this section, we'll show you how to create new users in App Services. Before you start, make sure you're logged on to your Capella instance as an administrator.

1. Select your App Endpoint
2. Select the **Security** tab.
3. From the menu on the left, select **App Users**

Click **\+ Create App User**

![Create App User](../_images/user-management/create-app-user.png) 

Figure 1\. Create User

From here, you can fill in the UserName, the password and set whether the user is enabled. You can also add the channels the user can access. Fill in the name of the channel, and then press the **+** button to add it to the list of channels. (For more information, see [Add Security with Channels](channels.md))

At this point, you can also assign administration roles to your new user.

When you're ready, save the new user by clicking **CREATE APP USER**

![Successfully created app service user](../_images/user-management/create-app-user-success.png) 

Figure 2\. Successfully created app service user

You can change any user details, or reset their password, by selecting the user from the list:

![Edit user details](../_images/user-management/edit-user.png) 

Figure 3\. Edit user details

From the Edit App User page, you can perform the following actions:

* Changing the user's password.
* Enabling or disabling the App User.

> [!NOTE]
> Disabled App Users cannot access App Endpoints.

* You can assign additional App Roles and Channels to the App User.
* You can view non-admin channels assigned to the user per collection via existing user roles or the Access Control Function.
* You can also view admin channels assigned by the Access Control Function per collection under the **Channels assigned by access control and data validation function** section.

> [!IMPORTANT]
> App Roles and channels created by the Access Control Function and assigned to the App User cannot be edited or deleted by the Capella UI or Admin API. You will need to edit the Access Control Function to apply any changes to these App Roles and channels.

## [](#see-also)See Also

* [Create App Roles](create-app-role.md)
* [Configure Access Control and Data Validation](../app-endpoints/access-control-data-validation.md)
* [Add Security with Channels](channels.md)
* [Set Up an Authentication Provider](set-up-authentication-provider.md)