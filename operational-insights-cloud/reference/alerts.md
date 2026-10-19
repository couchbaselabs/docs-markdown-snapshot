---
title: Operational Insights Services Alert Reference
description: This reference lists the alerts that Operational Insights services
  can emit, the conditions in which they occur, and a description for each.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Capella
    version: ""
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/reference/pages/alerts.adoc
  xref: xref:analytics:reference:alerts.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights-cloud/reference/alerts.html)

# Operational Insights Services Alert Reference

> This reference lists the alerts that Operational Insights services can emit, the conditions in which they occur, and a description for each. 

## [](#metric-based-alerts)Metric-Based Alerts

Alerts caused by changes to the usage of Operational Insights resources.

The notification messages you receive include information about the potential cause of the alert, as well as the actions you can take to resolve it. For help resolving the alerts, [contact Couchbase support](../../cloud/support/manage-support.md).

Operational Insights delivers alert notifications by:

* Displaying a message banner in the Operational Insights UI.
* Keeping a record of all current and past alerts in the activity logs.
* Sending email to users who enable email notifications for their accounts.

For more information about receiving alert notifications, see [Receive Alerts for a Cluster](../admin/monitoring/receive-alerts.md).

| Display Name             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| High Heap Memory Usage   | The Analytics Service is using high heap memory, and has used at least 95% of its available heap memory. High memory usage events can impact the throughput of your service.                                                                                                                                                                                                                                                                                                                                                                                   |
| Invalid Link Credentials | Link credentials failed more than 10 times in the last 5 minutes when connecting, creating, or editing an Operational Insights link. A large number of wrong failed credentials can indicate a security concern. Links can be Operational Insights links or Kafka links created to connect to data sources like MongoDB, MSK, or S3 that you configured when setting up Operational Insights.                                                                                                                                                                  |
| Link Connection Failure  | Remote link connection from the data source cluster to the Operational Insights cluster has failed and the link is in a disconnected state. If link connection fails, all data updates from the data source stop. A remote link can be any Confluent, MSK, S3, or Couchbase Server link created to connect to data sources like MongoDB, S3, or MySQL that you configured when setting up Operational Insights. Make sure that you're using the correct credentials, URL, and certificate so that the remote link has the correct data source cluster details. |
| HTTP Request Timeouts    | The Analytics Service is experiencing a large number of timeouts in HTTP requests. When the total number of HTTP requests is > 100, 20% of requests are timing out, indicating a connectivity issue when processing Analytics requests.                                                                                                                                                                                                                                                                                                                        |
| HTTP Request Failure     | The Analytics Service is experiencing a large number of failed HTTP requests. When the total number of HTTP requests is > 100, 20% of requests are failing, indicating potential issues with either the requests or the system.                                                                                                                                                                                                                                                                                                                                |
| Scan Wait Timeouts       | The scan consistency requests are timing out. Scan wait timeouts happen when the maximum time to wait for datasets to be updated before executing a query is exceeded. Make sure to provide the appropriate value for the scan\_consistency and scan\_wait parameters.                                                                                                                                                                                                                                                                                         |
| Record Parse Failure     | The Analytics Service is failing to parse records from a link. This indicates an issue with the records being parsed, with the parsing system, or with the link itself.                                                                                                                                                                                                                                                                                                                                                                                        |

## [](#see-also)See Also

* [Monitor a Cluster](../admin/monitoring/monitor-cluster.md)
* [Receive Alerts for a Cluster](../admin/monitoring/receive-alerts.md)