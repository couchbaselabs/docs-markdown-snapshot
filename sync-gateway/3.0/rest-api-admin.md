---
title: Admin REST API
description: Description of the Sync Gateway Admin REST API
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/rest-api-admin.adoc
pubDate: 2026-03-28T05:05:12.980Z
link: xref:3.0@sync-gateway::rest-api-admin.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/rest-api-admin.html)

# Admin REST API

> Description of the Sync Gateway Admin REST API  
> Use the API explorer to find out more about Sync Gateway's endpoints by functionality.

Related _REST API_ topics: [Public REST API](rest-api.md) | [Metrics REST API](rest-api-metrics.md)

> [!IMPORTANT]
> Content Blocking
> 
> Couchbase Mobile's API documentation utilizes [Swagger UI](https://swagger.io/tools/swagger-ui/)to deliver an interactive and dynamic user experience. The page will not function correctly if your organization's security policies restricts access to this type of content — instead see the alternate statics page [Admin REST API (Static Page)](rest%5Fapi%5Fadmin%5Fstatic.md)

## [](#introduction)Introduction

The Admin REST API is for administrator use only, and hence is **not** accessible from the clients directly.

To allow users to access the Admin API up you need to create a Couchbase Server-based RBAC-user for them — see: [REST API Access](rest-api-access.md)

> [!NOTE]
> For document changes sent to Sync Gateway through the Admin REST API, the Sync Function executes with **admin** privileges.  
> Calls to `requireUser`, `requireAccess` and `requireRole` will be no-ops, and will always appear successful.

## [](#api-explorer)API Explorer

The API explorer below groups all the endpoints by functionality. You can click on a label to expand the list of endpoints and also generate a curl request for each endpoint.

Each endpoint description specifies its RBAC role requirements, but see [RBAC Roles](rest-api-access-rbac-roles.md)and the Couchbase Server documentation here [Couchbase Server Authorization Roles](../../server/current/learn/security/roles.md)if further information is required.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](rest-api.md)
* [Admin REST API](#)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](configuration-schema-bootstrap.md)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)