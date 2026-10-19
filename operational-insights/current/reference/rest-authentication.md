---
title: Authentication API
description: Operational Insights supports authentication via local and external domains.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-authentication.adoc
  xref: xref:enterprise-analytics:reference:rest-authentication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-authentication.html)

# Authentication API

> Operational Insights supports authentication via local and external domains. 

## [](#authenticating-externally)Authenticating Locally and Externally

Users may be given an identity _locally_ on a cluster. This allows their credentials to be maintained and updated on the local cluster. A _password policy_ is enforced for the cluster: the defaults for this policy can be modified. A local user can change their own password.

Enterprises frequently centralize directory services, allowing all user-authentication to be handled by a single server or server-group. LDAP is frequently used in support of such centralization. The authentication handled in this way is therefore _external_ to Operational Insights.

Operational Insights supports external authentication. Users are registered as _external_, for authentication purposes. When such users pass their credentials to Operational Insights, Operational Insights recognizes the user as external, and duly passes the credentials to the external authentication facility: if the authentication succeeds there, Operational Insights is informed, and the user is given appropriate access, based on the roles and privileges on Operational Insights that they have been assigned.

The password policy, and how to change it, is described in [Set Password Policy](rest-set-password-policy.md). For further information about _local_ and _external_ domains, see [Authentication](../manage/manage-security/manage-authentication.md).

### [](#ldap-groups)LDAP Groups

LDAP supports _groups_, of which multiple users can be members. Operational Insights supports the association of LDAP groups with Operational Insights groups: a user successfully authenticated on an LDAP server may have their LDAP group information duly returned to Operational Insights. If Operational Insights has configured an association between one or more of the user's LDAP groups and corresponding groups defined on Operational Insights, the user is assigned the roles and privileges for the corresponding Operational Insights groups.

## [](#external-authentication-configuration-options)Configuration Options

Operational Insights provides a recommended REST method for simple and expedited configuration of LDAP-based authentication. This is described in [Configure LDAP](rest-configure-ldap.md).

Alternatively, a [legacy](rest-configure-saslauthd.md) REST API for establishing SASL administrator credentials can be used. Note that this requires prior, manual set-up of saslauthd for the cluster: see [Configure saslauthd](../manage/manage-security/configure-saslauthd.md).

## [](#apis-in-this-section)APIs in this section

A complete list of APIs described in this section is provided in the table below.

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