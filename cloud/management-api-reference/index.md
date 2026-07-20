---
title: Capella Operational Management API Reference
editUrl: https://github.com/couchbasecloud/couchbase-cloud/edit/main/docs/public/modules/management-api-reference/pages/index.adoc
pubDate: 2026-07-20T13:54:32.914Z
link: xref:cloud:management-api-reference:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/management-api-reference/index.html)

# Capella Operational Management API Reference

* Capella Operational
  * Alert Integration
    * postCreate Alert Integration
    * getList Alert Integrations
    * postList Channels for an Alert Integration
    * getGet Alert Integration
    * putUpdate Alert Integration
    * delDelete Alert Integration
    * postTest Alert Integration
  * Allowed CIDRs (App Services)
    * delDelete App Service Allowed CIDR
    * getList Allowed CIDRs for an App Service
    * postCreate Allowed CIDR
  * Allowed CIDRs (Cluster)
    * postCreate Allowed CIDR
    * getList Allowed CIDRs
    * getget allowed CIDR
    * delDelete Allowed CIDR
  * Api Keys
    * postCreate API Key
    * getList API keys
    * getGet API Key
    * delDelete API Key
    * postRotate API Key
  * App Endpoints
    * getList App Endpoints
    * postCreate App Endpoint
    * getGet App Endpoint
    * putUpdate App Endpoint
    * delDelete App Endpoint
    * getList App Endpoint Collections
    * postResume or Bring an App Endpoint online
    * delPause or Take an App Endpoint offline
    * getGet the App Endpoint Cross-Origin Resource Sharing (CORS) Configuration.
    * putUpsert the App Endpoint Cross-Origin Resource Sharing (CORS) Configuration.
    * getGet Access Control and Validation function
    * putUpsert custom Access Control and Validation function
    * delDelete Access Control and Validation function
    * getGet Import Filter
    * putUpsert Import Filter
    * delDelete Import Filter
    * postCreate App Endpoint OpenID Connect (OIDC) Provider
    * getList App Endpoint OpenID Connect (OIDC) Providers
    * getGet App Endpoint OpenID Connect (OIDC) Provider
    * putUpdate App Endpoint OpenID Connect (OIDC) Provider
    * delDelete App Endpoint OpenID Connect (OIDC) Provider
    * putUpdate App Endpoint Default OIDC Provider
    * getGet Resync Status
    * postStart Resync
    * delStop Resync
  * App Services
    * postCreate App Service
    * getList AppServices
    * getGet App Service
    * putUpdate App Service
    * delDelete App Service
    * postTurn On App Service
    * delTurn Off App Service
    * postCreate App Service Admin User
    * getList App Service Admin Users
    * putUpdate App Service Admin User
    * delDelete App Service Admin User
    * getGet App Service Admin User
    * putOpt App Service Back In to Metadata Isolation
    * getGet App Service Metadata Isolation State
    * getGet Public Certificate for App Service
    * getList App Endpoint Admin Users
  * App Services Audit Logging
    * putEnable or Disable App Service Audit Logging
    * getGet App Service Audit Log State
    * getList App Endpoint Audit Log Event IDs
    * putUpdate App Endpoint Audit Logging Config
    * getGet App Endpoint Audit Logging Config
    * putConfigure App Service Audit Log Streaming
    * patchStart or Resume Audit Log Streaming
    * getGet App Service Audit Log Streaming State
    * postInitiate Audit Log Export
    * getList Audit Log Export Jobs
    * getGet Audit Log Export Job
  * App Services Log Streaming
    * postResume App Service Log Streaming
    * delPause App Service Log Streaming
    * postConfigure App Service Log Streaming
    * getGet App Service Log Streaming Configuration and State
    * delDisable App Service Log Streaming
    * putUpdate App Endpoint Log Streaming Config
    * getGet App Endpoint Log Streaming Config
  * App Services Private Endpoints
    * postEnable App Service Private Endpoints
    * getGet App Service Private Endpoints State
    * delDisable App Service Private Endpoints
    * postGet App Service Private Endpoints Command
    * getList App Service Private Endpoints
    * postAccept Private Endpoint Request
    * delDelete Private Endpoint Request
  * Audit Logs
    * putUpdate Cluster Audit Log Configuration
    * getGet Cluster Audit Log Configuration
    * getList Filterable Audit Log Events
    * postCreate Cluster Audit Log Export job
    * getList Cluster Audit Log Export Jobs
    * getGet Cluster Audit Log Export
  * Backup Schedule (Bucket)
    * postCreate Backup Schedule
    * getGet Backup Schedule
    * putUpdate Backup Schedule
    * delDelete Backup Schedule
    * getList Cycles
    * getList Backups
  * Backups & Restore (Bucket)
    * postCreate Backup
    * getList Cluster Backups
    * getGet Backup
    * delDelete Backup Cycle
    * postRestore Backup
  * Billing
    * postGet Categorized Billing
    * postGet Itemized Billing Per Cluster
    * getGet Prepaid Credits Billing
    * getGet Pay As You Go Billing
    * postDownload Categorized Billing
    * postDownload Itemized Billing
  * Buckets, Scopes, & Collections
    * postCreate Bucket
    * getList Buckets
    * getGet Bucket
    * putUpdate Bucket
    * delDelete Bucket
    * putFlush Bucket Data
    * postCreate Scope
    * getList Scopes
    * getGet Scope
    * delDelete Scope
    * postCreate Collection
    * getList Collections
    * getGet Collection
    * putUpdate Collection
    * delDelete Collection
  * Certificates
    * getGet Certificate
  * Cloud Snapshot Backups & Restore
    * postCreate Cloud Snapshot Backup
    * getList Cloud Snapshot Backups
    * getList Cloud Snapshot Restores
    * getList Available Geographic Regions for Cross-region Operations
    * putEdit Backup Retention
    * delDelete Backup
    * postRestore Backup
    * getList Cloud Snapshot Backups at the Project Level
    * postClone Cluster Backup
  * Cloud Snapshot Backups Schedule
    * putUpsert Backup Schedule
    * getGet Backup Schedule
    * delDelete Backup Schedule
  * Clusters
    * postCreate Cluster
    * getList Clusters
    * getGet Cluster
    * putUpdate Cluster
    * delDelete Cluster
    * getGet Cluster Capacity Statistics
    * postTurn On Cluster
    * delTurn Off Cluster
    * putMigrate Buckets
    * putUpdate Deletion Protection
  * CMEK
    * getGet Cloud Accounts
    * getGet Azure Application ID
    * getGet Azure Application ID For Project
    * postCreate Key Metadata
    * getList Key Metadata
    * postCreate Azure Key Metadata For Project
    * getList Azure Key Metadata For Project
    * getList Key Rotation History
    * getGet Key Metadata
    * putRotate Key
    * delDelete Key Metadata
    * getGet Azure Key Metadata For Project
    * putRotate Azure Key For Project
    * delDelete Azure Key Metadata For Project
    * putEnable CMEK For Cloud Services Provider
    * putEnable Azure CMEK For Project
    * postAssociate Key with Cluster
    * postUnassociate Key from Cluster
  * Data API
    * putUpdate Data API
    * getGet Data API Status
    * postGet CLI Commands For Setting Up Private Endpoint Connection
    * getList Data API Private Endpoints
    * postAccept Data API Private Endpoint Connection
    * postDisassociate Data API Private Endpoint
  * Database Credentials
    * getList Database Credentials
    * postCreate Database Credentials
    * getGet Database Credentials
    * putUpdate Database Credentials
    * delDelete Database Credentials
  * Eventing Functions
    * getGet Eventing Function Code
    * putUpdate Eventing Function Code
    * getGet Eventing Function
    * delDelete Eventing Function
    * putUpdate Eventing Function
    * postCreate Eventing Function
    * getList Eventing Functions
    * putSet Eventing Function State
    * getGet Function Logs
  * Events
    * getList Events
    * getGet Event
    * getList Events
    * getGet Project Event
  * Free Tier
    * postCreate Free Tier Cluster
    * getGet Free Tier Cluster
    * putUpdate Free Tier Cluster
    * delDelete Free Tier Cluster
    * postTurn On Free Tier Cluster
    * delTurn Off Free Tier Cluster
    * postCreate Free Tier App Service
    * getGet Free Tier App Service
    * putUpdate Free Tier App Service
    * delDelete Free Tier App Service
    * postCreate Free Tier Bucket
    * getList Free Tier Buckets
    * getGet Free Tier Bucket
    * putUpdate Free Tier Bucket
    * delDelete Free Tier Bucket
  * Network Peers
    * postCreate Network Peering
    * getList Network Peering Records
    * getGet Network Peering record
    * delDelete Network Peering
    * postGet Azure VNET Peering CLI Command
  * On/Off Schedule
    * postCreate Cluster On/Off schedule
    * getGet Cluster On/Off schedule
    * putUpdate Cluster On/Off schedule
    * delDelete Cluster On/Off schedule
    * delPause Cluster On/Off Schedule
    * postUnpause Cluster On/Off Schedule
  * Organizations
    * getGet Organization
    * putUpdate Organization Configuration
    * getList Organizations
  * Private Endpoint Service
    * getGet Private Endpoint Service Status
    * postEnable Private Endpoint Service
    * putUpdate Private Endpoint Service Configuration
    * delDisable Private Endpoint Service
    * getList Private Endpoints
    * postGet Private Endpoint CLI Command required to setup private endpoint for specific CSP
    * postAccept Private Endpoint Request
    * postReject or disassociate Private Endpoint
  * Projects
    * postCreate Project
    * getList Project
    * getGet Project
    * putUpdate Project
    * delDelete Project
  * Query Indexes
    * postManage Query Indexes
    * getGet List Of Index Definitions
    * getGet Index Properties
    * getGet Index Build Status
  * Replications
    * getGet replication details
    * delDelete a replication
    * putUpdate an existing replication
    * getGet replication job details
    * getList replications for a given cluster
    * postCreate a new replication
    * getList replications for a given project
    * delPause a replication
    * postResume a replication
  * Sample Bucket
    * postLoad Sample Data
    * getList Sample Data Import Buckets
    * getGet Sample Import Bucket
    * delDelete Sample Import Bucket
  * Users
    * postCreate User
    * getList Users
    * getGet User
    * patchUpdate User
    * delDelete User
* AI Data Plane
  * AI Data Plane Providers
    * getList providers
    * postCreate provider
    * getGet provider
    * putUpdate provider
    * delDelete provider
  * AI Workflows
    * getList AI Workflows
    * postCreate AI Workflow
    * getGet AI Workflow
    * delDelete AI Workflow
    * getList AI Workflow Runs
    * postRun an AI Workflow
    * delStop AI Workflow Run
    * getGet AI Workflow Run
    * getGet AI Workflow Run Processed Files
    * getGet Supported External Embedding Models
  * Model Services API Keys (AI Data Plane)
    * postCreate API Key
    * getList API keys
    * getGet API Key
    * delDelete API key
  * Models (AI Data Plane)
    * getList Models
    * postCreate Model
    * getGet Model
    * delDelete Model
    * putUpdate Model
    * getGet Model Connection String
    * postTurn On Model
    * delTurn Off Model

[API docs by Redocly](https://redocly.com/redoc/)

# Couchbase Capella Management API (v4.0)

Download OpenAPI specification:

The Couchbase Capella Management API provides a set of REST APIs for creating and managing Capella instances. It enables users to perform operations such as creating new Capella instances, managing their configurations, and interacting with the Capella services. This API documentation specifies the endpoints, request and response formats, and authentication requirements for seamless integration with Couchbase Capella.

To access the Management API, you need an API key. To create an initial bootstrap API key you must use the Capella UI. Once you have created an initial bootstrap API key, you can use the Management API itself to create further API keys. To learn more, see [Get Started with the Management API v4.0](https://docs.couchbase.com/cloud/management-api-guide/management-api-start.html).

For a history of updates to the Management API, see [Management API v4.0 Change Log](https://docs.couchbase.com/cloud/management-api-guide/management-api-log.html).

**API Base URL:**

`https://cloudapi.cloud.couchbase.com`

[Back to Management API v4.0 Documentation](https://docs.couchbase.com/cloud/management-api-guide/management-api-intro.html)

## [](#tag/Alert-Integration)Alert Integration

Couchbase Capella supports sending Capella alert notifications to the most common service like ServiceNow.

## [](#tag/Alert-Integration/operation/postAlertIntegration)Create Alert Integration 

Creates a new alert integration for a project.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

##### Request Body schema: application/json

| kindrequired   | string Enum: "webhook" "slack" "teams" Type of alert integration.                |
| -------------- | -------------------------------------------------------------------------------- |
| namerequired   | string <= 1024 characters Name of the alert integration (up to 1024 characters). |
| configrequired | object or object or object (RequestConfig)                                       |

### Responses

**201** 

Successfully created an alert integration.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**504** 

The server did not get a response in time from the upstream server in order to complete the request.

post/v4/organizations/{organizationId}/projects/{projectId}/alertIntegrations

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/alertIntegrations

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "kind": "slack",
* "name": "test alert 1",
* "config": {
  * "webhook": {
    * "method": "POST",
    * "url": "<https://company.servicenow.com>",
    * "token": "QktxVUtFU1dKV1FlJBYXdnTVlRemFZdlRDZTg6eFh4dzU4JUYjqdUwwYkJoTjZSTmlzRWFIRHF0b1h4a08yazBpQjJ1bms1OW4yTUhdsfRib3IhVQ==",
    * "basicAuth": {
      * "user": "username80085",
      * "password": "yed69khj420_i"  
      },
    * "headers": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "exclude": {
      * "clusters": [
        * "ffffffff-aaaa-1414-eeee-000000000000",
        * "..."  
            ],
      * "appServices": [
        * "ffffffff-aaaa-1414-eeee-000000000000",
        * "..."  
            ]  
      }  
  },
  * "slack": {
    * "botToken": "string",
    * "channel": "#alerts",
    * "clusterChannelMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "appServiceChannelMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "clusterWebhookChannelMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "appServiceWebhookChannelMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "channelWebhookUrlMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "customPayloads": {
      * "property1": {
        * "payload": { }  
            },
      * "property2": {
        * "payload": { }  
            }  
      }  
  },
  * "teams": {
    * "webhookUrlMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "clusterWebhookMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "appServiceWebhookMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "customPayloads": {
      * "property1": {
        * "payload": { }  
            },
      * "property2": {
        * "payload": { }  
            }  
      }  
  }  
}
}`

### Response samples 

* 201
* 403
* 404
* 409
* 422
* 429
* 500
* 504

Content type

application/json

Copy

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/Alert-Integration/operation/listAlertIntegrations)List Alert Integrations 

Lists all the alert integrations under the project.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Organization Member
* Project Owner
* Project Manager
* Project Viewer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                 |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                       |
| sortBy        | Array of strings Example: sortBy=nameSets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **id**, **name**. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                              |

### Responses

**200** 

Successfully listed all the alert integrations under the project.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**504** 

The server did not get a response in time from the upstream server in order to complete the request.

get/v4/organizations/{organizationId}/projects/{projectId}/alertIntegrations

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/alertIntegrations

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500
* 504

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "name": "test alert 1",
    * "tenantId": "ffffffff-aaaa-1414-eeee-000000000000",
    * "projectId": "ffffffff-aaaa-1414-eeee-000000000000",
    * "kind": "teams",
    * "configKey": "ffffffff-aaaa-1414-eeee-000000000000-alert-integration",
    * "status": "healthy",
    * "enabled": false,
    * "config": {
      * "webhook": {
        * "method": "POST",
        * "url": "<https://company.servicenow.com>",
        * "headers": {
          * "property1": "string",
          * "property2": "string"  
                    },
        * "exclude": {
          * "clusters": [
            * "ffffffff-aaaa-1414-eeee-000000000000",
            * "..."  
                              ],
          * "appServices": [
            * "ffffffff-aaaa-1414-eeee-000000000000",
            * "..."  
                              ]  
                    }  
            },
      * "slack": {
        * "channel": "#alerts",
        * "clusterChannelMappings": {
          * "property1": "string",
          * "property2": "string"  
                    },
        * "appServiceChannelMappings": {
          * "property1": "string",
          * "property2": "string"  
                    },
        * "clusterWebhookChannelMappings": {
          * "property1": "string",
          * "property2": "string"  
                    },
        * "appServiceWebhookChannelMappings": {
          * "property1": "string",
          * "property2": "string"  
                    },
        * "customPayloads": {
          * "property1": {
            * "payload": { }  
                              },
          * "property2": {
            * "payload": { }  
                              }  
                    }  
            },
      * "teams": {
        * "clusterWebhookMappings": {
          * "property1": "string",
          * "property2": "string"  
                    },
        * "appServiceWebhookMappings": {
          * "property1": "string",
          * "property2": "string"  
                    },
        * "customPayloads": {
          * "property1": {
            * "payload": { }  
                              },
          * "property2": {
            * "payload": { }  
                              }  
                    }  
            }  
      },
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56Z",
      * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "modifiedAt": "2021-09-01T12:34:56Z",
      * "version": 1  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/Alert-Integration/operation/postListAlertIntegrationChannels)List Channels for an Alert Integration 

Lists Slack or Teams channels available to a bot token or existing alert integration, for populating channel mappings.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

##### Request Body schema: application/json

One of 

objectobject

| botTokenrequired | string Slack bot token (starts with xoxb-). Mutually exclusive with integrationId.                   |
| ---------------- | ---------------------------------------------------------------------------------------------------- |
| integrationId    | string <uuid\> ID of an existing Slack or Teams alert integration. Mutually exclusive with botToken. |

### Responses

**200** 

Successfully listed the channels.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**504** 

The server did not get a response in time from the upstream server in order to complete the request.

post/v4/organizations/{organizationId}/projects/{projectId}/alertIntegrations/channels

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/alertIntegrations/channels

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "botToken": "xoxb-1234567890-1234567890123-AbCdEfGhIjKlMnOpQrStUvWx",
* "integrationId": "497a18ca-284e-40c0-985d-f72be35d468e"
}`

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500
* 504

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "channels": [
  * {
    * "id": "C01234ABCDE",
    * "name": "alerts",
    * "type": "public"  
  }  
]
}`

## [](#tag/Alert-Integration/operation/getAlertIntegrationByID)Get Alert Integration 

Fetches the details of the given alert integration.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Organization Member
* Project Owner
* Project Manager
* Project Viewer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| alertIntegrationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the alert integration. |

### Responses

**200** 

Successfully fetched the alert integration based on the alertIntegrationId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**504** 

The server did not get a response in time from the upstream server in order to complete the request.

get/v4/organizations/{organizationId}/projects/{projectId}/alertIntegrations/{alertIntegrationId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/alertIntegrations/{alertIntegrationId}

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500
* 504

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "name": "test alert 1",
* "tenantId": "ffffffff-aaaa-1414-eeee-000000000000",
* "projectId": "ffffffff-aaaa-1414-eeee-000000000000",
* "kind": "teams",
* "configKey": "ffffffff-aaaa-1414-eeee-000000000000-alert-integration",
* "status": "healthy",
* "enabled": false,
* "config": {
  * "webhook": {
    * "method": "POST",
    * "url": "<https://company.servicenow.com>",
    * "headers": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "exclude": {
      * "clusters": [
        * "ffffffff-aaaa-1414-eeee-000000000000",
        * "..."  
            ],
      * "appServices": [
        * "ffffffff-aaaa-1414-eeee-000000000000",
        * "..."  
            ]  
      }  
  },
  * "slack": {
    * "channel": "#alerts",
    * "clusterChannelMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "appServiceChannelMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "clusterWebhookChannelMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "appServiceWebhookChannelMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "customPayloads": {
      * "property1": {
        * "payload": { }  
            },
      * "property2": {
        * "payload": { }  
            }  
      }  
  },
  * "teams": {
    * "clusterWebhookMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "appServiceWebhookMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "customPayloads": {
      * "property1": {
        * "payload": { }  
            },
      * "property2": {
        * "payload": { }  
            }  
      }  
  }  
},
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
}
}`

## [](#tag/Alert-Integration/operation/putAlertIntegration)Update Alert Integration 

Update the details of the given alert integration.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| alertIntegrationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the alert integration. |

##### Request Body schema: application/json

| kind    | string Enum: "webhook" "slack" "teams" Type of alert integration. If provided, must match the existing integration's kind. This field cannot be used to change the integration kind. |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| name    | string or null <= 1024 characters Name of the alert integration (up to 1024 characters).                                                                                             |
| enabled | boolean Enables or disables the integration.                                                                                                                                         |
| config  | object or object or object (UpdateRequestConfig)                                                                                                                                     |

### Responses

**200** 

Successfully updated the metadata for the alert integration.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**504** 

The server did not get a response in time from the upstream server in order to complete the request.

put/v4/organizations/{organizationId}/projects/{projectId}/alertIntegrations/{alertIntegrationId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/alertIntegrations/{alertIntegrationId}

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "kind": "slack",
* "name": "test alert 1",
* "enabled": true,
* "config": {
  * "webhook": {
    * "method": "POST",
    * "url": "<https://company.servicenow.com>",
    * "token": "QktxVUtFU1dKV1FlJBYXdnTVlRemFZdlRDZTg6eFh4dzU4JUYjqdUwwYkJoTjZSTmlzRWFIRHF0b1h4a08yazBpQjJ1bms1OW4yTUhdsfRib3IhVQ==",
    * "basicAuth": {
      * "user": "username80085",
      * "password": "yed69khj420_i"  
      },
    * "headers": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "exclude": {
      * "clusters": [
        * "ffffffff-aaaa-1414-eeee-000000000000",
        * "..."  
            ],
      * "appServices": [
        * "ffffffff-aaaa-1414-eeee-000000000000",
        * "..."  
            ]  
      }  
  },
  * "slack": {
    * "botToken": "string",
    * "channel": "string",
    * "clusterChannelMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "appServiceChannelMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "clusterWebhookChannelMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "appServiceWebhookChannelMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "channelWebhookUrlMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "customPayloads": {
      * "property1": {
        * "payload": { }  
            },
      * "property2": {
        * "payload": { }  
            }  
      }  
  },
  * "teams": {
    * "webhookUrlMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "clusterWebhookMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "appServiceWebhookMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "customPayloads": {
      * "property1": {
        * "payload": { }  
            },
      * "property2": {
        * "payload": { }  
            }  
      }  
  }  
}
}`

### Response samples 

* 200
* 400
* 403
* 404
* 409
* 412
* 422
* 429
* 500
* 504

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "name": "test alert 1",
* "tenantId": "ffffffff-aaaa-1414-eeee-000000000000",
* "projectId": "ffffffff-aaaa-1414-eeee-000000000000",
* "kind": "teams",
* "configKey": "ffffffff-aaaa-1414-eeee-000000000000-alert-integration",
* "status": "healthy",
* "enabled": false,
* "config": {
  * "webhook": {
    * "method": "POST",
    * "url": "<https://company.servicenow.com>",
    * "headers": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "exclude": {
      * "clusters": [
        * "ffffffff-aaaa-1414-eeee-000000000000",
        * "..."  
            ],
      * "appServices": [
        * "ffffffff-aaaa-1414-eeee-000000000000",
        * "..."  
            ]  
      }  
  },
  * "slack": {
    * "channel": "#alerts",
    * "clusterChannelMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "appServiceChannelMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "clusterWebhookChannelMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "appServiceWebhookChannelMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "customPayloads": {
      * "property1": {
        * "payload": { }  
            },
      * "property2": {
        * "payload": { }  
            }  
      }  
  },
  * "teams": {
    * "clusterWebhookMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "appServiceWebhookMappings": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "customPayloads": {
      * "property1": {
        * "payload": { }  
            },
      * "property2": {
        * "payload": { }  
            }  
      }  
  }  
},
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
}
}`

## [](#tag/Alert-Integration/operation/deleteAlertIntegrationByID)Delete Alert Integration 

Deletes an existing alert integration.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| alertIntegrationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the alert integration. |

### Responses

**204** 

Successfully deleted the alert integration by its alertIntegrationId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**504** 

The server did not get a response in time from the upstream server in order to complete the request.

delete/v4/organizations/{organizationId}/projects/{projectId}/alertIntegrations/{alertIntegrationId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/alertIntegrations/{alertIntegrationId}

### Response samples 

* 403
* 404
* 429
* 500
* 504

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Alert-Integration/operation/postTestAlertIntegration)Test Alert Integration 

Tests a new alert integration for a project.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

##### Request Body schema: application/json

One of 

objectobjectobject

| kindrequired   | string Enum: "webhook" "slack" "teams" Type of alert integration. |
| -------------- | ----------------------------------------------------------------- |
| configrequired | object or object or object                                        |

### Responses

**202** 

Successfully tested an alert integration.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**504** 

The server did not get a response in time from the upstream server in order to complete the request.

post/v4/organizations/{organizationId}/projects/{projectId}/alertIntegrationTest

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/alertIntegrationTest

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "kind": "slack",
* "config": {
  * "webhook": {
    * "method": "POST",
    * "url": "<https://company.servicenow.com>",
    * "token": "QktxVUtFU1dKV1FlJBYXdnTVlRemFZdlRDZTg6eFh4dzU4JUYjqdUwwYkJoTjZSTmlzRWFIRHF0b1h4a08yazBpQjJ1bms1OW4yTUhdsfRib3IhVQ==",
    * "basicAuth": {
      * "user": "username80085",
      * "password": "yed69khj420_i"  
      },
    * "headers": {
      * "property1": "string",
      * "property2": "string"  
      },
    * "exclude": {
      * "clusters": [
        * "ffffffff-aaaa-1414-eeee-000000000000",
        * "..."  
            ],
      * "appServices": [
        * "ffffffff-aaaa-1414-eeee-000000000000",
        * "..."  
            ]  
      }  
  },
  * "slack": {
    * "webhookURL": "<http://example.com>",
    * "webhookUrl": "<http://example.com>",
    * "channelName": "#alerts",
    * "channel": "#alerts",
    * "botToken": "string"  
  },
  * "teams": {
    * "url": "<http://example.com>"  
  }  
}
}`

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500
* 504

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Allowed-CIDRs-%28App-Services%29)Allowed CIDRs (App Services)

App Services only allow trusted IP addresses to connect and use its REST APIs. Each App Service has a configurable Allowed IP list that can include up to 75 entries. Each entry can be a single IP address or an IP address space. Any IP address you add to this list can have a user-specified expiration time for temporary access, or be permanent. Capella automatically denies any connection attempts to and from an IP not in the allowed IP list.

## [](#tag/Allowed-CIDRs-%28App-Services%29/operation/deleteAppServiceAllowedCidr)Delete App Service Allowed CIDR 

Deletes an Allowed CIDR by ID on the specified App Service.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| allowedCidrIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the allowed CIDR. |

### Responses

**204** 

Successfully deleted the Allowed CIDR by its ID.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/allowedcidrs/{allowedCidrId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/allowedcidrs/{allowedCidrId}

### Response samples 

* 403
* 404
* 409
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Allowed-CIDRs-%28App-Services%29/operation/listAppServiceAllowedCidrs)List Allowed CIDRs for an App Service 

Lists the Allowed CIDRs for the specified App Service.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                            |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                  |
| sortBy        | Array of strings Example: sortBy=id Sets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **id**, **type**, **status**. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                         |

### Responses

**200** 

Successfully retrieved the allowed CIDRs for the App Service.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/allowedcidrs

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/allowedcidrs

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "cidr": "1.23.45.67/32",
    * "comment": "Allows access from my local developer machine",
    * "expiresAt": "2023-05-14T21:49:58.465Z",
    * "status": "active",
    * "type": "temporary",
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56Z",
      * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "modifiedAt": "2021-09-01T12:34:56Z",
      * "version": 1  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/Allowed-CIDRs-%28App-Services%29/operation/postAppServiceAllowedCidr)Create Allowed CIDR 

Adds a trusted CIDR to the specified App Service's list of allowed CIDRs.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

##### Request Body schema: application/json

| cidrrequired | string The trusted CIDR to allow network connections from. The example represents a single IP address (i.e. a subnet mask of 32).                                                                |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| comment      | string A short description of the allowed CIDR.                                                                                                                                                  |
| expiresAt    | string <date-time\> An RFC3339 timestamp determining when the allowed CIDR should expire. If this field is empty/omitted then the allowed CIDR is permanent and will never automatically expire. |

### Responses

**201** 

Successfully added an Allowed CIDR for the App Service.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/allowedcidrs

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/allowedcidrs

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "cidr": "6.60.28.100/32",
* "comment": "Allows access from my local developer machine",
* "expiresAt": "2023-05-14T21:49:58.465Z"
}`

### Response samples 

* 201
* 400
* 403
* 404
* 409
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/Allowed-CIDRs-%28Cluster%29)Allowed CIDRs (Cluster)

Couchbase Capella only allows trusted IP addresses to connect to databases. Each database has a configurable Allowed IP list that can include up to 75 entries. Each entry can be a single IP address or an IP address space. Any IP address you add to this list can have a user-specified expiration time for temporary access, or be permanent. Capella automatically denies any connection attempts to and from an IP not in the allowed IP list.

## [](#tag/Allowed-CIDRs-%28Cluster%29/operation/postAllowedCidrs)Create Allowed CIDR 

Adds a trusted CIDR to a cluster's list of allowed CIDRs.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

Note that updating this resource is not supported; you must delete and recreate allowed CIDRs instead. As a result, ETags are also not supported for this resource.

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| cidrrequired | string The trusted CIDR to allow the database connections from. The example represents a single IP address (i.e. a subnet mask of 32).                                                           |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| comment      | string A short description of the allowed CIDR.                                                                                                                                                  |
| expiresAt    | string <date-time\> An RFC3339 timestamp determining when the allowed CIDR should expire. If this field is empty/omitted then the allowed CIDR is permanent and will never automatically expire. |

### Responses

**201** 

Successfully added an allowed CIDR for the cluster.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/allowedcidrs

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/allowedcidrs

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "cidr": "6.60.28.100/32",
* "comment": "Allows access from my local developer machine",
* "expiresAt": "2023-05-14T21:49:58.465Z"
}`

### Response samples 

* 201
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/Allowed-CIDRs-%28Cluster%29/operation/listAllowedCidrs)List Allowed CIDRs 

Lists all of the allowed CIDRs for a given cluster.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                            |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                  |
| sortBy        | Array of strings Example: sortBy=id Sets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **id**, **type**, **status**. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                         |

### Responses

**200** 

Successfully listed all allowed CIDRs for the cluster.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/allowedcidrs

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/allowedcidrs

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "cidr": "1.23.45.67/32",
    * "comment": "Allows access from my local developer machine",
    * "expiresAt": "2023-05-14T21:49:58.465Z",
    * "status": "active",
    * "type": "temporary",
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56Z",
      * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "modifiedAt": "2021-09-01T12:34:56Z",
      * "version": 1  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/Allowed-CIDRs-%28Cluster%29/operation/getAllowedCidrByID)get allowed CIDR 

Fetches the details for the specified allowed CIDR.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| allowedCidrIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the allowed CIDR. |

### Responses

**200** 

Successfully fetched the allowed CIDR details.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/allowedcidrs/{allowedCidrId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/allowedcidrs/{allowedCidrId}

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "cidr": "1.23.45.67/32",
* "comment": "Allows access from my local developer machine",
* "expiresAt": "2023-05-14T21:49:58.465Z",
* "status": "active",
* "type": "temporary",
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
}
}`

## [](#tag/Allowed-CIDRs-%28Cluster%29/operation/deleteAllowedCidrByID)Delete Allowed CIDR 

Deletes the existing allowed CIDR.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| allowedCidrIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the allowed CIDR. |

### Responses

**204** 

Successfully deleted the allowed CIDR by its ID.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/allowedcidrs/{allowedCidrId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/allowedcidrs/{allowedCidrId}

### Response samples 

* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Api-Keys)Api Keys

Couchbase Capella Management API uses a Bearer token mechanism for authentication; each call to the Management API has to be authenticated by API key.

## [](#tag/Api-Keys/operation/postOrganizationAPIKeys)Create API Key 

Creates a new API key under an organization.

Organization Owners can create Organization and Project scoped API keys.

Project Owner and Project Creator can create project scoped keys.

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| namerequired              | string (APIKeyName) Name of the API key.                                                                                                                                                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| description               | string (APIKeyDescription) Default: "" Description for the API key.                                                                                                                                                                                                       |
| expiry                    | number <float\>  (APIKeyExpiry) Default: 180 Expiry of the API key in number of days. If set to -1, the token will not expire.                                                                                                                                            |
| allowedCIDRs              | Array of strings (APIKeyAllowedCIDRs) Default: \["0.0.0.0/0"\] List of inbound CIDRs for the API key. The system making a request must come from one of the allowed CIDRs.                                                                                                |
| organizationRolesrequired | Array of strings (APIKeyOrganizationRoles) Items Enum: "organizationOwner" "organizationMember" "projectCreator"                                                                                                                                                          |
| resources                 | Array of objects (APIKeyResources) Default: \[\] Resources are the resource level permissions associated with the API key. To learn more about Organization Roles, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html). |

### Responses

**201** 

Successfully created an API key under an organization.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/apikeys

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/apikeys

### Request samples 

* Payload

Content type

application/json

Example

createOrganizationOwnerAPIKeycreateProjectOwnerAPIKeycreateOrganizationOwnerAPIKey

Copy

 Expand all  Collapse all 

`{
* "name": "Organization Owner API Key",
* "description": "Creates an API key with a Organization Owner role.",
* "expiry": 720,
* "allowedCIDRs": [
  * "8.8.8.8/32"  
],
* "organizationRoles": [
  * "organizationOwner"  
],
* "resources": [ ]
}`

### Response samples 

* 201
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "IS9DrRsw4KWFS72Zhbj4xmhllHvPcdCL",
* "token": "QktxVUtFU1dKV1FlMmxwbzJBYXdnTVlRemFZdlRDZTg6eFh4dzU4JUYjekJVYWZPY3lqdUwwYkJoTjZSTmlzRWFIRHF0b1h4a08yazBpQjJ1bms1OW4yTUhAenRib3IhVQ=="
}`

## [](#tag/Api-Keys/operation/listOrganizationAPIKeys)List API keys 

Lists all the API keys under an organization.

Organization Owners can list all the API keys inside the Organization.

Organization Members and Project Creators can list all the Project scoped API key for which they are Project Owner.

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                                     |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                           |
| sortBy        | Array of strings Example: sortBy=name Sets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **name**, **createdAt**, **expiry**. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                                  |

### Responses

**200** 

Successfully listed all the apikeys under an organization.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/apikeys

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/apikeys

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "IS9DrRsw4KWFS72Zhbj4xmhllHvPcdCL",
    * "name": "Production",
    * "description": "API key to manage production Capella Cluster.",
    * "expiry": 180,
    * "allowedCIDRs": [
      * "0.0.0.0/0"  
      ],
    * "organizationRoles": [
      * "organizationMember"  
      ],
    * "resources": [ ],
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56Z",
      * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "modifiedAt": "2021-09-01T12:34:56Z",
      * "version": 1  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/Api-Keys/operation/getOrganizationAPIKeyByAccessKey)Get API Key 

Fetches the details of the given API key under an organization.

Organization Owners can get any API key inside the Organization.

Organization Members and Project Creator can get any Project scoped API key for which they are Project Owner.

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| ApiKeyIdrequired       | string Example: ffffffffaaaa1414eeee000000000000The ID (Access key) of the API key.           |

### Responses

**200** 

Successfully fetched the API key by its Access key.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/apikeys/{ApiKeyId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/apikeys/{ApiKeyId}

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "IS9DrRsw4KWFS72Zhbj4xmhllHvPcdCL",
* "name": "Organization Owner API Key",
* "description": "Creates an API key with an Organization Owner role.",
* "expiry": 720,
* "allowedCIDRs": [
  * "8.8.8.8/32"  
],
* "organizationRoles": [
  * "organizationOwner"  
],
* "resources": [ ],
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
}
}`

## [](#tag/Api-Keys/operation/deleteOrganizationAPIKey)Delete API Key 

Deletes the given API key under an organization.

Organization Owners can delete any API key inside the Organization.

Organization Members and Project Creator can delete any Project scoped API key for which they are Project Owner.

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| ApiKeyIdrequired       | string Example: ffffffffaaaa1414eeee000000000000The ID (Access key) of the API key.           |

### Responses

**204** 

Successfully deleted the API key by its Access key.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/apikeys/{ApiKeyId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/apikeys/{ApiKeyId}

### Response samples 

* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Api-Keys/operation/postOrganizationAPIKeyRotate)Rotate API Key 

Rotate the secret of a given API key under an organization.

Organization Owners can rotate any API key inside the Organization.

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| ApiKeyIdrequired       | string Example: ffffffffaaaa1414eeee000000000000The ID (Access key) of the API key.           |

##### Request Body schema: application/json

| secret | string A secret associated with API key. One has to follow the secret key policy, such as allowed characters and a length of 64 characters. If this field is left empty, a secret will be auto-generated. |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**200** 

Successfully rotated the API key.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/apikeys/{ApiKeyId}/rotate

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/apikeys/{ApiKeyId}/rotate

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "secret": "<YOUR_SECRET_KEY_HERE>"
}`

### Response samples 

* 200
* 403
* 404
* 422
* 500

Content type

application/json

Copy

`{
* "secretKey": "<YOUR_SECRET_KEY_HERE>",
* "token": "<YOUR_TOKEN_HERE>"
}`

## [](#tag/App-Endpoints)App Endpoints

App Endpoints represent instances of mobile applications on App Services. Each App Endpoint is linked to one bucket and synchronizes data to a set of linked collections. Users can configure App Endpoints, including setting the Access Control function, Import Filter and OpenID Connect (OIDC) authentication configuration.

## [](#tag/App-Endpoints/operation/listAppEndpoints)List App Endpoints 

Lists all the App Endpoints under a specific App Service along with their associated configurations such as Access Control function, Import Filter or user defined xattr key.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                         |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                                |
| sortBy        | Array of strings Example: sortBy=name Sets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **name**, **offline**, **bucket**. |

### Responses

**200** 

Successfully listed all the App Endpoints under a specific App Service.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500
* 503

Content type

application/json

Example

ListAppEndpointsDefaultCollListAppEndpointNamedCollListAppEndpointsDefaultColl

Copy

 Expand all  Collapse all 

`{
* "data": {
  * "bucket": "bucket1",
  * "name": "defaultAppEndpoint",
  * "userXattrKey": "key",
  * "disablePublicAllDocs": false,
  * "deltaSyncEnabled": true,
  * "oidc": [
    * {
      * "issuer": "<https://example.auth.com>",
      * "register": true,
      * "clientId": "foo_client",
      * "userPrefix": "fooOIDC",
      * "discoveryUrl": "<https://foo.com/.well-known/openid-configuration>",
      * "usernameClaim": "fooAlt",
      * "rolesClaim": "roles",
      * "providerId": "ffffffff-aaaa-1414-eeee-000000000000",
      * "isDefault": true  
      },
    * {
      * "issuer": "<https://example.auth.com>",
      * "register": true,
      * "clientId": "bar_client",
      * "userPrefix": "barOIDC",
      * "discoveryUrl": "<https://bar.com/.well-known/openid-configuration>",
      * "usernameClaim": "barAlt",
      * "providerId": "ffffffff-aaaa-1414-eeee-000000000000",
      * "isDefault": false  
      }  
  ],
  * "cors": {
    * "origin": [
      * "<http://example.com>",
      * "<http://staging.example.com>"  
      ],
    * "loginOrigin": [
      * "<http://example.com>"  
      ],
    * "headers": [
      * "Content-Type",
      * "X-Forwarded-Host"  
      ],
    * "disabled": false,
    * "maxAge": 120  
  },
  * "scopes": {
    * "_default": {
      * "collections": {
        * "_default": {
          * "accessControlFunction": "function(doc){channel(doc.channels);}",
          * "importFilter": "function(doc) { if (doc.type != 'mobile') { return false; } return true; }"  
                    }  
            }  
      }  
  },
  * "requireResync": {
    * "_default": {
      * "items": [ ]  
      }  
  },
  * "adminURL": "<https://wdltntbkyuqpaaco.apps.sandbox.project1.com:4985>",
  * "metricsURL": "<https://wdltntbkyuqpaaco.apps.sandbox.project1.com:4986>",
  * "publicURL": "<https://wdltntbkyuqpaaco.apps.sandbox.project1.com:4984>"  
},
* "cursor": {
  * "hrefs": { },
  * "pages": {
    * "last": 1,
    * "page": 1,
    * "perPage": 5,
    * "totalItems": 5  
  }  
}
}`

## [](#tag/App-Endpoints/operation/postAppEndpoint)Create App Endpoint 

Creates an App Endpoint within an App Service with specific configurations such as collection level Access Control function and Import Filter. If the scopes property is not included in the request body, the default scope and collection will be used. The first OpenID Connect provider given will be set as the default provider for the App Endpoint. To change the default, please use the Change App Endpoint OIDC Default Provider endpoint.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

##### Request Body schema: application/json

| bucketrequired       | string The Capella Cluster backing bucket for the App Endpoint.                                                                                                                                                                           |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| oidc                 | Array of objects (OIDCProvider) OpenID Connect provider configuration.                                                                                                                                                                    |
| cors                 | object (CORSConfig)                                                                                                                                                                                                                       |
| scopes               | object (ScopesConfig) Default: {"\_default":{"collections":{"\_default":{"accessControlFunction":"function(doc){channel(doc.channels);}","importFilter":" function(doc) { if (doc.type != 'mobile') { return false; } return true; }"}}}} |
| namerequired         | string App Endpoint name. Must be less than 228 characters. It can only contain lowercase letters, numbers, or the following characters \-\_$+()                                                                                          |
| deltaSyncEnabled     | boolean Default: false Enable/disable delta sync                                                                                                                                                                                          |
| userXattrKey         | string The key of the user-extended attributes (xattr) that will be accessible from the Access control and validation function. If left empty, the feature will be disabled.                                                              |
| disablePublicAllDocs | boolean Default: false Disable the \_all\_docs endpoint for this App Endpoint on the App Services Public API.                                                                                                                             |

### Responses

**201** 

Successfully created an App Endpoint.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints

### Request samples 

* Payload

Content type

application/json

Example

CreateAppEndpointRequestDefaultCollectionCreateAppEndpointRequestNamedCollectionsCreateAppEndpointRequestDefaultCollection

Copy

 Expand all  Collapse all 

`{
* "bucket": "bucket1",
* "name": "defaultAppEndpoint",
* "userXattrKey": "key",
* "disablePublicAllDocs": false,
* "deltaSyncEnabled": true,
* "scopes": {
  * "_default": {
    * "collections": {
      * "_default": {
        * "accessControlFunction": "function(doc){channel(doc.channels);}",
        * "importFilter": "function(doc) { if (doc.type != 'mobile') { return false; } return true; }"  
            }  
      }  
  }  
},
* "cors": {
  * "origin": [
    * "<http://example.com>",
    * "<http://staging.example.com>"  
  ],
  * "loginOrigin": [
    * "<http://example.com>"  
  ],
  * "headers": [
    * "Content-Type"  
  ],
  * "disabled": true  
},
* "oidc": [
  * {
    * "issuer": "<https://example.auth.com>",
    * "register": true,
    * "clientId": "foo_client",
    * "userPrefix": "fooOIDC",
    * "discoveryUrl": "<https://foo.com/.well-known/openid-configuration>",
    * "usernameClaim": "fooAlt",
    * "rolesClaim": "roles",
    * "scope": [
      * "openid",
      * "profile",
      * "email"  
      ]  
  },
  * {
    * "issuer": "<https://example.auth.com>",
    * "register": true,
    * "clientId": "bar_client",
    * "userPrefix": "barOIDC",
    * "discoveryUrl": "<https://bar.com/.well-known/openid-configuration>",
    * "usernameClaim": "barAlt"  
  }  
]
}`

### Response samples 

* 400
* 403
* 404
* 409
* 412
* 422
* 429
* 500
* 503

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/App-Endpoints/operation/getAppEndpoint)Get App Endpoint 

Fetches the details of the given App Endpoint, including operational and resync states and various configurations such as Access Control function and Import Filter.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                        |

### Responses

**200** 

Successfully fetched the App Endpoint based on the App Endpoint name.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}

### Response samples 

* 200
* 400
* 403
* 404
* 412
* 422
* 429
* 500
* 503

Content type

application/json

Example

GetAppEndpointDefaultCollectionGetAppEndpointNamedCollectionGetAppEndpointDefaultCollection

Copy

 Expand all  Collapse all 

`{
* "bucket": "bucket1",
* "name": "defaultAppEndpoint",
* "userXattrKey": "key",
* "disablePublicAllDocs": false,
* "deltaSyncEnabled": true,
* "oidc": [
  * {
    * "issuer": "<https://example.auth.com>",
    * "register": true,
    * "clientId": "foo_client",
    * "userPrefix": "fooOIDC",
    * "discoveryUrl": "<https://foo.com/.well-known/openid-configuration>",
    * "usernameClaim": "fooAlt",
    * "rolesClaim": "roles",
    * "providerId": "ffffffff-aaaa-1414-eeee-000000000000",
    * "isDefault": true  
  }  
],
* "cors": {
  * "origin": [
    * "<http://example.com>",
    * "<http://staging.example.com>"  
  ],
  * "loginOrigin": [
    * "<http://example.com>"  
  ],
  * "headers": [
    * "Content-Type"  
  ],
  * "maxAge": 600,
  * "disabled": false  
},
* "scopes": {
  * "_default": {
    * "collections": {
      * "_default": {
        * "accessControlFunction": "function(doc){channel(doc.channels);}",
        * "importFilter": "function(doc) { if (doc.type != 'mobile') { return false; } return true; }"  
            }  
      }  
  }  
},
* "requireResync": {
  * "_default": {
    * "items": [ ]  
  }  
},
* "adminURL": "<https://wdltntbkyuqpaaco.apps.sandbox.project1.com:4985>",
* "metricsURL": "<https://wdltntbkyuqpaaco.apps.sandbox.project1.com:4986>",
* "publicURL": "<https://wdltntbkyuqpaaco.apps.sandbox.project1.com:4984>"
}`

## [](#tag/App-Endpoints/operation/putAppEndpoint)Update App Endpoint 

Replaces a specified App Endpoint's configurations such as Access Control function, Import Filter, Delta Sync, or user defined xattr key. The first OpenID Connect provider given will be set as the default provider for the App Endpoint. To change the default, please use the Change App Endpoint OIDC Default Provider endpoint. All fields are required, the App Endpoint and bucket names cannot be changed.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                        |

##### Request Body schema: application/json

| namerequired                 | string App Endpoint name. Cannot be changed.                                                                                                                                                                                              |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bucketrequired               | string The Capella Cluster backing bucket for the App Endpoint. Cannot be changed.                                                                                                                                                        |
| scopesrequired               | object (ScopesConfig) Default: {"\_default":{"collections":{"\_default":{"accessControlFunction":"function(doc){channel(doc.channels);}","importFilter":" function(doc) { if (doc.type != 'mobile') { return false; } return true; }"}}}} |
| deltaSyncEnabledrequired     | boolean Enable or disable delta sync                                                                                                                                                                                                      |
| userXattrKeyrequired         | string Key of user xattr that will be accessible from the Access control and validation function. If empty, the feature will be disabled.                                                                                                 |
| disablePublicAllDocsrequired | boolean Default: false Disable the \_all\_docs endpoint for this App Endpoint on the App Services Public API.                                                                                                                             |
| oidcrequired                 | Array of objects (OIDCProvider) OpenID Connect provider configuration.                                                                                                                                                                    |
| corsrequired                 | object (CORSConfig)                                                                                                                                                                                                                       |

### Responses

**204** 

Successfully updated the App Endpoint metadata.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "name": "appEndpoint1",
* "bucket": "store_locations",
* "scopes": {
  * "scope_1": {
    * "collections": {
      * "collection_1": {
        * "accessControlFunction": "function(doc){channel(doc.channels);}",
        * "importFilter": "function(doc) { if (doc.type != 'mobile') { return false; } return true; }"  
            },
      * "collection_2": {
        * "accessControlFunction": "function(doc){channel(doc.channels);}",
        * "importFilter": "function(doc) { if (doc.type != 'mobile') { return false; } return true; }"  
            }  
      }  
  }  
},
* "deltaSyncEnabled": true,
* "userXattrKey": "syncFnXattr",
* "disablePublicAllDocs": false,
* "oidc": [
  * {
    * "issuer": "<https://foo.com>",
    * "register": true,
    * "clientId": "foo_client",
    * "userPrefix": "fooOIDC",
    * "discoveryUrl": "<https://foo.com/.well-known/openid-configuration>",
    * "usernameClaim": "fooAlt",
    * "scope": [
      * "openid",
      * "foo"  
      ]  
  }  
],
* "cors": {
  * "origin": [
    * "<http://example.com>",
    * "<http://staging.example.com>"  
  ],
  * "loginOrigin": [
    * "<http://example.com>"  
  ],
  * "headers": [
    * "Content-Type"  
  ],
  * "maxAge": 600,
  * "disabled": false  
}
}`

### Response samples 

* 400
* 403
* 404
* 409
* 422
* 429
* 500
* 503

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/App-Endpoints/operation/deleteAppEndpoint)Delete App Endpoint 

Deletes an existing App Endpoint given its name.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                        |

### Responses

**202** 

Successfully deleted the App Endpoint by its App Endpoint name.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500
* 503

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/App-Endpoints/operation/listAppEndpointCollections)List App Endpoint Collections 

Lists all the collections under a specific App Endpoint along with their associated configurations such as Access Control function, Import Filter or user defined xattr key.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                        |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                    |
| ------------- | ------------------------------------------------------------------------------------------------ |
| perPage       | integer Sets the number of results you would like to have on each page.                          |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted. |

### Responses

**200** 

Successfully listed all the collections under a specific App Endpoint.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/collections

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/collections

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500
* 503

Content type

application/json

Example

ListAppEndpointCollectionsDefaultCollListAppEndpointCollectionsNamedCollListAppEndpointCollectionsDefaultNamedCollListAppEndpointCollectionsDefaultColl

Copy

 Expand all  Collapse all 

`{
* "scopes": {
  * "_default": {
    * "collections": {
      * "_default": {
        * "accessControlFunction": "function(doc){channel(doc.channels);}",
        * "importFilter": "function(doc) { if (doc.type != 'mobile') { return false; } return true; }"  
            }  
      }  
  }  
}
}`

## [](#tag/App-Endpoints/operation/postAppEndpointActivationStatus)Resume or Bring an App Endpoint online 

Brings an App Endpoint online to close and reopen the connection to the backing Cluster bucket, re-establish access from the Public REST API and accept all incoming Admin API requests.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                        |

### Responses

**202** 

Accepted request to resume App Endpoint.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**412** 

Returned when there is a mismatch with the Etag version.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/activationStatus

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/activationStatus

### Response samples 

* 403
* 404
* 409
* 412
* 429
* 500
* 503

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/App-Endpoints/operation/deleteAppEndpointActivationStatus)Pause or Take an App Endpoint offline 

Take the database offline to run resync or to make changes without disrupting current App Endpoint operations. Clients currently connected to the App Endpoint will not be able to sync data with the Cluster while the App Endpoint is paused. This will not take the backing Cluster bucket offline. Pausing an App Endpoint that is in the progress of coming online will pause the App Endpoint after it comes online.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                        |

### Responses

**202** 

Accepted request to pause App Endpoint.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**412** 

Returned when there is a mismatch with the Etag version.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/activationStatus

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/activationStatus

### Response samples 

* 403
* 404
* 409
* 412
* 429
* 500
* 503

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/App-Endpoints/operation/getAppEndpointCORS)Get the App Endpoint Cross-Origin Resource Sharing (CORS) Configuration. 

Fetch the App Endpoint Cross-Origin Resource Sharing (CORS) Configuration. CORS is disabled by default. For more information See [Cross-Origin Resource Sharing (CORS) on App Endpoints.](https://docs.couchbase.com/cloud/app-services/deployment/cors-configuration-for-app-services.html)

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                        |

### Responses

**200** 

Successfully fetched the App Endpoint CORS config.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

**504** 

The server did not get a response in time from the upstream server in order to complete the request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/cors

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/cors

### Response samples 

* 200
* 403
* 404
* 429
* 500
* 503
* 504

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "origin": [
  * "<http://example.com>",
  * "<http://staging.example.com>"  
],
* "loginOrigin": [
  * "<http://example.com>"  
],
* "headers": [
  * "Content-Type"  
],
* "maxAge": 600,
* "disabled": false
}`

## [](#tag/App-Endpoints/operation/putAppEndpointCORS)Upsert the App Endpoint Cross-Origin Resource Sharing (CORS) Configuration. 

Upsert the App Endpoint Cross-Origin Resource Sharing (CORS) Configuration. CORS is disabled by default. For more information See [Cross-Origin Resource Sharing (CORS) on App Endpoints.](https://docs.couchbase.com/cloud/app-services/deployment/cors-configuration-for-app-services.html)

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                        |

##### Request Body schema: application/json

| originrequired | Array of strings List of allowed origins, use \['\*'\] to allow access from everywhere. This is required when CORS is enabled (i.e. disabled is false). |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| loginOrigin    | Array of strings List of allowed login origins                                                                                                          |
| headers        | Array of strings List of allowed headers                                                                                                                |
| maxAge         | integer Default: 5 Specifies the duration (in seconds) for which the results of a preflight request can be cached.                                      |
| disabled       | boolean Disable CORS headers in all App Endpoint responses. When true, no other CORS configuration properties should be provided.                       |

### Responses

**204** 

Succesfully upserted App Endpoint CORS config.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

**504** 

The server did not get a response in time from the upstream server in order to complete the request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/cors

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/cors

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "origin": [
  * "<http://example.com>",
  * "<http://staging.example.com>"  
],
* "loginOrigin": [
  * "<http://example.com>"  
],
* "headers": [
  * "Content-Type"  
],
* "maxAge": 600,
* "disabled": false
}`

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500
* 503
* 504

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/App-Endpoints/operation/getAccessFunction)Get Access Control and Validation function 

Retrieves the Access Control and Validation function for the given keyspace.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| projectIdrequired           | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| clusterIdrequired           | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| appServiceIdrequired        | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| appEndpointKeyspacerequired | string Example: endpoint1.scope1.collection1A specific collection denoted by the App Endpoint name, the scope name and collection name separated by a period, for example "endpoint1.scope1.collection1". If only an App Endpoint name is provided this will be interpreted as "endpoint1.\_default.\_default". If only an App Endpoint name and collection name are provided these will interpreted as a named collection within the default scope, for example "endpoint1.collection1" will be interpreted as "endpoint1.\_default.collection1". |

### Responses

**200** 

Successfully retrieved the Access control and validation function.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointKeyspace}/accessControlFunction

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointKeyspace}/accessControlFunction

### Response samples 

* 400
* 403
* 404
* 412
* 422
* 429
* 500
* 503

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/App-Endpoints/operation/putAccessFunction)Upsert custom Access Control and Validation function 

Used to upsert a custom Access Control and Validation function for the given keyspace. This is a Javascript function specified at a keyspace, where a user's read/write access is defined for documents in that particular keyspace. Every document mutation is processed by this function. If an Access Control function is not explicitly defined, a default is applied. [Read more.](https://docs.couchbase.com/cloud/app-services/deployment/access-control-data-validation.html?)

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| projectIdrequired           | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| clusterIdrequired           | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| appServiceIdrequired        | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| appEndpointKeyspacerequired | string Example: endpoint1.scope1.collection1A specific collection denoted by the App Endpoint name, the scope name and collection name separated by a period, for example "endpoint1.scope1.collection1". If only an App Endpoint name is provided this will be interpreted as "endpoint1.\_default.\_default". If only an App Endpoint name and collection name are provided these will interpreted as a named collection within the default scope, for example "endpoint1.collection1" will be interpreted as "endpoint1.\_default.collection1". |

##### Request Body schema: application/javascript

string (AccessFunction) 

All mutations in this collection are processed by this Javascript function

### Responses

**204** 

Successfully upserted the Access control and validation function .

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointKeyspace}/accessControlFunction

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointKeyspace}/accessControlFunction

### Response samples 

* 400
* 403
* 404
* 409
* 412
* 422
* 429
* 500
* 503

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/App-Endpoints/operation/deleteAccessFunction)Delete Access Control and Validation function 

Deletes the Access Control and Validation function for the given keyspace.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| projectIdrequired           | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| clusterIdrequired           | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| appServiceIdrequired        | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| appEndpointKeyspacerequired | string Example: endpoint1.scope1.collection1A specific collection denoted by the App Endpoint name, the scope name and collection name separated by a period, for example "endpoint1.scope1.collection1". If only an App Endpoint name is provided this will be interpreted as "endpoint1.\_default.\_default". If only an App Endpoint name and collection name are provided these will interpreted as a named collection within the default scope, for example "endpoint1.collection1" will be interpreted as "endpoint1.\_default.collection1". |

### Responses

**202** 

Successfully deleted the Access control and validation function.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointKeyspace}/accessControlFunction

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointKeyspace}/accessControlFunction

### Response samples 

* 400
* 403
* 404
* 409
* 412
* 422
* 429
* 500
* 503

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/App-Endpoints/operation/getImportFilter)Get Import Filter 

Retrieves the Import Filter for the given keyspace.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| projectIdrequired           | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| clusterIdrequired           | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| appServiceIdrequired        | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| appEndpointKeyspacerequired | string Example: endpoint1.scope1.collection1A specific collection denoted by the App Endpoint name, the scope name and collection name separated by a period, for example "endpoint1.scope1.collection1". If only an App Endpoint name is provided this will be interpreted as "endpoint1.\_default.\_default". If only an App Endpoint name and collection name are provided these will interpreted as a named collection within the default scope, for example "endpoint1.collection1" will be interpreted as "endpoint1.\_default.collection1". |

### Responses

**200** 

Successfully retrieved the Import Filter.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointKeyspace}/importFilter

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointKeyspace}/importFilter

### Response samples 

* 403
* 404
* 412
* 422
* 429
* 500
* 503

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/App-Endpoints/operation/putImportFilter)Upsert Import Filter 

Upserts the Import Filter for the given keyspace. By default, there is no import filter and all documents are imported. Import Filters identify the subset of documents eligible to be replicated by App services based on user-defined requirements. This subset is applied to all future mutations. Once the document has been imported and processed by the App Endpoint, changing the Import Filter will not remove it, even if the updated import filters would prevent newer mutations or iterations of the document from getting imported. [Read more.](https://docs.couchbase.com/cloud/app-services/deployment/import-filters.html)

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| projectIdrequired           | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| clusterIdrequired           | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| appServiceIdrequired        | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| appEndpointKeyspacerequired | string Example: endpoint1.scope1.collection1A specific collection denoted by the App Endpoint name, the scope name and collection name separated by a period, for example "endpoint1.scope1.collection1". If only an App Endpoint name is provided this will be interpreted as "endpoint1.\_default.\_default". If only an App Endpoint name and collection name are provided these will interpreted as a named collection within the default scope, for example "endpoint1.collection1" will be interpreted as "endpoint1.\_default.collection1". |

##### Request Body schema: application/javascript

string (ImportFilter) 

The Javascript function used to specify the documents in this collection that are to be imported by the App Endpoint. By default, all documents in corresponding collection are imported.

### Responses

**204** 

Successfully upserted the Import Filter .

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointKeyspace}/importFilter

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointKeyspace}/importFilter

### Response samples 

* 400
* 403
* 404
* 409
* 412
* 422
* 429
* 500
* 503

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/App-Endpoints/operation/deleteImportFilter)Delete Import Filter 

Deletes the Import Filter for the given keyspace.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| projectIdrequired           | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| clusterIdrequired           | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| appServiceIdrequired        | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| appEndpointKeyspacerequired | string Example: endpoint1.scope1.collection1A specific collection denoted by the App Endpoint name, the scope name and collection name separated by a period, for example "endpoint1.scope1.collection1". If only an App Endpoint name is provided this will be interpreted as "endpoint1.\_default.\_default". If only an App Endpoint name and collection name are provided these will interpreted as a named collection within the default scope, for example "endpoint1.collection1" will be interpreted as "endpoint1.\_default.collection1". |

### Responses

**202** 

Successfully deleted the Import Filter.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointKeyspace}/importFilter

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointKeyspace}/importFilter

### Response samples 

* 403
* 404
* 409
* 412
* 422
* 429
* 500
* 503

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/App-Endpoints/operation/createAppEndpointOIDCProvider)Create App Endpoint OpenID Connect (OIDC) Provider 

Creates an OIDC provider for the specified App Endpoint. The first OIDC provider will automatically be set as the default OIDC provider. All client requests will use the default OIDC provider, unless the OIDC provider for the request is explicitly specified on authentication. See more [here](https://docs.couchbase.com/cloud/app-services/user-management/set-up-authentication-provider.html#oidc-authorization-step-by-step).

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                        |

##### Request Body schema: application/json

| issuerrequired   | string The URL for the OpenID Connect issuer.                                                                                                                                                                                                           |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| register         | boolean Indicates whether to register a new App Service user account when a user logs in using OpenID Connect.                                                                                                                                          |
| clientIdrequired | string The OpenID Connect provider client ID.                                                                                                                                                                                                           |
| userPrefix       | string Username prefix for all users created for this provider                                                                                                                                                                                          |
| discoveryUrl     | string The URL for the non-standard discovery endpoint.                                                                                                                                                                                                 |
| usernameClaim    | string Allows a different OpenID Connect field to be specified instead of the Subject (sub).                                                                                                                                                            |
| rolesClaim       | string If set, the value(s) of the given OpenID Connect authentication token claim will be added to the user's roles. The value of this claim in the OIDC token must be either a string or an array of strings, any other type will result in an error. |
| scope            | Array of strings Default: \["openid","email"\] The scope sent for the OpenID Connect request.                                                                                                                                                           |

### Responses

**201** 

Successfully created OIDC Provider.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

**504** 

The server did not get a response in time from the upstream server in order to complete the request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/oidcProviders

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/oidcProviders

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "issuer": "<https://foo.com>",
* "register": true,
* "clientId": "foo_client",
* "userPrefix": "fooOIDC",
* "discoveryUrl": "<https://foo.com/.well-known/openid-configuration>",
* "usernameClaim": "fooAlt"
}`

### Response samples 

* 201
* 400
* 403
* 404
* 409
* 422
* 429
* 500
* 503
* 504

Content type

application/json

Copy

`{
* "providerId": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/App-Endpoints/operation/listAppEndpointOIDCProviders)List App Endpoint OpenID Connect (OIDC) Providers 

List OpenID Connect (OIDC) Providers configured on an App Endpoint.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                        |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                    |
| ------------- | ------------------------------------------------------------------------------------------------ |
| perPage       | integer Sets the number of results you would like to have on each page.                          |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted. |

### Responses

**200** 

Successfully fetched OIDC Providers.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

**504** 

The server did not get a response in time from the upstream server in order to complete the request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/oidcProviders

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/oidcProviders

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500
* 503
* 504

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "issuer": "<https://example.auth.com>",
    * "register": true,
    * "clientId": "foo_client",
    * "userPrefix": "fooOIDC",
    * "discoveryUrl": "<https://foo.com/.well-known/openid-configuration>",
    * "usernameClaim": "fooAlt",
    * "rolesClaim": "roles",
    * "providerId": "ffffffff-aaaa-1414-eeee-000000000000",
    * "isDefault": true  
  },
  * {
    * "issuer": "<https://example.auth.com>",
    * "register": true,
    * "clientId": "bar_client",
    * "userPrefix": "barOIDC",
    * "discoveryUrl": "<https://bar.com/.well-known/openid-configuration>",
    * "usernameClaim": "barAlt",
    * "providerId": "ffffffff-aaaa-1414-eeee-000000000000",
    * "isDefault": false  
  }  
]
}`

## [](#tag/App-Endpoints/operation/getAppEndpointOIDCProvider)Get App Endpoint OpenID Connect (OIDC) Provider 

Fetches an OIDC provider by ID for the specified App Endpoint.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ----------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.              |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                                   |
| OIDCProviderIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the OpenID Connect Provider. |

### Responses

**200** 

Successfully fetched the OIDC Provider.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

**504** 

The server did not get a response in time from the upstream server in order to complete the request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/oidcProviders/{OIDCProviderId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/oidcProviders/{OIDCProviderId}

### Response samples 

* 200
* 403
* 404
* 429
* 500
* 503
* 504

Content type

application/json

Copy

`{
* "issuer": "foo",
* "register": true,
* "clientId": "foo_client",
* "userPrefix": "fooOIDC",
* "discoveryUrl": "<https://foo.com/.well-known/openid-configuration>",
* "usernameClaim": "fooAlt",
* "isDefault": true
}`

## [](#tag/App-Endpoints/operation/updateAppEndpointOIDCProvider)Update App Endpoint OpenID Connect (OIDC) Provider 

Updates an OIDC provider for the specified App Endpoint.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ----------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.              |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                                   |
| OIDCProviderIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the OpenID Connect Provider. |

##### Request Body schema: application/json

| issuerrequired   | string The URL for the OpenID Connect issuer.                                                                                                                                                                                                           |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| register         | boolean Indicates whether to register a new App Service user account when a user logs in using OpenID Connect.                                                                                                                                          |
| clientIdrequired | string The OpenID Connect provider client ID.                                                                                                                                                                                                           |
| userPrefix       | string Username prefix for all users created for this provider                                                                                                                                                                                          |
| discoveryUrl     | string The URL for the non-standard discovery endpoint.                                                                                                                                                                                                 |
| usernameClaim    | string Allows a different OpenID Connect field to be specified instead of the Subject (sub).                                                                                                                                                            |
| rolesClaim       | string If set, the value(s) of the given OpenID Connect authentication token claim will be added to the user's roles. The value of this claim in the OIDC token must be either a string or an array of strings, any other type will result in an error. |
| scope            | Array of strings Default: \["openid","email"\] The scope sent for the OpenID Connect request.                                                                                                                                                           |

### Responses

**204** 

Successfully updated the App Endpoint OIDC provider based on the OIDCProviderId.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

**504** 

The server did not get a response in time from the upstream server in order to complete the request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/oidcProviders/{OIDCProviderId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/oidcProviders/{OIDCProviderId}

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "issuer": "<https://foo.com>",
* "register": true,
* "clientId": "foo_client",
* "userPrefix": "fooOIDC",
* "discoveryUrl": "<https://foo.com/.well-known/openid-configuration>",
* "usernameClaim": "fooAlt"
}`

### Response samples 

* 400
* 403
* 404
* 409
* 422
* 429
* 500
* 503
* 504

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/App-Endpoints/operation/deleteAppEndpointOIDCProvider)Delete App Endpoint OpenID Connect (OIDC) Provider 

Deletes an OIDC provider for the specified App Endpoint. Deleting the default provider will error unless it is the only provider. Before deleting the default provider, you must set a new provider as default or have no other providers.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ----------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.              |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                                   |
| OIDCProviderIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the OpenID Connect Provider. |

### Responses

**202** 

Successfully deleted the OIDC Provider.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

**504** 

The server did not get a response in time from the upstream server in order to complete the request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/oidcProviders/{OIDCProviderId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/oidcProviders/{OIDCProviderId}

### Response samples 

* 400
* 403
* 404
* 409
* 429
* 500
* 503
* 504

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/App-Endpoints/operation/updateAppEndpointOIDCDefaultProvider)Update App Endpoint Default OIDC Provider 

Updates the default OIDC provider for the specified App Endpoint. All client requests will use the default OIDC provider, unless the OIDC provider for the request is explicitly specified. See more [here](https://docs.couchbase.com/cloud/app-services/user-management/set-up-authentication-provider.html#oidc-authorization-step-by-step).

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                        |

##### Request Body schema: application/json

| providerIdrequired | string |
| ------------------ | ------ |

### Responses

**204** 

Successfully updated the default OIDC provider.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

**504** 

The server did not get a response in time from the upstream server in order to complete the request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/oidcProviders/defaultProvider

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/oidcProviders/defaultProvider

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "providerId": "ffffffff-aaaa-1414-eeee-000000000000"
}`

### Response samples 

* 400
* 403
* 404
* 409
* 422
* 429
* 500
* 503
* 504

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/App-Endpoints/operation/getAppEndpointResync)Get Resync Status 

Fetches the Resync status of the given App Endpoint. If no resync operation was triggered, the response will say the status is completed with 0 values for other properties.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                        |

### Responses

**200** 

Successfully fetched the App Endpoint Resync status based on the App Endpoint name.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

**504** 

The server did not get a response in time from the upstream server in order to complete the request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/resync

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/resync

### Response samples 

* 200
* 403
* 404
* 412
* 422
* 429
* 500
* 503
* 504

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "state": "running",
* "startTime": "2023-10-12T07:20:50.52Z",
* "lastError": "string",
* "docsChanged": 100,
* "docsProcessed": 500,
* "collections_processing": {
  * "scope1": [
    * "collection_1",
    * "collection_2"  
  ]  
}
}`

## [](#tag/App-Endpoints/operation/postAppEndpointResync)Start Resync 

Initialises the Resync operation for the given collections. By default, all collections that require resync will be resynced unless they are specified in the scopes property, in which case only the specified collections that require resync will be resynced.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                        |

##### Request Body schema: application/json

| scopes | object |
| ------ | ------ |

### Responses

**202** 

The request to start the resync operation has been accepted.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

**504** 

The server did not get a response in time from the upstream server in order to complete the request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/resync

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/resync

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "scopes": {
  * "scope1": [
    * "collection1",
    * "collection2"  
  ]  
}
}`

### Response samples 

* 400
* 403
* 404
* 412
* 422
* 429
* 500
* 503
* 504

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/App-Endpoints/operation/deleteAppEndpointResync)Stop Resync 

Stops the Resync operation. When stopping resync, it will be stopped for all collections being processed. In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                        |

### Responses

**202** 

The request to stop the resync operation has been accepted.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

**504** 

The server did not get a response in time from the upstream server in order to complete the request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/resync

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/resync

### Response samples 

* 400
* 403
* 404
* 412
* 422
* 429
* 500
* 503
* 504

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/App-Services)App Services

App Services is a fully managed application backend designed to provide data synchronization between mobile or IoT applications running Couchbase Lite and your Couchbase Capella database.

## [](#tag/App-Services/operation/postAppService)Create App Service 

Creates a new App Service.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| namerequired | string <= 256 characters Name of the cluster (up to 256 characters).                                                                                       |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| description  | string A short description of the App Service.                                                                                                             |
| nodes        | integer Number of nodes configured for the App Service. Number of nodes configured for the App Service. The number of nodes can range from 2 to 12.        |
| compute      | object (AppServiceCompute) The CPU and RAM configuration of the App Service. The supported combinations are: CPU (cores) RAM (GB) 2 4 4 8 8 16 16 32 36 72 |
| version      | string The version of the App Service server. If left empty, it will be defaulted to the latest available version.                                         |

### Responses

**201** 

Successfully created an App Service.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "name": "MyAppSyncService",
* "description": "My app sync service.",
* "nodes": 2,
* "compute": {
  * "cpu": 2,
  * "ram": 4  
},
* "version": "3.0"
}`

### Response samples 

* 201
* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/App-Services/operation/listAppServices)List AppServices 

Lists all the clusters under the organization.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

Returned set of clusters is reduced to what the caller has access to view. To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                         |
| sortBy        | Array of strings Example: sortBy=name Sets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **name**, **id**, **description**. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                                |
| projectId     | string <uuid\> Example: projectId=ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                                                                                                              |

### Responses

**200** 

Successfully listed appservices matching query.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/appservices

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/appservices

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "name": "My App Service",
    * "description": "Description of the App Service.",
    * "cloudProvider": "aws",
    * "nodes": 2,
    * "compute": {
      * "cpu": 2,
      * "ram": 4  
      },
    * "clusterId": "ffffffff-aaaa-1414-eeee-000000000000",
    * "currentState": "deploying",
    * "version": "3.141.5",
    * "plan": "basic",
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56Z",
      * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "modifiedAt": "2021-09-01T12:34:56Z",
      * "version": 1  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/App-Services/operation/getAppService)Get App Service 

Fetches the details of the given App Service.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

### Responses

**200** 

Successfully fetched the App Service based on the appServiceId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "name": "My App Service",
* "description": "Description of the App Service.",
* "cloudProvider": "aws",
* "nodes": 2,
* "compute": {
  * "cpu": 2,
  * "ram": 4  
},
* "clusterId": "ffffffff-aaaa-1414-eeee-000000000000",
* "currentState": "deploying",
* "version": "3.141.5",
* "plan": "basic",
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
}
}`

## [](#tag/App-Services/operation/putAppService)Update App Service 

Updates an existing App Service.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

##### header Parameters

| If-Match | string Example: 12A precondition header that specifies the entity tag of a resource. |
| -------- | ------------------------------------------------------------------------------------ |

##### Request Body schema: application/json

| nodesrequired   | integer Number of nodes configured for the App Service. The number of nodes can range from 2 to 12.                                                        |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| computerequired | object (AppServiceCompute) The CPU and RAM configuration of the App Service. The supported combinations are: CPU (cores) RAM (GB) 2 4 4 8 8 16 16 32 36 72 |

### Responses

**204** 

Successfully updated the App Service metadata.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "nodes": 2,
* "compute": {
  * "cpu": 2,
  * "ram": 4  
}
}`

### Response samples 

* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/App-Services/operation/deleteAppService)Delete App Service 

Deletes an existing App Service.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

### Responses

**202** 

Successfully deleted the App Service by its appServiceId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}

### Response samples 

* 403
* 404
* 412
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/App-Services/operation/appServiceOn)Turn On App Service 

Turn App Service on. App Services can only be turned on when the linked cluster is turned on and healthy.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

### Responses

**202** 

Successfully switched the App Service to on state.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/activationState

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/activationState

### Response samples 

* 403
* 404
* 409
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/App-Services/operation/appServiceOff)Turn Off App Service 

Turn App Service off.

Turn off an App Service to temporarily deactivate it and reduce its consumption of compute resources. The App Service itself and its related infrastructure will be removed once turned off.

Any private endpoints configured on App Services will remain and will be available when App Service is turned back on. You will continue to incur costs for any private endpoints configured on App Services. If you don't wish to incur these costs, you must explicitly disable private endpoint service and reinstate private endpoints when App Service is turned back on again.

Free tier App Service can only be turned off when the linked free tier cluster is turned off.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

### Responses

**202** 

Successfully switched the App Service to off state.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/activationState

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/activationState

### Response samples 

* 403
* 404
* 409
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/App-Services/operation/AddAppServiceAdminUser)Create App Service Admin User 

Creates an Admin User on the specified App Service. The user can either be granted access to all App Endpoints or to specific App Endpoints by listing them in the `endpoints` field.

Currently, the user will be granted admin access to all App Endpoints in a bucket (that is currently associated with the App Endpoint(s) specified in the endpoints field), including ones that are created in future. An option to grant access to specific App Endpoints in a bucket will be available in the future.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

##### Request Body schema: application/json

| namerequired            | string The name of the user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| passwordrequired        | string The password of the user.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| enableBucketLevelAccess | boolean Default: true When set to true, the user will automatically be granted admin access to all App Endpoints in a bucket (that is currently associated with the App Endpoint(s) specified in the endpoints field), including ones that are created in future. The flag defaults to true. Currently, the only supported value is true, which means that the user will have admin access to all App Endpoints in this bucket. In the future, there will be the option to set this to false. |
| accessrequired          | UpdateAppServiceAdminUserAllEndpointsRequest (object) or UpdateAppServiceAdminUserEndpointList (object)                                                                                                                                                                                                                                                                                                                                                                                       |

### Responses

**201** 

Successfully created an App Service Admin User.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/adminUsers

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/adminUsers

### Request samples 

* Payload

Content type

application/json

Example

CreateAdminUserSpecificEndpointsCreateAdminUserAllEndpointsCreateAdminUserSpecificEndpoints

Copy

 Expand all  Collapse all 

`{
* "name": "user1",
* "password": "password",
* "enableBucketLevelAccess": false,
* "access": {
  * "endpoints": [
    * "endpoint1",
    * "endpoint2"  
  ]  
}
}`

### Response samples 

* 201
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "eeeeeeee-aaaa-1414-eeee-999999999999"
}`

## [](#tag/App-Services/operation/ListAppServiceAdminUsers)List App Service Admin Users 

List the admin users for the specified App Service.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                    |
| ------------- | ------------------------------------------------------------------------------------------------ |
| perPage       | integer Sets the number of results you would like to have on each page.                          |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted. |

### Responses

**200** 

Successfully listed the Admin Users for the specified App Service.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/adminUsers

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/adminUsers

### Response samples 

* 200
* 403
* 404
* 429
* 500
* 503

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "eeeeeeee-aaaa-1414-eeee-999999999999",
    * "tenantId": "ffffffff-aaaa-1414-eeee-000000000000",
    * "projectId": "dddddddd-cccc-1414-eeee-77777777777",
    * "clusterId": "gggggggg-zzzz-1414-eeee-55555555555",
    * "name": "admin",
    * "endpoints": [
      * "appEndpoint1",
      * "appEndpoint2"  
      ],
    * "accessAllEndpoints": "false,",
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2024-09-01T12:34:56Z",
      * "modifiedBy": "",
      * "modifiedAt": "2024-09-01T12:34:56Z",
      * "version": 1  
      }  
  },
  * {
    * "id": "eeeeeeee-gggg-1456-tttt-999999999999",
    * "tenantId": "ffffffff-aaaa-1414-eeee-000000000000",
    * "projectId": "dddddddd-cccc-1414-eeee-77777777777",
    * "clusterId": "gggggggg-zzzz-1414-eeee-55555555555",
    * "name": "admin",
    * "endpoints": [
      * "appEndpoint1",
      * "appEndpoint2"  
      ],
    * "accessAllEndpoints": false,
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2024-09-01T12:34:56Z",
      * "modifiedBy": "",
      * "modifiedAt": "2024-09-01T12:34:56Z",
      * "version": 1  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/App-Services/operation/UpdateAppServiceAdminUser)Update App Service Admin User 

Updates the Admin User's access to App Endpoints on the specified App Service. The update operation can either grant access to all App Endpoints or to specific App Endpoints by listing them in the `endpoints` field.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.        |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.             |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.             |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.          |
| userIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the database credential. |

##### Request Body schema: application/json

One of 

UpdateAppServiceAdminUserEndpointListUpdateAppServiceAdminUserAllEndpointsRequest

| endpointsrequired | Array of strings The list of App Endpoints that the user has access to. |
| ----------------- | ----------------------------------------------------------------------- |

### Responses

**204** 

Successfully updated the App Service Admin User.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/adminUsers/{userId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/adminUsers/{userId}

### Request samples 

* Payload

Content type

application/json

Example

UpdateAdminUserSpecificEndpointsUpdateAdminUserAllEndpointsUpdateAdminUserSpecificEndpoints

Copy

 Expand all  Collapse all 

`{
* "endpoints": [
  * "endpoint1",
  * "endpoint2"  
]
}`

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500
* 503

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/App-Services/operation/DeleteAppServiceAdminUser)Delete App Service Admin User 

Deletes the Admin User.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.        |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.             |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.             |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.          |
| userIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the database credential. |

### Responses

**202** 

Successfully deleted the App Service Admin User.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/adminUsers/{userId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/adminUsers/{userId}

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/App-Services/operation/getAppServiceAdminUser)Get App Service Admin User 

Fetches the Admin User.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.        |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.             |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.             |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.          |
| userIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the database credential. |

### Responses

**200** 

Successfully fetched the App Service Admin User.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/adminUsers/{userId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/adminUsers/{userId}

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500
* 503

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "tenantId": "ffffffff-aaaa-1414-eeee-000000000000",
* "projectId": "ffffffff-aaaa-1414-eeee-000000000000",
* "clusterId": "ffffffff-aaaa-1414-eeee-000000000000",
* "name": "user1",
* "endpoints": [
  * "appEndpoint1",
  * "appEndpoint2"  
],
* "accessAllEndpoints": false,
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
}
}`

## [](#tag/App-Services/operation/putAppServiceMetadataIsolation)Opt App Service Back In to Metadata Isolation 

Opt an App Service back in to system metadata collection (metadata isolation) after a support-initiated opt-out. Only the value `true` is accepted, and opting back in is permanent: once enabled the App Service cannot be opted out again. Requires App Services version 4.1 or later.

New App Services are opted in automatically and existing App Services are opted in on upgrade to 4.1, so this endpoint is only useful after a previous opt-out via Couchbase support.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

##### Request Body schema: application/json

| enabledrequired | boolean Value: true Whether metadata isolation is enabled on the App Service. Only true is accepted via this API to opt back in after support has previously opted the App Service out. Opting back in is permanent: the App Service cannot be opted out again once enabled. |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**204** 

App Service successfully opted back in to metadata isolation.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/metadataIsolation

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/metadataIsolation

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "enabled": true
}`

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/App-Services/operation/getAppServiceMetadataIsolation)Get App Service Metadata Isolation State 

Retrieve the current metadata isolation state for the App Service.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

### Responses

**200** 

Current metadata isolation state.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/metadataIsolation

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/metadataIsolation

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "enabled": true
}`

## [](#tag/App-Services/operation/getAppServiceCertificate)Get Public Certificate for App Service 

The public certificate is a trusted Certificate Authority (CA) signed certificate. You can copy or download the endpoint's SSL public certificate to bundle into your mobile application. Pinning your certificate to your App is not recommended as it can increase maintenance overhead and downtime risks. For more information, see [here](https://docs.couchbase.com/cloud/app-services/connect/connect-apps-to-endpoint.html#setting-up-the-connection).

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

### Responses

**200** 

Successfully fetched the App Service based on the appServiceId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/certificates

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/certificates

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "certificate": "-----BEGIN CERTIFICATE-----\nMIIDFTCCAf2gAwIBAgI[...]CSYBWaK0ofivA==\n-----END CERTIFICATE-----\n"
}`

## [](#tag/App-Services/operation/ListAppEndpointAdminUsers)List App Endpoint Admin Users 

Lists the Admin Users that have access to the specified App Endpoint.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                        |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                    |
| ------------- | ------------------------------------------------------------------------------------------------ |
| perPage       | integer Sets the number of results you would like to have on each page.                          |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted. |

### Responses

**200** 

Successfully listed the Admin Users for the specified App Endpoint.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/adminUsers

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/adminUsers

### Response samples 

* 200
* 403
* 404
* 429
* 500
* 503

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "eeeeeeee-aaaa-1414-eeee-999999999999",
    * "tenantId": "ffffffff-aaaa-1414-eeee-000000000000",
    * "projectId": "dddddddd-cccc-1414-eeee-77777777777",
    * "clusterId": "gggggggg-zzzz-1414-eeee-55555555555",
    * "name": "admin",
    * "endpoints": [
      * "appEndpoint1",
      * "appEndpoint2"  
      ],
    * "accessAllEndpoints": "false,",
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2024-09-01T12:34:56Z",
      * "modifiedBy": "",
      * "modifiedAt": "2024-09-01T12:34:56Z",
      * "version": 1  
      }  
  },
  * {
    * "id": "eeeeeeee-gggg-1456-tttt-999999999999",
    * "tenantId": "ffffffff-aaaa-1414-eeee-000000000000",
    * "projectId": "dddddddd-cccc-1414-eeee-77777777777",
    * "clusterId": "gggggggg-zzzz-1414-eeee-55555555555",
    * "name": "admin",
    * "endpoints": [
      * "appEndpoint1",
      * "appEndpoint2"  
      ],
    * "accessAllEndpoints": false,
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2024-09-01T12:34:56Z",
      * "modifiedBy": "",
      * "modifiedAt": "2024-09-01T12:34:56Z",
      * "version": 1  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/App-Services-Audit-Logging)App Services Audit Logging

Users can configure audit log support on Capella App Services and can export audit logs from cloud blob storage to an AWS S3 bucket. Users can retrieve audit logs from a pre-signed download URL. Logs are retained for 30 days.

## [](#tag/App-Services-Audit-Logging/operation/putAppServiceAuditLogState)Enable or Disable App Service Audit Logging 

Enable or disable Audit Logging for an App Service.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

##### Request Body schema: application/json

| auditEnabledrequired | boolean Determines whether audit logging is enabled or not on the App Service. |
| -------------------- | ------------------------------------------------------------------------------ |

### Responses

**204** 

App service audit logging enabled/disabled successfully.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/auditLog

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/auditLog

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "auditEnabled": true
}`

### Response samples 

* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/App-Services-Audit-Logging/operation/getAppServiceAuditLogState)Get App Service Audit Log State 

Retrieves the audit logging state for a specific App Service.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

### Responses

**200** 

Successful retrieval of audit log settings

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/auditLog

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/auditLog

### Response samples 

* 200
* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "auditEnabled": true
}`

## [](#tag/App-Services-Audit-Logging/operation/getAppServiceAuditLogEvents)List App Endpoint Audit Log Event IDs 

Retrieves all audit log event ids, their descriptions and enabled status for an App Endpoint. The list of filterable event IDs can be specified while configuring audit logging for the App Service.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                        |

### Responses

**200** 

Successful retrieval of audit log events

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/auditLogEvents

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/auditLogEvents

### Response samples 

* 200
* 403
* 404
* 409
* 412
* 422
* 429
* 500
* 503

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "events": {
  * "53290": {
    * "description": "Admin API user successfully authenticated",
    * "enabled": true,
    * "filterable": true,
    * "name": "Admin API user authenticated"  
  },
  * "53292": {
    * "description": "Admin API user failed to authorize",
    * "enabled": true,
    * "filterable": true,
    * "name": "Admin API user authorization failed"  
  }  
}
}`

## [](#tag/App-Services-Audit-Logging/operation/putAppEndpointAuditLogConfig)Update App Endpoint Audit Logging Config 

Updates the audit logging configuration for a specific App Endpoint. Operations performed by disabled users and roles are excluded from audit logs. See a list of event IDs by calling /auditLogEvents, add event IDs to the enabledEventIds field to enable audit logging for those events.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                        |

##### Request Body schema: application/json

| auditEnabled    | boolean Determines whether audit logging is enabled |
| --------------- | --------------------------------------------------- |
| enabledEventIds | Array of objects                                    |
| disabledUsers   | Array of objects (DisabledUserRoles)                |
| disabledRoles   | Array of objects (DisabledUserRoles)                |

### Responses

**204** 

Successful update of audit logging configuration

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/auditLog

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/auditLog

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "auditEnabled": true,
* "enabledEventIds": [
  * {
    * "id": 0  
  }  
],
* "disabledUsers": [
  * {
    * "domain": "string",
    * "name": "string"  
  }  
],
* "disabledRoles": [
  * {
    * "domain": "string",
    * "name": "string"  
  }  
]
}`

### Response samples 

* 400
* 403
* 404
* 412
* 422
* 429
* 500
* 503

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/App-Services-Audit-Logging/operation/getAppEndpointAuditLogConfig)Get App Endpoint Audit Logging Config 

Retrieves the audit logging configuration for a specific App Endpoint.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                        |

### Responses

**200** 

Successful retrieval of audit logging configuration

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/auditLog

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/auditLog

### Response samples 

* 200
* 400
* 403
* 404
* 412
* 422
* 429
* 500
* 503

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "auditEnabled": true,
* "enabledEventIds": [
  * {
    * "id": 0  
  }  
],
* "disabledUsers": [
  * {
    * "domain": "string",
    * "name": "string"  
  }  
],
* "disabledRoles": [
  * {
    * "domain": "string",
    * "name": "string"  
  }  
]
}`

## [](#tag/App-Services-Audit-Logging/operation/putAppServiceAuditLogStreaming)Configure App Service Audit Log Streaming 

Sets up audit log streaming for a specific App Service with filters. If streamingEnabled is true log streaming will begin.

Ensure you have provided collector credentials if you wish to begin streaming; log streaming cannot be enabled without credentials. Refer to schema below to see required fields for your log collection provider. Providers include Datadog, Sumo Logic, Grafana Loki, Elasticsearch (versions 8 and newer only) and generic HTTP. To start or resume streaming, set streamingEnabled to true while providing the rest of the log collector config.

To disable log streaming and remove the log streaming config including credentials, set streamingEnabled to false and leave the rest of the payload empty.

To pause log streaming, set streamingEnabled to false while providing the rest of the log collector config.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

##### Request Body schema: application/json

| streamingEnabledrequired | boolean Determines whether audit log streaming is enabled or not. To start or resume streaming, set this to true. To disable or pause log streaming, set this to false.                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| disabledAppEndpoints     | Array of strings List of App Endpoints to be excluded from audit log streaming.                                                                                                                                                                          |
| outputType               | string Enum: "datadog" "generic\_http" "sumologic" "loki" "elastic" "splunk" "dynatrace" The type of output for the audit log streaming. Required when starting, resuming or pausing log streaming.                                                      |
| credentials              | datadog (object) or sumologic (object) or generic\_http (object) or elastic (object) or loki (object) or splunk (object) or dynatrace (object) Secrets for audit log streaming configuration. Required when starting, resuming or pausing log streaming. |

### Responses

**202** 

Successful Setup of Audit Log Streaming

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/auditLogStreaming

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/auditLogStreaming

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "streamingEnabled": true,
* "disabledAppEndpoints": [
  * "string"  
],
* "outputType": "datadog",
* "credentials": {
  * "apiKey": "apiKey",
  * "url": "<https://http-intake.logs.datadoghq.eu>"  
}
}`

### Response samples 

* 400
* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/App-Services-Audit-Logging/operation/patchAppServiceAuditLogStreaming)Start or Resume Audit Log Streaming 

To start or resume streaming, set streamingEnabled to true. To pause log streaming, set streamingEnabled to false.

If log streaming is paused we will retain the collector credentials. To clear these use the PUT request.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

##### Request Body schema: application/json

| oprequired    | string Value: "update" Type of operation.                         |
| ------------- | ----------------------------------------------------------------- |
| pathrequired  | string Path of resource that needs to be updated.                 |
| valuerequired | boolean Determines whether audit log streaming is enabled or not. |

### Responses

**202** 

Successfully patched Audit Log Streaming config.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

patch/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/auditLogStreaming

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/auditLogStreaming

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "op": "update",
* "path": "/streamingEnabled",
* "value": true
}`

### Response samples 

* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/App-Services-Audit-Logging/operation/getAppServiceAuditLogStreaming)Get App Service Audit Log Streaming State 

Retrieves the current state of audit log streaming for a specific App Service, as well as the output type and enabled App endpoints.

The audit log streaming states are:

* disabled
* disabling
* enabled
* enabling
* paused
* pausing
* errored

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

### Responses

**200** 

Successful retrieval of audit log streaming state

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/auditLogStreaming

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/auditLogStreaming

### Response samples 

* 200
* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "streamingEnabled": true,
* "logStreamingState": "enabling",
* "disabledAppEndpoints": [
  * "string"  
],
* "outputType": "datadog"
}`

## [](#tag/App-Services-Audit-Logging/operation/postAppServiceAuditLogExport)Initiate Audit Log Export 

Initiates an audit log export for a specific App Service.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

##### Request Body schema: application/json

| startrequired | string <date-time\> Specifies the audit log's start date and time. |
| ------------- | ------------------------------------------------------------------ |
| endrequired   | string <date-time\> Specifies the audit log's end date and time.   |

### Responses

**202** 

Successfully created audit export job for the cluster.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/auditLogExports

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/auditLogExports

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "start": "2022-09-04T00:56:07.000Z",
* "end": "2022-09-05T04:56:07.000Z"
}`

### Response samples 

* 202
* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "exportId": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/App-Services-Audit-Logging/operation/listAppServiceAuditLogExports)List Audit Log Export Jobs 

Retrieves a list of all audit log export jobs for an App Service.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                    |
| ------------- | ------------------------------------------------------------------------------------------------ |
| perPage       | integer Sets the number of results you would like to have on each page.                          |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted. |

### Responses

**200** 

Successfully retrieved list of audit export documents

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/auditLogExports

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/auditLogExports

### Response samples 

* 200
* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "920e7b93-28c7-421b-993b-9fffecfd3598",
    * "download_id": "<https://cb-audit-logs-333d2ad2-1408-405e-9995-XXXX.s3.us-east-1.amazonaws.com/export/app-service-audit-logs-XXXX-from-2024-07-06-to-2024-08-05.tar.gz?X-Amz-Algorithm=AWS4-HMAC-SHA256&X>",
    * "download_expires": "2024-08-08T13:43:48.420487299Z",
    * "status": "Ready",
    * "appServiceId": "01071798-23e5-4ec6-b814-13bebef70572",
    * "tenantId": "333d2ad2-1408-405e-9995-68338d20ab5c",
    * "clusterId": "71dd1cb2-34ac-43ae-a503-b2a9202f02d4",
    * "audit": {
      * "createdBy": "d4fa667c-206a-4916-9a24-3a03c2ec5771",
      * "createdAt": "2024-08-05T13:43:45.998790923Z",
      * "modifiedBy": "d4fa667c-206a-4916-9a24-3a03c2ec5771",
      * "modifiedAt": "2024-08-05T13:43:48.420521466Z",
      * "version": 3  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/App-Services-Audit-Logging/operation/getAppServiceAuditLogExportById)Get Audit Log Export Job 

Retrieves details of a specific audit log export job for a given App Service.

 In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.  |
| ------------------------ | ---------------------------------------------------------------------------------------------- |
| projectIdrequired        | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.       |
| clusterIdrequired        | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.       |
| appServiceIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.    |
| auditLogExportIdrequired | string Example: ffffffff-aaaa-1414-eeee-000000000000The export ID of the audit log export job. |

### Responses

**200** 

Successfully retrieved details of audit export job

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/auditLogExports/{auditLogExportId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/auditLogExports/{auditLogExportId}

### Response samples 

* 200
* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "920e7b93-28c7-421b-993b-9fffecfd3598",
* "download_id": "<https://cb-audit-logs-333d2ad2-1408-405e-9995-XXXX.s3.us-east-1.amazonaws.com/export/app-service-audit-logs-XXXX-from-2024-07-06-to-2024-08-05.tar.gz?X-Amz-Algorithm=AWS4-HMAC-SHA256&X>",
* "download_expires": "2024-08-08T13:43:48.420487299Z",
* "status": "Ready",
* "appServiceId": "01071798-23e5-4ec6-b814-13bebef70572",
* "tenantId": "333d2ad2-1408-405e-9995-68338d20ab5c",
* "clusterId": "71dd1cb2-34ac-43ae-a503-b2a9202f02d4",
* "audit": {
  * "createdBy": "d4fa667c-206a-4916-9a24-3a03c2ec5771",
  * "createdAt": "2024-08-05T13:43:45.998790923Z",
  * "modifiedBy": "d4fa667c-206a-4916-9a24-3a03c2ec5771",
  * "modifiedAt": "2024-08-05T13:43:48.420521466Z",
  * "version": 3  
}
}`

## [](#tag/App-Services-Log-Streaming)App Services Log Streaming

Log Streaming provides a mechanism for real-time streaming of App Services operational logs to third-party observability platforms or self-hosted HTTP logs collectors. This is a crucial tool to gain instant insights into application behavior, enabling rapid issue detection and resolution to enhance application reliability, performance, and security.

## [](#tag/App-Services-Log-Streaming/operation/resumeAppServiceLogStreaming)Resume App Service Log Streaming 

Re-enables Log Streaming for an App Service that was previously paused. Log Streaming needs to be previously configured for the App Service before it can be paused or resumed.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

### Responses

**202** 

Successfully resumed log streaming for the app service.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/logStreaming/activationState

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/logStreaming/activationState

### Response samples 

* 403
* 404
* 422
* 429
* 500
* 503

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/App-Services-Log-Streaming/operation/pauseAppServiceLogStreaming)Pause App Service Log Streaming 

Temporarily disables Log Streaming for an App Service. Log Streaming needs to be previously configured for the App Service before it can be paused or resumed.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

### Responses

**202** 

Successfully paused log streaming for the app service.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/logStreaming/activationState

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/logStreaming/activationState

### Response samples 

* 403
* 404
* 422
* 429
* 500
* 503

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/App-Services-Log-Streaming/operation/postAppServiceLogStreaming)Configure App Service Log Streaming 

Sets up log streaming for a specific App Service.

Ensure you have provided collector credentials if you wish to begin streaming; log streaming cannot be enabled without credentials. Refer to schema below to see required fields for your log collection provider. Supported providers include Datadog, Sumo Logic, Grafana Loki, Elasticsearch (versions 8 and newer only), generic HTTP, Splunk, and Dynatrace.

Log streaming can only be configured while the config state is either enabled, paused, or disabled.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

##### Request Body schema: application/json

| outputTyperequired  | string Enum: "datadog" "generic\_http" "sumologic" "loki" "elastic" "splunk" "dynatrace" The log collector to have logs streamed to.                                                                              |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| credentialsrequired | datadog (object) or sumologic (object) or generic\_http (object) or elastic (object) or loki (object) or splunk (object) or dynatrace (object) The credentials to be used to authenticate with the log collector. |

### Responses

**202** 

Successful configuration of log streaming

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/logStreaming

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/logStreaming

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "outputType": "datadog",
* "credentials": {
  * "apiKey": "apiKey",
  * "url": "<https://http-intake.logs.datadoghq.eu>"  
}
}`

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500
* 503

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/App-Services-Log-Streaming/operation/getAppServiceLogStreaming)Get App Service Log Streaming Configuration and State 

Retrieves the configured output type, current config state, current streaming state of log streaming for a specific App Service.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

### Responses

**200** 

Successful retrieval of log streaming configuration and state

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/logStreaming

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/logStreaming

### Response samples 

* 200
* 403
* 404
* 429
* 500
* 503

Content type

application/json

Copy

`{
* "outputType": "datadog",
* "configState": "enabled",
* "streamingState": "healthy"
}`

## [](#tag/App-Services-Log-Streaming/operation/deleteAppServiceLogStreaming)Disable App Service Log Streaming 

Disables log streaming for a specific App Service.

This will remove the log streaming configuration for the App Service. To enable log streaming again, you will need to provide the configuration details once more using the "Configure App Service Log Streaming" endpoint.

Log streaming can only be disabled while the config state is either enabled or paused.

It may take a few minutes for the log streaming to be fully disabled.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

### Responses

**202** 

Log streaming disabled

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/logStreaming

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/logStreaming

### Response samples 

* 403
* 404
* 422
* 429
* 500
* 503

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/App-Services-Log-Streaming/operation/putAppEndpointLogStreamingConfig)Update App Endpoint Log Streaming Config 

Updates the log streaming config for an app endpoint, which configures log levels and keys used to filter log messages.

This app endpoint log streaming config can only be updated while the log streaming config state is either "paused" or "enabled".

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                        |

##### Request Body schema: application/json

| logLevelrequired | string Enum: "info" "warn" "error" Controls the verbosity of logs based on the specified log level                                                                          |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| logKeysrequired  | Array of stringsItems Enum: "Admin" "Access" "Auth" "Cache" "Changes" "CRUD" "HTTP" "HTTP+" "Import" "Javascript" "Query" "Sync" "SyncMsg" Filter logs to specific log keys |

### Responses

**204** 

Successful update of the app endpoint log streaming configuration

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

**504** 

The server did not get a response in time from the upstream server in order to complete the request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/logStreaming

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/logStreaming

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "logLevel": "warn",
* "logKeys": [
  * "HTTP",
  * "Import",
  * "Sync"  
]
}`

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500
* 503
* 504

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/App-Services-Log-Streaming/operation/getAppEndpointLogStreamingConfig)Get App Endpoint Log Streaming Config 

Retrieves log streaming config for an app endpoint, which shows log levels and keys used to filter log messages.

This app endpoint log streaming config can only be retrieved while the log streaming config state is either "paused" or "enabled".

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired  | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired    | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| appEndpointNamerequired | string Example: endpoint1The name of the App Endpoint.                                        |

### Responses

**200** 

Successful retrieval of the app endpoint log streaming configuration

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource. This response can also indicate that the requested App Endpoint or bucket does not exist or the user does not have access to it.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**503** 

The server is currently unable to handle the request

**504** 

The server did not get a response in time from the upstream server in order to complete the request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/logStreaming

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/appEndpoints/{appEndpointName}/logStreaming

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500
* 503
* 504

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "logLevel": "warn",
* "logKeys": [
  * "HTTP",
  * "Import",
  * "Sync"  
]
}`

## [](#tag/App-Services-Private-Endpoints)App Services Private Endpoints

App Services Private Endpoints enables you to configure a secure private network connection between the Virtual Private Cloud (VPC) hosting your applications and the VPC of your Couchbase Capella App Services. Note: This is currently only available for AWS.

## [](#tag/App-Services-Private-Endpoints/operation/postAppServicePrivateEndpoints)Enable App Service Private Endpoints 

Enable Private Endpoints for an App Service.

Supporting infrastructure is deployed and it may take a few minutes for Private Endpoints to be available. Once enabled, you can create Private Endpoints in your network. You can do this using the cloud provider's CLI. To obtain the command use the /privateEndpointService/privateEndpointCommand endpoint.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

### Responses

**202** 

App Service Private Endpoints enabled successfully.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/privateEndpointService

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/privateEndpointService

### Response samples 

* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/App-Services-Private-Endpoints/operation/getAppServicePrivateEndpoints)Get App Service Private Endpoints State 

The App Service Private Endpoint service allows you to access your Capella cluster from your private network, using Private Endpoints.

This endpoint determines if the endpoint service is enabled or disabled for your App Service.

It returns both a state and targetState. The state indicates the current status of the service, while the targetState indicates the desired end state of the service.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

### Responses

**200** 

Successful retrieval of Private Endpoints state

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/privateEndpointService

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/privateEndpointService

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "state": "enabled",
* "targetState": "enabled"
}`

## [](#tag/App-Services-Private-Endpoints/operation/deleteAppServicePrivateEndpoints)Disable App Service Private Endpoints 

Disable Private Endpoints for an App Service.

Supporting infrastructure is removed and it may take a few minutes before the Private Endpoint service is disabled.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

### Responses

**202** 

App Service Private Endpoints disabled successfully.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/privateEndpointService

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/privateEndpointService

### Response samples 

* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/App-Services-Private-Endpoints/operation/getAppServicePrivateEndpointsCommand)Get App Service Private Endpoints Command 

Retrieves the Private Endpoints command in order to create Private Endpoints and initiate the connection between the specified VPC and the App Service.

An example for AWS:

```
aws ec2 create-vpc-endpoint \
  --vpc-id vpc-1234 \
  --region us-east-1 \
  --service-name com.amazonaws.vpce.us-east-1.vpce-svc-1234 \
  --vpc-endpoint-type Interface \
  --subnet-ids subnet-1234

```

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

##### Request Body schema: application/json

One of 

CreateVPCEndpointCommandRequest

| vpcIDrequired     | string \[ 12 .. 21 \] characters The ID of your virtual network |
| ----------------- | --------------------------------------------------------------- |
| subnetIDsrequired | Array of strings                                                |

### Responses

**200** 

Successfully returned commands to establish a private connection to the App Service.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/privateEndpointService/privateEndpointCommand

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/privateEndpointService/privateEndpointCommand

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "vpcID": "vpc-1234",
* "subnetIDs": [
  * "subnet-1234"  
]
}`

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "command": "aws ec2 create-vpc-endpoint --vpc-id vpc-1234 --region us-east-1 --service-name com.amazonaws.vpce.us-east-1.vpce-svc-1234 --vpc-endpoint-type Interface --subnet-ids subnet-1234"
}`

## [](#tag/App-Services-Private-Endpoints/operation/listAppServicePrivateEndpoints)List App Service Private Endpoints 

Returns a list of the Private Endpoints associated with your Capella App Service with its current state. Each of these Private Endpoints is either attempting to connect or is connected to the App Service network.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Creator
* Project Viewer To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

### Responses

**200** 

Successfully retrieved list of App Service Private Endpoints.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/privateEndpointService/endpoints

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/privateEndpointService/endpoints

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "privateEndpointDNS": "abcdef123456.pl.cloud.couchbase.com",
* "endpoints": [
  * {
    * "id": "vpce-000000000000aaaaa",
    * "serviceName": "com.amazonaws.vpce.us-east-1.vpce-svc-000000000000aaaaa",
    * "status": "linked"  
  }  
]
}`

## [](#tag/App-Services-Private-Endpoints/operation/acceptPrivateEndpointRequest)Accept Private Endpoint Request 

Accepts a Private Endpoint connection request for an App Service. This completes the connection and means the Private Endpoint is now associated with the App Service and available for use.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| endpointIdrequired     | string Example: vpce-1234The VPC endpoint ID.                                                 |

### Responses

**204** 

Successfully accepted Private Endpoint connection request.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/privateEndpointService/endpoints/{endpointId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/privateEndpointService/endpoints/{endpointId}

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/App-Services-Private-Endpoints/operation/deletePrivateEndpointRequest)Delete Private Endpoint Request 

If the Private Endpoint is already connected and accepted this will unassociate the Private Endpoint from the App Service. If the Private Endpoint is not already connected this will reject the Private Endpoint connection request.

Both cases will remove the Private Endpoint from the App Service and it will no longer be available for use and any connection will be terminated.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |
| endpointIdrequired     | string Example: vpce-1234The VPC endpoint ID.                                                 |

### Responses

**204** 

Successfully deleted private endpoint.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/privateEndpointService/endpoints/{endpointId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/{appServiceId}/privateEndpointService/endpoints/{endpointId}

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Audit-Logs)Audit Logs

Users can configure audit log support on Capella database and can export audit logs from cloud blob storage to an AWS S3 bucket. Users can retrieve audit logs from a pre-signed download URL. Logs are retained for 30 days.

## [](#tag/Audit-Logs/operation/putClusterAuditSettings)Update Cluster Audit Log Configuration 

Updates the audit log configuration for the cluster.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| auditEnabledrequired    | boolean Determines whether audit logging is enabled or not on the cluster.                                |
| ----------------------- | --------------------------------------------------------------------------------------------------------- |
| disabledUsersrequired   | Array of objects (AuditSettingsDisabledUsers) List of users whose filterable events will not be logged.   |
| enabledEventIDsrequired | Array of integers <int32\> \[ items <int32 \> \] List of enabled filterable audit events for the cluster. |

### Responses

**204** 

Successfully updated the cluster audit log configuration.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/auditLog

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/auditLog

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "auditEnabled": true,
* "disabledUsers": [
  * {
    * "domain": "local",
    * "name": "@eventing"  
  }  
],
* "enabledEventIDs": [
  * 8243,
  * 8255  
]
}`

### Response samples 

* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Audit-Logs/operation/getClusterAuditSettings)Get Cluster Audit Log Configuration 

Fetches information on whether audit logging is enabled, and which event IDs are enabled.

To learn more about cluster audit logs, please refer to [audit management](https://docs.couchbase.com/cloud/security/audit-management.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**200** 

Successfully retrieved the cluster audit log settings.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/auditLog

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/auditLog

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "auditEnabled": true,
* "disabledUsers": [
  * {
    * "domain": "local",
    * "name": "dfelton"  
  }  
],
* "enabledEventIDs": [
  * [
    * 8243,
    * 8255  
  ]  
]
}`

## [](#tag/Audit-Logs/operation/getAuditLogEventIDs)List Filterable Audit Log Events 

Retrieves a list of audit event IDs. The list of filterable event IDs can be specified while configuring audit log for cluster.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**200** 

Successfully retrieved audit event Ids.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/auditLogEvents

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/auditLogEvents

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "events": [
  * {
    * "description": "Document was mutated via the REST API",
    * "id": 8243,
    * "module": "ns_server",
    * "name": "mutate document"  
  }  
]
}`

## [](#tag/Audit-Logs/operation/postAuditLogExport)Create Cluster Audit Log Export job 

Creates a new audit log export job.

Audit Logs for the last 30 days can be requested, otherwise they are purged. A pre-signed URL to a s3 bucket location is returned, which is used to download these audit logs.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| startrequired | string <date-time\> Specifies the audit log's start date and time. |
| ------------- | ------------------------------------------------------------------ |
| endrequired   | string <date-time\> Specifies the audit log's end date and time.   |

### Responses

**202** 

Successfully created audit export job for the cluster.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/auditLogExports

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/auditLogExports

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "start": "2022-09-04T00:56:07.000Z",
* "end": "2022-09-05T04:56:07.000Z"
}`

### Response samples 

* 202
* 403
* 404
* 409
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "exportId": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/Audit-Logs/operation/listAuditLogExports)List Cluster Audit Log Export Jobs 

Lists all the audit log export jobs and shows the status for each job.

It will show the pre-signed URL if the export was successful, a failure error if it was unsuccessful or a message saying no audit logs available if there were no audit logs found.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### query Parameters

| page    | integer Sets the page you would like to view.                           |
| ------- | ----------------------------------------------------------------------- |
| perPage | integer Sets the number of results you would like to have on each page. |

### Responses

**200** 

Successfully lists all audit export jobs for the cluster.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/auditLogExports

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/auditLogExports

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "cursor": {
  * "pages": {
    * "last": 1,
    * "next": 1,
    * "page": 1,
    * "perPage": 10,
    * "previous": 1,
    * "totalItems": 2  
  },
  * "hrefs": {
    * "first": "<https://cloudapi.cloud.couchbase.com/v4/organizations/ffffffff-aaaa-1414-eeee-000000000000/projects/ffffffff-aaaa-1414-eeee-000000000000/clusters/ffffffff-aaaa-1414-eeee-000000000000/auditLogExports?page=1&perPage=10>",
    * "last": "<https://cloudapi.cloud.couchbase.com/v4/organizations/ffffffff-aaaa-1414-eeee-000000000000/projects/ffffffff-aaaa-1414-eeee-000000000000/clusters/ffffffff-aaaa-1414-eeee-000000000000/auditLogExports?page=1&perPage=10>",
    * "next": "<https://cloudapi.cloud.couchbase.com/v4/organizations/ffffffff-aaaa-1414-eeee-000000000000/projects/ffffffff-aaaa-1414-eeee-000000000000/clusters/ffffffff-aaaa-1414-eeee-000000000000/auditLogExports?page=1&perPage=10>",
    * "previous": ""  
  }  
},
* "data": [
  * {
    * "createdAt": "2023-05-16T06:43:46.264296574Z",
    * "exportId": "d9db8594-4d0d-43b5-8dfe-1a6679d5b7d3",
    * "start": "2023-05-15T04:56:07Z",
    * "end": "2023-05-16T06:43:46.255479842Z",
    * "status": "Failed"  
  },
  * {
    * "createdAt": "2023-05-16T06:39:33.745602046Z",
    * "exportId": "624752e7-4600-4007-9a29-15d1323fbd0c",
    * "start": "2023-05-15T04:56:07Z",
    * "end": "2023-05-16T06:39:33.732661698Z",
    * "status": "Queued"  
  }  
]
}`

## [](#tag/Audit-Logs/operation/getAuditLogExport)Get Cluster Audit Log Export 

Fetches the status of a single audit log export job.

It will show the pre-signed URL if the export was successful, a failure error if it was unsuccessful or a message saying no audit logs available if there were no audit logs found during the given timeframe.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.  |
| ------------------------ | ---------------------------------------------------------------------------------------------- |
| projectIdrequired        | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.       |
| clusterIdrequired        | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.       |
| auditLogExportIdrequired | string Example: ffffffff-aaaa-1414-eeee-000000000000The export ID of the audit log export job. |

### Responses

**200** 

Successfully retrieved audit export job.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/auditLogExports/{auditLogExportId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/auditLogExports/{auditLogExportId}

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Example

InProgressQueuedFailedCompletedInProgress

Copy

`{
* "createdAt": "2023-05-16T04:00:08.870076042Z",
* "auditLogExportId": "40b9318a-cc93-458d-bc3e-7d4ffa778386",
* "start": "2023-05-15T04:56:07Z",
* "end": "2023-05-16T04:56:07Z",
* "status": "In Progress"
}`

## [](#tag/Backup-Schedule-%28Bucket%29)Backup Schedule (Bucket)

Couchbase supports a robust scheduled backup and retention time policy as part of an overall disaster recovery plan for production data. Couchbase Capella supports scheduled and on-demand backups of bucket data. A backup can be restored to the same database where it was created or another database in the same organization. On setting up a backup schedule, the bucket automatically backs up the bucket based on the chosen schedule.

## [](#tag/Backup-Schedule-%28Bucket%29/operation/postBackupSchedule)Create Backup Schedule 

Creates a scheduled backup for a bucket.

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/backup-restore.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |

##### Request Body schema: application/json

| type           | string Value: "weekly"                                               |
| -------------- | -------------------------------------------------------------------- |
| weeklySchedule | object Schedule a full backup once a week with regular incrementals. |

### Responses

**202** 

Successfully created a scheduled backup for a bucket.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/backup/schedules

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/backup/schedules

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "type": "weekly",
* "weeklySchedule": {
  * "dayOfWeek": "sunday",
  * "startAt": 10,
  * "incrementalEvery": 4,
  * "retentionTime": "90days",
  * "costOptimizedRetention": false  
}
}`

### Response samples 

* 400
* 403
* 404
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Backup-Schedule-%28Bucket%29/operation/getBackupSchedule)Get Backup Schedule 

Fetched the backup schedule for a bucket in a cluster.

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/backup-restore.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |

### Responses

**200** 

Successfully listed all backups for a bucket under the cluster.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/backup/schedules

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/backup/schedules

### Response samples 

* 200
* 400
* 403
* 404
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "type": "weekly",
* "clusterID": "ffffffff-aaaa-1414-eeee-000000000000",
* "bucketId": "dGVzdA",
* "weeklySchedule": {
  * "dayOfWeek": "sunday",
  * "startAt": 10,
  * "incrementalEvery": 4,
  * "retentionTime": "90days",
  * "costOptimizedRetention": false  
}
}`

## [](#tag/Backup-Schedule-%28Bucket%29/operation/putBackupSchedule)Update Backup Schedule 

Updates an existing backup schedule.

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/backup-restore.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |

##### Request Body schema: application/json

| type           | string Value: "weekly"                                               |
| -------------- | -------------------------------------------------------------------- |
| weeklySchedule | object Schedule a full backup once a week with regular incrementals. |

### Responses

**204** 

Successfully updated backup schedule.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/backup/schedules

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/backup/schedules

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "type": "weekly",
* "weeklySchedule": {
  * "dayOfWeek": "sunday",
  * "startAt": 0,
  * "incrementalEvery": 4,
  * "retentionTime": "90days",
  * "costOptimizedRetention": false  
}
}`

### Response samples 

* 400
* 403
* 404
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Backup-Schedule-%28Bucket%29/operation/deleteBackupSchedule)Delete Backup Schedule 

Deletes an existing backup schedule

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/backup-restore.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |

### Responses

**202** 

Successfully deleted the backup schedule.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/backup/schedules

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/backup/schedules

### Response samples 

* 400
* 403
* 404
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Backup-Schedule-%28Bucket%29/operation/listCycles)List Cycles 

Lists the cycles for a bucket in a cluster.

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/backup-restore.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |

##### query Parameters

| startDate | string <date\> Example: startDate=2023-07-19Filters bucket backups beginning from the start date. Specify the start date to retrieve relevant bucket backups from start date. |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| endDate   | string <date\> Example: endDate=2023-07-21Filters bucket backups till the end date. Specify the end date to retrieve relevant bucket backups till end date.                   |

### Responses

**200** 

Successfully listed all cycles for a bucket in the cluster.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/backup/cycles

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/backup/cycles

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "cycleID": "8109f151-4475-4d31-bf7e-559b0ecf345e",
    * "createdAt": "2021-09-01T12:34:56Z"  
  }  
]
}`

## [](#tag/Backup-Schedule-%28Bucket%29/operation/listBackups)List Backups 

Lists the backups for a cycle in a bucket.

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/backup-restore.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |
| cycleIdrequired        | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cycle.                   |

### Responses

**200** 

Successfully listed the backups for a cycle in a bucket.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/backup/cycles/{cycleId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/backup/cycles/{cycleId}

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "clusterID": "ffffffff-aaaa-1414-eeee-000000000000",
    * "tenantID": "ffffffff-aaaa-1414-eeee-000000000000",
    * "projectID": "ffffffff-aaaa-1414-eeee-000000000000",
    * "cycleID": "string",
    * "date": "2021-09-01T12:34:56Z",
    * "restoreBefore": "2021-09-02T12:34:56Z",
    * "status": "pending",
    * "method": "incremental",
    * "bucketName": "My-First-Bucket",
    * "bucketID": "dGVzdA",
    * "source": "scheduled",
    * "provider": "aws",
    * "stats": {
      * "sizeInMb": 0.1,
      * "items": 150,
      * "mutations": 150,
      * "tombstones": 4,
      * "gsi": 46,
      * "fts": 30,
      * "cbas": 30,
      * "event": 25  
      },
    * "elapsedTimeInSeconds": 30,
    * "scheduleInfo": {
      * "backupType": "Weekly",
      * "backupTime": "2023-07-13 20:26:54.990864215 +0000 UTC",
      * "increment": 4,
      * "retention": "90days"  
      }  
  }  
]
}`

## [](#tag/Backups-and-Restore-%28Bucket%29)Backups & Restore (Bucket)

Couchbase supports a robust scheduled backup and retention time policy as part of an overall disaster recovery plan for production data. Couchbase Capella supports scheduled and on-demand backups of bucket data. A backup can be restored to the same database where it was created or another database in the same organization. An on-demand backup of a bucket is always a Full backup. Capella schedules on-demand backup to start immediately.

## [](#tag/Backups-and-Restore-%28Bucket%29/operation/postBackup)Create Backup 

Creates an on-demand backup for a bucket.

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/backup-restore.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |

### Responses

**202** 

Successfully created an on-demand backup for a bucket.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/backups

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/backups

### Response samples 

* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Backups-and-Restore-%28Bucket%29/operation/listClusterBackups)List Cluster Backups 

Lists the latest backup for all buckets in a cluster.

Note: This endpoint doesn't return queued backups and only returns ones that are actively being processed or are completed/failed.

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/backup-restore.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**200** 

Successfully listed the latest backups for all buckets under the cluster.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/backups

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/backups

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "clusterID": "ffffffff-aaaa-1414-eeee-000000000000",
    * "tenantID": "ffffffff-aaaa-1414-eeee-000000000000",
    * "projectID": "ffffffff-aaaa-1414-eeee-000000000000",
    * "cycleID": "string",
    * "date": "2021-09-01T12:34:56Z",
    * "restoreBefore": "2021-09-02T12:34:56Z",
    * "status": "pending",
    * "method": "incremental",
    * "bucketName": "My-First-Bucket",
    * "bucketID": "dGVzdA",
    * "source": "scheduled",
    * "provider": "aws",
    * "stats": {
      * "sizeInMb": 0.1,
      * "items": 150,
      * "mutations": 150,
      * "tombstones": 4,
      * "gsi": 46,
      * "fts": 30,
      * "cbas": 30,
      * "event": 25  
      },
    * "elapsedTimeInSeconds": 30,
    * "scheduleInfo": {
      * "backupType": "Weekly",
      * "backupTime": "2023-07-13 20:26:54.990864215 +0000 UTC",
      * "increment": 4,
      * "retention": "90days"  
      },
    * "bucketDownloadsCount": 2  
  }  
]
}`

## [](#tag/Backups-and-Restore-%28Bucket%29/operation/getBackupByID)Get Backup 

Fetches the details of an existing backup.

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/backup-restore.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| backupIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the backup.       |

### Responses

**200** 

Successfully fetched the backup by its backupId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/backups/{backupId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/backups/{backupId}

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "clusterID": "ffffffff-aaaa-1414-eeee-000000000000",
* "tenantID": "ffffffff-aaaa-1414-eeee-000000000000",
* "projectID": "ffffffff-aaaa-1414-eeee-000000000000",
* "cycleID": "string",
* "date": "2021-09-01T12:34:56Z",
* "restoreBefore": "2021-09-02T12:34:56Z",
* "status": "pending",
* "method": "incremental",
* "bucketName": "My-First-Bucket",
* "bucketID": "dGVzdA",
* "source": "scheduled",
* "provider": "aws",
* "stats": {
  * "sizeInMb": 0.1,
  * "items": 150,
  * "mutations": 150,
  * "tombstones": 4,
  * "gsi": 46,
  * "fts": 30,
  * "cbas": 30,
  * "event": 25  
},
* "elapsedTimeInSeconds": 30,
* "scheduleInfo": {
  * "backupType": "Weekly",
  * "backupTime": "2023-07-13 20:26:54.990864215 +0000 UTC",
  * "increment": 4,
  * "retention": "90days"  
}
}`

## [](#tag/Backups-and-Restore-%28Bucket%29/operation/deleteBackupCycleByID)Delete Backup Cycle 

Deletes the backup records that belong to the same cycle from the DB by using the backup ID.

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/backup-restore.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| backupIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the backup.       |

### Responses

**202** 

Successfully deleted the backup by its backupId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/backups/{backupId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/backups/{backupId}

### Response samples 

* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Backups-and-Restore-%28Bucket%29/operation/postRestore)Restore Backup 

Creates an on-demand restore job for a backup immediately.

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/backup-restore.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| backupIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the backup.       |

##### Request Body schema: application/json

| targetClusterIDrequired | string <uuid\> The ID of the target cluster to restore to.                                               |
| ----------------------- | -------------------------------------------------------------------------------------------------------- |
| sourceClusterIDrequired | string <uuid\> The ID of the source cluster the restore is based on.                                     |
| backupIDrequired        | string <uuid\> The backup record ID that contains the backup to restore from.                            |
| servicesrequired        | Array of strings (Services) Items Enum: "data" "query"                                                   |
| forceUpdates            | boolean Forces data in the Couchbase cluster to be overwritten even if the data in the cluster is newer. |
| autoRemoveCollections   | boolean Automatically delete scopes/collections which are known to be deleted in the backup.             |
| filterKeys              | string Only restore data where the key matches a particular regular expression.                          |
| filterValues            | string Only restore data where the value matches a particular regular expression.                        |
| includeData             | string Restores only the data specified here.                                                            |
| excludeData             | string Skips restoring the data specified here.                                                          |
| mapData                 | string Specified when you want to restore source data into a different location.                         |
| replaceTTL              | string Enum: "none" "all" "expired" Sets a new expiration (time-to-live) value for the specified keys.   |
| replaceTTLWith          | string Updates the expiration for the keys.                                                              |

### Responses

**202** 

Successfully created an on-demand restore for a bucket.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/backups/{backupId}/restore

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/backups/{backupId}/restore

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "targetClusterID": "ffffffff-aaaa-1414-eeee-000000000000",
* "sourceClusterID": "ffffffff-aaaa-1414-eeee-000000000000",
* "backupID": "ffffffff-aaaa-1414-eeee-000000000000",
* "services": [
  * "data",
  * "query"  
],
* "forceUpdates": true,
* "autoRemoveCollections": true,
* "filterKeys": "",
* "filterValues": "",
* "includeData": "bucket-1.scope1",
* "excludeData": "bucket-1.scope1.coll1",
* "mapData": "bucket1=new1",
* "replaceTTL": "all",
* "replaceTTLWith": "2021-09-01T12:34:56Z"
}`

### Response samples 

* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Billing)Billing

The Billing endpoints allow you to retrieve billing information for your organization. You can view usage data organized by time period and filter by categories, projects, or instances.

## [](#tag/Billing/operation/categorizedBilling)Get Categorized Billing 

Retrieves billing information for the organization within the specified date range and filters.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| startDaterequired | string <date\> The start date of the billing period in YYYY-MM-DD format. |
| ----------------- | ------------------------------------------------------------------------- |
| endDaterequired   | string <date\> The end date of the billing period in YYYY-MM-DD format.   |
| filters           | object (BillingFilters) Filters to narrow down the billing information.   |

### Responses

**200** 

Successfully retrieved the categorized billing information.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/billing

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/billing

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "value": {
  * "startDate": "2025-04-01",
  * "endDate": "2025-04-30",
  * "filters": {
    * "categories": [
      * "analyticsCompute",
      * "analyticsStorage"  
      ],
    * "projectIds": [
      * "ffffffff-aaaa-1414-eeee-000000000000",
      * "ffffffff-aaaa-1414-eeee-000000000001"  
      ],
    * "instanceIds": [
      * "ffffffff-aaaa-1414-eeee-000000000000",
      * "ffffffff-aaaa-1414-eeee-000000000001"  
      ]  
  }  
}
}`

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Example

Monthly usage in amount (currency)Monthly usage in creditsDaily usage (for date ranges within a month)Monthly usage in amount (currency)

Copy

 Expand all  Collapse all 

`{
* "data": {
  * "periods": [
    * {
      * "startDate": "2025-04-01",
      * "endDate": "2025-04-30",
      * "categories": [
        * {
          * "category": "analyticsCompute",
          * "creditSpend": null,
          * "currencySpend": 90.1,
          * "contributionPercent": 74  
                    },
        * {
          * "category": "analyticsStorage",
          * "creditSpend": null,
          * "currencySpend": 31.65,
          * "contributionPercent": 26  
                    }  
            ],
      * "totalCreditSpend": null,
      * "totalCurrencySpend": 3302.11  
      }  
  ],
  * "total": {
    * "startDate": "2025-04-01",
    * "endDate": "2025-04-30",
    * "categories": [
      * {
        * "category": "analyticsCompute",
        * "creditSpend": null,
        * "currencySpend": 2914.46,
        * "contributionPercent": 11.15  
            },
      * {
        * "category": "analyticsStorage",
        * "creditSpend": null,
        * "currencySpend": 1250.25,
        * "contributionPercent": 4.78  
            }  
      ],
    * "totalCreditSpend": null,
    * "totalCurrencySpend": 26120.18  
  },
  * "billingCurrency": "USD"  
}
}`

## [](#tag/Billing/operation/itemizedBillingPerCluster)Get Itemized Billing Per Cluster 

Retrieves itemized billing information for a specific cluster within the specified date range and filters. Note: This endpoint supports operational clusters only.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| startDaterequired | string <date\> The start date of the billing period in YYYY-MM-DD format.                |
| ----------------- | ---------------------------------------------------------------------------------------- |
| endDaterequired   | string <date\> The end date of the billing period in YYYY-MM-DD format.                  |
| filters           | object (ItemizedBillingFilters) Filters to narrow down the itemized billing information. |

### Responses

**200** 

Successfully retrieved the itemized billing information for the cluster.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/billing

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/billing

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "value": {
  * "startDate": "2025-04-01",
  * "endDate": "2025-04-30",
  * "filters": {
    * "categories": [
      * "operationalComputeAndStorage",
      * "operationalBucketBackup"  
      ]  
  }  
}
}`

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": {
  * "clusterName": "test-123",
  * "supportPlan": "DeveloperPro",
  * "periods": [
    * {
      * "startDate": "2025-04-01",
      * "endDate": "2025-04-30",
      * "categories": [
        * {
          * "category": "operationalComputeAndStorage",
          * "creditSpend": null,
          * "currencySpend": 90.1,
          * "contributionPercent": 74  
                    },
        * {
          * "category": "operationalBucketBackup",
          * "creditSpend": null,
          * "currencySpend": 31.65,
          * "contributionPercent": 26  
                    }  
            ],
      * "totalCreditSpend": null,
      * "totalCurrencySpend": 3302.11  
      }  
  ],
  * "total": {
    * "startDate": "2025-04-01",
    * "endDate": "2025-04-30",
    * "categories": [
      * {
        * "category": "operationalComputeAndStorage",
        * "creditSpend": null,
        * "currencySpend": 2914.46,
        * "contributionPercent": 11.15  
            },
      * {
        * "category": "operationalBucketBackup",
        * "creditSpend": null,
        * "currencySpend": 1250.25,
        * "contributionPercent": 4.78  
            }  
      ],
    * "totalCreditSpend": null,
    * "totalCurrencySpend": 26120.18  
  },
  * "billingCurrency": "USD"  
}
}`

## [](#tag/Billing/operation/prepaidCreditsBilling)Get Prepaid Credits Billing 

Retrieves prepaid credits information for the organization, including credit details, usage, and remaining amounts.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### query Parameters

| page    | integer Sets the page you would like to view.                           |
| ------- | ----------------------------------------------------------------------- |
| perPage | integer Sets the number of results you would like to have on each page. |

### Responses

**200** 

Successfully retrieved the prepaid credits billing information.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/billing/prePaidCredits

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/billing/prePaidCredits

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "sfdc-credit-id-12345",
    * "creditName": "CN-12345",
    * "supportPlan": "Plan: Developer Pro",
    * "startDate": "2024-01-01T00:00:00Z",
    * "expirationDate": "2024-12-31T23:59:59Z",
    * "total": 1000,
    * "used": 350.5,
    * "remaining": 649.5,
    * "remainingPercent": 64.95  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/Billing/operation/payAsYouGoBilling)Get Pay As You Go Billing 

Retrieves pay-as-you-go billing information for the organization within the specified date range, broken down by support plan type.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### query Parameters

| startDate | string <date\> Example: startDate=2025-04-01The start date of the billing period in YYYY-MM-DD format. |
| --------- | ------------------------------------------------------------------------------------------------------ |
| endDate   | string <date\> Example: endDate=2025-05-31The end date of the billing period in YYYY-MM-DD format.     |

### Responses

**200** 

Successfully retrieved the pay-as-you-go billing information.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/billing/payAsYouGo

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/billing/payAsYouGo

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": {
  * "periods": [
    * {
      * "startDate": "2025-04-01",
      * "endDate": "2025-04-30",
      * "cost": {
        * "basic": 0,
        * "devPro": 316.62,
        * "enterprise": 150  
            },
      * "total": 466.62  
      },
    * {
      * "startDate": "2025-05-01",
      * "endDate": "2025-05-31",
      * "cost": {
        * "basic": 100,
        * "devPro": 450.25,
        * "enterprise": 200  
            },
      * "total": 750.25  
      }  
  ],
  * "total": {
    * "startDate": "2025-04-01",
    * "endDate": "2025-05-31",
    * "cost": {
      * "basic": 100,
      * "devPro": 766.87,
      * "enterprise": 350  
      },
    * "total": 1216.87  
  },
  * "billingCurrency": "USD"  
}
}`

## [](#tag/Billing/operation/downloadCategorizedBilling)Download Categorized Billing 

Downloads a csv file with categorized billing information for the organization within the specified date range and filters. Downloaded CSV file named `capella-categorized-billing-{organizationId}-{startDate}_to_{endDate}.csv` with the following columns:

* `startDate` : The start date
* `endDate` : The end date
* `category`: The category name
* `creditSpend`: Usage in Capella credits for this category
* `currencySpend`: Usage in dollar or any billingCurrency amount for this category
* `contributionPercent`: contributionPercent of total consumption
* `billingCurrency`: currency

`Total` \- The final row of the CSV will contain totals across all categories over the full time period

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| startDaterequired | string <date\> The start date of the billing period in YYYY-MM-DD format. |
| ----------------- | ------------------------------------------------------------------------- |
| endDaterequired   | string <date\> The end date of the billing period in YYYY-MM-DD format.   |
| filters           | object (BillingFilters) Filters to narrow down the billing information.   |

### Responses

**200** 

Successfully downloaded the categorized billing information as a CSV file.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/billing/download

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/billing/download

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "startDate": "2025-04-01",
* "endDate": "2025-04-30",
* "filters": {
  * "categories": [
    * "analyticsCompute",
    * "analyticsStorage"  
  ],
  * "projectIds": [
    * "ffffffff-aaaa-1414-eeee-000000000000",
    * "ffffffff-aaaa-1414-eeee-000000000001"  
  ],
  * "instanceIds": [
    * "ffffffff-aaaa-1414-eeee-000000000000",
    * "ffffffff-aaaa-1414-eeee-000000000001"  
  ]  
}
}`

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Billing/operation/downloadItemizedBilling)Download Itemized Billing 

Downloads a CSV file with itemized billing information for a specific cluster within the specified date range and filters. Note: This endpoint supports operational clusters only. Downloaded CSV file named `capella-itemized-billing-{clusterId}-{startDate}_to_{endDate}.csv` with the following columns:

* `startDate` : The start date
* `endDate` : The end date
* `category`: The category name
* `projectId`: The UUID of the project containing the cluster
* `clusterId`: The UUID of the cluster
* `clusterName`: The name of the cluster
* `supportPlan`: The support plan of the cluster (e.g., DeveloperPro, Enterprise).
* `creditSpend`: Usage in Capella credits for this category
* `currencySpend`: Usage in dollar or any billingCurrency amount for this category
* `contributionPercent`: contributionPercent of total consumption
* `billingCurrency`: currency

`Total` \- The final row of the CSV will contain totals across all categories over the full time period

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| startDaterequired | string <date\> The start date of the billing period in YYYY-MM-DD format.                |
| ----------------- | ---------------------------------------------------------------------------------------- |
| endDaterequired   | string <date\> The end date of the billing period in YYYY-MM-DD format.                  |
| filters           | object (ItemizedBillingFilters) Filters to narrow down the itemized billing information. |

### Responses

**200** 

Successfully downloaded the itemized billing information as a CSV file.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/billing/download

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/billing/download

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "startDate": "2025-04-01",
* "endDate": "2025-04-30",
* "filters": {
  * "categories": [
    * "operationalComputeAndStorage",
    * "operationalBucketBackup"  
  ]  
}
}`

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Buckets-Scopes-and-Collections)Buckets, Scopes, & Collections

A bucket is the fundamental space for storing data in Couchbase Capella. Scopes and Collections are logical containers within a bucket and a way for organizing data within buckets. A scope is a mechanism for the grouping of multiple collections. A collection is a data container for related documents.

## [](#tag/Buckets-Scopes-and-Collections/operation/postBucket)Create Bucket 

Creates a new bucket configuration under a cluster.

To learn more about bucket configuration, see [Buckets](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/buckets.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| namerequired             | string <= 100 characters Name of the bucket. This field cannot be changed later. The name should adhere to the following rules: Characters used for the name should be in the ranges of A-Z, a-z, and 0-9; plus the underscore, period, dash, and percent characters. The name can be a maximum of 100 characters in length. The name cannot have 0 characters or empty. Minimum length of name is 1. The name cannot start with a . (period).                                                                                                                                                                                                                                                              |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type                     | string (Type) Default: "couchbase" Enum: "couchbase" "ephemeral" Type of the bucket. If selected Ephemeral, it is not eligible for imports or App Endpoints creation. This field cannot be changed later. The options may also be referred to as Memory and Disk (Couchbase), Memory Only (Ephemeral) in the Couchbase documentation. To learn more, see [Create a Bucket](https://docs.couchbase.com/cloud/clusters/data-service/manage-buckets.html#add-bucket).                                                                                                                                                                                                                                          |
| storageBackend           | string (StorageBackend) Enum: "couchstore" "magma" The storage engine to be assigned to and used by the bucket. Ephemeral buckets do not support StorageBackend, hence not applicable for Ephemeral buckets and throws an error if this field is added. This field is only applicable for a Couchbase bucket. The default value before Couchbase Server 8.0 is couchstore. The default value for Couchbase Server 8.0 and above is magma with 128 vbuckets. This field cannot be changed later. To learn more, see [Storage Engines](https://docs.couchbase.com/cloud/clusters/data-service/storage-engines.html).                                                                                          |
| vbuckets                 | integer Default: 128 Enum: 128 1024 This field only applies to Couchbase Server 8.0 and above for magma buckets. There are two options for the number of vBuckets: 128 and 1024\. The number of vBuckets cannot be changed after the bucket is created.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| memoryAllocationInMb     | integer The amount of memory to allocate for the bucket memory in MiB. This is the maximum limit is dependent on the allocation of the KV service. For example, 80% of the allocation. For Couchbase buckets, the default and minimum memory allocation changes according to the Storage Backend type as follows: For Couchstore, the default and minimum memory allocation is 100 MiB. For Magma, the default and minimum memory allocation is 1024 MiB with 1024 buckets for Couchbase server below 8.0\. The default and minimum memory allocation is 100 MiB with 128 vbuckets for Couchbase server version 8.0 and above. For Ephemeral buckets, the default and minimum memory allocation is 100 MiB. |
| bucketConflictResolution | string (BucketConflictResolution) Default: "seqno" Enum: "seqno" "lww" The means by which conflicts are resolved during replication. This field may be referred to as "conflict resolution" in the Couchbase documentation, and seqno and lww may be referred to as "sequence number" and "timestamp" respectively. This field cannot be changed later.  To learn more, see [Conflict Resolution](https://docs.couchbase.com/cloud/clusters/xdcr/xdcr.html#conflict-resolution).                                                                                                                                                                                                                            |
| durabilityLevel          | string (DurabilityLevel) Default: "none" Enum: "none" "majority" "majorityAndPersistActive" "persistToMajority" This is the minimum level at which all writes to the bucket must occur.  The options for Durability level are as follows, according to the bucket type. For a Couchbase bucket: None Replicate to Majority Majority and Persist to Active Persist to Majority For an Ephemeral bucket: None Replicate to Majority  To learn more, see [Create a Bucket](https://docs.couchbase.com/cloud/clusters/data-service/manage-buckets.html#add-bucket).                                                                                                                                             |
| replicas                 | integer (Replicas) Default: 1 Enum: 1 2 3 The number of replicas for the bucket. To learn more, see [Create a Bucket](https://docs.couchbase.com/cloud/clusters/data-service/manage-buckets.html#add-bucket).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| flush                    | boolean Deprecated Default: false Replaced by flushEnabled. This property is deprecated and will be removed in a future release. Determines whether flushing is enabled on the bucket. Enable Flush to delete all items in this bucket at the earliest opportunity. Disable Flush to avoid inadvertent data loss.                                                                                                                                                                                                                                                                                                                                                                                           |
| flushEnabled             | boolean Default: false Determines whether bucket flush is enabled. Set flushEnabled to true to be able to delete all items in this bucket using the /flush endpoint. Disable flushEnabled to avoid inadvertent data loss by calling the /flush endpoint .                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| timeToLiveInSeconds      | integer Default: 0 Specify the time to live (TTL) value in seconds. This is the maximum time to live for items in the bucket. Default is 0, that means TTL is disabled. This is a non-negative value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| evictionPolicy           | string (EvictionPolicy) Default: "fullEviction" Enum: "fullEviction" "noEviction" "nruEviction" The policy which Capella adopts to prevent data loss due to memory exhaustion. This may be also known as Ejection Policy in the Couchbase documentation. For Couchbase bucket, Eviction Policy is fullEviction by default. For Ephemeral buckets, Eviction Policy is a required field, and should be one of the following: noEviction nruEviction To learn more, see [Ejection Policy](https://docs.couchbase.com/server/current/rest-api/rest-bucket-create.html#evictionpolicy).                                                                                                                          |
| priority                 | integer (BucketPriority) Default: 0 Priority of the bucket. Specify relative bucket priority so that buckets will be recovered in the order specified during failover. Bucket ranking/priority is only available in Couchbase Server 7.6 and above Default bucket priority is 0 and can be set to a value between 0 and 1000\. 1000 is the highest priority and 0 is the lowest.                                                                                                                                                                                                                                                                                                                            |

### Responses

**201** 

Successfully created a bucket.

**403** 

The client does not have the necessary permissions to access this resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets

### Request samples 

* Payload

Content type

application/json

Example

PostBucketTypeCouchbasePostBucketTypeEphemeralPostBucketWithDefaultsPostBucketWithEphemeralDefaultsPostBucketWithPersistToMajorityPostBucketWithEphemeralNoEvictionPostBucketWithCouchbaseMagmaPostBucketWithBucketPriorityPostBucketWithMagma128PostBucketWithMagma1024PostBucketTypeCouchbase

Copy

`{
* "name": "CBExample1",
* "type": "couchbase",
* "storageBackend": "couchstore",
* "memoryAllocationInMb": 105,
* "bucketConflictResolution": "seqno",
* "durabilityLevel": "majorityAndPersistActive",
* "replicas": 2,
* "flush": true,
* "timeToLiveInSeconds": 100
}`

### Response samples 

* 201
* 403
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "dGVzdA"
}`

## [](#tag/Buckets-Scopes-and-Collections/operation/listBuckets)List Buckets 

Lists all the buckets under the cluster.

To learn more about bucket configuration, see [Buckets](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/buckets.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**200** 

Successfully listed all the buckets under the cluster.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "dGVzdA",
    * "name": "My-First-Bucket",
    * "type": "string",
    * "storageBackend": "couchstore",
    * "vbuckets": 128,
    * "memoryAllocationInMb": 100,
    * "bucketConflictResolution": "string",
    * "durabilityLevel": "string",
    * "replicas": 0,
    * "flush": false,
    * "flushEnabled": false,
    * "timeToLiveInSeconds": 100,
    * "enableCrossClusterVersioning": true,
    * "evictionPolicy": "fullEviction",
    * "stats": {
      * "itemCount": 10,
      * "opsPerSecond": 0,
      * "diskUsedInMib": 17,
      * "memoryUsedInMib": 50  
      },
    * "priority": 0  
  }  
],
* "clusterStats": {
  * "freeMemoryInMb": 640,
  * "totalMemoryInMb": 1040,
  * "maxReplicas": 2  
}
}`

## [](#tag/Buckets-Scopes-and-Collections/operation/getBucketByID)Get Bucket 

Fetches the configuration of the given bucket.

To learn more about bucket configuration, see [Buckets](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/buckets.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |

### Responses

**200** 

Successfully fetched the bucket based on the bucketId.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "dGVzdA",
* "name": "My-First-Bucket",
* "type": "string",
* "storageBackend": "couchstore",
* "vbuckets": 128,
* "memoryAllocationInMb": 100,
* "bucketConflictResolution": "string",
* "durabilityLevel": "string",
* "replicas": 0,
* "flush": false,
* "flushEnabled": false,
* "timeToLiveInSeconds": 100,
* "enableCrossClusterVersioning": true,
* "evictionPolicy": "fullEviction",
* "stats": {
  * "itemCount": 10,
  * "opsPerSecond": 0,
  * "diskUsedInMib": 17,
  * "memoryUsedInMib": 50  
},
* "priority": 0
}`

## [](#tag/Buckets-Scopes-and-Collections/operation/putBucket)Update Bucket 

Updates an existing bucket.

To learn more about bucket configuration, see [Buckets](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/buckets.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |

##### Request Body schema: application/json

| memoryAllocationInMbrequired | integer The new amount of memory to allocate for the bucket memory in MiB. The maximum limit is dependent on the allocation of the KV service; for example, 80% of the allocation. For Couchbase buckets, the default and minimum memory allocation changes according to the Storage Backend type, as follows: For Couchstore, the default and minimum memory allocation is 100 MiB. For Magma, the default and minimum memory allocation is 1024 MiB. For Ephemeral buckets, the default and minimum memory allocation is 100 MiB.                                                                                                  |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| durabilityLevelrequired      | string Enum: "none" "majority" "majorityAndPersistActive" "persistToMajority" This is the minimum level at which all writes to the bucket must occur. The options for Durability level are as follows, according to the bucket type. For a Couchbase bucket: None Replicate to Majority Majority and Persist to Active Persist to Majority For an Ephemeral bucket: None Replicate to Majority A Durability other than None cannot be set on a bucket that is linked with an App Endpoint. To learn more, see [Create a Bucket](https://docs.couchbase.com/cloud/clusters/data-service/manage-buckets.html#add-bucket).              |
| replicasrequired             | integer Enum: 1 2 3 The number of replicas for the bucket. To learn more, see [Create a Bucket](https://docs.couchbase.com/cloud/clusters/data-service/manage-buckets.html#add-bucket).                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| flush                        | boolean Deprecated Default: false Replaced by flushEnabled. This property is deprecated and will be removed in a future release. The new value of flush property. This determines whether bucket flush is enabled. Enable Flush to be able to delete all items in this bucket at the earliest opportunity using /flush endpoint. Disable Flush to avoid inadvertent data loss by calling the /flush endpoint                                                                                                                                                                                                                         |
| flushEnabled                 | boolean Default: false This determines whether bucket flush is enabled. Enable flushEnabled to delete all items in this bucket at the earliest opportunity by calling the /flush endpoint. Disable flushEnabled to avoid inadvertent data loss by calling the /flush endpoint.                                                                                                                                                                                                                                                                                                                                                       |
| timeToLiveInSecondsrequired  | integer Specify the new time to live (TTL) value in seconds. This is the maximum time to live for items in the bucket. If specified as 0, TTL is disabled. This is a non-negative value. A bucket that is linked with an App Endpoint cannot have a TTL configured.                                                                                                                                                                                                                                                                                                                                                                  |
| enableCrossClusterVersioning | boolean (EnableCrossClusterVersioning) This being enabled is a pre-requisite to a few XDCR features. When enabled, each document processed by XDCR will have additional metadata stored, called the Hybrid Logical Vector (HLV), in the document extended attributes (xattrs). The Cross Cluster Versioning setting cannot be disabled after it is enabled. By default, this value reflects what its current value is in the bucket, so omit this setting to leave it as it's current value. See the documentation for enableCrossClusterVersioning and the dependent features for important details on when to enable this setting. |
| priority                     | integer (BucketPriority) Default: 0 Priority of the bucket. Specify relative bucket priority so that buckets will be recovered in the order specified during failover. Bucket ranking/priority is only available in Couchbase Server 7.6 and above Default bucket priority is 0 and can be set to a value between 0 and 1000\. 1000 is the highest priority and 0 is the lowest.                                                                                                                                                                                                                                                     |

### Responses

**204** 

Successfully accepted updated bucket configuration.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "memoryAllocationInMb": 100,
* "durabilityLevel": "none",
* "replicas": 1,
* "flush": false,
* "flushEnabled": false,
* "timeToLiveInSeconds": 100,
* "enableCrossClusterVersioning": true,
* "priority": 0
}`

### Response samples 

* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Buckets-Scopes-and-Collections/operation/deleteBucketByID)Delete Bucket 

Deletes an existing bucket.

To learn more about bucket configuration, see [Buckets](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/buckets.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |

### Responses

**204** 

Successfully deleted the bucket by its bucketId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}

### Response samples 

* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Buckets-Scopes-and-Collections/operation/FlushBucket)Flush Bucket Data 

Flushing of the bucket occurs, causing all items in the bucket to be deleted by the system at the earliest opportunity. This operation can only be performed if the bucket has been configured with flushEnabled to true. If it is disabled, it will throw an error.

It is recommended not to run with the flushEnabled configuration set to true in production; due to the danger of all a bucket's data being inadvertently lost. 

To learn more about bucket configuration, see [Buckets](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/buckets.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |

### Responses

**200** 

Successfully flushed a bucket.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/flush

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/flush

### Response samples 

* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Buckets-Scopes-and-Collections/operation/postScope)Create Scope 

Creates a new scope in a bucket.

To learn more about scopes and collections, see [Buckets, Scopes, and Collections](https://docs.couchbase.com/cloud/clusters/data-service/about-buckets-scopes-collections.html).

 In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |

##### Request Body schema: application/json

| namerequired | string The name of the scope. The name should adhere to the following rules: The name must be between 1 and 251 characters in length. The name can contain only the characters A-Z, a-z, 0-9, and the symbols \_, -, and %. The name cannot start with \_ or %. Note that scope and collection names are case-sensitive. |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### Responses

**201** 

Successfully created a scope.

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/scopes

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/scopes

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "name": "my-scope"
}`

### Response samples 

* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Buckets-Scopes-and-Collections/operation/getScopes)List Scopes 

Lists all the scopes in the bucket.

To learn more about scopes and collections, see [Buckets, Scopes, and Collections](https://docs.couchbase.com/cloud/clusters/data-service/about-buckets-scopes-collections.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |

### Responses

**200** 

Successfully listed all the scopes under the bucket.

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/scopes

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/scopes

### Response samples 

* 200
* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "scopes": [
  * {
    * "name": "inventory",
    * "collections": [
      * {
        * "name": "airport",
        * "maxTTL": 0  
            }  
      ]  
  }  
]
}`

## [](#tag/Buckets-Scopes-and-Collections/operation/getScopeByName)Get Scope 

Fetches the details of the given scope.

To learn more about scopes and collections, see [Buckets, Scopes, and Collections](https://docs.couchbase.com/cloud/clusters/data-service/about-buckets-scopes-collections.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |
| scopeNamerequired      | string Example: inventoryThe name of the scope.                                                          |

### Responses

**200** 

Successfully fetched the scope by its name.

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/scopes/{scopeName}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/scopes/{scopeName}

### Response samples 

* 200
* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "name": "inventory",
* "collections": [
  * {
    * "name": "airport",
    * "maxTTL": 0  
  }  
]
}`

## [](#tag/Buckets-Scopes-and-Collections/operation/deleteScopeByName)Delete Scope 

Deletes an existing scope.

To learn more about scopes and collections, see [Buckets, Scopes, and Collections](https://docs.couchbase.com/cloud/clusters/data-service/about-buckets-scopes-collections.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |
| scopeNamerequired      | string Example: inventoryThe name of the scope.                                                          |

### Responses

**204** 

Successfully deleted the scope by its name.

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/scopes/{scopeName}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/scopes/{scopeName}

### Response samples 

* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Buckets-Scopes-and-Collections/operation/postCollection)Create Collection 

Creates a new collection in a scope.

To learn more about scopes and collections, see [Buckets, Scopes, and Collections](https://docs.couchbase.com/cloud/clusters/data-service/about-buckets-scopes-collections.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |
| scopeNamerequired      | string Example: inventoryThe name of the scope.                                                          |

##### Request Body schema: application/json

| namerequired | string The name of the collection. The name should adhere to the following rules: The name must be between 1 and 251 characters in length. The name can contain only the characters A-Z, a-z, 0-9, and the symbols \_, -, and %. The name cannot start with \_ or %. Note that scope and collection names are case-sensitive.                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| maxTTL       | integer Specify the time to live (TTL) value in seconds. Defines the duration (Seconds) for which the documents in a collection are kept before automatic removal from the database. - For server versions < 7.6.0, this is a non-negative value. Set to 0 to use the bucket's maxTTL value. - For server versions >= 7.6.0, this value should be >= -1\. Set to -1 to disable expiry for that collection. Set to 0 to use the bucket's maxTTL value. - The maximum value that can be set for maxTTL is 2147483647. |

### Responses

**201** 

Successfully created a collection.

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/scopes/{scopeName}/collections

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/scopes/{scopeName}/collections

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "name": "my-collection",
* "maxTTL": 100
}`

### Response samples 

* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Buckets-Scopes-and-Collections/operation/getCollections)List Collections 

Lists all the collections in a scope.

To learn more about scopes and collections, see [Buckets, Scopes, and Collections](https://docs.couchbase.com/cloud/clusters/data-service/about-buckets-scopes-collections.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |
| scopeNamerequired      | string Example: inventoryThe name of the scope.                                                          |

### Responses

**200** 

Successfully listed all the collections in a scope in the bucket.

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/scopes/{scopeName}/collections

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/scopes/{scopeName}/collections

### Response samples 

* 200
* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "name": "airport",
    * "maxTTL": 0  
  }  
]
}`

## [](#tag/Buckets-Scopes-and-Collections/operation/getCollectionByName)Get Collection 

Fetches the details of the given collection.

To learn more about scopes and collections, see [Buckets, Scopes, and Collections](https://docs.couchbase.com/cloud/clusters/data-service/about-buckets-scopes-collections.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |
| scopeNamerequired      | string Example: inventoryThe name of the scope.                                                          |
| collectionNamerequired | string Example: airlineThe name of the collection.                                                       |

### Responses

**200** 

Successfully fetched the collection by its name.

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/scopes/{scopeName}/collections/{collectionName}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/scopes/{scopeName}/collections/{collectionName}

### Response samples 

* 200
* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "name": "airport",
* "maxTTL": 0
}`

## [](#tag/Buckets-Scopes-and-Collections/operation/putCollection)Update Collection 

Updates an existing collection.

This operation is only allowed for a cluster with server version >= 7.6.0\. A collection cannot be updated for the server versions lower than this.

This allows to update the maxTTL of the given collection.

To learn more about scopes and collections, see [Buckets, Scopes, and Collections](https://docs.couchbase.com/cloud/clusters/data-service/about-buckets-scopes-collections.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |
| scopeNamerequired      | string Example: inventoryThe name of the scope.                                                          |
| collectionNamerequired | string Example: airlineThe name of the collection.                                                       |

##### Request Body schema: application/json

| maxTTLrequired | integer Specify the new time to live (TTL) value in seconds. This value should be >= -1\. Set to -1 to disable expiry for that collection. Set to 0 to use the bucket's maxTTL value. The maximum value that can be set for maxTTL is 2147483647. A collection that is linked with an App Endpoint cannot have a TTL configured. |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**204** 

Successfully accepted updated collection configuration.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/scopes/{scopeName}/collections/{collectionName}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/scopes/{scopeName}/collections/{collectionName}

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "maxTTL": 100
}`

### Response samples 

* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Buckets-Scopes-and-Collections/operation/deleteCollectionByName)Delete Collection 

Deletes an existing collection.

To learn more about scopes and collections, see [Buckets, Scopes, and Collections](https://docs.couchbase.com/cloud/clusters/data-service/about-buckets-scopes-collections.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |
| scopeNamerequired      | string Example: inventoryThe name of the scope.                                                          |
| collectionNamerequired | string Example: airlineThe name of the collection.                                                       |

### Responses

**204** 

Successfully deleted the collection by its name.

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/scopes/{scopeName}/collections/{collectionName}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/{bucketId}/scopes/{scopeName}/collections/{collectionName}

### Response samples 

* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Certificates)Certificates

Couchbase Capella supports the use of x.509 certificates, for clients and servers. This ensures that only approved users, applications, machines, and endpoints have access to system resources. Consequently, the mechanism can be used by Couchbase SDK clients to access Couchbase Services, and by source clusters that use XDCR to replicate data to target clusters. Clients can verify the identity of Couchbase Capella, thereby ensuring that they are not exchanging data with a rogue entity.

## [](#tag/Certificates/operation/getCertificate)Get Certificate 

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**200** 

Successfully returned a self-signed certificate.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/certificates

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/certificates

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "certificate": "-----BEGIN CERTIFICATE-----\nMIIDFTCCAf2gAwIBAgI[...]CSYBWaK0ofivA==\n-----END CERTIFICATE-----\n"
}`

## [](#tag/Cloud-Snapshot-Backups-and-Restore)Cloud Snapshot Backups & Restore

Couchbase supports a robust scheduled backup and retention time policy as part of an overall disaster recovery plan for production data. Couchbase Capella supports scheduled and on-demand backups of cloud snapshot data. A backup can be restored to the same database where it was created or another database in the same organization. A backup can also be cloned to create a new database with the same specifications as the backed up cluster in the same organization. An on-demand backup of a bucket is always a Full backup. Capella schedules on-demand backup to start immediately.

## [](#tag/Cloud-Snapshot-Backups-and-Restore/operation/createCloudSnapshotBackup)Create Cloud Snapshot Backup 

Creates a cloud snapshot backup for a cluster.

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/cloud-snapshots.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| retention     | integer Represents interval in hours to retain the backup.                                                                                                               |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| regionsToCopy | Array of strings Specifies the regions where the backup will be copied. A maximum of two regions can be selected. If not provided, the backup will remain single-region. |

### Responses

**202** 

Successfully created a cloud snapshot backup for a cluster.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cloudsnapshotbackups

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cloudsnapshotbackups

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "retention": 168,
* "regionsToCopy": [
  * "us-west-1",
  * "us-east-1"  
]
}`

### Response samples 

* 202
* 403
* 404
* 409
* 429
* 500

Content type

application/json

Copy

`{
* "backupId": "IS9DrRsw4KWFS72Zhbj4xmhllHvPcdCL"
}`

## [](#tag/Cloud-Snapshot-Backups-and-Restore/operation/listCloudSnapshotBackups)List Cloud Snapshot Backups 

List the backups belonging to a cluster.

Note: This endpoint doesn't return queued backups and only returns ones that are actively being processed or are completed/failed.

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/cloud-snapshots.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                                                                               |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                                                                     |
| sortBy        | Array of strings Example: sortBy=createdAtSets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **id**, **createdAt**, **expiration**, **retention**, **sizee**, **type**. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                                                                            |

### Responses

**200** 

Successfully listed the backups belonging to a cluster.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cloudsnapshotbackups

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cloudsnapshotbackups

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "cursor": {
  * "hrefs": { },
  * "pages": {
    * "last": 1,
    * "page": 1,
    * "perPage": 5,
    * "totalItems": 5  
  }  
},
* "data": [
  * {
    * "data": {
      * "clusterId": "49b2c7f7-9612-4c99-b202-d4067b276b89",
      * "createdAt": "2023-11-25T13:02:32.409980126Z",
      * "expiration": "2023-12-25T13:02:32.409980126Z",
      * "id": "42bf3a6c-ebd9-495f-a391-57708b8c267d",
      * "progress": {
        * "status": "complete",
        * "time": "2024-01-18T10:47:18Z"  
            },
      * "projectId": "39387120-0a23-41bf-8d53-9048e6080dd1",
      * "retention": 604800000000000,
      * "cmek": [
        * {
          * "id": "ffffffff-aaaa-1414-eeee-000000000000",
          * "providerId": "example-arn-1"  
                    }  
            ],
      * "server": "7.2.3",
      * "size": 127569288,
      * "tenantId": "10f52cbd-8367-47f8-a840-e692339b4b04",
      * "type": "on_demand"  
      },
    * "permissions": {
      * "create": {
        * "accessible": true  
            },
      * "delete": {
        * "accessible": true  
            },
      * "read": {
        * "accessible": true  
            },
      * "update": {
        * "accessible": true  
            }  
      }  
  },
  * {
    * "data": {
      * "clusterId": "49b2c7f7-9612-4c99-b202-d4067b276b89",
      * "createdAt": "2023-11-25T13:02:32.409980126Z",
      * "expiration": "2023-12-25T13:02:32.409980126Z",
      * "id": "42bf3a6c-ebd9-495f-a391-57708b8c267d",
      * "progress": {
        * "status": "pending",
        * "time": "2024-01-18T10:47:18Z"  
            },
      * "projectId": "39387120-0a23-41bf-8d53-9048e6080dd1",
      * "retention": 604800000000000,
      * "cmek": [
        * {
          * "id": "ffffffff-aaaa-1414-eeee-000000000000",
          * "providerId": "example-arn-1"  
                    },
        * {
          * "id": "ffffffff-aaaa-1414-eeee-000000000000",
          * "providerId": "example-arn-2"  
                    }  
            ],
      * "crossRegionCopies": [
        * {
          * "regionCode": "us-west-2",
          * "status": "complete",
          * "time": "2024-01-18T10:48:18Z"  
                    },
        * {
          * "regionCode": "ap-southeast-4",
          * "status": "complete",
          * "time": "2024-01-18T10:49:21Z"  
                    }  
            ],
      * "server": "7.2.3",
      * "databaseSize": 127569,
      * "tenantId": "10f52cbd-8367-47f8-a840-e692339b4b04",
      * "type": "scheduled"  
      },
    * "permissions": {
      * "create": {
        * "accessible": true  
            },
      * "delete": {
        * "accessible": true  
            },
      * "read": {
        * "accessible": true  
            },
      * "update": {
        * "accessible": true  
            }  
      }  
  }  
],
* "permissions": {
  * "create": {
    * "accessible": true  
  },
  * "delete": {
    * "accessible": true  
  },
  * "read": {
    * "accessible": true  
  },
  * "update": {
    * "accessible": true  
  }  
}
}`

## [](#tag/Cloud-Snapshot-Backups-and-Restore/operation/listCloudSnapshotRestores)List Cloud Snapshot Restores 

Lists the restores that have taken place for a given cluster.

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/cloud-snapshots.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                                                                               |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                                                                     |
| sortBy        | Array of strings Example: sortBy=createdAtSets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **id**, **createdAt**, **expiration**, **retention**, **sizee**, **type**. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                                                                            |

### Responses

**200** 

Successfully listed the cloud snapshot restores belonging to a cluster.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cloudsnapshotbackups/restores

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cloudsnapshotbackups/restores

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "cursor": {
  * "hrefs": { },
  * "pages": {
    * "last": 1,
    * "page": 1,
    * "perPage": 5,
    * "totalItems": 5  
  }  
},
* "data": [
  * {
    * "data": {
      * "clusterId": "49b2c7f7-9612-4c99-b202-d4067b276b89",
      * "createdAt": "2023-11-25T13:02:32.409980126Z",
      * "expiration": "2023-12-25T13:02:32.409980126Z",
      * "id": "42bf3a6c-ebd9-495f-a391-57708b8c267d",
      * "progress": {
        * "status": "complete",
        * "time": "2024-01-18T10:47:18Z"  
            },
      * "projectId": "39387120-0a23-41bf-8d53-9048e6080dd1",
      * "retention": 604800000000000,
      * "server": "7.2.3",
      * "size": 127569288,
      * "tenantId": "10f52cbd-8367-47f8-a840-e692339b4b04",
      * "type": "on_demand"  
      },
    * "permissions": {
      * "create": {
        * "accessible": true  
            },
      * "delete": {
        * "accessible": true  
            },
      * "read": {
        * "accessible": true  
            },
      * "update": {
        * "accessible": true  
            }  
      }  
  },
  * {
    * "data": {
      * "clusterId": "49b2c7f7-9612-4c99-b202-d4067b276b89",
      * "createdAt": "2023-11-25T13:02:32.409980126Z",
      * "expiration": "2023-12-25T13:02:32.409980126Z",
      * "id": "42bf3a6c-ebd9-495f-a391-57708b8c267d",
      * "progress": {
        * "status": "pending",
        * "time": "2024-01-18T10:47:18Z"  
            },
      * "projectId": "39387120-0a23-41bf-8d53-9048e6080dd1",
      * "retention": 604800000000000,
      * "server": "7.2.3",
      * "size": 127569288,
      * "tenantId": "10f52cbd-8367-47f8-a840-e692339b4b04",
      * "type": "scheduled"  
      },
    * "permissions": {
      * "create": {
        * "accessible": true  
            },
      * "delete": {
        * "accessible": true  
            },
      * "read": {
        * "accessible": true  
            },
      * "update": {
        * "accessible": true  
            }  
      }  
  }  
],
* "permissions": {
  * "create": {
    * "accessible": true  
  },
  * "delete": {
    * "accessible": true  
  },
  * "read": {
    * "accessible": true  
  },
  * "update": {
    * "accessible": true  
  }  
}
}`

## [](#tag/Cloud-Snapshot-Backups-and-Restore/operation/ListGeographicRegions)List Available Geographic Regions for Cross-region Operations 

Lists the geographic regions where replicas of original backups can be stored, to ensure global availability and robust disaster recovery.

These regions can also be used for cross-region restores between clusters or for deploying new clusters in any listed region using backup data from every region included in the response.

At present, cross-region backups and restores are supported only for AWS and Azure clusters.

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/cloud-snapshots.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**200** 

Successfully lists the available geographic regions for cross-region cloud snapshot backups and restores.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**501** 

The server does not support the functionality required to fulfill the request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cloudsnapshotbackups/regions

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cloudsnapshotbackups/regions

### Response samples 

* 200
* 403
* 404
* 429
* 500
* 501

Content type

application/json

Copy

`[
* "af-south-1",
* "ap-east-1",
* "ap-northeast-1",
* "ap-northeast-2",
* "ap-south-1",
* "ap-south-2",
* "ap-southeast-1",
* "ap-southeast-2",
* "ap-southeast-3",
* "ap-southeast-4",
* "ca-central-1",
* "eu-central-1",
* "eu-central-2",
* "eu-north-1",
* "eu-south-1",
* "eu-west-1",
* "eu-west-2",
* "eu-west-3",
* "il-central-1",
* "me-central-1",
* "me-south-1",
* "sa-east-1",
* "us-east-1",
* "us-east-2",
* "us-west-2"
]`

## [](#tag/Cloud-Snapshot-Backups-and-Restore/operation/editCloudSnapshotBackupRetention)Edit Backup Retention 

Edits the retention time for a backup.

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/cloud-snapshots.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| backupIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the backup.       |

##### Request Body schema: application/json

| retention | integer Represents interval in hours to retain the backup. |
| --------- | ---------------------------------------------------------- |

### Responses

**204** 

Successfully edited backup retention time.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cloudsnapshotbackups/{backupId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cloudsnapshotbackups/{backupId}

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "retention": 730
}`

### Response samples 

* 403
* 404
* 409
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Cloud-Snapshot-Backups-and-Restore/operation/deleteCloudSnapshotBackup)Delete Backup 

Deletes the backup.

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/cloud-snapshots.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| backupIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the backup.       |

### Responses

**202** 

Successfully deleted the backup.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cloudsnapshotbackups/{backupId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cloudsnapshotbackups/{backupId}

### Response samples 

* 202
* 403
* 404
* 409
* 422
* 429
* 500

Content type

application/json

Copy

`{ }`

## [](#tag/Cloud-Snapshot-Backups-and-Restore/operation/restore)Restore Backup 

Creates a restore job for a backup immediately.

When multiple cross-regional cloud snapshots are available, a region of preference can be specified within the request payload to ensure optimal recovery in scenarios where the original snapshot in the cluster's primary region is not restorable. In such cases, cross-regional copies serve as a reliable fallback to maintain data availability and minimize downtime. Selecting the geographically closest cross-regional snapshot among the available options helps reduce latency during data retrieval and significantly lowers data transfer costs due to shorter network paths.

If no preferred region order is specified, the system automatically selects the most suitable snapshot based on availability.

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/cloud-snapshots.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| backupIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the backup.       |

##### Request Body schema: application/json

| crossRegionRestorePreference | Array of strings unique Defines the priority order of cross-regional cloud snapshots, based on the index of the array, to be used as a fallback for cluster restoration when the primary backup in the cluster's region is not restorable. The first region in the list is assigned the highest priority, followed by each subsequent region in order. |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### Responses

**202** 

Successfully triggered a restore of a cluster.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cloudsnapshotbackups/{backupId}/restore

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cloudsnapshotbackups/{backupId}/restore

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "crossRegionRestorePreference": [
  * "us-east-1",
  * "ap-southeast-4"  
]
}`

### Response samples 

* 202
* 400
* 403
* 404
* 409
* 429
* 500

Content type

application/json

Copy

`{
* "restoreId": "IS9DrRsw4KWFS72Zhbj4xmhllHvPcdCL"
}`

## [](#tag/Cloud-Snapshot-Backups-and-Restore/operation/listProjectLevelCloudSnapshotBackups)List Cloud Snapshot Backups at the Project Level 

Lists cloud snapshot backups associated with operational clusters within a specific project.

The "most recent" and "oldest" backup fields do not include backups that are in a queued state. Only backups that are actively being processed, successfully completed, or marked as failed are returned.

For detailed guidance on backup and restore functionality, please refer to [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/cloud-snapshots.html).

The provided API key must have at least one of the following roles.

* Organization Owner
* Project Owner
* Project Manager

For more information about roles and access, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                                                                                                                                                                                                                                                                             |
| sortBy        | Array of stringsItems Enum: "creationDateTime" "createdBy" "currentStatus" "cloudProvider" "region" Example: sortBy=creationDateTimeSpecifies the sorting criteria for the results, including the key by which the results should be ordered. Valid fields to sort the results include the following. - **creationDateTime** \- **createdBy** \- **currentStatus** \- **cloudProvider** \- **region**Provide the desired fields in the order of sorting preference. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                                                                                                                                                                                                                                                                                    |

### Responses

**200** 

Successful retrieval of the list of backups associated with the clusters within the project.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/cloudsnapshotbackups

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/cloudsnapshotbackups

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "clusterId": "ffffffff-aaaa-1414-eeee-000000000000",
    * "clusterName": "example-cluster",
    * "creationDateTime": "2024-11-14T14:14:22.122057304Z",
    * "createdBy": "user@company.com",
    * "currentStatus": "healthy",
    * "cloudProvider": "hostedAWS",
    * "region": "us-east-1",
    * "mostRecentSnapshot": {
      * "clusterId": "string",
      * "createdAt": "2019-08-24T14:15:22Z",
      * "expiration": "2019-08-24T14:15:22Z",
      * "id": "string",
      * "progress": {
        * "status": "string",
        * "time": "2019-08-24T14:15:22Z"  
            },
      * "projectId": "string",
      * "appService": "3.141.5",
      * "cmek": [
        * {
          * "id": "ffffffff-aaaa-1414-eeee-000000000000",
          * "providerId": "arn:aws:kms:us-west-1:123456789012:key/abcd1234-a123-456a-a12b-a123b4cd56ef"  
                    }  
            ],
      * "crossRegionCopies": [
        * {
          * "regionCode": "string",
          * "status": "string",
          * "time": "2019-08-24T14:15:22Z"  
                    }  
            ],
      * "retention": 0,
      * "server": {
        * "version": "7.1"  
            },
      * "databaseSize": 0,
      * "tenantId": "string",
      * "type": "string"  
      },
    * "oldestSnapshot": {
      * "clusterId": "string",
      * "createdAt": "2019-08-24T14:15:22Z",
      * "expiration": "2019-08-24T14:15:22Z",
      * "id": "string",
      * "progress": {
        * "status": "string",
        * "time": "2019-08-24T14:15:22Z"  
            },
      * "projectId": "string",
      * "appService": "3.141.5",
      * "cmek": [
        * {
          * "id": "ffffffff-aaaa-1414-eeee-000000000000",
          * "providerId": "arn:aws:kms:us-west-1:123456789012:key/abcd1234-a123-456a-a12b-a123b4cd56ef"  
                    }  
            ],
      * "crossRegionCopies": [
        * {
          * "regionCode": "string",
          * "status": "string",
          * "time": "2019-08-24T14:15:22Z"  
                    }  
            ],
      * "retention": 0,
      * "server": {
        * "version": "7.1"  
            },
      * "databaseSize": 0,
      * "tenantId": "string",
      * "type": "string"  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/Cloud-Snapshot-Backups-and-Restore/operation/clone)Clone Cluster Backup 

Clones the cluster backup into a new cluster.

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/cloud-snapshots.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| backupIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the backup.       |

##### Request Body schema: application/json

| namerequired          | string <= 256 characters Name of the cloned cluster (up to 256 characters).                                                                                                                                                                                                                                                                                              |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| description           | string <= 1024 characters Description of the cloned cluster (up to 1024 characters).                                                                                                                                                                                                                                                                                     |
| cloudProviderrequired | object (CloudProvider) The cloud provider where the cluster will be hosted. For information about providers and supported regions, see: [Amazon Web Services](https://docs.couchbase.com/cloud/reference/aws.html) [Google Cloud Platform](https://docs.couchbase.com/cloud/reference/gcp.html) [Microsoft Azure](https://docs.couchbase.com/cloud/reference/azure.html) |
| availabilityrequired  | object (Availability)                                                                                                                                                                                                                                                                                                                                                    |
| supportrequired       | object (Support)                                                                                                                                                                                                                                                                                                                                                         |
| zones                 | Array of strings Zones is the cloud services provider availability zones for the cloned cluster. Currently Supported only for single AZ clusters so only 1 zone is allowed in list.                                                                                                                                                                                      |

### Responses

**202** 

Successfully triggered a clone of a cluster.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/cloudsnapshotbackups/{backupId}/clone

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/cloudsnapshotbackups/{backupId}/clone

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "name": "Cloned Cluster",
* "description": "This is a cloned cluster.",
* "cloudProvider": {
  * "type": "aws",
  * "region": "us-east-1",
  * "cidr": "10.1.30.0/23"  
},
* "availability": {
  * "type": "single"  
},
* "zones": [
  * "use1-az1"  
],
* "support": {
  * "plan": "developer pro",
  * "timezone": "PT"  
}
}`

### Response samples 

* 202
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "restoreId": "IS9DrRsw4KWFS72Zhbj4xmhllHvPcdCL",
* "clusterId": "IS9DrRsw4KWFS72Zhbj4xmhllHvPcdCL"
}`

## [](#tag/Cloud-Snapshot-Backups-Schedule)Cloud Snapshot Backups Schedule

Couchbase supports a robust scheduled backup and retention time policy as part of an overall disaster recovery plan for production data. Couchbase Capella supports scheduled and on-demand backups of cloud snapshot data. A backup can be restored to the same database where it was created or another database in the same organization. On setting up a backup schedule, the bucket automatically backs up the bucket based on the chosen schedule.

## [](#tag/Cloud-Snapshot-Backups-Schedule/operation/upsertCloudSnapshotBackupSchedule)Upsert Backup Schedule 

Creates or updates a cloud snapshot backup schedule for a cluster.

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/cloud-snapshots.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| interval      | integer Represents the time interval.                                                                                                                                                               |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| retention     | integer Represents interval in hours to retain the backup.                                                                                                                                          |
| startTime     | string <date-time\> Represents the start time in ISO 8601 format.                                                                                                                                   |
| copyToRegions | Array of strings Represents the list of geographical regions where snapshot copies to be stored in addition to the primary region. Currently, this feature is supported for AWS and Azure clusters. |

### Responses

**204** 

Successfully created or updated a backup schedule.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

**501** 

The server does not support the functionality required to fulfill the request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cloudsnapshotbackupschedule

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cloudsnapshotbackupschedule

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "interval": 1,
* "retention": 24,
* "startTime": "2024-01-05T16:00:00+00:00",
* "copyToRegions": [
  * "us-east-1",
  * "ap-southeast-4"  
]
}`

### Response samples 

* 400
* 403
* 404
* 409
* 429
* 500
* 501

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Cloud-Snapshot-Backups-Schedule/operation/getCloudSnapshotBackupSchedule)Get Backup Schedule 

Retrieves the cloud snapshot backup schedule for a cluster.

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/cloud-snapshots.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**200** 

Successfully retrieved the backup schedule.

**204** 

Cluster does not have a defined backup schedule.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cloudsnapshotbackupschedule

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cloudsnapshotbackupschedule

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "interval": 1,
* "retention": 24,
* "startTime": "2024-01-05T16:00:00+00:00",
* "copyToRegions": [
  * "us-east-1",
  * "ap-southeast-4"  
]
}`

## [](#tag/Cloud-Snapshot-Backups-Schedule/operation/deleteCloudSnapshotBackupSchedule)Delete Backup Schedule 

Deletes the backup schedule for a cluster.

To learn more about backup and restore, see [Backup and Restore Data](https://docs.couchbase.com/cloud/clusters/cloud-snapshots.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**204** 

Successfully deleted the backup schedule.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cloudsnapshotbackupschedule

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cloudsnapshotbackupschedule

### Response samples 

* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Clusters)Clusters

A Couchbase cluster consists of one or more instances of Couchbase Capella, each running on an independent node. Data and services are shared across the cluster. A cluster may be referred to as a "database" in the documentation and in the Couchbase Capella user interface.

## [](#tag/Clusters/operation/postCluster)Create Cluster 

Creates a new Couchbase Capella provisioned cluster.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

##### Request Body schema: application/json

| namerequired               | string <= 256 characters Name of the cluster (up to 256 characters).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| description                | string <= 1024 characters Description of the cluster (up to 1024 characters).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| configurationType          | string (ConfigurationType) Deprecated Default: "multiNode" Enum: "singleNode" "multiNode" Multi-node databases are best for deployments that require high availability. If your app requires high performance and high availability, choose the Multi-node option. Single-node databases have resource limitations that make them a good choice for learning, prototyping, and non-production uses. They have limited availability. Single-node databases should contain only 1 node and 1 Service Group. Adding number of nodes or service groups > 1 is not allowed for such databases. By default the configurationType is multiNode. |
| cloudProviderrequired      | object (CloudProvider) The cloud provider where the cluster will be hosted. For information about providers and supported regions, see: [Amazon Web Services](https://docs.couchbase.com/cloud/reference/aws.html) [Google Cloud Platform](https://docs.couchbase.com/cloud/reference/gcp.html) [Microsoft Azure](https://docs.couchbase.com/cloud/reference/azure.html)                                                                                                                                                                                                                                                                 |
| couchbaseServer            | object (CouchbaseServer)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| serviceGroupsrequired      | Array of objects (ServiceGroup) non-empty The couchbase service groups to be run. - The set of nodes that share the same disk, number of nodes and services. - At least one service group must contain the data service.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| availabilityrequired       | object (Availability)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| supportrequired            | object (Support)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| zones                      | Array of strings Zones is the cloud services provider availability zones for the cluster. Currently Supported only for single AZ clusters so only 1 zone is allowed in list.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| cmekId                     | string <uuid\> The ID of the CMEK Key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| enablePrivateDNSResolution | boolean EnablePrivateDNSResolution signals that the cluster should have hostnames that are hosted in a public DNS zone that resolve to a private DNS address. This exists to support the use case of customers connecting from their own data centers where it is not possible to make use of a cloud service provider DNS zone.                                                                                                                                                                                                                                                                                                         |

### Responses

**202** 

Successfully created a cluster.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters

### Request samples 

* Payload

Content type

application/json

Example

PostClusterAWSMultipleServiceGroupsPostClusterAWSSingleAvailabilityBasicPlanPostClusterAWSWithoutServerVersionPostClusterAWSWithServerVersionAndMaxNodesPostClusterAWSWithServerWithMaxNodesPostClusterAzurePremiumDiskPostClusterAzureUltraDiskPostClusterAzureWithAutoExpansionPostClusterGCPPostCMEKClusterPostClusterEnabledPrivateDNSResolutionPostClusterAWSMultipleServiceGroups

Copy

 Expand all  Collapse all 

`{
* "name": "Test-Cluster-1",
* "description": "My first test AWS cluster for multiple services.",
* "cloudProvider": {
  * "type": "aws",
  * "region": "us-east-1",
  * "cidr": "10.1.30.0/23"  
},
* "couchbaseServer": {
  * "version": "7.2"  
},
* "serviceGroups": [
  * {
    * "node": {
      * "compute": {
        * "cpu": 4,
        * "ram": 16  
            },
      * "disk": {
        * "storage": 50,
        * "type": "gp3",
        * "iops": 3000  
            }  
      },
    * "numOfNodes": 3,
    * "services": [
      * "data",
      * "query",
      * "index",
      * "search"  
      ]  
  },
  * {
    * "node": {
      * "compute": {
        * "cpu": 4,
        * "ram": 32  
            },
      * "disk": {
        * "storage": 50,
        * "type": "io2",
        * "iops": 3005  
            }  
      },
    * "numOfNodes": 2,
    * "services": [
      * "analytics"  
      ]  
  }  
],
* "availability": {
  * "type": "multi"  
},
* "support": {
  * "plan": "developer pro",
  * "timezone": "PT"  
}
}`

### Response samples 

* 202
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/Clusters/operation/listClusters)List Clusters 

Lists all the clusters under the organization.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

Returned set of clusters is reduced to what the caller has access to view. To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                                                                                             |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                                                                                   |
| sortBy        | Array of strings Example: sortBy=nameSets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **id**, **availability**, **cloudProvider**, **couchbaseServer**, **currentState**, **name**. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                                                                                          |

### Responses

**200** 

Successfully listed all the clusters under the organization.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "appServiceId": "ffffffff-aaaa-1414-eeee-000000000000",
    * "name": "Test Cluster",
    * "description": "Description of the cluster",
    * "configurationType": "multiNode",
    * "connectionString": "couchbases://cb.irxmynm6vekhe5.cloud.couchbase.com",
    * "cloudProvider": {
      * "type": "aws",
      * "region": "us-east-1",
      * "cidr": "10.1.30.0/23"  
      },
    * "couchbaseServer": {
      * "version": "7.1"  
      },
    * "serviceGroups": [
      * {
        * "node": {
          * "compute": {
            * "cpu": 4,
            * "ram": 16  
                              },
          * "disk": {
            * "type": "gp3",
            * "storage": 50,
            * "iops": 3000  
                              }  
                    },
        * "numOfNodes": 3,
        * "services": [
          * "data"  
                    ]  
            }  
      ],
    * "availability": {
      * "type": "single"  
      },
    * "support": {
      * "plan": "basic",
      * "timezone": "ET"  
      },
    * "currentState": "deploying",
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56Z",
      * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "modifiedAt": "2021-09-01T12:34:56Z",
      * "version": 1  
      },
    * "cmekId": "ffffffff-aaaa-1414-eeee-000000000000",
    * "enablePrivateDNSResolution": true,
    * "deletionProtection": false,
    * "expressScaling": "enabled"  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/Clusters/operation/getCluster)Get Cluster 

Fetches the details of the given cluster.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**200** 

Successfully fetched the cluster based on the clusterId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "appServiceId": "ffffffff-aaaa-1414-eeee-000000000000",
* "name": "Test Cluster",
* "description": "Description of the cluster",
* "configurationType": "multiNode",
* "connectionString": "couchbases://cb.irxmynm6vekhe5.cloud.couchbase.com",
* "cloudProvider": {
  * "type": "aws",
  * "region": "us-east-1",
  * "cidr": "10.1.30.0/23"  
},
* "couchbaseServer": {
  * "version": "7.1"  
},
* "serviceGroups": [
  * {
    * "node": {
      * "compute": {
        * "cpu": 4,
        * "ram": 16  
            },
      * "disk": {
        * "type": "gp3",
        * "storage": 50,
        * "iops": 3000  
            }  
      },
    * "numOfNodes": 3,
    * "services": [
      * "data"  
      ]  
  }  
],
* "availability": {
  * "type": "single"  
},
* "support": {
  * "plan": "basic",
  * "timezone": "ET"  
},
* "currentState": "deploying",
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
},
* "cmekId": "ffffffff-aaaa-1414-eeee-000000000000",
* "enablePrivateDNSResolution": true,
* "deletionProtection": false,
* "expressScaling": "enabled"
}`

## [](#tag/Clusters/operation/putCluster)Update Cluster 

Updates an existing cluster.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### header Parameters

| If-Match | string Example: 12A precondition header that specifies the entity tag of a resource. |
| -------- | ------------------------------------------------------------------------------------ |

##### Request Body schema: application/json

| namerequired          | string <= 256 characters The new name of the cluster (up to 256 characters).   |
| --------------------- | ------------------------------------------------------------------------------ |
| descriptionrequired   | string <= 1024 characters The new cluster description (up to 1024 characters). |
| supportrequired       | object (Support)                                                               |
| serviceGroupsrequired | Array of objects (ServiceGroup)                                                |

### Responses

**204** 

Successfully submitted request to update cluster.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "name": "My-New-Cluster",
* "description": "The extended description of my new cluster.",
* "support": {
  * "plan": "basic",
  * "timezone": "ET"  
},
* "serviceGroups": [
  * {
    * "node": {
      * "compute": {
        * "cpu": 4,
        * "ram": 16  
            },
      * "disk": {
        * "type": "gp3",
        * "storage": 50,
        * "iops": 3000  
            }  
      },
    * "numOfNodes": 3,
    * "services": [
      * "data"  
      ]  
  }  
]
}`

### Response samples 

* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Clusters/operation/deleteCluster)Delete Cluster 

Deletes an existing cluster.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### query Parameters

| retainsnapshotbackups | boolean Example: retainsnapshotbackups=trueRetain snapshot backups parameter specifies whether to retain snapshot backups after cluster deletion. |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**202** 

Successfully deleted the cluster by its clusterId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}

### Response samples 

* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Clusters/operation/getClusterStats)Get Cluster Capacity Statistics 

Fetches cluster-level capacity statistics including memory availability and replica limits.

This endpoint provides cluster capacity information that is not specific to any individual bucket, allowing clients to make informed decisions when managing buckets.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**200** 

Successfully fetched the cluster capacity statistics.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/stats

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/stats

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "freeMemoryInMb": 640,
* "totalMemoryInMb": 1040,
* "maxReplicas": 2
}`

## [](#tag/Clusters/operation/clusterOn)Turn On Cluster 

Turn cluster on.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| turnOnLinkedAppService | boolean Default: false Set this value to true if you want to turn on the app service linked with the cluster, false if not. If set to true, the app service, if present, will turn on with the cluster. Default value for this is false, which means the linked app service will be kept off. |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**202** 

Successfully switched the cluster to on state.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/activationState

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/activationState

### Request samples 

* Payload

Content type

application/json

Example

ClusterOnAppServiceOnClusterOnAppServiceOffClusterOnAppServiceOn

Copy

`{
* "turnOnLinkedAppService": true
}`

### Response samples 

* 403
* 404
* 409
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Clusters/operation/clusterOff)Turn Off Cluster 

Turn cluster off.

* Turning off your cluster turns off the compute for your cluster but the storage remains. All of the data, schema (buckets, scopes, and collections), and indexes remain, as well as cluster configuration, including users and allow lists.
* Turning off cluster will also turn off any linked app services.
* Turning off cluster will not stop charges being incurred for Data API.

 In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**202** 

Successfully switched the cluster to off state.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/activationState

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/activationState

### Response samples 

* 403
* 404
* 409
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Clusters/operation/putBucketStorageBackend)Migrate Buckets 

Updates the storage backend of an existing bucket from Couchstore to Magma.

The following should be noted while doing this operation -

1. The outcome of this migration is that all data service nodes in the cluster will be replaced.
* During the migration all buckets will remain operational and still be able to perform read and writes. Hence applications will not incur any downtime during this migration and can continue to read/write to the cluster.
* The re-balances that occur from the node replacements will result in the bucket(s) being migrated to Magma.
* The status of the cluster can be monitored via the [GET cluster API](https://docs.couchbase.com/cloud/management-api-reference/index.html#tag/clusters/operation/getCluster). The cluster will transition to healthy state after migration is completed for all listed buckets.
1. This operation is only allowed for clusters with server version >= 7.6.0\. The storage backend cannot be updated for the cluster with server versions lower than this. All the nodes must be upgraded to 7.6.0 before the bucket migration can be performed.
2. Before migrating from Couchstore to Magma, the bucket memory allocation should be upgraded to at least the minimum amount required for a Magma bucket that is 1024 MiB.
3. Cluster must be in a healthy state to perform this operation.

To learn more about bucket configuration, see [Buckets](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/buckets.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| bucketsrequired | Array of strings <= 30 items Names of the buckets which need to be migrated from Couchstore to Magma. |
| --------------- | ----------------------------------------------------------------------------------------------------- |

### Responses

**202** 

Successfully accepted updated storage backend for the bucket.

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/bucketStorageMigration

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/bucketStorageMigration

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "buckets": [
  * "sample-bucket",
  * "my-bucket"  
]
}`

### Response samples 

* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Clusters/operation/putClusterDeletionProtection)Update Deletion Protection 

Enable or disable deletion protection for a cluster.

When deletion protection is enabled, the cluster, its app service, and its buckets cannot be deleted, and bucket data cannot be flushed.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| deletionProtectionrequired | boolean Set to true to enable deletion protection for the cluster, false to disable it. When enabled, the cluster, its app service, and its buckets cannot be deleted, and bucket data cannot be flushed. |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**204** 

Successfully updated deletion protection setting.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/deletionProtection

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/deletionProtection

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "deletionProtection": true
}`

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/CMEK)CMEK

The CMEK (Customer Managed Encryption Keys) endpoints facilitate the management of encryption keys used by clusters for data encryption. They allow organizations to register, list, retrieve, rotate, and delete the metadata associated with their own encryption keys within Capella. This suite of endpoints ensures that organizations have full control over the lifecycle of their keys, enhancing security and compliance by allowing encryption keys that are managed in external key management services like AWS KMS or GCP KMS to be used within the organization's clusters.

## [](#tag/CMEK/operation/getCloudAccounts)Get Cloud Accounts 

Fetches the cloud account ID associated with the organization. Use this account ID when adding CMEK to other AWS databases in your organization.

To learn more, see [CMEK at Rest](https://docs.couchbase.com/cloud/security/cmek.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Creator
* Organization Member

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

### Responses

**200** 

Successfully fetched the cloud account ID associated with the organization.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/cloudAccounts

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/cloudAccounts

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "gcp-capella-project": "MyApp-Prod-Project",
* "aws-capella-account": "MyApp-Prod-Project",
* "azure-capella-subscription": "MyApp-Prod-Project"
}`

## [](#tag/CMEK/operation/getAzureApplicationID)Get Azure Application ID 

Retrieves the application ID so that the customer can install the service principal in their Azure tenant.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Organization Member

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

### Responses

**200** 

Successfully retrieved the Azure application ID.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/cmekAzureApplication

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/cmekAzureApplication

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/CMEK/operation/getAzureApplicationIDForProject)Get Azure Application ID For Project 

Retrieves the application ID so that the customer can install the service principal in their Azure tenant for a specific project.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Organization Member
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

### Responses

**200** 

Successfully retrieved the Azure application ID for a project.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/cmekAzureApplication

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/cmekAzureApplication

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/CMEK/operation/postCMEKMetadata)Create Key Metadata 

Initializes the metadata record for a customer-managed encryption key stored in AWS, GCP or Azure, linking it to the organization.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| namerequired   | string <= 128 characters Name of the key (up to 256 characters).         |
| -------------- | ------------------------------------------------------------------------ |
| description    | string <= 512 characters Description of the key (up to 1024 characters). |
| configrequired | AWSConfig (object) or GCPConfig (object) or AzureConfig (object)         |

### Responses

**200** 

Successfully created the encryption key metadata.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/cmek

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/cmek

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "name": "Test Key",
* "description": "Description of the Key",
* "config": {
  * "arn": "arn:aws:kms:us-west-2:123456789012:key/abcd1234-a123-456a-a12b-a123b4cd56ef"  
}
}`

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/CMEK/operation/getKeyMetadataList)List Key Metadata 

Retrieves detailed metadata for all customer-managed encryption keys associated with the organization.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Organization Member

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                               |
| sortBy        | Array of strings Example: sortBy=nameSets the order of how you would like to sort the results and the key you would like to order by. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                      |

### Responses

**200** 

Successfully listed the detailed metadata for all encryption keys associated with the organization.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/cmek

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/cmek

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "name": "Test Key",
    * "description": "Description of the cluster",
    * "config": {
      * "arn": "arn:aws:kms:us-west-2:123456789012:key/abcd1234-a123-456a-a12b-a123b4cd56ef"  
      },
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56Z",
      * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "modifiedAt": "2021-09-01T12:34:56Z",
      * "version": 1  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/CMEK/operation/postCMEKAzureMetadataForProject)Create Azure Key Metadata For Project 

Initializes the metadata record for a customer-managed encryption key stored for a project. This only applies to Azure.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

##### Request Body schema: application/json

| namerequired   | string <= 256 characters Name of the key.         |
| -------------- | ------------------------------------------------- |
| description    | string <= 1024 characters Description of the key. |
| configrequired | object (AzureConfig)                              |

### Responses

**201** 

Successfully created the encryption key metadata.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/cmek

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/cmek

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "name": "Test Key",
* "description": "Description of the Key",
* "config": {
  * "keyLocation": "<https://my-vault.vault.azure.net/keys/my-key/846dec161545466586fd1f19849dd1ef>",
  * "region": "eastus"  
}
}`

### Response samples 

* 201
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/CMEK/operation/getAzureKeyMetadataListForProject)List Azure Key Metadata For Project 

Retrieves detailed metadata for all Azure customer-managed encryption keys associated with the project.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                               |
| sortBy        | Array of strings Example: sortBy=nameSets the order of how you would like to sort the results and the key you would like to order by. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                      |

### Responses

**200** 

Successfully listed the detailed metadata for all Azure encryption keys associated with the project.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/cmek

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/cmek

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "name": "Test Key",
    * "description": "Description of the cluster",
    * "config": {
      * "keyLocation": "<https://my-vault.vault.azure.net/keys/my-key/846dec161545466586fd1f19849dd1ef>",
      * "region": "eastus"  
      },
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56Z",
      * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "modifiedAt": "2021-09-01T12:34:56Z",
      * "version": 1  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/CMEK/operation/listCMEKHistory)List Key Rotation History 

Retrieves the full history of rotations for a specific customer-managed encryption key within the organization. In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Organization Member To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.     |
| ---------------------- | ------------------------------------------------------------------------------------------------- |
| cmekIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the KMS Key metadata. |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                                                                                                  |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                                                                                        |
| sortBy        | string Enum: "active" "associatedAt" "associatedBy" "key" Example: sortBy=activeSets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **active**, **associatedAt**, **associatedBy**, **key** |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                                                                                               |

### Responses

**200** 

Successfully fetched the key rotation history based on its ID.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/cmek/{cmekId}/history

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/cmek/{cmekId}/history

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "cursor": {
  * "hrefs": { },
  * "pages": {
    * "last": 1,
    * "page": 1,
    * "perPage": 2,
    * "totalItems": 2  
  }  
},
* "data": [
  * {
    * "config": {
      * "arn": "arn:aws:kms:us-west-2:123456789012:key/12345678-1234-1234-1234-123456789012"  
      },
    * "active": true,
    * "associatedBy": "ffffffff-aaaa-1414-eeee-000000000000",
    * "associatedAt": "2023-09-01T12:34:56Z"  
  },
  * {
    * "config": {
      * "arn": "arn:aws:kms:us-west-2:000000000000:key/00000000-0000-0000-0000-000000000000"  
      },
    * "active": false,
    * "associatedBy": "ffffffff-aaaa-1414-eeee-000000000000",
    * "associatedAt": "2023-09-01T12:34:56Z"  
  }  
]
}`

## [](#tag/CMEK/operation/getKeyMetadata)Get Key Metadata 

Retrieves the full metadata details for a specific customer-managed encryption key within the organization.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Organization Member

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.     |
| ---------------------- | ------------------------------------------------------------------------------------------------- |
| cmekIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the KMS Key metadata. |

### Responses

**200** 

Successfully fetched the encryption key details based on its ID.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/cmek/{cmekId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/cmek/{cmekId}

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "name": "Test Key",
* "description": "Description of the cluster",
* "config": {
  * "arn": "arn:aws:kms:us-west-2:123456789012:key/abcd1234-a123-456a-a12b-a123b4cd56ef"  
},
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
}
}`

## [](#tag/CMEK/operation/rotateCMEKKey)Rotate Key 

Initiates the process to rotate a customer-managed encryption key and update its associated metadata within the system.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.     |
| ---------------------- | ------------------------------------------------------------------------------------------------- |
| cmekIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the KMS Key metadata. |

##### Request Body schema: application/json

| configrequired | AWSConfig (object) or GCPConfig (object) or AzureConfig (object) |
| -------------- | ---------------------------------------------------------------- |

### Responses

**204** 

Successfully submitted request to rotate the encryption key.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/cmek/{cmekId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/cmek/{cmekId}

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "config": {
  * "arn": "arn:aws:kms:us-west-2:123456789012:key/abcd1234-a123-456a-a12b-a123b4cd56ef"  
}
}`

### Response samples 

* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/CMEK/operation/deleteKeyMetadata)Delete Key Metadata 

Permanently removes the specified customer-managed encryption key's metadata from the organization's account.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.     |
| ---------------------- | ------------------------------------------------------------------------------------------------- |
| cmekIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the KMS Key metadata. |

### Responses

**204** 

Successfully deleted the the specified encryption key's metadata by its ID.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/cmek/{cmekId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/cmek/{cmekId}

### Response samples 

* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/CMEK/operation/getAzureKeyMetadataForProject)Get Azure Key Metadata For Project 

Retrieves the full metadata details for a specific Azure customer-managed encryption key in a project.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.     |
| ---------------------- | ------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.          |
| cmekIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the KMS Key metadata. |

### Responses

**200** 

Successfully fetched the encryption key details based on its ID in a project.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/cmek/{cmekId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/cmek/{cmekId}

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "name": "Test Key",
* "description": "Description of the cluster",
* "config": {
  * "keyLocation": "<https://my-vault.vault.azure.net/keys/my-key/846dec161545466586fd1f19849dd1ef>",
  * "region": "eastus"  
},
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
}
}`

## [](#tag/CMEK/operation/rotateAzureKeyMetadataForProject)Rotate Azure Key For Project 

Initiates the process to rotate an Azure customer-managed encryption key in a project and update its associated metadata within the system.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.     |
| ---------------------- | ------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.          |
| cmekIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the KMS Key metadata. |

##### Request Body schema: application/json

| configrequired | object (AzureConfig) |
| -------------- | -------------------- |

### Responses

**204** 

Successfully submitted request to rotate the encryption key.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/cmek/{cmekId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/cmek/{cmekId}

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "config": {
  * "keyLocation": "<https://my-vault.vault.azure.net/keys/my-key/846dec161545466586fd1f19849dd1ef>",
  * "region": "eastus"  
}
}`

### Response samples 

* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/CMEK/operation/deleteAzureKeyMetadataForProject)Delete Azure Key Metadata For Project 

Permanently removes the specified Azure customer-managed encryption key's metadata from the project.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.     |
| ---------------------- | ------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.          |
| cmekIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the KMS Key metadata. |

### Responses

**204** 

Successfully deleted the specified encryption key's metadata by its ID in a project.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/cmek/{cmekId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/cmek/{cmekId}

### Response samples 

* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/CMEK/operation/enableCMEK)Enable CMEK For Cloud Services Provider 

Enables the customer-managed encryption keys feature for the specified cloud service provider within the organization.

For AWS and GCP enabling the customer-managed encryption keys feature is only required if no AWS or GCP cluster respectively has ever been created in the organization.

The customer-managed encryption keys feature must always be enabled for Azure before Azure keys can be created. This operation provisions a multi-tenant Azure Entra ID application for the organization, which is required for Capella to access customer-managed encryption keys.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| cloudProviderrequired | string Enum: "aws" "gcp" "azure" Cloud provider for CMEK keys. |
| --------------------- | -------------------------------------------------------------- |

### Responses

**204** 

Successfully enabled the CMEK feature for the cloud services provider.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/cmek/providers

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/cmek/providers

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "cloudProvider": "aws"
}`

### Response samples 

* 400
* 403
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/CMEK/operation/enableCMEKAzureProject)Enable Azure CMEK For Project 

Enables the customer-managed encryption keys feature for Azure on a project.

The customer-managed encryption keys feature must always be enabled for Azure before Azure keys can be created. This operation provisions a multi-tenant Azure Entra ID application for a project, which is required for Capella to access customer-managed encryption keys.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

##### Request Body schema: application/json

| cloudProviderrequired | string Value: "azure" Cloud provider for CMEK keys. |
| --------------------- | --------------------------------------------------- |

### Responses

**204** 

Successfully enabled the Azure CMEK feature for a project.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/cmek/providers

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/cmek/providers

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "cloudProvider": "azure"
}`

### Response samples 

* 400
* 403
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/CMEK/operation/AssociateCMEK)Associate Key with Cluster 

Redeploys the cluster and encrypts the disks with the newly associated customer-managed encryption key. Throws an error before redeploying the cluster if the customer-managed encryption key is inaccessible.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.     |
| ---------------------- | ------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.          |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.          |
| cmekIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the KMS Key metadata. |

### Responses

**204** 

Successfully associated the key with the cluster and encrypted the disks.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cmek/{cmekId}/associate

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cmek/{cmekId}/associate

### Response samples 

* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/CMEK/operation/UnassociateCMEK)Unassociate Key from Cluster 

Removes the customer-managed encryption key associated with the cluster, which redeploys the cluster and removes any encryption on the disks. This does not delete the customer-managed encryption key itself since the same key could be used across clusters.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.     |
| ---------------------- | ------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.          |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.          |
| cmekIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the KMS Key metadata. |

### Responses

**204** 

Successfully disassociated the key from the cluster and removed encryption.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cmek/{cmekId}/unassociate

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/cmek/{cmekId}/unassociate

### Response samples 

* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Data-API)Data API

Data API is a RESTful interface that allows users to access and manipulate data in your Couchbase Capella cluster.

## [](#tag/Data-API/operation/updateDataApiAndPeering)Update Data API 

Enable or disable Data API on your cluster. Additional charges will be incurred when this feature is enabled. Enabling data API is an asynchronous call and can take several minutes depending on the CSP.

You can also enable network peering when enabling Data API. If network peering is enabled, please complete setup by using commands returned in GET /networkPeers/{peerId} endpoint.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Manager
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| enableDataApirequired        | boolean Default: false enable or disable Data API for the cluster.                 |
| ---------------------------- | ---------------------------------------------------------------------------------- |
| enableNetworkPeeringrequired | boolean Default: false enable or disable network peering when Data API is enabled. |

### Responses

**202** 

Successfully submitted request to enable Data API. Use the GET /dataAPI endpoint to monitor the status of the request.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/dataAPI

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/dataAPI

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "enableDataApi": true,
* "enableNetworkPeering": true
}`

### Response samples 

* 400
* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Data-API/operation/getDataAPIStatus)Get Data API Status 

Get the status of Data API and network peering on your cluster.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**200** 

Successfully retrieved data API and network peering status of cluster.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/dataAPI

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/dataAPI

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "enabled": true,
* "state": "enabled",
* "enabledForNetworkPeering": true,
* "stateForNetworkPeering": "enabled",
* "connectionString": "<https://dpmr2ygad6rwzvsf.data.cloud.couchbase.com>"
}`

## [](#tag/Data-API/operation/getDataAPIPrivateEndpointCommand)Get CLI Commands For Setting Up Private Endpoint Connection 

Retrieve the command or script to be executed in order to create the private endpoint which will provides a private connection between the specified VPC and the specified Capella Data API Endpoint. An example for AWS:

```
aws ec2 create-vpc-endpoint \
  --vpc-id vpc-1234 \
  --region us-east-1 \
  --service-name com.amazonaws.vpce.us-east-1.vpce-svc-1234 \
  --vpc-endpoint-type Interface \
  --subnet-ids subnet-1234

```

An example for Azure:

```
az network private-endpoint create \
  --connection-name connection-1 \
  --name private-endpoint \
  --private-connection-resource-id svc-1 \
  --resource-group test-rg \
  --subnet subnet-1 \
  --group-id sites \
  --vnet-name vnet-1

```

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

One of 

CreateVPCEndpointCommandRequestCreateAzurePrivateEndpointCommandRequest

| vpcIDrequired     | string \[ 12 .. 21 \] characters The ID of your virtual network |
| ----------------- | --------------------------------------------------------------- |
| subnetIDsrequired | Array of strings                                                |

### Responses

**200** 

Successfully returned command to establish a private connection to Data API endpoint.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/dataAPI/privateEndpointCommand

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/dataAPI/privateEndpointCommand

### Request samples 

* Payload

Content type

application/json

Example

PostAWSCommandRequestPostAzureCommandRequestPostAWSCommandRequest

Copy

 Expand all  Collapse all 

`{
* "vpcID": "vpc-1234",
* "subnetIDs": [
  * "subnet-1234"  
]
}`

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "command": "aws ec2 create-vpc-endpoint --vpc-id vpc-1234 --region us-east-1 --service-name com.amazonaws.vpce.us-east-1.vpce-svc-1234 --vpc-endpoint-type Interface --subnet-ids subnet-1234"
}`

## [](#tag/Data-API/operation/listDataAPIPrivateEndpoints)List Data API Private Endpoints 

Returns a list of Data API private endpoints associated with your Capella cluster, along with the endpoint state. Each private endpoint connects a private network to Data API on a Capella cluster.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Creator
* Project Viewer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**200** 

Successfully retrieved list of Data API private endpoints.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/dataAPI/privateEndpoints

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/dataAPI/privateEndpoints

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "privateEndpointDNS": "abcdef123456.pl.cloud.couchbase.com",
* "endpoints": [
  * {
    * "id": "vpce-000000000000aaaaa",
    * "serviceName": "com.amazonaws.vpce.us-east-1.vpce-svc-000000000000aaaaa",
    * "status": "linked"  
  }  
]
}`

## [](#tag/Data-API/operation/associateDataAPIPrivateEndpointRequest)Accept Data API Private Endpoint Connection 

Accept a new private endpoint connection request so that it is associated with the Data API. Once accepted, the private endpoint is available for use.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| endpointIdrequired     | string Example: vpce-1234The VPC endpoint ID.                                                 |

### Responses

**204** 

Successfully associated private endpoint.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/dataAPI/privateEndpoints/{endpointId}/associate

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/dataAPI/privateEndpoints/{endpointId}/associate

### Response samples 

* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Data-API/operation/disassociateDataAPIPrivateEndpoint)Disassociate Data API Private Endpoint 

Removes or disassociates the private endpoint. If the private endpoint connection has still not yet been accepted, the request is rejected. Turning off the cluster will not automatically remove any of the Data API Endpoints and the endpoints will be available when cluster is turned back on. If you remove the private endpoint before turning off a cluster, you must associate it back again with data api is turned back on. Retaining private endpoints when cluster is off does not result in any additional charges beyond the cost of enabling Data API.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| endpointIdrequired     | string Example: vpce-1234The VPC endpoint ID.                                                 |

### Responses

**204** 

Successfully disassociated private endpoint.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/dataAPI/privateEndpoints/{endpointId}/unassociate

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/dataAPI/privateEndpoints/{endpointId}/unassociate

### Response samples 

* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Database-Credentials)Database Credentials

Database credentials provide programmatic and application-level access to data on a database. Only database credentials can access data.

## [](#tag/Database-Credentials/operation/listDatabaseCredentials)List Database Credentials 

Lists all the database credential information under a cluster.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Viewer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                  |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                        |
| sortBy        | Array of strings Example: sortBy=name Sets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **name**, **id**. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                               |

### Responses

**200** 

Successfully listed all the database credentials under the cluster.

**403** 

The client does not have the necessary permissions to access this resource.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/users

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/users

### Response samples 

* 200
* 403
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/ffffffff-aaaa-1414-eeee-000000000000/ffffffff-aaaa-1414-eeee-000000000000/ffffffff-aaaa-1414-eeee-000000000000?page=2&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/ffffffff-aaaa-1414-eeee-000000000000/ffffffff-aaaa-1414-eeee-000000000000/ffffffff-aaaa-1414-eeee-000000000000?page=10&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/ffffffff-aaaa-1414-eeee-000000000000/ffffffff-aaaa-1414-eeee-000000000000/ffffffff-aaaa-1414-eeee-000000000000?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/ffffffff-aaaa-1414-eeee-000000000000/ffffffff-aaaa-1414-eeee-000000000000/ffffffff-aaaa-1414-eeee-000000000000?page=3&perPage=10>"  
  }  
},
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "name": "ReadInventory",
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56Z",
      * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "modifiedAt": "2021-09-01T12:34:56Z",
      * "version": 1  
      },
    * "access": [
      * {
        * "privileges": [
          * "data_reader",
          * "data_writer"  
                    ],
        * "resources": {
          * "buckets": [
            * {
              * "name": "travel-sample",
              * "scopes": [
                * {
                  * "name": "inventory"  
                                                                        }  
                                                        ]  
                                          }  
                              ]  
                    }  
            }  
      ]  
  }  
]
}`

## [](#tag/Database-Credentials/operation/postDatabaseCredential)Create Database Credentials 

Creates a new database credential under a cluster.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

Valid fields to sort the results are: "id", "name".

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| namerequired   | string \[ 2 .. 128 \] characters Username for the database credential. The name should adhere to the following rules: The name must be between 2 & 128 characters. The name cannot contain spaces. The name cannot contain the following characters - ) ( > < , ; : " \\ / \] \[ ? = } { The name cannot begin with @ character.                                                                                                                                                   |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| password       | string \>= 8 characters A password associated with the database credential. If this field is left empty, a password will be auto-generated. The password should adhere to the following rules: The password should have at least 8 characters. Characters used for the password should contain at least one uppercase (A-Z), one lowercase (a-z), one numerical (0-9), and one special character. The password must not contain any of the following characters: < > ; . \* & \| £ |
| accessrequired | Array of objects (Access) Describes the access information of the database credential.                                                                                                                                                                                                                                                                                                                                                                                             |

### Responses

**201** 

Successfully created a database access record under a cluster.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/users

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/users

### Request samples 

* Payload

Content type

application/json

Example

ReadWriteOnSomeCollectionsReadAndWriteOnAllCollectionsInABucketAndScopeReadAccessOnAllBucketsSeparateAccessForDifferentScopesWriteAccessForAllBucketsMultipleLevelOfAccessReadWriteOnSomeCollections

Copy

 Expand all  Collapse all 

`{
* "name": "ReadWriteOnSpecificCollections",
* "access": [
  * {
    * "privileges": [
      * "data_reader",
      * "data_writer"  
      ],
    * "resources": {
      * "buckets": [
        * {
          * "name": "travel-sample",
          * "scopes": [
            * {
              * "name": "inventory",
              * "collections": [
                * "airport",
                * "airline"  
                                                        ]  
                                          }  
                              ]  
                    }  
            ]  
      }  
  }  
]
}`

### Response samples 

* 201
* 400
* 403
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "password": "P@ssw0rd!"
}`

## [](#tag/Database-Credentials/operation/getDatabaseCredential)Get Database Credentials 

Fetches the details of a given cluster's database credential information.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Viewer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.        |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.             |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.             |
| userIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the database credential. |

### Responses

**200** 

Successfully fetched the cluster's database credential information based on the userId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/users/{userId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/users/{userId}

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "name": "ReadInventory",
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
},
* "access": [
  * {
    * "privileges": [
      * "data_reader",
      * "data_writer",
      * "read",
      * "write"  
      ],
    * "resources": {
      * "buckets": [
        * {
          * "name": "travel-sample",
          * "scopes": [
            * {
              * "name": "inventory",
              * "collections": [
                * "airlines",
                * "airport",
                * "tickets"  
                                                        ]  
                                          }  
                              ]  
                    }  
            ]  
      }  
  }  
]
}`

## [](#tag/Database-Credentials/operation/putDatabaseCredential)Update Database Credentials 

Updates an existing database credential.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.        |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.             |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.             |
| userIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the database credential. |

##### header Parameters

| If-Match | string Example: 12A precondition header that specifies the entity tag of a resource. |
| -------- | ------------------------------------------------------------------------------------ |

##### Request Body schema: application/json

| access   | Array of objects (Access) Describes the access information of the database credential. |
| -------- | -------------------------------------------------------------------------------------- |
| password | string The updated password of the database credential.                                |

### Responses

**204** 

Successfully updated the access in the cluster's database credential.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/users/{userId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/users/{userId}

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "access": [
  * {
    * "privileges": [
      * "data_reader",
      * "data_writer"  
      ],
    * "resources": {
      * "buckets": [
        * {
          * "name": "travel-sample",
          * "scopes": [
            * {
              * "name": "inventory",
              * "collections": [
                * "airport",
                * "airline",
                * "tickets"  
                                                        ]  
                                          }  
                              ]  
                    }  
            ]  
      }  
  }  
]
}`

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Database-Credentials/operation/deleteDatabaseCredential)Delete Database Credentials 

Deletes an existing cluster's database credential.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.        |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.             |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.             |
| userIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the database credential. |

### Responses

**204** 

Successfully deleted the cluster's database access record by its userId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/users/{userId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/users/{userId}

### Response samples 

* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Eventing-Functions)Eventing Functions

The Eventing Service runs JavaScript code in response to data changes in a collection. You define OnUpdate and OnDelete handlers, and Couchbase invokes them whenever documents are created, modified, or deleted. It works like a database trigger which runs asynchronously on dedicated Eventing nodes.

## [](#tag/Eventing-Functions/operation/getFunctionCode)Get Eventing Function Code 

Retrieves the JavaScript code for the specified function. The code is not escaped.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.                                                  |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                                                       |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                                                       |
| functionNamerequired   | string \[ 1 .. 100 \] characters ^\[a-zA-Z0-9\]\[a-zA-Z0-9\_-\]\*$ Example: my\_eventing\_functionThe name of the eventing function to target. |

### Responses

**200** 

Successfully returned the Eventing function code.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/eventingFunctions/{functionName}/code

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/eventingFunctions/{functionName}/code

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`"function OnUpdate(doc, meta, xattrs) {\n log(\"Doc created/updated\", meta.id);\n}\n\nfunction OnDelete(meta, options) {\n log(\"Doc deleted/expired\", meta.id);\n}\n"`

## [](#tag/Eventing-Functions/operation/updateFunctionCode)Update Eventing Function Code 

Update the JavaScript code for the specified function.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.                                                  |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                                                       |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                                                       |
| functionNamerequired   | string \[ 1 .. 100 \] characters ^\[a-zA-Z0-9\]\[a-zA-Z0-9\_-\]\*$ Example: my\_eventing\_functionThe name of the eventing function to target. |

##### Request Body schema: application/javascript

string (UpdateFunctionCodeRequest) 

The JavaScript code of the eventing function that gets executed in response to document mutations.

The eventing service compresses the code before storing it. The compressed code must not exceed 128 KiB (131072 bytes); code larger than this limit after compression is rejected.

### Responses

**204** 

Successfully updated the Eventing function code.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/eventingFunctions/{functionName}/code

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/eventingFunctions/{functionName}/code

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Eventing-Functions/operation/getEventingFunction)Get Eventing Function 

Retrieves the full definition of an eventing function, including its JavaScript code, deployment configuration, runtime settings, and bindings.

By default the response includes the current `status` of the function. Set the `export` query parameter to `true` to omit read-only fields (currently only `status`) so that the response payload can be used as the body of a create request. This is useful for backing up an eventing function or for transferring it to a different cluster. Note that any URL bindings retain their redacted sensitive fields (passwords and bearer tokens are returned as `*****`), which must be replaced with their actual values before the payload is passed to the create eventing function endpoint.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.                                                  |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                                                       |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                                                       |
| functionNamerequired   | string \[ 1 .. 100 \] characters ^\[a-zA-Z0-9\]\[a-zA-Z0-9\_-\]\*$ Example: my\_eventing\_functionThe name of the eventing function to target. |

##### query Parameters

| export | boolean Default: false Example: export=trueWhen set to true, read-only fields are omitted from the response so that the payload can be used as the body of a create request. This is useful for backing up an eventing function or transferring it to a different cluster. Any URL bindings retain their redacted sensitive fields (passwords and bearer tokens are returned as \*\*\*\*\*). These must be replaced with their actual values before the payload is passed to the create eventing function endpoint. |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**200** 

Successfully retrieved the eventing function definition.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/eventingFunctions/{functionName}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/eventingFunctions/{functionName}

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "name": "my_function",
* "description": "Replicates document mutations to a downstream collection.",
* "status": "deployed",
* "code": "function OnUpdate(doc, meta, xattrs) {\n log(\"Doc created/updated\", meta.id);\n}\n\nfunction OnDelete(meta, options) {\n log(\"Doc deleted/expired\", meta.id);\n}\n",
* "eventSource": {
  * "bucket": "travel-sample",
  * "scope": "inventory",
  * "collection": "airline"  
},
* "eventMetadataStorage": {
  * "bucket": "travel-sample",
  * "scope": "inventory",
  * "collection": "airline"  
},
* "settings": {
  * "workerCount": 1,
  * "scriptTimeout": 30,
  * "sqlConsistency": "request",
  * "languageCompatibility": "7.2.0",
  * "feedBoundary": "everything",
  * "maxTimerContextSize": 1024,
  * "allowSyncDocuments": false,
  * "cursorAware": true  
},
* "bindings": {
  * "buckets": [
    * {
      * "alias": "src",
      * "bucket": "travel-sample",
      * "scope": "*",
      * "collection": "*",
      * "permission": "readWrite"  
      }  
  ],
  * "urls": [
    * {
      * "alias": "api",
      * "url": "<https://api.example.com/path>",
      * "allowCookies": true,
      * "validateTLSCertificate": true,
      * "authentication": {
        * "type": "none"  
            }  
      }  
  ],
  * "constants": [
    * {
      * "alias": "maxRetries",
      * "value": "3"  
      }  
  ]  
}
}`

## [](#tag/Eventing-Functions/operation/deleteEventingFunction)Delete Eventing Function 

Delete an eventing function. The function must be undeployed prior to deletion.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.                                                  |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                                                       |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                                                       |
| functionNamerequired   | string \[ 1 .. 100 \] characters ^\[a-zA-Z0-9\]\[a-zA-Z0-9\_-\]\*$ Example: my\_eventing\_functionThe name of the eventing function to target. |

### Responses

**204** 

Successfully deleted the eventing function.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/eventingFunctions/{functionName}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/eventingFunctions/{functionName}

### Response samples 

* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Eventing-Functions/operation/putEventingFunction)Update Eventing Function 

Applies a partial update to an existing eventing function on the specified cluster.

Only the fields that are supplied in the request body are modified; any field that is omitted is left unchanged on the function. For nested objects (`eventSource`, `eventMetadataStorage`, `settings`), the same rule applies recursively. For the binding lists under `bindings`, supplying a category replaces that list in full with the value provided, and omitting a category leaves it unchanged.

Updates to `feedBoundary` only take effect when the function goes from undeployed to deployed. Other settings, code, and bindings changes are applied immediately.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Database Data Reader/Writer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.                                                  |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                                                       |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                                                       |
| functionNamerequired   | string \[ 1 .. 100 \] characters ^\[a-zA-Z0-9\]\[a-zA-Z0-9\_-\]\*$ Example: my\_eventing\_functionThe name of the eventing function to target. |

##### Request Body schema: application/json

required

| description          | string The eventing function description.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code                 | string The JavaScript code of the eventing function that gets executed in response to document mutations. The eventing service compresses the code before storing it. The compressed code must not exceed 128 KiB (131072 bytes); a function whose code is larger than this limit after compression is rejected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| eventSource          | object A reference to a Couchbase keyspace, identified by its bucket, scope, and collection. Every field is optional in an update request, and any field that is omitted is left unchanged on the function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| eventMetadataStorage | object A reference to a Couchbase keyspace, identified by its bucket, scope, and collection. Every field is optional in an update request, and any field that is omitted is left unchanged on the function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| settings             | object Runtime settings that control how the eventing function is executed. Every field is optional, and any field that is omitted is left unchanged on the function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| bindings             | object A binding is a construct that lets you separate environment-specific variables, like keyspace names, external endpoint URLs and credentials, and global constants, from the source code of the eventing function. A binding provides indirection between environment-specific artifacts and symbolic names, and helps move a function definition from a development to a production environment without changing the eventing code. Binding names must be valid JavaScript identifiers, and cannot conflict with built-in types. When a binding category (buckets, urls, or constants) is supplied, the corresponding list on the function is replaced in full with the value provided. Categories that are omitted are left unchanged. To remove every binding in a category, supply an empty array. Aliases must be unique across all three binding types. |

### Responses

**204** 

Successfully applied the update to the eventing function.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/eventingFunctions/{functionName}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/eventingFunctions/{functionName}

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "description": "Replicates document mutations to a downstream collection.",
* "code": "function OnUpdate(doc, meta, xattrs) {\n log(\"Doc created/updated\", meta.id);\n}\n\nfunction OnDelete(meta, options) {\n log(\"Doc deleted/expired\", meta.id);\n}\n",
* "eventSource": {
  * "bucket": "travel-sample",
  * "scope": "inventory",
  * "collection": "airline"  
},
* "eventMetadataStorage": {
  * "bucket": "travel-sample",
  * "scope": "inventory",
  * "collection": "airline"  
},
* "settings": {
  * "workerCount": 1,
  * "scriptTimeout": 30,
  * "sqlConsistency": "request",
  * "languageCompatibility": "7.2.0",
  * "feedBoundary": "everything",
  * "maxTimerContextSize": 1024,
  * "allowSyncDocuments": false,
  * "cursorAware": true  
},
* "bindings": {
  * "buckets": [
    * {
      * "alias": "src",
      * "bucket": "travel-sample",
      * "scope": "*",
      * "collection": "*",
      * "permission": "readWrite"  
      }  
  ],
  * "urls": [
    * {
      * "alias": "api",
      * "url": "<https://api.example.com/path>",
      * "allowCookies": true,
      * "validateTLSCertificate": true,
      * "authentication": {
        * "type": "none"  
            }  
      }  
  ],
  * "constants": [
    * {
      * "alias": "maxRetries",
      * "value": "3"  
      }  
  ]  
}
}`

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Eventing-Functions/operation/postEventingFunction)Create Eventing Function 

Creates a new eventing function on the specified cluster. The function is created in the `undeployed` state and must be deployed separately before it begins processing mutations.

The cluster must have at least one eventing node available in order to create a function.

The function includes its JavaScript code, the source and metadata keyspaces, runtime settings, and any bucket, URL, or constant bindings. Optional fields that are omitted from the payload are populated with the defaults documented on the request schema.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Database Data Reader/Writer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

required

| namerequired                 | string \[ 1 .. 100 \] characters ^\[a-zA-Z0-9\]\[a-zA-Z0-9\_-\]\*$ The name of the eventing function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| description                  | string or null The eventing function description.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| code                         | string Default: "function OnUpdate(doc, meta, xattrs) {\\n // Add your mutation logic here\\n}\\n\\nfunction OnDelete(meta, options) {\\n // Add your delete handling logic here\\n}\\n" The JavaScript code of the eventing function that gets executed in response to document mutations. The eventing service compresses the code before storing it. The compressed code must not exceed 128 KiB (131072 bytes); a function whose code is larger than this limit after compression is rejected.                                                                                                                                                                                                     |
| eventSourcerequired          | object A reference to a Couchbase keyspace, identified by its bucket, scope, and collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| eventMetadataStoragerequired | object A reference to a Couchbase keyspace, identified by its bucket, scope, and collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| settings                     | object (EventingFunctionSettings) Runtime settings that control how the function is executed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| bindings                     | object (EventingFunctionBindings) A binding is a construct that lets you separate environment-specific variables, like keyspace names, external endpoint URLs and credentials, and global constants, from the source code of the Eventing Function. A binding provides indirection between environment-specific artifacts and symbolic names, and helps move a function definition from a development to a production environment without changing the eventing code. Binding names must be valid JavaScript identifiers, and cannot conflict with built-in types. An Eventing Function can have no bindings, one binding, or several bindings. Aliases must be unique across all three binding types. |

### Responses

**201** 

Successfully created the eventing function.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/eventingFunctions

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/eventingFunctions

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "name": "my_function",
* "description": "Replicates document mutations to a downstream collection.",
* "code": "function OnUpdate(doc, meta, xattrs) {\n log(\"Doc created/updated\", meta.id);\n}\n\nfunction OnDelete(meta, options) {\n log(\"Doc deleted/expired\", meta.id);\n}\n",
* "eventSource": {
  * "bucket": "travel-sample",
  * "scope": "inventory",
  * "collection": "airline"  
},
* "eventMetadataStorage": {
  * "bucket": "travel-sample",
  * "scope": "inventory",
  * "collection": "airline"  
},
* "settings": {
  * "workerCount": 1,
  * "scriptTimeout": 30,
  * "sqlConsistency": "request",
  * "languageCompatibility": "7.2.0",
  * "feedBoundary": "everything",
  * "maxTimerContextSize": 1024,
  * "allowSyncDocuments": false,
  * "cursorAware": true  
},
* "bindings": {
  * "buckets": [
    * {
      * "alias": "src",
      * "bucket": "travel-sample",
      * "scope": "*",
      * "collection": "*",
      * "permission": "readWrite"  
      }  
  ],
  * "urls": [
    * {
      * "alias": "api",
      * "url": "<https://api.example.com/path>",
      * "allowCookies": true,
      * "validateTLSCertificate": true,
      * "authentication": {
        * "type": "none"  
            }  
      }  
  ],
  * "constants": [
    * {
      * "alias": "maxRetries",
      * "value": "3"  
      }  
  ]  
}
}`

### Response samples 

* 400
* 403
* 404
* 409
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Eventing-Functions/operation/listEventingFunctions)List Eventing Functions 

Lists the eventing functions on the cluster, including their status. You can optionally filter on status.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                                                                                                                                                            |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                                                                                                                                                  |
| sortBy        | Array of strings Example: sortBy=nameSets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **name**, **status**.                                                                                                                                        |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                                                                                                                                                         |
| status        | Array of stringsItems Enum: "deployed" "deploying" "undeployed" "undeploying" "paused" "pausing" Filter eventing functions by one or more status. When this query parameter is not set, all eventing functions will be returned no matter the state. Accepts a comma-separated list, or the same query parameter defined multiple times. |

### Responses

**200** 

Successfully retrieved the list of eventing functions.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/eventingFunctions

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/eventingFunctions

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "name": "my_function",
    * "description": "Replicates document mutations to a downstream collection.",
    * "status": "deployed",
    * "code": "function OnUpdate(doc, meta, xattrs) {\n log(\"Doc created/updated\", meta.id);\n}\n\nfunction OnDelete(meta, options) {\n log(\"Doc deleted/expired\", meta.id);\n}\n",
    * "eventSource": {
      * "bucket": "travel-sample",
      * "scope": "inventory",
      * "collection": "airline"  
      },
    * "eventMetadataStorage": {
      * "bucket": "travel-sample",
      * "scope": "inventory",
      * "collection": "airline"  
      },
    * "settings": {
      * "workerCount": 1,
      * "scriptTimeout": 30,
      * "sqlConsistency": "request",
      * "languageCompatibility": "7.2.0",
      * "feedBoundary": "everything",
      * "maxTimerContextSize": 1024,
      * "allowSyncDocuments": false,
      * "cursorAware": true  
      },
    * "bindings": {
      * "buckets": [
        * {
          * "alias": "src",
          * "bucket": "travel-sample",
          * "scope": "*",
          * "collection": "*",
          * "permission": "readWrite"  
                    }  
            ],
      * "urls": [
        * {
          * "alias": "api",
          * "url": "<https://api.example.com/path>",
          * "allowCookies": true,
          * "validateTLSCertificate": true,
          * "authentication": {
            * "type": "none"  
                              }  
                    }  
            ],
      * "constants": [
        * {
          * "alias": "maxRetries",
          * "value": "3"  
                    }  
            ]  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/Eventing-Functions/operation/setFunctionState)Set Eventing Function State 

This endpoint allows the user to change the eventing function to a deployed, undeployed, or paused state.

The mapping for this is as follows:

* deploy: deploys an undeployed eventing function causing it to start processing events.
* undeploy: undeploys a deployed or paused eventing function, causing it to stop processing any events.
* pause: pauses a deployed eventing function, causing it to stop processing events with the ability to resume its current progress in the future.
* resume: resumes a paused eventing function (back to deployed state), causing it to continue to process events from where it was paused.

In order to access this endpoint, the provided API key must have at least one of the following roles: - Organization Owner - Project Owner - Project Manager

To learn more, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.                                                  |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                                                       |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                                                       |
| functionNamerequired   | string \[ 1 .. 100 \] characters ^\[a-zA-Z0-9\]\[a-zA-Z0-9\_-\]\*$ Example: my\_eventing\_functionThe name of the eventing function to target. |

##### Request Body schema: application/json

| staterequired | string Enum: "deploy" "undeploy" "pause" "resume" The action to take on the specified eventing function. |
| ------------- | -------------------------------------------------------------------------------------------------------- |

### Responses

**204** 

Successfully set the Eventing function state.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/eventingFunctions/{functionName}/activationState

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/eventingFunctions/{functionName}/activationState

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "state": "deploy"
}`

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Eventing-Functions/operation/getFunctionLogs)Get Function Logs 

Returns the most recent 40960 bytes of application log messages for the specified function.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.                                                  |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                                                       |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                                                       |
| functionNamerequired   | string \[ 1 .. 100 \] characters ^\[a-zA-Z0-9\]\[a-zA-Z0-9\_-\]\*$ Example: my\_eventing\_functionThe name of the eventing function to target. |

### Responses

**200** 

Successfully returned the Eventing function logs.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/eventingFunctions/{functionName}/logs

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/eventingFunctions/{functionName}/logs

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

text/plain

Copy

2026-05-07T18:39:00.742+00:00 [INFO] "Doc created/updated" "doc1"

## [](#tag/Events)Events

Events represent a trail of actions that users performs within Capella at an organization or project level

## [](#tag/Events/operation/listEvents)List Events 

Lists all the events information under a organization.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Creator
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader
* Database Data Reader/Writer

The results are always limited by the role and scope of the caller's privileges. Currently, only the `tags` filter is multi-valued; all other filters are single-valued.

By default, `to` is set to the request time, and `from` is set to 24 hours before the request time. If 'to' is set and 'from' is not set, then 'from' is set to 24 hours before 'to'.

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### query Parameters

| page           | integer Sets the page you would like to view.                                                                                                                                                                                                                                                                                                                                            |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage        | integer Sets the number of results you would like to have on each page.                                                                                                                                                                                                                                                                                                                  |
| sortBy         | Array of stringsItems Enum: "timestamp" "severity" Example: sortBy=timestamp Sets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **severity**, **timestamp**.                                                                                                                                         |
| sortDirection  | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                                                                                                                                                                                                         |
| userIds        | Array of strings <uuid\> \[ items <uuid \> \] Example: userIds=ffffffff-aaaa-1414-eeee-000000000000Filter by user UUID. Default is to return events corresponding to all users.                                                                                                                                                                                                          |
| clusterIds     | Array of strings <uuid\> \[ items <uuid \> \] Example: clusterIds=ffffffff-aaaa-1414-eeee-000000000000List of clusterIds to filter on. By default events corresponding to all clusters are returned.                                                                                                                                                                                     |
| projectIds     | Array of strings <uuid\> \[ items <uuid \> \] Example: projectIds=ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of projects to filter on. By default, events corresponding to all projects are returned                                                                                                                                                                               |
| severityLevels | Array of stringsItems Enum: "info" "warning" "critical" Filter by severity levels. Default is to return events corresponding to all supported severity levels.                                                                                                                                                                                                                           |
| tags           | Array of stringsItems Enum: "availability" "billing" "maintenance" "performance" "security" "alert" Example: tags=availability&tags=billing&tags=maintenance&tags=performance&tags=security&tags=alertFilter by tags. Default is to return events corresponding to all supported tag. Tags are **availability**, **billing**, **maintenance**, **performance**, **security**, **alert**. |
| from           | string <date-time\> Example: from=2024-04-24T12:53:59.000ZStart date in RFC3339 format. If not provided, events starting from last 24 hours are returned.                                                                                                                                                                                                                                |
| to             | string <date-time\> Example: to=2024-04-25T12:53:59.000ZEnd datetime in the last 24 hours, RFC3339 format. Defaults to Now.                                                                                                                                                                                                                                                              |

### Responses

**200** 

Successfully listed the events under the organization.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/events

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/events

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000001",
    * "source": "System",
    * "key": "cluster_down",
    * "severity": "critical",
    * "timestamp": "2024-04-24T08:30:00Z",
    * "projectId": "ffffffff-aaaa-1414-eeee-000000000003",
    * "projectName": "example-project",
    * "clusterId": "ffffffff-aaaa-1414-eeee-000000000004",
    * "clusterName": "example-cluster",
    * "appServiceId": "ffffffff-aaaa-1414-eeee-000000000006",
    * "appServiceName": "example-appService",
    * "userId": "ffffffff-aaaa-1414-eeee-000000000008",
    * "userName": "John Doe",
    * "userEmail": "john.doe@example.com",
    * "sessionId": "ffffffff-aaaa-1414-eeee-000000000009",
    * "requestId": "ffffffff-aaaa-1414-eeee-000000000010",
    * "kv": {
      * "key1": "value1",
      * "key2": "value2"  
      },
    * "summary": "Cluster is down due to network outage.",
    * "incidentIds": [
      * "ffffffff-aaaa-1414-eeee-000000000011"  
      ],
    * "occurrenceCount": 3,
    * "imageURL": "<https://example.com/chart.png>",
    * "alertKey": "cluster_down_example"  
  }  
]
}`

## [](#tag/Events/operation/getEventByID)Get Event 

Fetches the details of an event by ID.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Creator
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader
* Database Data Reader/Writer

The results are always limited by the role and scope of the caller's privileges.

To learn more, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| eventIdrequired        | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The event ID of the event.        |

### Responses

**200** 

Successfully returned the event details.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/events/{eventId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/events/{eventId}

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000001",
* "source": "System",
* "key": "cluster_down",
* "severity": "critical",
* "timestamp": "2024-04-24T08:30:00Z",
* "projectId": "ffffffff-aaaa-1414-eeee-000000000003",
* "projectName": "example-project",
* "clusterId": "ffffffff-aaaa-1414-eeee-000000000004",
* "clusterName": "example-cluster",
* "appServiceId": "ffffffff-aaaa-1414-eeee-000000000006",
* "appServiceName": "example-appService",
* "userId": "ffffffff-aaaa-1414-eeee-000000000008",
* "userName": "John Doe",
* "userEmail": "john.doe@example.com",
* "sessionId": "ffffffff-aaaa-1414-eeee-000000000009",
* "requestId": "ffffffff-aaaa-1414-eeee-000000000010",
* "kv": {
  * "key1": "value1",
  * "key2": "value2"  
},
* "summary": "Cluster is down due to network outage.",
* "incidentIds": [
  * "ffffffff-aaaa-1414-eeee-000000000011"  
],
* "occurrenceCount": 3,
* "imageURL": "<https://example.com/chart.png>",
* "alertKey": "cluster_down_example"
}`

## [](#tag/Events/operation/listProjectEvents)List Events 

Lists all the events information under a project.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader
* Database Data Reader/Writer

The results are always limited by the role and scope of the caller's privileges. Currently, only the `tags` filter is multi-valued; all other filters are single-valued.

By default, `to` is set to the request time, and `from` is set to 24 hours before the request time. If 'to' is set and 'from' is not set, then 'from' is set to 24 hours before 'to'.

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

##### query Parameters

| page           | integer Sets the page you would like to view.                                                                                                                                                                                                                                                                                                                                            |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage        | integer Sets the number of results you would like to have on each page.                                                                                                                                                                                                                                                                                                                  |
| sortBy         | Array of stringsItems Enum: "timestamp" "severity" Example: sortBy=timestamp Sets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **severity**, **timestamp**.                                                                                                                                         |
| sortDirection  | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                                                                                                                                                                                                         |
| userIds        | Array of strings <uuid\> \[ items <uuid \> \] Example: userIds=ffffffff-aaaa-1414-eeee-000000000000Filter by user UUID. Default is to return events corresponding to all users.                                                                                                                                                                                                          |
| clusterIds     | Array of strings <uuid\> \[ items <uuid \> \] Example: clusterIds=ffffffff-aaaa-1414-eeee-000000000000List of clusterIds to filter on. By default events corresponding to all clusters are returned.                                                                                                                                                                                     |
| severityLevels | Array of stringsItems Enum: "info" "warning" "critical" Filter by severity levels. Default is to return events corresponding to all supported severity levels.                                                                                                                                                                                                                           |
| tags           | Array of stringsItems Enum: "availability" "billing" "maintenance" "performance" "security" "alert" Example: tags=availability&tags=billing&tags=maintenance&tags=performance&tags=security&tags=alertFilter by tags. Default is to return events corresponding to all supported tag. Tags are **availability**, **billing**, **maintenance**, **performance**, **security**, **alert**. |
| from           | string <date-time\> Example: from=2024-04-24T12:53:59.000ZStart date in RFC3339 format. If not provided, events starting from last 24 hours are returned.                                                                                                                                                                                                                                |
| to             | string <date-time\> Example: to=2024-04-25T12:53:59.000ZEnd datetime in the last 24 hours, RFC3339 format. Defaults to Now.                                                                                                                                                                                                                                                              |

### Responses

**200** 

Successfully listed the events under the organization.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/events

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/events

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000001",
    * "source": "System",
    * "key": "cluster_down",
    * "severity": "critical",
    * "timestamp": "2024-04-24T08:30:00Z",
    * "projectId": "ffffffff-aaaa-1414-eeee-000000000003",
    * "projectName": "example-project",
    * "clusterId": "ffffffff-aaaa-1414-eeee-000000000004",
    * "clusterName": "example-cluster",
    * "appServiceId": "ffffffff-aaaa-1414-eeee-000000000006",
    * "appServiceName": "example-appService",
    * "userId": "ffffffff-aaaa-1414-eeee-000000000008",
    * "userName": "John Doe",
    * "userEmail": "john.doe@example.com",
    * "sessionId": "ffffffff-aaaa-1414-eeee-000000000009",
    * "requestId": "ffffffff-aaaa-1414-eeee-000000000010",
    * "kv": {
      * "key1": "value1",
      * "key2": "value2"  
      },
    * "summary": "Cluster is down due to network outage.",
    * "incidentIds": [
      * "ffffffff-aaaa-1414-eeee-000000000011"  
      ],
    * "occurrenceCount": 3,
    * "imageURL": "<https://example.com/chart.png>",
    * "alertKey": "cluster_down_example"  
  }  
]
}`

## [](#tag/Events/operation/getProjectEventByID)Get Project Event 

Fetches the details of an event by ID within a project.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader
* Database Data Reader/Writer

The results are always limited by the role and scope of the caller's privileges.

To learn more, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| eventIdrequired        | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The event ID of the event.        |

### Responses

**200** 

Successfully returned the event details.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/events/{eventId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/events/{eventId}

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000001",
* "source": "System",
* "key": "cluster_down",
* "severity": "critical",
* "timestamp": "2024-04-24T08:30:00Z",
* "projectId": "ffffffff-aaaa-1414-eeee-000000000003",
* "projectName": "example-project",
* "clusterId": "ffffffff-aaaa-1414-eeee-000000000004",
* "clusterName": "example-cluster",
* "appServiceId": "ffffffff-aaaa-1414-eeee-000000000006",
* "appServiceName": "example-appService",
* "userId": "ffffffff-aaaa-1414-eeee-000000000008",
* "userName": "John Doe",
* "userEmail": "john.doe@example.com",
* "sessionId": "ffffffff-aaaa-1414-eeee-000000000009",
* "requestId": "ffffffff-aaaa-1414-eeee-000000000010",
* "kv": {
  * "key1": "value1",
  * "key2": "value2"  
},
* "summary": "Cluster is down due to network outage.",
* "incidentIds": [
  * "ffffffff-aaaa-1414-eeee-000000000011"  
],
* "occurrenceCount": 3,
* "imageURL": "<https://example.com/chart.png>",
* "alertKey": "cluster_down_example"
}`

## [](#tag/Free-Tier)Free Tier

Endpoints to manage resources that are available with free tier plan. These resources are buckets, clusters and app services.

## [](#tag/Free-Tier/operation/createFreeTierCluster)Create Free Tier Cluster 

Creates a free tier cluster. This is a 1 node cluster than only runs data, query, index and search services.

You can have at most 1 free tier cluster per tenant.

The following features are not available for free tier clusters:

* backup/restore
* private endpoint service
* network peering
* audit logs
* alert integration
* CMEK
* on/off schedule

Only cluster name, description, CSP, region and CIDR are configurable.

There are limited regions available based on CSP: a. for AWS they are us-east-2, eu-west-1, ap-southeast-1 b. for GCP they are us-central1, europe-west1, asia-east1 c. for Azure they are eastus, swedencentral, koreacentral

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

##### Request Body schema: application/json

| namerequired          | string <= 256 characters Name of the cluster (up to 256 characters).                                                                                                                                                                                                                                                                                                     |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| description           | string <= 1024 characters Description of the cluster (up to 1024 characters).                                                                                                                                                                                                                                                                                            |
| cloudProviderrequired | object (CloudProvider) The cloud provider where the cluster will be hosted. For information about providers and supported regions, see: [Amazon Web Services](https://docs.couchbase.com/cloud/reference/aws.html) [Google Cloud Platform](https://docs.couchbase.com/cloud/reference/gcp.html) [Microsoft Azure](https://docs.couchbase.com/cloud/reference/azure.html) |

### Responses

**202** 

Successfully submitted job to create a free tier cluster.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error. For example when client tries to create more than 1 free tier cluster in tenant.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/freeTier

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/freeTier

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "name": "Free-Tier-Cluster-1",
* "description": "My first test AWS cluster for multiple services.",
* "cloudProvider": {
  * "type": "aws",
  * "region": "us-east-2",
  * "cidr": "10.1.30.0/23"  
}
}`

### Response samples 

* 202
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/Free-Tier/operation/getFreeTierCluster)Get Free Tier Cluster 

Get details of the free tier cluster.

While only cluster name, description, CSP, region and CIDR are configurable, other read only fields are retrieved.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**200** 

Successfully got the free tier cluster.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/freeTier/{clusterId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/freeTier/{clusterId}

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "appServiceId": "ffffffff-aaaa-1414-eeee-000000000000",
* "name": "Test Cluster",
* "description": "Description of the cluster",
* "configurationType": "multiNode",
* "connectionString": "couchbases://cb.irxmynm6vekhe5.cloud.couchbase.com",
* "cloudProvider": {
  * "type": "aws",
  * "region": "us-east-1",
  * "cidr": "10.1.30.0/23"  
},
* "couchbaseServer": {
  * "version": "7.1"  
},
* "serviceGroups": [
  * {
    * "node": {
      * "compute": {
        * "cpu": 4,
        * "ram": 16  
            },
      * "disk": {
        * "type": "gp3",
        * "storage": 50,
        * "iops": 3000  
            }  
      },
    * "numOfNodes": 3,
    * "services": [
      * "data"  
      ]  
  }  
],
* "availability": {
  * "type": "single"  
},
* "support": {
  * "plan": "free",
  * "timezone": "ET"  
},
* "currentState": "deploying",
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
},
* "cmekId": "ffffffff-aaaa-1414-eeee-000000000000",
* "enablePrivateDNSResolution": true
}`

## [](#tag/Free-Tier/operation/updateFreeTierCluster)Update Free Tier Cluster 

Updates an existing free tier cluster. Only name and description are configurable.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### header Parameters

| If-Match | string Example: 12A precondition header that specifies the entity tag of a resource. |
| -------- | ------------------------------------------------------------------------------------ |

##### Request Body schema: application/json

| namerequired        | string <= 256 characters The new name of the cluster (up to 256 characters).   |
| ------------------- | ------------------------------------------------------------------------------ |
| descriptionrequired | string <= 1024 characters The new cluster description (up to 1024 characters). |

### Responses

**204** 

Successfully updated free tier cluster.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/freeTier/{clusterId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/freeTier/{clusterId}

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "name": "My-New-Cluster",
* "description": "The extended description of my new cluster."
}`

### Response samples 

* 400
* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Free-Tier/operation/deleteFreeTierCluster)Delete Free Tier Cluster 

Deletes an existing free tier cluster.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**202** 

Successfully submitted request to delete the free tier cluster.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/freeTier/{clusterId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/freeTier/{clusterId}

### Response samples 

* 403
* 404
* 409
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Free-Tier/operation/freeTierClusterOn)Turn On Free Tier Cluster 

Turn free tier cluster on. It will also turn on the linked app services, if any.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**202** 

Successfully switched the free tier cluster to on state.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/freeTier/{clusterId}/activationState

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/freeTier/{clusterId}/activationState

### Response samples 

* 400
* 403
* 404
* 409
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Free-Tier/operation/freeTierClusterOff)Turn Off Free Tier Cluster 

Turn free tier cluster off.

* Turning off your cluster turns off the compute for your cluster but the storage remains. All of the data, schema (buckets, scopes, and collections), and indexes remain, as well as cluster configuration, including users and allow lists.
* Turning off cluster will also turn off any linked app services.

 In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**202** 

Successfully switched the free tier cluster to off state.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/freeTier/{clusterId}/activationState

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/freeTier/{clusterId}/activationState

### Response samples 

* 400
* 403
* 404
* 409
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Free-Tier/operation/createFreeTierAppService)Create Free Tier App Service 

Creates a free tier App Service. This is a 1 node cluster which can only be linked to a free tier cluster.

The following features are not available for free tier clusters:

* audit logging
* turn App Service off/on

Free tier App Service can only be turned off/on when the linked free tier cluster is turned off/on.

Only name a description are configurable.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| namerequired | string <= 256 characters Name of App Service.                    |
| ------------ | ---------------------------------------------------------------- |
| description  | string <= 256 characters A short description of the App Service. |

### Responses

**202** 

Successfully submitted request to create a free tier app cluster.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/freeTier

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/freeTier

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "name": "MyAppSyncService",
* "description": "My app sync service."
}`

### Response samples 

* 202
* 400
* 403
* 404
* 409
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/Free-Tier/operation/getFreeTierAppService)Get Free Tier App Service 

Fetches the details of the free tier App Service.

While only name and description are configurable, other read only fields will be displayed.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

### Responses

**200** 

Successfully fetched the free tier App Service.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/freeTier/{appServiceId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/freeTier/{appServiceId}

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "name": "My App Service",
* "description": "Description of the App Service.",
* "cloudProvider": "aws",
* "nodes": 2,
* "compute": {
  * "cpu": 2,
  * "ram": 4  
},
* "clusterId": "ffffffff-aaaa-1414-eeee-000000000000",
* "currentState": "deploying",
* "version": "3.141.5",
* "plan": "free",
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
}
}`

## [](#tag/Free-Tier/operation/updateFreeTierAppService)Update Free Tier App Service 

Updates an existing free tier App Service. Only name and description are configurable.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

##### header Parameters

| If-Match | string Example: 12A precondition header that specifies the entity tag of a resource. |
| -------- | ------------------------------------------------------------------------------------ |

##### Request Body schema: application/json

| name        | string <= 256 characters Name of the App Service (up to 256 characters). |
| ----------- | ------------------------------------------------------------------------ |
| description | string A short description of the App Service.                           |

### Responses

**204** 

Successfully updated the free tier App Service.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/freeTier/{appServiceId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/freeTier/{appServiceId}

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "name": "MyAppSyncService",
* "description": "My app sync service."
}`

### Response samples 

* 400
* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Free-Tier/operation/deleteFreeTierAppService)Delete Free Tier App Service 

Deletes an existing free tier App Service.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| appServiceIdrequired   | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the appService.   |

### Responses

**202** 

Successfully submitted request to delete the free tier App Service.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/freeTier/{appServiceId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/appservices/freeTier/{appServiceId}

### Response samples 

* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Free-Tier/operation/createFreeTierBucket)Create Free Tier Bucket 

Creates a new free tier bucket. This is a Couchbase bucket where only the name a memory quota is configurable. Other bucket properties use default values. 

The following features are not available for free tier buckets:

* bucket flush
* migrate to another storage engine like magma

Note that you can only create a free tier bucket on a free tier cluster.

To learn more about bucket configuration, see [Buckets](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/buckets.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| namerequired         | string <= 100 characters Name of the bucket. This field cannot be changed later. The name should adhere to the following rules: Characters used for the name should be in the ranges of A-Z, a-z, and 0-9; plus the underscore, period, dash, and percent characters. The name can be a maximum of 100 characters in length. The name cannot have 0 characters or empty. Minimum length of name is 1. The name cannot start with a . (period). |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| memoryAllocationInMb | integer Default: 100 The bucket memory quota. It defaults to 100 MiB.                                                                                                                                                                                                                                                                                                                                                                          |

### Responses

**201** 

Successfully created a free tier bucket.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/freeTier

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/freeTier

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "name": "A-Free-Tier-Bucket",
* "memoryAllocationInMb": 200
}`

### Response samples 

* 201
* 400
* 403
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "dGVzdA"
}`

## [](#tag/Free-Tier/operation/listFreeTierBuckets)List Free Tier Buckets 

Lists all buckets in the free tier cluster. While only name and memory quota are configurable for free tier buckets, the response will show additional read only bucket properties such as replicas, etc.

To learn more about bucket configuration, see [Buckets](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/buckets.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**200** 

Successfully listed all the buckets in the free tier cluster.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/freeTier

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/freeTier

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "dGVzdA",
    * "name": "My-First-Bucket",
    * "type": "string",
    * "storageBackend": "couchstore",
    * "vbuckets": 128,
    * "memoryAllocationInMb": 100,
    * "bucketConflictResolution": "string",
    * "durabilityLevel": "string",
    * "replicas": 0,
    * "flush": false,
    * "flushEnabled": false,
    * "timeToLiveInSeconds": 100,
    * "enableCrossClusterVersioning": true,
    * "evictionPolicy": "fullEviction",
    * "stats": {
      * "itemCount": 10,
      * "opsPerSecond": 0,
      * "diskUsedInMib": 17,
      * "memoryUsedInMib": 50  
      },
    * "priority": 0  
  }  
],
* "clusterStats": {
  * "freeMemoryInMb": 640,
  * "totalMemoryInMb": 1040,
  * "maxReplicas": 2  
}
}`

## [](#tag/Free-Tier/operation/getFreeTierBucketByID)Get Free Tier Bucket 

Get bucket. While only name and memory quota are configurable for free tier buckets, the response will show additional read only bucket properties such as replicas, etc.

To learn more about bucket configuration, see [Buckets](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/buckets.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |

### Responses

**200** 

Successfully fetched free tier bucket by bucket id.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/freeTier/{bucketId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/freeTier/{bucketId}

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "dGVzdA",
* "name": "My-First-Bucket",
* "type": "string",
* "storageBackend": "couchstore",
* "vbuckets": 128,
* "memoryAllocationInMb": 100,
* "bucketConflictResolution": "string",
* "durabilityLevel": "string",
* "replicas": 0,
* "flush": false,
* "flushEnabled": false,
* "timeToLiveInSeconds": 100,
* "enableCrossClusterVersioning": true,
* "evictionPolicy": "fullEviction",
* "stats": {
  * "itemCount": 10,
  * "opsPerSecond": 0,
  * "diskUsedInMib": 17,
  * "memoryUsedInMib": 50  
},
* "priority": 0
}`

## [](#tag/Free-Tier/operation/updateFreeTierBucket)Update Free Tier Bucket 

Updates an existing free tier bucket. Only bucket memory quota is configurable. Once created bucket name cannot be changed.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |

##### Request Body schema: application/json

| memoryAllocationInMbrequired | integer The new amount of memory to allocate for the bucket memory in MiB.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| enableCrossClusterVersioning | boolean (EnableCrossClusterVersioning) This being enabled is a pre-requisite to a few XDCR features. When enabled, each document processed by XDCR will have additional metadata stored, called the Hybrid Logical Vector (HLV), in the document extended attributes (xattrs). The Cross Cluster Versioning setting cannot be disabled after it is enabled. By default, this value reflects what its current value is in the bucket, so omit this setting to leave it as it's current value. See the documentation for enableCrossClusterVersioning and the dependent features for important details on when to enable this setting. |

### Responses

**204** 

Successfully accepted updated bucket configuration.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/freeTier/{bucketId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/freeTier/{bucketId}

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "memoryAllocationInMb": 0,
* "enableCrossClusterVersioning": true
}`

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Free-Tier/operation/deleteFreeTierBucketByID)Delete Free Tier Bucket 

Deletes an existing free tier bucket.

To learn more about bucket configuration, see [Buckets](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/buckets.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |

### Responses

**204** 

Successfully deleted the free tier bucket by its bucket id.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/freeTier/{bucketId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/buckets/freeTier/{bucketId}

### Response samples 

* 403
* 404
* 409
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Network-Peers)Network Peers

Network Peering enables you to configure a secure private network connection between the Virtual Private Cloud (VPC) hosting your applications and the VPC of your Couchbase Capella database. You can set a network peering connection from a Couchbase Capella database hosted with Amazon Web Services (AWS), Google Cloud (GCP) or Azure.

## [](#tag/Network-Peers/operation/postNetworkPeering)Create Network Peering 

Creates a network peering record for Capella. Capella does not support peering of networks between different cloud providers. For example, you cannot peer GCP VPC that hosts Capella cluster with an AWS VPC hosting an application.

* Create configures a Couchbase Capella private networking with the cloud provider. Setting up a private network enables your application to interact with Couchbase Capella over a private connection by co-locating them through network peering.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| namerequired           | string Name of the peering relationship. - The name of the peering relationship must be at least 2 characters long. - The name can not exceed 128 characters. |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| providerTyperequired   | string Type of the cloud provider for which the peering connection is created. Which are- 1\. aws 2\. gcp 3\. azure                                           |
| providerConfigrequired | AWSConfigData (object) or GCPConfigData (object) or AzureConfigData (object) The config data for a peering relationship for a cluster on AWS, GCP, or Azure.  |

### Responses

**201** 

Successfully created network peering.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/networkPeers

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/networkPeers

### Request samples 

* Payload

Content type

application/json

Example

PostNetworkPeersAWSPostNetworkPeersGCPPostNetworkPeersAzurePostNetworkPeersAWS

Copy

 Expand all  Collapse all 

`{
* "name": "VPCPeerTestAWS",
* "providerType": "aws",
* "providerConfig": {
  * "accountID": 123456789110,
  * "vpcId": "vpc-00ff00ff00ff0f",
  * "region": "us-east-1",
  * "cidr": "10.1.0.0/23"  
}
}`

### Response samples 

* 201
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/Network-Peers/operation/listNetworkPeeringRecords)List Network Peering Records 

Lists all the network peering records.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                             |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                   |
| sortBy        | Array of strings Example: sortBy=nameSets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **id**, **name**, **status**. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                          |

### Responses

**200** 

Successfully listed all the network peering records.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/networkPeers

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/networkPeers

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "name": "VPCPeerTest",
    * "status": {
      * "state": "complete",
      * "reasoning": "sample_reasoning"  
      },
    * "providerConfig": {
      * "providerId": "pcx-000000fff000fff",
      * "AWSConfig": {
        * "accountId": "00000011123",
        * "vpcId": "vpc-141f0fffff141aa00",
        * "region": "us-east-1",
        * "cidr": "10.0.0.0/16"  
            }  
      },
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56Z",
      * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "modifiedAt": "2021-09-01T12:34:56Z",
      * "version": 1  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/Network-Peers/operation/getNetworkPeeringRecord)Get Network Peering record 

Fetches the details of the network peering meta data based on the peerID provided.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.  |
| ---------------------- | ---------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.       |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.       |
| peerIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The ID of the network peer record. |

### Responses

**200** 

Successfully fetched the network peering meta data based on the peerID.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/networkPeers/{peerId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/networkPeers/{peerId}

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "name": "VPCPeerTest",
* "status": {
  * "state": "complete",
  * "reasoning": "sample_reasoning"  
},
* "commands": [
  * "string"  
],
* "providerConfig": {
  * "providerId": "pcx-000000fff000fff",
  * "AWSConfig": {
    * "accountId": "00000011123",
    * "vpcId": "vpc-141f0fffff141aa00",
    * "region": "us-east-1",
    * "cidr": "10.0.0.0/16"  
  }  
},
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
}
}`

## [](#tag/Network-Peers/operation/deleteNetworkPeering)Delete Network Peering 

Deletes the network peering relationship.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.  |
| ---------------------- | ---------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.       |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.       |
| peerIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The ID of the network peer record. |

### Responses

**204** 

Successfully deleted the network peering relationship.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/networkPeers/{peerId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/networkPeers/{peerId}

### Response samples 

* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Network-Peers/operation/getAzureVnetPeeringCommand)Get Azure VNET Peering CLI Command 

Retrieves the role assignment command or script to be executed in the Azure CLI to assign a new network contributor role. It scopes only to the specified subscription and the virtual network within that subscription.

* Before using this API, please make sure that the _Admin consent granting_ process has been completed through the Capella UI.
* This process to grant consent to the VNET peering service principal in the external Azure tenant needs to be done only once for the organization i.e. the first time when the VNET peering is created.
* Consenting to this permission request creates a service principal that grants Capella access to the Azure tenant to perform VNET peering.
* To complete the admin consent granting process, the Organization owner should follow the steps below -

  1. Login to the Capella UI.
  2. Deploy an Azure Cluster or open an existing one you want to peer with your application.
  3. Click the Settings tab, in the navigation pane click VNET Peering.
  4. Click Setup VNET Peering.
  5. Confirm that you have a user with the Global Administrator Role.
  6. Add the Azure configuration details to allow peering access.
  7. Click Allow Peering Access - A new browser tab opens. Sign in to Azure if you have not already.
  8. In Azure, accept Capella's permissions request - The Azure permissions request page is open in the new browser tab and consent to the new permissions request. For more information refer \[docs\]- <https://docs.couchbase.com/cloud/clouds/vpc-peering/peer-azure.html>
* On accepting the new permission, you automatically return to the Capella VNET peering page. The Capella VNET peering page shows a notice indicating that peering access is successful.
* The Organization Owner should set this up once, then for network peering, use the public API -

  1. Use this `Get Azure VNET Peering CLI Command` API to fetch the command.
  2. Run the role assignment command in the Azure CLI.
  3. Use the `Create VPC Peering` API to create the network peering.
* In order to access this endpoint, the provided API key must have at least one of the following roles:

  * Organization Owner
  * Project Owner

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| tenantIdrequired                    | string The Azure tenant ID. To find your tenant ID, see [How to find your Azure Active Directory tenant ID](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant).                                                                                               |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| subscriptionIdrequired              | string Subscription ID is a GUID that uniquely identifies your subscription to use Azure services. To find your subscription ID, see [Find your Azure subscription](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id#find-your-azure-subscription).  |
| resourceGrouprequired               | string The resource group name holding the resource you're connecting with Capella.                                                                                                                                                                                                 |
| vnetIdrequired                      | string The VNet ID is the name of the virtual network in Azure.                                                                                                                                                                                                                     |
| vnetPeeringServicePrincipalrequired | string The enterprise application object ID for the Capella service principal. You can find the enterprise application object ID in Azure by selecting Azure Active Directory -> Enterprise applications. Next, select the application name, the object ID is in the Object ID box. |

### Responses

**200** 

Successfully provided command to create a network peering.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/networkPeers/networkPeerCommand

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/networkPeers/networkPeerCommand

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "tenantId": "ffffffff-aaaa-1414-eeee-000000000000",
* "subscriptionId": "ffffffff-aaaa-1414-eeee-000000000000",
* "resourceGroup": "sample-resource-group",
* "vnetId": "sample-vnet",
* "vnetPeeringServicePrincipal": "ffffffff-aaaa-1414-eeee-000000000000"
}`

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "command": "az role assignment create \\ --assignee-object-id ffffffff-aaaa-1414-eeee-000000000000 \\ --role \"Network Contributor\" \\ --scope /subscriptions/ffffffff-aaaa-1414-eeee-000000000000/resourceGroups/cb-private-net-demo/providers/Microsoft.Network/virtualNetworks/vnet-test \\ --assignee-principal-type ServicePrincipal"
}`

## [](#tag/OnOff-Schedule)On/Off Schedule

The On/Off Schedule endpoint enables you to schedule when your provisioned database should turn on or off to save costs. Turning off your database only turns off the compute; all of your data, schema (buckets, scopes, and collections), and indexes remain, as well as your cluster configuration, including users and allow lists. When you turn your provisioned database off, you will be charged the OFF amount for the database. You can turn the cluster and any linked app services on or off on demand using the [cluster API](https://docs.couchbase.com/cloud/management-api-reference/index.html#tag/clusters).

## [](#tag/OnOff-Schedule/operation/postOnOffSchedule)Create Cluster On/Off schedule 

This provides the means to add a new cluster on/off schedule.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| timezonerequired | string (onOffTimezone) Enum: "Pacific/Midway" "US/Hawaii" "US/Alaska" "US/Pacific" "US/Mountain" "US/Central" "US/Eastern" "America/Puerto\_Rico" "Canada/Newfoundland" "America/Argentina/Buenos\_Aires" "Atlantic/Cape\_Verde" "Europe/London" "Europe/Amsterdam" "Europe/Athens" "Africa/Nairobi" "Asia/Tehran" "Indian/Mauritius" "Asia/Karachi" "Asia/Calcutta" "Asia/Dhaka" "Asia/Bangkok" "Asia/Hong\_Kong" "Asia/Tokyo" "Australia/North" "Australia/Sydney" "Pacific/Ponape" "Antarctica/South\_Pole" Timezone for the schedule |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| daysrequired     | Array of objects (Days)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### Responses

**204** 

Successfully created the cluster on/off schedule based on the clusterId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/onOffSchedule

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/onOffSchedule

### Request samples 

* Payload

Content type

application/json

Example

PostClusterOnOffSchedulePostClusterOnOffScheduleDefaultBoundaryWithoutToBodyPostClusterOnOffScheduleDefaultsBoundaryWithoutHourMinutePostClusterOnOffScheduleDefaultsBoundaryPostClusterOnOffScheduleDefaultsBoundaryWithoutHourMinuteBodyPostClusterOnOffSchedule

Copy

 Expand all  Collapse all 

`{
* "timezone": "US/Pacific",
* "days": [
  * {
    * "day": "monday",
    * "state": "custom",
    * "from": {
      * "hour": 12,
      * "minute": 30  
      },
    * "to": {
      * "hour": 14,
      * "minute": 30  
      }  
  },
  * {
    * "day": "tuesday",
    * "state": "custom",
    * "from": {
      * "hour": 21,
      * "minute": 30  
      },
    * "to": {
      * "hour": 23,
      * "minute": 30  
      }  
  },
  * {
    * "day": "wednesday",
    * "state": "on"  
  },
  * {
    * "day": "thursday",
    * "state": "on"  
  },
  * {
    * "day": "friday",
    * "state": "custom",
    * "from": {
      * "hour": 12,
      * "minute": 30  
      },
    * "to": {
      * "hour": 15,
      * "minute": 30  
      }  
  },
  * {
    * "day": "saturday",
    * "state": "off"  
  },
  * {
    * "day": "sunday",
    * "state": "off"  
  }  
]
}`

### Response samples 

* 403
* 404
* 409
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/OnOff-Schedule/operation/getOnOffSchedule)Get Cluster On/Off schedule 

Fetches the details of the cluster on/off schedule for the given cluster.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**200** 

Successfully fetched the cluster on/off schedule based on the clusterId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/onOffSchedule

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/onOffSchedule

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "activationStatus": "active",
* "timezone": "US/Pacific",
* "days": [
  * {
    * "day": "monday",
    * "state": "custom",
    * "from": {
      * "hour": 12,
      * "minute": 30  
      },
    * "to": {
      * "hour": 14,
      * "minute": 30  
      }  
  },
  * {
    * "day": "tuesday",
    * "state": "custom",
    * "from": {
      * "hour": 12,
      * "minute": 30  
      },
    * "to": {
      * "hour": 14,
      * "minute": 30  
      }  
  },
  * {
    * "day": "wednesday",
    * "state": "on"  
  },
  * {
    * "day": "thursday",
    * "state": "on"  
  },
  * {
    * "day": "friday",
    * "state": "custom",
    * "from": {
      * "hour": 12,
      * "minute": 30  
      },
    * "to": {
      * "hour": 14,
      * "minute": 30  
      }  
  },
  * {
    * "day": "saturday",
    * "state": "off"  
  },
  * {
    * "day": "sunday",
    * "state": "off"  
  }  
]
}`

## [](#tag/OnOff-Schedule/operation/putOnOffSchedule)Update Cluster On/Off schedule 

This provides the means to update an existing cluster on/off schedule.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| timezonerequired | string (onOffTimezone) Enum: "Pacific/Midway" "US/Hawaii" "US/Alaska" "US/Pacific" "US/Mountain" "US/Central" "US/Eastern" "America/Puerto\_Rico" "Canada/Newfoundland" "America/Argentina/Buenos\_Aires" "Atlantic/Cape\_Verde" "Europe/London" "Europe/Amsterdam" "Europe/Athens" "Africa/Nairobi" "Asia/Tehran" "Indian/Mauritius" "Asia/Karachi" "Asia/Calcutta" "Asia/Dhaka" "Asia/Bangkok" "Asia/Hong\_Kong" "Asia/Tokyo" "Australia/North" "Australia/Sydney" "Pacific/Ponape" "Antarctica/South\_Pole" Timezone for the schedule |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| daysrequired     | Array of objects (Days)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### Responses

**204** 

Successfully updated the cluster on/off schedule based on the clusterId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/onOffSchedule

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/onOffSchedule

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "timezone": "US/Pacific",
* "days": [
  * {
    * "day": "monday",
    * "state": "custom",
    * "from": {
      * "hour": 12,
      * "minute": 30  
      },
    * "to": {
      * "hour": 14,
      * "minute": 30  
      }  
  },
  * {
    * "day": "tuesday",
    * "state": "custom",
    * "from": {
      * "hour": 12,
      * "minute": 30  
      },
    * "to": {
      * "hour": 14,
      * "minute": 30  
      }  
  },
  * {
    * "day": "wednesday",
    * "state": "on"  
  },
  * {
    * "day": "thursday",
    * "state": "on"  
  },
  * {
    * "day": "friday",
    * "state": "custom",
    * "from": {
      * "hour": 12,
      * "minute": 30  
      },
    * "to": {
      * "hour": 14,
      * "minute": 30  
      }  
  },
  * {
    * "day": "saturday",
    * "state": "off"  
  },
  * {
    * "day": "sunday",
    * "state": "off"  
  }  
]
}`

### Response samples 

* 403
* 404
* 409
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/OnOff-Schedule/operation/deleteOnOffSchedule)Delete Cluster On/Off schedule 

Deletes the cluster on/off schedule for the given cluster.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**204** 

Successfully deleted the cluster on/off schedule by its clusterId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/onOffSchedule

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/onOffSchedule

### Response samples 

* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/OnOff-Schedule/operation/pauseClusterOnOffSchedule)Pause Cluster On/Off Schedule 

Temporarily suspends the cluster on/off schedule without deleting its configuration. While paused, the cluster will not automatically start or stop based on the defined schedule. You can resume the schedule at any time using the corresponding unpause endpoint.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**204** 

Successfully paused the cluster on/off schedule

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/onOffSchedule/activationState

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/onOffSchedule/activationState

### Response samples 

* 403
* 404
* 409
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/OnOff-Schedule/operation/unpauseClusterOnOffSchedule)Unpause Cluster On/Off Schedule 

Unpause cluster on/off schedule

 In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**204** 

Successfully unpaused the cluster on/off schedule

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/onOffSchedule/activationState

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/onOffSchedule/activationState

### Response samples 

* 403
* 404
* 409
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Organizations)Organizations

Couchbase Capella uses an ordered hierarchy to help you keep all of your data organized and securely accessible. The entity at the top of the hierarchy is called an organization. Everything you do in Capella, whether it's creating a cluster or managing billing, happens within the scope of an organization.

## [](#tag/Organizations/operation/getOrganizationByID)Get Organization 

Fetches the details of an organization by ID.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Creator
* Organization Member

To learn more, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

### Responses

**200** 

Successfully returned the organization details.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "name": "My-Organization",
* "subdomain": "abc",
* "description": "The description of the organization.",
* "preferences": {
  * "sessionDuration": 3600  
},
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
}
}`

## [](#tag/Organizations/operation/putOrganizationConfiguration)Update Organization Configuration 

Updates an existing organization configuration. Use this endpoint to add, update, and delete network subdomains.

Subdomains are not automatically available. You must contact Couchbase support to enable this feature. To open a Support ticket, see [Create a Support Ticket](https://docs.couchbase.com/cloud/support/manage-support.html#create-support-ticket).

Subdomains:

* Can have a maximum of 30 alphanumeric characters.
* Must be a unique string and not already in use in another tenant or organization. Empty strings are allowed.
* Only affect new clusters. You cannot update existing clusters to include a new subdomain.

In order to access this endpoint, the provided API key must have the following role:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### header Parameters

| If-Match | string Example: 12A precondition header that specifies the entity tag of a resource. |
| -------- | ------------------------------------------------------------------------------------ |

##### Request Body schema: application/json

| subdomainrequired | string <= 30 characters The new name of the subdomain for the organization. |
| ----------------- | --------------------------------------------------------------------------- |

### Responses

**204** 

Successfully updated the organization configuration.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/configuration

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/configuration

### Request samples 

* Payload

Content type

application/json

Example

UpdateSubdomainDeleteSubdomainUpdateSubdomain

Copy

`{
* "subdomain": "abc"
}`

### Response samples 

* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Organizations/operation/listOrganizations)List Organizations 

Returns a list of all organizations the user has access to.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Creator
* Organization Member

To learn more, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html).

##### Authorizations:

_token_

### Responses

**200** 

Successfully listed all the organizations.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations

https://cloudapi.cloud.couchbase.com/v4/organizations

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "name": "My-Organization",
    * "subdomain": "abc",
    * "description": "The description of the organization.",
    * "preferences": {
      * "sessionDuration": 3600  
      },
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56Z",
      * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "modifiedAt": "2021-09-01T12:34:56Z",
      * "version": 1  
      }  
  }  
]
}`

## [](#tag/Private-Endpoint-Service)Private Endpoint Service

Access your Capella cluster from your cloud provider's private network.

## [](#tag/Private-Endpoint-Service/operation/getPrivateEndpointServiceStatus)Get Private Endpoint Service Status 

Private endpoint service allows you to access your Capella cluster from your private network, using private endpoints.

This endpoint determines if the endpoint service is enabled or disabled on your cluster, and shows which routes are configured to use private endpoints. The REST route (port 18091) is used by XDCR, so enabling it allows XDCR to use private endpoints. The `routes` field is only present when private endpoint service is enabled (`enabled: true`), showing the current state of each route (e.g., `xdcr: true` if enabled, `xdcr: false` if disabled). When private endpoint service is disabled (`enabled: false`), the `routes` field is not included in the response.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**200** 

Successfully retrieved private endpoint status of cluster.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/privateEndpointService

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/privateEndpointService

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "enabled": true,
* "status": "enabled",
* "routes": {
  * "xdcr": true,
  * "metrics": false  
}
}`

## [](#tag/Private-Endpoint-Service/operation/enablePrivateEndpointService)Enable Private Endpoint Service 

Enable private endpoint service on your cluster.

Supporting infrastructure is deployed and it may take a few minutes for private endpoints to be available. After it's enabled, you can create private endpoint in your network. You can do this using the cloud provider's CLI. For an example, use the POST privateEndpointService/endpointCommand endpoint to get the command.

You can optionally enable routes such as REST API (port 18091) to use private endpoints at the time of enablement. Enabling the REST route allows XDCR to use private endpoints since XDCR uses the REST API.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Manager
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| routes | object Routes configuration for private endpoints. Only present when private endpoint service is enabled (enabled: true), showing the current state of each route (true if enabled, false if disabled). |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**202** 

Successfully submitted request to enable private endpoint service.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/privateEndpointService

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/privateEndpointService

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "routes": {
  * "xdcr": true,
  * "metrics": false  
}
}`

### Response samples 

* 400
* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Private-Endpoint-Service/operation/updatePrivateEndpointService)Update Private Endpoint Service Configuration 

Update the configuration of routes to use private endpoints after private endpoint service has been enabled.

This endpoint allows you to enable or disable private endpoint usage for routes. The REST route (port 18091) is used by XDCR, so enabling it allows XDCR to use private endpoints, while disabling it stops routing XDCR traffic via private endpoints. Setting a route to true routes traffic through private endpoints, while setting it to false stops routing that route's traffic via private endpoints.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Manager
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| routesrequired | object Routes configuration for private endpoints. Only present when private endpoint service is enabled (enabled: true), showing the current state of each route (true if enabled, false if disabled). |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**202** 

Successfully submitted request to update private endpoint service configuration.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/privateEndpointService

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/privateEndpointService

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "routes": {
  * "xdcr": true,
  * "metrics": false  
}
}`

### Response samples 

* 400
* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Private-Endpoint-Service/operation/disablePrivateEndpointService)Disable Private Endpoint Service 

Disable private endpoint service on your cluster.

Supporting infrastructure is removed and it may take a few minutes before private endpoints is disabled.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**202** 

Successfully submitted request to disable private endpoint service.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/privateEndpointService

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/privateEndpointService

### Response samples 

* 400
* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Private-Endpoint-Service/operation/listPrivateEndpoints)List Private Endpoints 

Returns a list of private endpoints associated with the endpoint service for your Capella cluster, along with the endpoint state. Each private endpoint connects a private network to the Capella cluster.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Creator
* Project Viewer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**200** 

Successfully retrieved list of private endpoints.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/privateEndpointService/endpoints

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/privateEndpointService/endpoints

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "privateEndpointDNS": "abcdef123456.pl.cloud.couchbase.com",
* "endpoints": [
  * {
    * "id": "vpce-000000000000aaaaa",
    * "serviceName": "com.amazonaws.vpce.us-east-1.vpce-svc-000000000000aaaaa",
    * "status": "linked"  
  }  
]
}`

## [](#tag/Private-Endpoint-Service/operation/getPrivateEndpointCommand)Get Private Endpoint CLI Command required to setup private endpoint for specific CSP 

Retrieve the command or script to be executed in order to create the private endpoint which will provides a private connection between the specified VPC and the specified Capella private endpoint service. An example for AWS:

```
aws ec2 create-vpc-endpoint \
  --vpc-id vpc-1234 \
  --region us-east-1 \
  --service-name com.amazonaws.vpce.us-east-1.vpce-svc-1234 \
  --vpc-endpoint-type Interface \
  --subnet-ids subnet-1234

```

An example for Azure:

```
az network private-endpoint create \
  --connection-name connection-1 \
  --name private-endpoint \
  --private-connection-resource-id svc-1 \
  --resource-group test-rg \
  --subnet subnet-1 \
  --group-id sites \
  --vnet-name vnet-1

```

An example for GCP:

```
#!/bin/bash
REGION='us-east1'
NETWORK='psc-test'
SUBNET='psc-test-1'
CLUSTER='cluster-id'
# Do not change
BASE_DNS_NAME='private-endpoint.random.cloud.couchbase.com'
SERVICE_ATTACHMENT=''projects/project-id/regions/us-east1/serviceAttachments/psc-id''
BOOTSTRAP_SERVICE=''projects/project-id/regions/us-east1/serviceAttachments/psc-bootstrap-id''

NETWORK_SHORT=${NETWORK:0:15}
CLUSTER_SHORT=${CLUSTER:0:15}

# Create private DNS zone
gcloud dns managed-zones create $NETWORK_SHORT-$CLUSTER_SHORT --description="Private Endpoint for Capella cluster" --dns-name=$BASE_DNS_NAME --networks=$NETWORK --visibility=private
gcloud dns record-sets transaction start --zone=$NETWORK_SHORT-$CLUSTER_SHORT

# Create attachments and DNS records
gcloud compute addresses create pe-address-$NETWORK_SHORT-$CLUSTER_SHORT --region=$REGION --subnet=$SUBNET
IP_ADDRESS=$(gcloud compute addresses list --filter="name=pe-address-$NETWORK_SHORT-$CLUSTER_SHORT AND region:$REGION AND subnetwork:$SUBNET" --format="value(address)")
gcloud compute forwarding-rules create endpoint-$NETWORK_SHORT-$CLUSTER_SHORT --region=$REGION --network=$NETWORK --address=pe-address-$NETWORK_SHORT-$CLUSTER_SHORT --target-service-attachment=$SERVICE_ATTACHMENT
gcloud dns record-sets transaction add $IP_ADDRESS --name=pe.$BASE_DNS_NAME --type=A --ttl=300 --zone=$NETWORK_SHORT-$CLUSTER_SHORT

gcloud compute addresses create pe-address-bootstrap-$NETWORK_SHORT-$CLUSTER_SHORT --region=$REGION --subnet=$SUBNET
IP_ADDRESS=$(gcloud compute addresses list --filter="name=pe-address-bootstrap-$NETWORK_SHORT-$CLUSTER_SHORT AND region:$REGION AND subnetwork:$SUBNET" --format="value(address)")
gcloud compute forwarding-rules create endpoint-bootstrap-$NETWORK_SHORT-$CLUSTER_SHORT --region=$REGION --network=$NETWORK --address=pe-address-bootstrap-$NETWORK_SHORT-$CLUSTER_SHORT --target-service-attachment=$BOOTSTRAP_SERVICE
gcloud dns record-sets transaction add $IP_ADDRESS --name=private-endpoint.$BASE_DNS_NAME --type=A --ttl=300 --zone=$NETWORK_SHORT-$CLUSTER_SHORT

# Execute transactions
gcloud dns record-sets transaction execute --zone=$NETWORK_SHORT-$CLUSTER_SHORT

```

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

One of 

CreateVPCEndpointCommandRequestCreateAzurePrivateEndpointCommandRequestCreateGCPPrivateEndpointCommandRequest

| vpcIDrequired     | string \[ 12 .. 21 \] characters The ID of your virtual network |
| ----------------- | --------------------------------------------------------------- |
| subnetIDsrequired | Array of strings                                                |

### Responses

**200** 

Successfully provided command to create a private endpoint.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/privateEndpointService/endpointCommand

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/privateEndpointService/endpointCommand

### Request samples 

* Payload

Content type

application/json

Example

PostAWSCommandRequestPostAzureCommandRequestPostGCPCommandRequestPostAWSCommandRequest

Copy

 Expand all  Collapse all 

`{
* "vpcID": "vpc-1234",
* "subnetIDs": [
  * "subnet-1234"  
]
}`

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "command": "aws ec2 create-vpc-endpoint --vpc-id vpc-1234 --region us-east-1 --service-name com.amazonaws.vpce.us-east-1.vpce-svc-1234 --vpc-endpoint-type Interface --subnet-ids subnet-1234"
}`

## [](#tag/Private-Endpoint-Service/operation/acceptPrivateEndpoint)Accept Private Endpoint Request 

Accept a new private endpoint connection request so that it is associated with the endpoint service. This means the private endpoint is available for use.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| endpointIdrequired     | string Example: vpce-1234The VPC endpoint ID.                                                 |

### Responses

**204** 

Successfully accepted private endpoint.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/privateEndpointService/endpoints/{endpointId}/associate

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/privateEndpointService/endpoints/{endpointId}/associate

### Response samples 

* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Private-Endpoint-Service/operation/deletePrivateEndpoint)Reject or disassociate Private Endpoint 

Removes the private endpoint associated with the endpoint service. This means the private endpoint is no longer able to connect to the private endpoint service.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| endpointIdrequired     | string Example: vpce-1234The VPC endpoint ID.                                                 |

### Responses

**204** 

Successfully deleted private endpoint.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/privateEndpointService/endpoints/{endpointId}/unassociate

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/privateEndpointService/endpoints/{endpointId}/unassociate

### Response samples 

* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Projects)Projects

Projects contain and allow access to Couchbase databases. Projects are used to organize and manage groups of Couchbase databases within organizations. An organization can contain any number of projects, and a project can contain any number of databases.

## [](#tag/Projects/operation/postProject)Create Project 

Creates a new project under the organization.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Creator

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| namerequired | string <= 128 characters The name of the project (up to 128 characters).            |
| ------------ | ----------------------------------------------------------------------------------- |
| description  | string <= 256 characters A short description of the project (up to 256 characters). |

### Responses

**201** 

Successfully created a project under the organization.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "name": "My Project",
* "description": "My awesome project"
}`

### Response samples 

* 201
* 400
* 403
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/Projects/operation/listProjects)List Project 

Lists all the projects under the organization.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                 |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                       |
| sortBy        | Array of strings Example: sortBy=nameSets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **id**, **name**. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                              |

### Responses

**200** 

Successfully listed all the projects under the organization.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "description": "The description of my awesome project",
    * "name": "My-Awesome-Project",
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56Z",
      * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "modifiedAt": "2021-09-01T12:34:56Z",
      * "version": 1  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/Projects/operation/getProjectByID)Get Project 

Fetches the details of the given project.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

### Responses

**200** 

Successfully fetched the project based on the projectId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "description": "The description of my awesome project",
* "name": "My-Awesome-Project",
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
}
}`

## [](#tag/Projects/operation/putProject)Update Project 

Update project name and or project description.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

##### header Parameters

| If-Match | string Example: 12A precondition header that specifies the entity tag of a resource. |
| -------- | ------------------------------------------------------------------------------------ |

##### Request Body schema: application/json

| namerequired | string <= 128 characters The new project name (up to 128 characters).        |
| ------------ | ---------------------------------------------------------------------------- |
| description  | string <= 256 characters The new project description (up to 256 characters). |

### Responses

**204** 

Successfully updated the project metadata.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "name": "My-New-Project",
* "description": "The extended description of my awesome project."
}`

### Response samples 

* 400
* 403
* 404
* 412
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Projects/operation/deleteProjectByID)Delete Project 

Deletes an existing project.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

### Responses

**204** 

Successfully deleted the project by its projectId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}

### Response samples 

* 403
* 404
* 409
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Query-Indexes)Query Indexes

Used to manage primary and secondary indexes on your Capella cluster. You can CREATE/ALTER/DROP/BUILD indexes.

It is recommended to use deferred index builds, especially for larger indexes. When creating indexes in bulk, we do not recommend sending requests to create all of them at once. Instead, we strongly recommend creating indexes in batches of 100 or less.

## [](#tag/Query-Indexes/operation/manageQueryIndexes)Manage Query Indexes 

CREATE/DROP/ALTER/BUILD primary and secondary indexes.

To learn more about indexes please refer to the [documentation](https://docs.couchbase.com/server/current/learn/services-and-indexes/indexes/indexing-and-query-perf.html).

It is recommended to use deferred index builds, especially for larger indexes. When creating indexes in bulk, we do not recommend sending requests to create all of them at once. Instead, we strongly recommend creating indexes in batches of 100 or less.

To access this endpoint the API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Database Data Reader/Writer

To learn more, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| definitionrequired | string The index DDL statement. This can be a CREATE/DROP/ALTER/BUILD statement. Multiple delimited queries are not allowed. It is recommended to use deferred index builds, especially for larger indexes. When creating indexes in bulk, we do not recommend sending requests to create all of them at once. Instead, we strongly recommend creating indexes in batches of 100 or less. |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**200** 

Successfully sent index DDL statement. A 200 response does not imply that the DDL was successfully executed. It implies that request was accepted but there could be an error in processing the index command.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

Index with specified name was not found in case of DELETE, ALTER or BUILD.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/queryService/indexes

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/queryService/indexes

### Request samples 

* Payload

Content type

application/json

Example

CreateIndexExampleAlterIndexExampleDropIndexExampleBuildIndexExampleCreateIndexExample

Copy

`` {
* "definition": "create index idx1 on `travel-sample`.inventory.route(airline, destinationairport, sourceairport) partition by hash(airline) where id in [1000,2000,3000]"
} ``

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "errors": [
  * {
    * "msg": "Index Not Found - cause: GSI index idx1 not found."  
  }  
]
}`

## [](#tag/Query-Indexes/operation/listIndexDefinitions)Get List Of Index Definitions 

Get index definitions in a keyspace.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### query Parameters

| bucketrequired | string Example: bucket=bucket=travel-sampleSpecifies the bucket part of the key space. To learn more about scopes and collections, see [Buckets, Scopes, and Collections](https://docs.couchbase.com/cloud/clusters/data-service/about-buckets-scopes-collections.html).                                                          |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| scope          | string Example: scope=scope=inventorySpecifies the scope part of the key space. If unspecified, this will be the default scope. To learn more about scopes and collections, see [Buckets, Scopes, and Collections](https://docs.couchbase.com/cloud/clusters/data-service/about-buckets-scopes-collections.html).                 |
| collection     | string Example: collection=collection=hotelSpecifies the collection part of the key space. If unspecified, this will be the default collection. To learn more about scopes and collections, see [Buckets, Scopes, and Collections](https://docs.couchbase.com/cloud/clusters/data-service/about-buckets-scopes-collections.html). |

### Responses

**200** 

Successfully retrieved list of index definitions.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

Index with specified name was not found in case of DELETE, ALTER or BUILD.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/queryService/indexes

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/queryService/indexes

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`` {
* "definitions": [
  * {
    * "indexName": "def_icao",
    * "definition": "CREATE INDEX `def_icao` ON `travel-sample`(`icao`)"  
  }  
]
} ``

## [](#tag/Query-Indexes/operation/indexDefinition)Get Index Properties 

Get the index properties of a specified index in a keyspace.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| indexNamerequired      | string Example: def\_cityThe name of the index.                                               |

##### query Parameters

| bucketrequired | string Example: bucket=bucket=travel-sampleSpecifies the bucket part of the key space. To learn more about scopes and collections, see [Buckets, Scopes, and Collections](https://docs.couchbase.com/cloud/clusters/data-service/about-buckets-scopes-collections.html).                                                          |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| scope          | string Example: scope=scope=inventorySpecifies the scope part of the key space. If unspecified, this will be the default scope. To learn more about scopes and collections, see [Buckets, Scopes, and Collections](https://docs.couchbase.com/cloud/clusters/data-service/about-buckets-scopes-collections.html).                 |
| collection     | string Example: collection=collection=hotelSpecifies the collection part of the key space. If unspecified, this will be the default collection. To learn more about scopes and collections, see [Buckets, Scopes, and Collections](https://docs.couchbase.com/cloud/clusters/data-service/about-buckets-scopes-collections.html). |

### Responses

**200** 

Successfully retrieved index properties.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

Index with specified name was not found in case of DELETE, ALTER or BUILD.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/queryService/indexes/{indexName}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/queryService/indexes/{indexName}

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "defnId": 14488149950011906000,
* "indexName": "idx10",
* "bucket": "travel-sample",
* "scope": "inventory",
* "collection": "airline",
* "isPrimary": false,
* "secExprs": [
  * "destinationairport",
  * "sourceairport"  
],
* "where": "name is valued",
* "numReplica": 1,
* "status": "Ready"
}`

## [](#tag/Query-Indexes/operation/indexBuildStatus)Get Index Build Status 

Monitor the build status of an index.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| indexNamerequired      | string Example: def\_cityThe name of the index.                                               |

##### query Parameters

| bucketrequired | string Example: bucket=bucket=travel-sampleSpecifies the bucket part of the key space. To learn more about scopes and collections, see [Buckets, Scopes, and Collections](https://docs.couchbase.com/cloud/clusters/data-service/about-buckets-scopes-collections.html).                                                          |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| scope          | string Example: scope=scope=inventorySpecifies the scope part of the key space. If unspecified, this will be the default scope. To learn more about scopes and collections, see [Buckets, Scopes, and Collections](https://docs.couchbase.com/cloud/clusters/data-service/about-buckets-scopes-collections.html).                 |
| collection     | string Example: collection=collection=hotelSpecifies the collection part of the key space. If unspecified, this will be the default collection. To learn more about scopes and collections, see [Buckets, Scopes, and Collections](https://docs.couchbase.com/cloud/clusters/data-service/about-buckets-scopes-collections.html). |

### Responses

**200** 

Successfully retrieved build status for a given index.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

Index with specified name was not found in case of DELETE, ALTER or BUILD.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/queryService/indexBuildStatus/{indexName}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/queryService/indexBuildStatus/{indexName}

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "status": "Ready"
}`

## [](#tag/Replications)Replications

Replications (XDCR- Cross Data Center Replication) is a feature that allows you to replicate data across multiple Couchbase clusters. Cross Data Center Replication can protect against data-center failure, and also provide high-performance access to data for globally distributed mission-critical applications.

## [](#tag/Replications/operation/getReplication)Get replication details 

Fetches the details of the given replication.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.        |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.             |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.             |
| replicationIdrequired  | string Example: aBc23DeFgHiJkLmNop6qRsTuVwX4yZaBcDeFgHiJk5LmNoPqRsTuVwXyZ1The ID of the replication. |

### Responses

**200** 

Replication detail response.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/replications/{replicationId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/replications/{replicationId}

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Example

getReplicationgetReplicationAllScopesgetReplicationAllCollectionsgetReplication

Copy

 Expand all  Collapse all 

`{
* "id": "MDIwN23ewrerfetrmZmUzYzExYTcxMTA4MjJkYjJiNmYvdGVzdDEvdGVzdDI=",
* "status": "running",
* "changesLeft": 100,
* "source": {
  * "project": {
    * "id": "44508406-5ef0-4b0b-be9f-f31dcc422ea0",
    * "name": "SourceProject"  
  },
  * "cluster": {
    * "id": "a86f56c2-c4b4-425c-8df6-fddd6e2c7ddb",
    * "name": "SourceCluster"  
  },
  * "bucket": {
    * "id": "dGVzdA",
    * "name": "SourceBucket",
    * "conflictResolutionType": "seqno"  
  },
  * "scopes": [
    * {
      * "name": "source-scope-1",
      * "collections": [
        * "source-collection-1",
        * "source-collection-2"  
            ]  
      },
    * {
      * "name": "source-scope-2",
      * "collections": [
        * "source-collection-3"  
            ]  
      }  
  ]  
},
* "target": {
  * "project": {
    * "id": "55619517-6fg1-5c1c-cf0g-g42edd533fb1",
    * "name": "TargetProject"  
  },
  * "cluster": {
    * "id": "b95f56d2-d4c4-425c-8df6-eee7c2c8edab",
    * "name": "TargetCluster"  
  },
  * "bucket": {
    * "id": "dPVzdB",
    * "name": "TargetBucket",
    * "conflictResolutionType": "seqno"  
  },
  * "scopes": [
    * {
      * "name": "target-scope-2",
      * "collections": [
        * "target-collection-2",
        * "target-collection-4"  
            ]  
      },
    * {
      * "name": "target-scope-3",
      * "collections": [
        * "target-collection-5"  
            ]  
      }  
  ]  
},
* "mappings": [
  * {
    * "sourceScope": "source-scope-1",
    * "targetScope": "target-scope-2",
    * "collections": [
      * {
        * "sourceCollection": "source-collection-1",
        * "targetCollection": "target-collection-2"  
            },
      * {
        * "sourceCollection": "source-collection-2",
        * "targetCollection": "target-collection-4"  
            }  
      ]  
  },
  * {
    * "sourceScope": "source-scope-2",
    * "targetScope": "target-scope-3",
    * "collections": [
      * {
        * "sourceCollection": "source-collection-3",
        * "targetCollection": "target-collection-5"  
            }  
      ]  
  }  
],
* "direction": "oneWay",
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z"  
}
}`

## [](#tag/Replications/operation/deleteReplication)Delete a replication 

Deletes the specified replication.

Note: Deleting an already-deleted replication returns a 404 Not Found.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html). 

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.        |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.             |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.             |
| replicationIdrequired  | string Example: aBc23DeFgHiJkLmNop6qRsTuVwX4yZaBcDeFgHiJk5LmNoPqRsTuVwXyZ1The ID of the replication. |

### Responses

**204** 

Replication deleted successfully.

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/replications/{replicationId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/replications/{replicationId}

### Response samples 

* 400
* 401
* 403
* 404
* 409
* 422
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Replications/operation/updateReplication)Update an existing replication 

Update the configuration of an existing replication.

**Update Behavior**:

Only fields included in the request body will be updated. Omitted fields remain unchanged.

**Note on Mappings**:

When updating the mappings, you have three options:

* **Keep current settings**: Omit the `mappings` field & `allScopes` field entirely
* **Set explicit mappings**: Include `mappings` array with scope and/or collection definitions
* **Replicate full bucket**: Include `allScopes: true` instead of mappings

You cannot specify both `mappings` and `allScopes: true` in the same request.

**Note on Filter Expression Updates**:

When the `filter.expressions.regEx` value is updated, the user must explicitly set `filter.expressions.skipRestream` to indicate the desired behavior:

* If `skipRestream` is `false` (default), the replication will be saved and restarted to apply the new filter expression to all data.
* If `skipRestream` is `true`, the new filter expression will apply **only to new mutations**, and the replication will not be restarted.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html). 

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.        |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.             |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.             |
| replicationIdrequired  | string Example: aBc23DeFgHiJkLmNop6qRsTuVwX4yZaBcDeFgHiJk5LmNoPqRsTuVwXyZ1The ID of the replication. |

##### Request Body schema: application/json

required

| priority          | string Default: "high" Enum: "low" "medium" "high" Priority represents the resource allocation to the replication. low: Resource constraints are applied when competing with high priority replications medium: Resource constraints are applied during initial processing when competing with high priority replications, then operates as high priority high: No resource constraints are applied (default priority) |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| networkUsageLimit | integer Default: 0 Network usage limit in MiB per second. Default is 0 meaning it is unlimited.                                                                                                                                                                                                                                                                                                                        |
| filter            | object (filter) Filter contains the replication settings which are passed to the Couchbase server API while creating a replication.                                                                                                                                                                                                                                                                                    |
| allScopes         | boolean Default: false If true, all scopes will be replicated. If false, the scopes specified in the mappings field will be replicated.                                                                                                                                                                                                                                                                                |
| mappings          | Array of objects (mappings) Defines mappings from source to target scopes and collections. This field is only required if you are replicating specific scopes and collections. Note: If the collections array is empty or omitted, it implies all collections under that scope would be replicated.                                                                                                                    |

### Responses

**204** 

Replication updated successfully.

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/replications/{replicationId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/replications/{replicationId}

### Request samples 

* Payload

Content type

application/json

Example

updateReplicationupdateReplicationAllScopesupdateReplicationScopesupdateReplicationAllFiltersupdateReplicationFilterExpressionsupdateReplication

Copy

 Expand all  Collapse all 

`{
* "priority": "high",
* "networkUsageLimit": 100,
* "filter": {
  * "documentExcludeOptions": {
    * "deletion": false,
    * "expiration": false,
    * "ttl": false,
    * "binary": false  
  },
  * "expressions": {
    * "regEx": "REGEXP_CONTAINS(country, \"France\")",
    * "skipRestream": false  
  }  
},
* "mappings": [
  * {
    * "sourceScope": "source-scope-1",
    * "targetScope": "target-scope-1",
    * "collections": [
      * {
        * "sourceCollection": "source-collection-1",
        * "targetCollection": "target-collection-1"  
            },
      * {
        * "sourceCollection": "source-collection-2",
        * "targetCollection": "target-collection-2"  
            }  
      ]  
  }  
]
}`

### Response samples 

* 400
* 401
* 403
* 404
* 409
* 422
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Replications/operation/getReplicationJob)Get replication job details 

Fetches the details of the given replication job.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |
| jobIdrequired          | string <uuid\> Example: 3d4354af-6271-4ba3-aeba-469820d96d12The ID of the job.                |

### Responses

**200** 

Replication job detail response.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/replications/jobs/{jobId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/replications/jobs/{jobId}

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "jobId": "3d4354af-6271-4ba3-aeba-469820d96d12",
* "state": "pending",
* "retryNumber": 1,
* "lastError": "fake error",
* "replicationId": "UmlqdSBpcyBhd2Vzb21l",
* "reverseReplicationId": "MDIwN23ewrerfetrmZmUzYzExYTcxMTA4MjJkYjJiNmYvdGVzdDEvdGVzdDI",
* "lastUpdatedTimestamp": "2021-09-01T12:34:56Z"
}`

## [](#tag/Replications/operation/listClusterReplications)List replications for a given cluster 

Retrieves a paginated list of replications for the specified cluster. 

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html). 

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                                                                                        |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                                                                              |
| sortBy        | Array of strings Example: sortBy=statusSets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **id**, **sourceCluster**, **targetCluster**, **status**, **direction**, **priority**. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                                                                                     |

### Responses

**200** 

List of replications for the cluster.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/replications

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/replications

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "MDIwN23ewrerfetrmZmUzYzExYTcxMTA4MjJkYjJiNmYvdGVzdDEvdGVzdDI=",
    * "sourceCluster": "ClusterA",
    * "targetCluster": "ClusterB",
    * "status": "running",
    * "direction": "oneWay",
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56Z"  
      }  
  },
  * {
    * "id": "MDIwN23ewrerfetrmZmUzYzExYTcxMTA4MjJkYjJiNmYvdGVzdDMvdGVzdDQ=",
    * "sourceCluster": "ClusterA",
    * "targetCluster": "ClusterB",
    * "status": "paused",
    * "direction": "twoWay",
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T13:45:30Z"  
      }  
  },
  * {
    * "id": "MDIwN23ewrerfetrmZmUzYzExYTcxMTA4MjJkYjJiNmYvdGVzdDUvdGVzdDY=",
    * "sourceCluster": "ClusterA",
    * "targetCluster": "ClusterB",
    * "status": "pending",
    * "direction": "oneWay",
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T15:10:22Z"  
      }  
  }  
],
* "cursor": {
  * "hrefs": { },
  * "pages": {
    * "last": 1,
    * "page": 1,
    * "perPage": 5,
    * "totalItems": 3  
  }  
}
}`

## [](#tag/Replications/operation/createReplication)Create a new replication 

Creates a new replication between a source and a target cluster within the specified organization and project.

Note: Replication is created from the perspective of the source cluster. The clusterId in the path should refer to the source cluster.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html). 

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

required

| sourceBucketrequired | string The ID of the source bucket.                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| targetrequired       | object Target contains all the metadata about a replication target.                                                                                                                                                                                                                                                                                                                                                    |
| mode                 | string Default: "async" Enum: "async" "sync" This specifies the replication creation mode.                                                                                                                                                                                                                                                                                                                             |
| mappings             | Array of objects (mappings) Defines mappings from source to target scopes and collections. This field is only required if you are replicating specific scopes and collections. Note: If the collections array is empty or omitted, it implies all collections under that scope would be replicated.                                                                                                                    |
| direction            | string Default: "oneWay" Enum: "oneWay" "twoWay" Direction specifies the replication flow — whether it's oneWay (source to target only) or twoWay (also from target back to source).                                                                                                                                                                                                                                   |
| priority             | string Default: "high" Enum: "low" "medium" "high" Priority represents the resource allocation to the replication. low: Resource constraints are applied when competing with high priority replications medium: Resource constraints are applied during initial processing when competing with high priority replications, then operates as high priority high: No resource constraints are applied (default priority) |
| networkUsageLimit    | integer Default: 0 Network usage limit in MiB per second. 0 means unlimited.                                                                                                                                                                                                                                                                                                                                           |
| filter               | object (filter) Filter contains the replication settings which are passed to the Couchbase server API while creating a replication.                                                                                                                                                                                                                                                                                    |

### Responses

**201** 

Replication created successfully.

**202** 

Replication creation started asynchronously.

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/replications

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/replications

### Request samples 

* Payload

Content type

application/json

Example

createReplicationcreateReplicationAsynccreateReplicationSynccreateReplicationAllScopescreateReplicationAllCollectionscreateReplicationWithFilterscreateReplicationSelfManagedTargetcreateReplication

Copy

 Expand all  Collapse all 

`{
* "sourceBucket": "dGVzdA",
* "target": {
  * "cluster": "b95f56d2-d4c4-425c-8df6-eee7c2c8edab",
  * "bucket": "dPVzdB"  
},
* "mappings": [
  * {
    * "sourceScope": "source-scope-1",
    * "targetScope": "target-scope-1",
    * "collections": [
      * {
        * "sourceCollection": "source-collection-1",
        * "targetCollection": "target-collection-1"  
            },
      * {
        * "sourceCollection": "source-collection-2",
        * "targetCollection": "target-collection-2"  
            }  
      ]  
  }  
]
}`

### Response samples 

* 201
* 202
* 400
* 401
* 403
* 404
* 409
* 422
* 500

Content type

application/json

Copy

`{
* "replicationId": "MDIwN23ewrerfetrmZmUzYzExYTcxMTA4MjJkYjJiNmYvdGVzdDEvdGVzdDI=",
* "reverseReplicationId": "MDIwN23ewrerfetrmZmUzYzExYTcxMTA4MjJkYjJiNmYvdGVzdDEvdGVzdDI="
}`

## [](#tag/Replications/operation/listProjectReplications)List replications for a given project 

Retrieves a paginated list of replications for the specified project. 

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html). 

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                                                                                        |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                                                                              |
| sortBy        | Array of strings Example: sortBy=statusSets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **id**, **sourceCluster**, **targetCluster**, **status**, **direction**, **priority**. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                                                                                     |

### Responses

**200** 

List of replications for the project.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/replications

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/replications

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "MDIwN23ewrerfetrmZmUzYzExYTcxMTA4MjJkYjJiNmYvdGVzdDEvdGVzdDI=",
    * "sourceCluster": "ClusterA",
    * "targetCluster": "ClusterB",
    * "status": "running",
    * "direction": "oneWay",
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56Z"  
      }  
  },
  * {
    * "id": "MDIwN23ewrerfetrmZmUzYzExYTcxMTA4MjJkYjJiNmYvdGVzdDMvdGVzdDQ=",
    * "sourceCluster": "ClusterA",
    * "targetCluster": "ClusterB",
    * "status": "paused",
    * "direction": "twoWay",
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T13:45:30Z"  
      }  
  },
  * {
    * "id": "MDIwN23ewrerfetrmZmUzYzExYTcxMTA4MjJkYjJiNmYvdGVzdDUvdGVzdDY=",
    * "sourceCluster": "ClusterA",
    * "targetCluster": "ClusterB",
    * "status": "pending",
    * "direction": "oneWay",
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T15:10:22Z"  
      }  
  }  
],
* "cursor": {
  * "hrefs": { },
  * "pages": {
    * "last": 1,
    * "page": 1,
    * "perPage": 5,
    * "totalItems": 3  
  }  
}
}`

## [](#tag/Replications/operation/pauseReplication)Pause a replication 

Deactivates (pauses) a running replication.

Note: Pausing a replication that is not in a valid state returns a 409 Conflict.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html). 

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.        |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.             |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.             |
| replicationIdrequired  | string Example: aBc23DeFgHiJkLmNop6qRsTuVwX4yZaBcDeFgHiJk5LmNoPqRsTuVwXyZ1The ID of the replication. |

### Responses

**204** 

Replication paused successfully.

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/replications/{replicationId}/activationStatus

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/replications/{replicationId}/activationStatus

### Response samples 

* 400
* 401
* 403
* 404
* 409
* 422
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Replications/operation/resumeReplication)Resume a replication 

Resumes a paused replication.

Note: Resuming a replication that is not in a valid state returns a 409 Conflict.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html). 

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.        |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.             |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.             |
| replicationIdrequired  | string Example: aBc23DeFgHiJkLmNop6qRsTuVwX4yZaBcDeFgHiJk5LmNoPqRsTuVwXyZ1The ID of the replication. |

### Responses

**204** 

Replication resumed successfully.

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/replications/{replicationId}/activationStatus

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/replications/{replicationId}/activationStatus

### Response samples 

* 400
* 401
* 403
* 404
* 409
* 422
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Sample-Bucket)Sample Bucket

The sampleBucket endpoint lets users easily create a bucket filled with sample data. This is a quick way for users to try out features and learn how things work with ready-to-use data.

## [](#tag/Sample-Bucket/operation/postSampleBucket)Load Sample Data 

Loads predefined sample data into a cluster by selecting from three available options:

* travel-sample
* gamesim-sample
* beer-sample

Upon a successful request, a new bucket is created within the cluster, and populated with the chosen sample data.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| namerequired | string Enum: "travel-sample" "gamesim-sample" "beer-sample" The name of the sample dataset to be loaded. The name has to be one of the following sample datasets. travel-sample gamesim-sample beer-sample |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**201** 

Successfully started sample data load.

**403** 

The client does not have the necessary permissions to access this resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/sampleBuckets

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/sampleBuckets

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "name": "travel-sample"
}`

### Response samples 

* 201
* 403
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "bucketId": "dGVzdA",
* "name": "travel-sample"
}`

## [](#tag/Sample-Bucket/operation/listSampleBuckets)List Sample Data Import Buckets 

Lists all the sample buckets under the organization.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

### Responses

**200** 

Successfully listed all the sample buckets under the organization.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/sampleBuckets

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/sampleBuckets

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "dGVzdA",
    * "name": "My-First-Bucket",
    * "type": "string",
    * "storageBackend": "couchstore",
    * "vbuckets": 128,
    * "memoryAllocationInMb": 100,
    * "bucketConflictResolution": "string",
    * "durabilityLevel": "string",
    * "replicas": 0,
    * "flush": false,
    * "flushEnabled": false,
    * "timeToLiveInSeconds": 100,
    * "enableCrossClusterVersioning": true,
    * "evictionPolicy": "fullEviction",
    * "stats": {
      * "itemCount": 10,
      * "opsPerSecond": 0,
      * "diskUsedInMib": 17,
      * "memoryUsedInMib": 50  
      },
    * "priority": 0  
  }  
],
* "clusterStats": {
  * "freeMemoryInMb": 640,
  * "totalMemoryInMb": 1040,
  * "maxReplicas": 2  
}
}`

## [](#tag/Sample-Bucket/operation/getSampleBucketById)Get Sample Import Bucket 

Fetches the configuration of the given bucket.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |

### Responses

**200** 

Successfully fetched the sample bucket based on the bucketId.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/sampleBuckets/{bucketId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/sampleBuckets/{bucketId}

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "dGVzdA",
* "name": "My-First-Bucket",
* "type": "string",
* "storageBackend": "couchstore",
* "vbuckets": 128,
* "memoryAllocationInMb": 100,
* "bucketConflictResolution": "string",
* "durabilityLevel": "string",
* "replicas": 0,
* "flush": false,
* "flushEnabled": false,
* "timeToLiveInSeconds": 100,
* "enableCrossClusterVersioning": true,
* "evictionPolicy": "fullEviction",
* "stats": {
  * "itemCount": 10,
  * "opsPerSecond": 0,
  * "diskUsedInMib": 17,
  * "memoryUsedInMib": 50  
},
* "priority": 0
}`

## [](#tag/Sample-Bucket/operation/deleteSampleDataByBucketID)Delete Sample Import Bucket 

Deletes an existing bucket which was loaded with sample data.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.            |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                 |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                 |
| bucketIdrequired       | string Example: dGVzdAThe ID of the bucket. It is the URL-compatible base64 encoding of the bucket name. |

### Responses

**204** 

Successfully deleted the bucket by its bucketId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/sampleBuckets/{bucketId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/sampleBuckets/{bucketId}

### Response samples 

* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Users)Users

To access an organization, your Couchbase Capella user account must be added to it. Accounts are added to an organization using email invitations sent from Capella by a user with the Organization Owner organization role. All organization users are given one or more organization roles that define what they can view and manage in their organization.

## [](#tag/Users/operation/postUser)Create User 

Invites a new user under the organization.

After making a REST API request, an invitation email is triggered and sent to the user. Upon receiving the invitation email, the user is required to click on a provided URL, which will redirect them to a page with a user interface (UI) where they can set their username and password.

The modification of any personal information related to a user can only be performed by the user through the UI. Similarly, the user can solely conduct password updates through the UI.

The "caller" possessing Organization Owner access rights retains the exclusive user creation capability. They hold the authority to assign roles at the organization and project levels.

At present, our support is limited to the resourceType of "project" exclusively.

In order to access this endpoint, the provided API key must have the following role:

* Organization Owner

To learn more, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| name                      | string <= 128 characters The name of the user.                                                             |
| ------------------------- | ---------------------------------------------------------------------------------------------------------- |
| emailrequired             | string (Email) Email of the user.                                                                          |
| organizationRolesrequired | Array of strings (OrganizationRoles) Items Enum: "organizationOwner" "organizationMember" "projectCreator" |
| resources                 | Array of objects (Resource) Default: \[\]                                                                  |

### Responses

**201** 

Successfully sent invite to the user.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/users

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/users

### Request samples 

* Payload

Content type

application/json

Example

CreateOrganizationMemberCreateOrganizationOwnerCreateOrganizationMember

At present, our support is limited to the resourceType of "project" exclusively. Furthermore, the role designation is solely related to roles at the project level.

Copy

 Expand all  Collapse all 

`{
* "name": "John",
* "email": "john.doe@example.com",
* "organizationRoles": [
  * "organizationMember"  
],
* "resources": [
  * {
    * "id": "550e8400-e29b-41d4-a716-446655440000",
    * "type": "project",
    * "roles": [
      * "projectViewer"  
      ]  
  },
  * {
    * "id": "550e8400-e29b-41d4-a716-446655440000",
    * "type": "project",
    * "roles": [
      * "projectDataReaderWriter"  
      ]  
  }  
]
}`

### Response samples 

* 201
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/Users/operation/listUsers)List Users 

Lists all the users in the organization and filter on the basis of projectId.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Organization Member
* Project Creator

The results are always limited by the role and scope of the caller's privileges.

When retrieving a list of users through a GET request, if a user holds the organization owner role, the response will exclude project-level permissions for those users. This is because organization owners have full access to all resources within the organization, making project-level permissions irrelevant for them.

To learn more about the roles, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html) and [Project Roles](https://docs.couchbase.com/cloud/projects/project-roles.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                                                      |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                                            |
| sortBy        | Array of strings Example: sortBy=nameSets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **id**, **name**, **email**, **status**, **inactive**. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                                                   |
| projectId     | string <uuid\> Example: projectId=ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                                                                                                                                 |

### Responses

**200** 

Successfully listed all the user in the organization.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/users

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/users

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Example

ApiKeyIsOrgOwnerApiKeyIsProjectOwnerReturnedUserIsOrganizationOwnerApiKeyIsOrgOwner

In the event that the API key holds "organizationOwner" access, information related to all projects within the organization will be returned.

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "name": "John",
    * "email": "john.doe@example.com",
    * "status": "verified",
    * "inactive": false,
    * "organizationId": "ffffffff-aaaa-1414-eeee-000000000000",
    * "organizationRoles": [
      * "organizationMember"  
      ],
    * "lastLogin": "2023-07-17T07:05:39.116Z",
    * "region": "North America",
    * "timeZone": "(UTC +5:30) India Standard Time",
    * "enableNotifications": false,
    * "expiresAt": "2023-07-17T07:05:39.116Z",
    * "resources": [
      * {
        * "id": "f98e6c87-41e3-4faa-9df4-906e8d4f1aaf",
        * "type": "project",
        * "roles": [
          * "projectViewer"  
                    ]  
            },
      * {
        * "id": "b7c745ac-9fb8-4b63-a0e4-51230097a169",
        * "type": "project",
        * "roles": [
          * "projectDataReaderWriter"  
                    ]  
            },
      * {
        * "id": "28b67422-63d5-46b1-9234-8ad4a1d2f7be",
        * "type": "project",
        * "roles": [
          * "projectDataReaderWriter"  
                    ]  
            },
      * {
        * "id": "e3942eaa-0f52-43da-963d-87a5b6cb3805",
        * "type": "project",
        * "roles": [
          * "projectDataReaderWriter"  
                    ]  
            }  
      ],
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56.000Z",
      * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "modifiedAt": "2021-09-01T12:34:56.000Z",
      * "version": 1  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/Users/operation/getUser)Get User 

Fetches the details of the given user.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Organization Member
* Project Creator

The results are always limited by the role and scope of the caller's privileges.

When performing a GET request for a user with an organization owner role, the response will exclude project-level permissions for that user. This is because organization owners have access to all resources at the organization level, rendering project-level permissions unnecessary for them.

To learn more about the roles, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html) and [Project Roles](https://docs.couchbase.com/cloud/projects/project-roles.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.       |
| ---------------------- | --------------------------------------------------------------------------------------------------- |
| userIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the control plane user. |

### Responses

**200** 

Successfully fetched the user based on the userId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/users/{userId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/users/{userId}

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "name": "alex",
* "email": "john.doe@example.com",
* "status": "not-verified",
* "inactive": false,
* "organizationId": "ffffffff-aaaa-1414-eeee-000000000000",
* "organizationRoles": [
  * "projectCreator"  
],
* "lastLogin": "2023-07-17T07:05:39.116124897Z",
* "region": "North America",
* "timeZone": "(UTC -9:00) Alaska Standard Time",
* "enableNotifications": true,
* "expiresAt": "2023-07-17T07:05:39.116124897Z",
* "resources": [
  * {
    * "type": "project",
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "roles": [
      * "projectManager"  
      ]  
  }  
],
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
}
}`

## [](#tag/Users/operation/patchUser)Update User 

Updates organizationRole and resources of the user.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

An Organization Owner API key can be utilized to update organizational-level roles and project-level roles for all projects within the organization.

The Project Owner API key allows for updating project-level roles, solely within the projects where the API key holds the Project Owner role.

The modification of any personal information related to a user, such as password updates, can only be performed by the respective user through the user interface (UI).

The results are always limited by the role and scope of the caller's privileges. To learn more about the roles, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html) and [Project Roles](https://docs.couchbase.com/cloud/projects/project-roles.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.       |
| ---------------------- | --------------------------------------------------------------------------------------------------- |
| userIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the control plane user. |

##### Request Body schema: application/json

 Array 

| oprequired   | string Enum: "add" "remove" Type of operation.                                                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pathrequired | string Path of resource that needs to be updated. Organization Roles: /organizationRoles Resources: /resources/{resourceId} Resource Roles: /resources/{resourceId}/roles |
| value        | Array of OrganizationRoles (strings) or Array of ProjectRoles (strings) or Resource (object)                                                                              |

### Responses

**200** 

Successfully updated the user metadata.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

patch/v4/organizations/{organizationId}/users/{userId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/users/{userId}

### Request samples 

* Payload

Content type

application/json

Example

addOrganizationRoleremoveOrganizationRoleaddResourceremoveResourceRoleaddResourceRoleremoveResourceperformMultipleOperationsaddOrganizationRole

Copy

 Expand all  Collapse all 

`[
* {
  * "op": "add",
  * "path": "/organizationRoles",
  * "value": [
    * "projectCreator"  
  ]  
}
]`

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Example

addOrganizationRoleremoveOrganizationRoleaddResourceremoveResourceRoleaddResourceRoleremoveResourceperformMultipleOperationaddOrganizationRole

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "name": "Jane",
* "email": "jane.doe@example.com",
* "status": "verified",
* "inactive": false,
* "organizationId": "ffffffff-aaaa-1414-eeee-000000000000",
* "organizationRoles": [
  * "organizationMember",
  * "projectCreator"  
],
* "lastLogin": "2023-07-17T07:05:39.116Z",
* "region": "North America",
* "timeZone": "(UTC +5:30) India Standard Time",
* "enableNotifications": false,
* "expiresAt": "2023-07-17T07:05:39.116Z",
* "resources": [
  * {
    * "id": "b7c745ac-9fb8-4b63-a0e4-51230097a169",
    * "type": "project",
    * "roles": [
      * "projectViewer"  
      ]  
  },
  * {
    * "id": "28b67422-63d5-46b1-9234-8ad4a1d2f7be",
    * "type": "project",
    * "roles": [
      * "projectDataReaderWriter"  
      ]  
  }  
],
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56.000Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56.000Z",
  * "version": 2  
}
}`

## [](#tag/Users/operation/deleteUser)Delete User 

Removes user from the organization.

In order to access this endpoint, the provided API key must have the following role:

* Organization Owner

To learn more about the roles, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.       |
| ---------------------- | --------------------------------------------------------------------------------------------------- |
| userIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the control plane user. |

### Responses

**204** 

Successfully removed the user from the organization.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/users/{userId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/users/{userId}

### Response samples 

* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/AI-Data-Plane-Providers)AI Data Plane Providers

Providers represents the integrations with external services that are required by the AI Data Plane. These endpoints facilitate interactions with external services providers required by the AI Data Plane.

## [](#tag/AI-Data-Plane-Providers/operation/listProviders)List providers 

Lists all the Provider integrations configured a given organization. Use the `providerType` to filter on the type of Provider.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### query Parameters

| page         | integer Sets the page you would like to view.                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage      | integer Sets the number of results you would like to have on each page.                                                                      |
| providerType | string Enum: "awsS3" "openAI" "awsBedrock" Example: providerType=openAIType of provider to filter on. By default all providers are returned. |

### Responses

**200** 

Successfully listed all the providers under the organization.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/aiServices/providers

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/aiServices/providers

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "provider1-ffffffff-aaaa-1414-eeee-000000000000",
    * "name": "my-aws-s3-provider",
    * "type": "awsS3",
    * "configuration": {
      * "awsRegion": "string",
      * "bucket": "string",
      * "folderPath": "string"  
      },
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56Z",
      * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "modifiedAt": "2021-09-01T12:34:56Z",
      * "version": 1  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/AI-Data-Plane-Providers/operation/createProvider)Create provider 

Creates a new integration for a given organization.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| typerequired          | string Enum: "awsS3" "openAI" "awsBedrock" The type of provider to create.                                                                                                     |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| namerequired          | string <= 50 characters The name for the provider integration to create.                                                                                                       |
| configurationrequired | CreateS3ConfigurationRequest (object) or CreateOpenAIConfigurationRequest (object) or CreateBedrockConfigurationRequest (object) The configuration for the provider to create. |

### Responses

**201** 

Successfully created a provider.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/aiServices/providers

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/aiServices/providers

### Request samples 

* Payload

Content type

application/json

Example

CreateOpenAIProviderExampleCreateS3ProviderExampleCreateS3ProviderWithSessionTokenExampleCreateBedrockProviderExampleCreateBedrockProviderWithAPIKeyExampleCreateOpenAIProviderExample

Copy

 Expand all  Collapse all 

`{
* "type": "openAI",
* "name": "provider1",
* "configuration": {
  * "apiKey": "your-openai-key"  
}
}`

### Response samples 

* 201
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "provider1-ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/AI-Data-Plane-Providers/operation/getProvider)Get provider 

Fetches the details of a specific provider.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.        |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| providerIdrequired     | string Example: provider1-ffffffff-aaaa-1414-eeee-000000000000The unique identifier of the provider. |

### Responses

**200** 

Successfully fetched the details of the provider.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/aiServices/providers/{providerId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/aiServices/providers/{providerId}

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Example

GetOpenAIProviderExampleGetS3ProviderExampleGetS3ProviderWithSessionTokenExampleGetBedrockProviderExampleGetOpenAIProviderExample

Copy

 Expand all  Collapse all 

`{
* "name": "provider1",
* "type": "openAI",
* "configuration": null,
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
}
}`

## [](#tag/AI-Data-Plane-Providers/operation/updateProvider)Update provider 

Updates an existing provider.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.        |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| providerIdrequired     | string Example: provider1-ffffffff-aaaa-1414-eeee-000000000000The unique identifier of the provider. |

##### header Parameters

| If-Match | string Example: 12A precondition header that specifies the entity tag of a resource. |
| -------- | ------------------------------------------------------------------------------------ |

##### Request Body schema: application/json

| configurationrequired | UpdateS3ConfigurationRequest (object) or UpdateOpenAIConfigurationRequest (object) or UpdateBedrockConfigurationRequest (object) The configuration for the provider to update. |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### Responses

**204** 

Successfully submitted request to update provider.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/aiServices/providers/{providerId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/aiServices/providers/{providerId}

### Request samples 

* Payload

Content type

application/json

Example

UpdateOpenAIProviderExampleUpdateS3ProviderExampleUpdateS3ProviderWithSessionTokenExampleUpdateBedrockProviderExampleUpdateBedrockProviderWithAPIKeyExampleUpdateBedrockProviderAPIKeyOnlyExampleUpdateOpenAIProviderExample

Copy

 Expand all  Collapse all 

`{
* "configuration": {
  * "apiKey": "new-openai-api-key"  
}
}`

### Response samples 

* 400
* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/AI-Data-Plane-Providers/operation/deleteProvider)Delete provider 

Deletes an existing provider.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.        |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| providerIdrequired     | string Example: provider1-ffffffff-aaaa-1414-eeee-000000000000The unique identifier of the provider. |

### Responses

**204** 

Successfully deleted the provider by its providerId.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/aiServices/providers/{providerId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/aiServices/providers/{providerId}

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/AI-Workflows)AI Workflows

Workflows can vectorize data stored either in Capella operational clusters or in external files. These workflows generate embeddings on the data using a specified AI model.

**Workflow types:**

* `structuredDataProcessing`: For importing and vectorizing structured data in JSON format.
* `unstructuredDataProcessing`: For processing and vectorizing unstructured data in formats such as PDF, JPG, PNG, DOC, and DOCX.
* `vectorization`: For vectorizing JSON data stored in Capella operational clusters.

## [](#tag/AI-Workflows/operation/listAiWorkflows)List AI Workflows 

Lists all the workflows for a specific cluster.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Data Reader
* Data Reader/Writer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### query Parameters

| page    | integer Sets the page you would like to view.                           |
| ------- | ----------------------------------------------------------------------- |
| perPage | integer Sets the number of results you would like to have on each page. |

### Responses

**200** 

Successfully listed all the workflows for the cluster.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/aiServices/workflows

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/aiServices/workflows

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "name": "my-workflow-name",
    * "type": "structuredDataProcessing",
    * "configuration": {
      * "source": {
        * "name": "provider1",
        * "providerId": "provider1-ffffffff-aaaa-1414-eeee-000000000000"  
            },
      * "targetCouchbaseKeyspace": {
        * "bucket": "my-bucket",
        * "scope": "my-scope",
        * "collection": "my-collection"  
            },
      * "structuredDataProcessingConfig": {
        * "keyFieldName": "document_id",
        * "jsonType": "jsonlines"  
            },
      * "vectorizationConfig": {
        * "createIndexes": true,
        * "embeddingFieldMappings": {
          * "property1": {
            * "sourceFields": [
              * "field1"  
                                          ]  
                              },
          * "property2": {
            * "sourceFields": [
              * "field1"  
                                          ]  
                              }  
                    },
        * "embeddingModel": {
          * "external": {
            * "openAiIntegration": {
              * "name": "provider1",
              * "providerId": "provider1-ffffffff-aaaa-1414-eeee-000000000000"  
                                          },
            * "modelName": "text-embedding-3-small"  
                              }  
                    }  
            }  
      },
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56Z",
      * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "modifiedAt": "2021-09-01T12:34:56Z",
      * "version": 1  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/AI-Workflows/operation/createAiWorkflow)Create AI Workflow 

Creates a new workflow based on the specified workflow type.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### Request Body schema: application/json

| namerequired          | string The name of the workflow.                                                                                                      |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| typerequired          | string Enum: "structuredDataProcessing" "unstructuredDataProcessing" "vectorization" The type of workflow.                            |
| configurationrequired | CreateStructuredWorkflowRequest (object) or CreateUnstructuredWorkflowRequest (object) or CreateVectorizationWorkflowRequest (object) |

### Responses

**201** 

Successfully created a workflow.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/aiServices/workflows

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/aiServices/workflows

### Request samples 

* Payload

Content type

application/json

Example

Structured Data WorkflowUnstructured Data WorkflowVectorization WorkflowStructured Data Workflow with BedrockUnstructured Data Workflow with BedrockVectorization Workflow with BedrockStructured Data Workflow

Copy

 Expand all  Collapse all 

`{
* "name": "my-structured-workflow",
* "type": "structuredDataProcessing",
* "configuration": {
  * "source": {
    * "providerId": "provider2-ffffffff-aaaa-1414-eeee"  
  },
  * "targetCouchbaseKeyspace": {
    * "bucket": "my-bucket",
    * "scope": "my-scope",
    * "collection": "my-collection"  
  },
  * "structuredDataProcessingConfig": {
    * "jsonType": "jsonlist"  
  },
  * "vectorizationConfig": {
    * "createIndexes": true,
    * "embeddingFieldMappings": {
      * "vectorEmbeddingField1": {
        * "sourceFields": [
          * "field1",
          * "field2"  
                    ]  
            },
      * "vectorEmbeddingField2": {
        * "sourceFields": [
          * "field3",
          * "field4"  
                    ]  
            }  
      },
    * "embeddingModel": {
      * "capellaHosted": {
        * "id": "550e8400-e29b-41d4-a716-446655440000"  
            }  
      }  
  }  
}
}`

### Response samples 

* 201
* 400
* 403
* 404
* 500

Content type

application/json

Copy

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/AI-Workflows/operation/getAiWorkflow)Get AI Workflow 

Retrieves the details of a specific workflow.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Data Reader
* Data Reader/Writer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.         |
| ---------------------- | ----------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.              |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.              |
| workflowIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The unique identifier of the AI workflow. |

### Responses

**200** 

Successfully retrieved the details of the workflow.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/aiServices/workflows/{workflowId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/aiServices/workflows/{workflowId}

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Example

Vectorization WorkflowStructured Data WorkflowUnstructured Data WorkflowVectorization Workflow

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "name": "my-vectorization-workflow",
* "type": "vectorization",
* "configuration": {
  * "targetCouchbaseKeyspace": {
    * "bucket": "my-bucket",
    * "scope": "my-scope",
    * "collection": "my-collection"  
  },
  * "vectorizationConfig": {
    * "createIndexes": true,
    * "embeddingFieldMappings": {
      * "vectorEmbeddingField1": {
        * "sourceFields": [
          * "field1",
          * "field2"  
                    ]  
            }  
      },
    * "embeddingModel": {
      * "external": {
        * "openAiIntegration": {
          * "name": "my-openai-integration",
          * "providerId": "provider1-ffffffff-aaaa-1414-eeee-000000000000"  
                    },
        * "modelName": "text-embedding-3-small"  
            }  
      }  
  }  
},
* "audit": {
  * "createdAt": "2021-01-01T00:00:00Z",
  * "createdByUserID": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-01-01T00:00:00Z",
  * "modifiedByUserID": "ffffffff-aaaa-1414-eeee-000000000000",
  * "version": 1  
}
}`

## [](#tag/AI-Workflows/operation/deleteAiWorkflow)Delete AI Workflow 

Deletes an existing workflow.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.         |
| ---------------------- | ----------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.              |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.              |
| workflowIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The unique identifier of the AI workflow. |

### Responses

**202** 

Workflow deletion is in progress.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/aiServices/workflows/{workflowId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/aiServices/workflows/{workflowId}

### Response samples 

* 400
* 403
* 404
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/AI-Workflows/operation/listAiWorkflowRuns)List AI Workflow Runs 

Lists all the workflow runs for a specific workflow.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Data Reader
* Data Reader/Writer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.         |
| ---------------------- | ----------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.              |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.              |
| workflowIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The unique identifier of the AI workflow. |

##### query Parameters

| page    | integer Sets the page you would like to view.                           |
| ------- | ----------------------------------------------------------------------- |
| perPage | integer Sets the number of results you would like to have on each page. |

### Responses

**200** 

Successfully listed all the workflow runs for the specified workflow.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/aiServices/workflows/{workflowId}/runs

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/aiServices/workflows/{workflowId}/runs

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "string",
    * "status": "deploying",
    * "totalFiles": 0,
    * "processedFiles": 0,
    * "erroredFiles": 0,
    * "createdAt": "2021-01-01T00:00:00Z",
    * "createdByUserID": "string"  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/AI-Workflows/operation/createAiWorkflowRun)Run an AI Workflow 

Starts a specific workflow. On the first run, the workflow processes all files specified in the workflow configuration. On subsequent runs, it processes only new, updated, or previously failed files.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Data Reader/Writer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.         |
| ---------------------- | ----------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.              |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.              |
| workflowIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The unique identifier of the AI workflow. |

### Responses

**202** 

Successfully started a workflow run.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/aiServices/workflows/{workflowId}/runs

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/aiServices/workflows/{workflowId}/runs

### Response samples 

* 202
* 400
* 403
* 404
* 409
* 500

Content type

application/json

Copy

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/AI-Workflows/operation/stopAiWorkflowRun)Stop AI Workflow Run 

Stops a workflow run that is in progress.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Data Reader/Writer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.         |
| ---------------------- | ----------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.              |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.              |
| workflowIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The unique identifier of the AI workflow. |

### Responses

**202** 

Stopping the workflow. This may take a moment.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/aiServices/workflows/{workflowId}/runs

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/aiServices/workflows/{workflowId}/runs

### Response samples 

* 400
* 403
* 404
* 409
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/AI-Workflows/operation/getAiWorkflowRun)Get AI Workflow Run 

Retrieves the details of a specific workflow run.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Data Reader
* Data Reader/Writer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.             |
| ---------------------- | --------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                  |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                  |
| workflowIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The unique identifier of the AI workflow.     |
| runIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The unique identifier of the AI workflow run. |

### Responses

**200** 

Successfully retrieved the details of the workflow run.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/aiServices/workflows/{workflowId}/runs/{runId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/aiServices/workflows/{workflowId}/runs/{runId}

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "id": "123e4567-e89b-12d3-a456-426614174000",
* "totalFiles": 100,
* "processedFiles": 37,
* "erroredFiles": 2,
* "elapsedTime": 1234567890,
* "status": "running",
* "createdAt": "2021-01-01T00:00:00Z",
* "createdByUserID": "123e4567-e89b-12d3-a456-426614174000"
}`

## [](#tag/AI-Workflows/operation/getAiWorkflowRunProcessedFiles)Get AI Workflow Run Processed Files 

Retrieves the processed files for a specific workflow run.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Data Reader
* Data Reader/Writer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.             |
| ---------------------- | --------------------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                  |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.                  |
| workflowIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The unique identifier of the AI workflow.     |
| runIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The unique identifier of the AI workflow run. |

##### query Parameters

| page       | integer Sets the page you would like to view.                                                                                                        |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage    | integer Sets the number of results you would like to have on each page.                                                                              |
| fileStatus | string Enum: "success" "failed" "skipped" Example: fileStatus=successThe type of file status used for filtering. By default, all files are returned. |

### Responses

**200** 

Successfully retrieved the processed files for the workflow run.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/aiServices/workflows/{workflowId}/runs/{runId}/processedFiles

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/aiServices/workflows/{workflowId}/runs/{runId}/processedFiles

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "cursor": {
  * "pages": {
    * "page": 1,
    * "last": 1,
    * "perPage": 25,
    * "totalItems": 3  
  },
  * "hrefs": { }  
},
* "data": [
  * {
    * "fileName": "file1.pdf",
    * "filePath": "documents/reports",
    * "fileStatus": "success"  
  },
  * {
    * "fileName": "file2.json",
    * "filePath": "data",
    * "fileStatus": "failed",
    * "error": {
      * "code": "INVALID_FORMAT",
      * "message": "Invalid JSON format: unexpected token at position 145"  
      }  
  },
  * {
    * "fileName": "file3.docx",
    * "filePath": "uploads",
    * "fileStatus": "failed",
    * "error": {
      * "code": "SIZE_LIMIT_EXCEEDED",
      * "message": "File size exceeds the maximum allowed limit of 50MB"  
      }  
  }  
]
}`

## [](#tag/AI-Workflows/operation/getSupportedExternalEmbeddingModels)Get Supported External Embedding Models 

Retrieves a list of supported external embedding models that can be used for vectorization. This endpoint allows you to see which models are available for use in your projects. In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Cluster Owner To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |
| clusterIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the cluster.      |

##### query Parameters

| page     | integer Sets the page you would like to view.                                                                                                   |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage  | integer Sets the number of results you would like to have on each page.                                                                         |
| provider | string Enum: "openAI" "awsBedrock" Example: provider=openAIType of external model provider to filter on. By default all providers are returned. |

### Responses

**200** 

Successfully retrieved the list of supported external embedding models.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/aiServices/workflows/supportedExternalEmbeddingModels

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/aiServices/workflows/supportedExternalEmbeddingModels

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Example

Supported External Embedding Models Response ExampleSupported External Embedding Models Response with AWS Bedrock ExampleSupported External Embedding Models Response Example

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "name": "text-embedding-3-small",
    * "provider": "openAI",
    * "dimensions": {
      * "supported": [
        * 512,
        * 1536  
            ],
      * "default": 1536  
      },
    * "contextWindowSize": 8192  
  },
  * {
    * "name": "text-embedding-3-large",
    * "provider": "openAI",
    * "dimensions": {
      * "supported": [
        * 256,
        * 1024,
        * 3072  
            ],
      * "default": 3072  
      },
    * "contextWindowSize": 8192  
  },
  * {
    * "name": "text-embedding-ada-002",
    * "provider": "openAI",
    * "dimensions": {
      * "supported": [
        * 1536  
            ],
      * "default": 1536  
      },
    * "contextWindowSize": 8192  
  },
  * {
    * "name": "amazon.titan-embed-text-v1",
    * "provider": "awsBedrock",
    * "dimensions": {
      * "supported": [
        * 1536  
            ],
      * "default": 1536  
      },
    * "contextWindowSize": 8192  
  },
  * {
    * "name": "amazon.titan-embed-text-v2:0",
    * "provider": "awsBedrock",
    * "dimensions": {
      * "supported": [
        * 256,
        * 512,
        * 1024  
            ],
      * "default": 1024  
      },
    * "contextWindowSize": 8192  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 1,
    * "last": 1,
    * "perPage": 25,
    * "totalItems": 5  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/organizations/ffffffff-aaaa-1414-eeee-000000000000/projects/ffffffff-bbbb-2525-dddd-111111111111/clusters/ffffffff-cccc-3636-cccc-222222222222/aiServices/workflows/supportedExternalEmbeddingModels?page=1&perPage=25>",
    * "last": "<https://cloud.couchbase.com/v4/organizations/ffffffff-aaaa-1414-eeee-000000000000/projects/ffffffff-bbbb-2525-dddd-111111111111/clusters/ffffffff-cccc-3636-cccc-222222222222/aiServices/workflows/supportedExternalEmbeddingModels?page=1&perPage=25>",
    * "previous": "",
    * "next": ""  
  }  
}
}`

## [](#tag/Model-Services-API-Keys-%28AI-Data-Plane%29)Model Services API Keys (AI Data Plane)

Couchbase AI Data Plane Model Services uses Bearer token authentication for secure access to the AI models. Each inference request to access the models must include a valid API key in the Authorization header. The Model API Keys endpoints enable users to manage (create, retrieve, update, and delete) API keys for the models of a specific region, ensuring secure and controlled access to the models during inferencing. The API keys created for a specific region can be used to access all the models available in that region.

To send inference requests to your models and receive outputs, use the [Model Service API](https://docs.couchbase.com/ai/model-service-api-reference/rest-api.html). For more information, see [Make an API Call with the Model Service API](https://docs.couchbase.com/ai/api-guide/api-use.html#model-api-call).

## [](#tag/Model-Services-API-Keys-%28AI-Data-Plane%29/operation/createModelAPIKey)Create API Key 

Creates a new API Key for the specified region within an organization. API Key created for a region can be used to access all the models of that region for inferencing.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

required

| namerequired         | string <= 128 characters Name of the Language Model API Key.                                                                                                                                                                                                               |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| description          | string <= 250 characters Description of the Language Model API Key.                                                                                                                                                                                                        |
| expiryrequired       | number <float\> Expiry of the API key in number of days. Maximum value is 365 days.                                                                                                                                                                                        |
| allowedCIDRsrequired | Array of strings List of IP addresses or CIDR blocks that are allowed to use this API key.                                                                                                                                                                                 |
| allowedModels        | Array of strings Default: \["\*"\] List of allowed model IDs for this API key. If empty or omitted, defaults to "\*" (all models in the region). Can be set to \["\*"\] explicitly for all models. Can contain specific model IDs to restrict access to those models only. |
| regionrequired       | string The region where the API key will be created. The apikey created in a region can access all the models available in that region.                                                                                                                                    |

### Responses

**201** 

Successfully created API Key.

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

AI Gateway doesn't exist for the tenant in the specified region.

**422** 

Request validation error.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/aiServices/models/apiKeys

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/aiServices/models/apiKeys

### Request samples 

* Payload

Content type

application/json

Example request for creating a new Language Model API Key with access to all models (allowedModels empty defaults to wildcard)

Copy

 Expand all  Collapse all 

`{
* "name": "MyLanguageModelAPIKey-AllModels",
* "description": "API key for accessing all models in the region",
* "expiry": 180,
* "allowedCIDRs": [
  * "192.168.1.0/24",
  * "10.0.0.0/8"  
],
* "allowedModels": [ ],
* "region": "us-east-1"
}`

### Response samples 

* 201
* 400
* 401
* 403
* 404
* 422
* 500

Content type

application/json

Copy

`{
* "id": "60a95d98-8660-488c-a1e0-25b90e926a1e",
* "token": "cb_api_sk_1234567890abcdef"
}`

## [](#tag/Model-Services-API-Keys-%28AI-Data-Plane%29/operation/listModelAPIKeys)List API keys 

Lists all API keys for the given region in an organization.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                                                  |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                                        |
| sortBy        | Array of strings Example: sortBy=name Sets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **name**, **createdAt**, **expiry**.              |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                                               |
| filterBy      | string Example: filterBy=region:eq:us-east-1Filter criteria in the format 'field:operator:value'. Supported operators are 'eq' (equals). Currently, only 'region' is supported as a filter field. Example: region:eq:us-east-1 |

### Responses

**200** 

Successfully listed all the API keys.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**422** 

Request validation error.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/aiServices/models/apiKeys

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/aiServices/models/apiKeys

### Response samples 

* 200
* 401
* 403
* 422
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "keyId": "60a95d98-8660-488c-a1e0-25b90e926a1e",
    * "name": "MyLanguageModelAPIKey",
    * "description": "API key for accessing GPT-4 models",
    * "expiry": 180,
    * "allowedCIDRs": [
      * "192.168.1.0/24",
      * "10.0.0.0/8"  
      ],
    * "allowedModels": [
      * {
        * "id": "5ca127fe-49da-4a6a-aef9-08393b97643f",
        * "name": "GPT-4"  
            },
      * {
        * "id": "6db238gf-50eb-5b7b-bfg0-09404c08754g",
        * "name": "Claude 3"  
            }  
      ],
    * "region": "us-east-1",
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56Z",
      * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "modifiedAt": "2021-09-01T12:34:56Z",
      * "version": 1  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/Model-Services-API-Keys-%28AI-Data-Plane%29/operation/getModelAPIKey)Get API Key 

Returns an API Key for the given region in the organization by its ID.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.                |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| apiKeyIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000Unique identifier for the Language Model API key |

### Responses

**200** 

Successfully retrieved the API Key.

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/aiServices/models/apiKeys/{apiKeyId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/aiServices/models/apiKeys/{apiKeyId}

### Response samples 

* 200
* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "keyId": "60a95d98-8660-488c-a1e0-25b90e926a1e",
* "name": "MyLanguageModelAPIKey",
* "description": "API key for accessing GPT-4 models",
* "expiry": 180,
* "allowedCIDRs": [
  * "192.168.1.0/24",
  * "10.0.0.0/8"  
],
* "allowedModels": [
  * {
    * "id": "5ca127fe-49da-4a6a-aef9-08393b97643f",
    * "name": "GPT-4"  
  },
  * {
    * "id": "6db238gf-50eb-5b7b-bfg0-09404c08754g",
    * "name": "Claude 3"  
  }  
],
* "region": "us-east-1",
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
}
}`

## [](#tag/Model-Services-API-Keys-%28AI-Data-Plane%29/operation/deleteModelAPIKey)Delete API key 

Deletes an existing API Key for the given region in the organization.

In order to access this endpoint, the provided API key must have at least one of the following roles: - Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.                |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| apiKeyIdrequired       | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000Unique identifier for the Language Model API key |

### Responses

**204** 

API key deleted successfully.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/aiServices/models/apiKeys/{apiKeyId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/aiServices/models/apiKeys/{apiKeyId}

### Response samples 

* 401
* 403
* 404
* 409
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 401,
* "code": 1001,
* "message": "The request is unauthorized. Please ensure you have proper authentication credentials and try again.",
* "hint": "The request is unauthorized. Please ensure you have proper authentication credentials and try again."
}`

## [](#tag/Models-%28AI-Data-Plane%29)Models (AI Data Plane)

The Model Service endpoints allows you to deploy and manage your models - open LLMs like Llama3 and embedding models in Capella close to your data. The users can create, get, update, and delete language models.

To send inference requests to your models and receive outputs, use the [Model Service API](https://docs.couchbase.com/ai/model-service-api-reference/rest-api.html). For more information about the Model Service API, see [Manage Deployments with AI Data Plane APIs](https://docs.couchbase.com/ai/api-guide/api-intro.html#model-service-api).

## [](#tag/Models-%28AI-Data-Plane%29/operation/listModels)List Models 

Fetches the details of all the models.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Member

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### query Parameters

| page        | integer Sets the page you would like to view.                                                                                                                                                      |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage     | integer Sets the number of results you would like to have on each page.                                                                                                                            |
| modelStatus | string Enum: "pending" "deploying" "deployFailed" "healthy" "unhealthy" "pausing" "paused" "resuming" "pauseFailed" "resumeFailed" Filter by model status. All models are returned when set empty. |
| modelKind   | string Enum: "embedding-generation" "text-generation" Filter by model kind. All models are returned when this is set empty.                                                                        |

### Responses

**200** 

Successfully fetched the models.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/aiServices/models

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/aiServices/models

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "model": {
      * "id": "fffffffff-aaaa-1414-eeee-000000000000",
      * "name": "my-new-model",
      * "config": {
        * "catalogModelName": "meta-llama/Llama-3.1-8B-Instruct",
        * "type": "text-generation",
        * "provider": "meta",
        * "quantization": "fullPrecision",
        * "optimization": "latency",
        * "dimensions": 4096,
        * "caching": {
          * "enableStandard": true,
          * "enableConversational": false,
          * "semantic": {
            * "embeddingModel": "my-embedding-model-id",
            * "scoreThreshold": 0.75,
            * "dimensions": 4096,
            * "distanceMetric": "dot_product"  
                              },
          * "defaultCache": "semantic",
          * "expiryTTL": 1000  
                    },
        * "enableBatching": true,
        * "keywordFiltering": [
          * "harassment",
          * "murder"  
                    ]  
            },
      * "cloudConfig": {
        * "provider": "aws",
        * "region": "us-east-1",
        * "compute": {
          * "cpu": 4,
          * "gpuMemory": 48  
                    }  
            },
      * "status": "deploying",
      * "usageMetrics": {
        * "tokens": {
          * "value": 345,
          * "trend": "increasing"  
                    },
        * "requests": {
          * "value": 4094,
          * "trend": "increasing"  
                    }  
            },
      * "connectionString": "<http://endpoint.com>",
      * "audit": {
        * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
        * "createdAt": "2021-09-01T12:34:56Z",
        * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
        * "modifiedAt": "2021-09-01T12:34:56Z",
        * "version": 1  
            },
      * "actions": [
        * "delete"  
            ]  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/Models-%28AI-Data-Plane%29/operation/createModel)Create Model 

Create a new model deployment.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

required

| namerequired             | string Name of the model.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| catalogModelNamerequired | string Name of the model deployed from the model catalog.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| cloudConfigrequired      | object (CloudConfig) The cloud configuration for the model.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| quantization             | string Enum: "fp8" "fp16" "fullPrecision" Quantization options for the model. Options include 8-bit, 16bit, and full-precision.                                                                                                                                                                                                                                                                                                                                              |
| optimization             | string Enum: "throughput" "latency" Optimization profile option for the model.                                                                                                                                                                                                                                                                                                                                                                                               |
| dimensions               | integer Dimensions specify the vector dimensions for the underlying embedding model.                                                                                                                                                                                                                                                                                                                                                                                         |
| guardrails               | Array of strings List of guardrail categories as plain text strings. These will be formatted into a template and base64-encoded internally.                                                                                                                                                                                                                                                                                                                                  |
| jailbreak                | object Jailbreak model information.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| caching                  | object (Caching) Caching configuration for the model. Caching improves system efficiency by caching frequently accessed data, both at the conversational level (storing request-specific conversation history) and at the semantic level (saving the embeddings for queries and results), ensuring optimal performance while managing memory costs effectively. Supports multiple caching strategies for improved response times and reduced strain on backend LLM services. |
| enableBatching           | boolean Option to enable batching.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| keywordFiltering         | Array of strings Keywords in a comma-separated string to filter the input.                                                                                                                                                                                                                                                                                                                                                                                                   |

### Responses

**202** 

Model queued for deployment successfully.

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/aiServices/models

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/aiServices/models

### Request samples 

* Payload

Content type

application/json

Example

Deployment Payload for Embedding Model with g6.xlargeDeployment Payload for Text Generation Model - with security features and g6.xlargeDeployment Payload for Text Generation Model - without security features and g6.xlargeDeployment Payload for Text Generation Model - without value adds and g6.xlargeDeployment Payload for Text Generation Model - with value adds - all cache and g6.xlargeDeployment Payload for Text Generation Model - with value adds - only standard cache and g6.xlargeDeployment Payload for Text Generation Model - with value adds - only semantic cache and g6.xlargeDeployment Payload for Text Generation Model - with value adds - no conversational cache and g6.xlargeDeployment Payload for Text Generation Model - with value adds - without batching and g6.xlargeDeployment Payload for Text Generation Model - with value adds - without keyword filtering and g6.xlargeDeployment Payload for Embedding Model with g6.xlarge

Copy

 Expand all  Collapse all 

`{
* "name": "my-embedding-model",
* "catalogModelName": "Snowflake/snowflake-arctic-embed-m-v2.0",
* "cloudConfig": {
  * "provider": "aws",
  * "region": "us-east-1",
  * "compute": {
    * "cpu": 4,
    * "ram": 16  
  }  
},
* "quantization": "fullPrecision",
* "optimization": "throughput"
}`

### Response samples 

* 202
* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "fffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/Models-%28AI-Data-Plane%29/operation/getModel)Get Model 

Fetches the details of the given model.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Member

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| modelIdrequired        | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the model.        |

### Responses

**200** 

Successfully fetched the model based on the ModelId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/aiServices/models/{modelId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/aiServices/models/{modelId}

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "model": {
  * "id": "fffffffff-aaaa-1414-eeee-000000000000",
  * "name": "my-new-model",
  * "config": {
    * "catalogModelName": "meta-llama/Llama-3.1-8B-Instruct",
    * "type": "text-generation",
    * "provider": "meta",
    * "quantization": "fullPrecision",
    * "optimization": "latency",
    * "dimensions": 4096,
    * "caching": {
      * "enableStandard": true,
      * "enableConversational": false,
      * "semantic": {
        * "embeddingModel": "my-embedding-model-id",
        * "scoreThreshold": 0.75,
        * "dimensions": 4096,
        * "distanceMetric": "dot_product"  
            },
      * "defaultCache": "semantic",
      * "expiryTTL": 1000  
      },
    * "enableBatching": true,
    * "keywordFiltering": [
      * "harassment",
      * "murder"  
      ]  
  },
  * "cloudConfig": {
    * "provider": "aws",
    * "region": "us-east-1",
    * "compute": {
      * "cpu": 4,
      * "gpuMemory": 48  
      }  
  },
  * "status": "deploying",
  * "usageMetrics": {
    * "tokens": {
      * "value": 345,
      * "trend": "increasing"  
      },
    * "requests": {
      * "value": 4094,
      * "trend": "increasing"  
      }  
  },
  * "connectionString": "<http://endpoint.com>",
  * "audit": {
    * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
    * "createdAt": "2021-09-01T12:34:56Z",
    * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
    * "modifiedAt": "2021-09-01T12:34:56Z",
    * "version": 1  
  },
  * "actions": [
    * "delete"  
  ]  
}
}`

## [](#tag/Models-%28AI-Data-Plane%29/operation/destroyModel)Delete Model 

Destroys an existing model.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| modelIdrequired        | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the model.        |

### Responses

**202** 

Successfully queued the model for deletion.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/aiServices/models/{modelId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/aiServices/models/{modelId}

### Response samples 

* 403
* 404
* 409
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Models-%28AI-Data-Plane%29/operation/putModel)Update Model 

Updates an existing model.

Model updates may take up to a few minutes to take effect.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| modelIdrequired        | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the model.        |

##### header Parameters

| If-Match | string Example: 12A precondition header that specifies the entity tag of a resource. |
| -------- | ------------------------------------------------------------------------------------ |

##### Request Body schema: application/json

| name             | string Name of the model.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| caching          | object (Caching) Caching configuration for the model. Caching improves system efficiency by caching frequently accessed data, both at the conversational level (storing request-specific conversation history) and at the semantic level (saving the embeddings for queries and results), ensuring optimal performance while managing memory costs effectively. Supports multiple caching strategies for improved response times and reduced strain on backend LLM services. |
| enableBatching   | boolean Option to enable batching.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| keywordFiltering | Array of strings Keywords in a comma-separated string to filter the input.                                                                                                                                                                                                                                                                                                                                                                                                   |
| guardrails       | Array of strings List of guardrail categories as plain text strings. These will be formatted into a template and base64-encoded internally.                                                                                                                                                                                                                                                                                                                                  |
| jailbreak        | object Jailbreak model information.                                                                                                                                                                                                                                                                                                                                                                                                                                          |

### Responses

**204** 

Successfully submitted request to update model.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/aiServices/models/{modelId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/aiServices/models/{modelId}

### Request samples 

* Payload

Content type

application/json

Example

Update Model Request PayloadUpdate Model Request Payload - caching configurationUpdate Model Request Payload - Update security featuresUpdate Model Request Payload

Copy

 Expand all  Collapse all 

`{
* "name": "my-updated-text-generation-model",
* "caching": {
  * "enableStandard": true,
  * "enableConversational": true,
  * "semantic": {
    * "embeddingModel": "my-embedding-model-id",
    * "scoreThreshold": 0.8,
    * "dimensions": 4096,
    * "distanceMetric": "dot_product"  
  },
  * "defaultCache": "semantic",
  * "expiryTTL": 3600  
},
* "enableBatching": true,
* "keywordFiltering": [
  * "violence",
  * "harassment",
  * "inappropriate"  
],
* "guardrails": [
  * "hate speech",
  * "sexual content",
  * "violence"  
],
* "jailbreak": {
  * "scoreThreshold": 0.85  
}
}`

### Response samples 

* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Models-%28AI-Data-Plane%29/operation/getConnectionString)Get Model Connection String 

Fetches the connection string to connect to the model.

Use this connection string as the base URL in your [Model Service API](https://docs.couchbase.com/ai/model-service-api-reference/rest-api.html) inference requests. For more information, see [Make an API Call with the Model Service API](https://docs.couchbase.com/ai/api-guide/api-use.html#model-api-call).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Member

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| modelIdrequired        | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the model.        |

### Responses

**200** 

Successfully fetched the connectionString.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/aiServices/models/{modelId}/connectionString

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/aiServices/models/{modelId}/connectionString

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "connectionString": "<https://abcdefgh.ai.com>"
}`

## [](#tag/Models-%28AI-Data-Plane%29/operation/modelOn)Turn On Model 

Resumes the model or turns the model to On state.

The connection URL remains unchanged when the model is turned on or off.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| modelIdrequired        | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the model.        |

### Responses

**202** 

Successfully switched the model to on state.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/aiServices/models/{modelId}/activationState

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/aiServices/models/{modelId}/activationState

### Response samples 

* 403
* 404
* 409
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Models-%28AI-Data-Plane%29/operation/modelOff)Turn Off Model 

Pauses the model or turns the model to off state.

The connection URL remains unchanged when the model is turned on or off.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| modelIdrequired        | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the model.        |

### Responses

**202** 

Successfully switched the model to off state.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/aiServices/models/{modelId}/activationState

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/aiServices/models/{modelId}/activationState

### Response samples 

* 403
* 404
* 409
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`