---
title: Nodes and Clusters API
description: The REST API permits management of nodes and clusters.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/reference/pages/rest-cluster-intro.adoc
  xref: xref:enterprise-analytics:reference:rest-cluster-intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/reference/rest-cluster-intro.html)

# Nodes and Clusters API

> The REST API permits management of nodes and clusters. 

## [](#apis-in-this-section)APIs in this Section

The REST API provides extensive support of the management of nodes and clusters. Each operation is explained in this section. All endpoints are listed in the tables provided below.

### [](#cluster-initialization-and-provisioning)Cluster Initialization and Provisioning

| HTTP Method | URI                             | Documented at                                              |
| ----------- | ------------------------------- | ---------------------------------------------------------- |
| POST        | /clusterInit                    | [Initialize a Cluster](rest-initialize-cluster.md)         |
| POST        | /nodes/self/controller/settings | [Initializing a Node](rest-initialize-node.md)             |
| POST        | /settings/web                   | [Establishing Credentials](rest-establish-credentials.md)  |
| POST        | /node/controller/rename         | [Naming a Node](rest-name-node.md)                         |
| POST        | /pools/default                  | [Configuring Memory](rest-configure-memory.md)             |
| POST        | /node/controller/setupServices  | [Assigning Services](#reference:rest-set-up-services.adoc) |
| POST        | /pools/default                  | [Naming a Cluster](rest-name-cluster.md)                   |

### [](#node-addition-and-removal)Node Addition and Removal

| HTTP Method | URI                            | Documented at                                              |
| ----------- | ------------------------------ | ---------------------------------------------------------- |
| POST        | /controller/addNode            | [Adding Nodes to Clusters](rest-cluster-addnodes.md)       |
| POST        | /node/controller/doJoinCluster | [Joining Nodes to Clusters](rest-cluster-joinnode.md)      |
| POST        | /controller/ejectNode          | [Removing Nodes from Clusters](rest-cluster-removenode.md) |

### [](#rebalance)Rebalance

| HTTP Method | URI                                             | Documented at                                                                                      |
| ----------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| POST        | /controller/rebalance                           | [Rebalancing the Cluster](rest-cluster-rebalance.md)                                               |
| GET         | /pools/default                                  | [Getting Rebalance Reason Codes](rest-retrieve-cluster-rebalance-reason-codes.md)                  |
| GET         | /pools/default/rebalanceProgress                | [Getting Rebalance Progress](rest-get-rebalance-progress.md)                                       |
| GET         | /pools/default/retryRebalance                   | [Configuring Rebalance Retries](rest-configure-rebalance-retry.md)                                 |
| POST        | /pools/default/retryRebalance                   | [Configuring Rebalance Retries](rest-configure-rebalance-retry.md)                                 |
| GET         | /pools/default/pendingRetryRebalance            | [Getting Rebalance-Retry Status](rest-get-rebalance-retry.md)                                      |
| POST        | /controller/cancelRebalanceRetry/<rebalance-id> | [Canceling Rebalance Retries](rest-cancel-rebalance-retry.md)                                      |
| GET         | /settings/rebalance                             | [Limiting Concurrent vBucket Moves](#reference:rest-limit-rebalance-moves.adoc)                    |
| POST        | /settings/rebalance                             | [Limiting Concurrent vBucket Moves](#reference:rest-limit-rebalance-moves.adoc)                    |
| POST        | /internalSettings                               | [Disabling Consistent View Query Results on Rebalance](#reference:rest-cluster-disable-query.adoc) |

### [](#manual-failover)Manual-Failover

| HTTP Method | URI                               | Documented at                                                           |
| ----------- | --------------------------------- | ----------------------------------------------------------------------- |
| POST        | /controller/failOver              | [Performing Hard Failover](rest-node-failover.md)                       |
| POST        | /controller/startGracefulFailover | [Performing Graceful Failover](#reference:rest-failover-graceful.adoc)  |
| POST        | /controller/setRecoveryType       | [Setting Recovery Type](#reference:rest-node-recovery-incremental.adoc) |

### [](#auto-failover)Auto-Failover

| HTTP Method | URI                               | Documented at                                                               |
| ----------- | --------------------------------- | --------------------------------------------------------------------------- |
| GET         | /settings/autoFailover            | [Retrieving Auto-Failover Settings](rest-cluster-autofailover-settings.md)  |
| POST        | /settings/autoFailover            | [Enabling and Disabling Auto-Failover](rest-cluster-autofailover-enable.md) |
| POST        | /settings/autoFailover/resetCount | [Resetting Auto-Failover](rest-cluster-autofailover-reset.md)               |
| POST        | /controller/setRecoveryType       | [Setting Recovery Type](#reference:rest-node-recovery-incremental.adoc)     |

### [](#settings-and-connections)Settings and Connections

| HTTP Method | URI                                               | Documented at                                                                                                       |
| ----------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| GET         | /internalSettings                                 | [Managing Internal Settings](#reference:rest-get-internal-setting.adoc)                                             |
| POST        | /internalSettings                                 | [Managing Internal Settings](#reference:rest-get-internal-setting.adoc)                                             |
| GET         | /settings/maxParallelIndexers                     | [Managing Internal Settings](#reference:rest-get-internal-setting.adoc)                                             |
| POST        | /settings/maxParallelIndexers                     | [Managing Internal Settings](#reference:rest-get-internal-setting.adoc)                                             |
| GET         | /pools/default/settings/memcached/global          | [Managing Cluster Connections](#reference:rest-manage-cluster-connections.adoc)                                     |
| POST        | /pools/default/settings/memcached/global          | [Managing Cluster Connections](#reference:rest-manage-cluster-connections.adoc)                                     |
| PUT         | /node/controller/setupAlternateAddresses/external | [Managing Alternate Addresses](rest-set-up-alternate-address.md)                                                    |
| DELETE      | /node/controller/setupAlternateAddresses/external | [Managing Alternate Addresses](rest-set-up-alternate-address.md)                                                    |
| GET         | /settings/alerts                                  | [Getting Alert Settings](rest-cluster-email-notifications.md#rest-cluster-alerts-get)                               |
| POST        | /settings/alerts                                  | [Enabling and Disabling Email Notifications](rest-cluster-email-notifications.md#rest-cluster-alerts-enabledisable) |
| POST        | /settings/alerts/sendTestEmail                    | [Sending Test Emails](rest-cluster-email-notifications.md#rest-cluster-alerts-send)                                 |

### [](#status-and-events)Status and Events

| HTTP Method | URI                                        | Documented at                                                      |
| ----------- | ------------------------------------------ | ------------------------------------------------------------------ |
| GET         | /pools/default/tasks                       | [Getting Cluster Tasks](rest-get-cluster-tasks.md)                 |
| GET         | /logs/rebalanceReport?reportID=<report-id> | [Getting Cluster Tasks](rest-get-cluster-tasks.md)                 |
| GET         | /pools                                     | [Retrieving Cluster Information](rest-cluster-get.md)              |
| GET         | /pools/default                             | [Viewing Cluster Details](rest-cluster-details.md)                 |
| GET         | /events                                    | [Getting System Events](rest-get-system-events.md)                 |
| GET         | /eventsStreaming                           | [Getting System Events](rest-get-system-events.md)                 |
| GET         | /pools/default/terseClusterInfo            | [Identifying the Orchestrator Node](rest-identify-orchestrator.md) |
| GET         | /pools/nodes                               | [Getting information about Nodes](rest-node-get-info.md)           |
| GET         | /pools/default/nodeServices                | [Listing Node Services](rest-list-node-services.md)                |

### [](#statistics)Statistics

| HTTP Method | URI                                                               | Documented at                                              |
| ----------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| GET         | /pools/default/stats/range/<metric\_name>/\[function-expression\] | [Getting a Single Statistic](rest-statistics-single.md)    |
| POST        | /pools/default/stats/range                                        | [Getting Multiple Statistics](rest-statistics-multiple.md) |

### [](#logging)Logging

| HTTP Method | URI                              | Documented at                                                 |
| ----------- | -------------------------------- | ------------------------------------------------------------- |
| POST        | /controller/startLogsCollection  | [Collecting Logs](rest-manage-log-collection.md)              |
| POST        | /controller/cancelLogsCollection | [Collecting Logs](rest-manage-log-collection.md)              |
| GET         | /pools/default/tasks             | [Getting Cluster Tasks](rest-get-cluster-tasks.md)            |
| GET         | /diag                            | [Retrieving Diagnostic and Log Information](rest-logs-get.md) |
| GET         | /sasl\_logs                      | [Retrieving Diagnostic and Log Information](rest-logs-get.md) |
| POST        | /logClientError                  | [Logging Client-Side Errors](rest-client-logs.md)             |