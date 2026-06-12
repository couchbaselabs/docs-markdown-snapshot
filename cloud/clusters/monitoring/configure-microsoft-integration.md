---
title: Configure a Microsoft Teams Alert Integration
description: Send Capella metrics-based alerts to your Microsoft Teams channel
  with an alert integration.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/monitoring/configure-microsoft-integration.adoc
pubDate: 2026-06-12T16:31:57.907Z
link: xref:cloud:clusters:monitoring/configure-microsoft-integration.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/monitoring/configure-microsoft-integration.html)

# Configure a Microsoft Teams Alert Integration

> Send Capella metrics-based alerts to your Microsoft Teams channel with an alert integration. 

If your organization uses [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/log-in) to receive, assign, and monitor service issues, you can configure an alert integration to send alerts from Capella to Teams automatically.

Configure an alert integration for each project where you want to send alerts, using either the [Capella UI](#add) or the [Capella Management API](../../management-api-reference/index.md#tag/Alert-Integration).

## [](#prerequisites)Prerequisites

* For full access to Capella alert integrations, you must have 1 of the following roles:

  * [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner)
  * [Project Creator](../../organizations/organization-user-roles.md#organization-role-project-creator)
  * [Project Owner](../../projects/project-roles.md#project-owner-role)
  * [Cluster Manager](../../projects/project-roles.md#project-cluster-manager-role)
* For read-only access, you must have 1 of the following roles:

  * [Organization Member](../../organizations/organization-user-roles.md#organization-role-member) with Read access to the project
  * [Data Reader](../../projects/project-roles.md#project-cluster-data-reader)
* You have deployed an operational cluster or App Service linked to an operational cluster on the [Enterprise](../../billing/billing.md#enterprise) or the [Developer Pro](../../billing/billing.md#dev-pro) Support Plans.  
> [!TIP]  
> For analytics clusters, AI Services, and operational clusters and App Services on the [Basic](../../billing/billing.md#basic) plan, monitor alerts in the [Capella UI](activity-log.md) or by [email](alerts.md).
* You have configured your network firewall to allow inbound traffic from the following IP addresses for Capella alert integrations:

  * 54.236.200.31
  * 3.230.238.38
  * 54.156.132.156  
These IP addresses are static, but are subject to change based on Capella system updates. Capella provides a 30-60 day notice prior to any scheduled IP address rotations.
* You have obtained your connection details from your [Workflows app in Microsoft Teams](https://support.microsoft.com/en-us/office/get-started-with-the-workflows-app-in-microsoft-teams-b7023604-c62a-44d3-a097-fddb68e41ff3). Copy your **Webhook URL**, a user-defined HTTP callback mechanism that uniquely identifies the destination for the alert integration's notifications.  
For more information about incoming webhooks and how to find the URL in the Workflows app, see the [Microsoft Teams documentation on incoming webhooks](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=dotnet).

## [](#add)Add a Microsoft Teams Alert Integration

> [!NOTE]
> You can add up to 5 alert integrations for each project.

To create and configure an alert integration with the Management REST API, see [Create Alert Integration](../../management-api-reference/index.md#tag/Alert-Integration/operation/postAlertIntegration).

To add an alert integration with the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Projects**. Select the project where you want to add an alert integration.
  * Click your current project name or expand the project breadcrumb to select another project.
2. Go to **Alerts**.
3. In **Microsoft Teams**, click **Add Integration**.
4. Enter an identifying **Integration Name**. It can include only alphanumeric characters (`A-Z`, `a-z`, `0-9`), spaces, hyphens (`-`), and underscores (`_`).
5. Enter the **Webhook URL**. For a secure connection with Capella, the URL must begin with `https://`.

  1. (Optional) To add an additional **Webhook URL**, click .
6. Test the connection:

  1. Enter the **Channel Name** of the Microsoft Teams channel where you want to send the test alert.
  2. Click **Test Connection**. You cannot continue until your connection details are accurately configured and the connection test succeeds.
  3. Confirm that the test alert appears in the designated Microsoft Teams channel.
7. To map alerts to specific Microsoft Teams channels, select the relevant clusters or App Services in **Resources** and assign the **MS Teams Channel** that should receive their alerts.

  1. (Optional) To add additional mappings, click **Add More** and repeat the mapping process for each additional channel you want to send alerts to.  
> [!NOTE]  
> You must have at least 1 mapping to connect your integration. You can [edit your mappings](#edit) once your integration is created.
8. Click **Next**.
9. Select an **Alert Name** to customize the payload for that alert.  
You can customize multiple alert payloads in the same integration, and Capella saves each edit so you can configure alerts sequentially without losing previous changes.
10. Choose between a **Standard** template or an **Advanced** template for your alert:

  * Select **Standard Template** to use a pre-built template with no customizations.
  * Select **Advanced Template** to customize the payload.

    1. Customize your alert payload in the JSON editor:

      1. Add or remove variables to tailor the alert data you want in the payload. For a list of all the variables that Capella supports, see [Microsoft Teams Alert Payload](microsoft-reference.md#json-objects-keys-microsoft).
      2. Add custom static values to specify additional information. For example, you can label the alert's environment by adding an object such as `{"title": "Environment:", "value": "Production"}` to an Adaptive Card FactSet element.
      3. Customize the Adaptive Card elements to adjust the layout and appearance of the alert in Microsoft Teams.  
      Any changes to the payload must follow the Adaptive Cards JSON format required by Microsoft Teams. For more information about the Adaptive Card structure and elements, see [Getting Started with Adaptive Cards](https://learn.microsoft.com/en-us/adaptive-cards/authoring-cards/getting-started).  
      > [!CAUTION]  
      > Capella does not mask or sanitize personally identifiable information (PII) or other sensitive data in advanced alert templates. Review your templates and, if necessary, implement the appropriate safeguards to protect your data before sending it to any third-party tool.
    2. Click **Update Preview**.
    3. Review your alert payload format in the **Message Preview**. Capella flags any issues with your JSON formatting. If you receive an error message, confirm your edits follow the required JSON format and try again.
11. (Optional) To customize the payload for additional alerts, select another **Alert Name** and repeat the payload customization steps above.
12. Click **Create Integration**.

## [](#view)View a Microsoft Teams Alert Integration

> [!NOTE]
> The [activity log](activity-log.md) records all add, edit, and delete events for alert integrations. It also records any connection failure events that occur for an alert integration.

To view a list of your alert integrations with the Capella Management API, see [List Alert Integrations](../../management-api-reference/index.md#tag/Alert-Integration/operation/listAlertIntegrations). To view details about a specific alert integration with the Capella Management API, see [Get Alert Integration](../../management-api-reference/index.md#tag/Alert-Integration/operation/getAlertIntegrationByID).

To view an alert integration with the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Projects**. Select the project where you want to add an alert integration.
  * Click your current project name or expand the project breadcrumb to select another project.
2. Go to **Alerts**.
3. In **Microsoft Teams**, click **Manage Integrations**.

A Microsoft Teams alert integration in Capella can have 1 of the following statuses:

| Status   | Description                                                                                                  |
| -------- | ------------------------------------------------------------------------------------------------------------ |
| Active   | Your alert integration is active.                                                                            |
| Disabled | Your alert integration is disabled. [Enable](#enable-disable) your integration to continue receiving alerts. |

## [](#edit)Edit a Microsoft Teams Alert Integration

To edit an alert integration with the Capella Management API, see [Update Alert Integration](../../management-api-reference/index.md#tag/Alert-Integration/operation/putAlertIntegration).

To edit an alert integration with the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Projects**. Select the project where you want to add an alert integration.
  * Click your current project name or expand the project breadcrumb to select another project.
2. Go to **Alerts**.
3. In **Microsoft Teams**, click **Manage Integrations**.
4. Click **More Options (⋮)** **Edit**.
5. Return to the steps for [adding an alert integration](#add) and make your changes.

> [!IMPORTANT]
> You cannot edit your **Webhook URL** details. To change your **Webhook URL**, you must [delete](#delete) your existing alert integration and [create a new one](#add) with the updated details.

## [](#enable-disable)Disable or Enable a Microsoft Teams Alert Integration

Disabling an alert integration pauses it temporarily without deleting it. You can re-enable it when needed.

To disable or enable your alert integrations with the Capella Management API, see [Update Alert Integration](../../management-api-reference/index.md#tag/Alert-Integration/operation/putAlertIntegration).

To disable or enable an alert integration with the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Projects**. Select the project where you want to add an alert integration.
  * Click your current project name or expand the project breadcrumb to select another project.
2. Go to **Alerts**.
3. In **Microsoft Teams**, click **Manage Integrations**.
4. Find your alert integration and click **More Options (⋮)** **Disable** or **More Options (⋮)** **Enable**.
5. Confirm that you want to disable or enable your alert integration and click **Confirm Disable** or **Confirm Enable**.

## [](#delete)Delete a Microsoft Teams Alert Integration

To delete an alert integration with the Capella Management API, see [Delete Alert Integration](../../management-api-reference/index.md#tag/Alert-Integration/operation/deleteAlertIntegrationByID).

To delete an alert integration with the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Projects**. Select the project where you want to add an alert integration.
  * Click your current project name or expand the project breadcrumb to select another project.
2. Go to **Alerts**.
3. In **Microsoft Teams**, click **Manage Integrations**.
4. Find your alert integration and click **More Options (⋮)** **Delete**.
5. Confirm that you want to delete your alert integration and click **Disable and Delete**.

## [](#see-also)See Also

* [Alert Integrations](alert-integration.md)
* [Alert Reference](../../reference/alert-reference.md)
* [Capella Management API](../../management-api-reference/index.md#tag/Alert-Integration)
* [Receive Alerts](alerts.md)
* [Audit Events](../../security/auditing.md)
* [View Activity Logs](activity-log.md)