---
title: Hadoop Connector
description: The Couchbase Hadoop Connector has reached End-of-Life (EOL),
  <em>and is no longer supported</em>.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/connectors/pages/hadoop-1.2/hadoop.adoc
  xref: xref:7.6@server:connectors:hadoop-1.2/hadoop.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/connectors/hadoop-1.2/hadoop.html)

# Hadoop Connector

The Couchbase Hadoop Connector has reached End-of-Life (EOL), _and is no longer supported_. The Couchbase Hadoop Connector is not compatible with Couchbase Server 5.x or 6.x; because it relies on the TAP feed API which has been removed since Couchbase Server 5.x, in favor of the DCP feed. We recommend existing Hadoop integrations to migrate to a supported version of the [Couchbase Kafka Connector](../../../../kafka-connector/current/index.md).