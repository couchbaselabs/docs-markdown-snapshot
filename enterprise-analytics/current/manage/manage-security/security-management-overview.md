---
title: Security Management Overview
description: Enterprise Analytics can be rendered highly secure.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/manage/pages/manage-security/security-management-overview.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:enterprise-analytics:manage:manage-security/security-management-overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/manage/manage-security/security-management-overview.html)

# Security Management Overview

> Enterprise Analytics can be rendered highly secure. 

## [](#couchbase-server-security)Enterprise Analytics Security

Enterprise Analytics can be rendered highly secure. System-areas available to be managed include:

* Networked access, by administrators, users, and applications: Can be secured with TLS, using dedicated Enterprise Analytics-ports. Cipher-suites, TLS levels, and console-access can be individually managed. Networked communications between nodes within the cluster can also be secured: see [Manage Node-to-Node Encryption](../manage-nodes/apply-node-to-node-encryption.md), for details.
* Authentication: Can be handled by passing credentials explicitly, by means of client certificates, or by means of JSON Web Tokens (JWT). External (as well as local) authentication domains are supported: authentication mechanisms based on Native LDAP, saslauthd, PAM, and JWT are all available. For LDAP, see [Configure LDAP](configure-ldap.md). For JWT bearer token authentication, see [Configure JWT Authentication](configure-jwt.md).
* Authorization: Use Couchbase's Role-Based Access Control to check each authenticated user for their system-defined roles and associated privileges. Use roles and privileges to grant or deny access to users, based on the type of system-resource they're trying to access, and the operation they want to perform. Roles can be assigned by user and by group. For more information about configuring users, roles, and groups, see [Manage Users, Groups, and Roles](manage-users-and-roles.md).
* Auditing: You can enable auditing for any actions on Enterprise Analytics, so you can review at a later date. See [Manage Auditing](manage-auditing.md),
* Certificates: You can define and establish certificates for your cluster, and permit certificates presented by clients to access your cluster. See [Manage Certificates](manage-certificates.md).
* Logs: Log files can be redacted, ensuring that no private information is shared. For more information about how to configure logging, see [Manage Logging](../manage-logging/manage-logging.md).
* Sessions: You can choose to terminate sessions after a period of user inactivity. This is described in [Manage Sessions](manage-sessions.md).

See the navigation panel at the left, for details of additional management procedures documented in this section.

## [](#security-checklist)Security Checklist

The security checklist below should be reviewed and used in the set-up and maintenance of a Couchbase-Server cluster.

Optionally, the [checklist](../%5Fattachments/manage-security/cb7SecurityChecklist.pdf) can be accessed as a PDF file.

| Access control               | Create unique user accounts for each individual and application that accesses the platform.  Implement Role-Based Access Control and assign roles following a principle of least privilege  Use the strongest available authentication mechanisms  Ensure secure storage and transfer of credentials or certificates  Implement Multi-Factor Authentication for individual access |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Secure Network Communication | Replace self-signed certificates with external CA certificates  Ensure all applications are using encrypted connections only and block insecure ports  Enforce TLS with 'strict' encryption setting to encrypt all network traffic internally and externally.  Only Enable IP Address Families as needed                                                                          |
| Secure Data Storage          | Deploy encryption at rest  Implement (FLE) Field-level Encryption  Configure Secrets Management                                                                                                                                                                                                                                                                                   |
| Limit Data Exposure          | Remove unnecessary services and software  Regularly scan for and protect sensitive data  Control geographic distribution of data  Use log redaction when collecting and transferring logs  Deploy a comprehensive DR strategy utilizing offsite backups                                                                                                                           |
| Auditing                     | Enable and configure auditing  Review audit logs manually and programmatically for anomalies                                                                                                                                                                                                                                                                                      |
| Regular Review               | Assess security from core to edge and perform regular security health checks  Review enhancements provided with each new version of the Couchbase Data Platform  Apply upgrades to the Couchbase Data Platform & SDK software, app frameworks, OS, networking infrastructure, etc.                                                                                                |