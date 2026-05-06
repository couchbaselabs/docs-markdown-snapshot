---
title: View Capella Usage and Invoices
description: You can view current and past usage for the clusters and services
  in your organization, and view and download invoices.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/billing/pages/usage-invoices.adoc
pubDate: 2026-05-06T05:34:55.761Z
link: xref:cloud:billing:usage-invoices.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/billing/usage-invoices.html)

# View Capella Usage and Invoices

> You can view current and past usage for the clusters and services in your organization, and view and download invoices. 

From your organization's **Billing** tab, you can:

* [Access Your Usage Overview](#access-billing)
* [View and Filter Usage Reports](#filter-usage)

To retrieve billing information for your organization through the Management REST API, use the [Billing API](../management-api-reference/index.md#tag/Billing).

## [](#prerequisites)Prerequisites

* You have the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner), [Project Creator](../organizations/organization-user-roles.md#organization-role-project-creator), or [Organization Member](../organizations/organization-user-roles.md#organization-role-organization-member) role.

## [](#access-billing)Access Your Usage Overview

To get an overview of your monthly cluster and service usage, go to **Billing** **Overview**.

> [!NOTE]
> Data refresh periods
> 
> Usage data can take up to 5 days to appear in your billing overview and reports.

The **Overview** page lets you:

* Compare your organization's credit usage between now and the same time last month. You can also view a percentage value difference in credit usage.
* View your organization's monthly credit usage from the last year by category. Categories include App Services, Analytics, Data Transfer, and Cluster.
* Buy Capella credits through [Couchbase Sales](https://info.couchbase.com/Capella-Contact.html), [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-xrhx5zgue5c26), [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/couchbase.couchbase%5Fcapella%5Fdbaas?tab=overview), or [GCP Marketplace](https://console.cloud.google.com/marketplace/product/couchbase-public/couchbase-capella-database-as-a-service?pli=1).
* View your organization's [pay-as-you-go credit usage](billing.md#pay-as-you-go-credits) information for your last 3 months of usage. Capella displays your usage across your organization's Basic, Developer Pro, and Enterprise Support Plans.

## [](#filter-usage)View and Filter Usage Reports

To view and filter your organization's usage reports, from the navigation breadcrumbs in the Capella UI, click your organization name and go to **Billing** **Usage Reporting**.

You can use the following filters with the usage graph:

* **Date Range**: Pick an available date range or set a custom date range.
* **Category**: Choose all available categories, or choose specific categories of usage data.
* **Project**: Choose all available projects, or choose specific projects by name.
* **Cluster**: Choose all available clusters, or choose specific clusters by name.
* **Analytics**: Choose all available Analytics clusters, or choose specific Analytics clusters by name.
* **App Service**: Choose all available App Services, or choose specific App Services by name.

The **Summary by Category** section shows the usage percentage of different categories. The usage graph and the **Summary by Category** section updates based on the filters you select.

## [](#next-steps)Next Steps

You can [create billing alerts](manage-billing-alerts.md) to monitor usage in your organization.

If you added a credit card to your organization, Capella automatically creates alerts for:

* Processed payments
* Declined payments
* High usage
* Your default credit card expiring

You can also [Manage Billing Information](manage-billing.md).