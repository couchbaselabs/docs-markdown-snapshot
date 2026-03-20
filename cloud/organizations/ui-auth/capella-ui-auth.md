---
title: Capella UI Authentication
description: Couchbase Capella supports federated authentication with Single
  Sign-On (SSO) and Multi-Factor Authentication (MFA) for the Capella UI.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/organizations/pages/ui-auth/capella-ui-auth.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:organizations:ui-auth/capella-ui-auth.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/organizations/ui-auth/capella-ui-auth.html)

# Capella UI Authentication

> Couchbase Capella supports federated authentication with Single Sign-On (SSO) and Multi-Factor Authentication (MFA) for the Capella UI. 

This page covers authentication options for the Capella UI:

* [Single Sign-On (SSO)](#single-sign-on-sso-authentication) \- Configure Capella to work with your existing identity provider.

  * [Requirements](#configuration-requirements) for setting up SSO.
  * [Important considerations](#Considerations) when implementing SSO.
* [Multi-Factor Authentication (MFA)](#multi-factor-authentication-mfa) \- Enhance security using Capella’s built-in MFA option for non-SSO users.

These authentication methods apply only to the Capella UI. They do not affect programmatic access to Capella, which requires [Cluster Access Credentials](../../clusters/manage-database-users.md), [Access Control Accounts](../../../analytics/admin/auth/auth-data.md), or [Management API Keys](../../management-api-guide/management-api-start.md) depending on your use case.

## [](#single-sign-on-sso-authentication)Single Sign-On (SSO) Authentication

By configuring Capella to work with your existing identity provider (IdP), users in your organization can access the Capella UI using SSO authentication.

As part of your company’s existing security infrastructure, SSO provides the following advantages:

* Your company’s IdP manages Capella users—​not Couchbase. This means your administrators can onboard, offboard, and manage Capella users with existing workflows.
* All supported IdPs provide their own built-in multi-factor authentication (MFA).
* Your users can use Capella without needing to remember another set of credentials.

Capella SSO integration supports both the Security Assertion Markup Language (SAML) 2.0 and OpenID Connect (OIDC) protocols.

### [](#configuration-requirements)Configuration Requirements

To set up and use SSO authentication in Capella, you need the following:

Paid account

You need a paid Support Plan to enable single sign-on (SSO) authentication. SSO is not available to free tier accounts. To upgrade to a paid Support Plan, see [Upgrade to a Paid Account](../../get-started/create-account.md#upgrade-to-paid-account).

Identity Provider (IdP)

While you can configure Capella with any SAML 2.0 or OIDC compliant identity provider, Couchbase provides support for the following IdPs:

* [Okta](https://www.okta.com/)
* [Microsoft Entra ID](https://www.microsoft.com/en-ca/security/business/identity-access/microsoft-entra-id)
* [Ping Identity](https://www.pingidentity.com)
* [Google Workspace](https://workspace.google.com)
* [CyberArk](https://www.cyberark.com/)
* [OneLogin](https://www.onelogin.com/)

Realm

A realm in Capella manages the configuration linking your Capella organization with your IdP. Each organization can support one realm.

Only users with the [Organization Owner](../organization-user-roles.md#organization-role-organization-owner) role can create, manage, and view realms.

Team

Use teams to map user groups from your IdP to permission sets in Capella. When you create a realm, Capella creates a default "My First Team" with no pre-existing role-mapping. Each organization can support multiple teams and you can assign users to one or more teams.

Only users with the [Organization Owner](../organization-user-roles.md#organization-role-organization-owner) role can create and manage teams. Every user in an organization can view team information.

### [](#expect-after)What To Expect After You Enable SSO

When you add SSO authentication to your organization:

* Capella turns off [Capella MFA](mfa.md) for all SSO users in the organization who can then use the MFA provided by the IdP. Non-SSO users can continue to use the Capella MFA.
* SSO Users within the organization cannot change their name, email, or set a password.
* Capella adds each SSO user to the [default team](manage-role-mapping.md#default-teams) ("My First Team") as they sign in, unless you specify another default team or create IdP group mappings. You cannot delete a realm’s configured default team.
* If a realm has [group mapping turned off](manage-role-mapping.md#disable-group-mapping), Capella uses the [default team](manage-role-mapping.md#default-teams) to initially assign SSO users their roles. After SSO users sign in, you can manage their organization roles using the **People** tab and manage project access using each project’s **Collaborators** tab.
* Capella supports service provider-initiated (SP-initiated) authentication only. Capella does not support identity provider-initiated (IdP-initiated) sign-in, where there’s a sign-in request through the SSO page of the IdP.

## [](#multi-factor-authentication-mfa)Multi-Factor Authentication (MFA)

Any non-SSO user within your organization can use Capella’s MFA. MFA improves your Capella account security by requiring two credentials to sign in: your password and a time-based one-time password (TOTP).

To turn on MFA for your account, see [Manage Multi-Factor Authentication (MFA)](mfa.md).

## [](#see-also)See Also

* [Add federated and SSO authentication](add-sso-auth.md)
* [Turn on multi-factor authentication](mfa.md#turn-on-mfa)