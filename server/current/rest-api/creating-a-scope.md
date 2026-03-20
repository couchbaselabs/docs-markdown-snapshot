---
title: Creating a Scope
description: Scopes can be <em>created</em>, by means of the REST API.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/creating-a-scope.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:rest-api:creating-a-scope.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/rest-api/creating-a-scope.html)

# Creating a Scope

> Scopes can be _created_, by means of the REST API. 

## [](#description)Description

Scopes are created by means of the `POST /pools/default/buckets/_<bucketname>_/scopes/` HTTP method and URI.

## [](#http-method-and-uri)HTTP Method and URI

POST /pools/default/buckets/<bucket_name>/scopes

## [](#curl-syntax)Curl Syntax

The curl syntax is as follows:

curl -X POST -v -u [admin]:[password]
  http://<hostname-or-ip>:8091/pools/default/buckets/<bucket-name>/scopes
  -d name=<scope-name>

The `<bucket-name>` path-parameter specifies the bucket within which the new scope is to be created. The `name` parameter specifies the name of the scope to be created: this name cannot subsequently be changed.

## [](#responses)Responses

Success returns `200 OK`. Failure to authenticate gives `401 Unauthorized`. A malformed URI fails with `404 Object Not Found`. If the scope-name is improperly specified, a notification such as `"name":"Length must be in range from 1 to 30"` or `"name":"Can only contain characters A-Z, a-z, 0-9 and the following symbols _ - %"` is displayed. See [Naming for Scopes and Collections](../learn/data/scopes-and-collections.md#naming-for-scopes-and-collections), for an account of naming conventions.

## [](#example)Example

The following call creates a scope named `my_scope` in the bucket `testBucket`:

curl -X POST -v -u Administrator:password \
http://10.143.210.101:8091/pools/default/buckets/testBucket/scopes \
-d name=my_scope

If successful, the call returns a `uid`, such as the following:

{"uid":17}

## [](#see-also)See Also

An overview of scopes and collections is provided in [Scopes and Collections](../learn/data/scopes-and-collections.md). Step-by-step procedures for management are provided in [Manage Scopes and Collections](../manage/manage-scopes-and-collections/manage-scopes-and-collections.md). See also the CLI reference page for the [collection-manage](../cli/cbcli/couchbase-cli-collection-manage.md) command.