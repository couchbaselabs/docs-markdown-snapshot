---
title: Webhooks Alert Payload
description: Learn more about the JSON payload structure used in Capella
  Webhooks alert integrations.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/monitoring/webhook-reference.adoc
  xref: xref:cloud:clusters:monitoring/webhook-reference.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/monitoring/webhook-reference.html)

# Webhooks Alert Payload

> Learn more about the JSON payload structure used in Capella Webhooks alert integrations. 

In Capella, when you [configure a Webhooks alert integration](configure-webhook-integration.md), you cannot modify the structure of your alert payload.

Capella structures the payload with the following JSON objects and keys:

| Object or Key | Key         | Description                                                                                                                                               |
| ------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| details       | kind        | An abbreviated name for the alert.                                                                                                                        |
|               | name        | The display name of the alert.                                                                                                                            |
|               | severity    | Identifies the alert as either "critical" or "warning".                                                                                                   |
|               | summary     | A brief description of the alert.                                                                                                                         |
|               | description | A detailed description with potential causes and solutions. For more detailed information, see the [Alert Reference](../../reference/alert-reference.md). |
| tenant        | id          | The unique identifier of the project's tenant.                                                                                                            |
|               | name        | The user-defined name of the tenant.                                                                                                                      |
| project       | id          | The unique identifier of the project that contains the affected cluster or App Service.                                                                   |
|               | name        | The user-defined name of the project.                                                                                                                     |
| resource      | kind        | Identifies the affected entity as "cluster" for a cluster or "appService" for an App Service.                                                             |
|               | id          | The unique identifier of the affected cluster or App Service.                                                                                             |
|               | name        | The user-defined name of the resource.                                                                                                                    |
| createdAt     |             | When the event occurred: date and time in ISO 8601 format.                                                                                                |

The following example shows an alert payload for a High CPU Usage Warning alert that Capella sent to its supported third-party tool, ServiceNow:

Example: Alert Payload for ServiceNow

```JSON
{
    "details": {
        "kind": "cpu_usage_high_warning",
        "name": "High CPU Usage Warning",
        "severity": "warning",
        "summary": "The 5-minute average CPU usage of one or more cluster nodes has exceeded 85%.",
        "description": "During a 5-minute interval, the 5-minute average CPU usage of one or more cluster nodes exceeded 85%. High CPU usage events can impact the throughput of your cluster. This issue could be due to recent changes in the downstream application or dataset, such as changes to the data type sent, the amount of data sent, or natural data/transaction growth. Consider scaling your service nodes to address the issue. If new queries were recently introduced, validate and add the required indexes."
    },
    "tenant": {
        "id": "<tenantId>",
        "name": "Organization ABC"
    },
    "project": {
        "id": "<projectId>",
        "name": "Project ABC"
    },
    "resource": {
        "kind": "cluster",
        "id": "<clusterId>",
        "name": "Cluster ABC"
    },
    "createdAt": "2026-05-01T12:07:20Z"
}
```

The JSON payload is automatically formatted to be compatible with ServiceNow's standard webhook requirements. ServiceNow receives this payload and displays the information according to its own interface.

## [](#see-also)See Also

* [Configure a Webhooks Alert Integration](configure-webhook-integration.md)
* [Alert Integrations](alert-integration.md)
* [Alert Reference](../../reference/alert-reference.md)