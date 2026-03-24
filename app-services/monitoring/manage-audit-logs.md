---
title: Manage Audit Logs
description: How to configure and manage audit logging for App Services and App Endpoints.
editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/monitoring/manage-audit-logs.adoc
pubDate: 2026-03-24T03:43:23.693Z
link: xref:app-services::monitoring/manage-audit-logs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/monitoring/manage-audit-logs.html)

# Manage Audit Logs

> How to configure and manage audit logging for App Services and App Endpoints. 

This page is for App Services Audit Logging. To manage Couchbase Capella Operational audits, see [Manage Audits](../../cloud/security/audit-management.md).

To work with audit logging for App Services, you must use the Capella Operational Management API.

* For an overview of the Management API, see [Manage Deployments with the Capella Operational Management API](../../cloud/management-api-guide/management-api-intro.md).
* To get started with the Management API, see [Get Started with the Capella Operational Management API](../../cloud/management-api-guide/management-api-start.md).
* To make an API call, see [Make an API Call with the Capella Operational Management API](../../cloud/management-api-guide/management-api-use.md).
* For a full reference guide, see [Management API Reference](../../cloud/management-api-reference/index.md).

> [!IMPORTANT]
> Auditing is available only to clusters with an Enterprise Service Plan.

## [](#examples-on-this-page)Examples on this Page

In the examples on this page:

* `$organizationId` is the organization ID.
* `$projectId` is the project ID.
* `$clusterId` is the cluster ID.
* `$apiKeySecret` is the API key secret, used as the Bearer token.

The endpoints described on this page all have the same base path: `/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}`. For clarity, this is not shown in the instructions, but it’s included in the examples.

## [](#enable-disable-audit-logs)Enable and Disable App Services Audit Logs

You can enable or disable audit logs for each App Service.

### [](#enable-audit-logs)Enable App Services Audit Logs

To enable audit logging for a specified App Service:

1. Use [PUT /appservices/{appServiceId}/auditLog](../../cloud/management-api-reference/index.md#tag/App-Services-Audit-Logging/operation/putAppServiceAuditLogState).
2. Pass the App Service ID as a path parameter.
3. Pass `"auditEnabled": true` as the request body.

This example enables audit logging for an App Service.

* `$appServiceId` is the App Service ID.

Request

```sh
curl -X PUT "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/auditLog" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{"auditEnabled": true}'
```

### [](#disable-audit-logs)Disable App Services Audit Logs

To disable audit logging for a specified App Service:

1. Use [PUT /appservices/{appServiceId}/auditLog](../../cloud/management-api-reference/index.md#tag/App-Services-Audit-Logging/operation/putAppServiceAuditLogState).
2. Pass the App Service ID as a path parameter.
3. Pass `"auditEnabled": false` as the request body.

This example disables audit logging for an App Service.

* `$appServiceId` is the App Service ID.

Request

```sh
curl -X PUT "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/auditLog" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{"auditEnabled": false}'
```

### [](#view-log-status)View App Services Audit Logging Status

To view the current status of audit logging for a specified App Service:

1. Use [GET /appservices/{appServiceId}/auditLog](../../cloud/management-api-reference/index.md#tag/App-Services-Audit-Logging/operation/getAppServiceAuditLogState).
2. Pass the App Service ID as a path parameter.

If successful, the `auditEnabled` field indicates whether or not audit logging is enabled for the specified App Service.

This example views the status of audit logging for an App Service.

* `$appServiceId` is the App Service ID.

Request

```sh
curl "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/auditLog" \
  -H "Authorization: Bearer $apiKeySecret"
```

Output

```json
{
  "auditEnabled": true
}
```

## [](#filterable-audit-log-events)Filterable Audit Log Events

To get a list of filterable audit log events for a specified App Endpoint:

1. Use [GET /appservices/{appServiceId}/appEndpoints/{appEndpointName}/auditLogEvents](../../cloud/management-api-reference/index.md#tag/App-Services-Audit-Logging/operation/getAppServiceAuditLogEvents).
2. Pass the App Service ID and the App Endpoint name as path parameters.

If successful, the request returns list of all filterable audit log events for the App Endpoint. If a filterable audit log event is currently disabled, you can enable it by including its ID in the `enabledEventIDs` field of the App Endpoint audit log configuration. See [Set the Configuration of App Services Audit Logs](#set-log-config).

This example lists filterable audit log events for an App Endpoint.

* `$appServiceId` is the App Service ID.
* `$appEndpointName` is the App Endpoint name.

Request

```sh
curl "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/appEndpoints/$appEndpointName/auditLogEvents" \
  -H "Authorization: Bearer $apiKeySecret"
```

Output

```json
{
  "events": {
    "53290": {
      "description": "Admin API user successfully authenticated",
      "enabled": true,
      "filterable": true,
      "name": "Admin API user authenticated"
    },
    "53292": {
      "description": "Admin API user failed to authorize",
      "enabled": true,
      "filterable": true,
      "name": "Admin API user authorization failed"
    }
  }
}
```

## [](#configure-app-services-audit-logs)Configure App Services Audit Logs

You can enable, disable, and configure audit logging at the App Endpoint level.

### [](#view-log-config)View the Configuration of App Services Audit Logs

To view the current audit logging configuration for a specified App Endpoint:

1. Use [GET /appservices/{appServiceId}/appEndpoints/{appEndpointName}/auditLog](../../cloud/management-api-reference/index.md#tag/App-Services-Audit-Logging/operation/getAppEndpointAuditLogConfig).
2. Pass the App Service ID and the App Endpoint name as path parameters.

This example shows the current audit logging configuration for an App Endpoint.

* `$appServiceId` is the App Service ID.
* `$appEndpointName` is the App Endpoint name.

Request

```sh
curl "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/appEndpoints/$appEndpointName/auditLog" \
  -H "Authorization: Bearer $apiKeySecret"
```

Output

```json
{
  "auditEnabled": true,
  "enabledEventIds": [
    {
      "id": 0
    }
  ],
  "disabledUsers": [
    {
      "domain": "<DOMAIN>",
      "name": "<USER>"
    }
  ],
  "disabledRoles": [
    {
      "domain": "<DOMAIN>",
      "name": "<ROLE>"
    }
  ]
}
```

### [](#set-log-config)Set the Configuration of App Services Audit Logs

To set the audit log configuration for a specified App Endpoint:

1. Use [PUT /appservices/{appServiceId}/appEndpoints/{appEndpointName}/auditLog](../../cloud/management-api-reference/index.md#tag/App-Services-Audit-Logging/operation/putAppEndpointAuditLogConfig).
2. Pass the App Service ID and the App Endpoint name as path parameters.
3. Pass the required audit logging settings as the request body. For details, see the [request body schema](../../cloud/management-api-reference/index.md#tag/App-Services-Audit-Logging/operation/putAppEndpointAuditLogConfig).

This example sets the audit logging configuration for an App Endpoint.

* `$appServiceId` is the App Service ID.
* `$appEndpointName` is the App Endpoint name.

Request

```sh
curl -X PUT "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/appEndpoints/$appEndpointName/auditLog" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{
  "auditEnabled": true,
  "enabledEventIds": [
    {
      "id": 0
    }
  ],
  "disabledUsers": [
    {
      "domain": "<DOMAIN>",
      "name": "<USER>"
    }
  ],
  "disabledRoles": [
    {
      "domain": "<DOMAIN>",
      "name": "<ROLE>"
    }
  ]
}'
```

## [](#stream-app-services-audit-logs)Stream App Services Audit Logs

You can stream your App Services audit logs to an external storage (host) via a remote endpoint.

> [!NOTE]
> You’re responsible for any third-party audit log collectors that you configure.

### [](#set-streaming-config)Configure Streaming for App Services Audit Logs

To configure audit log streaming for a specified App Service:

1. Use [PUT /appservices/{appServiceId}/auditLogStreaming](../../cloud/management-api-reference/index.md#tag/App-Services-Audit-Logging/operation/putAppServiceAuditLogStreaming).
2. Pass the App Service ID as a path parameter.
3. Pass the required streaming configuration as the request body. For details, see the [request body schema](../../cloud/management-api-reference/index.md#tag/App-Services-Audit-Logging/operation/putAppServiceAuditLogStreaming).

> [!NOTE]
> If you set `"streamingEnabled": true` in the request body, streaming starts. Similarly, if you set `"streamingEnabled": false` in the request body, streaming stops.

This example configures audit log streaming for an App Service.

* `$appServiceId` is the App Service ID.

Request

```sh
curl -X PUT "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/auditLogStreaming" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{
  "streamingEnabled": true,
  "disabledAppEndpoints": [
    "<APPENDPOINT>"
  ],
  "outputType": "https",
  "credentials": {
    "apiKey": "<APIKEY>",
    "url": "<HOSTURL>"
  }
}'
```

### [](#pause-resume-streaming)Pause and Resume Streaming for App Services Audit Logs

To pause audit log streaming for a specified App Service:

1. Use [PATCH /appservices/{appServiceId}/auditLogStreaming](../../cloud/management-api-reference/index.md#tag/App-Services-Audit-Logging/operation/patchAppServiceAuditLogStreaming).
2. Pass the App Service ID as a path parameter.
3. Set `"path": "/streamingEnabled"` and `"value": false` in the request body.

This example pauses audit log streaming for an App Service.

* `$appServiceId` is the App Service ID.

Request

```sh
curl -X PATCH "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/auditLogStreaming" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{
  "op": "update",
  "path": "/streamingEnabled",
  "value": false
}'
```

To resume audit log streaming for a specified App Service:

1. Use [PATCH /appservices/{appServiceId}/auditLogStreaming](../../cloud/management-api-reference/index.md#tag/App-Services-Audit-Logging/operation/patchAppServiceAuditLogStreaming).
2. Pass the App Service ID as a path parameter.
3. Set `"path": "/streamingEnabled"` and `"value": true` in the request body.

This example resumes audit log streaming for an App Service.

* `$appServiceId` is the App Service ID.

Request

```sh
curl -X PATCH "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/auditLogStreaming" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{
  "op": "update",
  "path": "/streamingEnabled",
  "value": true
}'
```

### [](#view-streaming-status)View Status of Streaming for App Services Audit Logs

To view the current state of audit log streaming for a specified App Service:

1. Use [GET /appservices/{appServiceId}/auditLogStreaming](../../cloud/management-api-reference/index.md#tag/App-Services-Audit-Logging/operation/getAppServiceAuditLogStreaming).
2. Pass the App Service ID as a path parameter.

This example shows the status of audit log streaming for an App Service.

* `$appServiceId` is the App Service ID.

Request

```sh
curl "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/auditLogStreaming" \
  -H "Authorization: Bearer $apiKeySecret"
```

Output

```json
{
  "streamingEnabled": true,
  "logStreamingState": "enabling",
  "disabledAppEndpoints": [
    "<APPENDPOINT>"
  ],
  "outputType": "datadog"
}
```

## [](#export-app-services-audit-logs)Export App Services Audit Logs

When you have enabled auditing for an App Endpoint, you can export App Services audit log files to an S3 bucket.

You must create an export job to gather and prepare the audit log files for export.

When the export job has finished, you can download the compressed file from S3, using the supplied download URL. Export requests expire after 72 hours. The download URL is valid for 1 hour when the export request is created.

### [](#create-export-job)Create an App Services Audit Log Export Job

To create an audit log export job for a specified App Service:

1. Use [POST /appservices/{appServiceId}/auditLogExports](../../cloud/management-api-reference/index.md#tag/App-Services-Audit-Logging/operation/postAppServiceAuditLogExport).
2. Pass the App Service ID as a path parameter.
3. Pass the start time and end time for the audit log export job in the request body.

The value for `start` and `end` must in each case be a timestamp in [RFC3339](https://www.rfc-editor.org/rfc/rfc3339.html) format. The `start` must be at least 15 minutes in the past and no more than 30 days in the past. The `end` must be at least 15 minutes after the `start`. For additional requirements, see [Limitations on Export Requests](../../cloud/security/auditing.md#limitations).

If successful, the request returns an audit log Export ID. You can use this to [get the status of an App Services audit log export job](#view-export-job).

This example creates an audit log export job for an App Service.

* `$appServiceId` is the App Service ID.

Request

```sh
curl -X POST "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/auditLogExports" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{
  "start": "2022-09-04T00:56:07.000Z",
  "end": "2022-09-05T04:56:07.000Z"
}'
```

Output

```json
{
  "exportId": "ffffffff-aaaa-1414-eeee-000000000000"
}
```

### [](#view-export-job)Get an App Services Audit Log Export Job

You need the Export ID that was returned when you [created the audit log export job](#create-export-job) to get the status of an App Services audit log export job.

To get the status of an audit log export job for a specified App Service:

1. Use [GET /appservices/{appServiceId}/auditLogExports/{auditLogExportId}](../../cloud/management-api-reference/index.md#tag/App-Services-Audit-Logging/operation/getAppServiceAuditLogExportById).
2. Pass the App Service ID and the Audit Log Export ID as path parameters.

If successful, the request returns the details of the specified audit log export job.

When the export is ready, the `download_id` field gives a URL that you can use to download the exported audit log. The URL remains active for 1 hour. You must start the download before the URL expires.

This example gets the status of an audit log export job for an App Service.

* `$appServiceId` is the App Service ID.
* `$auditLogExportId` is the Audit Log Export ID.

Request

```sh
curl "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/auditLogExports/$auditLogExportId" \
  -H "Authorization: Bearer $apiKeySecret"
```

Output

```json
{
  "id": "920e7b93-28c7-421b-993b-9fffecfd3598",
  "download_id": "https://cb-audit-logs-333d2ad2-1408-405e-9995-XXXX.s3.us-east-1.amazonaws.com/export/app-service-audit-logs-XXXX-from-2024-07-06-to-2024-08-05.tar.gz?X-Amz-Algorithm=AWS4-HMAC-SHA256&X",
  "download_expires": "2024-08-08T13:43:48.420487299Z",
  "status": "Ready",
  "appServiceId": "01071798-23e5-4ec6-b814-13bebef70572",
  "tenantId": "333d2ad2-1408-405e-9995-68338d20ab5c",
  "clusterId": "71dd1cb2-34ac-43ae-a503-b2a9202f02d4",
  "createdByUserID": "d4fa667c-206a-4916-9a24-3a03c2ec5771",
  "upsertedByUserID": "",
  "createdAt": "2024-08-05T13:43:45.998790923Z",
  "upsertedAt": "0001-01-01T00:00:00Z",
  "modifiedByUserID": "d4fa667c-206a-4916-9a24-3a03c2ec5771",
  "modifiedAt": "2024-08-05T13:43:48.420521466Z",
  "version": 3
}
```

### [](#list-export-jobs)List App Services Audit Log Export Jobs

To get a list of all audit log export jobs for a specified App Service:

1. Use [GET /appservices/{appServiceId}/auditLogExports](../../cloud/management-api-reference/index.md#tag/App-Services-Audit-Logging/operation/listAppServiceAuditLogExports).
2. Pass the App Service ID as a path parameter.

If successful, the request returns an array of all the audit log export jobs for the specified App Service.

For each audit log export job, when the export is ready, the `download_id` field gives a URL that you can use to download the exported audit log.

This example gets the status of all audit log export jobs for an App Service.

* `$appServiceId` is the App Service ID.

Request

```sh
curl "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/auditLogExports" \
  -H "Authorization: Bearer $apiKeySecret"
```

Output

```json
{
  "data": [
    {
      "id": "920e7b93-28c7-421b-993b-9fffecfd3598",
      "download_id": "https://cb-audit-logs-333d2ad2-1408-405e-9995-XXXX.s3.us-east-1.amazonaws.com/export/app-service-audit-logs-XXXX-from-2024-07-06-to-2024-08-05.tar.gz?X-Amz-Algorithm=AWS4-HMAC-SHA256&X",
      "download_expires": "2024-08-08T13:43:48.420487299Z",
      "status": "Ready",
      "appServiceId": "01071798-23e5-4ec6-b814-13bebef70572",
      "tenantId": "333d2ad2-1408-405e-9995-68338d20ab5c",
      "clusterId": "71dd1cb2-34ac-43ae-a503-b2a9202f02d4",
      "createdByUserID": "d4fa667c-206a-4916-9a24-3a03c2ec5771",
      "upsertedByUserID": "",
      "createdAt": "2024-08-05T13:43:45.998790923Z",
      "upsertedAt": "0001-01-01T00:00:00Z",
      "modifiedByUserID": "d4fa667c-206a-4916-9a24-3a03c2ec5771",
      "modifiedAt": "2024-08-05T13:43:48.420521466Z",
      "version": 3
    }
  ],
  "cursor": {
    // ...
  }
}
```

## [](#see-also)See Also

* For an overview of App Services audit logs, see [Audit Logging](audit-logging.md).