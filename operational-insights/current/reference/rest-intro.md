---
title: REST API Overview
description: Operational Insights provides REST APIs for running requests,
  managing the service, and managing the cluster.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-intro.adoc
  xref: xref:enterprise-analytics:reference:rest-intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-intro.html)

# REST API Overview

> Operational Insights provides REST APIs for running requests, managing the service, and managing the cluster. 

The REST APIs fall into two groups:

* [Service APIs](rest-analytics.md): run requests and manage the service — querying, administration, configuration parameters, links, Iceberg catalogs, and logging. By default, they listen on port 8095, or 18095 for secure access.
* [Cluster Management APIs](rest-cluster-management.md): manage the cluster — initialization, nodes, rebalance and failover, server groups, security, statistics, and service settings. By default, they listen on port 8091, or 18091 for secure access.

This page provides a complete list of HTTP methods and URIs. It also lists [HTTP Request Headers](#http-request-headers) and [HTTP Response Codes](#http-response-codes).

## [](#service-apis)Service APIs

The Service APIs are listed in the following tables.

### [](#request-api)Request API

| HTTP Method | URI                                            | Documented at                                                                                    |
| ----------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| POST        | /api/v1/request                                | [Request Service](../analytics-rest-service/index.md#operation/post%5Fservice)                   |
| GET         | /api/v1/request                                | [Read-Only Request Service](../analytics-rest-service/index.md#operation/get%5Fservice)          |
| GET         | /api/v1/request/status/{request\_id}/{job\_id} | [Request Status](../analytics-rest-service/index.md#operation/get%5Frequest%5Fstatus)            |
| GET         | /api/v1/request/result/{request\_id}/{job\_id} | [Retrieve Request Result](../analytics-rest-service/index.md#operation/get%5Frequest%5Fresult)   |
| DELETE      | /api/v1/request/result/{request\_id}/{job\_id} | [Discard Request Result](../analytics-rest-service/index.md#operation/delete%5Frequest%5Fresult) |

### [](#administration-api)Administration API

| HTTP Method | URI                         | Documented at                                                                            |
| ----------- | --------------------------- | ---------------------------------------------------------------------------------------- |
| GET         | /api/v1/active\_requests    | [Active Requests](../analytics-rest-admin/index.md#operation/return%5Factive%5Frequests) |
| DELETE      | /api/v1/active\_requests    | [Request Cancellation](../analytics-rest-admin/index.md#operation/cancel%5Frequest)      |
| GET         | /api/v1/completed\_requests | [Completed Requests](../analytics-rest-admin/index.md#operation/completed%5Frequests)    |
| GET         | /api/v1/open\_requests      | [Open Requests](../analytics-rest-admin/index.md#operation/open%5Frequests)              |
| GET         | /api/v1/status/service      | [Service Status](../analytics-rest-admin/index.md#operation/service%5Fstatus)            |
| POST        | /api/v1/service/restart     | [Service Restart](../analytics-rest-admin/index.md#operation/restart%5Fservice)          |
| POST        | /api/v1/node/restart        | [Node Restart](../analytics-rest-admin/index.md#operation/restart%5Fnode)                |
| GET         | /api/v1/status/ingestion    | [Ingestion Status](../analytics-rest-admin/index.md#operation/ingestion%5Fstatus)        |
| GET         | /api/v1/health              | [Health Check](../analytics-rest-admin/index.md#operation/health%5Fcheck)                |

### [](#configuration-api)Configuration API

| HTTP Method | URI                    | Documented at                                                                                |
| ----------- | ---------------------- | -------------------------------------------------------------------------------------------- |
| GET         | /api/v1/config/service | [View Service-Level Parameters](../analytics-rest-config/index.md#operation/get%5Fservice)   |
| PUT         | /api/v1/config/service | [Modify Service-Level Parameters](../analytics-rest-config/index.md#operation/put%5Fservice) |
| GET         | /api/v1/config/node    | [View Node-Specific Parameters](../analytics-rest-config/index.md#operation/get%5Fnode)      |
| PUT         | /api/v1/config/node    | [Modify Node-Specific Parameters](../analytics-rest-config/index.md#operation/put%5Fnode)    |

### [](#links-api)Links API

| HTTP Method | URI                 | Documented at                                                                              |
| ----------- | ------------------- | ------------------------------------------------------------------------------------------ |
| POST        | /api/v1/link/{name} | [Create Link](../analytics-rest-links/index.md#tag/Single-Links/operation/post%5Flink)     |
| GET         | /api/v1/link/{name} | [Query Link](../analytics-rest-links/index.md#tag/Single-Links/operation/get%5Flink)       |
| PUT         | /api/v1/link/{name} | [Edit Link](../analytics-rest-links/index.md#tag/Single-Links/operation/put%5Flink)        |
| DELETE      | /api/v1/link/{name} | [Delete Link](../analytics-rest-links/index.md#tag/Single-Links/operation/delete%5Flink)   |
| GET         | /api/v1/link        | [Query All Links](../analytics-rest-links/index.md#tag/Multiple-Links/operation/get%5Fall) |

### [](#iceberg-api)Iceberg API

| HTTP Method | URI                                                                  | Documented at                                                                                           |
| ----------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| GET         | /api/v1/iceberg/catalog                                              | [List Catalogs](../analytics-rest-iceberg/index.md#tag/Iceberg/operation/list%5Ficeberg%5Fcatalogs)     |
| GET         | /api/v1/iceberg/catalog/{catalogName}/namespace                      | [List Namespaces](../analytics-rest-iceberg/index.md#tag/Iceberg/operation/list%5Ficeberg%5Fnamespaces) |
| GET         | /api/v1/iceberg/catalog/{catalogName}/namespace/{namespace}/table    | [List Tables](../analytics-rest-iceberg/index.md#tag/Iceberg/operation/list%5Ficeberg%5Ftables)         |
| GET         | /api/v1/iceberg/snapshot/{databaseName}/{scopeName}/{collectionName} | [List Snapshots](../analytics-rest-iceberg/index.md#tag/Iceberg/operation/list%5Ficeberg%5Fsnapshots)   |

### [](#logging-api)Logging API

| HTTP Method | URI                              | Documented at                                                                              |
| ----------- | -------------------------------- | ------------------------------------------------------------------------------------------ |
| GET         | /api/v1/cluster/logging          | [View Configured Loggers](../analytics-rest-logging/index.md#operation/get%5Floggers)      |
| PUT         | /api/v1/cluster/logging          | [Modify Logger Levels](../analytics-rest-logging/index.md#operation/put%5Floggers)         |
| DELETE      | /api/v1/cluster/logging          | [Reset All Loggers](../analytics-rest-logging/index.md#operation/delete%5Floggers)         |
| GET         | /api/v1/cluster/logging/all      | [List Available Loggers](../analytics-rest-logging/index.md#operation/get%5Fall%5Floggers) |
| GET         | /api/v1/cluster/logging/{logger} | [View Logger Level](../analytics-rest-logging/index.md#operation/get%5Flogger)             |
| PUT         | /api/v1/cluster/logging/{logger} | [Modify Logger Level](../analytics-rest-logging/index.md#operation/put%5Flogger)           |
| DELETE      | /api/v1/cluster/logging/{logger} | [Reset Logger Level](../analytics-rest-logging/index.md#operation/delete%5Flogger)         |

## [](#cluster-management-apis)Cluster Management APIs

> [!NOTE]
> Some `GET` endpoints in these APIs return fields that do not apply to Operational Insights. These fields are not documented, and can be ignored.

### [](#nodes-and-clusters-api)Nodes and Clusters API

The Cluster API provides support for managing and retrieving information about clusters. It also provides support for managing _rebalance_, _failover_, and _server group awareness_. The APIs for each area are assigned a table, below.

#### [](#cluster-initialization-and-provisioning)Cluster Initialization and Provisioning

| HTTP Method | URI                             | Documented at                                             |
| ----------- | ------------------------------- | --------------------------------------------------------- |
| POST        | /clusterInit                    | [Initialize a Cluster](rest-initialize-cluster.md)        |
| POST        | /nodes/self/controller/settings | [Initializing a Node](rest-initialize-node.md)            |
| POST        | /settings/web                   | [Establishing Credentials](rest-establish-credentials.md) |
| POST        | /node/controller/rename         | [Naming a Node](rest-name-node.md)                        |
| POST        | /pools/default                  | [Configuring Memory](rest-configure-memory.md)            |
| POST        | /pools/default                  | [Naming a Cluster](rest-name-cluster.md)                  |

#### [](#node-addition-and-removal)Node Addition and Removal

| HTTP Method | URI                            | Documented at                                              |
| ----------- | ------------------------------ | ---------------------------------------------------------- |
| POST        | /controller/addNode            | [Adding Nodes to Clusters](rest-cluster-addnodes.md)       |
| POST        | /node/controller/doJoinCluster | [Joining Nodes to Clusters](rest-cluster-joinnode.md)      |
| POST        | /controller/ejectNode          | [Removing Nodes from Clusters](rest-cluster-removenode.md) |

#### [](#rebalance)Rebalance

| HTTP Method | URI                                             | Documented at                                                                     |
| ----------- | ----------------------------------------------- | --------------------------------------------------------------------------------- |
| POST        | /controller/rebalance                           | [Rebalancing the Cluster](rest-cluster-rebalance.md)                              |
| GET         | /pools/default                                  | [Getting Rebalance Reason Codes](rest-retrieve-cluster-rebalance-reason-codes.md) |
| GET         | /pools/default/rebalanceProgress                | [Getting Rebalance Progress](rest-get-rebalance-progress.md)                      |
| GET         | /settings/retryRebalance                        | [Configuring Rebalance Retries](rest-configure-rebalance-retry.md)                |
| POST        | /settings/retryRebalance                        | [Configuring Rebalance Retries](rest-configure-rebalance-retry.md)                |
| GET         | /pools/default/pendingRetryRebalance            | [Getting Rebalance-Retry Status](rest-get-rebalance-retry.md)                     |
| POST        | /controller/cancelRebalanceRetry/<rebalance-id> | [Canceling Rebalance Retries](rest-cancel-rebalance-retry.md)                     |

#### [](#manual-failover)Manual-Failover

| HTTP Method | URI                         | Documented at                                     |
| ----------- | --------------------------- | ------------------------------------------------- |
| POST        | /controller/failOver        | [Performing Hard Failover](rest-node-failover.md) |
| POST        | /controller/setRecoveryType | [Setting Recovery Type](rest-node-recovery.md)    |
| POST        | /controller/hardResetNode   | [Reinitializing Nodes](rest-reinitialize-node.md) |

#### [](#auto-failover)Auto-Failover

| HTTP Method | URI                               | Documented at                                                               |
| ----------- | --------------------------------- | --------------------------------------------------------------------------- |
| GET         | /settings/autoFailover            | [Retrieving Auto-Failover Settings](rest-cluster-autofailover-settings.md)  |
| POST        | /settings/autoFailover            | [Enabling and Disabling Auto-Failover](rest-cluster-autofailover-enable.md) |
| POST        | /settings/autoFailover/resetCount | [Resetting Auto-Failover](rest-cluster-autofailover-reset.md)               |
| POST        | /controller/setRecoveryType       | [Setting Recovery Type](rest-node-recovery.md)                              |

#### [](#settings-and-connections)Settings and Connections

| HTTP Method | URI                                               | Documented at                                                                                 |
| ----------- | ------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| PUT         | /node/controller/setupAlternateAddresses/external | [Managing Alternate Addresses](rest-set-up-alternate-address.md)                              |
| DELETE      | /node/controller/setupAlternateAddresses/external | [Managing Alternate Addresses](rest-set-up-alternate-address.md)                              |
| GET         | /settings/alerts                                  | [Getting Alert Settings](rest-cluster-email-notifications.md#curl-syntax)                     |
| POST        | /settings/alerts                                  | [Enabling and Disabling Email Notifications](rest-cluster-email-notifications.md#curl-syntax) |
| POST        | /settings/alerts/testEmail                        | [Sending Test Emails](rest-cluster-email-notifications.md#curl-syntax)                        |
| GET         | /settings/alerts/limits                           | [Getting Alert Limits](rest-cluster-email-notifications.md#curl-syntax)                       |
| POST        | /settings/alerts/limits                           | [Setting Alert Limits](rest-cluster-email-notifications.md#curl-syntax)                       |

#### [](#status-and-events)Status and Events

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

#### [](#statistics)Statistics

| HTTP Method | URI                                                               | Documented at                                              |
| ----------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| GET         | /pools/default/stats/range/<metric\_name>/\[function-expression\] | [Getting a Single Statistic](rest-statistics-single.md)    |
| POST        | /pools/default/stats/range                                        | [Getting Multiple Statistics](rest-statistics-multiple.md) |
| GET         | /prometheus\_sd\_config                                           | [Prometheus Discovery API](rest-discovery-api.md)          |

#### [](#logging)Logging

| HTTP Method | URI                              | Documented at                                                 |
| ----------- | -------------------------------- | ------------------------------------------------------------- |
| POST        | /controller/startLogsCollection  | [Collecting Logs](rest-manage-log-collection.md)              |
| POST        | /controller/cancelLogsCollection | [Collecting Logs](rest-manage-log-collection.md)              |
| GET         | /pools/default/tasks             | [Getting Cluster Tasks](rest-get-cluster-tasks.md)            |
| GET         | /diag                            | [Retrieving Diagnostic and Log Information](rest-logs-get.md) |
| GET         | /sasl\_logs                      | [Retrieving Diagnostic and Log Information](rest-logs-get.md) |
| POST        | /logClientError                  | [Logging Client-Side Errors](rest-client-logs.md)             |

### [](#server-groups-api)Server Groups API

_Server Group Awareness_ provides enhanced availability. Specifically, it protects a cluster from large-scale infrastructure failure, through the definition of groups. Its REST API is expressed by the following table.

| HTTP Method | URI                                         | Documented at                                                   |
| ----------- | ------------------------------------------- | --------------------------------------------------------------- |
| GET         | /pools/default/serverGroups                 | [Getting Group Information](rest-servergroup-get.md)            |
| POST        | /pools/default/serverGroups                 | [Creating Groups](rest-servergroup-post-create.md)              |
| POST        | /pools/default/serverGroups/<:uuid>/addNode | [Adding Nodes to Groups](rest-servergroup-post-add.md)          |
| PUT         | /pools/default/serverGroups/<:uuid>         | [Renaming Groups](rest-servergroup-put.md)                      |
| PUT         | /pools/default/serverGroups?rev=<:number>   | [Updating Group Membership](rest-servergroup-put-membership.md) |
| DELETE      | /pools/default/serverGroups/<:uuid>         | [Deleting Groups](rest-servergroup-delete.md)                   |

### [](#security-api)Security API

The Security REST API provides the endpoints for general security, for authentication, and for authorization. These APIs are listed in the tables below.

#### [](#general-security)General Security

| HTTP Method | URI                                        | Documented at                                                       |
| ----------- | ------------------------------------------ | ------------------------------------------------------------------- |
| GET         | /whoami                                    | [Who Am I?](rest-whoami.md)                                         |
| GET         | /settings/audit                            | [Configure Auditing](rest-auditing.md)                              |
| POST        | /settings/audit                            | [Configure Auditing](rest-auditing.md)                              |
| GET         | /settings/audit/descriptors                | [Configure Auditing](rest-auditing.md)                              |
| GET         | /settings/audit/nonFilterableDescriptors   | [Configure Auditing](rest-auditing.md)                              |
| GET         | /settings/security                         | [Restrict Node-Addition](rest-specify-node-addition-conventions.md) |
| POST        | /settings/security                         | [Restrict Node-Addition](rest-specify-node-addition-conventions.md) |
| POST        | /clusterInit                               | [Initialize a Cluster](rest-initialize-cluster.md)                  |
| GET         | /settings/security/\[service-name\]        | [Configure On-the-Wire Security](rest-setting-security.md)          |
| POST        | /settings/security/\[service-name\]        | [Configure On-the-Wire Security](rest-setting-security.md)          |
| POST        | /node/controller/rotateInternalCredentials | [Rotate Internal Credentials](rest-rotate-internal-credentials.md)  |
| GET         | /settings/security/responseHeaders         | [Configure HSTS](rest-setting-hsts.md)                              |
| POST        | /settings/security/responseHeaders         | [Configure HSTS](rest-setting-hsts.md)                              |
| DELETE      | /settings/security/responseHeaders         | [Configure HSTS](rest-setting-hsts.md)                              |

#### [](#authentication)Authentication

| HTTP Method | URI                                                         | Documented at                                                         |
| ----------- | ----------------------------------------------------------- | --------------------------------------------------------------------- |
| GET         | /settings/ldap                                              | [Configure LDAP](rest-configure-ldap.md#get-settings-ldap)            |
| POST        | /settings/ldap                                              | [Configure LDAP](rest-configure-ldap.md#post-settings-ldap)           |
| GET         | /settings/saml                                              | [Configure SAML](rest-configure-saml.md#get-settings-saml)            |
| POST        | /settings/saml                                              | [Configure SAML](rest-configure-saml.md#post-settings-saml)           |
| GET         | /settings/saslauthdAuth                                     | [Configure saslauthd](rest-configure-saslauthd.md)                    |
| POST        | /settings/saslauthdAuth                                     | [Configure saslauthd](rest-configure-saslauthd.md)                    |
| GET         | /settings/passwordPolicy                                    | [Set Password Policy](rest-set-password-policy.md)                    |
| POST        | /settings/passwordPolicy                                    | [Set Password Policy](rest-set-password-policy.md)                    |
| POST        | /controller/changePassword                                  | [Change Password](rest-set-password.md)                               |
| POST        | /node/controller/loadTrustedCAs                             | [Load Root Certificates](load-trusted-cas.md)                         |
| GET         | /pools/default/trustedCAs                                   | [Get Root Certificates](get-trusted-cas.md)                           |
| DELETE      | /pools/default/trustedCAs/<id>                              | [Delete Root Certificates](delete-trusted-cas.md)                     |
| GET         | /pools/default/certificates                                 | [Retrieve All Node Certificates](retrieve-all-node-certs.md)          |
| POST        | /node/controller/reloadCertificate                          | [Upload and Retrieve Node Certificates](upload-retrieve-node-cert.md) |
| GET         | /pools/default/certificate/node/<ip-address-or-domain-name> | [Upload and Retrieve Node Certificates](upload-retrieve-node-cert.md) |
| POST        | /controller/regenerateCertificate                           | [Regenerate All Certificates](rest-regenerate-all-certs.md)           |

#### [](#authorization)Authorization

| HTTP Method | URI                                               | Documented at                                                                       |
| ----------- | ------------------------------------------------- | ----------------------------------------------------------------------------------- |
| GET         | /settings/rbac/roles                              | [List Roles](rbac.md#list-roles)                                                    |
| GET         | /settings/rbac/users                              | [List Current Users and Their Roles](rbac.md#list-current-users-and-their-roles)    |
| POST        | /pools/default/checkPermissions                   | [Check Permissions](rbac.md#check-permissions)                                      |
| GET         | /settings/rbac/groups                             | [List Currently Defined Groups](rbac.md#list-currently-defined-groups)              |
| PUT         | /settings/rbac/users/local/<new-username>         | [Create a Local User](rbac.md#create-a-local-user-and-assign-roles)                 |
| PATCH       | /settings/rbac/users/local/<existing-username>    | [Create a Local User](rbac.md#create-a-local-user-and-assign-roles)                 |
| PUT         | /settings/rbac/users/external/<new-username>      | [Create an External User](rbac.md#create-an-external-user-and-assign-roles)         |
| PUT         | /settings/rbac/groups/<new-groupname>             | [Create a Group](rbac.md#create-a-group-and-assign-it-roles)                        |
| DELETE      | /settings/rbac/users/local/<local-username>       | [Delete Users and Groups](rbac.md#delete-users-and-groups)                          |
| DELETE      | /settings/rbac/users/external/<external-username> | [Delete Users and Groups](rbac.md#delete-users-and-groups)                          |
| DELETE      | /settings/rbac/groups/<groupname>                 | [Delete Users and Groups](rbac.md#delete-users-and-groups)                          |
| GET         | /settings/rbac/backup                             | [Back Up and Restore Users and Groups](rbac.md#backup-and-restore-users-and-groups) |
| PUT         | /settings/rbac/backup                             | [Back Up and Restore Users and Groups](rbac.md#backup-and-restore-users-and-groups) |

#### [](#system-secrets-management)System-Secrets Management

| HTTP Method | URI                                   | Documented at                                                                                                  |
| ----------- | ------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| GET         | /nodes/self/secretsManagement         | [Configuring System Secrets](../manage/manage-security/manage-system-secrets.md#configuring-system-secrets)    |
| POST        | /node/controller/secretsManagement    | [Configuring System Secrets](../manage/manage-security/manage-system-secrets.md#configuring-system-secrets)    |
| POST        | /node/controller/changeMasterPassword | [Changing the Master Password](../manage/manage-security/manage-system-secrets.md#setting-the-master-password) |
| POST        | /node/controller/rotateDataKey        | [Rotating the Data Key](../manage/manage-security/manage-system-secrets.md#password%5Frotation)                |

### [](#service-settings-api)Service Settings API

The Service Settings API configures cluster-wide settings for the service, such as the object storage that holds its data.

| HTTP Method | URI                           | Documented at                                                                            |
| ----------- | ----------------------------- | ---------------------------------------------------------------------------------------- |
| GET         | /settings/operationalInsights | [View Service Settings](../analytics-rest-settings/index.md#operation/get%5Fsettings)    |
| POST        | /settings/operationalInsights | [Modify Service Settings](../analytics-rest-settings/index.md#operation/post%5Fsettings) |

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

The Operational Insights returns one of the following HTTP status codes in response to REST API requests:

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