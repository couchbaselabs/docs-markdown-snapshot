---
title: System Secrets API
description: System secrets can be managed with the REST API.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/rest-api/pages/rest-secret-mgmt.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:rest-api:rest-secret-mgmt.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/rest-api/rest-secret-mgmt.html)

# System Secrets API

> System secrets can be managed with the REST API. 

## [](#apis-in-this-section)APIs in this Section

The REST API allows _system secrets_ to be managed. For a list of all methods and URIs covered in this section, see the table provided below.

| HTTP Method | URI                                   | Documented at                                                 |
| ----------- | ------------------------------------- | ------------------------------------------------------------- |
| GET         | /nodes/self/secretsManagement         | [Configuring System Secrets](system-secrets-configuration.md) |
| POST        | /node/controller/secretsManagement    | [Configuring System Secrets](system-secrets-configuration.md) |
| POST        | /node/controller/changeMasterPassword | [Changing the Master Password](change-master-password.md)     |
| POST        | /node/controller/rotateDataKey        | [Rotating the Data Key](rotate-data-key.md)                   |