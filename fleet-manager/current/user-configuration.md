---
title: User Configuration
description: Fleet Manager maintains its own list of users who can access the telemetry.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Fleet Manager
    version: "1.0"
  topic_type: how-to
antora:
  editUrl: https://github.com/couchbaselabs/docs-fleetmanager/edit/main/modules/ROOT/pages/user-configuration.adoc
  xref: xref:fleet-manager::user-configuration.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/fleet-manager/current/user-configuration.html)

# User Configuration

> Fleet Manager maintains its own list of users who can access the telemetry. This list can be set up directly within Fleet Manager or configured through LDAP. 

> [!NOTE]
> You can only see the User Configuration page if you have administrative access to Fleet Manager.

## [](#managing-users-in-fleet-manager)Managing Users in Fleet Manager

1. Sign in to Fleet Manager as an administrator.  
![initial sign in](_images/initial-sign-in.png)  
Figure 1\. Sign-in screen
2. Select **Users** from the side menu.  
![user list](_images/user-list.png)  
Figure 2\. User list
3. Click the **\+ Add User** button.  
![add user](_images/add-user.png)  
Figure 3\. Add user
4. For the `Identity Source` you can select `Local Account` which is managed by Fleet Manager, or your own `LDAP`\[[1](#%5Ffootnotedef%5F1 "View footnote.")\] service. Make sure that you have selected `Local Account`.  
> [!NOTE]  
> If you want to use your LDAP service to manage Fleet Manager users, then see the [Managing Users through LDAP](#manage-using-ldap) section below.
5. Enter a name for the new user (Make sure that the name is unique to your Fleet Manager installation.)
6. Enter a password for the new user. (Fleet Manager requests a new password when the new user logs on for the first time.) The new password must contain:

  * Twelve or more characters.
  * At least 1 upper case character.
  * At least 1 lower case character.
  * At least 1 numeric character (0–9)
  * At least 1 special character (!@#$%^&\*)
7. Select whether the user can access Fleet Manager as a `Viewer` (a user who's not permitted to change Fleet Manager's settings) or an `Admin` (a user who can change Fleet Manager's setting, including adding additional users.)

## [](#manage-using-ldap)Managing Users through LDAP

Fleet Manager supports LDAP, meaning that you can manage your Fleet Manager users through your existing LDAP directory.

1. Sign in to Fleet Manager as an administrator.
2. Select **Users** from the side menu.
3. Click on the **Configure LDAP** button.
4. You're now presented with the configuration screen for your LDAP service:  
![configure LDAP](_images/configure-LDAP.png)  
Figure 4\. LDAP configuration
5. Make sure that `Enable LDAP user authentication` is selected.
6. Fill in the LDAP hostname or IP address for your LDAP service. (You may need to ask your systems administrator for this information.)

---

[1](#%5Ffootnoteref%5F1). Lightweight Directory Access Protocol