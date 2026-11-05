---
title: Hadoop Connector
description: The Couchbase Hadoop Connector has reached End-of-Life (EOL),
  <em>and is no longer supported</em>.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
  topic_type: landing-page
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/connectors/pages/hadoop-1.2/hadoop.adoc
  xref: xref:7.6@server:connectors:hadoop-1.2/hadoop.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/connectors/hadoop-1.2/hadoop.html)

# Hadoop Connector

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

The Couchbase Hadoop Connector has reached End-of-Life (EOL), _and is no longer supported_. The Couchbase Hadoop Connector is not compatible with Couchbase Server 5.x or 6.x; because it relies on the TAP feed API which has been removed since Couchbase Server 5.x, in favor of the DCP feed. We recommend existing Hadoop integrations to migrate to a supported version of the [Couchbase Kafka Connector](../../../../kafka-connector/current/index.md).