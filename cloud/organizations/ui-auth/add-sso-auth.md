[View original HTML](/cloud/organizations/ui-auth/add-sso-auth.html)

> Add federated authentication with single sign-on (SSO) to your Couchbase Capella organization. 

Couchbase Capella provides Single Sign-On (SSO) for users to access your Capella organization through a single authentication source. This allows you to better manage team access and improve organizational security. Capella SSO integration supports both the Security Assertion Markup Language (SAML) 2.0 and OpenID Connect (OIDC) protocols.

## [](#access-and-enable-sso-settings)Step 1: Enable SSO For Your Organization

You can manage federated and SSO authentication from the **SSO** page in your organization’s settings.

|  | SSO is available only to paid accounts. Only users with the [Organization Owner](../organization-user-roles.md#organization-role-organization-owner) role can view and use the **SSO** page. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **Settings** **SSO**.
3. Click **Enable SSO**.

## [](#configure-federated-and-sso-authentication)Step 2: Set Up Capella SSO To Use Your IdP

While you can configure Capella SSO with other identity providers that support SAML or OIDC, Couchbase provides instructions and support for the following:

* [Microsoft Entra ID](sso-entra-id.md)
* [Okta](sso-okta.md)
* [PingOne](sso-ping.md)
* [Google Workspace](sso-google.md)
* [CyberArk](sso-cyberark.md)
* [OneLogin](sso-onelogin.md)

## [](#next-steps)Next Steps

* [What To Expect After You Enable SSO](capella-ui-auth.md#expect-after)
* [Map User Roles](manage-role-mapping.md)
* [Sign in to Capella with SSO](sign-in-with-sso.md)
* [Manage Identity Providers](manage-identity-providers.md)