---
title: Manage Security Settings
description: Enterprise Analytics security-settings can be managed from
  Couchbase Web Console, and by means of the REST API.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/manage/pages/manage-security/manage-security-settings.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:2.0@enterprise-analytics:manage:manage-security/manage-security-settings.adoc[]
---

[View original HTML](/enterprise-analytics/2.0/manage/manage-security/manage-security-settings.html)

# Manage Security Settings

> Enterprise Analytics security-settings can be managed from Couchbase Web Console, and by means of the REST API. 

## [](#couchbase-security-settings)Couchbase Security Settings

The basic settings for Couchbase security, available to _Full_ and _Security_ administrators, allow configuration of the following:

* _Users & Groups_: Users and groups can be created, given passwords, and assigned roles that allow them to access specific system resources.
* The _Root Certificate_ for the node, which allows the server to identify itself to clients.
* _Client Certificate_ settings, which determine whether a client can or must present a certificate in order to authenticate with the server.
* _Audit_ settings, determining which system events are audited.
* _Log Redaction_ settings, determining what forms of content are to be considered private, and redacted from system logs.
* _Session_ management setting, whereby users are logged out of Enterprise Analytics Web Console after a specified period of inactivity.

These areas are described below.

## [](#access-security-screen)Access the Security Screen

To start managing Enterprise Analytics security-settings, within Enterprise Analytics Web Console, access the **Security** screen, by means of the **Security** tab, on the left-hand navigation bar.

This brings up the **Security** screen. It features a horizontal control-bar with tabs for **Users & Groups**, **Certificates**, **Audit**, **Log Redaction**, and **Other Settings**. To display the corresponding screen-content for each, left-click on the tab.

The upper area of the screen displays notices regarding the enablement-status of _LDAP_, which can be used in support of _external_ user-authentication. See [Authentication Domains](../../../../server/current/learn/security/authentication-domains.md), for an overview.

## [](#users-security-screen-display)Users & Groups

The **Users & Groups** display (shown above) lists users and groups currently registered on the cluster. The display can be toggled, to provide information for either users or groups.

Each user has a **username** and (optionally) a **full name**; and can have one or more **roles** associated with them. These roles are themselves associated with _privileges_ that permit access to specified system-resources. The **auth domain** for each user can be _Local_ or _External_. To add users and, in so doing, assign them roles, administrators use the **ADD USER** button, at the upper right. Additionally, each user can be made a member of a defined _group_.

Each defined group has a **group name** and (optionally) a **description**; and can have one or more **roles** assigned to it. If a user becomes a member of a group, the user inherts all the group’s assigned roles. A group can also be assigned a _mapping_ to an LDAP group that is maintained on a remote, LDAP server. For information about how _Native LDAP Support_ can be used to support mappings, see [Authorization](../../../../server/current/learn/security/authorization-overview.md).

A full account of adding and editing users and groups is provided in [Manage Users, Groups, and Roles](manage-users-and-roles.md).

## [](#ldap)LDAP

The **LDAP** section of the **Security** screen provides a toggle to enable or disable LDAP support. When enabled, the _Native LDAP Support_ feature allows users to authenticate with Enterprise Analytics using credentials stored in an external LDAP server.

For more information, see [Configure LDAP](configure-ldap.md).

## [](#saml)SAML

The **SAML** section of the **Security** screen provides a toggle to enable or disable SAML support. When enabled, the _SAML_ feature allows users to authenticate with Enterprise Analytics using credentials stored in an external SAML Identity Provider (IdP).

For more information, see [Configure SAML](configure-saml.md).

## [](#root-certificate-security-screen-display)Certificates

This displays a screen featuring two panels. The panel to the left features the _root CA certificates_ that have been defined for the cluster.

Initially, before any administrator-driven configuration has occurred, this panel contains a single, system-generated, _self-signed_certificate. To increase system-security, a new X.509 certificate should be created. Once this has been done, the new, uploaded certificate is displayed beneath the original, system-generated certificate as shown here.

See [Configure Server Certificates](configure-server-certificates.md), for further information.

The right-hand panel features settings for the cluster’s handling of certificates that are presented by clients attempting access.

The user interface allows the handling of client certificates to be _enabled_, and optionally to be made _mandatory_. Note that such handling is _disabled_ by default. The **Path**, **Prefix**, and **Delimiter**fields allow the specification of which details within the client certificate are to be used by the server for client-identification.

An explanation of how to use this interface is provided in [Enable Client-Certificate Handling](enable-client-certificate-handling.md). A detailed account of establishing client-certificate settings is provided in [Configure Client Certificates](configure-client-certificates.md).

## [](#audit-security-screen-display)Audit

This displays the _audit_ options for the cluster.

The options permit selection of the directory within which the audit log file is to be saved, and the frequency with which it will be _rotated_. Specific events can also be included in the audit process, or excluded from it.

For further information, see [Manage Auditing](manage-auditing.md).

## [](#log-redaction-security-screen-display)Other Settings

The **Other Settings** panel provides settings for **Log Redaction**, **Session Timeout**, and **Cluster Encryption**.

### [](#log-redaction)**Log Redaction**

This allows specification of whether log files should be _redacted_.

A redacted log file is one purged of sensitive information: this allows log files to be shared for review purposes, without private data being compromised.

For detailed information, see [Manage Logging](../manage-logging/manage-logging.md).

### [](#session-security-screen-display)Session Timeout

This allows sessions with Enterprise Analytics Web Console to be terminated, following a specified period of user-inactivity. The UI provides a field to enter the timeout duration in minutes.

For information about how to use, see [Manage Sessions](manage-sessions.md).

### [](#cluster-encryption)Cluster Encryption

The cluster encryption control provides a pull-down menu to select the encryption level.

The pull-down menu offers three values, which are **control**, **all**, and **strict**. For a full explanation, see [On-the-Wire Security](../../../../server/current/learn/security/on-the-wire-security.md).