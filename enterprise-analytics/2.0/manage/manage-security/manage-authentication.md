---
title: Manage Authentication
description: To access Enterprise Analytics, administrators and applications
  must be authenticated.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/manage/pages/manage-security/manage-authentication.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.0@enterprise-analytics:manage:manage-security/manage-authentication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/manage/manage-security/manage-authentication.html)

# Manage Authentication

> To access Enterprise Analytics, administrators and applications must be authenticated. _Authentication_ is a process for identifying a user who is attempting to access a system. 

## [](#passing-credentials)Passing Credentials

Couchbase-Server authentication relies on _credentials_, which must be passed into the system by the user who is attempting access. Credentials can be entered manually, or passed into the system by an application. The credentials passed must match ones already stored and accessible by the system: if a match is achieved, the user is thereby recognized, and so _may_ be granted access. If no match is achieved, the user is denied access.

To access Enterprise Analytics, administrators authenticate by means of a username and password. These credentials can be validated by Enterprise Analytics itself: alternatively if the Enterprise Edition of Enterprise Analytics for Linux is used, validation can be performed either on a network-accessible directory-server, by means of the _Lightweight Directory Access Protocol_ (LDAP); or by means of the _Pluggable Authentication Modules_ (PAM) authentication-framework.