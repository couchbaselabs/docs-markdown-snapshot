---
title: Inter-Sync&#160;Gateway Replication Configuration
description: Using Sync Gateway's Admin REST API to configure and manage
  inter-Sync&#160;Gateway replications
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.3/modules/configuration/pages/configuration-schema-isgr.adoc
  xref: xref:3.3@sync-gateway:configuration:configuration-schema-isgr.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.3/configuration/configuration-schema-isgr.html)

# Inter-Sync&#160;Gateway Replication Configuration

> Using Sync Gateway's Admin REST API to configure and manage inter-Sync Gateway replications  

_Related topics_: [Overview](configuration-overview.md) | [Bootstrap](configuration-schema-bootstrap.md) | [Database](configuration-schema-database.md) | [Database Security](configuration-schema-db-security.md) | [Access Control](configuration-schema-access-control.md) | [Import](configuration-schema-import-filter.md) | [Inter-Sync Gateway Replication](configuration-schema-isgr.md)

> [!IMPORTANT]
> Pre-3.0 Legacy Configuration Equivalents
> 
> This content describes configuration for Sync Gateway 3.0 and higher — for legacy configuration, see: [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

## [](#introduction)Introduction

Sync Gateway 3.0 and later uses the Admin REST API to provision persistent configuration changes. This page introduces the [Add or Update a Replication](#put%5Fdb-%5Freplication-replicationid) endpoint for convenience — see [Replication](../rest-api/rest%5Fapi%5Fadmin.md#tag/Replication) for a full description of the endpoints available.

Using CA Certificates

Required CA certificates must be added to the system certificate pool.

On Linux, this is done using one of the following methods:

* Adding the location of the certificate to `SSL_CERT_FILE` environment variable,
* Placing the certificate in a location pointed to by the `SSL_CERT_DIR` environment variable.
* Using one of the system-dependent locations [listed in this file](https://go.dev/src/crypto/x509/root%5Flinux.go).

For Windows-based systems, add CA certificate files to the system root certificate store.

## [](#put%5Fdb-%5Freplication-replicationid)Upsert a replication

PUT /{db}/_replication/{replicationid}

### [](#put%5Fdb-%5Freplication-replicationid-description)Description

Create or update a replication in the database.

The replication ID does **not** need to be set in the request body.

If an existing replication is being updated, that replication must be stopped first and, if the `replication_id` is specified in the request body, it must match the replication ID in the URI.

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

Consumes

* application/json

Produces

* application/json

### [](#put%5Fdb-%5Freplication-replicationid-parameters)Parameters

#### [](#put%5Fdb-%5Freplication-replicationid-path)Path Parameters

| Name                         | Description                                             | Schema |
| ---------------------------- | ------------------------------------------------------- | ------ |
| **db** _required_            | The name of the database to run the operation against.  | String |
| **replicationid** _required_ | What replication to target based on its replication ID. | String |

#### [](#put%5Fdb-%5Freplication-replicationid-body)Body Parameter

| Name                | Description                                                                                                                                                                                                                                   | Schema                                           |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| **Body** _optional_ | If the replication\_id matches an existing replication then the existing configuration will be updated. Only the specified fields in the request will be used to update the existing configuration. Unspecified fields will remain untouched. | [Schema](#UserConfigurableReplicationProperties) |

### [](#put%5Fdb-%5Freplication-replicationid-responses)Responses

| HTTP Code | Description                                 | Schema                  |
| --------- | ------------------------------------------- | ----------------------- |
| 200       | Updated existing configuration successfully |                         |
| 201       | Created new replication successfully        |                         |
| 400       | There was a problem with your request       | [Errors](#HTTP%5FError) |
| 404       | Resource could not be found                 | [Errors](#HTTP%5FError) |

## [](#example)Example

* Curl
* HTTP

```bash
curl --location --request PUT 'http://localhost:4985/db1-local/_replication/db1-rep-id1 '\
--header 'Content-Type: application/json' \
--data-raw '{
  "direction": "push",
  "purge_on_removal": false,
  "remote": "http://user1:password1@example.com:4984/db1-remote",
  "filter":"sync_gateway/bychannel",
  "query_params": {
    "channels":["channel.user1"]
  },
  "continuous": false
  }'
```

```http
PUT /db1-local/_replication/db1-rep-id1 HTTP/1.1
Host: localhost:4985
Content-Type: application/json
Content-Length: 235

{"direction": "push",
  "purge_on_removal":false,
  "remote": "http://user1:password1@example.com:4984/db1-remote",
  "filter":"sync_gateway/bychannel",
  "query_params": {
    "channels":["channel.user1"]
  },
  "continuous": false
}
```

## [](#UserConfigurableReplicationProperties)Schema

This section shows Sync Gateway's replication configuration settings in schema format for convenience in constructing JSON models for use in the Admin REST API.

The configuration settings described here are provisioned through the [Replication](../rest-api/rest%5Fapi%5Fadmin.md#tag/Replication) endpoints.


{
   [adhoc](#adhoc): false,
   [batch_size](#batch%5Fsize): 200,
   [collections_enabled](#collections%5Fenabled): false,
   [collections_local](#collections%5Flocal): ["string"...],
   [collections_remote](#collections%5Fremote): ["string"...],
   [conflict_resolution_type](#conflict%5Fresolution%5Ftype): "default",
   [continuous](#continuous): false,
   [custom_conflict_resolver](#custom%5Fconflict%5Fresolver): "",
   [direction](#direction): "string",
   [enable_delta_sync](#enable%5Fdelta%5Fsync): false,
   [filter](#filter): "string",
   [initial_state](#initial%5Fstate): "running",
   [max_backoff_time](#max%5Fbackoff%5Ftime): 5,
   [purge_on_removal](#purge%5Fon%5Fremoval): false,
   [query_params](#query%5Fparams): ["string"...],
   [remote](#remote): "string",
   [remote_password](#remote%5Fpassword): "string",
   [remote_username](#remote%5Fusername): "string",
   [replication_id](#replication%5Fid): "string",
   [run_as](#run%5Fas): "string"
}

#### `adhoc`

Type

boolean

Description

Set to true to run the replication as an adhoc replication instead of a persistent one.

This means that the replication will only last the period of the replication until the status is changed to `stopped` and then it will be removed automatically. It will also be removed if Sync Gateway restarts or if removed due to user action.

#### `batch_size`

Type

integer

Default

200

Description

The amount of changes to be sent in one batch of replications. Changing this is an Enterprise Edition only feature.

#### `collections_enabled`

Type

boolean

Description

If true, the replicator will run with collections, and will replicate all collections, unless otherwise limited by `collections_local`.

If false, the replicator will only replicate the default collection.

#### `collections_local`

Type

array

Description

Limits the set of collections replicated to those listed in this array.

The replication will use all collections defined on the database if this list is empty.

#### `collections_remote`

Type

array

Description

Remaps the local collection name to the one specified in this array when replicating with the remote.

If only a subset of collections need remapping, elements in this array can be specified as `null` to preserve the local collection name.

The same index is used for both `collections_remote` and `collections_local`, and both arrays must be the same length.

#### `conflict_resolution_type`

Type

string

Default

default

Description

This defines what conflict resolution policy Sync Gateway should use to apply when resolving conflicting revisions.

Changing this is an Enterprise Edition only feature.

#### `continuous`

Type

boolean

Description

If true, changes will be immediately synced when they happen. This is known as a continuous replication.

If false, all changes will be synced until they have been processed. The replication will then cease and not process any future changes (unless started again by the user). This is known as a one-shot replication.

#### `custom_conflict_resolver`

Type

string

Description

This specifies the Javascript function to use to resolve conflicts between conflicting revisions.

This **must** be used when `conflict_resolution_type=custom`. This property will be ignored when `conflict_resolution_type` is not `custom`.

The Javascript function to provide this property should be in backticks (like the sync function). The function takes 1 parameter which is a struct that represents the conflict. This struct has 2 properties:

* `LocalDocument` \- The local document. This contains the document ID under the `_id` key.
* `RemoteDocument` \- The remote document The function should return the new document's body. This can be the winning revision (for example, `return conflict.LocalDocument`), a new body, or `nil` to resolve as a delete.

Example:

```javascript
function(conflict) {
  console.log("Doc ID: "+conflict.LocalDocument._id);
  console.log("Full remote doc: "+JSON.stringify(conflict.RemoteDocument));
  return conflict.RemoteDocument;
}

```

Using complex `custom_conflict_resolver` functions can noticeably degrade performance. Use a built-in resolver whenever possible.

This is an Enterprise Edition only feature.

#### `direction`

Type

string

Description

This specifies which direction the replication will be replicating with the `remote` replicator.

#### `enable_delta_sync`

Type

boolean

Description

This will turn on delta-sync for the replication. In order to enable delta-sync for a replication, the database level setting `delta_sync.enabled` must also be set to true.

Using delta-sync is an Enterprise Edition only feature.

#### `filter`

Type

string

Description

This defines whether to filter documents.

#### `initial_state`

Type

string

Default

running

Description

This is what state to start the replication in when creating a new replication.

This allows you to control if the replication starts in a `stopped` start or `running` state.

Replications prior to Sync Gateway 2.8 will run in the default state `running`.

#### `max_backoff_time`

Type

integer

Default

5

Description

Specifies the maximum time-period (in minutes) that Sync Gateway will attempt to reconnect to a lost or unreachable remote.

When a disconnection happens, Sync Gateway will do an exponential backoff up to this specified value. When this value is met, it will attempt to reconnect indefinitely every `max_backoff_time` minutes.

If this is set to 0, Sync Gateway will do the normal exponential backoff after the disconnect happens but then attempting 10 minutes and stop the replication.

Note: this defaults to 5 minutes for replications created prior to Sync Gateway 2.8.

#### `purge_on_removal`

Type

boolean

Description

Specifies whether to purge a document if the remote user loses access to all of the channels on the document when attempting to pull it from the remote.

If false, documents will not be replicated and not be purged when the user loses access.

#### `query_params`

Type

array

Description

This is a set of key/value pairs used in the query string of the replication.

If `filters=sync_gateway/bychannel` then this can be used to set the channels to filter by in a pull replication. To do this, set the `channels` key to a string array of the channels to filter by. For example:

```json
"filter":"sync_gateway/bychannel",
"query_params": {
  "channels":["chanUser1"]
},

```

#### `remote`

Type

string

Description

This is the endpoint of the database for the remote Sync Gateway that is the subject of this replication's `push`, `pull`, or `pushAndPull` action.

Typically this would include the URI, port, and database name. For example, `https://localhost:4985/db`.

#### `remote_password`

Type

string

Description

The password to use to authenticate with the remote. This password will be redacted in the replication config.

#### `remote_username`

Type

string

Description

The username to use to authenticate with the remote.

#### `replication_id`

Type

string

Description

This is the ID of the replication.

When creating a new replication using a POST request, this will be set to a random UUID if not explicitly set.

When the replication ID is specified in the URL, this must be set to the same replication ID if specifying it at all.

#### `run_as`

Type

string

Description

This is used if you want to specify a user to run the replication as. This means that the replication will only be able to replicate what the user access to what the user has access to.

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