---
title: Import Filter Configuration
description: Using Sync Gateway's Admin REST API and the Import Filter function
  to configure access
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.1/modules/configuration/pages/configuration-schema-import-filter.adoc
  xref: xref:sync-gateway:configuration:configuration-schema-import-filter.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/configuration/configuration-schema-import-filter.html)

# Import Filter Configuration

> [!IMPORTANT]
> Pre-3.0 Legacy Configuration Equivalents
> 
> This content describes configuration for Sync Gateway 3.0 and higher — for legacy configuration, see: [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

## [](#introduction)Introduction

Using an import filter improves efficiency when working with large datasets:

* You define import filters at the collection level to retrieve only the relevant documents you need rather than the entire dataset. The import filter determines which documents Sync Gateway can import, evaluating the application's requirements and applying these criteria to all future changes.
* By reducing the amount of data to process, an import filter improves the performance of your queries and analysis. Sync Gateway imports all documents by default, so use an import filter unless you have specific requirements otherwise.

For more information, see [Import filter](../sync/import-processing.md).

## [](#lbl-set-import-filter)Set database import filter

Configure an import filter to control which documents are imported from Couchbase Server to Sync Gateway.

For complete endpoint details, including header parameters (such as `If-Match` for optimistic concurrency control) and body parameters, see [/{keyspace}/\_config/import\_filter](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-import%5Ffilter) in the Admin REST API.

### [](#provisioning-methods)Provisioning Methods

You can provision an import filter using:

* **Admin REST API** (Sync Gateway 3.0+): Use the [/{keyspace}/\_config/import\_filter](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-import%5Ffilter) endpoint with the `application/javascript` mime type.
* **Legacy Configuration**: Include the import filter in your configuration file. For more information, see [import-filter](configuration-properties-legacy.md#databases-this%5Fdb-import%5Ffilter).

### [](#configuration-structure)Configuration Structure

> [!NOTE]
> Custom scopes and collections require Couchbase Lite 3.1 or later and Sync Gateway 3.1 or later.  
> Capella App Services and Sync Gateway releases earlier than version 3.1 do not support custom scopes and collections. When using Couchbase Lite 3.1 or later with earlier Sync Gateway versions, use the default collection as an alternative.

The configuration settings described here are provisioned through the [Database Configuration](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration) endpoints.

```JSON
{
  "scopes": {
      "scopename...": {
         "collections": {
            "collectionname...": {
               "import_filter": "function(doc) { if (doc.type != 'mobile') { return false } return true }",
            }
         }
      }
   },
   // other configuration
}
```

For more information, see [Database Configuration Schema](configuration-schema-database.md#DatabaseConfig).

| Property       | Description                                                                                                                                                             |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| scopename      | Represents the name of each scope                                                                                                                                       |
| collections    | Contains different collections within each scope                                                                                                                        |
| collectionname | Represents the name of each collection within a scope.                                                                                                                  |
| import\_filter | Determines whether to import a document. The function checks the document's type property. If it's not 'mobile', the function returns false, otherwise it returns true. |

### [](#example)Example

Example 1\. Configure import filter

This example demonstrates how to configure an import filter for a Sync Gateway database.

* Admin REST API
* Legacy Configuration

```bash
curl -X PUT "http://localhost:4985/froglist/_config/import_filter" \
-H "accept: application/json" \
-H "Content-Type: application/javascript" \
-H "Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=" \
-d "\"function(doc) {\ if (doc.type != 'mobile') {\ return false\ }\ return true\}\\\""
```

```json
  {
    "databases": {
      "getting-started-db": {
        "bucket": "getting-started-bucket",
        "import_docs": true,
        "num_index_replicas": 0,
        // ... other config as required
        "import_filter": `
        function(doc) {
          if (doc.type != "mobile") {
            return false
          }
          return true
          }`,
        }
      }
  }
```

## [](#%5FImport%5Ffilter)Schema

This section describes Sync Gateway's import filter configuration in schema format to assist with constructing JSON models for use with the Admin REST API.

The configuration settings are provisioned through the [Database Configuration](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration) endpoints.

### [](#%5Fimport%5Ffilter%5Fmodel)Import Filter Model

The `import_filter` determines whether to make a document written to the Couchbase Server bucket available to Couchbase Mobile clients (whether to import it).

You should provision the filter as a JavaScript function in the request body of a call to the Admin Rest API endpoint `PUT {db}/_config/import_filter`.

Set the header's content type to `content-Type: application/javascript`.

The function takes the document body as parameter and returns a boolean to indicate whether to import the document.

If you do not provide a filter function, Sync Gateway imports all documents.

**Type**: string

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