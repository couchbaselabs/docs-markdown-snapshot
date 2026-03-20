---
title: Stream Data from Remote Sources
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sources/pages/manage-remote.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:enterprise-analytics:sources:manage-remote.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sources/manage-remote.html)

# Stream Data from Remote Sources

> If you want to stream data to your Enterprise Analytics database, you create a remote data source. 

Enterprise Analytics streams data from remote data sources and stores it in 1 or more collections. As long as it remains connected to the remote source, Enterprise Analytics copies any changes in the remote data to the local copy. If you disconnect it from the remote source, Enterprise Analytics still retains a copy of the data. If you later reconnect the link, it catches up on any updates it missed and continues streaming data changes.

## [](#configuring-streaming)Configuring Streaming

Configuring Enterprise Analytics to stream data from a remote source is a 3-step process:

1. Create an Enterprise Analytics remote link that defines the data source and the credentials to use the data.
2. Create a linked collection to receive the streamed data.
3. Connect the link to start the flow of data.

Enterprise Analytics saves the streamed data into collections dedicated to streamed data. To shadow data in different source topics or collections, you set up a collection for each one. You can associate all of the collections that require the same access credentials with the same link.

## [](#required-privileges)Required Privileges

Your Enterprise Analytics account must have the `**Enterprise Analytics Access**` role along with specific privileges to be able to create a link and its associated collection.

## [](#supported-remote-sources)Supported Remote Sources

Enterprise Analytics supports data event streaming from the following data services:

* Couchbase Server
* Couchbase Capella Operational
* Confluent for Kafka

## [](#creating-a-link-with-an-sdk)Creating a Link with an SDK

Enterprise Analytics uses different types of links to store credentials for accessing different types of data sources. You can use the UI to create links.

To create a link with an SDK, note the following:

* Remote Couchbase: in an SDK, you use the `remoteAnalyticsLink` class and then the `AnalyticsIndexManager` class to create the link.
* Remote non-Couchbase: link creation is not supported by the SDKs. Use the UI to create and manage remote links to [non-Couchbase Data Sources](#kafka).

For more information about data sources, see [Access and Organize Data in Enterprise Analytics](database-objects.md).

## [](#see-also)See Also

* [Stream Data from Couchbase Capella](remote-cb-capella.md)
* [Create a Kafka Pipeline Link](remote-kafka.md)
* [Access and Organize Data in Enterprise Analytics](database-objects.md)