---
title: Import Processing
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/sync/pages/import-processing.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:sync-gateway:sync:import-processing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/sync/import-processing.html)

# Import Processing

## [](#overview)Overview

The **import process** is a key part of mobile convergence. It is the means by which sync gateway becomes aware of non-sync gateway data changes and obtains the mobile metadata it requires to replicate changes.

![shared bucket access](../_images/shared-bucket-access.png) 

## [](#operation)Operation

Any non-sync gateway change is eligible for import. For more information, refer to the [Sync Function](../access-control/sync-function/sync-function.md) documentation.

The document is first run through the Sync Function to compute read security and routing, with the following differences:

* The import is processed with an admin user context in the Sync Function, similar to writes made through the sync gateway Admin API. This means that `requireAccess`, `requireUser` and `requireRole` calls in the Sync Function are treated as no-ops.
* During import, `oldDoc` is `nil` when the Sync Function is executed.

You can specify a filter function dynamically using the [/{keyspace}/\_config/import\_filter](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-import%5Ffilter) endpoint, or you can define one when you set up a database. Refer to the [Import Filter Configuration](../configuration/configuration-schema-import-filter.md) documentation for more information.

> [!TIP]
> Use the `logging-console-log-keys` in the [Bootstrap Schema](../configuration/configuration-schema-bootstrap.md#lbl-schema) log key to troubleshoot import processing issues in the logs.

## [](#function-provision)Function Provision

Use the [Database Configuration](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration) Admin Rest API endpoint [POST /{db}/\_config](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/post%5Fdb-%5Fconfig) to provision an import filter for a database using the `application/javascript` mime type.

If you are using legacy configuration then, you need to include it in your configuration file, see: [import-filter](../configuration/configuration-properties-legacy.md#databases-this%5Fdb-import%5Ffilter).

## [](#configuration)Configuration

> [!NOTE]
> You need Couchbase Lite 3.1+ and Sync Gateway 3.1+ to use `custom` Scopes and Collections.  
> If you’re using Capella App Services or Sync Gateway releases that are older than version 3.1, you won’t be able to access `custom` Scopes and Collections. To use Couchbase Lite 3.1+ with these older versions, you can use the `default` Collection as a backup option.

The configuration settings described here are provisioned through the [Database Configuration](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration) endpoints.

```JSON
{
  scopes: {
      {scopename...}: {
         collections: {
            {collectionname...}: {
               import_filter: "function(doc) { if (doc.type != 'mobile') { return false; } return true; }",
            }
         }
      }
   },
   // other configuration
}
```

For more information, see [Database Configuration Schema](../configuration/configuration-schema-database.md#DatabaseConfig).

| Property       | Description                                                                                                                                                                  |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| scopename      | Represents the name of each scope                                                                                                                                            |
| collections    | Contains different collections within each scope                                                                                                                             |
| collectionname | Represents the name of each collection within a scope.                                                                                                                       |
| import\_filter | Used to decide if a document should be imported. It checks the type property of the document. If it is not 'mobile', the function returns false, otherwise, it returns true. |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

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