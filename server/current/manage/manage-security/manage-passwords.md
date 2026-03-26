---
title: Manage Passwords
description: Couchbase Server lets you manage passwords for local users, and
  enforce password policies.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/manage/pages/manage-security/manage-passwords.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:manage:manage-security/manage-passwords.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/manage/manage-security/manage-passwords.html)

# Manage Passwords

> Couchbase Server lets you manage passwords for local users, and enforce password policies. 

Couchbase Server manages passwords for users in the local domain when using password authentication. The administrator, who installs and configures Couchbase Server, can create, reset, and enforce password policies for these accounts through the Web UI, CLI, or REST API. Local user accounts also support additional security controls such as forced password changes.

External authentication systems such as LDAP or SAML manage user credentials in the external domain. Couchbase Server relies on these systems to verify user identity, which means that password creation, storage, and policy enforcement occur outside of Couchbase. This separation allows organizations to centralize identity management, apply consistent authentication policies across applications, and reduce administrative overhead.

## [](#user-password-changes)User Password Changes

Local users and external users can change their own passwords.

### [](#password-changes-for-local-users)Password Changes for Local Users

Users defined in the local domain can change their own passwords in the following ways through Couchbase Server:

* On-demand.
* When prompted by the administrator.

A local user can change their password from the following interfaces:

* **Couchbase Web Console/Web UI**: The local users with the Couchbase Web Console UI access can sign in to their account and change their password. For more information about changing password on-demand from the UI, see [Change Password On-demand from the UI](#change-password-on-demand-from-ui).  
An administrator can enforce a local user, existing or new, to change their password at the next login. For more information about changing password, prompted by administrator during a login, from the UI, see [Change Password When Prompted](#change-password-prompted-by-admin).
* **CLI**: The local users can change their password, either on-demand or when prompted by administrator, by using the `couchbase-cli user-change-password` command. For more information about changing password using the CLI, see [Change Password On-demand Using the CLI](#change-password-on-demand-using-cli).
* **REST API**: The local users can change their password, either on-demand or when prompted by administrator, by calling the `/controller/changePassword` endpoint. For more information about changing password using the REST API, see [Change Password On-demand Using the REST API](#change-password-on-demand-using-api).

This flexibility allows local users to manage their credentials without administrator involvement, which reduces administrative workload, and improves security by ensuring that only the user knows their active password. In addition, Couchbase Server can enforce policies such as forced password changes to improve security for local accounts.

### [](#password-changes-for-external-users)Password Changes for External Users

External domain users can change their passwords through their identity provider (IdP) or authentication system.

* Couchbase Server does not store or manage external user passwords.
* External users must use external authentication systems such as LDAP or SAML to change their passwords.
* After changing the password in the IdP, external users must use the new password to access Couchbase.

## [](#administrative-password-controls)Administrative Password Controls

Administrators can set initial passwords for users when creating accounts in the local domain. They can also change passwords for existing users through the Web UI, CLI, or REST API, ensuring that accounts remain secure if credentials are compromised. In addition, administrators can force a user to change their password at the next login, which is useful when assigning temporary passwords or when stronger security is required.

This feature ensures that users set their own private password as soon as possible.

> [!NOTE]
> External users must use external authentication systems such as LDAP or SAML to change their passwords.

### [](#reset-password)Reset Passwords for Existing Users

You can reset any local user's password associated with your cluster.

> [!NOTE]
> You cannot reset the password for external domain user accounts. The **Reset Password** button appears on the **Users** section only if the user is locally defined.

To reset a local user's password, do the following:

1. On the **Security** screen, select **Users & Groups**, and then select **Users**.  
![userSecurityRowClicked](../_images/manage-security/userSecurityRowClicked.png)
2. Select the user account from the list for which you want to reset the password and select **Reset Password** associated with that user. The **Reset Password** dialog is displayed.  
![resetPassword](../_images/manage-security/resetPassword.png)
3. In the **Reset Password** dialog, enter the new password for the user in the **New Password** field and re-enter to confirm the password in the **Confirm Password** field.
4. Select **Save** to save the password changes.

The local user's password is reset.

### [](#set-initial-password)Set Initial Password for a New User

As an administrator, you can set an initial password for a new local user, during the user creation process. The user can continue to use this password until they change it.

You can set the first password using the UI, CLI, or REST API.

#### [](#set-initial-password-ui)Set Initial Password for a New User from the UI

To set an initial password for a new user from the UI, do the following:

1. On the **Security** screen, select **Users & Groups**, and then select **Users**.
2. Select **Add User** to create a new user.
3. In the **Add New User** dialog, enter the following user's details:

  * Enter the **Username**.
  * Enter a temporary password in the **Password** field and re-enter it in the **Verify Password** field.
4. Select the necessary user roles and groups. For more information, see [Add a Locally Authenticated User](manage-users-and-roles.md#add-a-locally-authenticated-user).
5. Select **Add User** to create the user with an initial password.

The local user can then log in with the initial password when prompted to change it upon first login.

#### [](#set-initial-password-for-a-new-user-using-the-cli)Set Initial Password for a New User Using the CLI

As an administrator, you can use the command `couchbase-cli user-manage` with the arguments `--rbac-username` and `--rbac-password` to set an initial password for a new local user using the CLI.

Follow one of the procedures in the [Manage Local Users with the CLI](manage-users-and-roles.md#create-local-users-with-the-cli), as necessary.

See the following example:

/opt/couchbase/bin/couchbase-cli user-manage \
--cluster http://10.144.210.101 \
--username Administrator \
--password password \
--set \
--rbac-username dgreen \
--rbac-password firstpassword \
--roles cluster_admin \
--auth-domain local

The command sets the initial password to `firstpassword` for the new local user `dgreen`.

#### [](#set-initial-password-for-a-new-user-using-the-rest-api)Set Initial Password for a New User Using the REST API

As an administrator, you can use the method and URI `PUT /settings/rbac/users/local/<username>` with the argument `-d password` to set an initial password for a new local user using the REST API.

Follow one of the procedures in the [Manage Local Users Using the REST API](manage-users-and-roles.md#manage-local-users-using-api), as necessary.

See the following example:

curl -v -X  PUT -u Administrator:password \
http://10.143.192.101:8091/settings/rbac/users/local/dgreen \
-d password=firstpassword \
-d roles=cluster_admin \

The API request sets the initial password to `firstpassword` for the new local user `dgreen`.

### [](#force-password-update)Force Password Update

As an administrator, you can force a password update for any local user, associated with your cluster, in the following ways:

* When creating a local user, set a temporary initial password, and force a password change at their first login.
* For an existing user, force a password change at their next login.

After authentication, the Couchbase Web Console UI prompts the user to set a new password.

> [!IMPORTANT]
> Users can proceed to use Couchbase Server only after they change their password.

#### [](#create-temporary-password)Create a Temporary Password for a New User

As an administrator, you can create a temporary password for a new local user during the user creation process. Then you can force the user to change their password at the first login.

Couchbase Server allows the new user to authenticate only after changing their temporary password.

##### [](#create-a-temporary-password-for-a-new-user-from-the-ui)Create a Temporary Password for a New User from the UI

As an administrator, to force a new user to change their password during their first login, do the following:

1. Begin by following steps from the section [Set Initial Password for a New User](#set-initial-password).
2. In the Force Password Update panel, enable **User must change password at next logon**.
3. Select **Add User** to save the details.

When the local user logs in for the first time, the system prompts them to change their temporary password. For more information, see [Change Password When Prompted](#change-password-prompted-by-admin).

##### [](#force-new-user-to-change-password-api)Create a Temporary Password for a New User Using the REST API

As an administrator, you can use the method and URI `PUT /settings/rbac/users/local/<new-username>` with the attribute `temporaryPassword=true` to create a local user and force them to change their password at the first login, using the REST API.

See the following example:

curl -v -X  PUT -u Administrator:password \
http://10.143.192.101:8091/settings/rbac/users/local/dgreen \
-d password=firstpassword \
-d roles=cluster_admin \
-d temporaryPassword=true

The API request sets the temporary password to `firstpassword` for the new local user `dgreen` and prompts them to change their password at the first login.

#### [](#force-password-update-existing-users)Force Existing Users to Change Passwords

As an administrator, you can force an existing user to change their password at their next login.

Couchbase Server allows the user to authenticate only after changing their password.

##### [](#force-existing-users-to-change-passwords-from-the-ui)Force Existing Users to Change Passwords from the UI

As an administrator, to force existing users to change their passwords, do the following:

1. On the **Security** screen, select **Users & Groups**, and then select **Users**.
2. Select the local user account from the list for which you want to force a password change and select **Edit**.
3. In the **Edit User** dialog, in the Force Password Update section, enable **User must change password at next logon**.  
> [!NOTE]  
> You cannot undo this setting once set from the Web UI. You can undo this setting only via the REST API.
4. Select **Save Changes**.

The system prompts the user to change their password during their next login. For more information, see [Change Password When Prompted](#change-password-prompted-by-admin).

##### [](#force-existing-users-to-change-password-api)Force Existing Users to Change Passwords using the REST API

This section is similar to [Create a Temporary Password for a New User Using the REST API](#force-new-user-to-change-password-api). As an administrator, you can use the method and URI `PUT /settings/rbac/users/local/<username>` with the attribute `temporaryPassword=true` to force an existing local user to change their password at the next login, using the REST API.

See the following example:

curl -v -X  PUT -u Administrator:password \
http://10.143.192.101:8091/settings/rbac/users/local/dgreen \
-d password=nextpassword \
-d roles=cluster_admin \
-d temporaryPassword=true

The API request sets the new password to `nextpassword` for the existing local user `dgreen` and prompts them to change their password at the first login.

> [!NOTE]
> You can set the attribute `temporaryPassword=false` to undo this setting; to cancel the forcing of password change on a user.

## [](#local-user-password-changes)Local User Password Changes

Local domain users can manage their own passwords, including changing and resetting them as needed. In this scenario, they do not have to rely on administrators.

However, administrators can enforce password policies and restrictions on local user accounts to make sure of the security compliance.

### [](#change-password-on-demand)Change Password On-demand

Local users can change their passwords whenever needed using the UI, CLI, or REST API.

#### [](#change-password-on-demand-from-ui)Change Password On-demand from the UI

As a local user, to change the password whenever needed, do the following:

1. Log in to the Couchbase Web Console UI.
2. Select your username on the top-right corner and select **Change Password**.
3. In the **Change Password** dialog, enter the current password in the **Current Password** field, and then enter the new password in the **New Password** field and re-enter it in the **Confirm Password** field.
4. Select **Save** to save the password changes.

#### [](#change-password-on-demand-using-cli)Change Password On-demand Using the CLI

Local users can change their passwords using the Couchbase CLI command, [user-change-password](../../cli/cbcli/couchbase-cli-user-change-password.md).

The command is as follows:

/opt/couchbase/bin/couchbase-cli user-change-password --cluster http://10.144.210.101 \
--username <username> \
--password <old-password> \
--new-password <new-password>

#### [](#change-password-on-demand-using-api)Change Password On-demand Using the REST API

Local users can change their passwords using the Couchbase REST API method and URI `POST /controller/changePassword` as follows:

curl -X POST http://<ip-address-or-domain-name>:8091/controller/changePassword
  -u <username>:<password>
  -d <new-password>

An example command to change the password using the REST API is as follows:

curl -X POST http://localhost:8091/controller/changePassword \
-u localuser:password \
-d password=localpassword

Successful call returns `200 OK` and the local user password is changed.

### [](#change-password-prompted-by-admin)Change Password When Prompted

An administrator can force a password change for a local user.

To change your password when prompted at the login screen, whether you're a new user or an existing user, do the following:

1. Open the Couchbase Web Console UI.
2. Enter your temporary password if you're a new user or current password if you're an existing user. You're redirected to the **Provide New Password** dialog.
3. Enter the new password in the **New Password** field and re-enter it in the **Confirm Password** field.
4. Select **Change Password** to save the new password.

For more information, see [Password Changes for Local Users](#password-changes-for-local-users) and [Force Existing Users to Change Passwords](#force-password-update-existing-users).