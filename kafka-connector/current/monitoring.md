---
title: Monitoring the Connector
editUrl: https://github.com/couchbase/docs-kafka/edit/release/4.3/modules/ROOT/pages/monitoring.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:kafka-connector::monitoring.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/kafka-connector/current/monitoring.html)

# Monitoring the Connector

> Resources for monitoring the connector's performance. 

The Kafka Connect framework exposes basic status information over a REST interface. Fine-grained metrics, including the number of processed messages and the rate of processing, are available via JMX. For more information, see [Monitoring Kafka Connect and Connectors](https://docs.confluent.io/current/connect/managing/monitoring.html) (published by Confluent, also applies to a standard Apache Kafka distribution).