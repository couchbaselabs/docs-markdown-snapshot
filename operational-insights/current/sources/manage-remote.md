---
title: Stream Data from Remote Sources
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/sources/pages/manage-remote.adoc
  xref: xref:enterprise-analytics:sources:manage-remote.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/sources/manage-remote.html)

# Stream Data from Remote Sources

> If you want to stream data to your Operational Insights database, you create a remote data source. 

Operational Insights streams data from remote data sources and stores it in 1 or more collections. As long as it remains connected to the remote source, Operational Insights copies any changes in the remote data to the local copy. If you disconnect it from the remote source, Operational Insights still retains a copy of the data. If you later reconnect the link, it catches up on any updates it missed and continues streaming data changes.

## [](#configuring-streaming)Configuring Streaming

Configuring Operational Insights to stream data from a remote source is a 3-step process:

1. Create an Operational Insights remote link that defines the data source and the credentials to use the data.
2. Create a linked collection to receive the streamed data.
3. Connect the link to start the flow of data.

Operational Insights saves the streamed data into collections dedicated to streamed data. To shadow data in different source topics or collections, you set up a collection for each one. You can associate all of the collections that require the same access credentials with the same link.

## [](#required-privileges)Required Privileges

Your Operational Insights account must have the `**Operational Insights Access**` role along with specific privileges to be able to create a link and its associated collection.

## [](#supported-remote-sources)Supported Remote Sources

Operational Insights supports data event streaming from the following data services:

* Couchbase Server
* Couchbase Capella Operational
* Confluent for Kafka

## [](#creating-a-link-with-an-sdk)Creating a Link with an SDK

Operational Insights uses different types of links to store credentials for accessing different types of data sources. You can use the UI to create links.

To create a link with an SDK, note the following:

* Remote Couchbase: in an SDK, you use the `remoteAnalyticsLink` class and then the `AnalyticsIndexManager` class to create the link.
* Remote non-Couchbase: link creation is not supported by the SDKs. Use the UI to create and manage remote links to [non-Couchbase Data Sources](remote-kafka.md).

For more information about data sources, see [Data Model & Hierarchy](database-objects.md).

## [](#see-also)See Also

* [Stream Data from Couchbase Capella](remote-cb-capella.md)
* [Create a Kafka Pipeline Link](remote-kafka.md)
* [Data Model & Hierarchy](database-objects.md)