---
title: Dropping a Scope
description: Scopes can be <em>dropped</em>, by means of the REST API.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/dropping-a-scope.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:rest-api:dropping-a-scope.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/rest-api/dropping-a-scope.html)

# Dropping a Scope

> Scopes can be _dropped_, by means of the REST API. 

## [](#description)Description

Scopes are dropped by means of the `DELETE /pools/default/buckets/<bucket_name>/scopes/<scope_name>` HTTP method and URI.

## [](#http-method-and-uri)HTTP Method and URI

DELETE /pools/default/buckets/<bucket_name>/scopes/<scope_name>

## [](#syntax)Syntax

The curl syntax is as follows:

curl -X DELETE -v -u [admin]:[password]
  http://<hostname-or-ip>:8091/pools/default/buckets/\
    <bucket_name>/scopes/<scope_name>

The `<bucket-name>` path-parameter specifies the bucket whose scope is to be dropped. The `<scope-name>` path-parameter specifies the scope that is to be dropped.

## [](#responses)Responses

Success returns `200 OK`. Failure to authenticate gives `401 Unauthorized`. A malformed URI fails with `404 Object Not Found`. If the scope-name is improperly specified, a notification such as `"name":"Length must be in range from 1 to 30"` or `"name":"Can only contain characters A-Z, a-z, 0-9 and the following symbols _ - %"` is displayed. See [Scopes and Collections](../learn/data/scopes-and-collections.md), for an account of naming conventions.

## [](#example)Example

Curl request example:

curl -X DELETE -v -u Administrator:password \
http://10.143.210.101:8091/pools/default/buckets/\
testBucket/scopes/my_scope

If successful, the call returns a UID. For example:

{"uid":20}

## [](#see-also)See Also

An overview of scopes and collections is provided in [Scopes and Collections](../learn/data/scopes-and-collections.md). Step-by-step procedures for management are provided in [Manage Scopes and Collections](../manage/manage-scopes-and-collections/manage-scopes-and-collections.md). See also the CLI reference page for the [collection-manage](../cli/cbcli/couchbase-cli-collection-manage.md) command.