---
title: Upgrade Your Account
description: Add an Activation ID or a credit card to upgrade from a free tier
  plan and access all Couchbase Capella features for your operational clusters.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/billing/pages/upgrade-account.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:billing:upgrade-account.adoc[]
---

[View original HTML](/cloud/billing/upgrade-account.html)

# Upgrade Your Account

> Add an Activation ID or a credit card to upgrade from a free tier plan and access all Couchbase Capella features for your operational clusters. 

To upgrade from a free tier plan to a paid Support plan in Capella, you need to either:

* [Use an Activation ID from Couchbase Sales](#use-activation-id).
* [Add a credit card to your organization](#add-credit-card).

You must keep a valid credit card on your account or use an Activation ID to keep using a paid Support Plan and other paid features.

> [!TIP]
> You can switch from credit card payments to purchasing credits through Couchbase Sales with an Activation ID at any time. You cannot switch your organization to credit card payments after you add an Activation ID to your account.

You can also go to one of the Capella Cloud Service Provider marketplaces to purchase credits and start using paid Support Plans without an Activation ID or adding a credit card to Capella:

* [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-xrhx5zgue5c26)
* [GCP Marketplace](https://console.cloud.google.com/marketplace/product/couchbase-public/couchbase-capella-database-as-a-service?pli=1)
* [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/couchbase.couchbase%5Fcapella%5Fdbaas?tab=overview)

For more information about the available Support Plans for Couchbase Capella, see [About Cluster and Service Support Plans](billing.md#paid-plan).

## [](#prerequisites)Prerequisites

* To upgrade your organization to a paid Support Plan, you must have the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) role.

## [](#use-activation-id)Use an Activation ID from Couchbase Sales

You can upgrade your account by [getting an Activation ID from Couchbase Sales](#get-activation-id) and [adding that Activation ID to your organization](#add-activation-id).

When you add an Activation ID, you can create clusters with any Support Plan, based on the credits you add to your organization. For more information, see [About Cluster and Service Support Plans](billing.md#support-plans).

### [](#get-activation-id)Get an Activation ID

To contact Couchbase Sales:

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **Settings** **Upgrade**.
3. Click **Contact Sales**.
4. In the **Contact Us** form, enter the following information:

  1. Your **First Name**.
  2. Your **Last Name**.
  3. Your **Email Address**.
  4. Your **Company Name**.
  5. Your **Preferred method of contact**.
  6. Your Activation ID request.
5. Click **Submit**.

### [](#add-activation-id)Add an Activation ID

When you add an Activation ID, the **Payment** and **Usage** pages show your billing information based on your [payment plan](billing.md#payment-options).

To add an Activation ID to your organization:

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **Settings** **Upgrade**.
3. In the **Activation ID** field, enter your Activation ID from Couchbase Sales.
4. Click **Upgrade My Account**.

## [](#add-credit-card)Add a Credit Card

When you add a credit card to your organization, you can create clusters with the **Basic** or **Developer Pro** Support Plans in your organization. If you want to create a cluster with the **Enterprise** Support Plan, you must get an Activation ID and purchase Capella Credits. For more information, see [About Cluster and Service Support Plans](billing.md#support-plans).

To add a credit card to your organization:

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **Settings** **Upgrade**.
3. Click **Add Credit Card**.
4. Enter the details for the credit card you want to use for your Capella usage.
5. Click **Upgrade Account**.
6. Confirm that you want to upgrade your account and click **Upgrade**.  
If you have already deployed a free tier cluster, your current free tier cluster will be deleted.

## [](#transition-from-free)Transitioning from a Free Tier Plan

Capella allows only one free tier operational cluster per organization at any time.

> [!WARNING]
> When you upgrade to a paid Support Plan, Couchbase deletes your old free tier operational cluster.

With your paid plan, you can choose to deploy another free tier operational cluster alongside your paid operational clusters.

To back up and transfer your data from the old free tier operational cluster to a new free tier or paid operational cluster, you must use the `cbbackupmgr` tool. For more information about using the `cbbackupmgr` tool, see [Backup a Free Tier Capella Operational Cluster](../clusters/cli-backup-restore.md#backup-free-cluster).

## [](#next-steps)Next Steps

* If you need to purchase [Couchbase Capella Credits](billing.md#direct-invoice) for your organization, contact [Couchbase Sales](https://info.couchbase.com/Capella-Contact.html). You must have a credit balance in your account before you can deploy a cluster.
* If you still need to deploy a cluster, see [Create A Paid Cluster](../clusters/create-database.md).