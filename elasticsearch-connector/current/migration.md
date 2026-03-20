---
title: Migration Considerations
editUrl: https://github.com/couchbase/docs-elastic-search/edit/main/modules/ROOT/pages/migration.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:elasticsearch-connector::migration.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/elasticsearch-connector/current/migration.html)

# Migration Considerations

> Prior to version 4, the Couchbase Elasticsearch connector was implemented as an Elasticsearch plug-in. Here’s what you need to know if you’re migrating from the plug-in to the new standalone connector. 

In this document, version 4 of the connector is referred to as the "standalone connector" to distinguish it from the Elasticsearch plug-in of prior versions.

## [](#upgrading-from-the-plug-in)Upgrading from the Plug-in

> [!CAUTION]
> This is a major version upgrade. Because the plug-in and the standalone connector are so different, there is no online upgrade process.

The standalone connector stores its replication state in a way that is incompatible with the plug-in. Unfortunately, the standalone connector cannot continue replicating from exactly where the plug-in stops.

### [](#upgrade-with-re-streaming)Upgrade with Re-streaming

The **recommended approach** is to uninstall the plug-in and restart the Elasticsearch nodes for the removal to take effect. Then start the standalone connector and allow it to re-stream all Couchbase documents to Elasticsearch.

If you intend to use the new metadata fields introduced by the new connector, this approach ensures all documents have complete metadata.

### [](#upgrade-with-checkpoint-overlap)Upgrade with Checkpoint Overlap

If re-streaming is not possible for your deployment, consider this workaround.

1. Use the new checkpoint management tools to create a checkpoint from the current state of the bucket (with `cbes-checkpoint-clear --catch-up`).
2. Allow the plug-in to continue replicating documents until it has processed all changes that occurred prior to when you set the checkpoint.
3. Uninstall the plugin and restart the Elasticsearch nodes for the removal to take effect.
4. Start the standalone connector, which will begin streaming from the point in Couchbase history when you set the checkpoint.

## [](#parent-child-relationships)Parent-Child Relationships

Elasticsearch 6 no longer supports parent-child relationships. Because the connector is primarily focused on Elasticsearch 6 and beyond, parent-child relationships are no longer supported by the connector.

## [](#document-structure-and-metadata)Document structure and metadata

By default, Elasticsearch documents created by the standalone connector have the same structure and metadata as those created by the plug-in, with the addition of new metadata fields that can be used to build a Couchbase Mutation Token.

__Table 1\. Metadata Fields__
| Name       | Datatype | New in 4.0? |
| ---------- | -------- | ----------- |
| vbucket    | integer  | ✓           |
| vbuuid     | long     | ✓           |
| seqno      | long     | ✓           |
| revSeqno   | long     | ✓           |
| cas        | long     | ✓           |
| lockTime   | integer  | ✓           |
| rev        | string   |             |
| flags      | integer  |             |
| expiration | integer  |             |
| id         | string   |             |