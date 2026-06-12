---
title: Microsoft Teams Alert Payload
description: Learn more about the JSON payload structure used in Capella
  Microsoft Teams alert integrations.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/monitoring/microsoft-reference.adoc
pubDate: 2026-06-12T16:31:57.907Z
link: xref:cloud:clusters:monitoring/microsoft-reference.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/monitoring/microsoft-reference.html)

# Microsoft Teams Alert Payload

> Learn more about the JSON payload structure used in Capella Microsoft Teams alert integrations. 

When you [configure a Microsoft Teams alert integration](configure-microsoft-integration.md), you can structure the JSON alert payload using a template. You can choose between:

* **Standard Template**: A predefined, read-only template.
* **Advanced Template**: A customizable template that you can modify to include specific variables or fields. For more information, see [Advanced Template](alert-integration.md#advanced-template).

These templates use the [Adaptive Cards](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/connectors-using?tabs=cURL%2Ctext1#send-adaptive-cards-using-an-incoming-webhook) message format. Capella automatically inserts both template types with variables that map to the following JSON objects and keys in the alert payload:

| Object or Key | Key                | Description                                                                                                                                                   |
| ------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| alert         | name               | The display name of the alert.                                                                                                                                |
|               | severity           | Identifies the alert as either "critical" or "warning".                                                                                                       |
|               | alertDuration      | The duration of the alert.                                                                                                                                    |
|               | alertDetectedAt    | The date and time when the alert was detected.                                                                                                                |
|               | description        | A description of the alert with potential causes and solutions. For more detailed information, see the [Alert Reference](../../reference/alert-reference.md). |
| tenant        | tenantId           | The unique identifier of the project's tenant.                                                                                                                |
|               | tenantName         | The user-defined name of the tenant.                                                                                                                          |
| project       | projectId          | The unique identifier of the project that contains the affected cluster or App Service.                                                                       |
|               | projectName        | The user-defined name of the project.                                                                                                                         |
| resource      | clusterId          | The unique identifier of the affected cluster.                                                                                                                |
|               | clusterName        | The user-defined name of the cluster.                                                                                                                         |
|               | appServiceId       | The unique identifier of the affected App Service.                                                                                                            |
|               | appServiceName     | The user-defined name of the App Service.                                                                                                                     |
|               | regionProvider     | The region and cloud service provider (CSP) of the resource.                                                                                                  |
|               | capellaResourceUrl | The URL to view the resource in the Capella UI.                                                                                                               |

The following example shows an alert payload for a High CPU Usage Warning alert that Capella sent to Microsoft Teams, formatted using the **Standard Template**:

Example: Alert Payload for Microsoft Teams

```JSON
{
  "type": "AdaptiveCard",
  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
  "version": "1.3",
  "body": [
    {
      "type": "ColumnSet",
      "columns": [
        {
          "type": "Column",
          "items": [
            {
              "type": "TextBlock",
              "text": "🚨",
              "size": "Medium",
              "weight": "Bolder",
              "color": "Attention"
            }
          ],
          "width": "auto"
        },
        {
          "type": "Column",
          "items": [
            {
              "type": "TextBlock",
              "text": "**[Warning] High CPU Usage Warning | Cluster ABC**",
              "weight": "Bolder",
              "size": "Medium",
              "wrap": true,
              "color": "Attention"
            }
          ],
          "width": "stretch",
          "verticalContentAlignment": "Center"
        }
      ]
    },
    {
      "type": "FactSet",
      "facts": [
        {
          "title": "Tenant:",
          "value": "<tenantId>, Tenant ABC"
        },
        {
          "title": "Project:",
          "value": "<projectId>, Project ABC"
        },
        {
          "title": "Cluster:",
          "value": "<clusterId>"
        },
        {
          "title": "Region/Provider:",
          "value": "us-east-1 (AWS)"
        },
        {
          "title": "Alert detected at:",
          "value": "2026-05-08T12:07:20Z"
        },
        {
          "title": "Alert Duration:",
          "value": "42s"
        }
      ],
      "spacing": "Large"
    },
    {
      "type": "TextBlock",
      "text": "**ALERT DETAILS:** During a 5-minute interval, the 5-minute average CPU usage of one or more cluster nodes exceeded 85%. High CPU usage events can impact the throughput of your cluster. This issue could be due to recent changes in the downstream application or dataset, such as changes to the data type sent, the amount of data sent, or natural data/transaction growth. Consider scaling your service nodes to address the issue. If new queries were recently introduced, validate and add the required indexes.",
      "wrap": true,
      "spacing": "Large",
      "separator": true,
      "size": "Default"
    },
    {
      "type": "ColumnSet",
      "spacing": "Medium",
      "columns": [
        {
          "type": "Column",
          "width": "auto",
          "verticalContentAlignment": "Center",
          "items": [
            {
              "type": "Image",
              "url": "https://www.couchbase.com/favicon.ico",
              "size": "Small",
              "width": "18px"
            }
          ]
        },
        {
          "type": "Column",
          "width": "stretch",
          "verticalContentAlignment": "Center",
          "items": [
            {
              "type": "TextBlock",
              "text": "Couchbase Capella Monitoring",
              "size": "Small",
              "isSubtle": true,
              "wrap": true
            }
          ]
        }
      ]
    }
  ],
  "actions": [
    {
      "type": "Action.OpenUrl",
      "title": "View Cluster in Capella",
      "url": "https://cloud.couchbase.com/tenant/<tenantId>/project/<projectId>/clusters/<clusterId>"
    },
    {
      "type": "Action.OpenUrl",
      "title": "Create Support Ticket",
      "url": "https://cloud.couchbase.com/support"
    }
  ]
}
```

## [](#see-also)See Also

* [Configure a Microsoft Teams Alert Integration](configure-microsoft-integration.md)
* [Alert Integrations](alert-integration.md)
* [Alert Reference](../../reference/alert-reference.md)