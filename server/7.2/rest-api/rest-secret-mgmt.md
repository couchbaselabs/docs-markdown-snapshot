---
title: Secret-Management API
description: An Administrator can change the master password and data key.
  Rotating the key and resetting the password require authentication.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/rest-secret-mgmt.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:rest-api:rest-secret-mgmt.adoc[]
---

[View original HTML](/server/7.2/rest-api/rest-secret-mgmt.html)

# Secret-Management API

> An Administrator can change the master password and data key. Rotating the key and resetting the password require authentication. 

## [](#post-nodecontrollerchangemasterpassword)POST /node/controller/changeMasterPassword

**Description:**

This command sets the master password.

**Parameters:**

* newPassword - Specify a new master password. Required.

**Syntax:**

$ curl -v -X POST -d 'newPassword=blah' \
http://Administrator:password@127.0.0.1:8091/node/controller/changeMasterPassword

## [](#post-nodecontrollerrotatedatakey)POST /node/controller/rotateDataKey

**Description:**

This command rotates the data key.

**Parameters:**

* None

**Syntax:**

$ curl -v -X POST http://Administrator:password@127.0.0.1:8091/node/controller/rotateDataKey