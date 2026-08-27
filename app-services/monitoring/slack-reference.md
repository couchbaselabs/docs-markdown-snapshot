---
title: Slack JSON Payload for App Services
description: Learn more about the JSON payload structure used in Capella Slack
  alert integrations.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/monitoring/slack-reference.adoc
  xref: xref:app-services::monitoring/slack-reference.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/monitoring/slack-reference.html)

# Slack JSON Payload for App Services

> Learn more about the JSON payload structure used in Capella Slack alert integrations. 

When you [configure a Slack alert integration](configure-slack-integration.md), you can structure the JSON alert payload using a template. You can choose between:

* **Standard Template**: A predefined, read-only template.
* **Advanced Template**: A customizable template that you can modify to include specific variables or fields. For more information, see [Advanced Template](alert-integration.md#advanced-template).

These templates use [Slack Block Kit](https://api.slack.com/block-kit) message format. Capella automatically inserts both template types with variables that map to the following JSON objects and keys in the alert payload:

| Object or Key | Key                | Description                                                                                                                                                         |
| ------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| alert         | name               | The display name of the alert.                                                                                                                                      |
|               | severity           | Identifies the alert as either "critical" or "warning".                                                                                                             |
|               | alertDuration      | The duration of the alert.                                                                                                                                          |
|               | alertDetectedAt    | The date and time when the alert was detected.                                                                                                                      |
|               | description        | A description of the alert with potential causes and solutions. For more detailed information, see the [Alert Reference](../../cloud/reference/alert-reference.md). |
| tenant        | tenantId           | The unique identifier of the project's tenant.                                                                                                                      |
|               | tenantName         | The user-defined name of the tenant.                                                                                                                                |
| project       | projectId          | The unique identifier of the project that contains the affected cluster or App Service.                                                                             |
|               | projectName        | The user-defined name of the project.                                                                                                                               |
| resource      | clusterId          | The unique identifier of the affected cluster.                                                                                                                      |
|               | clusterName        | The user-defined name of the cluster.                                                                                                                               |
|               | appServiceId       | The unique identifier of the affected App Service.                                                                                                                  |
|               | appServiceName     | The user-defined name of the App Service.                                                                                                                           |
|               | regionProvider     | The region and cloud service provider (CSP) of the resource.                                                                                                        |
|               | capellaResourceUrl | The URL to view the resource in the Capella UI.                                                                                                                     |

The following example shows an alert payload for a High CPU Usage Warning alert that Capella sent to Slack, formatted using the **Standard Template**:

Example: Alert Payload for Slack

```JSON
{
  "blocks": [
    {
      "type": "header",
      "text": {
        "type": "plain_text",
        "text": "🚨 [Warning] High CPU Usage Warning | Cluster ABC"
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*Tenant:* <tenantId>, Tenant ABC\n\n\n*Project:* <projectId>, Project ABC\n\n\n*Cluster:* <clusterId>\n\n\n*Region/Provider:* us-east-1 (AWS)\n\n\n*Alert detected at:* 2026-05-08T12:07:20Z\n\n\n*Alert Duration:* 42s\n\n\n\n\n\n*ALERT DETAILS:* During a 5-minute interval, the 5-minute average CPU usage of one or more cluster nodes exceeded 85%. High CPU usage events can impact the throughput of your cluster. This issue could be due to recent changes in the downstream application or dataset, such as changes to the data type sent, the amount of data sent, or natural data/transaction growth. Consider scaling your service nodes to address the issue. If new queries were recently introduced, validate and add the required indexes."
      }
    },
    {
      "type": "actions",
      "elements": [
        {
          "type": "button",
          "text": {
            "type": "plain_text",
            "text": "View Resource in Capella",
            "emoji": true
          },
          "url": "https://cloud.couchbase.com/tenant/<tenantId>/project/<projectId>/clusters/<clusterId>",
          "action_id": "view_capella_resource"
        },
        {
          "type": "button",
          "text": {
            "type": "plain_text",
            "text": "Raise a Ticket",
            "emoji": true
          },
          "url": "https://cloud.couchbase.com/support",
          "action_id": "create_ticket"
        }
      ]
    },
    {
      "type": "context",
      "elements": [
        {
          "type": "image",
          "image_url": "https://www.couchbase.com/favicon.ico",
          "alt_text": "Couchbase Logo"
        },
        {
          "type": "mrkdwn",
          "text": "Couchbase Capella Monitoring"
        }
      ]
    }
  ]
}
```

For more information about monitoring your App Services, see

* [Alert Integrations for App Services](alert-integration.md)
* [Configure a Slack Alert Integration for App Services](configure-slack-integration.md)
* [Alert Reference](../../cloud/reference/alert-reference.md)