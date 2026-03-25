---
title: Inter-Sync&#160;Gateway Replication Configuration
description: Using Sync Gateway's Admin REST API to configure and manage
  inter-Sync&#160;Gateway replications
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/configuration-schema-isgr.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.0@sync-gateway::configuration-schema-isgr.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/configuration-schema-isgr.html)

# Inter-Sync&#160;Gateway Replication Configuration

> Using Sync Gateway’s Admin REST API to configure and manage inter-Sync Gateway replications  

_Related topics_: [Overview](configuration-overview.md) | [Bootstrap](configuration-schema-bootstrap.md) | [Database](configuration-schema-database.md) | [Database Security](#configuration-schema-db-security&.adoc#8212;​page}) | [Access Control](configuration-schema-access-control.md) | [Import](configuration-schema-import-filter.md) | Inter-Sync Gateway Replication

> [!IMPORTANT]
> Pre-3.0 Legacy Configuration Equivalents
> 
> This content describes configuration for Sync Gateway 3.0 and higher — for legacy configuration, see: [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

## [](#introduction)Introduction

In 3.0 we use the Admin REST API to provision persistent configuration changes. This content introduces the [Add or Update a Replication](#lbl-upsert-replication) endpoint for convenience — see [Replication](rest-api-admin.md#/Replication) for a full description of the endpoints available.

Using CA Certificates

Required CA certificates must be added to the system certificate pool.

On Linux, this is done using one of the following methods:

* Adding the location of the certificate to `SSL_CERT_FILE` environment variable,
* Placing the certificate in a location pointed to by the `SSL_CERT_DIR` environment variable.
* Using one of the system-dependent locations [listed in this file](https://go.dev/src/crypto/x509/root%5Flinux.go).

For Windows-based systems, add CA certificate files to the system root certificate store.

## [](#lbl-upsert-replication)Add or Update a Replication

PUT {db}/_config/_replication

The _replication endpoint is used to manage both \_ad hoc_ and _persistent_ replication operations. 

Using a PUT request you can update (or insert, if it doesn’t exist) a set of replication details.

**To cancel a replication**You can cancel continuous replications by adding the cancel field to the JSON request object and setting the value to true.

Note that the structure of the request must be identical to the original for the cancellation request to be honoured.

For example, if you requested continuous replication, the cancellation request must also contain the continuous field.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Replicator

## [](#parameters)Parameters

| Type     | Name                           | Description                                                                                                                                                                                                                                                                                                 | Schema                                        |
| -------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **Path** | **db** _required_              | Database name                                                                                                                                                                                                                                                                                               | string                                        |
| **Path** | **replicationID** _required_   | If supplied, the <i>replicationID</i> parameter must be a valid replication id. If it is not supplied for a <i>new</i> replication\*, then a random UUID is generated.                                                                                                                                      | string                                        |
| **Body** | **ReplicationBody** _optional_ | This replication request message body is a JSON document that comprises all the properties required to upsert a replication. If the replicationID matches an existing replication\_id then the values of any properties provided in the body are used to update the existing replication’s property values. | [Replication\_model](#%5Freplication%5Fmodel) |

## [](#responses)Responses

| HTTP Code | Description                       | Schema                                         |
| --------- | --------------------------------- | ---------------------------------------------- |
| **200**   | Replication successfully updated  | [ReplicationResponse](#%5Freplicationresponse) |
| **201**   | Replication successfully inserted | [ReplicationResponse](#%5Freplicationresponse) |

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

## [](#replication)Schema

This section shows Sync Gateway’s replication configuration settings in schema format for convenience in constructing JSON models for use in the Admin REST API.

The configuration settings described here are provisioned through the [Replication](rest-api-admin.md#/Replication) endpoints.

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
* [Inter-Sync Gateway Replication](#)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)