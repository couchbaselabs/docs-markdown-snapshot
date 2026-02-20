---
title: View Activity Logs
description: Capella Activity Logs provide audit trails of events in your
  organization, project, and cluster.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/monitoring/activity-log.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:clusters:monitoring/activity-log.adoc[]
---

[View original HTML](/cloud/clusters/monitoring/activity-log.html)

# View Activity Logs

> Capella Activity Logs provide audit trails of events in your organization, project, and cluster. 

## [](#prerequisites)Prerequisites

To view an activity log, filter it, and view its events, you need:

* A [project role](../../projects/project-roles.md) in any project where you want to see events generated from its clusters.

## [](#view-an-activity-log)View an Activity Log

To view an activity log in the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. To view the activity log for your organization, click your organization name.
  2. To view the activity log for a project, click your current project name or search for a project.
  3. To view the activity log for a different cluster, expand the cluster breadcrumb and search for a cluster.
2. Go to **Settings** **Activity Log**.

Activity Logs show a running log of events for the chosen scope. Each event includes details about when, where, and if relevant, why the event occurred.

> [!NOTE]
> Events in the **Activity Log** are automatically deleted after 2 years.

Activity Logs include the following information for each logged event:

| Field         | Description                                                                                                                                                                                                 |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Summary**   | The title of the event. Clicking the summary opens an event details page.                                                                                                                                   |
| **Severity**  | The severity of the event. Each event has one severity level: Info, Warning, or Critical. See [Events](monitoring.md#events) for more information.                                                          |
| **Resource**  | The Capella resource where the event occurred. Resources can include specific organizations, projects, clusters, or App Services.                                                                           |
| **User**      | Who initiated the event. The user can be someone in your organization or "System" representing system-originating events.                                                                                   |
| **Timestamp** | The date and time of the event. Timestamps include the date and your local time when the event occurred and how many days, weeks, or months ago it was. All time in the Activity Log is in your local time. |

## [](#filter-activity-logs)Filter Activity Logs

Use filtering to choose what events appear in an Activity Log based on the user, cluster, project, event severity, event tag, and time range. You can combine multiple filters to narrow down what you’re looking for. The available filters depend on which Activity Log you’re viewing. For example, when viewing the Activity Log for a cluster you won’t be able to filter by cluster or project.

Filter by time range

Use the **From** and **To** date and time pickers to choose a time range where you want to see activity. All time in the Activity Log is in your local time.

Filter by user

Choose a user whose initiated events you want to see.

Filter by cluster

Choose a cluster from which you want to see events.

Filter by project

Choose the project from which you want to see events. This includes events from every cluster within the chosen project.

Filter by severity

Choose the [severity](monitoring.md#event-severity) of the events you want to see.

Filter by event tag

Choose the [tag](monitoring.md#event-tags) of the events you want to see.

To remove a specific filter, deselect the attribute from its related list. Refreshing the page removes all of the filters applied to an Activity Log.

For a list of all the alerts that appear in the Activity Log and their tags, see [Alert Reference](../../reference/alert-reference.md).

## [](#alert-flyout)View Events

To view the details of an event shown in the Activity Log, click the event’s name.

When you view an event, you can:

* Click the cluster’s name to open the cluster where the event occured.
* Click the **Open chart image** link to open a metric chart in a new browser tab. This chart shows metrics related to the event for the time period before and when the event occurred.
* Click **Create Support Ticket** to create a support ticket related to that open event.

## [](#next-steps)Next Steps

* [View Monitoring Dashboards](metrics-dashboard.md)
* [Receive Alerts](alerts.md)