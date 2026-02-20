---
title: Rotating the Data Key
description: The data key can be rotated, by means of the REST API.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/rest-api/pages/rotate-data-key.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:rest-api:rotate-data-key.adoc[]
---

[View original HTML](/server/7.6/rest-api/rotate-data-key.html)

# Rotating the Data Key

> The data key can be rotated, by means of the REST API. 

## [](#http-methods-and-uris)HTTP Method and URI

POST /node/controller/rotateDataKey

## [](#description)Description

This command rotates the data key. The **Full Admin**, **Local User Security Admin**, or **External User Security Admin** role is required.

## [](#curl-syntax)Curl Syntax

curl -X POST http://127.0.0.1:8091/node/controller/rotateDataKey
  -u Administrator:password

## [](#responses)Responses

Success returns `200 OK`. Failure to authenticate due to incorrect credentials returns `401 Unauthorized`. Attempt to authenticate with the wrong role returns `403 Forbidden`, and a message such as `{"message":"Forbidden. User needs the following permissions","permissions":["cluster.admin.security!write"]}`. An incorrectly expressed URI fails with `404 Object Not Found`.

## [](#example)Example

The following example rotates the data key.

curl -v -X POST http://localhost:8091/node/controller/rotateDataKey -u Administrator:password

## [](#see-also)See Also

For a full description of system secrets and their management, see [Manage System Secrets](../manage/manage-security/manage-system-secrets.md).