---
title: Dropping a Collection
description: Scopes can be <em>dropped</em>, by means of the REST API.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/rest-api/pages/dropping-a-collection.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/rest-api/dropping-a-collection.html)

# Dropping a Collection

> Scopes can be _dropped_, by means of the REST API. 

## [](#description)Description

Collections are dropped by means of the `DELETE /pools/default/buckets/_<bucketname>_/scopes/_<scopename>_/collections/_<collectionname>_` HTTP method and URI.

## [](#http-method-and-uri)HTTP Method and URI

DELETE /pools/default/buckets/<bucket_name>/scopes/<scope_name>/collections/<collection_name>

## [](#syntax)Syntax

The curl syntax is as follows:

curl -X DELETE -v -u [admin]:[password]
  http://<hostname-or-ip>:8091/pools/default/buckets/\
    <bucket-name>/scopes/<scope-name>/collections/<collection-name>

The `<bucket-name>` path-parameter specifies the bucket whose collection is to be dropped. The `<scope-name>` path-parameter specifies the scope that contains the collection that is to be dropped. The `<collection-name>` path-parameter specifies the name of the collection that is to be dropped.

Success returns `200 OK` and a UID. Failure to authenticate gives `401 Unauthorized`. A malformed URI fails with `404 Object Not Found`.

## [](#responses)Responses

Success returns `200 OK`. Failure to authenticate gives `401 Unauthorized`. A malformed URI fails with `404 Object Not Found`. If the scope-name or collection-name is improperly specified, a notification such as `"name":"Length must be in range from 1 to 30"` or `"name":"Can only contain characters A-Z, a-z, 0-9 and the following symbols _ - %"` is displayed. See [Scopes and Collections](../learn/data/scopes-and-collections.md), for an account of naming conventions.

## [](#examples)Examples

curl -X DELETE -v -u Administrator:password \
http://10.143.210.101:8091/pools/default/buckets/\
testBucket/scopes/my_scope/collections/my_collection_in_my_scope_1

If successful, the call returns a UID. For example:

{"uid":"3"}

## [](#see-also)See Also

An overview of scopes and collections is provided in [Scopes and Collections](../learn/data/scopes-and-collections.md). Step-by-step procedures for management are provided in [Manage Scopes and Collections](../manage/manage-scopes-and-collections/manage-scopes-and-collections.md). See also the CLI reference page for the [collection-manage](../cli/cbcli/couchbase-cli-collection-manage.md) command.