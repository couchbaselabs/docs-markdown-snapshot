---
title: View Health Advisor
description: Capella Health Advisor analyzes the health of your operational
  cluster and provides expert advice to optimize its configurations,
  performance, and stability.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/monitoring/health-advisor.adoc
  xref: xref:cloud:clusters:monitoring/health-advisor.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/monitoring/health-advisor.html)

# View Health Advisor

> Capella Health Advisor analyzes the health of your operational cluster and provides expert advice to optimize its configurations, performance, and stability. 

Capella Health Advisor is a cluster monitoring tool that provides you with ready-to-use insights, best practices, and recommendations for your active operational cluster. Based on Couchbase expertise and knowledge, Health Advisor analyzes your operational cluster and generates a report detailing its current health state.

With proactive warnings and guidance on solutions, the Health Advisor report helps you better understand how to reduce your cluster's risk of incurring future problems.

These reports can be available on a scheduled or per-use basis.

## [](#prerequisites)Prerequisites

To generate a Health Advisor report, you need:

* A paid operational cluster deployed with the **Developer Pro** or **Enterprise** plan.
* An [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner) or [Project Owner](../../projects/project-roles.md#project-owner-role) role in any project where you want to view a Health Advisor report.

To view existing Health Advisor reports:

* A [project role](../../projects/project-roles.md) in any project where you want to view a Health Advisor report.

> [!NOTE]
> This feature is not available to use with Capella Analytics clusters, free tier operational clusters or operational clusters deployed with the **Basic** plan. Use the [**Monitoring** dashboards](metrics-dashboard.md) to view cluster metrics for all Capella operational clusters or [upgrade your plan](../../billing/upgrade-account.md) to get expert advice on your cluster.

## [](#generate-a-new-health-advisor-report)Generate a New Health Advisor Report

To generate a Health Advisor report in the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to get advice.
3. Go to **Monitoring** **Overview**.
4. Click **Get New Health Report**.

It may take a few minutes to generate your new Health Advisor report. You have the option to save it as a PDF for future reference.

## [](#view-health-advisor-reports)View Health Advisor Reports

To view a Health Advisor report in the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to get advice.
3. Go to **Monitoring** **Overview**. As a default, Health Advisor displays the most recent report.
4. (Optional) To view any of the last 10 Health Advisor reports, select the report you want from the date and time list.

### [](#schedule-automatic-reports)Schedule Automatic Reports

> [!NOTE]
> Automatic report scheduling is only available to clusters on an [**Enterprise**](../../support/support.md#support-levels) Plan. To upgrade your Support Plan, see [Change a Cluster's Plan and Support Timezone](../../billing/change-support-plan.md).

Health Advisor supports automatic report generation and delivery. You can choose to schedule and receive weekly reports to your Capella account email address every Monday. You can also enable or disable the automatic generation of Health Advisor reports for your cluster.

To adjust these settings:

1. From your operational cluster, go to **Settings** **Health Advisor**.

## [](#cluster-health-assessment)Cluster Health Assessment

Capella Health Advisor has over 30 different health checks for your cluster. When generating a report, Health Advisor goes through these health checks by analyzing different categories of your cluster, evaluating their severity level and offering advice to optimize your cluster's health.

### [](#severity-level)Severity

Health Advisor checks are assigned a severity level. A higher severity level means greater urgency.

Health Advisor severity levels, from least to most urgent, include:

* **Good**: Your cluster has passed the related checks.
* **Needs Review**: It's recommended to consider following the advice and fixing any issues to prevent future issues.
* **Warning**: It's highly recommended you follow the advice provided and fix any issues in your cluster as soon as possible.

> [!NOTE]
> If your cluster configurations are intentional, but get flagged as **Needs Review**, the advice provided might not be relevant to you.

All Health Advisor advice provided is optional. You can choose which advice and recommendations you want to follow at any time.

### [](#category)Category

Health Advisor reports categorize your clusters health checks and advice with the following categories:

* **Cluster Health**
* **Services Health**: Data, Index and Query Services only.
* **Node Health**
* **App Services Health**

## [](#advice-examples)Advice Examples

The severity levels are there to help direct you to the problem areas in your operational cluster and point out the most relevant advice during that point in time.

The following examples demonstrate different kinds of advice a Health Advisor report could provide for your cluster:

| Advice                      | Severity         | Category | Details                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------------- | ---------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Resident Ratio         | **Good**         | Data     | Your cluster passed this Health Advisor check.                                                                                                                                                                                                                                                                        | A bucket memory quota sets the maximum memory for a bucket's chosen storage engine. The resident ratio for a bucket is the percentage of its data that's stored in RAM.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Multiple Availability Zones | **Needs Review** | Cluster  | Your cluster is currently not deployed using Multiple Availability Zones. Use Multiple Availability Zones to distribute your cluster nodes evenly across your Cloud Service Provider's (CSP) availability zones. Multiple Availability Zones help keep your data available, even if 1 Availability Zone goes offline. | Your cluster is currently not deployed using Multiple Availability Zones. Your cluster could be vulnerable to an Availability Zone outage. You cannot change this setting after you deploy your cluster. If you have an enterprise cluster that requires high availability, create a support ticket to get help with migrating your cluster to Multiple Availability Zones.                                                                                                                                                                                                                  |
| Index Resident Ratio        | **Warning**      | Index    | The resident ratio for 1 or more nodes running the Index Service in your cluster is low, indicating potential memory issues. An index resident ratio is the ratio of index data that can be cached in memory on a node running the Index Service.                                                                     | The index resident ratio on 1 or more Index Service nodes is critically low. We recommend you take immediate action to restore query performance and reduce disk I/O for your index data. We recommend you increase the memory resources on any nodes running the Index Service. If your indexes are partitioned, add the Index Service to additional nodes in your cluster. Consider reviewing and removing unused indexes, merging 2 or more indexes into a single index, or using the Index Advisor to build more efficient indexes. Create a support ticket if you need more assistance. |

For the full list of Health Advisor advice, see [Health Advisor Reference](../../reference/health-advisor-reference.md).

## [](#see-also)See Also

* [View Activity Logs](activity-log.md)
* [Receive Alerts](alerts.md)