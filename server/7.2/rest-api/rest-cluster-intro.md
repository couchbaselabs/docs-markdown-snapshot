[View original HTML](/server/7.2/rest-api/rest-cluster-intro.html)

> The REST API permits management of nodes and clusters. 

## [](#apis-in-this-section)APIs in this Section

The REST API provides extensive support of the management of nodes and clusters. Each operation is explained in this section. All endpoints are listed in the tables provided below.

### [](#cluster-initialization-and-provisioning)Cluster Initialization and Provisioning

| HTTP Method | URI                             | Documented at                                             |
| ----------- | ------------------------------- | --------------------------------------------------------- |
| POST        | /clusterInit                    | [Initialize a Cluster](rest-initialize-cluster.md)        |
| POST        | /nodes/self/controller/settings | [Initializing a Node](rest-initialize-node.md)            |
| POST        | /settings/web                   | [Establishing Credentials](rest-establish-credentials.md) |
| POST        | /node/controller/rename         | [Naming a Node](rest-name-node.md)                        |
| POST        | /pools/default                  | [Configuring Memory](rest-configure-memory.md)            |
| POST        | /node/controller/setupServices  | [Assigning Services](rest-set-up-services.md)             |
| POST        | /pools/default                  | [Naming a Cluster](rest-name-cluster.md)                  |

### [](#node-addition-and-removal)Node Addition and Removal

| HTTP Method | URI                            | Documented at                                              |
| ----------- | ------------------------------ | ---------------------------------------------------------- |
| POST        | /controller/addNode            | [Adding Nodes to Clusters](rest-cluster-addnodes.md)       |
| POST        | /node/controller/doJoinCluster | [Joining Nodes to Clusters](rest-cluster-joinnode.md)      |
| POST        | /controller/ejectNode          | [Removing Nodes from Clusters](rest-cluster-removenode.md) |

### [](#rebalance)Rebalance

| HTTP Method | URI                                             | Documented at                                                                         |
| ----------- | ----------------------------------------------- | ------------------------------------------------------------------------------------- |
| POST        | /controller/rebalance                           | [Rebalancing the Cluster](rest-cluster-rebalance.md)                                  |
| GET         | /pools/default/rebalanceProgress                | [Getting Rebalance Progress](rest-get-rebalance-progress.md)                          |
| GET         | /pools/default/retryRebalance                   | [Configuring Rebalance Retries](rest-configure-rebalance-retry.md)                    |
| POST        | /pools/default/retryRebalance                   | [Configuring Rebalance Retries](rest-configure-rebalance-retry.md)                    |
| GET         | /pools/default/pendingRetryRebalance            | [Getting Rebalance-Retry Status](rest-get-rebalance-retry.md)                         |
| POST        | /controller/cancelRebalanceRetry/<rebalance-id> | [Canceling Rebalance Retries](rest-cancel-rebalance-retry.md)                         |
| GET         | /settings/rebalance                             | [Limiting Concurrent vBucket Moves](rest-limit-rebalance-moves.md)                    |
| POST        | /settings/rebalance                             | [Limiting Concurrent vBucket Moves](rest-limit-rebalance-moves.md)                    |
| POST        | /internalSettings                               | [Disabling Consistent View Query Results on Rebalance](rest-cluster-disable-query.md) |

### [](#manual-failover)Manual-Failover

| HTTP Method | URI                               | Documented at                                              |
| ----------- | --------------------------------- | ---------------------------------------------------------- |
| POST        | /controller/failOver              | [Performing Hard Failover](rest-node-failover.md)          |
| POST        | /controller/startGracefulFailover | [Performing Graceful Failover](rest-failover-graceful.md)  |
| POST        | /controller/setRecoveryType       | [Setting Recovery Type](rest-node-recovery-incremental.md) |

### [](#auto-failover)Auto-Failover

| HTTP Method | URI                               | Documented at                                                               |
| ----------- | --------------------------------- | --------------------------------------------------------------------------- |
| GET         | /settings/autoFailover            | [Retrieving Auto-Failover Settings](rest-cluster-autofailover-settings.md)  |
| POST        | /settings/autoFailover            | [Enabling and Disabling Auto-Failover](rest-cluster-autofailover-enable.md) |
| POST        | /settings/autoFailover/resetCount | [Resetting Auto-Failover](rest-cluster-autofailover-reset.md)               |
| POST        | /controller/setRecoveryType       | [Setting Recovery Type](rest-node-recovery-incremental.md)                  |

### [](#settings-and-connections)Settings and Connections

| HTTP Method | URI                                               | Documented at                                                                                                       |
| ----------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| GET         | /internalSettings                                 | [Managing Internal Settings](rest-get-internal-setting.md)                                                          |
| POST        | /internalSettings                                 | [Managing Internal Settings](rest-get-internal-setting.md)                                                          |
| GET         | /settings/maxParallelIndexers                     | [Managing Internal Settings](rest-get-internal-setting.md)                                                          |
| POST        | /settings/maxParallelIndexers                     | [Managing Internal Settings](rest-get-internal-setting.md)                                                          |
| GET         | /pools/default/settings/memcached/global          | [Managing Cluster Connections](rest-manage-cluster-connections.md)                                                  |
| POST        | /pools/default/settings/memcached/global          | [Managing Cluster Connections](rest-manage-cluster-connections.md)                                                  |
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
| GET         | /pools/nodes                               | [Getting Information on Nodes](rest-node-get-info.md)              |
| GET         | /pools/default/nodeServices                | [Listing Node Services](rest-list-node-services.md)                |

### [](#statistics)Statistics

| HTTP Method | URI                                                               | Documented at                                              |
| ----------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| GET         | /prometheus\_sd\_config                                           | [Prometheus Discovery API](rest-discovery-api.md)          |
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