[View original HTML](/analytics/admin/monitoring/receive-alerts.html)

> Alerts notify you when events with the warning or critical severity level occur in a Capella Analytics cluster. 

You can view alerts in the Capella Analytics UI or enable email notifications to receive email alerts.

For a complete list of alerts, the conditions in which they occur, and a description for each, see [Alerts Reference](../../reference/alerts.md).

## [](#prerequisites)Prerequisites

To receive alerts, you must have a [project role](../../../cloud/projects/project-roles.md) in the project you want to receive alerts about.

## [](#view-alerts-in-the-ui)View Alerts in the UI

Alert banners automatically display in the Capella Analytics UI whenever warning or critical severity events occur in your Capella Analytics cluster. These banners remain on the screen until the event conditions causing the alert are no longer present in your cluster, or until you manually dismiss them.

For example, a critical severity alert banner displays if your cluster’s memory usage exceeds 95% of the available high heap memory. If the issue is addressed, the banner automatically disappears.

The activity logs also keep a record of all current and past alerts. For more information about activity logs and event severity, see [View the Activity Log for a Cluster](view-activity.md).

## [](#receive-email-alerts)Receive Email Alerts

To turn on email notifications and receive email alerts:

1. Go to **My Account**.
2. In the **Notifications** section, click **Receive email notifications**.
3. Click **Save** to start receiving email alerts.

After you turn on email notifications, you receive email alerts from all clusters that belong to projects where you have a project role. These email alerts include the event name, the affected resource, and a link to view the event details in your Capella Analytics cluster’s activity log.

## [](#see-also)See Also

* [Alerts Reference](../../reference/alerts.md)
* [View the Activity Log for a Cluster](view-activity.md)
* [Project Roles](../../../cloud/projects/project-roles.md)