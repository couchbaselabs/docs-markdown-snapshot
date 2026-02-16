[View original HTML](/sync-gateway/current/rest-api/rest-api-admin.html)

> Description of the Sync Gateway Admin REST API  

Related _REST API_ topics: [Public REST API](rest-api.md) | [Metrics REST API](rest-api-metrics.md)

## [](#introduction)Introduction

The Admin REST API is for administrator use only, and hence is **not** accessible from the clients directly.

To allow users to access the Admin API up you need to create a Couchbase Server-based RBAC-user for them — see: [REST API Access](rest-api-access.md).

Couchbase recommends that you do not expose the Sync Gateway admin interface to the internet. Due to this, features such as CORS are not supported on the admin interface.

|  | For document changes sent to Sync Gateway through the Admin REST API, the Sync Function executes with **admin** privileges.Calls to requireUser, requireAccess and requireRole will be no-ops, and will always appear successful. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#api-reference)API Reference

The [API reference](rest%5Fapi%5Fadmin.md) groups all the endpoints by functionality.

Each endpoint description specifies its RBAC role requirements, but see [RBAC Roles](rest-api-access-rbac-roles.md)and the Couchbase Server documentation here [Couchbase Server Authorization Roles](../../../server/current/learn/security/roles.md)if further information is required.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](../configuration/configuration-schema-bootstrap.md)
* [Database](../configuration/configuration-schema-database.md)
* [Database Security](../configuration/configuration-schema-db-security.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Import Filter](../configuration/configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](../configuration/configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)