---
title: Manage Log Streaming with the Management API
description: You can configure and manage log streaming for App Services using
  the Couchbase Capella Management API.
editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/monitoring/manage-log-streaming.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:app-services::monitoring/manage-log-streaming.adoc[]
---

[View original HTML](/app-services/monitoring/manage-log-streaming.html)

# Manage Log Streaming with the Management API

> You can configure and manage log streaming for App Services using the Couchbase Capella Management API. 

* For an overview of the Management API, see [Manage Deployments with the Management API](../../cloud/management-api-guide/management-api-intro.md).
* To get started with the Management API, see [Get Started with the Management API](../../cloud/management-api-guide/management-api-start.md).
* To make an API call, see [Make an API Call with the Management API](../../cloud/management-api-guide/management-api-use.md).
* For a full reference guide, see [Management API Reference](../../cloud/management-api-reference/index.md).

You can also configure log streaming using the Capella UI. See [Enable Log Streaming](configure-log-collector-app-service.md) and [Configure Log Streaming for an App Endpoint](configure-log-streaming-app-endpoint.md).

## [](#examples)About API Call Examples

In the examples on this page:

* `$organizationId` is the organization ID.
* `$projectId` is the project ID.
* `$clusterId` is the cluster ID.
* `$appServiceId` is the App Service ID.
* `$apiKeySecret` is the API key secret, used as the Bearer token.

The endpoints described on this page all have the same base path: `/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}`. For clarity, this is not shown in the instructions, but it’s included in the examples.

## [](#prerequisites)Prerequisites

Before you configure log streaming for an App Service:

* You must have deployed a [Couchbase Capella cluster](../../cloud/clusters/create-database.md) and a linked [App Service](../app-services/creating-an-app-service.md).
* You must have set up your Log Collector and verified that it’s reachable. See [Supported Log Collector Providers](log-streaming.md#supported-providers).
* You must understand the [resource considerations](log-streaming.md#resource-consideration) and cost implications of log streaming.

## [](#app-service-log-streaming)Configure Log Streaming for an App Service

You can enable and configure log streaming at the App Service level. This sets up the log collector connection and applies default log levels and filters.

### [](#enable-log-streaming)Enable and Configure Log Streaming

To enable and configure log streaming for a specified App Service:

1. Use the [POST /appservices/{appServiceId}/logStreaming](../../cloud/management-api-reference/index.md#tag/App-Services-Log-Streaming/operation/postAppServiceLogStreaming) endpoint.
2. Pass the App Service ID as a path parameter.
3. Pass the required log streaming configuration as the request body. For details, see the [request body schema](../../cloud/management-api-reference/index.md#tag/App-Services-Log-Streaming/operation/postAppServiceLogStreaming).

The configuration includes:

* Log collector type and credentials.
* Whether to enable streaming.
* Optional App Endpoints to exclude from streaming.  
You can exclude specific App Endpoints from streaming by listing them in the `disabledAppEndpoints` array. For an example, see [Example 1](#ex-enable-exclude-endpoints).

In all of the following examples, `$appServiceId` is the App Service ID.

#### [](#datadog)Datadog

In this example:

* `$YOUR_DATADOG_API_KEY` is your Datadog API key.

To find your Datadog API key, see the [Datadog Organization Settings documentation](https://docs.datadoghq.com/account%5Fmanagement/org%5Fsettings/).

Request

```bash
curl -X POST "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/logStreaming" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{
  "streamingEnabled": true,
  "outputType": "datadog",
  "credentials": {
    "apiKey": "$YOUR_DATADOG_API_KEY",
    "url": "https://http-intake.logs.datadoghq.com"
  }
}'
```

#### [](#sumo-logic)Sumo Logic

Sumo Logic uses a signed collectURL for secure log transmission. To get your collector URL, create an HTTP Source in Sumo Logic and copy the provided HTTP Source Address. For more information, see the [Sumo Logic HTTP Source documentation](https://help.sumologic.com/docs/send-data/hosted-collectors/http-source/).

Request

```bash
curl -X POST "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/logStreaming" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{
  "streamingEnabled": true,
  "outputType": "sumologic",
  "credentials": {
    "url": "https://collectors.sumologic.com/receiver/v1/http/$YOUR_COLLECTOR_URL"
  }
}'
```

#### [](#elasticsearch)Elasticsearch

> [!NOTE]
> Capella App Services supports only Elasticsearch versions 8+ with basic auth.

In this example:

* `$YOUR_ELASTICSEARCH_INSTANCE` is the URL of your Elasticsearch instance. Make sure to connect through port `9200`.
* `$YOUR_ELASTIC_USER` is the username of the Elastic user account you want to use to connect to your Elasticsearch instance.
* `$YOUR_ELASTIC_PASSWORD` is the password for the account you want to use to connect.

To find your Elasticsearch instance URL, see the [Elasticsearch documentation on finding your Elasticsearch connection details](https://www.elastic.co/docs/solutions/search/search-connection-details) or your Elasticsearch deployment settings.

Request

```bash
curl -X POST "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/logStreaming" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{
  "streamingEnabled": true,
  "outputType": "elasticsearch",
  "credentials": {
    "url": "https://$YOUR_ELASTICSEARCH_INSTANCE.com:9200",
    "username": "$YOUR_ELASTIC_USER",
    "password": "$YOUR_ELASTIC_PASSWORD"
  }
}'
```

#### [](#grafana-loki)Grafana Loki

In this example:

* `$YOUR_LOKI_USER` is the username of the Grafana Loki user account you want to use to connect.
* `$YOUR_LOKI_PASSWORD` is the password for the Grafana Loki account you want to use to connect.

Request

```bash
curl -X POST "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/logStreaming" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{
  "streamingEnabled": true,
  "outputType": "loki",
  "credentials": {
    "url": "https://logs-prod-us-central1.grafana.net/loki/api/v1/push",
    "username": "$YOUR_LOKI_USER",
    "password": "$YOUR_LOKI_PASSWORD"
  }
}'
```

#### [](#splunk)Splunk

In this example:

* `$YOUR_SPLUNK_HEC_TOKEN` is your Splunk HTTP Event Collector (HEC) token.
* `$YOUR_SPLUNK_INSTANCE` is the URL for your Splunk instance.

To find your Splunk HEC token and URL, see the [Splunk documentation on setting up HTTP Event Collector](https://help.splunk.com/en/splunk-cloud-platform/get-started/get-data-in/10.1.2507/get-data-with-http-event-collector/set-up-and-use-http-event-collector-in-splunk-web).

Request

```bash
curl -X POST "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/logStreaming" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{
  "streamingEnabled": true,
  "outputType": "splunk",
  "credentials": {
    "token": "$YOUR_SPLUNK_HEC_TOKEN",
    "url": "https://$YOUR_SPLUNK_INSTANCE.com:8088/services/collector"
  }
}'
```

#### [](#dynatrace)Dynatrace

In this example:

* `$YOUR_DYNATRACE_API_TOKEN` is your Dynatrace API token.
* `$YOUR_ENVIRONMENT_ID` is your Dynatrace environment ID.

To find your Dynatrace API token and environment ID, see the [Dynatrace API authentication documentation](https://docs.dynatrace.com/docs/dynatrace-api/basics/dynatrace-api-authentication) and your Dynatrace environment settings.

Request

```bash
curl -X POST "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/logStreaming" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{
  "streamingEnabled": true,
  "outputType": "dynatrace",
  "credentials": {
    "apiKey": "$YOUR_DYNATRACE_API_TOKEN",
    "url": "https://$YOUR_ENVIRONMENT_ID.live.dynatrace.com/api/v2/logs/ingest"
  }
}'
```

#### [](#custom-http)Custom HTTP

In this example:

* `$YOUR_CUSTOM_COLLECTOR` is the URL of your custom log collector.
* `$YOUR_COLLECTOR_USER` is the username of the account for your custom log collector.
* `$YOUR_COLLECTOR_PASSWORD` is the password of your custom log collector account.

> [!NOTE]
> The username and password fields are optional for custom HTTP collectors.

Request

```bash
curl -X POST "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/logStreaming" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{
  "streamingEnabled": true,
  "outputType": "https",
  "credentials": {
    "url": "https://$YOUR_CUSTOM_COLLECTOR.com/logs",
    "username": "$YOUR_COLLECTOR_USER",
    "password": "$YOUR_COLLECTOR_PASSWORD"
  }
}'
```

Example 1\. Enable log streaming with excluded App Endpoints

In this example, the `disabledAppEndpoints` array excludes specific App Endpoints from streaming.

Request

```bash
curl -X POST "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/logStreaming" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{
  "streamingEnabled": true,
  "outputType": "datadog",
  "disabledAppEndpoints": ["test-endpoint", "staging-endpoint"],
  "credentials": {
    "apiKey": "YOUR_DATADOG_API_KEY",
    "url": "https://http-intake.logs.datadoghq.com"
  }
}'
```

### [](#get-log-streaming-config)Get Log Streaming Configuration

To view the current log streaming configuration for a specified App Service:

1. Use the [GET /appservices/{appServiceId}/logStreaming](../../cloud/management-api-reference/index.md#tag/App-Services-Log-Streaming/operation/getAppServiceLogStreaming) endpoint.
2. Pass the App Service ID as a path parameter.

Example 2\. Get log streaming configuration

In this example:

* `$appServiceId` is the App Service ID.

Request

```bash
curl -X GET "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/logStreaming" \
  -H "Authorization: Bearer $apiKeySecret"
```

Response

```json
{
  "streamingEnabled": true,
  "logStreamingState": "enabled",
  "outputType": "datadog",
  "disabledAppEndpoints": []
}
```

### [](#pause-resume-log-streaming)Pause and Resume Log Streaming

You can pause log streaming temporarily without removing the configuration, and resume it later.

#### [](#pause-log-streaming)Pause Log Streaming

To pause log streaming for a specified App Service:

1. Use the [DELETE /appservices/{appServiceId}/logStreaming/activationState](../../cloud/management-api-reference/index.md#tag/App-Services-Log-Streaming/operation/deleteAppServiceLogStreamingActivationState) endpoint.
2. Pass the App Service ID as a path parameter.

Example 3\. Pause log streaming

In this example:

* `$appServiceId` is the App Service ID.

Request

```bash
curl -X DELETE "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/logStreaming/activationState" \
  -H "Authorization: Bearer $apiKeySecret"
```

#### [](#resume-log-streaming)Resume Log Streaming

To resume log streaming for a specified App Service:

1. Use the [POST /appservices/{appServiceId}/logStreaming/activationState](../../cloud/management-api-reference/index.md#tag/App-Services-Log-Streaming/operation/postAppServiceLogStreamingActivationState) endpoint.
2. Pass the App Service ID as a path parameter.

Example 4\. Resume log streaming

In this example:

* `$appServiceId` is the App Service ID.

Request

```bash
curl -X POST "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/logStreaming/activationState" \
  -H "Authorization: Bearer $apiKeySecret"
```

### [](#disable-log-streaming)Disable Log Streaming

To disable log streaming for a specified App Service:

1. Use the [DELETE /appservices/{appServiceId}/logStreaming](../../cloud/management-api-reference/index.md#tag/App-Services-Log-Streaming/operation/deleteAppServiceLogStreaming) endpoint.
2. Pass the App Service ID as a path parameter.

This removes the log streaming configuration and stops all streaming.

Example 5\. Disable log streaming

In this example:

* `$appServiceId` is the App Service ID.

Request

```bash
curl -X DELETE "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/logStreaming" \
  -H "Authorization: Bearer $apiKeySecret"
```

## [](#app-endpoint-log-streaming)Change an App Endpoint’s Log Streaming Configuration

You can change the log streaming configuration on an App Endpoint to customize log levels and filters for specific endpoints.

### [](#configure-endpoint-log-streaming)Change App Endpoint Log Streaming Configuration

To change the log streaming configuration for a specified App Endpoint:

1. Use the [PUT /appservices/{appServiceId}/appEndpoints/{appEndpointName}/logStreaming](../../cloud/management-api-reference/index.md#tag/App-Services-Log-Streaming/operation/putAppEndpointLogStreaming) endpoint.
2. Pass the App Service ID and App Endpoint name as path parameters.
3. Pass the log level and filters configuration as the request body. For details, see the [request body schema](../../cloud/management-api-reference/index.md#tag/App-Services-Log-Streaming/operation/putAppEndpointLogStreaming).

> [!NOTE]
> Changing log streaming configuration for an App Endpoint causes it to go offline briefly, which may result in temporary downtime for client applications.

Example 6\. Configure App Endpoint with Info level and default filters

In this example:

* `$appServiceId` is the App Service ID.
* `$appEndpointName` is the App Endpoint name.

Request

```bash
curl -X PUT "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/appEndpoints/$appEndpointName/logStreaming" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{
  "logLevel": "info",
  "logKeys": ["Cache", "Changes", "CRUD", "HTTP", "HTTP+", "Query"]
}'
```

Example 7\. Configure App Endpoint with additional filters

In this example:

* `$appServiceId` is the App Service ID.
* `$appEndpointName` is the App Endpoint name.

This configuration includes additional filters for auth, sync, and DCP operations.

Request

```bash
curl -X PUT "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/appEndpoints/$appEndpointName/logStreaming" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{
  "logLevel": "info",
  "logKeys": [
    "Admin",
    "Auth",
    "Cache",
    "Changes",
    "CRUD",
    "DCP",
    "HTTP",
    "HTTP+",
    "Query",
    "Sync",
    "SyncMsg"
  ]
}'
```

Example 8\. Configure App Endpoint with Warning level

In this example:

* `$appServiceId` is the App Service ID.
* `$appEndpointName` is the App Endpoint name.

Setting the log level to `warning` or `error` reduces the volume of logs streamed.

Request

```bash
curl -X PUT "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/appEndpoints/$appEndpointName/logStreaming" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{
  "logLevel": "warning",
  "logKeys": ["HTTP", "CRUD", "Sync"]
}'
```

### [](#get-endpoint-log-streaming)Get App Endpoint Log Streaming Configuration

To view the current log streaming configuration for a specified App Endpoint:

1. Use the [GET /appservices/{appServiceId}/appEndpoints/{appEndpointName}/logStreaming](../../cloud/management-api-reference/index.md#tag/App-Services-Log-Streaming/operation/getAppEndpointLogStreaming) endpoint.
2. Pass the App Service ID and App Endpoint name as path parameters.

Example 9\. Get App Endpoint log streaming configuration

In this example:

* `$appServiceId` is the App Service ID.
* `$appEndpointName` is the App Endpoint name.

Request

```bash
curl -X GET "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/appEndpoints/$appEndpointName/logStreaming" \
  -H "Authorization: Bearer $apiKeySecret"
```

Response

```json
{
  "logLevel": "info",
  "logKeys": ["Cache", "Changes", "CRUD", "HTTP", "HTTP+", "Query"]
}
```

### [](#reset-endpoint-log-streaming)Reset App Endpoint Log Streaming to Defaults

To reset the log streaming configuration for a specified App Endpoint to the App Service defaults:

1. Use the [DELETE /appservices/{appServiceId}/appEndpoints/{appEndpointName}/logStreaming](../../cloud/management-api-reference/index.md#tag/App-Services-Log-Streaming/operation/deleteAppEndpointLogStreaming) endpoint.
2. Pass the App Service ID and App Endpoint name as path parameters.

Example 10\. Reset App Endpoint log streaming configuration

In this example:

* `$appServiceId` is the App Service ID.
* `$appEndpointName` is the App Endpoint name.

Request

```bash
curl -X DELETE "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/appEndpoints/$appEndpointName/logStreaming" \
  -H "Authorization: Bearer $apiKeySecret"
```

## [](#see-also)See Also

* [Log Streaming](log-streaming.md)
* [Enable Log Streaming](configure-log-collector-app-service.md)
* [Configure Log Streaming for an App Endpoint](configure-log-streaming-app-endpoint.md)