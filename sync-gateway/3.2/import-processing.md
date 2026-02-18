---
title: Import Processing
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.2/modules/ROOT/pages/import-processing.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/sync-gateway/3.2/import-processing.html)

# Import Processing

## [](#overview)Overview

The **import process** is a key part of mobile convergence. It’s the means by which Sync Gateway becomes aware of non-Sync Gateway data changes and obtains the mobile metadata it requires to replicate changes.

![shared bucket access](_images/shared-bucket-access.png) 

## [](#operation)Operation

Any non-Sync Gateway change is eligible for import. For more information, refer to the [Sync Function](sync-function.md) documentation.

The document is first run through the Sync Function to compute read security and routing, with the following differences:

* The Sync Function processes the import using an admin user context, similar to how the Sync Gateway Admin API handles writes. This means the Sync Function treats `requireAccess`, `requireUser`, and `requireRole` calls as no-ops.
* During import, the Sync Function executes with `oldDoc` set to `nil`.

When importing a deleted document:

* Include the `doc` object with the `_deleted` property set to `true`.
* Do not include the `_id` and `_rev` fields in the `doc` object.
* Include an explicit check for `doc._deleted` in your import filter function to verify it handles deletions.

```javascript
function(doc) {
    // Always return true for deletions so they are not ignored during import
    if (doc._deleted === true) {
        return true;
    }
    // Only import mobile-type documents
    if (doc.type != 'mobile') {
        return false;
    }
    return true;
}
```

> [!TIP]
> Check for the `_deleted` property to avoid skipping deletion events.

You can specify a filter function dynamically using [/{keyspace}/\_config/import\_filter](rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/get%5Fkeyspace-%5Fconfig-import%5Ffilter), or you can define one when you set up a database. Refer to the [Import Filter Configuration](configuration-schema-import-filter.md) documentation for more information.

> [!TIP]
> Use the `logging-console-log-keys` in the [Bootstrap Schema](configuration-schema-bootstrap.md#lbl-schema) log key to troubleshoot import processing issues in the logs.

## [](#function-provision)Function Provision

Use the [Database Configuration](rest%5Fapi%5Fadmin.md#tag/Database-Configuration) Admin Rest API endpoint [POST /{db}/\_config](rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/post%5Fdb-%5Fconfig) to provision an import filter for a database using the `application/javascript` mime type.

If you are using legacy configuration then, you need to include it in your configuration file, see: [import-filter](configuration-properties-legacy.md#databases-this%5Fdb-import%5Ffilter).

## [](#configuration)Configuration

> [!NOTE]
> You need Couchbase Lite 3.1+ and Sync Gateway 3.1+ to use `custom` Scopes and Collections.  
> If you’re using Capella App Services or Sync Gateway releases that are older than version 3.1, you won’t be able to access `custom` Scopes and Collections. To use Couchbase Lite 3.1+ with these older versions, you can use the `default` Collection as a backup option.

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