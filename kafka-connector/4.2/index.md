---
title: Introduction
editUrl: https://github.com/couchbase/docs-kafka/edit/release/4.2/modules/ROOT/pages/index.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:4.2@kafka-connector::index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/kafka-connector/4.2/index.html)

# Introduction

> The Couchbase Kafka connector is a plug-in for the [Kafka Connect](https://kafka.apache.org/documentation.html#connect) framework. It provides source and sink components. 

The source connector streams documents from Couchbase Server using the high-performance Database Change Protocol (DCP) and publishes the latest version of each document to a Kafka topic in near real-time.

The sink connector subscribes to Kafka topics and writes the messages to Couchbase Server.

## [](#delivery-guarantees)Delivery Guarantees

Refer to the [Delivery Guarantees](delivery-guarantees.md) page for a description of important limitations.

## [](#compatibility)Compatibility

Refer to the [Compatibility](compatibility.md) page for information on compatible versions of Kafka and Couchbase Server.

## [](#contributing)Contributing

Couchbase welcomes community contributions to the Kafka connector. The [Kafka Connector source code](https://github.com/couchbase/kafka-connect-couchbase) is available on GitHub.