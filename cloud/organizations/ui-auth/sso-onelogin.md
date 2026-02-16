[View original HTML](/cloud/organizations/ui-auth/sso-onelogin.html)

> Configure Single Sign-On (SSO) between OneLogin and Couchbase Capella to allow your organization’s users to authenticate securely without managing separate credentials. This integration enables streamlined access management while maintaining enterprise-grade security. 

## [](#prerequisites)Prerequisites

To configure OneLogin as an IdP, you need:

* To [enable SSO](add-sso-auth.md#access-and-enable-sso-settings) for your Capella organization.
* A [OneLogin](https://www.onelogin.com) account.
* To sign in to the OneLogin Admin panel as an [Account Owner](https://onelogin.service-now.com/support?id=kb%5Farticle&sys%5Fid=c925543e87a5a190695f0f66cebb354d).

## [](#procedure)Procedure

Choose the tab for your preferred authentication protocol.

* SAML
* OIDC

To configure federated and SSO authentication using SAML with OneLogin as your identity provider (IdP), you must complete three procedures in the following order:

1. [In OneLogin, create an Application](#create-onelogin-app).
2. [In Capella, create a realm](#create-onelogin-realm).
3. [In OneLogin, complete the configuration](#complete-onelogin-config).

---

Add an Application in OneLogin

Start by adding an application for Capella in the OneLogin Admin panel. You need information from this step to create a realm in Capella.

1. In the OneLogin Admin panel, click **Applications** **Applications**.
2. Create the application:

  1. Click **Add App**.
  2. In the search field, type `SAML` and press Enter.
  3. From the `templates` list, find and click **SAML Test Connector (IdP)**.
  4. Complete the following fields:

    * **Display Name**: Enter a meaningful display name.
    * (Optional) **Rectangular Icon** / **Square Icon**: Add the Capella logo.
    * (Optional) **Description**: Add a description of the application.
  5. Click **Save**.
3. In the navigation pane, click **SSO**.
4. In the **X.509 Certificate** section, click **View Details**.
5. Select SHA256 as the **SHA fingerprint**.
6. Copy the **X.509 Certificate**.
7. Click **Save**.

Create a Realm in Capella

With the application created in OneLogin, you need to create a realm in Capella using information from OneLogin.

1. In the Capella UI, click **Settings** **SSO**.
2. Click **Create Realm** **SAML**.
3. Complete the **Create Realm** page:

  1. Copy the following information from your OneLogin configuration to Capella:

|  | All this information is in the **SSO** section of the OneLogin Admin panel when configuring your application. |
|  | ------------------------------------------------------------------------------------------------------------- |

| OneLogin Field           |                          | Capella Field |
| ------------------------ | ------------------------ | ------------- |
| X.509 Certificate        | SAML Signing Certificate |               |
| SAML 2.0 Endpoint (HTTP) | Sign-in Endpoint URL     |               |
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
  If you do not use group mapping, Capella uses the [default team](manage-role-mapping.md#default-teams) to give SSO users their roles when they first sign in. Without group mapping, you must manage your users' organization roles using the **People** tab and project roles using each project’s **Collaborators** tab.
4. Click **Create Realm**.  
Capella creates the new realm with an auto-generated name.

|  | Users need to know the realm name to sign in with SSO. You can change the a realm name after you create the realm. For more information, see [Change the Realm Name](manage-identity-providers.md#change-realm-name). |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Complete the OneLogin Configuration

Now that you have created the realm, you must finish configuring the OneLogin application.

1. In OneLogin, click **Configuration**.
2. Copy the following fields from your Capella realm configuration to the OneLogin configuration:

|  | To find this information for your organization’s Capella realm, open the **Settings** **SSO** page. Listed on this page is the realm you just created with an auto-generated name. Click its listing to open the realm information page. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| Capella Field |                                                 | OneLogin Fields |
| ------------- | ----------------------------------------------- | --------------- |
| Callback URL  | ACS (Consumer) URL Validator ACS (Consumer) URL |                 |
| Entity ID     | Audience                                        |                 |
3. In OneLogin, click **Save**.
4. Add the parameters:

  1. In OneLogin, with the application open, click **Parameters**.
  2. Click **+** to add each of the following attributes:

| Field name   | Flags                     | Value      |
| ------------ | ------------------------- | ---------- |
| given\_name  | Include in SAML assertion | First Name |
| family\_name | Include in SAML assertion | Last Name  |
| email        | Include in SAML assertion | Email      |
| groups       | Include in SAML assertion | User Roles |
5. Click **Save**.
6. Assign users to the application or add the application to a role.  
For more information, see the [Roles](https://onelogin.service-now.com/support?id=kb%5Farticle&sys%5Fid=ff4d016a973c2950c90c3b0e6253af0c) and [App Management](https://onelogin.service-now.com/support?id=kb%5Farticle&sys%5Fid=a77462cb872d2590695f0f66cebb35cd&kb%5Fcategory=e9866930db185340d5505eea4b9619b7#assign) pages of the OneLogin documentation.

To configure federated and SSO authentication using OIDC with OneLogin as your identity provider (IdP), you must complete three procedures in the following order:

1. [In OneLogin, create an Application](#create-onelogin-app-oidc).
2. [In Capella, create a realm](#create-onelogin-realm-oidc).
3. [In OneLogin, complete the configuration](#complete-onelogin-config-oidc).

---

Add an Application in OneLogin

Start by adding an application for Capella in the OneLogin Admin panel. You need information from this step to create a realm in Capella.

1. In the OneLogin Admin panel, click **Applications** **Applications**.
2. Click **Add App** and search for `oidc`.
3. Find and click **OpenId Connect (OIDC)**.
4. Complete the following fields:

  * **Display Name**: Enter the display name for this app.
  * (Optional) **Rectangular Icon** / **Square Icon**: Add the Capella logo.
  * (Optional) **Description**: Add a description of the application.
5. Click **Save**.

Create a Realm in Capella

With the application created in OneLogin, you need to create a realm in Capella using information from OneLogin.

1. In Capella, click **Settings** **SSO**.
2. Click **Create Realm** **OpenID Connect**.
3. Copy the following information from your OneLogin configuration to Capella:

|  | All this information is in the **SSO** section of the OneLogin Admin panel when configuring your application. |
|  | ------------------------------------------------------------------------------------------------------------- |

| OneLogin Field |                              | Capella Field |
| -------------- | ---------------------------- | ------------- |
| Issuer URL     | OpenID Connect Discovery URL |               |
| Client ID      | Client ID                    |               |
| Client Secret  | Client Secret                |               |
4. Configure scopes:  
Scopes determine which user information Capella requests from your identity provider. The `openid`, `email`, and `profile` scopes are automatically included in the realm by default, so you do not need to add them.  
When adding additional scopes, separate each entry with a space.
5. Configure a default team and group mapping.

  1. Choose a default team.  
  Capella automatically assigns users to the chosen default team when they do not match any team based on their SSO groups. All users assigned to the default team have its chosen permission set.  
  For more information, see [Map User Roles](manage-role-mapping.md).
  2. Choose to turn on or off group mapping.  
  Group mapping allows you to assign roles to SSO users based on which teams map to their SSO group.  
  If you do not use group mapping, Capella uses the [default team](manage-role-mapping.md#default-teams) to give SSO users their roles when they first sign in. Without group mapping, you must manage your users' organization roles using the **People** tab and project roles using each project’s **Collaborators** tab.
6. Click **Create Realm**.  
Capella creates the new realm with an auto-generated name.

|  | Users need to know the realm name to sign in with SSO. You can change the a realm name after you create the realm. For more information, see [Change the Realm Name](manage-identity-providers.md#change-realm-name). |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Complete the OneLogin Configuration

Now that you have created the realm, you must finish configuring the OneLogin application.

1. In OneLogin, click **Configuration** and view the **Application details**.
2. Copy information from your Capella realm configuration to the OneLogin configuration:

|  | To find this information for your organization’s Capella realm, open the **Settings** **SSO** page. Listed on this page is the realm you just created with an auto-generated name. Click its listing to open the realm information page. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| Capella Field |                | OneLogin Fields |
| ------------- | -------------- | --------------- |
| Callback URL  | Redirect URI’s |                 |
3. Click **Save**.
4. In the OneLogin Admin panel, click **SSO**.
5. Change the **Token Endpoint Authentication Method** to `POST`.
6. Click **Save**.
7. Assign users to the application or add the application to a role.  
For more information, see the [Roles](https://onelogin.service-now.com/support?id=kb%5Farticle&sys%5Fid=ff4d016a973c2950c90c3b0e6253af0c) and [App Management](https://onelogin.service-now.com/support?id=kb%5Farticle&sys%5Fid=a77462cb872d2590695f0f66cebb35cd&kb%5Fcategory=e9866930db185340d5505eea4b9619b7#assign) pages of the OneLogin documentation.

## [](#next-steps)Next Steps

* [Sign in to Capella with SSO](sign-in-with-sso.md)
* [Map User Roles](manage-role-mapping.md)
* [Manage Identity Providers](manage-identity-providers.md)