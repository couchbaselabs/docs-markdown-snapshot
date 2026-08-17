---
title: Change a Cluster&#8217;s Plan and Support Timezone
description: You can change the Support Plan for your Couchbase Capella clusters
  and their support timezones at any time.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/billing/pages/change-support-plan.adoc
  xref: xref:cloud:billing:change-support-plan.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/billing/change-support-plan.html)

# Change a Cluster&#8217;s Plan and Support Timezone

> You can change the Support Plan for your Couchbase Capella clusters and their support timezones at any time. 

Change a cluster's [Support Plan](billing.md#support-plans) to change its support level and capabilities.

Change its support timezone to change when you can receive support for any issues with your Capella clusters.

## [](#prerequisites)Prerequisites

* You must have the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) role.

## [](#change-a-cluster-support-plan)Change a Cluster Support Plan

To change a cluster Support Plan:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to make changes to your Support Plan.
3. Go to **Settings** **Plan**.
4. Select the Support Plan you want for your cluster.  
For more information about the available Support Plans for Couchbase Capella, see [Plans and Pricing](https://www.couchbase.com/pricing) on the Couchbase website.  
> [!NOTE]  
> If you pay for your Capella usage with [pre-paid credits](billing.md#pre-paid-credits) and you choose a Support Plan that has no available pre-paid credit balance, Capella warns you that you'll incur [pay-as-you-go usage](billing.md#pay-as-you-go-credits) for that plan. If your chosen Support Plan has a [low pre-paid credit balance](billing.md#low-credits) and could incur pay-as-you-go charges within the first month of running your cluster, Capella also shows a warning.
5. Click **Save**.

Your plan changes take effect on the next clock hour.

## [](#change-a-clusters-support-timezone)Change a Cluster's Support Timezone

To change a cluster's support timezone:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to make changes to your support timezone.
3. Go to **Settings** **Plan**.
4. In the **Support Time Zone** list, select an available support timezone.
5. Click **Save**.

Your support timezone changes take effect on the next clock hour.