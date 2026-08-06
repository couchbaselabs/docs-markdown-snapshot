---
title: Channel History Management
description: Remove historical channel entries from document and user metadata
  in Sync Gateway 4.1 to reduce metadata bloat and prevent unnecessary
  revocations.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.1/modules/manage/pages/channel-history.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:sync-gateway:manage:channel-history.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/manage/channel-history.html)

# Channel History Management

> Remove historical channel entries from document and user metadata in Sync Gateway 4.1 to reduce metadata bloat and prevent unnecessary revocations.  

Related _Manage_ topics: [Release Notes](../product-notes/release-notes.md)

## [](#overview)Overview

Sync Gateway tracks channel assignments for both documents and users in internal metadata. This history accumulates over time and is retained indefinitely by default.

In high-churn deployments where documents and users frequently enter and leave channels, this history can grow large enough to cause two problems:

* **Metadata bloat:** Document `_sync` attributes and user documents grow continuously, increasing storage overhead and degrading performance.
* **Unnecessary revocations:** When a Couchbase Lite client performs a zero-checkpoint (clear-start) replication, such as after an app reinstall or checkpoint rollback, Sync Gateway replays the full channel history. Old revocation entries in that history are re-sent to the client even for channels that are no longer relevant.

Sync Gateway 4.1 introduces Admin REST API endpoints that let administrators selectively remove historical channel entries from documents and users. Both operations are non-destructive to document content and do not interrupt active replications.

## [](#document-channel-history)Document Channel History

### [](#about-document-channel-history)About Document Channel History

Sync Gateway stores channel assignment history in the `_sync` extended attribute (xattr) of each document. This history tracks which channels a document has been assigned to and when it left each channel, using database sequence numbers rather than timestamps.

Each time a document is assigned to a channel and then removed, a new entry is added to its channel history. For documents that move through many channels over time, this history grows without bound.

You can remove channel history entries older than a specified sequence number. If you use the current database head sequence, all entries in the channel history is removed.

The operation removes only historical entries. It does not affect the document body, active channel assignments, or ongoing replications.

### [](#identify-a-safe-sequence-boundary)Identify a Safe Sequence Boundary

Before pruning, identify the sequence number to use as the boundary. All inactive channel history entries with sequences below this number are removed.

To get the current database head sequence, call `GET /{db}/` and read the `update_seq` field from the response:

```bash
GET /{db}/
```

```json
{
  "db_name": "db",
  "update_seq": 98765,
  ...
}
```

Use the `update_seq` value as the `seq` parameter to perform a deep clean of all historical channel entries for the targeted documents.

> [!NOTE]
> Choose the sequence boundary carefully. Any inactive channel history at or before the sequence you provide is permanently removed. This operation cannot be undone.

### [](#retrieve-document-channel-history)Retrieve Document Channel History

Retrieve the channel revocation history for a document to review which channels are recorded and at which sequences the document left each channel. Use this information to identify a suitable sequence boundary before compacting, or to select a specific sequence for a partial compact.

**Endpoint:** `GET /{keyspace}/_channel_history/{docid}`

**Required RBAC roles:** Sync Gateway Application, Sync Gateway Application Read Only

| Path parameter      | Description                                                                                                                                                 |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| keyspace (required) | The keyspace to run the operation against. A keyspace is a dot-separated string comprised of a database name and, optionally, a named scope and collection. |
| docid (required)    | The document ID whose channel history you want to retrieve.                                                                                                 |

**Example request:**

```bash
GET /mydb/_channel_history/order-12345
```

**Example response:**

```json
{
  "orders-2023": [
    5,
    7
  ],
  "orders-archived": [7]
}
```

The response maps each channel name to an array of sequences at which the document was removed from that channel. Multiple sequences for a given channel indicate the document left and re-entered that channel more than once.

For the full API reference, see [GET /{keyspace}/\_channel\_history/{docid}](../rest-api/rest%5Fapi%5Fadmin.md#tag/Document/operation/get%5Fkeyspace-%5Fchannel%5Fhistory).

### [](#compact-document-channel-history)Compact Document Channel History

Remove channel history entries from one or more documents older than a specified sequence number.

**Endpoint:** `POST /{keyspace}/_channel_history/{docid}/compact`

**Required RBAC roles:** Sync Gateway Application

| Request body field | Description                                                                                                                            |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| seq (required)     | Sequence number boundary. All channel history entries with sequences earlier than this value are removed from the specified documents. |

**Example request:**

```bash
POST /mydb/_channel_history/order-12345/compact
```

```json
{
  "seq": 98765
}
```

**Example response:**

```json
{
  "compacted_channels": [
    "orders-2023",
    "orders-archived"
  ]
}
```

The response is a list of channels that were compacted.

For the full API reference, see [POST /{keyspace}/\_channel\_history/{docid}/compact](../rest-api/rest%5Fapi%5Fadmin.md#tag/Document/operation/post%5Fkeyspace-%5Fchannel%5Fhistory-compact).

## [](#user-access-history)User Access History

### [](#about-user-access-history)About User Access History

Sync Gateway maintains a history of channel access grants and revocations for each user. In deployments where channels are frequently granted and revoked, this history grows indefinitely in the user's metadata document.

The operational impact is specific to zero-checkpoint replications. When a Couchbase Lite client performs a clear-start replication, such as after an app reinstall or a checkpoint rollback, Sync Gateway replays the user's full channel history. Old revocation entries in that history are re-sent to the client for channels that are no longer relevant, causing Sync Gateway to perform unnecessary work and potentially triggering conflict resolution on the client.

Selectively removing channel entries from the history prevents Sync Gateway from sending revocations for those channels during future zero-checkpoint replications. The operation does not affect the user's current channel access, does not modify underlying documents, and does not interrupt active continuous replications.

### [](#retrieve-user-access-history)Retrieve User Access History

Before compacting, retrieve the current channel access history for a user to confirm which channels are recorded.

**Endpoint:** `GET /{db}/_user/{name}/_access_history`

**Required RBAC roles:** Sync Gateway Architect, Sync Gateway Application, Sync Gateway Application Read Only

**Example request:**

```bash
GET /mydb/_user/alice/_access_history
```

**Example response:**

```json
{
  "channels": {
    "inventory": {
      "default": [
        "warehouse-east",
        "warehouse-west-2023",
        "warehouse-archived"
      ]
    }
  }
}
```

The response shows all access history entries organised by scope and collection.

For the full API reference, see [GET /{db}/\_user/{name}/\_access\_history](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Security/operation/get%5Fdb-%5Fuser-name-%5Faccess%5Fhistory).

### [](#compact-user-access-history)Compact User Access History

Remove specific channel entries from a user's channel access history.

**Endpoint:** `POST /{db}/_user/{name}/_access_history/compact`

**Required RBAC roles:** Sync Gateway Architect, Sync Gateway Application

Provide the channels you want to remove, organised by scope and collection.

**Example request:**

```bash
POST /mydb/_user/alice/_access_history/compact
```

```json
{
  "channels": {
    "inventory": {
      "default": [
        "warehouse-west-2023",
        "warehouse-archived"
      ]
    }
  }
}
```

**Example response:**

```json
{
  "compacted_channels": {
    "inventory": {
      "default": [
        "warehouse-west-2023",
        "warehouse-archived"
      ]
    }
  }
}
```

The response confirms the channels removed from the user's access history.

For the full API reference, see [POST /{db}/\_user/{name}/\_access\_history/compact](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Security/operation/post%5Fdb-%5Fuser-name-%5Faccess%5Fhistory-compact).

## [](#api-reference-summary)API Reference Summary

| Endpoint                                       | Method | Description                                                                                          |
| ---------------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------- |
| /{keyspace}/\_channel\_history/{docid}         | GET    | Retrieve inactive channel history entries for a document.                                            |
| /{keyspace}/\_channel\_history/{docid}/compact | POST   | Remove inactive channel history entries from the specified document older than a specified sequence. |
| /{db}/\_user/{name}/\_access\_history          | GET    | Retrieve the full channel access history for a user.                                                 |
| /{db}/\_user/{name}/\_access\_history/compact  | POST   | Remove specific channel entries from a user's channel access history.                                |

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