---
title: Security API
description: The REST API supports all aspects of Operational Insights security
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-security.adoc
  xref: xref:enterprise-analytics:reference:rest-security.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-security.html)

# Security API

> The REST API supports all aspects of Operational Insights security 

## [](#apis-in-this-section)APIs in this Section

The Security REST API provides the endpoints for general security, for authentication, and for authorization. For a list of the endpoints, see the tables below.

### [](#general-security)General Security

| HTTP Method | URI                                        | Documented at                                                       |
| ----------- | ------------------------------------------ | ------------------------------------------------------------------- |
| GET         | /whoami                                    | [Who Am I?](rest-whoami.md)                                         |
| GET         | /settings/audit                            | [Configure Auditing](rest-auditing.md)                              |
| POST        | /settings/audit                            | [Configure Auditing](rest-auditing.md)                              |
| GET         | /settings/audit/descriptors                | [Configure Auditing](rest-auditing.md)                              |
| GET         | /settings/audit/nonFilterableDescriptors   | [Configure Auditing](rest-auditing.md)                              |
| GET         | /settings/security                         | [Restrict Node-Addition](rest-specify-node-addition-conventions.md) |
| POST        | /settings/security                         | [Restrict Node-Addition](rest-specify-node-addition-conventions.md) |
| POST        | /clusterInit                               | [Initialize a Cluster](rest-initialize-cluster.md)                  |
| GET         | /settings/security/\[service-name\]        | [Configure On-the-Wire Security](rest-setting-security.md)          |
| POST        | /settings/security/\[service-name\]        | [Configure On-the-Wire Security](rest-setting-security.md)          |
| POST        | /node/controller/rotateInternalCredentials | [Rotate Internal Credentials](rest-rotate-internal-credentials.md)  |
| GET         | /settings/security/responseHeaders         | [Configure HSTS](rest-setting-hsts.md)                              |
| POST        | /settings/security/responseHeaders         | [Configure HSTS](rest-setting-hsts.md)                              |
| DELETE      | /settings/security/responseHeaders         | [Configure HSTS](rest-setting-hsts.md)                              |

### [](#authentication)Authentication

| HTTP Method | URI                                                         | Documented at                                                         |
| ----------- | ----------------------------------------------------------- | --------------------------------------------------------------------- |
| GET         | /settings/ldap                                              | [Configure LDAP](rest-configure-ldap.md#get-settings-ldap)            |
| POST        | /settings/ldap                                              | [Configure LDAP](rest-configure-ldap.md#post-settings-ldap)           |
| GET         | /settings/saml                                              | [Configure SAML](rest-configure-saml.md#get-settings-saml)            |
| POST        | /settings/saml                                              | [Configure SAML](rest-configure-saml.md#post-settings-saml)           |
| GET         | /settings/saslauthdAuth                                     | [Configure saslauthd](rest-configure-saslauthd.md)                    |
| POST        | /settings/saslauthdAuth                                     | [Configure saslauthd](rest-configure-saslauthd.md)                    |
| GET         | /settings/passwordPolicy                                    | [Set Password Policy](rest-set-password-policy.md)                    |
| POST        | /settings/passwordPolicy                                    | [Set Password Policy](rest-set-password-policy.md)                    |
| POST        | /controller/changePassword                                  | [Change Password](rest-set-password.md)                               |
| POST        | /node/controller/loadTrustedCAs                             | [Load Root Certificates](load-trusted-cas.md)                         |
| GET         | /pools/default/trustedCAs                                   | [Get Root Certificates](get-trusted-cas.md)                           |
| DELETE      | /pools/default/trustedCAs/<id>                              | [Delete Root Certificates](delete-trusted-cas.md)                     |
| GET         | /pools/default/certificates                                 | [Retrieve All Node Certificates](retrieve-all-node-certs.md)          |
| POST        | /node/controller/reloadCertificate                          | [Upload and Retrieve Node Certificates](upload-retrieve-node-cert.md) |
| GET         | /pools/default/certificate/node/<ip-address-or-domain-name> | [Upload and Retrieve Node Certificates](upload-retrieve-node-cert.md) |
| POST        | /controller/regenerateCertificate                           | [Regenerate All Certificates](rest-regenerate-all-certs.md)           |

### [](#authorization)Authorization

| HTTP Method | URI                                               | Documented at                                                                       |
| ----------- | ------------------------------------------------- | ----------------------------------------------------------------------------------- |
| GET         | /settings/rbac/roles                              | [List Roles](rbac.md#list-roles)                                                    |
| GET         | /settings/rbac/users                              | [List Current Users and Their Roles](rbac.md#list-current-users-and-their-roles)    |
| POST        | /pools/default/checkPermissions                   | [Check Permissions](rbac.md#check-permissions)                                      |
| GET         | /settings/rbac/groups                             | [List Currently Defined Groups](rbac.md#list-currently-defined-groups)              |
| PUT         | /settings/rbac/users/local/<new-username>         | [Create a Local User](rbac.md#create-a-local-user-and-assign-roles)                 |
| PATCH       | /settings/rbac/users/local/<existing-username>    | [Create a Local User](rbac.md#create-a-local-user-and-assign-roles)                 |
| PUT         | /settings/rbac/users/external/<new-username>      | [Create an External User](rbac.md#create-an-external-user-and-assign-roles)         |
| PUT         | /settings/rbac/groups/<new-groupname>             | [Create a Group](rbac.md#create-a-group-and-assign-it-roles)                        |
| DELETE      | /settings/rbac/users/local/<local-username>       | [Delete Users and Groups](rbac.md#delete-users-and-groups)                          |
| DELETE      | /settings/rbac/users/external/<external-username> | [Delete Users and Groups](rbac.md#delete-users-and-groups)                          |
| DELETE      | /settings/rbac/groups/<groupname>                 | [Delete Users and Groups](rbac.md#delete-users-and-groups)                          |
| GET         | /settings/rbac/backup                             | [Back Up and Restore Users and Groups](rbac.md#backup-and-restore-users-and-groups) |
| PUT         | /settings/rbac/backup                             | [Back Up and Restore Users and Groups](rbac.md#backup-and-restore-users-and-groups) |

### [](#system-secrets)System Secrets

| HTTP Method | URI                                   | Documented at                                                                                                  |
| ----------- | ------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| GET         | /nodes/self/secretsManagement         | [Configuring System Secrets](../manage/manage-security/manage-system-secrets.md#configuring-system-secrets)    |
| POST        | /node/controller/secretsManagement    | [Configuring System Secrets](../manage/manage-security/manage-system-secrets.md#configuring-system-secrets)    |
| POST        | /node/controller/changeMasterPassword | [Changing the Master Password](../manage/manage-security/manage-system-secrets.md#setting-the-master-password) |
| POST        | /node/controller/rotateDataKey        | [Rotating the Data Key](../manage/manage-security/manage-system-secrets.md#password%5Frotation)                |