[View original HTML](/app-services/monitoring/audit-logging.html)

> Audit logging is the process of recording and storing detailed logs of user and system activity within your application. This feature helps administrators track operational irregularities and supports regulatory and security compliance standards. 

This page is for App Services Audit Logging. For Couchbase Capella Operational auditing, see [Audit Events](../../cloud/security/auditing.md).

## [](#about-audit-logging)About Audit Logging

* **Audit Logs**: Logs use JSON format structures and capture essential details like who performs an action, what action occurs, when it happens, and where the action takes place. Once recorded, no one alters these logs, ensuring the integrity of the records.
* **Configurability**: Capella provides a high degree of flexibility, allowing administrators to enable, disable, and configure audit logging to fit their operational needs via the Management API.
* **Retrieving Audit Logs through Data Export and Streaming**: You can export Audit logs for download or stream them in real time to third-party observability platforms.

|  | Auditing is available only to clusters with an Enterprise Service Plan. |
|  | ----------------------------------------------------------------------- |

## [](#configuring-audit-logging)Configuring Audit Logging

Audit logging is an opt-in feature that administrators can enable and configure through the [Capella Operational Management API](../../cloud/management-api-reference/index.md). Configuration options enable administrators to activate or deactivate audit logging, specify users whose actions to exclude, and define which events to capture, providing granular control over logging behavior.

## [](#auditing-events)Auditing Events

Audit logging provides robust control over event management:

* **Enable/Disable Audit Logging**: Administrators can opt-in to enable or disable audit logging based on operational needs.
* **Filtering Events**: By configuring the enabled event IDs, disabled users, or disabled roles, administrators can filter which events are logged and exclude specific users' or roles' actions from audit logging.

To see a list of available Audit Logs events and their corresponding IDs, see [Audit Logging Events Reference](../../sync-gateway/current/security/audit-log-events.md).

|  | The bootstrap configuration and Admin API mentioned on the see [Audit Logging Events Reference](../../sync-gateway/current/security/audit-log-events.md) page do not apply to App Services. Use this page to determine which events you want to add to the App Services audit log. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#retrieving-audit-logs)Retrieving Audit Logs

Capella stores audit logs and writes them in [JSON-lines format](https://jsonlines.org/). Only one audit log file remains active at a time, which the system periodically rotates. Capella provides two ways to retrieve audit logs: through log export and zip download, or through real-time audit logs streaming.

|  | Log Persistence Couchbase does not guarantee the persistence of logs on Capella. To verify that logs persist for your required duration, download them through logs export or retrieve them in real-time via streaming to a third-party platform or self-hosted log collector. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### [](#log-export-and-download)Log Export and Download

Capella makes audit logs exportable once rotation completes. You can start the export of logs via the Capella Operational Management API by specifying a start and end date for the requested logs.

Audit logs are rotated automatically based on two thresholds:

* **File size limit**: Logs rotate when they reach 100MB in size.
* **Time period limit**: Logs rotate after 3 hours.

Whichever threshold is reached first triggers the rotation, making the logs available for export.

* You can start multiple export jobs per App Service.
* Capella assigns each export job a unique ID.
* When the export job status is ready, it returns a download URL. You can use this URL to download logs as a 'zip' file from Amazon S3.

For details, see [Export App Services Audit Logs](manage-audit-logs.md#export-app-services-audit-logs).

### [](#real-time-audit-log-streaming)Real-Time Audit Log Streaming

|  | Couchbase is not responsible for any third-party endpoints you configure. |
|  | ------------------------------------------------------------------------- |

Capella App Services allows real-time streaming of audit logs to third-party observability platforms or self-hosted log collectors. This is managed via the Capella Operational Management API.

Supported Log Collector Providers:

* [Datadog](https://www.datadoghq.com/)
* [Sumo Logic](https://www.sumologic.com/)
* [Grafana Loki](https://grafana.com/oss/loki/)
* [Elasticsearch](https://www.elastic.co/elasticsearch)
* [Splunk](https://www.splunk.com/)
* [Dynatrace](https://www.dynatrace.com/)
* Self-hosted collectors via HTTPS

For details, see [Stream App Services Audit Logs](manage-audit-logs.md#stream-app-services-audit-logs).

|  | App Service audit log streaming is not the same as [App Service log streaming](log-streaming.md), which allows real-time streaming of console logs to gain insights into the behavior of the application and has its own opt-in and configuration process. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

|  | Capella supports only Elasticsearch versions 8+. Elasticsearch supports only the basic auth method. Elasticsearch creates and uses an Elasticsearch Index named capella-app-services. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#see-also)See Also

* To manage App Services audit logs, see [Manage Audit Logs](manage-audit-logs.md).