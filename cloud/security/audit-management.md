[View original HTML](/cloud/security/audit-management.html)

> You can use the Management API to audit actions performed on Capella. This allows users to ensure that system-management tasks are being appropriately performed. 

## [](#audit-records-and-their-content)Audit Records and Their Content

Capella Auditing creates records and captures information about what actions have been performed, and whether those actions were successful. Each record is stored as a JSON document, and appended to a log file, per node. Use the Management API to configure audit logging and download log files for a given time period.

For an overview of event auditing, see [Auditing](auditing.md).

For lists of auditable events, see [Event Tables](auditing.md#event%5Ftables).

|  | Auditing is available only to clusters with an Enterprise Service Plan. |
|  | ----------------------------------------------------------------------- |

## [](#auditing-api)Auditing API

As part of the Management API, the auditing methods and endpoints allow you to:

* List filterable audit log events. A filterable event is one that can be individually enabled or disabled.
* Get the cluster audit log configuration. Output includes a list of all enabled audit events, a list of disabled users, and whether audit logging is currently enabled for a cluster.
* Update the cluster audit log configuration. Enable or disable audit logging, and configure enabled events and disabled users.
* Create an audit log export job. An audit log export job prepares a download of all log files within a user-specified time-period.
* List recent cluster audit log export jobs or a get cluster audit log export. The output includes a status for each audit log export job, and a URL to a compressed archive of the audit logs once fully processed by Capella.

For more information about how to use the Management API and the calls described on this page, see [Make an API Call with the Management API](../management-api-guide/management-api-use.md).

### [](#list-filterable-audit-log-events)List Filterable Audit Log Events

To return a list of all filterable audit log events, use [GET /v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/auditLogEvents](../management-api-reference/index.md#tag/Audit-Logs/operation/getAuditLogEventIDs).

Output resembles the following:

```json
{
  "events": [
    {
      "description": "Document was mutated via the REST API",
      "id": 8243,
      "module": "ns_server",
      "name": "mutate document"
    },
    {
      "description": "Document was read via the REST API",
      "id": 8255,
      "module": "ns_server",
      "name": "read document"
    },
    {
      "description": "An alert email was successfully sent",
      "id": 8257,
      "module": "ns_server",
      "name": "alert email sent"
    },
    {
      "description": "RBAC information was retrieved",
      "id": 8265,
      "module": "ns_server",
      "name": "RBAC information retrieved"
    },
            .
            .
            .
  ]
}
```

The list contains all filterable audit log events for the cluster. If a filterable audit log event is currently disabled, you can enable it by including its ID in the `enabledEventIDs` field of [Update Cluster Audit Log Configuration](#update-cluster-audit-log-configuration).

### [](#get-cluster-audit-log-configuration)Get Cluster Audit Log Configuration

To get the current audit settings for the cluster, use [GET /v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/auditLog](../management-api-reference/index.md#tag/Audit-Logs/operation/getClusterAuditSettings).

Output resembles the following:

```json
{
  "auditEnabled": true,
  "disabledUsers": [
    {
      "domain": "local",
      "name": "dfelton"
    }
  ],
  "enabledEventIDs": [
    [
      8243,
      8255
    ]
  ]
}
```

In this sample output, the value of `auditEnabled` is `true`. When this setting is true, auditing is enabled for the whole cluster. All non-filterable audit events and a user-specified subset of filterable audit events are enabled.

The value of `disabledUsers` is an array. Each element in the array is an object that specifies a domain and a name. If a user is disabled, no filterable events are logged for that user. For information on disabling users, see [Ignoring Filterable Events by User](auditing.md#ignoring-events-by-user).

The value of `enabledEventIDs` is an array. Each element in the array is the ID of a filterable event. Each filterable event that corresponds to an ID in the array is enabled. If a filterable event does not have its ID in the array, it is disabled.

|  | The API still returns the ID values of enabled filterable events, even when the value of auditEnabled is false and no auditing occurs on the cluster. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#update-cluster-audit-log-configuration)Update Cluster Audit Log Configuraiton

To update your audit log configuration, use [PUT /v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/auditLog](../management-api-reference/index.md#tag/Audit-Logs/operation/putClusterAuditSettings).

Output resembles the following:

```json
{
  "auditEnabled": true,
  "disabledUsers": [
    {
      "domain": "local",
      "name": "@eventing"
    }
  ],
  "enabledEventIDs": [
    8243,
    8255
  ]
}
```

The value of `auditEnabled` is `true`, specifying that auditing should be enabled for the entire cluster: this enables all _non-filterable_ audit events, and makes possible the enabling of specific _filterable_ audit events.

The value of `disabledUsers` is an array, each of whose elements is an object that specifies a domain and a username. For each user corresponding to a username, filterable audit events are disabled. See [Ignoring Filterable Events by User](auditing.md#ignoring-events-by-user).

The value of `enabledEventIDs` is an array of integers, each of which is the ID of a filterable audit event. Each event corresponding to an included ID is enabled for the cluster.

No object is returned. Subsequent to the call, the resulting configuration can be checked by means of [GET /v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/auditLog](../management-api-reference/index.md#tag/Audit-Logs/operation/getClusterAuditSettings).

### [](#create-cluster-audit-log-export-job)Create Cluster Audit Log Export Job

After enabling auditing for the cluster, you can use an audit log export job to download your log files.

Use the [POST /v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/auditLogExports](../management-api-reference/index.md#tag/Audit-Logs/operation/postAuditLogExport) endpoint, with a JSON payload such as the following:

```json
{
  "start": "2022-09-04T00:56:07.000Z",
  "end": "2022-09-05T04:56:07.000Z"
}
```

The value for `start` and `end` must in each case be a timestamp in [RFC3339](https://www.rfc-editor.org/rfc/rfc3339.html) format. The `start` must be at least 15 minutes in the past and no more than 30 days in the past. The `end` must be at least 15 minutes after the `start`. For additional requirements, see [Limitations on Export Requests](auditing.md#limitations).

The API triggers a request to collect and prepare a download of log files from the specified time-period. The returned value includes a `exportId`. Use this ID in a Get Cluster Audit Log Export call. For example:

```json
{
  "exportId": "ffffffff-aaaa-1414-eeee-000000000000"
}
```

### [](#get-cluster-audit-log-export)Get Cluster Audit Log Export

Once you create a cluster audit export job, use the [GET /v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/auditLogExports/{auditLogExportId}](../management-api-reference/index.md#tag/Audit-Logs/operation/getAuditLogExport) endpoint to get the status of the export.

This same endpoint returns the time the export job request was created, the start and end time of the log file period, and a download URL for the log files when the download is ready.

The `auditLogExportId` parameter must be an export ID previously returned by [POST /v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/auditLogExports](../management-api-reference/index.md#tag/Audit-Logs/operation/postAuditLogExport), as the value of the `exportId` field.

When the endpoint returns a `status` of `Completed`, the compressed file can be manually downloaded, using the download URL value from `AuditLogDownloadURL`. The `AuditLogDownloadURL` will be active for 1 hour. You must start the download before the URL expires.

|  | Each request generates a new download URL. Multiple download URLs can co-exist and be used to download an export. |
|  | ----------------------------------------------------------------------------------------------------------------- |

Requests for audit logs more than 24 hours in the past may take up to 5 minutes to finish processing. For example:

```json
{
  "createdAt": "2023-05-16T04:00:08.870Z",
  "auditLogExportId": "40b9318a-cc93-458d-bc3e-7d4ffa778386",
  "start": "2023-05-15T04:56:07.000Z",
  "end": "2023-05-16T04:56:07.000Z",
  "status": "Completed",
  "auditLogDownloadURL": "https://cb-audit-logs-ffffffff-aaaa-1414-eeee-000000000000.s3.amazonaws.com/export/audit-logs-cluster-ffffffff-aaaa-1414-eeee-000000000000-from-2222-08-25%2007%3A52%3A44.377%20%2B0000%20UTC-to-2222-09-01%2007%3A52%3A44.377%20%2B0000%20UTC.tar.gz?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=JX7GZ5Q1WK9X7GZ5Q1WJF%2F20220901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220901T080237Z&X-Amz-Expires=259200&X-Amz-Security-Token=9qD87zY0m2fT4V3x6hC1sW5B2kEuG9jP7rA4N8Q0bO6lK5I3&X-Amz-SignedHeaders=host&X-Amz-Signature=k9X7gZ5Q1W",
  "expiration": "2023-05-19T04:00:08.870Z"
}
```

### [](#list-cluster-audit-log-export-jobs)List Cluster Audit Log Export Jobs

To return a list of all cluster audit log export jobs, use [GET /v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/auditLogExports](../management-api-reference/index.md#tag/Audit-Logs/operation/listAuditLogExports).

The list starts with the most recent request.

This endpoint returns the time the export job request was created, the start and end time of the log file period, a download URL for the compressed file containing the log files, and the status of the request.

For example, the following is an example response with a single request. You can also get this response with the `GET {id}/auditLogExports/{auditLogExportId}` endpoint, where `d9db8594-4d0d-43b5-8dfe-1a6679d5b7d3` is the `auditLogExportId`.

```json
{
  "cursor": {
    // ...
  },
  "data": [
    {
      "createdAt": "2023-05-16T06:43:46.264296574Z",
      "exportId": "d9db8594-4d0d-43b5-8dfe-1a6679d5b7d3",
      "start": "2023-05-15T04:56:07Z",
      "end": "2023-05-16T06:43:46.255479842Z",
      "status": "Failed"
    },
    {
      "createdAt": "2023-05-16T06:39:33.745602046Z",
      "exportId": "624752e7-4600-4007-9a29-15d1323fbd0c",
      "start": "2023-05-15T04:56:07Z",
      "end": "2023-05-16T06:39:33.732661698Z",
      "status": "Queued"
    }
  ]
}
```

In the above output, the `status` of the first request is `Failed`, and the second request is still `Queued`. A job must have a `status` of `Completed` before you can download the compressed file from the download URL in `AuditLogDownloadURL`.