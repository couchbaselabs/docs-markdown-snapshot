---
title: Stream Data from Remote Sources
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Capella
    version: ""
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sources/pages/manage-remote.adoc
  xref: xref:analytics:sources:manage-remote.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights-cloud/sources/manage-remote.html)

# Stream Data from Remote Sources

> If you want to stream data to your Operational Insights database, you create a remote data source. 

Operational Insights streams data from remote data sources and stores it in one or more collections. As long as it remains connected to the remote source, Operational Insights copies any changes in the remote data to the local copy. If you disconnect it from the remote source, Operational Insights still retains a copy of the data. If you later reconnect the link, it catches up on any updates it missed and continues streaming data changes.

## [](#configuring-streaming)Configuring Streaming

Configuring Operational Insights to stream data from a remote source is a three-step process:

1. Create an Operational Insights remote link that defines the data source and the credentials to access the data.
2. Create a linked collection to receive the streamed data.
3. Connect the link to start the flow of data.

The collections Operational Insights saves the streamed data into are dedicated to streamed data. To shadow data in different source topics or collections, you set up a collection for each one. You can associate all of the collections that require the same access credentials with the same link.

## [](#required-privileges)Required Privileges

Your Operational Insights account must have either the [Project Owner](../admin/auth/auth-ui.md#project-owner-role) or [Project Manager](../admin/auth/auth-ui.md#project-cluster-manager-role) role to be able to create a link and its associated collection. In addition, you must have credentials to connect to the remote system and access the data you want to stream.

## [](#supported-remote-sources)Supported Remote Sources

Operational Insights supports data event streaming from the following data services:

* Couchbase Capella operational
* Couchbase Server
* Confluent for Kafka
* Amazon MSK (Amazon Managed Streaming for Apache Kafka)

## [](#see-also)See Also

* [Stream Data from Couchbase Capella](remote-cb-capella.md)
* [Create a Kafka Pipeline Link](remote-kafka.md)
* [Access and Organize Data in Operational Insights Services](database-objects.md)