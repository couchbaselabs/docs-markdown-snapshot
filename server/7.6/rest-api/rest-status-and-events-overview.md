---
title: Status and Events
description: Cluster status and important system events can be retrieved by
  means of the REST API.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/rest-api/pages/rest-status-and-events-overview.adoc
  xref: xref:7.6@server:rest-api:rest-status-and-events-overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/rest-api/rest-status-and-events-overview.html)

# Status and Events

> Cluster status and important system events can be retrieved by means of the REST API. 

## [](#apis-in-this-section)APIs in this Section

Couchbase Server provides multiple ways of deriving cluster-status, by means of the REST API. Additionally, _system events_, which provide the details of significant occurrences on the cluster, can inspected — through either _batch_ or _dynamic_ retrieval. Each of the endpoints is listed in the following table.

| HTTP Method | URI                                        | Documented at                                                      |
| ----------- | ------------------------------------------ | ------------------------------------------------------------------ |
| GET         | /pools/default/tasks                       | [Getting Cluster Tasks](rest-get-cluster-tasks.md)                 |
| GET         | /logs/rebalanceReport?reportID=<report-id> | [Getting Cluster Tasks](rest-get-cluster-tasks.md)                 |
| GET         | /pools                                     | [Retrieving Cluster Information](rest-cluster-get.md)              |
| GET         | /pools/default                             | [Viewing Cluster Details](rest-cluster-details.md)                 |
| GET         | /events                                    | [Getting System Events](rest-get-system-events.md)                 |
| GET         | /eventsStreaming                           | [Getting System Events](rest-get-system-events.md)                 |
| GET         | /pools/default/terseClusterInfo            | [Identifying the Orchestrator Node](rest-identify-orchestrator.md) |
| GET         | /pools/nodes                               | [Getting Information on Nodes](rest-node-get-info.md)              |
| GET         | /pools/default/nodeServices                | [Listing Node Services](rest-list-node-services.md)                |