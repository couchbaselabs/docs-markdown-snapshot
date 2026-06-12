---
title: Alert Integrations
description: Use alert integrations in Capella to send metrics-based alerts to a
  third-party tool.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/monitoring/alert-integration.adoc
pubDate: 2026-06-12T16:31:57.907Z
link: xref:cloud:clusters:monitoring/alert-integration.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/monitoring/alert-integration.html)

# Alert Integrations

> Use alert integrations in Capella to send metrics-based alerts to a third-party tool. 

Capella alert integrations are designed to integrate into your existing workflows, and centralize metrics-based alerts for operational clusters and App Services inside your projects. [Metrics-based Capella alerts](../../reference/alert-reference.md#metric-alerts) can include high disk IOPS usage and data encryption key rotation failures. All alert integrations are configured at the project level in your organization.

You can also view alerts in the [Capella UI](activity-log.md) and receive them by [email](alerts.md).

> [!CAUTION]
> Alert integrations send only [metrics-based alerts](../../reference/alert-reference.md#metric-alerts). Capella alert integrations do not send [operational alerts](../../reference/alert-reference.md#operational-alerts), which are alerts caused by operational disruption.

When Capella flags an alert, it sends a [JSON payload](#alert-payload) with structured alert data to a [supported third-party tool](#third-party-tool). Capella applies a first-in, first-out queue to send 1 alert notification at a time. Typically, Capella sends alert notifications within milliseconds of creation. After Capella sends a notification, the third-party tool controls queuing and the timing of delivery via the connection method.

## [](#third-party-tool)Supported Third-Party Tools

In Capella, you can configure a new alert integration with the following third-party tools:

* [Slack](#slack)
* [Microsoft Teams](#microsoft-teams)
* [Webhooks](#webhooks)

### [](#slack)Slack

Use a Slack alert integration to send Capella alerts to a Slack workspace. In Capella, you can:

* Configure your alert payload with variables and static values to support your alerting needs. The template for Slack integrations uses the [Slack Block Kit](https://api.slack.com/block-kit) message format.
* Connect to Slack with a [bot token](https://docs.slack.dev/authentication/tokens/#bot) or [webhook URL](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/).

For more information about configuring a Slack alert integration, see [Configure a Slack Alert Integration](configure-slack-integration.md). For more information about Slack alert payloads, see [Slack Alert Payload](slack-reference.md).

### [](#microsoft-teams)Microsoft Teams

Use a Microsoft Teams alert integration to send Capella alerts to a Microsoft Teams channel. In Capella, you can:

* Configure your alert payload with variables and static values to support your alerting needs. The template for Microsoft Teams integrations uses the [Adaptive Cards](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/connectors-using?tabs=cURL%2Ctext1#send-adaptive-cards-using-an-incoming-webhook) message format.
* Connect to Microsoft Teams with a [webhook URL](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook).

For more information about configuring a Microsoft Teams alert integration, see [Configure a Microsoft Teams Alert Integration](configure-microsoft-integration.md). For more information about Microsoft Teams alert payloads, see [Microsoft Teams Alert Payload](microsoft-reference.md).

### [](#webhooks)Webhooks

Use a generic Webhooks alert integration to send Capella alerts to any third-party tool that supports webhooks. For example, you can send alerts to [ServiceNow](https://www.servicenow.com/community/in-other-news/how-to-integrate-webhooks-into-servicenow/ba-p/2271745), an incident management tool.

Capella automatically configures a fixed alert payload structure that's compatible with the webhook format. Connect to your third-party tool with a destination URL for the webhook, along with either basic or bearer token authentication and authorization.

For more information about configuring a Webhook alert integration, see [Configure a Webhooks Alert Integration](configure-webhook-integration.md). For more information about Webhook alert payloads, see [Webhooks Alert Payload](webhook-reference.md).

## [](#alert-payload)Alert Payload

The notification message that an alert integration sends includes an alert payload in JSON format. The structure of your alert payload can vary depending on the [third-party tool](#third-party-tool) you're integrating with:

* When you configure a [Slack](configure-slack-integration.md) or [Microsoft Teams](configure-microsoft-integration.md) integration in Capella, you can customize the structure of your alert payload with an [Advanced Template](#advanced-template).
* Webhooks alert integrations have a fixed payload structure that you cannot modify in Capella.

For more information about the alert payload structure for each supported third-party tool, including an example payload, see:

* [Slack Alert Payload](slack-reference.md)
* [Microsoft Teams Alert Payload](microsoft-reference.md)
* [Webhooks Alert Payload](webhook-reference.md)

> [!TIP]
> When you configure workflows in the receiving platform, you can refer to the alert payload to identify actionable values. Your third-party tool might use values in the payload to route, prioritize, or enrich messages from Capella. For example, you might use an alert's severity field to automatically route high-severity alerts to the appropriate destination, such as a channel or assignment group.

### [](#advanced-template)Advanced Template

> [!NOTE]
> The **Advanced Template** is only available for [Slack](configure-slack-integration.md) and [Microsoft Teams](configure-microsoft-integration.md) integrations.

The **Advanced Template** option in the Capella UI includes a JSON editor for customizing your alert payload. Capella initializes the template with default variables. You can modify the template for your workflow requirements by customizing variables, static values, or the layout of the alert payload. A real-time preview displays a valid alert payload with placeholders that update as your template changes. Capella also validates your JSON formatting and flags any syntax issues.

For more information about how to customize your alert payload templates, see [Add a Slack Alert Integration](configure-slack-integration.md#add) or [Add a Microsoft Teams Alert Integration](configure-microsoft-integration.md#add).

## [](#next-steps)Next Steps

Configure your alert integration to send Capella metrics-based alerts to a third-party tool. To get started with:

* The Capella UI, see:

  * [Configure a Slack Alert Integration](configure-slack-integration.md).
  * [Configure a Microsoft Teams Alert Integration](configure-microsoft-integration.md).
  * [Configure a Webhooks Alert Integration](configure-webhook-integration.md).
* The Management REST API, see [Capella Management API](../../management-api-reference/index.md#tag/Alert-Integration).

For more information about monitoring your operational clusters, see:

* [Alert Reference](../../reference/alert-reference.md)
* [Receive Alerts](alerts.md)
* [Audit Events](../../security/auditing.md)
* [View Activity Logs](activity-log.md)