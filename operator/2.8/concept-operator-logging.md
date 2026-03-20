---
title: Kubernetes Operator Logging
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.8/modules/ROOT/pages/concept-operator-logging.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.8@operator::concept-operator-logging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.8/concept-operator-logging.html)

# Kubernetes Operator Logging

> The Kubernetes Operator provides flexible logging support to enable failure detection and alerting. 

The Operator provides flexible logging support to enable failure detection and alerting. It is also a key resource when submitting a support request with the [cbopinfo](tools/cbopinfo.md) tool. This page describes logging that is specific to the Kubernetes Operator itself. For information about Couchbase cluster logging, refer to [Couchbase Server Logging](concept-couchbase-logging.md).

## [](#overview)Overview

The Kubernetes Operator [emits logs](howto-manage-operator-logging.md) on the pod console. Logs are structured as JSON with one entry per line, thus providing a simple and stable foundation for machine parsing and ingestion into 3rd-party logging databases.

Example of Kubernetes Operator Logs

```json
{"level":"info","ts":1580377225.2966235,"logger":"couchbaseutil","msg":"Cluster status","cluster":"default/cb-example","balance":"balanced","rebalancing":false}
{"level":"info","ts":1580377225.296685,"logger":"couchbaseutil","msg":"Node status","cluster":"default/cb-example","name":"cb-example-0000","version":"6.5.0","class":"all_services","managed":true,"status":"warmup"}
{"level":"info","ts":1580377225.6940928,"logger":"cluster","msg":"Pods warming up, skipping","cluster":"default/cb-example"}
{"level":"info","ts":1580377225.892829,"logger":"cluster","msg":"Reconcile completed","cluster":"default/cb-example"}
{"level":"info","ts":1580377226.7565176,"logger":"cluster","msg":"Creating XDCR remote cluster","cluster":"default/cb-example","remote":"remote"}
```

> [!TIP]
> Popular logging solutions that feature native support for JSON input
> 
> * [Fluentd JSON parser](https://docs.fluentd.org/parser/json)
> * [Logstash JSON codec](https://www.elastic.co/guide/en/logstash/current/plugins-codecs-json%5Flines.html)

## [](#related-content)Related Content

* [Kubernetes Operator Troubleshooting](howto-manage-operator-logging.md).
* [Kubernetes Operator Log Attributes](reference-operator-logging.md).
* [Operator Deployment Settings](reference-operator-configuration.md).