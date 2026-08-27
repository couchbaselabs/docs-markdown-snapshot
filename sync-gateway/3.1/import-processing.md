---
title: Import Processing
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.1/modules/ROOT/pages/import-processing.adoc
  xref: xref:3.1@sync-gateway::import-processing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.1/import-processing.html)

# Import Processing

## [](#overview)Overview

The **import process** is a key part of mobile convergence. It is the means by which sync gateway becomes aware of non-sync gateway data changes and obtains the mobile metadata it requires to replicate changes.

![shared bucket access](_images/shared-bucket-access.png) 

## [](#operation)Operation

Any non-sync gateway change is eligible for import. For more information, refer to the [Sync Function](sync-function.md) documentation.

The document is first run through the Sync Function to compute read security and routing, with the following differences:

* The import is processed with an admin user context in the Sync Function, similar to writes made through the sync gateway Admin API. This means that `requireAccess`, `requireUser` and `requireRole` calls in the Sync Function are treated as no-ops.
* During import, `oldDoc` is `nil` when the Sync Function is executed.

You can specify a filter function dynamically using [/{keyspace}/\_config/import\_filter](rest%5Fapi%5Fadmin%5Fstatic.md#get%5Fkeyspace-%5Fconfig-import%5Ffilter), or you can define one when you set up a database. Refer to the [Import Filter Configuration](configuration-schema-import-filter.md) documentation for more information.

> [!TIP]
> Use the `logging-console-log-keys` in the [Bootstrap Schema](configuration-schema-bootstrap.md#lbl-schema) log key to troubleshoot import processing issues in the logs.

## [](#function-provision)Function Provision

Use the [Database Configuration](rest-api-admin.md#/Database%5FConfiguration/) Admin Rest API endpoint [POST /{db}/\_config](rest%5Fapi%5Fadmin%5Fstatic.md#post%5Fdb-%5Fconfig) to provision an import filter for a database using the `application/javascript` mime type.

If you are using legacy configuration then, you need to include it in your configuration file, see: [import-filter](configuration-properties-legacy.md#databases-this%5Fdb-import%5Ffilter).

## [](#configuration)Configuration

> [!NOTE]
> You need Couchbase Lite 3.1+ and Sync Gateway 3.1+ to use `custom` Scopes and Collections.  
> If you're using Capella App Services or Sync Gateway releases that are older than version 3.1, you won't be able to access `custom` Scopes and Collections. To use Couchbase Lite 3.1+ with these older versions, you can use the `default` Collection as a backup option.

The configuration settings described here are provisioned through the [Database Configuration](rest-api-admin.md) endpoints.

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

For more information, see [Sync Gateway Configuration Schema](configuration-schema-database.md#%5Fdatabase).

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

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
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