---
title: View the Activity Log for a Capella Analytics Cluster
description: Activity logs provide an audit trail of events in your Capella
  Analytics cluster.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/admin/pages/monitoring/view-activity.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:analytics:admin:monitoring/view-activity.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/admin/monitoring/view-activity.html)

# View the Activity Log for a Capella Analytics Cluster

> Activity logs provide an audit trail of events in your Capella Analytics cluster. 

Activity logs include the following information for each logged event:

| Field         | Description                                                                                                                                                                                        |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Summary**   | The title of the event. You can click the summary to open a page with details of that specific event.                                                                                              |
| **Severity**  | The severity of the event. One of **Info**, **Warning**, or **Critical**. See [Event Severity](#event-severity) for more information.                                                              |
| **Resource**  | The cluster where the event occurred.                                                                                                                                                              |
| **User**      | Who the event was initiated by. Either a user or, for system-originating events, the System.                                                                                                       |
| **Timestamp** | The date and time of the event. Timestamps include the date and time when the event occurred and how many days, weeks, or months ago that was. All time in the activity log is in your local time. |

## [](#view-an-activity-log)View an Activity Log

To view an activity log:

1. In your Capella Analytics cluster, go to **Settings** **Activity Log**.
2. Use the following available filters to choose the events that appear in the activity log:

  * **User** to filter by who initiated the events.
  * **Severity** to filter by the [severity](#event-severity) of the events.
  * **Tag** to filter by the [tags](#event-tags) of the events.
  * The date and time pickers **To** and **From** to filter by a specific time range.

You can combine multiple filters to narrow down what you’re looking for.

## [](#view-an-event)View an Event

Events are items written to activity logs that reflect specific conditions in your Capella Analytics cluster. To view the details of an event shown in the activity log, click the name of the event under the **Summary** field.

Events with the **Info** severity usually include fewer details. Events with the **Warning** or **Critical** severity can include more information to help you resolve the issue.

To create a support ticket related to the event, click **Create Support Ticket**.

### [](#event-severity)Event Severity

Each event that Capella Analytics emits includes a severity level. The following event severity levels are available:

| Severity | Description                                                                                                                                                                                            |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Info     | Informational events like creating and deleting clusters. Events with an info severity range from user activities to regular database operation tasks.                                                 |
| Warning  | Unexpected issues that affect performance or cause other problems that might need intervention. Events with a warning severity often indicate a database is trending towards more critical thresholds. |
| Critical | Availability affecting events that require immediate intervention. Most events with a critical severity occur due to database resource usage exceeding critical utilization thresholds.                |

### [](#event-tags)Event Tags

Each event in Capella Analytics has one or more tags. Tags categorize events and allow you to filter them. The following tags are available:

| Tag          | Description                                                                                                                               |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Alert        | Events that indicate degraded database performance, availability, or both.                                                                |
| Availability | Events for the creation and deletion of databases and their related resources.                                                            |
| Billing      | Events that can affect billing, such as the creation and deletion of resources.                                                           |
| Maintenance  | Events relating to scheduled or on-demand maintenance tasks, like backup and restore.                                                     |
| Performance  | Events that signal performance-affecting conditions.                                                                                      |
| Security     | Events related to Capella Analytics UI or database access, like the invitation of a new user or the creation of new database credentials. |

## [](#see-also)See Also

* [Receive Alerts for a Cluster](receive-alerts.md)
* [Alerts Reference](#reference/alerts.adoc)