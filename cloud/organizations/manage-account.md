---
title: Manage Your Couchbase Capella Account
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/organizations/pages/manage-account.adoc
pubDate: 2026-06-17T06:07:18.814Z
link: xref:cloud:organizations:manage-account.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/organizations/manage-account.html)

# Manage Your Couchbase Capella Account

> Couchbase Capella accounts are independent of organizations. 

Your Couchbase Capella account is your personal account that you use to sign in to the Couchbase Capella UI. Your account can be part of multiple organizations, and you can manage your account settings independently from your organizations.

To manage your Couchbase Capella account settings:

1. Click your initials in the upper-right corner of the Capella UI.
2. Click **My Account** to open your account management page.

In **My Account**, you can:

* [Manage your account's general settings](#manage-general-settings)
* [Manage invitations to Couchbase Capella organizations](#manage-invitations)
* [View the list of organizations where you're a member](#manage-organizations)
* [View the activity log](#view-activity-log)

## [](#manage-general-settings)Manage General Settings

> [!IMPORTANT]
> Users who sign in with SSO cannot change their name, email, password, or activate Multi-Factor Authentication (MFA) settings.

To manage your profile's general settings and information, go to **General**. You can manage the following settings:

* [Profile name](#change-profile-name)
* [Account password](#change-password)
* [Multi-Factor Authentication (MFA) settings](#multi-factor-authentication)
* [Region and time settings](#update-region-time)
* [Email notification settings](#update-notifications)
* [Linking or unlinking your Capella account to a Google or GitHub account](#link-social-account)

### [](#change-profile-name)Change Your Profile Name

To change your account's profile name, go to the **Name** field and enter a new profile name. Click **Save** to save your changes.

### [](#change-password)Change Your Password

To change your password:

1. In **Login Credentials**, click **Reset Password** to manage your password settings.
2. Enter your existing password, and then enter and confirm your new password. Your new password must contain:

  * At least 12 characters
  * Uppercase characters (A-Z)
  * Lowercase characters (a-z)
  * Numbers (0-9)
  * Special characters, such as @, #, or $
3. Click **Change Password** to save your changes.

> [!NOTE]
> You can also reset your password by selecting **Forgot Password** from the log-in screen, which will send you a recovery email. You can only receive 1 password reset email per minute.

### [](#multi-factor-authentication)Activate Multi-Factor Authentication (MFA)

> [!IMPORTANT]
> Users who sign in with SSO cannot use Capella's multi-factor authentication (MFA) solution. Instead, they use the configured identity provider's MFA.

To activate MFA for your Capella account, go to the **Multi-Factor Authentication (MFA)** field and click **Activate MFA**.

For more information about activating MFA for your Capella account, see [Manage Multi-Factor Authentication (MFA)](ui-auth/mfa.md).

### [](#update-region-time)Update Region and Time

To update the region and time:

1. Click **Region** and select the part of the world you live in.
2. Click **Timezone** and select the time relative to where you are within your geographical region.
3. Click **Save** to save your changes.

### [](#update-notifications)Enable Email Notifications

You can enable email notifications to receive email alerts from all clusters in projects where you have a [project role](../projects/project-roles.md).

To enable email notifications, select **Receive email notifications** and click **Save** to save your changes.

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
> If Multi-Factor Authentication (MFA) is on for your Capella account, Capella keeps this, and you'll need your MFA time-based one-time password (TOTP) to sign in to your account after unlinking from a Google or GitHub account.
3. Click **Unlink from Google** or **Unlink from GitHub**.  
The next time you sign in, you must use your email address and the new password that you set.

## [](#access-invites)Manage Invitations

To view and accept your new invitations to organizations and projects, go to **Invitations**.

For more information about sending invitations, see [Organization Users](organizations.md#users).

## [](#access-organizations)Manage Organizations

To view a list of the organizations where you're a member, go to **Organizations**. Click on the name of an organization to open its **Organization** page, where you can make changes relative to your user permissions.

For more information about Organizations, see [Organizations and Organization Users Overview](organizations.md).

## [](#activity-log)View Activity Log

Go to **Activity Log** to view your user activity logs. The Activity Log provides you with insight into user actions and cluster activity.

For more information, see [View Activity Logs](../clusters/monitoring/activity-log.md).