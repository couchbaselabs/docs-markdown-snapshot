---
title: Manage Multi-Factor Authentication (MFA)
description: Couchbase Capella provides the option to enable multi-factor
  authentication (MFA) to further enhance account security.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/organizations/pages/ui-auth/mfa.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:organizations:ui-auth/mfa.adoc[]
---

[View original HTML](/cloud/organizations/ui-auth/mfa.html)

# Manage Multi-Factor Authentication (MFA)

> Couchbase Capella provides the option to enable multi-factor authentication (MFA) to further enhance account security. 

Multi-Factor Authentication (MFA) is a layered approach to account authentication where a user must present two or more credentials to verify their identity. When MFA is activated for your Couchbase Capella account, it requires two forms of credentials to sign in: your password and a time-based one-time password (TOTP). Capella supports the use of authenticator apps to generate and present a TOTP.

## [](#prerequisites)Prerequisites

> [!IMPORTANT]
> If your organization uses federated and single sign-on authentication, your SSO users can’t use Capella’s MFA solution. Instead, they use your Identity Provider’s MFA.

To enable MFA for your Capella account, you need:

* An authenticator app on an iOS or Android-powered device, such as:

  * 1Password
  * Authy
  * LastPass Authenticator
  * Microsoft Authenticator

For more information about what authenticator app to choose, contact your company’s IT or security team.

## [](#turn-on-mfa)Turn on Multi-Factor Authentication for your Account

Each user account in Capella can choose to turn MFA on or off.

To activate MFA:

1. Click your profile in the upper right corner of the Capella UI.
2. Click **My Account**.
3. On the account management page, click **Activate MFA**.
4. Scan the provided QR code with the MFA app on your device.  
A six-digit verification code is shown.
5. Enter the six-digit verification code into Capella.  
Capella activates multi-factor authentication for your account. You now need to use your MFA app to generate a TOTP when signing in to the Capella UI.

## [](#view-multi-factor-authentication-status-by-account)View Multi-Factor Authentication Status by Account

If you are an [Organization Owner](../organization-user-roles.md#organization-role-organization-owner), you can view the MFA status (_Activated_ or _Needs Activation_) for each account in your organization.

1. Navigate to the Multi-Factor Authentication page in Organization Administration:
2. In the navigation breadcrumbs in the Capella UI, click your organization name.
3. Go to **Settings** **MFA**.  
The Multi-Factor Authentication page lists all the user accounts in the current organization, their MFA status, and when they last signed in. Click a user in the list to open their profile page.