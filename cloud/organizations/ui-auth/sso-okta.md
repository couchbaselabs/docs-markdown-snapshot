---
title: Set Up Capella SSO Using Okta
description: Configure Single Sign-On (SSO) between Okta and Couchbase Capella
  to allow your organization's users to authenticate securely without managing
  separate credentials. This integration enables streamlined access management
  while maintaining enterprise-grade security.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/organizations/pages/ui-auth/sso-okta.adoc
  xref: xref:cloud:organizations:ui-auth/sso-okta.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/organizations/ui-auth/sso-okta.html)

# Set Up Capella SSO Using Okta

> Configure Single Sign-On (SSO) between Okta and Couchbase Capella to allow your organization's users to authenticate securely without managing separate credentials. This integration enables streamlined access management while maintaining enterprise-grade security. 

## [](#prerequisites)Prerequisites

To configure Okta as an IdP, you need:

* To [enable SSO](add-sso-auth.md#access-and-enable-sso-settings) for your Capella organization.
* An [Okta](https://www.okta.com) account.
* To sign in to the Okta Admin Console as a super admin.

## [](#procedure)Procedure

Choose the tab for your preferred authentication protocol.

* SAML
* OIDC

To configure federated and SSO authentication using SAML with Okta as your identity provider (IdP), you must complete three procedures in the following order:

1. [In Okta, create an App Integration](#create-okta-app)
2. [In Capella, create a realm](#create-okta-realm)
3. [In Okta, complete the configuration](#complete-okta-config)

---

Create an Okta App Integration

Start by creating an App Integration in Okta. You need information from this step to create a realm in Capella.

1. In the Okta Admin Console, click **Application** **Applications**.
2. Click **Create App Integration**.
3. For the sign-in method, choose **SAML 2.0**.
4. Click **Next**.
5. Configure the options on the **General Settings** page:

  1. **App Name**: Enter your desired application name.
  2. (Optional) **App logo**: Add the Capella logo.
  3. (Optional) **App visibility**: Adjust if you don't want to show the Capella app to users in Okta.
  4. Click **Next**.
6. Configure the options on the **Configure SAML** page:

  1. Add the following placeholders:

| Field                       | Value                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------ |
| Single Sign-On URL          | Enter a placeholder, such as https://placeholder. You'll provide the real value in a later step. |
| Audience URI (SP Entity ID) | Enter a placeholder, such as uri:placeholder. You'll provide the real value in a later step.     |
  2. Click **Show Advanced Settings**.  
  Verify that the advanced settings have the following values:

| Field                | Value       |
| -------------------- | ----------- |
| Response             | Signed      |
| Assertion Signature  | Signed      |
| Signature Algorithm  | RSA-SHA256  |
| Digest Algorithm     | SHA256      |
| Assertion Encryption | Unencrypted |
  3. In the **Attribute Statements (optional)** section, create the following three attributes:  
  > [!IMPORTANT]  
  > Values entered into the Name column are case-sensitive. Enter them as shown in the table.

| Name         | Name format | Value          |
| ------------ | ----------- | -------------- |
| email        | Unspecified | user.email     |
| given\_name  | Unspecified | user.firstName |
| family\_name | Unspecified | user.lastName  |
  4. In the **Group Attribute Statements (optional)** section, create the following attribute:

| Name   | Name format | Filter        | Filter Value |
| ------ | ----------- | ------------- | ------------ |
| groups | Basic       | Matches regex | .\*          |  
  This filter matches all group names associated with a user. You can filter the `groups` names sent to Capella further by adjusting the Filter and Filter Value.
  5. Click **Next**.
7. Complete the **Feedback** page:

  1. Add any further feedback if desired.
  2. Click **Finish**.

---

Create a Realm in Capella

With an Okta integration app created, you need to create a realm in Capella that requires some information from Okta.

1. In the Capella UI, click **Settings** **SSO**.
2. Click **Create Realm** **SAML**.
3. Complete the **Create Realm** page:

  1. Copy the following fields from your Okta configuration to Capella:  
  > [!TIP]  
  > To find this information in Okta, open the app integration you just created to the **Sign On** tab. Within the **SAML Setup** section of this page, click **View SAML setup instructions**.

| Okta Field                           |                          | Capella Field |
| ------------------------------------ | ------------------------ | ------------- |
| X.509 Certificate                    | SAML Signing Certificate |               |
| Identity Provider Single Sign-On URL | Sign-in Endpoint URL     |               |
  2. Verify that the remaining SAML protocol settings are as follows:

| Field                 | Value      |
| --------------------- | ---------- |
| Signature Algorithm   | RSA-SHA256 |
| Digest Algorithm      | SHA256     |
| SAML Protocol Binding | HTTP-POST  |
  3. Choose a default team.  
  Capella automatically assigns users to the chosen default team when they do not match any team based on their SSO groups. All users assigned to the default team have its chosen permission set.  
  For more information, see [Map User Roles](manage-role-mapping.md).
  4. Choose to turn on or off group mapping.  
  Group mapping allows you to assign roles to SSO users based on which teams map to their SSO group.  
  If you do not use group mapping, Capella uses the [default team](manage-role-mapping.md#default-teams) to give SSO users their roles when they first sign in. Without group mapping, you must manage your users' organization roles using the **People** tab and project roles using each project's **Collaborators** tab.
4. Click **Create Realm**.  
Capella creates the new realm with an auto-generated name.  
> [!IMPORTANT]  
> Users need to know the realm name to sign in with SSO. You can change the a realm name after you create the realm. For more information, see [Change the Realm Name](manage-identity-providers.md#change-realm-name).

---

Complete the Okta Configuration

Now that you have created the realm, you need to configure Okta to replace the placeholder values that you used.

1. In the Okta Console, open the app integration you [created](#create-okta-app) to the **General** tab.
2. Inside the **SAML Settings** section, click **Edit**.
3. On the **General Settings** page, click **Next**.
4. Edit the options on the **Configure SAML** page:

  1. Copy the following fields from your Capella realm configuration to the Okta configuration:  
  > [!TIP]  
  > To find this information for your organization's Capella realm, first open the **Settings** **SSO** page. Listed on this page is the realm that you just created with an auto-generated name. Click the down arrow to show the realm information page.

| Capella Field |                             | Okta Field |
| ------------- | --------------------------- | ---------- |
| Callback URL  | Single sign on URL          |            |
| Entity ID     | Audience URI (SP Entity ID) |            |
5. Click **Next**.
6. Click **Finish**.
7. In Okta, assign users to the Capella app integration.

  1. With the app integration open, click the **Assignments** tab.
  2. Make sure that all your Capella organization users who use the Okta service are enrolled. For more information, see the [Assign an app integration to a user](https://help.okta.com/en-us/Content/Topics/Provisioning/lcm/lcm-assign-app-user.htm) page of the Okta documentation.

To configure federated and SSO authentication using OIDC with Okta as your identity provider (IdP), you must complete three procedures in the following order:

1. [In Okta, create an App Integration](#create-okta-app-oidc)
2. [In Capella, create a realm](#create-okta-realm-oidc)
3. [In Okta, complete the configuration](#complete-okta-config-oidc)

---

Create an Okta App Integration

Start by creating an App Integration in Okta. You need information from this step to create a realm in Capella.

1. In the Okta Admin Console, click **Application** **Applications**.
2. Click **Create App Integration**.
3. Choose **OIDC - OpenID Connect**.
4. Choose **Web Application**.
5. Click **Next**.
6. Configure the **General Settings**:

  1. **App integration name**: Enter a meaningful name.
  2. **Sign-in redirect URIs**: Leave unchanged for now—​you'll add this later.
  3. **Assignments** Select if you'd like to assign this application to all users or only a specified group. Make sure that you enroll all of your Capella organization users who use Okta.  
  You can choose to skip this and do it at a later time. See the [Assign an app integration to a user](https://help.okta.com/en-us/Content/Topics/Provisioning/lcm/lcm-assign-app-user.htm) page of the Okta documentation for more detail.
  4. Click **Save**.

---

Create a Realm in Capella

With the application created in Okta, you need to create a realm in Capella using its information.

1. In Capella, click **Settings** **SSO**.
2. Click **Create Realm** **OpenID Connect**.
3. Copy the following information from your Okta application configuration to Capella:  
> [!TIP]  
> All this information is in the **SSO** section of the Okta Admin panel when configuring your application.

| Okta Field                                                                                                                                         |                              | Capella Field |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | ------------- |
| Use your Okta issuer URL followed by /.well-known/openid-configuration. For example: https://dev-example.okta.com/.well-known/openid-configuration | OpenID Connect Discovery URL |               |
| Client ID                                                                                                                                          | Client ID                    |               |
| Client Secret                                                                                                                                      | Client Secret                |               |
4. Configure scopes:  
Scopes determine which user information Capella requests from your identity provider. The `openid`, `email`, and `profile` scopes are automatically included in the realm by default, so you do not need to add them.  
When adding additional scopes, separate each entry with a space.
5. Configure a default team and group mapping.

  1. Choose a default team.  
  Capella automatically assigns users to the chosen default team when they do not match any team based on their SSO groups. All users assigned to the default team have its chosen permission set.  
  For more information, see [Map User Roles](manage-role-mapping.md).
  2. Choose to turn on or off group mapping.  
  Group mapping allows you to assign roles to SSO users based on which teams map to their SSO group.  
  If you do not use group mapping, Capella uses the [default team](manage-role-mapping.md#default-teams) to give SSO users their roles when they first sign in. Without group mapping, you must manage your users' organization roles using the **People** tab and project roles using each project's **Collaborators** tab.
6. Click **Create Realm**.  
Capella creates the new realm with an auto-generated name.  
> [!IMPORTANT]  
> Users need to know the realm name to sign in with SSO. You can change the a realm name after you create the realm. For more information, see [Change the Realm Name](manage-identity-providers.md#change-realm-name).

---

Complete the Okta Configuration

Now that you have created the realm, you need to configure Okta to replace the placeholder values that you used.

1. In the Okta Console, open the app integration you [created](#create-okta-app) to the **General** tab.
2. Scroll down to the **General Settings** section and click **Edit**.
3. Copy the following fields from your Capella realm configuration to the Okta configuration:  
> [!TIP]  
> To find this information for your organization's Capella realm, open the **Settings** **SSO** page. Listed on this page is the realm you just created with an auto-generated name. Click its listing to open the realm information page.

| Capella Field |                       | Okta Fields |
| ------------- | --------------------- | ----------- |
| Callback URL  | Sign-in redirect URIs |             |
4. Click **Save**.
5. In Okta, assign users to the Capella app integration if you have not already done so.

  1. With the app integration open, click the **Assignments** tab. See the [Assign an app integration to a user](https://help.okta.com/en-us/Content/Topics/Provisioning/lcm/lcm-assign-app-user.htm) page of the Okta documentation for more information.

## [](#next-steps)Next Steps

* [Sign in to Capella with SSO](sign-in-with-sso.md)
* [Map User Roles](manage-role-mapping.md)
* [Manage Identity Providers](manage-identity-providers.md)