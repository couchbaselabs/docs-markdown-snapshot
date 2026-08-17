---
title: Change Password
description: A local user of Couchbase Server can change their password.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/rest-set-password.adoc
  xref: xref:7.2@server:rest-api:rest-set-password.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/rest-api/rest-set-password.html)

# Change Password

> A local user of Couchbase Server can change their password. 

## [](#http-methods-and-uris)HTTP Method and URI

POST /controller/changePassword

## [](#description)Description

Changes the current, locally defined user-password to a new user-password.

## [](#curl-syntax)Curl Syntax

curl -X POST http://<ip-address-or-domain-name>:8091/controller/changePassword
  -u <username>:<password>
  -d <new-password>

The specified `new-password` must be for a locally defined user, and must conform to the currently established _password policy_ for the cluster. The default policy is described in [Password Strength](../learn/security/usernames-and-passwords.md#password-strengthd). For instructions on changing the current password policy, see [Set Password Policy](rest-set-password-policy.md). For information on _local_ and _external_ domains, see [Authentication Domains](../learn/security/authentication-domains.md).

## [](#responses)Responses

Success returns `200 OK`. Failure to authenticate returns `401 Unauthorized`. A malformed URI returns `404 Object Not Found`.

## [](#examples)Examples

The following example changes the locally defined password of user `localUser` from `localUserPassword` to `localUserNewPassword`:

curl -v -X POST http://localhost:8091/controller/changePassword \
-u localUser:localUserPassword \
-d password=localUserNewPassword

## [](#see-also)See Also

The default policy is described in [Password Strength](../learn/security/usernames-and-passwords.md#password-strengthd). For instructions on changing the current password policy, see [Set Password Policy](rest-set-password-policy.md). For information on _local_ and _external_ domains, see [Authentication Domains](../learn/security/authentication-domains.md).