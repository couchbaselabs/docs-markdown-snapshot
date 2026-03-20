---
title: Receive Alerts
description: Alerts notify you when events with the Critical or Warning severity
  level occur in your organization, project, or cluster.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/monitoring/alerts.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:clusters:monitoring/alerts.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/monitoring/alerts.html)

# Receive Alerts

> Alerts notify you when events with the Critical or Warning severity level occur in your organization, project, or cluster. 

You can enable email notifications for your account through the Capella UI, and view alerts in the UI. You can also [configure an integration](alert-integration.md) to send metric-based alerts to a third-party notification system. For a list of alerts and the conditions in which they occur, see [Alert Reference](../../reference/alert-reference.md).

## [](#prerequisites)Prerequisites

To receive alerts in the Capella UI or email, you need:

* A [project role](../../projects/project-roles.md) in any project where you want to receive alerts about events generated from its clusters.

## [](#get-alerts-through-email)Get Alerts through Email

> [!NOTE]
> Email notifications are opt-in for each user.

When you turn on email notifications for your Capella account, you receive email alerts from all clusters in projects where you have a [project role](../../projects/project-roles.md). Email alerts show the event name, affected resource, and a link to view the event in your organization’s Activity Log.

![An example of an email alert notification for a Low Node Disk Storage event.](../_images/alert-email-example.png) 

You manage email notifications for your own account. To turn email notifications for your Capella user account on or off:

1. Click your profile circle.  
Your profile circle appears near the top of every page in the Capella UI and contains your initials.
2. Click **My Account**.
3. Scroll to the **Notifications** section.
4. Select **Receive email notifications** to turn on email notifications or clear it to stop receiving them.
5. Click **Save**.

## [](#view)View Alerts in the Capella UI

Organizations experiencing an active event show an alert near the top of the Capella UI. Capella UI alerts remain until the event conditions causing the alert are no longer present or you dismiss it. For example, if the average CPU usage drops below the critical event threshold for five minutes or more, Capella automatically resolves the related alert. You can dismiss alerts in the Capella UI using the Close () button. The Activity Logs keep a record of all current and past alerts.

For more information about events, see [Monitoring and Alerting](monitoring.md#events).

## [](#see-also)See Also

* [Alert Integrations](alert-integration.md)
* To review a list of all the alerts that Capella can send, see [Alert Reference](../../reference/alert-reference.md).