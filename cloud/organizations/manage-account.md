---
title: Manage Your Couchbase Capella Account
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/organizations/pages/manage-account.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:organizations:manage-account.adoc[]
---

[View original HTML](/cloud/organizations/manage-account.html)

# Manage Your Couchbase Capella Account

> Couchbase Capella accounts are independent of organizations. 

## [](#access-your-account-management-settings)Access Your Account Management Settings

To manage your Couchbase Capella account settings, click your initials in the upper-right corner of the Capella UI. In the dropdown menu that appears, click **My Account** to open your account management page.

![The Dashboard screen highlighting the drop-down that appears after clicking your name in the upper-right of the UI.](_images/select-account-settings.png) 

## [](#manage-general-settings)Manage General Settings

In the account management menu, the **General** option offers settings to update your profile information, password, region and timezone, and enable notifications. Make sure you save any changes.

> [!IMPORTANT]
> Users who sign in with SSO cannot change their name, email, password, or activate Multi-Factor Authentication (MFA) settings.

![The General settings screen.](_images/general.png) 

> [!NOTE]
> You can also reset your password by selecting **Forgot Password** from the log-in screen, which will send you a recovery email. No matter how many times you click **Forgot Password**, you will only receive one password reset email per minute.

To activate MFA, see [Manage MFA](ui-auth/mfa.md).

### [](#link-social-account)Link Your Capella Account to a Google or GitHub Account

You can sign in to your existing Capella account using a Google account or GitHub account that has the same email as your Capella account.

To link an existing Capella account to a Google or GitHub Account, go to the [Couchbase Capella Sign-in page](https://cloud.couchbase.com/sign-up).

* GitHub Account
* Google Account

Prerequisites

* In GitHub, make sure that your primary email address is the same as the email address that your Capella account uses.
* In GitHub, make sure that your primary email address is [verified](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/verifying-your-email-address).
* In GitHub, make sure your primary email address is public.  
To set a public GitHub email address:

  1. Sign in to GitHub, and on your profile menu, click **Settings**.  
  Your Public profile page should display.
  2. In the navigation pane, click **Emails**.
  3. Clear **Keep my email addresses private**.
  4. Return to the **Public Profile** page and select your primary email address from the **Public email** list.

    1. Click **Update profile** to save the changes.

Procedure

1. Click **GitHub**.
2. Follow the GitHub prompts to sign in to your GitHub account.
3. Click **Link GitHub Account**
4. Enter your Capella account password, and if you have Multi-Factor Authentication (MFA) turned on, a MFA time-based one-time password (TOTP).
5. Click **Verify and Link**.

Prerequisites

* In Google, make sure your primary email address is the same as the email address that your Capella account uses.
* If your Google account uses a non-Google email, make sure that your account is [verified](https://support.google.com/accounts/answer/63950?sjid=12585803331733388295-NA).

Procedure

1. Click **Google**.
2. Follow the Google prompts to sign in to your Google account.
3. Click **Link Google Account**
4. Enter your Capella account password, and if you have Multi-Factor Authentication (MFA) turned on, a MFA time-based one-time password (TOTP).
5. Click **Verify and Link**.

### [](#unlink-your-capella-account-from-a-google-or-github-account)Unlink Your Capella Account from a Google or GitHub Account

To unlink your Couchbase Capella account from a Google or GitHub account:

1. On your profile page, click **Unlink from Google** or **Unlink from GitHub**.
2. Enter a new password for your Capella account and confirm it.  
> [!NOTE]  
> If Multi-Factor Authentication (MFA) is on for your Capella account, Capella keeps this, and you’ll need your MFA time-based one-time password (TOTP) to sign in to your account after unlinking from a Google or GitHub account.
3. Click **Unlink from Google** or **Unlink from Google**.  
The next time you sign in, you must use your email address and the new password that you set.

### [](#update-notifications)Update Notifications

Click **General** on the account management menu to change your notification settings.

Check the **Receive Email Notifications** check box if you want to receive notifications concerning activity within your account. Clear if you don’t want to receive notifications.

Click **Save** to apply your changes.

## [](#access-invites)Manage Invitations

Click **Invitations** on the **Account Management** menu to view and accept your new invitations to organizations and projects.

## [](#access-organizations)Manage Organizations

In the account management menu, click **Organizations** to view and access your organizations.

Click on the name of an organization to open its **Organization** page, where you can make changes relative to your user permissions.

## [](#activity-log)View Activity Log

In the account management menu, click **Activity Log** to access your user activity logs.

The [Activity Log](../clusters/monitoring/activity-log.md) is where you can view the activity in the organizations and the projects you’re involved. This tool displays a summary of all events in a chosen timespan.

The Activity Log provides you with insight into user actions and cluster activity. It can also give details and actionable recommendations to help resolve cluster issues before they impact downstream applications.