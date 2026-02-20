---
title: Support Overview
description: Couchbase Capella offers multiple levels of support for each cluster.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/support/pages/support.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:support:support.adoc[]
---

[View original HTML](/cloud/support/support.html)

# Support Overview

> Couchbase Capella offers multiple levels of support for each cluster. 

> [!NOTE]
> To ask for assistance, see [Request Support](manage-support.md).

All clusters in Couchbase Capella must have an associated _Support Plan_. For the free tier operational cluster, support is provided on the **Basic** plan on a best-effort basis through the Couchbase community. Different Support Plans are available. You can select a plan _per cluster_.

When deploying a cluster, you need to select a Support Plan and a Support Time Zone for the cluster.

The plan you select determines:

* The hourly price that you are [billed](../billing/billing.md) for that cluster.
* The [level of support](#support-levels) that the cluster is entitled to.

The [Support Time Zone](#support-time-zones) that you select determines when the time window for human support begins and ends for clusters that aren’t on a plan that comes with 24x7 support.

> [!NOTE]
> If you’re a free tier plan user, you’re community-supported.
> 
> This includes the Couchbase [forums](https://www.couchbase.com/forums/tag/couchbase-capella), [discord channel](https://discord.com/invite/K7NPMPGrPk?utm%5Fsource=forums&utm%5Fmedium=pinnedpost&utm%5Fcampaign=discord) and [documentation](../get-started/intro.md).
> 
> Find the support page in the Capella UI: next to your user profile, click **Get Help** to access the support you need.
> 
> You can also fill out a feedback form to provide your input and insights on Couchbase Capella. For more information, see [Provide Feedback](feedback.md).
> 
> For more support options, [upgrade your plan](../billing/upgrade-account.md).

## [](#support-levels)Cluster Support Plan Levels

Each [Support Plan](../billing/billing.md#support-plans) comes with entitlements to different levels of support. Clusters on the Enterprise Plan receive 24x7 human support and the fastest guaranteed support response time. Clusters on the Developer Pro plan receive a lower guaranteed support response time.

Where there is a time window for human support (as opposed to 24x7 support), the time window begins and ends based on the cluster’s [Support Time Zone](#support-time-zones).

To upgrade or downgrade a cluster to a particular Support Plan, see [Change a Cluster’s Plan](../billing/change-support-plan.md).

See the [Capella Support Policy](https://www.couchbase.com/support-policy/cloud) page for full conditions on the following paid Support Plans:

| Support Plan            | Description                                                                                          |
| ----------------------- | ---------------------------------------------------------------------------------------------------- |
| Developer Pro           | Use for production-ready applications with a 99.99% uptime SLA.                                      |
| Enterprise Support Plan | Use for mission critical applications, covering all services with the fastest support response time. |

## [](#support-time-zones)Support Time Zones

In addition to selecting a Support Plan for each cluster, you will also select a _Support Time Zone_. The time zone that you select primarily affects clusters that are on a Support Plan that comes with a support time window.

If a cluster’s Support Plan comes with a support time window of 9:00am - 5:00pm for P3 and P4 issues, then selecting Pacific Time for the Support Time Zone means that you can receive support for these issues, for that cluster, between 9:00am - 5:00pm PT (4:00pm - 12:00am GMT).

Couchbase Capella makes available a select number of Support Time Zones to choose from. Select the Support Time Zone that is most appropriate for each cluster. For example, when cluster administrators can interact with Couchbase Capella Support staff.

A cluster’s Support Time Zone is initially set when the [cluster is created](../clusters/create-database.md). To modify the Support Time Zone, see [Change a Cluster’s Support Timezone](../billing/change-support-plan.md).

## [](#log-handling)Log Handling

Couchbase Capella maintains a centralized log management system for the collection, storage, and analysis of log data. Logs include both infrastructure and Couchbase logs, and are used for health monitoring, troubleshooting, and security purposes.

Internal alerts are configured on clusters to notify Couchbase Capella Support staff of any operational concerns. When you open a support ticket, or when an internal alert is created for the cluster, a full log collection is automatically triggered. These logs are copied over from your cloud storage to a secure Couchbase Capella storage bucket for triage purposes. Logs are automatically purged from Couchbase’s storage after 90 days.