---
title: REST API reference
description: The REST API supports the management of Couchbase-Server clusters.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/rest-intro.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:rest-api:rest-intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/rest-api/rest-intro.html)

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
| GET         | /pools/default                                  | [Getting Rebalance Reason Codes](rest-retrieve-cluster-rebalance-reason-codes.md)     |
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

_Compaction_ can be managed: this is used by Couchbase Server to relocate on-disk data; so as to ensure the data's closest-possible proximity, and thereby reclaim fragments of unused disk-space. The periodic compaction of a bucket's data helps to ensure the ongoing efficiency of both reads and writes.

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

| HTTP Method | URI                                        | Documented at                                                       |
| ----------- | ------------------------------------------ | ------------------------------------------------------------------- |
| GET         | ./whoami                                   | [Who Am I?](rest-whoami.md)                                         |
| GET         | /settings/audit                            | [Configure Auditing](rest-auditing.md)                              |
| POST        | /settings/audit                            | [Configure Auditing](rest-auditing.md)                              |
| GET         | /settings/audit/descriptors                | [Configure Auditing](rest-auditing.md)                              |
| GET         | /settings/security                         | [Restrict Node-Addition](rest-specify-node-addition-conventions.md) |
| POST        | /settings/security                         | [Restrict Node-Addition](rest-specify-node-addition-conventions.md) |
| POST        | /clusterInit                               | [Initialize a Cluster](rest-initialize-cluster.md)                  |
| GET         | /settings/security/\[service-name\]        | [Configure On-the-Wire Security](rest-setting-security.md)          |
| POST        | /settings/security/\[service-name\]        | [Configure On-the-Wire Security](rest-setting-security.md)          |
| POST        | /node/controller/rotateInternalCredentials | [Rotate Internal Credentials](rest-rotate-internal-credentials.md)  |
| GET         | /settings/security/responseHeaders         | [Configure HSTS](rest-setting-hsts.md)                              |
| POST        | /settings/security/responseHeaders         | [Configure HSTS](rest-setting-hsts.md)                              |
| DELETE      | /settings/security/responseHeaders         | [Configure HSTS](rest-setting-hsts.md)                              |

### [](#authentication)Authentication

| HTTP Method | URI                                                         | Documented at                                                         |
| ----------- | ----------------------------------------------------------- | --------------------------------------------------------------------- |
| GET         | /settings/ldap                                              | [Configure LDAP](rest-configure-ldap.md#get-settingsldap)             |
| POST        | /settings/ldap                                              | [Configure LDAP](rest-configure-ldap.md#post-settingsldap)            |
| GET         | /settings/saml                                              | [Configure SAML](rest-configure-saml.md#get-settingssaml)             |
| POST        | /settings/saml                                              | [Configure SAML](rest-configure-saml.md#post-settingssaml)            |
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
| PUT         | /settings/rbac/users/external/<new-username>      | [Create an External User](rbac.md#create-an-external-user-and-assign-roles)      |
| PUT         | /settings/rbac/groups/<new-groupname>             | [Create a Group](rbac.md#create-a-group-and-assign-it-roles)                     |
| DELETE      | /settings/rbac/users/local/<local-username>       | [Delete Users and Groups](rbac.md#delete-users-and-groups)                       |
| DELETE      | /settings/rbac/users/external/<external-username> | [Delete Users and Groups](rbac.md#delete-users-and-groups)                       |
| DELETE      | /settings/rbac/groups/<groupname>                 | [Delete Users and Groups](rbac.md#delete-users-and-groups)                       |

### [](#system-secrets-management)System-Secrets Management

| HTTP Method | URI                                   | Documented at                                                 |
| ----------- | ------------------------------------- | ------------------------------------------------------------- |
| GET         | /nodes/self/secretsManagement         | [Configuring System Secrets](system-secrets-configuration.md) |
| POST        | /node/controller/secretsManagement    | [Configuring System Secrets](system-secrets-configuration.md) |
| POST        | /node/controller/changeMasterPassword | [Changing the Master Password](change-master-password.md)     |
| POST        | /node/controller/rotateDataKey        | [Rotating the Data Key](rotate-data-key.md)                   |

## [](#query-service-api)Query Service API

The _Query Service_ provides a REST API that covers four requirements; which are the administration of Query Service nodes, the configuration of the Query Service, the execution of SQL++ statements, and the management of JavaScript libraries and objects used to create SQL++ user-defined functions. The REST API is detailed in the tables below.

### [](#sql-statement-execution)SQL++ Statement Execution

| HTTP Method | URI            | Documented at                                                        |
| ----------- | -------------- | -------------------------------------------------------------------- |
| POST        | /query/service | [Query Service](../n1ql-rest-query/index.md#post%5Fservice)          |
| GET         | /query/service | [Read-Only Query Service](../n1ql-rest-query/index.md#get%5Fservice) |

### [](#query-service-administration)Query Service Administration

| HTTP Method | URI                                    | Documented at                                                                              |
| ----------- | -------------------------------------- | ------------------------------------------------------------------------------------------ |
| GET         | /admin/clusters                        | [Read All Clusters](../n1ql-rest-admin/index.md#get%5Fclusters)                            |
| GET         | /admin/clusters/{cluster}              | [Read a Cluster](../n1ql-rest-admin/index.md#get%5Fcluster)                                |
| GET         | /admin/clusters/{cluster}/nodes        | [Read All Nodes](../n1ql-rest-admin/index.md#get%5Fnodes)                                  |
| GET         | /admin/clusters/{cluster}/nodes/{node} | [Read a Node](../n1ql-rest-admin/index.md#get%5Fnode)                                      |
| GET         | /admin/config                          | [Read Configuration](../n1ql-rest-admin/index.md#get%5Fconfig)                             |
| GET         | /admin/prepareds                       | [Retrieve All Prepared Statements](../n1ql-rest-admin/index.md#get%5Fprepareds)            |
| GET         | /admin/prepareds/{name}                | [Retrieve a Prepared Statement](../n1ql-rest-admin/index.md#get%5Fprepared)                |
| DELETE      | /admin/prepareds/{name}                | [Delete a Prepared Statement](../n1ql-rest-admin/index.md#delete%5Fprepared)               |
| GET         | /admin/indexes/prepareds               | [Retrieve Prepared Index Statements](../n1ql-rest-admin/index.md#get%5Fprepared%5Findexes) |
| GET         | /admin/active\_requests                | [Retrieve All Active Requests](../n1ql-rest-admin/index.md#get%5Factive%5Frequests)        |
| GET         | /admin/active\_requests/{request}      | [Retrieve an Active Request](../n1ql-rest-admin/index.md#get%5Factive%5Frequest)           |
| DELETE      | /admin/active\_requests/{request}      | [Delete an Active Request](../n1ql-rest-admin/index.md#delete%5Factive%5Frequest)          |
| GET         | /admin/indexes/active\_requests        | [Retrieve Active Index Requests](../n1ql-rest-admin/index.md#get%5Factive%5Findexes)       |
| GET         | /admin/completed\_requests             | [Retrieve All Completed Requests](../n1ql-rest-admin/index.md#get%5Fcompleted%5Frequests)  |
| GET         | /admin/completed\_requests/{request}   | [Retrieve a Completed Request](../n1ql-rest-admin/index.md#get%5Fcompleted%5Frequest)      |
| DELETE      | /admin/completed\_requests/{request}   | [Delete a Completed Request](../n1ql-rest-admin/index.md#delete%5Fcompleted%5Frequest)     |
| GET         | /admin/indexes/completed\_requests     | [Retrieve Completed Index Requests](../n1ql-rest-admin/index.md#get%5Fcompleted%5Findexes) |
| GET         | /admin/vitals                          | [Retrieve Vitals](../n1ql-rest-admin/index.md#get%5Fvitals)                                |
| GET         | /admin/stats                           | [Retrieve All Statistics](../n1ql-rest-admin/index.md#get%5Fstats)                         |
| GET         | /admin/stats/{stats}                   | [Retrieve a Statistic](../n1ql-rest-admin/index.md#get%5Fstat)                             |
| GET         | /admin/settings                        | [Retrieve Node-Level Query Settings](../n1ql-rest-admin/index.md#get%5Fsettings)           |
| POST        | /admin/settings                        | [Update Node-Level Query Settings](../n1ql-rest-admin/index.md#post%5Fsettings)            |
| GET         | /admin/ping                            | [Ping](../n1ql-rest-admin/index.md#get%5Fping)                                             |
| GET         | /admin/gc                              | [Run Garbage Collector](../n1ql-rest-admin/index.md#get%5Fgc)                              |
| POST        | /admin/gc                              | [Run Garbage Collector and Release Memory](../n1ql-rest-admin/index.md#post%5Fgc)          |

### [](#query-service-settings)Query Service Settings

| HTTP Method | URI                                   | Documented at                                                                          |
| ----------- | ------------------------------------- | -------------------------------------------------------------------------------------- |
| GET         | /settings/querySettings               | [Retrieve Cluster-Level Query Settings](../n1ql-rest-settings/index.md#get%5Fsettings) |
| POST        | /settings/querySettings               | [Update Cluster-Level Query Settings](../n1ql-rest-settings/index.md#post%5Fsettings)  |
| GET         | /settings/querySettings/curlWhitelist | [Retrieve CURL Access List](../n1ql-rest-settings/index.md#get%5Faccess)               |
| POST        | /settings/querySettings/curlWhitelist | [Update CURL Access List](../n1ql-rest-settings/index.md#post%5Faccess)                |

### [](#javascript-management)JavaScript Management

| HTTP Method | URI                               | Documented at                                                                |
| ----------- | --------------------------------- | ---------------------------------------------------------------------------- |
| GET         | /evaluator/v1/libraries           | [Read All Libraries](../n1ql-rest-functions/index.md#get%5Fcollection)       |
| GET         | /evaluator/v1/libraries/{library} | [Read a Library](../n1ql-rest-functions/index.md#get%5Flibrary)              |
| POST        | /evaluator/v1/libraries/{library} | [Create or Update a Library](../n1ql-rest-functions/index.md#post%5Flibrary) |
| DELETE      | /evaluator/v1/libraries/{library} | [Delete a Library](../n1ql-rest-functions/index.md#delete%5Flibrary)         |

## [](#index-service-api)Index Service API

The _Index Service_ REST API provides configuration options for the Index Service. The APIs are listed below.

### [](#gsi-settings)GSI Settings

| HTTP Method | URI               | Documented at                                    |
| ----------- | ----------------- | ------------------------------------------------ |
| GET         | /settings/indexes | [Retrieve GSI Settings](get-settings-indexes.md) |
| POST        | /settings/indexes | [Set GSI Settings](post-settings-indexes.md)     |

### [](#index-statistics)Index Statistics

| HTTP Method | URI                              | Documented at                                                                  |
| ----------- | -------------------------------- | ------------------------------------------------------------------------------ |
| GET         | /api/v1/stats                    | [Get Node Statistics](../index-rest-stats/index.md#get%5Fnode%5Fstats)         |
| GET         | /api/v1/stats/{keyspace}         | [Get Keyspace Statistics](../index-rest-stats/index.md#get%5Fkeyspace%5Fstats) |
| GET         | /api/v1/stats/{keyspace}/{index} | [Get Index Statistics](../index-rest-stats/index.md#get%5Findex%5Fstats)       |

### [](#index-settings)Index Settings

| HTTP Method | URI       | Documented at                                                             |
| ----------- | --------- | ------------------------------------------------------------------------- |
| GET         | /settings | [Retrieve Index Settings](../index-rest-settings/index.md#get%5Fsettings) |
| POST        | /settings | [Update Index Settings](../index-rest-settings/index.md#post%5Fsettings)  |

## [](#backup-service-api)Backup Service API

The _Backup Service API_ supports management of the Backup Service, providing endpoints categorized as follows: _Cluster_, _Configuration_, _Repository_, _Plan_, _Task_, and _Data_. All calls require the Full Admin role, and use port `8097`. Each URI, in Couchbase Server Enterprise Edition Version 7.0 and later, must be prefixed with `/api/v1`.

The individual endpoints are listed by category, in the tables below.

### [](#cluster)Cluster

| HTTP Method | URI                  | Documented at                                                |
| ----------- | -------------------- | ------------------------------------------------------------ |
| GET         | /api/v1/cluster/self | [Get Information on the Cluster](backup-get-cluster-info.md) |

### [](#configuration)Configuration

| HTTP Method | URI                     | Description                                             |
| ----------- | ----------------------- | ------------------------------------------------------- |
| GET         | /api/v1/config          | [Manage Backup Configuration](backup-manage-config.md)  |
| POST        | /api/v1/config          | [Manage Backup Configuration](backup-manage-config.md)  |
| PUT         | /api/v1/config          | [Manage Backup Configuration](backup-manage-config.md)  |
| GET         | /api/v1/nodesThreadsMap | [Manage Backup Service Threads](backup-node-threads.md) |
| PATCH       | /api/v1/nodesThreadsMap | [Manage Backup Service Threads](backup-node-threads.md) |
| POST        | /api/v1/nodesThreadsMap | [Manage Backup Service Threads](backup-node-threads.md) |

### [](#repository)Repository

| HTTP Method | URI                                                                                         | Documented at                                                      |
| ----------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| GET         | /api/v1/cluster/self/repository/<'active'\|'archived'|'imported'>                           | [Get Backup Repository Information](backup-get-repository-info.md) |
| GET         | /api/v1/cluster/self/repository/active/<repository-id>                                      | [Get Backup Repository Information](backup-get-repository-info.md) |
| GET         | /api/v1/cluster/self/repository/<'active'\|'archived'|'imported'>/<repository-id>/info      | [Get Backup Repository Information](backup-get-repository-info.md) |
| POST        | /api/v1/cluster/self/repository/active/<repository-id>                                      | [Create a Repository](backup-create-repository.md)                 |
| POST        | /api/v1/cluster/self/repository/<'archived'\|'imported'>/<repository-id>/restore            | [Restore Data](backup-restore-data.md)                             |
| POST        | /api/v1/cluster/self/repository/import                                                      | [Import a Repository](backup-import-repository.md)                 |
| POST        | /api/v1/cluster/self/repository/<'active'\|'archived'|'imported'>/<repository-id>/examine   | [Examine Backed-Up Data](backup-examine-data.md)                   |
| POST        | /api/v1/cluster/self/repository/active/<repository-id>/backup                               | [Perform an Immediate Backup](backup-trigger-backup.md)            |
| POST        | /api/v1/cluster/self/repository/active/<repository-id>/merge                                | [Perform an Immediate Merge](backup-trigger-merge.md)              |
| POST        | /api/v1/cluster/self/repository/active/<repository-id>/archive                              | [Archive a Repository](backup-archive-a-repository.md)             |
| POST        | /api/v1/cluster/self/repository/active/<repository-id>/pause                                | [Pause and Resume Tasks](backup-pause-and-resume-tasks.md)         |
| POST        | /api/v1/cluster/self/repository/active/<repository-id>/resume                               | [Pause and Resume Tasks](backup-pause-and-resume-tasks.md)         |
| DELETE      | /api/v1/cluster/self/repository/<'archived'\|'imported'>/<repository-id>                    | [Delete a Repository](backup-delete-repository.md)                 |
| DELETE      | /api/v1/cluster/self/repository/<'archived'\|'imported'>/<repository-id>?remove\_repository | [Delete a Repository](backup-delete-repository.md)                 |
| DELETE      | /api/v1/cluster/self/repository/active/<repository-id>/backups/<backup-id>                  | [Delete a Backup](backup-delete-backups.md)                        |

### [](#plan)Plan

| HTTP Method | URI                                     | Documented at                                            |
| ----------- | --------------------------------------- | -------------------------------------------------------- |
| GET         | /api/v1/cluster/plan                    | [Get Backup Plan Information](backup-get-plan-info.md)   |
| GET         | /api/v1/cluster/plan/<plan-id>          | [Get Backup Plan Information](backup-get-plan-info.md)   |
| POST        | /api/v1/cluster/plan/<plan-id>          | [Create and Edit Plans](backup-create-and-edit-plans.md) |
| PUT         | /api/v1/cluster/plan/<existing-plan-id> | [Create and Edit Plans](backup-create-and-edit-plans.md) |
| DELETE      | /api/v1/plan/<plan-id>                  | [Delete a Plan](backup-delete-plan.md)                   |

### [](#task)Task

| HTTP Method | URI                                                                                                                              | Documented at                                      |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| GET         | /api/v1/cluster/self/repository/<'active'\|'archived'|'imported'>/<repository-id>/taskHistory                                    | [Get Backup Task History](backup-get-task-info.md) |
| GET         | /api/v1/cluster/self/repository/<'active'\|'archived'|'imported'>/<repository-id>/taskHistory?<task-subset-specification-string> | [Get Backup Task History](backup-get-task-info.md) |

### [](#data)Data

| HTTP Method | URI                                                                        | Documented at                              |
| ----------- | -------------------------------------------------------------------------- | ------------------------------------------ |
| DELETE      | /api/v1/cluster/self/repository/active/<repository-id>/backups/<backup-id> | [Delete Backups](backup-delete-backups.md) |

## [](#search-service-api)Search Service API

The Search Service allows users to create, manage, and query _Full Text Indexes_, whereby searches can be performed and matches attained on character strings. The Search Service REST API allows such indexes to be created and maintained. The API is listed in the tables below.

### [](#node-configuration)Node Configuration

| HTTP Method | URI              | Documented at                                                                 |
| ----------- | ---------------- | ----------------------------------------------------------------------------- |
| GET         | /api/cfg         | [Get Cluster Configuration](../fts-rest-nodes/index.md#getClusterConfig)      |
| POST        | /api/cfgRefresh  | [Refresh Node Configuration](../fts-rest-nodes/index.md#refreshClusterConfig) |
| POST        | /api/managerKick | [Replan Resource Assignments](../fts-rest-nodes/index.md#managerKick)         |
| GET         | /api/managerMeta | [Get Node Capabilities](../fts-rest-nodes/index.md#managerMeta)               |

### [](#node-diagnostics)Node Diagnostics

| HTTP Method | URI                         | Documented at                                                                           |
| ----------- | --------------------------- | --------------------------------------------------------------------------------------- |
| GET         | /api/diag                   | [Get Diagnostics](../fts-rest-nodes/index.md#getDiagnostics)                            |
| GET         | /api/log                    | [Get Node Logs](../fts-rest-nodes/index.md#getLogs)                                     |
| GET         | /api/runtime                | [Get Node Runtime Information](../fts-rest-nodes/index.md#getRuntimeInfo)               |
| GET         | /api/runtime/args           | [Get Node Runtime Arguments](../fts-rest-nodes/index.md#getRuntimeArgs)                 |
| POST        | /api/runtime/profile/cpu    | [Capture CPU Profiling Information](../fts-rest-nodes/index.md#captureCpuProfile)       |
| POST        | /api/runtime/profile/memory | [Capture Memory Profiling Information](../fts-rest-nodes/index.md#captureMemoryProfile) |

### [](#node-management)Node Management

| HTTP Method | URI             | Documented at                                                      |
| ----------- | --------------- | ------------------------------------------------------------------ |
| POST        | /api/runtime/gc | [Perform Garbage Collection](../fts-rest-nodes/index.md#performGC) |

### [](#node-monitoring)Node Monitoring

| HTTP Method | URI                         | Documented at                                                        |
| ----------- | --------------------------- | -------------------------------------------------------------------- |
| GET         | /api/runtime/stats          | [Get Runtime Statistics](../fts-rest-nodes/index.md#getRuntimeStats) |
| GET         | /api/runtime/stats/statsMem | [Get Memory Statistics](../fts-rest-nodes/index.md#getMemoryStats)   |

### [](#index-definition)Index Definition

| HTTP Method | URI                                                                | Documented at                                                                                          |
| ----------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| GET         | /api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index               | [Get All Search Index Definitions (Scoped)](../fts-rest-indexing/index.md#g-api-scoped-index)          |
| GET         | /api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME} | [Get Index Definition (Scoped)](../fts-rest-indexing/index.md#g-api-scoped-index-name)                 |
| PUT         | /api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME} | [Create or Update an Index Definition (Scoped)](../fts-rest-indexing/index.md#p-api-scoped-index-name) |
| DELETE      | /api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME} | [Delete Index Definition (Scoped)](../fts-rest-indexing/index.md#d-api-scoped-index-name)              |

### [](#index-management)Index Management

| HTTP Method | URI                                                                                       | Documented at                                                                                              |
| ----------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| POST        | /api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME}/ingestControl/{OP}     | [Set Index Ingestion Control (Scoped)](../fts-rest-indexing/index.md#p-api-scoped-ingestcontrol)           |
| POST        | /api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME}/planFreezeControl/{OP} | [Freeze Index Partition Assignment (Scoped)](../fts-rest-indexing/index.md#p-api-scoped-planfreezecontrol) |
| POST        | /api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME}/queryControl/{OP}      | [Stop Queries on an Index (Scoped)](../fts-rest-indexing/index.md#p-api-scoped-querycontrol)               |

### [](#index-monitoring-and-debugging)Index Monitoring and Debugging

| HTTP Method | URI                                                                       | Documented at                                                                                      |
| ----------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| GET         | /api/stats                                                                | [Get Indexing and Data Metrics for All Indexes](../fts-rest-indexing/index.md#g-api-stats)         |
| GET         | /api/stats/{INDEX\_NAME}                                                  | [Get Indexing and Data Metrics for an Index](../fts-rest-indexing/index.md#g-api-stats-index-name) |
| POST        | /api/stats/{INDEX\_NAME}/analyzeDoc                                       | [Analyze Document](../fts-rest-indexing/index.md#g-api-stats-index-name-analyzeDoc)                |
| GET         | /api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME}/status | [Get Index Status (Scoped)](../fts-rest-indexing/index.md#g-api-scoped-status)                     |

### [](#index-querying)Index Querying

| HTTP Method | URI                                                                             | Documented at                                                                                            |
| ----------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| GET         | /api/index/{INDEX\_NAME}/count                                                  | [Get Document Count for an Index](../fts-rest-indexing/index.md#g-api-index-name-count)                  |
| POST        | /api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME}/pindexLookup | [Look up the Index Partition for a Document (Scoped)](../fts-rest-indexing/index.md#p-api-pindex-lookup) |
| POST        | /api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME}/query        | [Query a Search Index (Scoped)](../fts-rest-indexing/index.md#p-api-scoped-query)                        |

### [](#index-partition-definition)Index Partition Definition

| HTTP Method | URI                      | Documented at                                                                 |
| ----------- | ------------------------ | ----------------------------------------------------------------------------- |
| GET         | /api/pindex              | [Get Index Partition Information](../fts-rest-advanced/index.md#getPartition) |
| GET         | /api/pindex/{pindexName} | [Get Index Partition by Name](../fts-rest-advanced/index.md#getPartitionName) |

### [](#index-partition-querying)Index Partition Querying

| HTTP Method | URI                            | Documented at                                                                         |
| ----------- | ------------------------------ | ------------------------------------------------------------------------------------- |
| GET         | /api/pindex/{pindexName}/count | [Get Index Partition Document Count](../fts-rest-advanced/index.md#getPartitionCount) |
| POST        | /api/pindex/{pindexName}/query | [Query Index Partition](../fts-rest-advanced/index.md#queryPartition)                 |

### [](#fts-memory-quota)FTS Memory Quota

| HTTP Method | URI            | Documented at                                                           |
| ----------- | -------------- | ----------------------------------------------------------------------- |
| POST        | /pools/default | [Set FTS Memory Quota](../fts-rest-advanced/index.md#setFtsMemoryQuota) |

### [](#search-statistics)Search Statistics

| HTTP Method | URI                              | Documented at                                                                                                     |
| ----------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| GET         | /api/nsstats                     | [Get Query, Mutation, and Partition Statistics for the Search Service](../fts-rest-stats/index.md#g-api-nsstats)  |
| GET         | /api/nsstats/index/{INDEX\_NAME} | [Get Query, Mutation, and Partition Statistics for an Index](../fts-rest-stats/index.md#g-api-nsstats-index-name) |

### [](#active-queries)Active Queries

| HTTP Method | URI                          | Documented at                                                           |
| ----------- | ---------------------------- | ----------------------------------------------------------------------- |
| GET         | /api/query                   | [View Active Node Queries](../fts-rest-query/index.md#api-query)        |
| GET         | /api/query/index/{indexName} | [View Active Index Queries](../fts-rest-query/index.md#api-query-index) |
| POST        | /api/query/{queryID}/cancel  | [Cancel Active Queries](../fts-rest-query/index.md#api-query-cancel)    |

### [](#search-manager-options)Search Manager Options

| HTTP Method | URI                 | Documented at                                                                 |
| ----------- | ------------------- | ----------------------------------------------------------------------------- |
| GET         | /api/managerOptions | [Rebalance Based on File Transfer](../fts-rest-manage/index.md#put%5Foptions) |

## [](#eventing-service-api)Eventing Service API

The _Eventing Service_ REST API provides methods for working with _Eventing Functions_. The complete API is listed at [Eventing REST API](../eventing-rest-api/index.md).

## [](#analytics-service-api)Analytics Service API

The _Analytics Service_ provides a REST API for querying, configuration, and the management of links and libraries. The API is listed in the following tables.

### [](#analytics-query-api)Analytics Query API

| HTTP Method | URI                | Documented at                                                                           |
| ----------- | ------------------ | --------------------------------------------------------------------------------------- |
| POST        | /analytics/service | [Query Service](../analytics-rest-service/index.md#post%5Fservice)                      |
| GET         | /analytics/service | [Read-Only Query Service](../analytics-rest-service/index.md#get%5Fservice)             |
| POST        | /query/service     | [Query Service (Alternative)](../analytics-rest-service/index.md#post%5Fquery)          |
| GET         | /query/service     | [Read-Only Query Service (Alternative)](../analytics-rest-service/index.md#get%5Fquery) |

### [](#analytics-admin-api)Analytics Admin API

| HTTP Method | URI                                  | Documented at                                                                  |
| ----------- | ------------------------------------ | ------------------------------------------------------------------------------ |
| GET         | /analytics/admin/active\_requests    | [Active Requests](../analytics-rest-admin/index.md#return%5Factive%5Frequests) |
| DELETE      | /analytics/admin/active\_requests    | [Request Cancellation](../analytics-rest-admin/index.md#cancel%5Frequest)      |
| GET         | /analytics/admin/completed\_requests | [Completed Requests](../analytics-rest-admin/index.md#completed%5Frequests)    |
| GET         | /analytics/cluster                   | [Cluster Status](../analytics-rest-admin/index.md#cluster%5Fstatus)            |
| POST        | /analytics/cluster/restart           | [Cluster Restart](../analytics-rest-admin/index.md#restart%5Fcluster)          |
| POST        | /analytics/node/restart              | [Node Restart](../analytics-rest-admin/index.md#restart%5Fnode)                |
| GET         | /analytics/status/ingestion          | [Ingestion Status](../analytics-rest-admin/index.md#ingestion%5Fstatus)        |

### [](#analytics-config-api)Analytics Config API

| HTTP Method | URI                       | Documented at                                                                      |
| ----------- | ------------------------- | ---------------------------------------------------------------------------------- |
| GET         | /analytics/config/service | [View Service-Level Parameters](../analytics-rest-config/index.md#get%5Fservice)   |
| PUT         | /analytics/config/service | [Modify Service-Level Parameters](../analytics-rest-config/index.md#put%5Fservice) |
| GET         | /analytics/config/node    | [View Node-Specific Parameters](../analytics-rest-config/index.md#get%5Fnode)      |
| PUT         | /analytics/config/node    | [Modify Node-Specific Parameters](../analytics-rest-config/index.md#put%5Fnode)    |

### [](#analytics-settings-api)Analytics Settings API

| HTTP Method | URI                 | Documented at                                                                    |
| ----------- | ------------------- | -------------------------------------------------------------------------------- |
| GET         | /settings/analytics | [View Analytics Settings](../analytics-rest-settings/index.md#get%5Fsettings)    |
| POST        | /settings/analytics | [Modify Analytics Settings](../analytics-rest-settings/index.md#post%5Fsettings) |

### [](#analytics-links-api)Analytics Links API

| HTTP Method | URI                            | Documented at                                                     |
| ----------- | ------------------------------ | ----------------------------------------------------------------- |
| POST        | /analytics/link/{scope}/{name} | [Create Link](../analytics-rest-links/index.md#post%5Flink)       |
| GET         | /analytics/link/{scope}/{name} | [Query Link](../analytics-rest-links/index.md#get%5Flink)         |
| PUT         | /analytics/link/{scope}/{name} | [Edit Link](../analytics-rest-links/index.md#put%5Flink)          |
| DELETE      | /analytics/link/{scope}/{name} | [Delete Link](../analytics-rest-links/index.md#delete%5Flink)     |
| GET         | /analytics/link                | [Query All Links](../analytics-rest-links/index.md#get%5Fall)     |
| GET         | /analytics/link/{scope}        | [Query Scope Links](../analytics-rest-links/index.md#get%5Fscope) |

### [](#analytics-library-api)Analytics Library API

| HTTP Method | URI                                  | Documented at                                                                   |
| ----------- | ------------------------------------ | ------------------------------------------------------------------------------- |
| GET         | /analytics/library                   | [Read All Libraries](../analytics-rest-library/index.md#get%5Fcollection)       |
| POST        | /analytics/library/{scope}/{library} | [Create or Update a Library](../analytics-rest-library/index.md#post%5Flibrary) |
| DELETE      | /analytics/library/{scope}/{library} | [Delete a Library](../analytics-rest-links/index.md#delete%5Flibrary)           |

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
| 202 Accepted              | The request is accepted for processing, but processing is not complete. Per HTTP/1.1, the response, if any, SHOULD include an indication of the request's current status, and either a pointer to a status monitor or some estimate of when the request will be fulfilled. |
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