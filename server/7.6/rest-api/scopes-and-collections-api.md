---
title: Scopes and Collections API
description: Scopes and collections can be managed with the REST API.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/rest-api/pages/scopes-and-collections-api.adoc
  xref: xref:7.6@server:rest-api:scopes-and-collections-api.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/rest-api/scopes-and-collections-api.html)

# Scopes and Collections API

> Scopes and collections can be managed with the REST API. 

## [](#apis-in-this-section)APIs in this Section

The REST API allows buckets to be created, edited, flushed, and deleted. For a list of all methods and URIs covered in this section, see the table provided below.

| HTTP Method | URI                                                                                       | Documented at                                                       |
| ----------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| POST        | /pools/default/buckets/<bucket\_name>/scopes                                              | [Creating a Scope](creating-a-scope.md)                             |
| POST        | /pools/default/buckets/<bucket\_name>/scopes/<scope\_name>/collections                    | [Creating a Collection](creating-a-collection.md)                   |
| GET         | /pools/default/buckets/<bucket\_name>/scopes/                                             | [Listing Scopes and Collections](listing-scopes-and-collections.md) |
| DELETE      | /pools/default/buckets/<bucket\_name>/scopes/<scope\_name>/collections/<collection\_name> | [Dropping a Collection](dropping-a-collection.md)                   |
| DELETE      | /pools/default/buckets/<bucket\_name>/scopes/<scope\_name>                                | [Dropping a Scope](dropping-a-scope.md)                             |