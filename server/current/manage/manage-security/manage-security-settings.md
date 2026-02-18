---
title: Manage Security Settings
description: Couchbase Server security-settings can be managed from Couchbase
  Web Console, and by means of the REST API.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/manage/pages/manage-security/manage-security-settings.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/manage/manage-security/manage-security-settings.html)

# Manage Security Settings

> Couchbase Server security-settings can be managed from Couchbase Web Console, and by means of the REST API. 

## [](#couchbase-security-settings)Couchbase Security Settings

The basic settings for Couchbase security, available to _Full_ and _Security_ administrators, allow configuration of the following:

* Users & Groups: Users and groups can be created, given passwords, and assigned roles that allow them to access specific system resources.
* LDAP: Integration with LDAP (Lightweight Directory Access Protocol) for user authentication and management.
* SAML: Integration with SAML (Security Assertion Markup Language) for single sign-on (SSO) authentication.
* Certificates: The Root Certificate for the node, which allows the server to identify itself to clients. Also, has the Client Certificate settings, which determine whether a client can or must present a certificate in order to authenticate with the server.
* Encryption at Rest: Settings that determine how data is encrypted when stored on disk.
* Audit: Settings that determine which system events and user activities are audited.
* Log Redaction: Settings that determine what forms of content are to be considered private, and redacted from system logs.
* Session Timeout: Settings that determine how long a user can be inactive before being logged out of Couchbase Web Console.
* Cluster Encryption: Settings that determine the level of encryption for data transmitted between nodes in the cluster.

These areas are described below.

## [](#access-security-screen)Access the Security Screen

To start managing Couchbase Server security-settings, within Couchbase Web Console, access the **Security** screen, by means of the **Security** tab, on the left-hand navigation bar.

This brings up the **Security** screen, which appears as follows:

![securityView](../_images/manage-security/securityView.png) 

Select each tab to view and manage the corresponding security settings.

The top part of the screen displays status of LDAP, which is useful during external user authentication. See [Authentication Domains](../../learn/security/authentication-domains.md), for an overview.

## [](#users-security-screen-display)Users & Groups

The **Users & Groups** display (shown above) lists users and groups currently registered on the cluster. The display can be toggled, to provide information for either users or groups.

Each user has a **username** and (optionally) a **full name**; and can have one or more **roles** associated with them. These roles are themselves associated with _privileges_ that permit access to specified system-resources. The **auth domain** for each user can be _Local_ or _External_. To add users and, in so doing, assign them roles, administrators use the **ADD USER** button, at the upper right. Additionally, each user can be made a member of a defined _group_.

Each defined group has a **group name** and (optionally) a **description**; and can have one or more **roles** assigned to it. If a user becomes a member of a group, the user inherts all the group’s assigned roles. A group can also be assigned a _mapping_ to an LDAP group that is maintained on a remote, LDAP server. For information on how _Native LDAP Support_ can be used to support mappings, see [Authorization](../../learn/security/authorization-overview.md).

A full account of adding and editing users and groups is provided in [Manage Users, Groups, and Roles](manage-users-and-roles.md).

## [](#root-certificate-security-screen-display)Certificates

This displays a screen featuring two panels. The panel to the left features the _root CA certificates_ that have been defined for the cluster:

![multiCApanelV2](../_images/manage-security/multiCApanelV2.png) 

Initially, before any administrator-driven configuration has occurred, this panel contains a single, system-generated, _self-signed_certificate. To increase system-security, a new X.509 certificate should be created: once this has been done, the new, uploaded certificate is displayed beneath the original, system-generated certificate; as shown here.

See [Configure Server Certificates](configure-server-certificates.md), for further information.

Note that the procedures for securing _Cross Data Center Replication_ (XDCR) may involve use of the root certificate: if so, the certificate can be copied from this screen. See [Secure a Replication](../manage-xdcr/secure-xdcr-replication.md) for details.

The right-hand panel features settings for the cluster’s handling of certificates that are presented by clients attempting access:

![clientCertificateDisplay](../_images/manage-security/clientCertificateDisplay.png) 

The user interface allows the handling of client certificates to be _enabled_, and optionally to be made _mandatory_. Note that such handling is _disabled_ by default. The **Path**, **Prefix**, and **Delimiter**fields allow the specification of which details within the client certificate are to be used by the server for client-identification.

An explanation of how to use this interface is provided in [Enable Client-Certificate Handling](enable-client-certificate-handling.md). A detailed account of establishing client-certificate settings is provided in [Configure Client Certificates](configure-client-certificates.md).

## [](#audit-security-screen-display)Audit

The audit options are displayed, for the cluster and the cluster user activities, as follows:

* **Audit events & write them to a log**: You can enable auditing of specific events, save those audits to a log file, and set the log rotation frequency.
* **User activity**: You can enable tracking of user activity within the cluster.

![auditOptionsDisplay](../_images/manage-security/auditOptionsDisplay.png) 

For more information, see [Manage Auditing](manage-auditing.md).

## [](#log-redaction-security-screen-display)Other Settings

The **Other Settings** panel provides settings for **Log Redaction**, **Session Timeout**, and **Cluster Encryption**.

### [](#log-redaction)**Log Redaction**

This allows specification of whether log files should be _redacted_:

![logRedactionDisplay](../_images/manage-security/logRedactionDisplay.png) 

A redacted log file is one purged of sensitive information: this allows log files to be shared for review purposes, without private data being compromised.

For detailed information, see [Manage Logging](../manage-logging/manage-logging.md).

### [](#session-security-screen-display)Session Timeout

This allows sessions with Couchbase Web Console to be terminated, following a specified period of user-inactivity:

![sessionTimeoutPanel](../_images/manage-security/sessionTimeoutPanel.png) 

For information on how to use, see [Manage Sessions](manage-sessions.md).

### [](#cluster-encryption)Cluster Encryption

The cluster encryption control appears as follows:

![clusterEncryption](../_images/manage-security/clusterEncryption.png) 

The pull-down menu offers three values, which are **control**, **all**, and **strict**. For a full explanation, see [On-the-Wire Security](../../learn/security/on-the-wire-security.md).