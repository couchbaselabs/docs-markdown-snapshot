---
title: Manage Authentication
description: To access Enterprise Analytics, administrators and applications
  must be authenticated.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/manage/pages/manage-security/manage-authentication.adoc
  xref: xref:enterprise-analytics:manage:manage-security/manage-authentication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/manage/manage-security/manage-authentication.html)

# Manage Authentication

> To access Enterprise Analytics, administrators and applications must be authenticated. 

To use Enterprise Analytics, authenticate using a username and password. You can validate and manage these credentials with Enterprise Analytics itself, or through 1 of the following methods on a network-accessible directory server:

* Lightweight Directory Access Protocol (LDAP)
* Pluggable Authentication Modules (PAM)

Enterprise Analytics 2.2 and later also supports JSON Web Token (JWT) authentication. JWT allows clients to authenticate using a bearer token issued by a trusted Identity Provider (IdP) — such as Keycloak or Okta — instead of a username and password. See [Configure JWT Authentication](configure-jwt.md).