---
title: Inter-Sync&#160;Gateway Replication Configuration
description: Using Sync Gateway's Admin REST API to configure and manage
  inter-Sync&#160;Gateway replications
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/configuration/pages/configuration-schema-isgr.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:sync-gateway:configuration:configuration-schema-isgr.adoc[]
---

[View original HTML](/sync-gateway/current/configuration/configuration-schema-isgr.html)

# Inter-Sync&#160;Gateway Replication Configuration

> Using Sync Gateway’s Admin REST API to configure and manage inter-Sync Gateway replications  

_Related topics_: [Overview](configuration-overview.md) | [Bootstrap](configuration-schema-bootstrap.md) | [Database](configuration-schema-database.md) | [Database Security](configuration-schema-db-security.md) | [Access Control](configuration-schema-access-control.md) | [Import](configuration-schema-import-filter.md) | [Inter-Sync Gateway Replication](configuration-schema-isgr.md)

> [!IMPORTANT]
> Pre-3.0 Legacy Configuration Equivalents
> 
> This content describes configuration for Sync Gateway 3.0 and higher — for legacy configuration, see: [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

## [](#introduction)Introduction

Sync Gateway 3.0 and later uses the Admin REST API to provision persistent configuration changes. This page introduces the [PUT/{url}/{db}/\_replication/{replicationId}](../rest-api/rest%5Fapi%5Fadmin.md#tag/Replication/operation/put%5Fdb-%5Freplication-replicationid) endpoint for convenience — see [Replication](../rest-api/rest%5Fapi%5Fadmin.md#tag/Replication) for a full description of the endpoints available.

Using CA Certificates

You must add required CA certificates to the system certificate pool.

On Linux, you can do this using 1 of the following methods:

* Adding the location of the certificate to `SSL_CERT_FILE` environment variable,
* Placing the certificate in a location pointed to by the `SSL_CERT_DIR` environment variable.
* Using 1 of the system-dependent locations [listed in this file](https://go.dev/src/crypto/x509/root%5Flinux.go).

For Windows-based systems, add CA certificate files to the system root certificate store.

## [](#upsert-a-replication)Upsert a Replication

For complete endpoint details, see [PUT/{url}/{db}/\_replication/{replicationId}](../rest-api/rest%5Fapi%5Fadmin.md#tag/Replication/operation/put%5Fdb-%5Freplication-replicationid).

### [](#example)Example

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

This section shows the replication configuration settings in schema format. Use these schemas to construct JSON models for the Admin REST API.

The configuration settings described here are provisioned through the [Replication](../rest-api/rest%5Fapi%5Fadmin.md#tag/Replication) endpoints.

ERROR (template-block): Data file attachment$bundled-admin.yaml not resolved

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