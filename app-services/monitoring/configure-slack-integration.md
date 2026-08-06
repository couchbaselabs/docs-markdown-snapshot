---
title: Configure a Slack Alert Integration for App Services
description: Send Capella metric-based alerts to your Slack workspace with an
  alert integration.
editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/monitoring/configure-slack-integration.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:app-services::monitoring/configure-slack-integration.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/monitoring/configure-slack-integration.html)

# Configure a Slack Alert Integration for App Services

> Send Capella metric-based alerts to your Slack workspace with an alert integration. 

If your organization uses [Slack](https://slack.com/) to receive, assign, and monitor service issues, you can configure an alert integration to send alerts from Capella to Slack automatically.

Configure an alert integration for each project where you want to send alerts, using either the [Capella UI](#add) or the [Capella Management API](../../cloud/management-api-reference/index.md#tag/Alert-Integration).

## [](#prerequisites)Prerequisites

* For full access to Capella alert integrations, you must have 1 of the following roles:

  * [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner)
  * [Project Creator](../../cloud/organizations/organization-user-roles.md#organization-role-project-creator)
  * [Project Owner](../../cloud/projects/project-roles.md#project-owner-role)
  * [Cluster Manager](../../cloud/projects/project-roles.md#project-cluster-manager-role)
* For read-only access, you must have 1 of the following roles:

  * [Organization Member](../../cloud/organizations/organization-user-roles.md#organization-role-member) with Read access to the project
  * [Data Reader](../../cloud/projects/project-roles.md#project-cluster-data-reader)
* You have deployed an operational cluster or App Service linked to an operational cluster on the [Enterprise](../../cloud/billing/billing.md#enterprise) or the [Developer Pro](../../cloud/billing/billing.md#dev-pro) Support Plans.  
> [!TIP]  
> For analytics clusters, the Couchbase AI Data Plane, and operational clusters and App Services on the [Basic](../../cloud/billing/billing.md#basic) plan, monitor alerts in the [Capella UI](../../cloud/clusters/monitoring/activity-log.md) or by [email](../../cloud/clusters/monitoring/alerts.md).
* You have configured your network firewall to allow inbound traffic from the following IP addresses for Capella alert integrations:

  * 54.236.200.31
  * 3.230.238.38
  * 54.156.132.156  
These IP addresses are static, but are subject to change based on Capella system updates. Capella provides a 30-60 day notice prior to any scheduled IP address rotations.
* You have obtained your connection details from your [Slack app](https://api.slack.com/apps). Copy either your:

  * **Webhook URL**: a user-defined HTTP callback mechanism that uniquely identifies the destination for the alert integration's notifications.  
  For more information about incoming webhooks and how to find the URL in the Slack app, see the [Slack documentation on incoming webhooks](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/).
  * **Bot Token**: authenticates Capella as a bot user so it can send messages to your Slack workspace.  
  For more information about bot tokens and how to find your bot token in the Slack app, see the [Slack documentation on bot tokens](https://docs.slack.dev/authentication/tokens/#bot).  
  > [!IMPORTANT]  
  > Bot Token Settings in Your Slack App  
  >  
  > For Capella to connect using a bot token, you must have:  
  >  
  > * Enabled the following bot token scopes to grant your Slack app the permissions Capella needs to interact with your Slack workspace:  
  >  
  >   * `chat:write`: send messages to channels your Slack app has been invited to.  
  >   * `channels:read`: view the list of public channels.  
  >   * `groups:read`: view the list of private channels your Slack app has been invited to.  
  >   * (Optional) `chat:write.public`: post to any public channel without requiring a manual channel invitation.  
  > For more information about enabling bot token scopes, see the [Slack documentation on scopes](https://docs.slack.dev/app-management/quickstart-app-settings#scopes).  
  > * Authorized your Slack app's access to the specific workspace channels you want Capella to interact with. For more information, see the [Slack documentation on authorization](https://docs.slack.dev/app-management/quickstart-app-settings#installing).

## [](#add)Add a Slack Alert Integration

> [!NOTE]
> You can add up to 5 alert integrations for each project.

To create and configure an alert integration with the Management REST API, see [Create Alert Integration](../../cloud/management-api-reference/index.md#tag/Alert-Integration/operation/postAlertIntegration).

To add an alert integration with the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Projects**. Select the project where you want to add an alert integration.
  * Click your current project name or expand the project breadcrumb to select another project.
2. Go to **Alerts**.
3. In **Slack**, click **Add Integration**.
4. Enter an identifying **Integration Name**. It can include only alphanumeric characters (`A-Z`, `a-z`, `0-9`), spaces, hyphens (`-`), and underscores (`_`).
5. To connect your integration, enter a **Bot Token** or a **Webhook URL**:  
> [!NOTE]  
> Connecting your integration with 1 **Webhook URL** allows you to send alerts to a single channel only. To send alerts to multiple channels, use a **Bot Token**, or configure additional **Webhook URLs**.

  * **Bot Token**: For a secure connection with Capella, the bot token must begin with `xoxb-`.
  * **Webhook URL**: For a secure connection with Capella, the URL must begin with `https://`.

    1. (Optional) To add an additional **Webhook URL**, click .
6. Test the connection:

  1. Enter the **Channel Name** of the Slack channel where you want to send the test alert.
  2. Click **Test Connection**. You cannot continue until your connection details are accurately configured and the connection test succeeds.
  3. Confirm that the test alert appears in the designated Slack channel.
7. To map alerts to specific Slack channels, select the relevant clusters or App Services in **Resources** and assign the **Slack Channel** that should receive their alerts.

  1. (Optional) To add additional mappings, click **Add More** and repeat the mapping process for each additional channel you want to send alerts to.  
> [!NOTE]  
> You must have at least 1 mapping to connect an integration. You can [edit your mappings](#edit) once your integration is created.
8. Click **Next**.
9. Select an **Alert Name** to customize the payload for that alert.  
You can customize multiple alert payloads in the same integration, and Capella saves each edit so you can configure alerts sequentially without losing previous changes.
10. Choose between a **Standard** template or an **Advanced** template for your alert:

  * Select **Standard Template** to use a pre-built template with no customizations.
  * Select **Advanced Template** to customize the payload.

    1. Customize your alert payload in the JSON editor:

      1. Add or remove variables to tailor the alert data you want in the payload. For a list of all the variables that Capella supports, see [Slack Alert Payload](slack-reference.md#json-objects-keys-slack).
      2. Add custom static values to specify additional information. For example, you can label the alert's environment by adding a key-value pair such as `"text": "Environment: Production"` inside a section block's text object.
      3. Customize the block elements to adjust the layout and appearance of the alert in Slack.  
      Any changes to the payload must follow the Slack Block Kit JSON format. For more information about the Slack block structure, types, and fields, see the [Slack documentation](https://docs.slack.dev/reference/block-kit/blocks).  
      > [!CAUTION]  
      > Capella does not mask or sanitize personally identifiable information (PII) or other sensitive data in advanced alert templates. Review your templates and, if necessary, implement the appropriate safeguards to protect your data before sending it to any third-party tool.
    2. Click **Update Preview**.
    3. Review your alert payload format in the **Message Preview**. Capella flags any issues with your JSON formatting. If you receive an error message, confirm your edits follow the required JSON format and try again.
11. (Optional) To customize the payload for additional alerts, select another **Alert Name** and repeat the payload customization steps above.
12. Click **Create Integration**.

## [](#view)View a Slack Alert Integration

> [!NOTE]
> The [activity log](../../cloud/clusters/monitoring/activity-log.md) records all add, edit, and delete events for alert integrations. It also records any connection failure events that occur for an alert integration.

To view a list of your alert integrations with the Capella Management API, see [List Alert Integrations](../../cloud/management-api-reference/index.md#tag/Alert-Integration/operation/listAlertIntegrations). To view details about a specific alert integration with the Capella Management API, see [Get Alert Integration](../../cloud/management-api-reference/index.md#tag/Alert-Integration/operation/getAlertIntegrationByID).

To view an alert integration with the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Projects**. Select the project where you want to add an alert integration.
  * Click your current project name or expand the project breadcrumb to select another project.
2. Go to **Alerts**.
3. In **Slack**, click **Manage Integrations**.

A Slack alert integration in Capella can have 1 of the following statuses:

| Status   | Description                                                                                                  |
| -------- | ------------------------------------------------------------------------------------------------------------ |
| Active   | Your alert integration is active.                                                                            |
| Disabled | Your alert integration is disabled. [Enable](#enable-disable) your integration to continue receiving alerts. |

## [](#edit)Edit a Slack Alert Integration

To edit an alert integration with the Capella Management API, see [Update Alert Integration](../../cloud/management-api-reference/index.md#tag/Alert-Integration/operation/putAlertIntegration).

To edit an alert integration with the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Projects**. Select the project where you want to add an alert integration.
  * Click your current project name or expand the project breadcrumb to select another project.
2. Go to **Alerts**.
3. In **Slack**, click **Manage Integrations**.
4. Click **More Options (⋮)** **Edit**.
5. Return to the steps for [adding an alert integration](#add) and make your changes.

> [!IMPORTANT]
> You cannot edit your **Bot Token** or **Webhook URL** details. To change your Bot Token or Webhook URL, you must [delete](#delete) your existing alert integration and [create a new one](#add) with the updated details.

## [](#enable-disable)Disable or Enable a Slack Alert Integration

Disabling an alert integration pauses it temporarily without deleting it. You can re-enable it when needed.

To disable or enable your alert integrations with the Capella Management API, see [Update Alert Integration](../../cloud/management-api-reference/index.md#tag/Alert-Integration/operation/putAlertIntegration).

To disable or enable an alert integration with the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Projects**. Select the project where you want to add an alert integration.
  * Click your current project name or expand the project breadcrumb to select another project.
2. Go to **Alerts**.
3. In **Slack**, click **Manage Integrations**.
4. Find your alert integration and click **More Options (⋮)** **Disable** or **More Options (⋮)** **Enable**.
5. Confirm that you want to disable or enable your alert integration and click **Confirm Disable** or **Confirm Enable**.

## [](#delete)Delete a Slack Alert Integration

To delete an alert integration with the Capella Management API, see [Delete Alert Integration](../../cloud/management-api-reference/index.md#tag/Alert-Integration/operation/deleteAlertIntegrationByID).

To delete an alert integration with the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Projects**. Select the project where you want to add an alert integration.
  * Click your current project name or expand the project breadcrumb to select another project.
2. Go to **Alerts**.
3. In **Slack**, click **Manage Integrations**.
4. Find your alert integration and click **More Options (⋮)** **Delete**.
5. Confirm that you want to delete your alert integration and click **Disable and Delete**.

For more information about monitoring your App Services, see

* [Alert Integrations for App Services](alert-integration.md)
* [Alert Reference](../../cloud/reference/alert-reference.md)
* [Monitor through the UI](monitoring-in-ui.md)