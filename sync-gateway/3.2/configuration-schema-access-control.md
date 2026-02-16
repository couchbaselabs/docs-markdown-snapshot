[View original HTML](/sync-gateway/3.2/configuration-schema-access-control.html)

|  | Pre-3.0 Legacy Configuration Equivalents This content describes configuration for Sync Gateway 3.0 and higher — for legacy configuration, see: [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md) |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#introduction)Introduction

The sync function is crucial to the security of your application. It is in charge of data validation, access control and routing. The function executes every time a new revision/update is made to a document.

For more on the Sync Function and access control see: [Sync Function Overview](#sync-function-overview.adoc)

## [](#put%5Fkeyspace-%5Fconfig-sync)Set database sync function

PUT /{keyspace}/_config/sync

### [](#put%5Fkeyspace-%5Fconfig-sync-description)Description

This will allow you to update the sync function.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

Consumes

* application/javascript

Produces

* application/json

### [](#put%5Fkeyspace-%5Fconfig-sync-parameters)Parameters

#### [](#put%5Fkeyspace-%5Fconfig-sync-path)Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |

#### [](#put%5Fkeyspace-%5Fconfig-sync-query)Query Parameters

| Name                                     | Description                                                                                 | Schema  |
| ---------------------------------------- | ------------------------------------------------------------------------------------------- | ------- |
| **disable\_oidc\_validation** _optional_ | If set, will not attempt to validate the configured OpenID Connect providers are reachable. | Boolean |

#### [](#put%5Fkeyspace-%5Fconfig-sync-header)Header Parameters

| Name                    | Description                                                                                                                                                      | Schema |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **If-Match** _optional_ | If set to a configuration's Etag value, enables optimistic concurrency control for the request. Returns HTTP 412 if another update happened underneath this one. | String |

#### [](#put%5Fkeyspace-%5Fconfig-sync-body)Body Parameter

| Name                | Description                  | Schema |
| ------------------- | ---------------------------- | ------ |
| **Body** _optional_ | The new sync function to use | String |

### [](#put%5Fkeyspace-%5Fconfig-sync-responses)Responses

| HTTP Code | Description                                                                                                                                                                                                                              | Schema                  |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| 200       | Updated sync function successfully                                                                                                                                                                                                       |                         |
| 400       | There was a problem with your request                                                                                                                                                                                                    | [Errors](#HTTP%5FError) |
| 404       | Resource could not be found                                                                                                                                                                                                              | [Errors](#HTTP%5FError) |
| 412       | Precondition Failed The supplied If-Match header did not match the current version of the configuration. Returned when optimistic concurrency control is used, and there has been an update to the configuration in between this update. | [Errors](#HTTP%5FError) |

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
* [Access Control](#)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)