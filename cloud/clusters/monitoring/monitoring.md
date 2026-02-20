---
title: Monitor Clusters
description: Couchbase Capella provides a variety of monitoring tools to assess
  the performance, health, and stability of your cluster.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/monitoring/monitoring.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:clusters:monitoring/monitoring.adoc[]
---

[View original HTML](/cloud/clusters/monitoring/monitoring.html)

# Monitor Clusters

> Couchbase Capella provides a variety of monitoring tools to assess the performance, health, and stability of your cluster. 

The monitoring tools available with Couchbase Capella include:

* Monitoring dashboards with cluster metrics.
* (Developer Pro and Enterprise plans only) Health Advisor reports with expert advice on cluster health and configurations.
* Activity logs with events.
* Alerts to notify you of critical cluster health events.

## [](#monitoring-dashboards)Monitoring Dashboards

The **Monitoring** dashboards in Capella help you monitor the current and past performance of your cluster.

These dashboards display a range of cluster metrics through the [Overview](#cluster-overview), [Service, and Node](#workload-monitoring) dashboards, each providing a different level of performance visibility across your cluster. To investigate specific issues or analyze metric relationships, use the [Metrics Explorer](#metrics-explorer) to select and view custom sets of metrics together.

### [](#cluster-overview)Cluster Overview

The **Cluster Overview** dashboard provides a general summary of your cluster’s metrics, including a quick view of its configuration, Health Advisor status, and recent entries from the Activity Log.

For more information, see [View Cluster Overview](#clusters:clusters:monitoring/metrics-dashboard.adoc#cluster-overview).

### [](#workload-monitoring)Workload Dashboards

The **Workload Monitoring** dashboards identify key metrics for monitoring the state and workload of your cluster’s Services and nodes.

Workload monitoring is available for:

* [Data Service](metrics-dashboard.md#data-service)
* [Index Service](metrics-dashboard.md#index-service)
* [Query Service](metrics-dashboard.md#query-service)
* [Node Metrics](metrics-dashboard.md#node-metrics)

Service-based metrics help you monitor resource usage, identify bottlenecks, and assess the efficiency of individual Services in real time. Node-based metrics help you monitor resource utilization, track performance trends, and identify potential issues at the node level.

For more information, see [View Workload Dashboards](metrics-dashboard.md#workload-monitoring).

### [](#metrics-explorer)Metrics Explorer

The **Metrics Explorer** dashboard allows you to customize what metrics to track and chart this data over specified time frames.

For more information, see [View Metrics Explorer](metrics-dashboard.md#metrics-explorer-dashboard).

## [](#health-advisor)Health Advisor

The Capella Health Advisor provides a proactive, weekly review of your cluster’s health by analyzing trends and patterns over a week at a time. It highlights potential issues, offers reactive observations, and recommends optimizations to improve stability, performance, and resource efficiency across your operational cluster.

Capella Health Advisor is only available for paid operational clusters deployed with the **Developer Pro** or **Enterprise** plan.

For more information, see [View Health Advisor](health-advisor.md).

## [](#activity-logs)Activity Logs

The Activity Logs in Capella provide a complete auditable timeline of [events](#events) occurring in your organization, projects, and clusters. Each event in an Activity Log includes a summary of the activity, severity, resource affected, actor, and when it occurred. Filtering allows you to narrow down what events appear in an Activity Log based on clusters, projects, users, severity, tag, and date. In Capella, you can [view an Activity Log](activity-log.md) for your organization, each project, and each cluster.

## [](#events)Events

Events are items written to [Activity Logs](#activity-logs) that reflect specific conditions in your Capella organization, project, and cluster. Events can include service-affecting conditions to user activity.

> [!TIP]
> For a list of the events and alerts in Capella, see [Alert Reference](../../reference/alert-reference.md).

### [](#event-severity)Event Severity

Each event that Capella emits includes a severity level. The following table describes the event severity levels in Capella:

| Severity | Description                                                                                                                                                                                         | Sends alert |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Info     | Informational events. Events with an info severity range from user activities to regular cluster operation tasks.                                                                                   |             |
| Warning  | Unexpected issues that affect performance or cause other problems that may need intervention. Events with a warning severity often indicate a cluster is trending towards more critical thresholds. | ✔           |
| Critical | Availability affecting events that require immediate intervention. Most events with a critical severity occur due to cluster resource usage exceeding critical utilization thresholds.              | ✔           |

### [](#event-tags)Event Tags

Each event in Capella has one or more tags. Tags categorize events, allowing you to filter events. The following table lists each available tag type:

| Tag          | Description                                                                                                                      |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| Alert        | Events that indicate degraded cluster performance, availability, or both.                                                        |
| Availability | Events for the creation and deletion of clusters and their related resources.                                                    |
| Billing      | Events that can affect billing, such as the creation and deletion of resources.                                                  |
| Maintenance  | Events relating to scheduled or on-demand maintenance tasks, such as backup and restore.                                         |
| Performance  | Events that signal performance-affecting conditions.                                                                             |
| Security     | Events related to Capella UI or cluster access, such as the invitation of a new user or the creation of new cluster credentials. |

## [](#alerts)Alerts

Capella generates an alert when there’s an event with a warning or critical severity.

To [receive alerts](alerts.md) from Capella, you can:

* Use the Capella UI to view and dismiss alerts.
* [Enable email notifications for your account](alerts.md#manage-email-notifications).
* [Configure an integration](alert-integration.md) with a third-party notification system.

To resolve an alert, improve the immediate conditions producing the related event.

[Activity Logs](#activity-logs) keep a record of all past events, including those that generate alerts.

## [](#see-also)See Also

* [Alert Reference](../../reference/alert-reference.md)
* [Receive Alerts](alerts.md)
* [Alert Integrations](alert-integration.md)
* [View Activity Logs](activity-log.md)
* [View Monitoring Dashboards](metrics-dashboard.md)
* [Audit Events](../../security/auditing.md)