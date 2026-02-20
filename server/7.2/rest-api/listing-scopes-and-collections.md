---
title: Listing Scopes and Collections
description: Scopes and collections can be <em>listed</em>, by means of the REST API.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/listing-scopes-and-collections.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:rest-api:listing-scopes-and-collections.adoc[]
---

[View original HTML](/server/7.2/rest-api/listing-scopes-and-collections.html)

# Listing Scopes and Collections

> Scopes and collections can be _listed_, by means of the REST API. 

## [](#description)Description

Scopes and collections are listed by means of the `GET /pools/default/buckets/_<bucketname>_/scopes/` HTTP method and URI.

## [](#http-method-and-uri)HTTP Method and URI

GET /pools/default/buckets/<bucket_name>/scopes/

## [](#syntax)Syntax

The curl syntax is as follows:

curl -X GET -v
  http://<hostname-or-ip>:8091/pools/default/buckets/<bucket_name>/scopes
  -u <username>:<password>

The `<bucket-name>` path-parameter specifies the name of the bucket whose defined collections are to be listed.

## [](#responses)Responses

Success returns `200 OK`. Failure to authenticate gives `401 Unauthorized`. A malformed URI fails with `404 Object Not Found`.

## [](#examples)Examples

The following example lists the collections in a bucket named `testBucket`:

curl -X GET -v -u Administrator:password \
http://10.143.210.101:8091/pools/default/buckets/testBucket/scopes

If successful, the call returns `200 OK`, and an object listing scopes and collections. For example:

{"uid":"0","scopes":[{"name":"_default","uid":"0","collections":[{"name":"_default","uid":"0"}]}]}

## [](#see-also)See Also

An overview of scopes and collections is provided in [Scopes and Collections](../learn/data/scopes-and-collections.md). Step-by-step procedures for management are provided in [Manage Scopes and Collections](../manage/manage-scopes-and-collections/manage-scopes-and-collections.md). See also the CLI reference page for the [collection-manage](../cli/cbcli/couchbase-cli-collection-manage.md) command.