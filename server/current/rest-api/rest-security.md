---
title: Security API
description: The REST API supports all aspects of Couchbase-Server security
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/rest-security.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:rest-api:rest-security.adoc[]
---

[View original HTML](/server/current/rest-api/rest-security.html)

# Security API

> The REST API supports all aspects of Couchbase-Server security 

## [](#apis-in-this-section)APIs in this Section

The Security REST API provides the endpoints for general security, for authentication, and for authorization. For a list of the endpoints, see the tables below.

### [](#general-security)General Security

| HTTP Method | URI                                        | Documented at                                                       |
| ----------- | ------------------------------------------ | ------------------------------------------------------------------- |
| GET         | ./whoami                                   | [Who Am I?](rest-whoami.md)                                         |
| GET         | /settings/audit                            | [Configure Auditing](rest-auditing.md)                              |
| POST        | /settings/audit                            | [Configure Auditing](rest-auditing.md)                              |
| GET         | /settings/audit/descriptors                | [Configure Auditing](rest-auditing.md)                              |
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
| GET         | /settings/ldap                                              | [Configure LDAP](rest-configure-ldap.md#get-settingsldap)             |
| POST        | /settings/ldap                                              | [Configure LDAP](rest-configure-ldap.md#post-settingsldap)            |
| GET         | /settings/saml                                              | [Configure SAML](rest-configure-saml.md#get-settingssaml)             |
| POST        | /settings/saml                                              | [Configure SAML](rest-configure-saml.md#post-settingssaml)            |
| GET         | /settings/saslauthdAuth                                     | [Configure saslauthd](rest-configure-saslauthd.md)                    |
| POST        | /settings/saslauthdAuth                                     | [Configure saslauthd](rest-configure-saslauthd.md)                    |
| GET         | /settings/passwordPolicy                                    | [Set Password Policy](rest-set-password-policy.md)                    |
| POST        | /settings/passwordPolicy                                    | [Set Password Policy](rest-set-password-policy.md)                    |
| POST        | /controller/changePassword                                  | [Change Password](rest-set-password.md)                               |
| POST        | /node/controller/loadTrustedCAs                             | [Load Root Certificates](load-trusted-cas.md)                         |
| GET         | /node/controller/loadTrustedCAs                             | [Get Root Certificates](get-trusted-cas.md)                           |
| DELETE      | /pools/default/trustedCAs/<id>                              | [Delete Root Certificates](delete-trusted-cas.md)                     |
| GET         | /pools/default/certificates                                 | [Retrieve All Node Certificates](retrieve-all-node-certs.md)          |
| POST        | /node/controller/reloadCertificate                          | [Upload and Retrieve Node Certificates](upload-retrieve-node-cert.md) |
| GET         | /pools/default/certificate/node/<ip-address-or-domain-name> | [Upload and Retrieve Node Certificates](upload-retrieve-node-cert.md) |
| POST        | /controller/regenerateCertificate                           | [Regenerate All Certificates](rest-regenerate-all-certs.md)           |

### [](#authorization)Authorization

| HTTP Method | URI                                               | Documented at                                                                    |
| ----------- | ------------------------------------------------- | -------------------------------------------------------------------------------- |
| GET         | /settings/rbac/roles                              | [List Roles](rbac.md#list-roles)                                                 |
| GET         | /settings/rbac/users                              | [List Current Users and Their Roles](rbac.md#list-current-users-and-their-roles) |
| POST        | /pools/default/checkPermissions                   | [Check Permissions](rbac.md#check-permissions)                                   |
| GET         | /settings/rbac/groups                             | [List Currently Defined Groups](rbac.md#list-currently-defined-groups)           |
| PUT         | /settings/rbac/users/local/<new-username>         | [Create a Local User](rbac.md#create-a-local-user-and-assign-roles)              |
| PATCH       | /settings/rbac/users/local/<existing-username>    | [Create a Local User](rbac.md#create-a-local-user-and-assign-roles)              |
| PUT         | /settings/rbac/users/external/<new-username>      | [Create an External User](rbac.md#create-an-external-user-and-assign-roles)      |
| PUT         | /settings/rbac/groups/<new-groupname>             | [Create a Group](rbac.md#create-a-group-and-assign-it-roles)                     |
| DELETE      | /settings/rbac/users/local/<local-username>       | [Delete Users and Groups](rbac.md#delete-users-and-groups)                       |
| DELETE      | /settings/rbac/users/external/<external-username> | [Delete Users and Groups](rbac.md#delete-users-and-groups)                       |
| DELETE      | /settings/rbac/groups/<groupname>                 | [Delete Users and Groups](rbac.md#delete-users-and-groups)                       |

### [](#system-secrets)System Secrets

| HTTP Method | URI                                   | Documented at                                                 |
| ----------- | ------------------------------------- | ------------------------------------------------------------- |
| GET         | /nodes/self/secretsManagement         | [Configuring System Secrets](system-secrets-configuration.md) |
| POST        | /node/controller/secretsManagement    | [Configuring System Secrets](system-secrets-configuration.md) |
| POST        | /node/controller/changeMasterPassword | [Changing the Master Password](change-master-password.md)     |
| POST        | /node/controller/rotateDataKey        | [Rotating the Data Key](rotate-data-key.md)                   |