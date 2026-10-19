---
title: Authentication
description: To access Operational Insights, administrators and applications
  must be authenticated.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/manage/pages/manage-security/manage-authentication.adoc
  xref: xref:enterprise-analytics:manage:manage-security/manage-authentication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/manage/manage-security/manage-authentication.html)

# Authentication

> To access Operational Insights, administrators and applications must be authenticated. 

To use Operational Insights, authenticate using a username and password. You can validate and manage these credentials with Operational Insights itself, or through 1 of the following methods on a network-accessible directory server:

* Lightweight Directory Access Protocol (LDAP)
* Pluggable Authentication Modules (PAM)

Operational Insights 2.2 and later also supports JSON Web Token (JWT) authentication. JWT allows clients to authenticate using a bearer token issued by a trusted Identity Provider (IdP) — such as Keycloak or Okta — instead of a username and password. See [Configure JWT Authentication](configure-jwt.md).