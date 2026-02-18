---
title: Changing the Master Password
description: The master password can be changed, by means of the REST API.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/change-master-password.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/rest-api/change-master-password.html)

# Changing the Master Password

> The master password can be changed, by means of the REST API. 

## [](#http-methods-and-uris)HTTP Method and URI

POST /node/controller/changeMasterPassword

## [](#description)Description

This command sets the master password for the current node.

For a full description of system secrets and their management, see [Manage System Secrets](../manage/manage-security/manage-system-secrets.md).

## [](#curl-syntax)Curl Syntax

curl -X POST http://127.0.0.1:8091/node/controller/changeMasterPassword
 -u Administrator:password
 -d newPassword=<new-password>

## [](#required-privileges)Required Privileges

You must have one of the following roles to change the master password:

* [Full Admin](../learn/security/roles.md#full-admin)
* [Security Admin](../learn/security/roles.md#security-admin)

## [](#responses)Responses

Success returns `200 OK`. Failure to authenticate due to incorrect credentials returns `401 Unauthorized`. Attempt to authenticate with the wrong role returns `403 Forbidden`, and a message such as `{"message":"Forbidden. User needs the following permissions","permissions":["cluster.admin.security!write"]}`. An incorrectly expressed URI fails with `404 Object Not Found`.

## [](#example)Example

The following example changes the master password.

curl -v -X POST http://localhost:8091/node/controller/changeMasterPassword \
-u Administrator:password \
-d newPassword=o12m2Bb?ufh3*a

## [](#see-also)See Also

For a full description of system secrets and their management, see [Manage System Secrets](../manage/manage-security/manage-system-secrets.md).