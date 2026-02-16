[View original HTML](/sync-gateway/3.2/configuration-schema-import-filter.html)

|  | Pre-3.0 Legacy Configuration Equivalents This content describes configuration for Sync Gateway 3.0 and higher — for legacy configuration, see: [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md) |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#introduction)Introduction

Using an import filter will significantly improve efficiency if you’re working with large datasets:

* Import filters are defined at the collection level and allow you to retrieve only the relevant documents you need rather than the entire dataset. The import filter helps determine which documents can be copied by Sync Gateway. It looks at the application’s needs and applies these criteria to all future changes.
* By reducing the amount of data that needs to be processed, an import filter will improve the performance of your queries and analysis. It’s worth noting that Sync Gateway imports all documents by default, so it’s generally a good idea to use an import filter unless you have a strong reason not to.

See: [Import filter](import-processing.md) for more.

## [](#function-provision)Function Provision

Use the [Database Configuration](rest%5Fapi%5Fadmin.md#tag/Database-Configuration) Admin Rest API endpoint [POST /{db}/\_config](rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/post%5Fdb-%5Fconfig) to provision an import filter for a database using the `application/javascript` mime type.

If you are using legacy configuration, you need to include it in your configuration file. See: [import-filter](configuration-properties-legacy.md#databases-this%5Fdb-import%5Ffilter).

## [](#configuration)Configuration

|  | You need Couchbase Lite 3.1+ and Sync Gateway 3.1+ to use custom Scopes and Collections.If you’re using Capella App Services or Sync Gateway releases that are older than version 3.1, you won’t be able to access custom Scopes and Collections. To use Couchbase Lite 3.1+ with these older versions, you can use the default Collection as a backup option. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

The configuration settings described here are provisioned through the [Database Configuration](rest-api-admin.md) endpoints.

```JSON
{
  "scopes": {
      "scopename...": {
         "collections": {
            "collectionname...": {
               "import_filter": "function(doc) { if (doc.type != 'mobile') { return false; } return true; }",
            }
         }
      }
   },
   // other configuration
}
```

For more information, see [Sync Gateway Configuration Schema](configuration-schema-database.md#DatabaseConfig).

| Property       | Description                                                                                                                                                                  |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| scopename      | Represents the name of each scope                                                                                                                                            |
| collections    | Contains different collections within each scope                                                                                                                             |
| collectionname | Represents the name of each collection within a scope.                                                                                                                       |
| import\_filter | Used to decide if a document should be imported. It checks the type property of the document. If it is not 'mobile', the function returns false, otherwise, it returns true. |

* API
* Legacy

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

## [](#put%5Fkeyspace-%5Fconfig-import%5Ffilter)Set database import filter

PUT /{keyspace}/_config/import_filter

### [](#put%5Fkeyspace-%5Fconfig-import%5Ffilter-description)Description

This will allow you to update the database's import filter.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

Consumes

* application/javascript

Produces

* application/json

### [](#put%5Fkeyspace-%5Fconfig-import%5Ffilter-parameters)Parameters

#### [](#put%5Fkeyspace-%5Fconfig-import%5Ffilter-path)Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |

#### [](#put%5Fkeyspace-%5Fconfig-import%5Ffilter-query)Query Parameters

| Name                                     | Description                                                                                 | Schema  |
| ---------------------------------------- | ------------------------------------------------------------------------------------------- | ------- |
| **disable\_oidc\_validation** _optional_ | If set, will not attempt to validate the configured OpenID Connect providers are reachable. | Boolean |

#### [](#put%5Fkeyspace-%5Fconfig-import%5Ffilter-header)Header Parameters

| Name                    | Description                                                                                                                                                      | Schema |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **If-Match** _optional_ | If set to a configuration's Etag value, enables optimistic concurrency control for the request. Returns HTTP 412 if another update happened underneath this one. | String |

#### [](#put%5Fkeyspace-%5Fconfig-import%5Ffilter-body)Body Parameter

| Name                | Description              | Schema |
| ------------------- | ------------------------ | ------ |
| **Body** _optional_ | The import filter to use | String |

### [](#put%5Fkeyspace-%5Fconfig-import%5Ffilter-responses)Responses

| HTTP Code | Description                                                                                                                                                                                                                              | Schema                  |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| 200       | Updated import filter successfully                                                                                                                                                                                                       |                         |
| 400       | There was a problem with your request                                                                                                                                                                                                    | [Errors](#HTTP%5FError) |
| 404       | Resource could not be found                                                                                                                                                                                                              | [Errors](#HTTP%5FError) |
| 412       | Precondition Failed The supplied If-Match header did not match the current version of the configuration. Returned when optimistic concurrency control is used, and there has been an update to the configuration in between this update. | [Errors](#HTTP%5FError) |

## [](#%5FImport%5Ffilter)Schema

This section shows Sync Gateway’s import control configuration settings in schema format for convenience in constructing JSON models for use in the Admin REST API.

The configuration settings described here are provisioned through [Authentication](rest%5Fapi%5Fadmin.md#tag/Authentication) endpoints.

### [](#%5Fimport%5Ffilter%5Fmodel)Import Filter Model

The `import_filter` controls whether a document written to the Couchbase Server bucket should be made available to Couchbase Mobile clients (that is, whether it ought to be imported).

You should provision the filter as a Javascript function in the request body of a call to the Admin Rest API endpoint `put {db}/_config/import_filter`.

Set the header’s content type to `content-Type: application/javascript`.

The function takes the document body as parameter and is expected to return a boolean to indicate whether the document should be imported.

If you do not provide a filter function then no filter will be applied and ALL documents will be imported.

_Type_ : string

## [](#HTTP%5FError)Errors

This section shows possible error responses returned by the Admin REST API.

| Property              |                        | Schema |
| --------------------- | ---------------------- | ------ |
| **error** _required_  | The error name.        | String |
| **reason** _required_ | The error description. | String |

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
* [Import Filter](#)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)