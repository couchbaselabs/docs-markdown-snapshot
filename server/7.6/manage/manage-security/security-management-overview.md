---
title: Security Management Overview
description: Couchbase Server can be rendered highly secure.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/manage/pages/manage-security/security-management-overview.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/manage/manage-security/security-management-overview.html)

# Security Management Overview

> Couchbase Server can be rendered highly secure. 

## [](#couchbase-server-security)Couchbase Server Security

Couchbase Server can be rendered highly secure. System-areas available to be managed include:

* _Networked access, by administrators, users, and applications_: Can be secured with TLS, using dedicated Couchbase Server-ports. Cipher-suites, TLS levels, and console-access can be individually managed. Networked communications between nodes within the cluster can also be secured: see [Manage Node-to-Node Encryption](../manage-nodes/apply-node-to-node-encryption.md), for details.
* _Authentication_: Can be handled by passing credentials explicitly, or by means of client certificates. _External_ (as well as _Local_) authentication-domains are supported: therefore, authentication-mechanisms based on _Native LDAP_, _saslauthd_, and _PAM_ can be used. For the recommended process, see [Configure LDAP](configure-ldap.md).
* _Authorization_: Couchbase _Role-Based Access Control_ ensures that each authenticated user is checked for the system-defined _roles_ (and, by due association, _privileges_) they have been assigned. This allows access to be granted or denied them, based on the type of system-resource they are trying to access, and the operation they wish to perform. Roles can be assigned by _user_ and by _group_. For details, see [Manage Users, Groups, and Roles](manage-users-and-roles.md).
* _Auditing_: Can be enabled on actions performed on Couchbase Server, so that reviews can occur. See [Manage Auditing](manage-auditing.md),
* _Certificates_: These can be defined and established for the cluster. Additionally, certificates presented by clients attempting server-access can be permitted. See [Manage Certificates](manage-certificates.md).
* _Logs_: These can be _redacted_, ensuring that no private information is shared. Information is provided in [Manage Logging](../manage-logging/manage-logging.md).
* _Sessions_: Can be configured for termination following periods of user-inactivity. This is described in [Manage Sessions](manage-sessions.md).

See the navigation panel at the left, for details of additional management procedures documented in this section.

## [](#security-checklist)Security Checklist

The security checklist below should be reviewed and used in the set-up and maintenance of a Couchbase-Server cluster.

Optionally, the [checklist](../%5Fattachments/manage-security/cb7SecurityChecklist.pdf) can be accessed as a PDF file.

| Access control               | Create unique user accounts for each individual and application that accesses the platform.  Implement Role-Based Access Control and assign roles following a principle of least privilege  Leverage strongest available authentication mechanisms  Ensure secure storage and transfer of credentials or certificates  Implement Multi-Factor Authentication for individual access |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Secure Network Communication | Replace self-signed certificates with external CA certificates  Ensure all applications are using encrypted connections only and block insecure ports  Enforce TLS with ‘strict’ encryption setting to encrypt all network traffic internally and externally.  Only Enable IP Address Families as needed                                                                           |
| Secure Data Storage          | Deploy encryption at rest  Implement (FLE) Field-level Encryption  Configure Secrets Management                                                                                                                                                                                                                                                                                    |
| Limit Data Exposure          | Remove unnecessary services and software  Regularly scan for and protect sensitive data  Control geographic distribution of data  Leverage log redaction when collecting and transferring logs  Deploy a comprehensive DR strategy utilizing offsite backups                                                                                                                       |
| Auditing                     | Enable and configure auditing  Review audit logs manually and programmatically for anomalies                                                                                                                                                                                                                                                                                       |
| Regular Review               | Assess security from core to edge and perform regular security health checks  Review enhancements provided with each new version of the Couchbase Data Platform  Apply upgrades to the Couchbase Data Platform & SDK software, app frameworks, OS, networking infrastructure, etc.                                                                                                 |