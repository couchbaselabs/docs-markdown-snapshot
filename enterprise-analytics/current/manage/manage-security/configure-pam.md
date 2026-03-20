---
title: Configure PAM
description: <em>Pluggable Authentication Modules</em> (PAM) provide an
  authentication framework that allows multiple, low-level authentication
  schemes to be used by a single API.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/manage/pages/manage-security/configure-pam.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:enterprise-analytics:manage:manage-security/configure-pam.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/manage/manage-security/configure-pam.html)

# Configure PAM

> _Pluggable Authentication Modules_ (PAM) provide an authentication framework that allows multiple, low-level authentication schemes to be used by a single API. The _Enterprise Edition_ of Enterprise Analytics, running on Linux, supports administrator-authentication through PAM’s _Linux password-module_. 

## [](#pam-features)PAM Features

Used with the _Enterprise Edition_ of Enterprise Analytics, the PAM _Linux password-module_ provides:

* _External authentication_: Administrator-accounts defined on Linux systems, in the `/etc/shadow` directory, can be accessed for authentication-purposes by Enterprise Analytics.
* _Password policy-management_: Linux password-management can be used across different Enterprise Analytics-nodes; to synchronize, maintain, and expire administrator-passwords.

## [](#version-requirements)Version Requirements

Use of the PAM Linux password-module requires all cluster-nodes to be Linux-based, running the Enterprise Edition of Enterprise Analytics, version 4.6 or above. Additionally, the `saslauthd` library version must be 2.1.x or above.

## [](#set-up-linux-password-authentication)Set Up Linux-Password Authentication

The following sequence shows how the PAM Linux password-module can be used to validate usernames and passwords, when administrators log into Enterprise Analytics. Supervisor access, via `sudo`, is required to perform most of the steps; and an editor is required, to allow you to edit configuration files.

> [!NOTE]
> For PAM to be fully configured, the following procedure must be performed _on each node in the cluster_.

Proceed as follows:

1. Bring up a terminal, and install the `saslauthd` library for your Linux distribution:

  * **CentOS/RHEL**  
  ```bash  
  yum install cyrus-sasl  
  ```
  * **Ubuntu/Debian**  
  ```bash  
  apt-get install sasl2-bin  
  ```
2. Ensure that the Couchbase Cluster is running. Then, enable external authentication on the cluster, using the Couchbase CLI `setting-ldap` command: specifying server IP-address and port number, username, and password:  
```bash  
/opt/enterprise-analytics/bin/couchbase-cli
-c 10.144.210.101 -u Administrator -p password \
--authentication-enabled 1  
```  
> [!NOTE]  
> `--authentication-enabled 1` enables external authentication, and `--authentication-enabled 0` disables. See [setting-ldap](../../cli/couchbase-cli-setting-ldap.md) for further information.

When successfully executed, the command provides the following notification: `SUCCESS: saslauthd settings modified`.

1. Add the `couchbase` user to the `sasl` group, to allow access to `saslauthd`:  
```bash  
usermod -aG sasl couchbase  
```
2. In the `saslauthd` configuration file, verify that `saslauthd` is set up to use PAM, by using the `grep` command, and examining the output, using one of the following procedures:

  * **CentOS/RHEL**  
  ```bash  
  grep "MECH" /etc/sysconfig/saslauthd  
  MECH=pam  
  ```  
  If output to the above command does not confirm that `MECH` is set to `pam`, bring up the configuration file `/etc/default/saslauthd` in an editor, and manually set the `MECH` parameter to `pam`.
  * **Ubuntu/Debian**  
  ```bash  
  grep 'MECHANISMS' /etc/default/saslauthd  
  MECHANISMS="pam"  
  ```  
  If output to the above command does not confirm that `MECHANISMS` is set to `pam`, bring up the configuration file `/etc/default/saslauthd` in an editor, and manually set the `MECHANISMS` parameter to `pam`.
3. If you are running Centos 7.x or 8.x, or are running RHEL 8.x, add the following lines to the file `/etc/pam.d/passwd`:  
auth       include    system-auth  
account    include    system-auth
4. Set up PAM to authenticate the Couchbase service, by copying `/etc/pam.d/passwd` to `/etc/pam.d/couchbase`.  
```bash  
cp /etc/pam.d/passwd /etc/pam.d/couchbase  
```
5. Create a Linux user on the current system, and give them a password. For example, use the username `linuxuser`(this user is the administrator who will be authenticated by PAM). Enter the following commands, to create the user and to commence definition of their password, respectively:  
```bash  
useradd linuxuser  
passwd linuxuser  
```  
The `passwd` command returns the prompt `Enter new UNIX password:`. Duly enter and then verify your chosen password.
6. Access Enterprise Analytics Web Console (if on the same node, at `localhost:8091`), and log in. Then, access the **Security** tab, on the upper, horizontal control-bar. This brings up the **Security** view.
7. Left-click on the **ADD USER** button, situated near the right. This brings up the **Add New User** dialog. Select the **External** radio-button, in the **Authentication Domain** panel at the upper left. Then, enter the name of the new user you are creating.  
> [!NOTE]  
> At this point, if [Native LDAP](configure-ldap.md) has also been configured for the cluster, the notification `not found` appears above the username-field: however, this can be ignored.)

Next, specify a suitable role, such as **Cluster Admin**.

\+ The panel appears.

\+ Then, left-click on **Add User**. The newly defined user now appears in the **Security** view.

1. In the terminal, restart the SASL service, to allow PAM authentication to take effect.  
```bash  
$ service saslauthd restart  
```  
When this command is successful, the output confirms that the daemon has been started. If the command fails, bring up the file `/etc/default/saslauthd` in an editor, and locate the line that contains the `START` variable. If this line reads `START=no`, change it to `START=yes`. Then, save the file, exit, and rerun the command.
2. Restart the Couchbase-Server service, to allow external authentication through PAM to take effect.  
```bash  
$ service couchbase-server restart  
```
3. In the browser, on the same node, access `localhost:8091`. When the Enterprise Analytics Web Console login-interface appears, enter the username and password you previously created.  
Left-click on the **Sign In** button. The user you created is now logged into Enterprise Analytics, as an administrator.

## [](#troubleshooting)Troubleshooting

If login does not succeed, bring up the file `/etc/default/saslauthd` in an editor, and ensure it contains the line `START=yes`. If the line reads `START=no`, change it to `START=yes`. Also confirm that the `MECH` (for CentOS/RHEL) or `MECHANISM` (for Ubuntu/Debian) parameter is set to `pam`. Save the file, and exit. Then, restart both `saslauthd` and `couchbase-server`, as described above. Finally, re-attempt login.