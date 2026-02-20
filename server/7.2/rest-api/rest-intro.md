---
title: REST API reference
description: The REST API supports the management of Couchbase-Server clusters.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/rest-intro.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:rest-api:rest-intro.adoc[]
---

[View original HTML](/server/7.2/rest-api/rest-intro.html)

# REST API reference

> The REST API supports the management of Couchbase-Server clusters. 

The REST API supports the management of Couchbase-Server clusters. This includes cluster-creation and the definition of nodes, services, and server groups. The API also supports the extensive retrieval of statistics.

This page provides a complete list of HTTP methods and URIs. It also lists [HTTP Request Headers](#http-request-headers) and [HTTP Response Codes](#http-response-codes).

## [](#nodes-and-clusters-api)Nodes and Clusters API

The Cluster API provides support for managing and retrieving information on clusters. It also provides support for managing _rebalance_, _failover_, and _server group awareness_. The APIs for each area are assigned a table, below.

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

## [](#buckets-api)Buckets API

Couchbase Server keeps items in _buckets_. Before an item can be saved, a bucket must exist for it. Buckets can be created and managed by means of the following REST API.

| HTTP Method | URI                                                                 | Documented at                                                |
| ----------- | ------------------------------------------------------------------- | ------------------------------------------------------------ |
| POST        | /pools/default/buckets                                              | [Creating and Editing Buckets](rest-bucket-create.md)        |
| POST        | /pools/default/buckets/<bucketName>                                 | [Creating and Editing Buckets](rest-bucket-create.md)        |
| GET         | /pools/default/buckets                                              | [Getting Bucket Information](rest-buckets-summary.md)        |
| GET         | /pools/default/buckets/<bucket-name>                                | [Getting Bucket Information](rest-buckets-summary.md)        |
| POST        | /pools/default/buckets/<bucket-name>/nodes                          | [Listing Nodes by Bucket](rest-retrieve-bucket-nodes.md)     |
| GET         | /pools/default/stats/range/\[metric\_name\]/\[function-expression\] | [Getting a Single Statistic](rest-statistics-single.md)      |
| POST        | /pools/default/stats/range                                          | [Getting Multiple Statistics](rest-statistics-multiple.md)   |
| GET         | /pools/default/buckets/default                                      | [Getting Bucket Streaming URI](rest-buckets-streamingURI.md) |
| DELETE      | /pools/default/buckets/\[bucket-name\]                              | [Deleting Buckets](rest-bucket-delete.md)                    |
| DELETE      | /pools/default/buckets/\[bucket-name\]                              | [Deleting Buckets](rest-bucket-delete.md)                    |
| POST        | /pools/default/buckets/\[bucket-name\]/controller/doFlush           | [Flushing Buckets](rest-bucket-flush.md)                     |
| GET         | /sampleBuckets                                                      | [Managing Sample Buckets](rest-sample-buckets.md)            |
| POST        | /sampleBuckets/install                                              | [Managing Sample Buckets](rest-sample-buckets.md)            |

## [](#scopes-and-collections-api)Scopes and Collections API

Couchbase Server provides _scopes_ and _collections_; allowing documents to be categorized and organized, within a bucket. The REST API provided for the creation and management of scopes and collections is listed below.

| HTTP Method | URI                                                                                       | Documented at                                                       |
| ----------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| POST        | /pools/default/buckets/<bucket\_name>/scopes                                              | [Creating a Scope](creating-a-scope.md)                             |
| POST        | /pools/default/buckets/<bucket\_name>/scopes/<scope\_name>/collections                    | [Creating a Collection](creating-a-collection.md)                   |
| GET         | /pools/default/buckets/<bucket\_name>/scopes/                                             | [Listing Scopes and Collections](listing-scopes-and-collections.md) |
| DELETE      | /pools/default/buckets/<bucket\_name>/scopes/<scope\_name>/collections/<collection\_name> | [Dropping a Collection](dropping-a-collection.md)                   |
| DELETE      | /pools/default/buckets/<bucket\_name>/scopes/<scope\_name>                                | [Dropping a Scope](dropping-a-scope.md)                             |

## [](#memory-and-storage-api)Memory and Storage API

_Memory quotas_ can be allocated to services, and the current allocations retrieved. During cluster initialization, the _on-disk paths_ for services can be specified on a _per node_ basis.

Reader and writer threads can be configured, to ensure that disk access is highly performant.

_Compaction_ can be managed: this is used by Couchbase Server to relocate on-disk data; so as to ensure the data’s closest-possible proximity, and thereby reclaim fragments of unused disk-space. The periodic compaction of a bucket’s data helps to ensure the ongoing efficiency of both reads and writes.

| HTTP Method | URI                                                                      | Documented at                                                      |
| ----------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| POST        | /nodes/self/controller/settings                                          | [Initializing a Node](rest-initialize-node.md)                     |
| POST        | /pools/default                                                           | [Configuring Memory](rest-configure-memory.md)                     |
| POST        | /pools/default/settings/memcached/global                                 | [Setting Thread Allocations](rest-reader-writer-thread-config.md)  |
| GET         | /nodes/self                                                              | [Getting Storage Information](rest-getting-storage-information.md) |
| POST        | /pools/default/buckets/\[bucket-name\]/controller/compactBucket          | [Performing Compaction Manually](rest-compact-post.md)             |
| POST        | /pools/default/buckets/\[bucket-name\]/controller/cancelBucketCompaction | [Performing Compaction Manually](rest-compact-post.md)             |
| GET         | /settings/autoCompaction                                                 | [Auto-Compaction: Global](rest-autocompact-global.md)              |
| POST        | /controller/setAutoCompaction                                            | [Auto-Compaction: Global](rest-autocompact-global.md)              |
| GET         | /pools/default/buckets/\[bucket-name\]                                   | [Auto-Compaction: Per Bucket](rest-autocompact-per-bucket.md)      |
| POST        | /pools/default/buckets/\[bucket-name\]                                   | [Auto-Compaction: Per Bucket](rest-autocompact-per-bucket.md)      |

## [](#server-groups-api)Server Groups API

_Server Group Awareness_ provides enhanced availability. Specifically, it protects a cluster from large-scale infrastructure failure, through the definition of groups. Its REST API is expressed by the following table.

| HTTP Method | URI                                         | Documented at                                                   |
| ----------- | ------------------------------------------- | --------------------------------------------------------------- |
| GET         | /pools/default/serverGroups                 | [Getting Group Information](rest-servergroup-get.md)            |
| POST        | /pools/default/serverGroups                 | [Creating Groups](rest-servergroup-post-create.md)              |
| POST        | /pools/default/serverGroups/<:uuid>/addNode | [Adding Nodes to Groups](rest-servergroup-post-add.md)          |
| PUT         | /pools/default/serverGroups/<:uuid>         | [Renaming Groups](rest-servergroup-put.md)                      |
| PUT         | /pools/default/serverGroups?rev=<:number>   | [Updating Group Membership](rest-servergroup-put-membership.md) |
| DELETE      | /pools/default/serverGroups/<:uuid>         | [Deleting Groups](rest-servergroup-delete.md)                   |

## [](#xdcr-api)XDCR API

Cross Data Center Replication (XDCR) replicates data between a source bucket and a target bucket. The buckets may be located on different clusters, and in different data centers: this provides protection against data-center failure, and also provides high-performance data-access for globally distributed, mission-critical applications. XDCR is supported by the REST API shown in the table below.

| HTTP Method | URI                                                        | Documented at                                                   |
| ----------- | ---------------------------------------------------------- | --------------------------------------------------------------- |
| POST        | /pools/default/remoteClusters                              | [Creating and Editing References](rest-xdcr-create-ref.md)      |
| GET         | /pools/default/remoteClusters                              | [Getting a Reference](rest-xdcr-get-ref.md)                     |
| POST        | /controller/createReplication                              | [Creating a Replication](rest-xdcr-create-replication.md)       |
| POST        | /settings/replications/\[replication\_id\]                 | [Pausing and Resuming a Replication](rest-xdcr-pause-resume.md) |
| DELETE      | /controller/cancelXDCR/\[url\_encoded\_replication\_id\]   | [Deleting a Replication](rest-xdcr-delete-replication.md)       |
| DELETE      | /pools/default/remoteClusters/\[destination-cluster-name\] | [Deleting a Reference](rest-xdcr-delete-ref.md)                 |
| POST        | /settings/replications/                                    | [Managing Advanced Settings](rest-xdcr-adv-settings.md)         |
| POST        | /settings/replications/<settings\_URI>                     | [Managing Advanced Settings](rest-xdcr-adv-settings.md)         |
| GET         | /settings/replications/                                    | [Managing Advanced Settings](rest-xdcr-adv-settings.md)         |
| GET         | /settings/replications/<settings\_URI>                     | [Managing Advanced Settings](rest-xdcr-adv-settings.md)         |
| GET         | /pools/default/stats/range/\[statistics\_name\]            | [Getting a Single Statistic](rest-statistics-single.md)         |

## [](#security-api)Security API

The Security REST API provides the endpoints for general security, for authentication, and for authorization. These APIs are listed in the tables below.

### [](#general-security)General Security

| HTTP Method | URI                                   | Documented at                                                                        |
| ----------- | ------------------------------------- | ------------------------------------------------------------------------------------ |
| GET         | ./whoami                              | [Who Am I?](rest-whoami.md)                                                          |
| GET         | /settings/audit                       | [Configure Auditing](rest-auditing.md)                                               |
| POST        | /settings/audit                       | [Configure Auditing](rest-auditing.md)                                               |
| GET         | /settings/audit/descriptors           | [Configure Auditing](rest-auditing.md)                                               |
| GET         | /settings/security                    | [Restrict Node-Addition](rest-specify-node-addition-conventions.md)                  |
| POST        | /settings/security                    | [Restrict Node-Addition](rest-specify-node-addition-conventions.md)                  |
| POST        | /clusterInit                          | [Initialize a Cluster](rest-initialize-cluster.md)                                   |
| GET         | /settings/security/\[service-name\]   | [Configure On-the-Wire Security](rest-setting-security.md)                           |
| POST        | /settings/security/\[service-name\]   | [Configure On-the-Wire Security](rest-setting-security.md)                           |
| GET         | /settings/security/responseHeaders    | [Configure HSTS](rest-setting-hsts.md)                                               |
| POST        | /settings/security/responseHeaders    | [Configure HSTS](rest-setting-hsts.md)                                               |
| DELETE      | /settings/security/responseHeaders    | [Configure HSTS](rest-setting-hsts.md)                                               |
| POST        | /node/controller/changeMasterPassword | [Secret-Management API](rest-secret-mgmt.md#post-nodecontrollerchangemasterpassword) |
| POST        | /node/controller/rotateDataKey        | [Secret-Management API](rest-secret-mgmt.md#post-nodecontrollerrotatedatakey)        |

### [](#authentication)Authentication

| HTTP Method | URI                                                         | Documented at                                                         |
| ----------- | ----------------------------------------------------------- | --------------------------------------------------------------------- |
| GET         | /settings/ldap                                              | [Configure LDAP](rest-configure-ldap.md#get-settingsldap)             |
| POST        | /settings/ldap                                              | [Configure LDAP](rest-configure-ldap.md#post-settingsldap)            |
| GET         | /settings/saslauthdAuth                                     | [Configure saslauthd](rest-configure-saslauthd.md)                    |
| POST        | /settings/saslauthdAuth                                     | [Configure saslauthd](rest-configure-saslauthd.md)                    |
| GET         | /settings/passwordPolicy                                    | [Set Password Policy](rest-set-password-policy.md)                    |
| POST        | /settings/passwordPolicy                                    | [Set Password Policy](rest-set-password-policy.md)                    |
| POST        | /controller/changePassword                                  | [Change Password](rest-set-password.md)                               |
| POST        | /node/controller/loadTrustedCAs                             | [Load Root Certificates](load-trusted-cas.md)                         |
| GET         | /node/controller/loadTrustedCAs                             | [Get Root Certificates](get-trusted-cas.md)                           |
| DELETE      | /pools/default/trustedCAs/<id>                              | [Delete Root Certificates](delete-trusted-cas.md)                     |
| GET         | /pools/default/certificates                                 | [Retrieve All Node Certificates](retrieve-all-node-certs.md)          |
| POST        | /node/controller/reloadCertificate                          | [Upload and Retrieve Node Certificates](upload-retrieve-node-cert.md) |
| GET         | /pools/default/certificate/node/<ip-address-or-domain-name> | [Upload and Retrieve Node Certificates](upload-retrieve-node-cert.md) |
| POST        | /controller/regenerateCertificate                           | [Regenerate All Certificates](rest-regenerate-all-certs.md)           |

### [](#authorization)Authorization

| HTTP Method | URI                                               | Documented at                                                                    |
| ----------- | ------------------------------------------------- | -------------------------------------------------------------------------------- |
| GET         | /settings/rbac/roles                              | [List Roles](rbac.md#list-roles)                                                 |
| GET         | /settings/rbac/users                              | [List Current Users and Their Roles](rbac.md#list-current-users-and-their-roles) |
| POST        | /pools/default/checkPermissions                   | [Check Permissions](rbac.md#check-permissions)                                   |
| GET         | /settings/rbac/groups                             | [List Currently Defined Groups](rbac.md#list-currently-defined-groups)           |
| PUT         | /settings/rbac/users/local/<new-username>         | [Create a Local User](rbac.md#create-a-local-user-and-assign-roles)              |
| PATCH       | /settings/rbac/users/local/<existing-username>    | [Create a Local User](rbac.md#create-a-local-user-and-assign-roles)              |
| PUT         | /settings/rbac/users/local/<new-username>         | [Create an External User](rbac.md#create-an-external-user-and-assign-roles)      |
| PUT         | /settings/rbac/groups/<new-groupname>             | [Create a Group](rbac.md#create-a-group-and-assign-it-roles)                     |
| DELETE      | /settings/rbac/users/local/<local-username>       | [Delete Users and Groups](rbac.md#delete-users-and-groups)                       |
| DELETE      | /settings/rbac/users/external/<external-username> | [Delete Users and Groups](rbac.md#delete-users-and-groups)                       |
| DELETE      | /settings/rbac/groups/<groupname>                 | [Delete Users and Groups](rbac.md#delete-users-and-groups)                       |

## [](#query-service-api)Query Service API

The _Query Service_ provides a REST API that covers four requirements; which are the administration of Query Service nodes, the configuration of the Query Service, the execution of SQL++ statements, and the management of JavaScript libraries and objects used to create SQL++ user-defined functions. The REST API is detailed in the tables below.

### [](#query-service-administration)Query Service Administration

| HTTP Method | URI                                    | Documented at                                                                                    |
| ----------- | -------------------------------------- | ------------------------------------------------------------------------------------------------ |
| GET         | /admin/clusters                        | [Read All Clusters](../n1ql/n1ql-rest-api/admin.md#%5Fget%5Fclusters)                            |
| GET         | /admin/clusters/{cluster}              | [Read a Cluster](../n1ql/n1ql-rest-api/admin.md#%5Fget%5Fcluster)                                |
| GET         | /admin/clusters/{cluster}/nodes        | [Read All Nodes](../n1ql/n1ql-rest-api/admin.md#%5Fget%5Fnodes)                                  |
| GET         | /admin/clusters/{cluster}/nodes/{node} | [Read a Node](../n1ql/n1ql-rest-api/admin.md#%5Fget%5Fnode)                                      |
| GET         | /admin/config                          | [Read Configuration](../n1ql/n1ql-rest-api/admin.md#%5Fget%5Fconfig)                             |
| GET         | /admin/prepareds                       | [Retrieve All Prepared Statements](../n1ql/n1ql-rest-api/admin.md#%5Fget%5Fprepareds)            |
| GET         | /admin/prepareds/{name}                | [Retrieve a Prepared Statement](../n1ql/n1ql-rest-api/admin.md#%5Fget%5Fprepared)                |
| DELETE      | /admin/prepareds/{name}                | [Delete a Prepared Statement](../n1ql/n1ql-rest-api/admin.md#%5Fdelete%5Fprepared)               |
| GET         | /admin/indexes/prepareds               | [Retrieve Prepared Index Statements](../n1ql/n1ql-rest-api/admin.md#%5Fget%5Fprepared%5Findexes) |
| GET         | /admin/active\_requests                | [Retrieve All Active Requests](../n1ql/n1ql-rest-api/admin.md#%5Fget%5Factive%5Frequests)        |
| GET         | /admin/active\_requests/{request}      | [Retrieve an Active Request](../n1ql/n1ql-rest-api/admin.md#%5Fget%5Factive%5Frequest)           |
| DELETE      | /admin/active\_requests/{request}      | [Delete an Active Request](../n1ql/n1ql-rest-api/admin.md#%5Fdelete%5Factive%5Frequest)          |
| GET         | /admin/indexes/active\_requests        | [Retrieve Active Index Requests](../n1ql/n1ql-rest-api/admin.md#%5Fget%5Factive%5Findexes)       |
| GET         | /admin/completed\_requests             | [Retrieve All Completed Requests](../n1ql/n1ql-rest-api/admin.md#%5Fget%5Fcompleted%5Frequests)  |
| GET         | /admin/completed\_requests/{request}   | [Retrieve a Completed Request](../n1ql/n1ql-rest-api/admin.md#%5Fget%5Fcompleted%5Frequest)      |
| DELETE      | /admin/completed\_requests/{request}   | [Delete a Completed Request](../n1ql/n1ql-rest-api/admin.md#%5Fdelete%5Fcompleted%5Frequest)     |
| GET         | /admin/indexes/completed\_requests     | [Retrieve Completed Index Requests](../n1ql/n1ql-rest-api/admin.md#%5Fget%5Fcompleted%5Findexes) |
| GET         | /admin/vitals                          | [Retrieve Vitals](../n1ql/n1ql-rest-api/admin.md#%5Fget%5Fvitals)                                |
| GET         | /admin/stats                           | [Retrieve All Statistics](../n1ql/n1ql-rest-api/admin.md#%5Fget%5Fstats)                         |
| GET         | /admin/stats/{stats}                   | [Retrieve a Statistic](../n1ql/n1ql-rest-api/admin.md#%5Fget%5Fstat)                             |
| GET         | /admin/settings                        | [Retrieve Node-Level Query Settings](../n1ql/n1ql-rest-api/admin.md#%5Fget%5Fsettings)           |
| POST        | /admin/settings                        | [Update Node-Level Query Settings](../n1ql/n1ql-rest-api/admin.md#%5Fpost%5Fsettings)            |
| GET         | /admin/ping                            | [Ping](../n1ql/n1ql-rest-api/admin.md#%5Fget%5Fping)                                             |

### [](#query-service-settings)Query Service Settings

| HTTP Method | URI                                   | Documented at                                                                             |
| ----------- | ------------------------------------- | ----------------------------------------------------------------------------------------- |
| GET         | /settings/querySettings               | [Retrieve Cluster-Level Query Settings](rest-cluster-query-settings.md#%5Fget%5Fsettings) |
| POST        | /settings/querySettings               | [Update Cluster-Level Query Settings](rest-cluster-query-settings.md#%5Fpost%5Fsettings)  |
| GET         | /settings/querySettings/curlWhitelist | [Retrieve CURL Access List](rest-cluster-query-settings.md#%5Fget%5Faccess)               |
| POST        | /settings/querySettings/curlWhitelist | [Update CURL Access List](rest-cluster-query-settings.md#%5Fpost%5Faccess)                |

### [](#sql-statement-execution)SQL++ Statement Execution

| HTTP Method | URI            | Documented at                                                              |
| ----------- | -------------- | -------------------------------------------------------------------------- |
| POST        | /query/service | [Query Service](../n1ql/n1ql-rest-api/index.md#%5Fpost%5Fservice)          |
| GET         | /query/service | [Read-Only Query Service](../n1ql/n1ql-rest-api/index.md#%5Fget%5Fservice) |

### [](#javascript-management)JavaScript Management

| HTTP Method | URI                               | Documented at                                                                      |
| ----------- | --------------------------------- | ---------------------------------------------------------------------------------- |
| GET         | /evaluator/v1/libraries           | [Read All Libraries](../n1ql/n1ql-rest-api/functions.md#%5Fget%5Fcollection)       |
| GET         | /evaluator/v1/libraries/{library} | [Read a Library](../n1ql/n1ql-rest-api/functions.md#%5Fget%5Flibrary)              |
| POST        | /evaluator/v1/libraries/{library} | [Create or Update a Library](../n1ql/n1ql-rest-api/functions.md#%5Fpost%5Flibrary) |
| DELETE      | /evaluator/v1/libraries/{library} | [Delete a Library](../n1ql/n1ql-rest-api/functions.md#%5Fdelete%5Flibrary)         |

## [](#index-service-api)Index Service API

The _Index Service_ REST API provides configuration options for the Index Service. The API is listed below.

| HTTP Method | URI                              | Documented at                                                            |
| ----------- | -------------------------------- | ------------------------------------------------------------------------ |
| GET         | /settings/indexes                | [Retrieve GSI Settings](get-settings-indexes.md)                         |
| POST        | /settings/indexes                | [Set GSI Settings](post-settings-indexes.md)                             |
| GET         | /api/v1/stats                    | [Get Node Statistics](rest-index-stats.md#%5Fget%5Fnode%5Fstats)         |
| GET         | /api/v1/stats/{keyspace}         | [Get Keyspace Statistics](rest-index-stats.md#%5Fget%5Fkeyspace%5Fstats) |
| GET         | /api/v1/stats/{keyspace}/{index} | [Get Index Statistics](rest-index-stats.md#%5Fget%5Findex%5Fstats)       |

## [](#backup-service-api)Backup Service API

The _Backup Service API_ supports management of the Backup Service, providing endpoints categorized as follows: _Cluster_, _Configuration_, _Repository_, _Plan_, _Task_, and _Data_. All calls require the Full Admin role, and use port `8097`. Each URI, in Couchbase Server Enterprise Edition Version 7.0 and later, must be prefixed with `/api/v1`.

The individual endpoints are listed by category, in the tables below.

### [](#cluster)Cluster

| HTTP Method | URI           | Documented at                                                |
| ----------- | ------------- | ------------------------------------------------------------ |
| GET         | /cluster/self | [Get Information on the Cluster](backup-get-cluster-info.md) |

### [](#configuration)Configuration

| HTTP Method | URI     | Description                                            |
| ----------- | ------- | ------------------------------------------------------ |
| GET         | /config | [Manage Backup Configuration](backup-manage-config.md) |
| POST        | /config | [Manage Backup Configuration](backup-manage-config.md) |
| PUT         | /config | [Manage Backup Configuration](backup-manage-config.md) |

### [](#repository)Repository

| HTTP Method | URI                                                                                  | Documented at                                                    |
| ----------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| GET         | /cluster/self/repository/<'active'\|'archived'|'imported'>                           | [Get Information on Repositories](backup-get-repository-info.md) |
| GET         | /cluster/self/repository/active/<repository-id>                                      | [Get Information on Repositories](backup-get-repository-info.md) |
| GET         | /cluster/self/repository/<'active'\|'archived'|'imported'>/<repository-id>/info      | [Get Information on Repositories](backup-get-repository-info.md) |
| POST        | /cluster/self/repository/active/<repository-id>                                      | [Create a Repository](backup-create-repository.md)               |
| POST        | /cluster/self/repository/<'archived'\|'imported'>/<repository-id>/restore            | [Restore Data](backup-restore-data.md)                           |
| POST        | /cluster/self/repository/import                                                      | [Import a Repository](backup-import-repository.md)               |
| POST        | /cluster/self/repository/<'active'\|'archived'|'imported'>/<repository-id>/examine   | [Examine Backed-Up Data](backup-examine-data.md)                 |
| POST        | /cluster/self/repository/active/<repository-id>/backup                               | [Perform an Immediate Backup](backup-trigger-backup.md)          |
| POST        | /cluster/self/repository/active/<repository-id>/merge                                | [Perform an Immediate Merge](backup-trigger-merge.md)            |
| POST        | /cluster/self/repository/active/<repository-id>/archive                              | [Archive a Repository](backup-archive-a-repository.md)           |
| POST        | /cluster/self/repository/active/<repository-id>/pause                                | [Pause and Resume Tasks](backup-pause-and-resume-tasks.md)       |
| POST        | /cluster/self/repository/active/<repository-id>/resume                               | [Pause and Resume Tasks](backup-pause-and-resume-tasks.md)       |
| DELETE      | /cluster/self/repository/<'archived'\|'imported'>/<repository-id>                    | [Delete a Repository](backup-delete-repository.md)               |
| DELETE      | /cluster/self/repository/<'archived'\|'imported'>/<repository-id>?remove\_repository | [Delete a Repository](backup-delete-repository.md)               |
| DELETE      | /cluster/self/repository/active/<repository-id>/backups/<backup-id>                  | [Delete a Backup](backup-delete-backups.md)                      |

### [](#plan)Plan

| HTTP Method | URI                              | Documented at                                            |
| ----------- | -------------------------------- | -------------------------------------------------------- |
| GET         | /cluster/plan                    | [Get Information on Plans](backup-get-plan-info.md)      |
| GET         | /cluster/plan/<plan-id>          | [Get Information on Plans](backup-get-plan-info.md)      |
| POST        | /cluster/plan/<plan-id>          | [Create and Edit Plans](backup-create-and-edit-plans.md) |
| PUT         | /cluster/plan/<existing-plan-id> | [Create and Edit Plans](backup-create-and-edit-plans.md) |
| DELETE      | /plan/<plan-id>                  | [Delete a Plan](backup-delete-plan.md)                   |

### [](#task)Task

| HTTP Method | URI                                                                                                                       | Documented at                                       |
| ----------- | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| GET         | /cluster/self/repository/<'active'\|'archived'|'imported'>/<repository-id>/taskHistory                                    | [Get Information on Tasks](backup-get-task-info.md) |
| GET         | /cluster/self/repository/<'active'\|'archived'|'imported'>/<repository-id>/taskHistory?<task-subset-specification-string> | [Get Information on Tasks](backup-get-task-info.md) |

### [](#data)Data

| HTTP Method | URI                                                                 | Documented at                              |
| ----------- | ------------------------------------------------------------------- | ------------------------------------------ |
| DELETE      | /cluster/self/repository/active/<repository-id>/backups/<backup-id> | [Delete Backups](backup-delete-backups.md) |

## [](#search-service-api)Search Service API

The Search Service allows users to create, manage, and query _Full Text Indexes_, whereby searches can be performed and matches attained on character strings. The Search Service REST API allows such indexes to be created and maintained. The API is listed in the tables below.

### [](#index-definition)Index Definition

| HTTP Method | URI                    | Documented at                                             |
| ----------- | ---------------------- | --------------------------------------------------------- |
| GET         | /api/index             | [Index Definition](rest-fts-indexing.md#index-definition) |
| GET         | /api/index/{indexName} | [Index Definition](rest-fts-indexing.md#index-definition) |
| PUT         | /api/index/{indexName} | [Index Definition](rest-fts-indexing.md#index-definition) |
| DELETE      | /api/index/{indexName} | [Index Definition](rest-fts-indexing.md#index-definition) |

### [](#index-management)Index Management

| HTTP Method | URI                                           | Documented at                                             |
| ----------- | --------------------------------------------- | --------------------------------------------------------- |
| POST        | /api/index/{indexName}/ingestControl/{op}     | [Index Management](rest-fts-indexing.md#index-management) |
| POST        | /api/index/{indexName}/planFreezeControl/{op} | [Index Management](rest-fts-indexing.md#index-management) |
| POST        | /api/index/{indexName}/planQueryControl/{op}  | [Index Management](rest-fts-indexing.md#index-management) |

### [](#index-monitoring-and-debugging)Index Monitoring and Debugging

| HTTP Method | URI                               | Documented at                                                                         |
| ----------- | --------------------------------- | ------------------------------------------------------------------------------------- |
| GET         | /api/stats                        | [Index Monitoring And Debugging](rest-fts-indexing.md#index-monitoring-and-debugging) |
| GET         | /api/stats/{indexName}            | [Index Monitoring And Debugging](rest-fts-indexing.md#index-monitoring-and-debugging) |
| POST        | /api/stats/{indexName}/analyzeDoc | [Index Monitoring And Debugging](rest-fts-indexing.md#index-monitoring-and-debugging) |
| GET         | /api/query/index/{indexName}      | [Index Monitoring And Debugging](rest-fts-indexing.md#index-monitoring-and-debugging) |

### [](#index-querying)Index Querying

| HTTP Method | URI                          | Documented at                                         |
| ----------- | ---------------------------- | ----------------------------------------------------- |
| GET         | /api/index/{indexName}/count | [Index Querying](rest-fts-indexing.md#index-querying) |
| POST        | /api/index/{indexName}/query | [Index Querying](rest-fts-indexing.md#index-querying) |

### [](#node-configuration)Node Configuration

| HTTP Method | URI              | Documented at                                             |
| ----------- | ---------------- | --------------------------------------------------------- |
| GET         | /api/cfg         | [Node Configuration](rest-fts-node.md#node-configuration) |
| POST        | /api/cfgRefresh  | [Node Configuration](rest-fts-node.md#node-configuration) |
| POST        | /api/managerKick | [Node Configuration](rest-fts-node.md#node-configuration) |
| GET         | /api/managerMeta | [Node Configuration](rest-fts-node.md#node-configuration) |

### [](#node-diagnostics)Node Diagnostics

| HTTP Method | URI                         | Documented at                                         |
| ----------- | --------------------------- | ----------------------------------------------------- |
| GET         | /api/diag                   | [Node Diagnostics](rest-fts-node.md#node-diagnostics) |
| GET         | /api/log                    | [Node Diagnostics](rest-fts-node.md#node-diagnostics) |
| GET         | /api/runtime                | [Node Diagnostics](rest-fts-node.md#node-diagnostics) |
| GET         | /api/runtime/args           | [Node Diagnostics](rest-fts-node.md#node-diagnostics) |
| POST        | /api/runtime/profile/cpu    | [Node Diagnostics](rest-fts-node.md#node-diagnostics) |
| POST        | /api/runtime/profile/memory | [Node Diagnostics](rest-fts-node.md#node-diagnostics) |

### [](#node-management)Node Management

| HTTP Method | URI             | Documented at                                       |
| ----------- | --------------- | --------------------------------------------------- |
| POST        | /api/runtime/gc | [Node Management](rest-fts-node.md#node-management) |

### [](#node-monitoring)Node Monitoring

| HTTP Method | URI                         | Documented at                                       |
| ----------- | --------------------------- | --------------------------------------------------- |
| GET         | /api/runtime/stats          | [Node Monitoring](rest-fts-node.md#node-monitoring) |
| GET         | /api/runtime/stats/statsMem | [Node Monitoring](rest-fts-node.md#node-monitoring) |

### [](#index-partition-definition)Index Partition Definition

| HTTP Method | URI                      | Documented at                                               |
| ----------- | ------------------------ | ----------------------------------------------------------- |
| GET         | /api/pindex              | [Advanced](rest-fts-advanced.md#index-partition-definition) |
| GET         | /api/pindex/{pindexName} | [Advanced](rest-fts-advanced.md#index-partition-definition) |

### [](#index-partition-querying)Index Partition Querying

| HTTP Method | URI                            | Documented at                                             |
| ----------- | ------------------------------ | --------------------------------------------------------- |
| GET         | /api/pindex/{pindexName}/count | [Advanced](rest-fts-advanced.md#index-partition-querying) |
| POST        | /api/pindex/{pindexName}/query | [Advanced](rest-fts-advanced.md#index-partition-querying) |

### [](#fts-memory-quota)FTS Memory Quota

| HTTP Method | URI            | Documented at                                     |
| ----------- | -------------- | ------------------------------------------------- |
| POST        | /pools/default | [Advanced](rest-fts-advanced.md#fts-memory-quota) |

## [](#eventing-service-api)Eventing Service API

The _Eventing Service_ REST API provides methods for working with _Eventing Functions_. The complete API is listed at [Eventing REST API](../eventing/eventing-api.md).

## [](#analytics-service-api)Analytics Service API

The _Analytics Service_ provides a REST API for querying, configuration, and the management of links and libraries. The API is listed in the following tables.

### [](#analytics-query-api)Analytics Query API

| HTTP Method | URI                | Documented at                                                                        |
| ----------- | ------------------ | ------------------------------------------------------------------------------------ |
| POST        | /analytics/service | [Query Service](../analytics/rest-service.md#%5Fpost%5Fservice)                      |
| GET         | /analytics/service | [Read-Only Query Service](../analytics/rest-service.md#%5Fget%5Fservice)             |
| POST        | /query/service     | [Query Service (Alternative)](../analytics/rest-service.md#%5Fpost%5Fquery)          |
| GET         | /query/service     | [Read-Only Query Service (Alternative)](../analytics/rest-service.md#%5Fget%5Fquery) |

### [](#analytics-admin-api)Analytics Admin API

| HTTP Method | URI                               | Documented at                                                          |
| ----------- | --------------------------------- | ---------------------------------------------------------------------- |
| DELETE      | /analytics/admin/active\_requests | [Request Cancellation](../analytics/rest-admin.md#%5Fcancel%5Frequest) |
| GET         | /analytics/cluster                | [Cluster Status](../analytics/rest-admin.md#%5Fcluster%5Fstatus)       |
| POST        | /analytics/cluster/restart        | [Cluster Restart](../analytics/rest-admin.md#%5Frestart%5Fcluster)     |
| POST        | /analytics/node/restart           | [Node Restart](../analytics/rest-admin.md#%5Frestart%5Fnode)           |
| GET         | /analytics/status/ingestion       | [Ingestion Status](../analytics/rest-admin.md#%5Fingestion%5Fstatus)   |

### [](#analytics-config-api)Analytics Config API

| HTTP Method | URI                       | Documented at                                                                   |
| ----------- | ------------------------- | ------------------------------------------------------------------------------- |
| GET         | /analytics/config/service | [View Service-Level Parameters](../analytics/rest-config.md#%5Fget%5Fservice)   |
| PUT         | /analytics/config/service | [Modify Service-Level Parameters](../analytics/rest-config.md#%5Fput%5Fservice) |
| GET         | /analytics/config/node    | [View Node-Specific Parameters](../analytics/rest-config.md#%5Fget%5Fnode)      |
| PUT         | /analytics/config/node    | [Modify Node-Specific Parameters](../analytics/rest-config.md#%5Fput%5Fnode)    |

### [](#analytics-settings-api)Analytics Settings API

| HTTP Method | URI                 | Documented at                                                                 |
| ----------- | ------------------- | ----------------------------------------------------------------------------- |
| GET         | /settings/analytics | [View Analytics Settings](../analytics/rest-settings.md#%5Fget%5Fsettings)    |
| POST        | /settings/analytics | [Modify Analytics Settings](../analytics/rest-settings.md#%5Fpost%5Fsettings) |

### [](#analytics-links-api)Analytics Links API

| HTTP Method | URI                            | Documented at                                                  |
| ----------- | ------------------------------ | -------------------------------------------------------------- |
| POST        | /analytics/link/{scope}/{name} | [Create Link](../analytics/rest-links.md#%5Fpost%5Flink)       |
| GET         | /analytics/link/{scope}/{name} | [Query Link](../analytics/rest-links.md#%5Fget%5Flink)         |
| PUT         | /analytics/link/{scope}/{name} | [Edit Link](../analytics/rest-links.md#%5Fput%5Flink)          |
| DELETE      | /analytics/link/{scope}/{name} | [Delete Link](../analytics/rest-links.md#%5Fdelete%5Flink)     |
| GET         | /analytics/link                | [Query All Links](../analytics/rest-links.md#%5Fget%5Fall)     |
| GET         | /analytics/link/{scope}        | [Query Scope Links](../analytics/rest-links.md#%5Fget%5Fscope) |

### [](#analytics-library-api)Analytics Library API

| HTTP Method | URI                                  | Documented at                                                                |
| ----------- | ------------------------------------ | ---------------------------------------------------------------------------- |
| GET         | /analytics/library                   | [Read All Libraries](../analytics/rest-library.md#%5Fget%5Fcollection)       |
| POST        | /analytics/library/{scope}/{library} | [Create or Update a Library](../analytics/rest-library.md#%5Fpost%5Flibrary) |
| DELETE      | /analytics/library/{scope}/{library} | [Delete a Library](../analytics/rest-links.md#%5Fdelete%5Flibrary)           |

## [](#http-request-headers)HTTP Request Headers

The following HTTP request headers are used to create requests:

| Header                               | Supported Values                                            | Description of Use                                                                           | Required                                      |
| ------------------------------------ | ----------------------------------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------------- |
| Accept                               | Comma-delimited list of media types or media type patterns. | Indicates to the server what media type(s) this client is prepared to accept.                | Recommended                                   |
| Authorization                        | Basic plus username and password (per RFC 2617).            | Identifies the authorized user making this request.                                          | No, unless secured                            |
| Content-Length                       | Body Length (in bytes)                                      | Describes the size of the message body.                                                      | Yes, on requests that contain a message body. |
| Content-Type                         | Content type                                                | Describes the representation and syntax of the request message body.                         | Yes, on requests that contain a message body. |
| Host                                 | Origin host name                                            | Required to allow support of multiple origin hosts at a single IP address.                   | All requests                                  |
| X-YYYYY-Client-Specification-Version | String                                                      | Declares the specification version of the YYYYY API that this client was programmed against. | No                                            |

## [](#http-response-codes)HTTP Response Codes

The Couchbase Server returns one of the following HTTP status codes in response to REST API requests:

| HTTP response             | Description                                                                                                                                                                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 200 OK                    | Successful request and an HTTP response body returns. If this creates a new resource with a URI, the 200 status will also have a location header containing the canonical URI for the newly created resource.                                                              |
| 201 Created               | Request to create a new resource is successful, but no HTTP response body returns. The URI for the newly created resource returns with the status code.                                                                                                                    |
| 202 Accepted              | The request is accepted for processing, but processing is not complete. Per HTTP/1.1, the response, if any, SHOULD include an indication of the request’s current status, and either a pointer to a status monitor or some estimate of when the request will be fulfilled. |
| 204 No Content            | The server fulfilled the request, but does not need to return a response body.                                                                                                                                                                                             |
| 400 Bad Request           | The request could not be processed because it contains missing or invalid information, such as validation error on an input field, a missing required value, and so on.                                                                                                    |
| 401 Unauthorized          | The credentials provided with this request are missing or invalid.                                                                                                                                                                                                         |
| 403 Forbidden             | The server recognized the given credentials, but you do not possess proper access to perform this request.                                                                                                                                                                 |
| 404 Not Found             | URI provided in a request does not exist.                                                                                                                                                                                                                                  |
| 405 Method Not Allowed    | The HTTP verb specified in the request (DELETE, GET, HEAD, POST, PUT) is not supported for this URI.                                                                                                                                                                       |
| 406 Not Acceptable        | The resource identified by this request cannot create a response corresponding to one of the media types in the Accept header of the request.                                                                                                                              |
| 409 Conflict              | A create or update request could not be completed, because it would cause a conflict in the current state of the resources supported by the server. For example, an attempt to create a new resource with a unique identifier already assigned to some existing resource.  |
| 500 Internal Server Error | The server encountered an unexpected condition which prevented it from fulfilling the request.                                                                                                                                                                             |
| 501 Not Implemented       | The server does not currently support the functionality required to fulfill the request.                                                                                                                                                                                   |
| 503 Service Unavailable   | The server is currently unable to handle the request due to temporary overloading or maintenance of the server.                                                                                                                                                            |