---
title: Manage Your Billing
description: Couchbase Capella bills you for the size and number of operational
  clusters in your organization.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/billing/pages/billing.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:cloud:billing:billing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/billing/billing.html)

# Manage Your Billing

> Couchbase Capella bills you for the size and number of operational clusters in your organization. 

All billing in Capella takes place at the organization level. Your billing settings apply to all projects and operational clusters in your organization.

To configure billing settings for your organization, you must have the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) role.

## [](#paid-plan)About Cluster and Service Support Plans

Billing for your organization is based on the chosen [Support Plan](#paid-plan) for your clusters or services:

* [Free Tier Plan](#free)
* [Basic Support Plan](#basic)
* [Developer Pro Support Plan](#dev-pro)
* [Enterprise Plan](#enterprise)

You can change the Support Plan for your cluster at any time. For more information about changing your cluster's plan, see [Change a Cluster's Plan and Support Timezone](change-support-plan.md).

For more information and a comparison of the available Support Plans, see [Plans and Pricing](https://www.couchbase.com/pricing/) and the [Capella Support Policy](https://couchbase.com/support-policy/cloud) on the Couchbase website.

### [](#free)Free Tier Plan

Clusters and services on the Free plan are always free and available, as long as you're actively using them. You do not need to have a credit balance or credit card in your organization to use the Free plan.

Each organization can use only 1 free tier cluster. You cannot change the support plan for a free tier cluster to a paid plan.

Free plan clusters are community-supported through the Couchbase forums.

### [](#basic)Basic Support Plan

Clusters and services on the Basic Plan receive technical support through the Couchbase forums. Basic clusters and services have limited capabilities, suited to development and non-mission critical production systems.

You can use the Basic plan with [credit card payments](#credit-cards), [pre-paid credits](#pre-paid-credits), or [pay-as-you-go](#pay-as-you-go-credits).

### [](#dev-pro)Developer Pro Support Plan

Clusters and services on the Developer Pro plan receive technical support through the Capella Support team, within 8 hours. Developer Pro clusters and services have more features, suited to production-ready applications and systems.

You can use the Developer Pro plan with [credit card payments](#credit-cards), [pre-paid credits](#pre-paid-credits), or [pay-as-you-go](#pay-as-you-go-credits).

### [](#enterprise)Enterprise Plan

Clusters and services on the Enterprise plan receive technical support through the Capella Support team, within 30 minutes. Enterprise clusters and services have the most features and are suited to mission-critical applications with heavy workloads.

You can use the Enterprise plan with [pre-paid credits](#pre-paid-credits), or [pay-as-you-go](#pay-as-you-go-credits).

## [](#bill-calculation)How Couchbase Calculates Your Bill

Couchbase calculates cluster charges daily.

Any hourly charges for the current day are reflected in your organization's balance on the next calendar day. Monthly usage periods for each calendar month include daily usage.

### [](#when-a-cluster-is-on)When a Cluster is On

Couchbase charges by the clock hour for Capella operational clusters. It bases this hourly rate on:

* The cloud service provider and region where the operational cluster is deployed.
* The operational cluster size, determined by:

  * Number of nodes
  * Number of vCPUs
  * Amount of RAM
  * GiB of disk storage
  * Disk IOPS and throughput (AWS and Azure Ultra Disk only)
* The operational cluster [Support Plan](#support-plans).

Your operational cluster becomes billable after it successfully deploys and is in a running state. You're billed for each clock hour that your operational cluster runs. For example, if your operational cluster ran at 10:30 a.m. and was turned off or deleted at 11:30 a.m. on the same day, you're billed for 2 **on** hours because the operational cluster ran during 2 clock hours.

You can [change a clusters size](../clusters/scale-database.md) or [change its Support Plan](change-support-plan.md) after its deployment. The hourly rate for that operational cluster increases or decreases based on your changes.

### [](#when-a-cluster-is-off)When a Cluster is Off

For each clock hour where a Capella operational cluster is off, the hourly rate for an operational cluster is based on:

* The cloud service provider and region where the operational cluster is deployed.
* The operational cluster size, determined by:

  * Number of nodes
  * GiB of disk storage
  * Disk IOPS and throughput (AWS and Azure Ultra Disk only)

For example, if your operational cluster ran at 10:30 a.m., was turned off at 11:30 a.m., and deleted at 1:30 p.m., you would be billed for 2 **on** clock hours and 2 **off** clock hours.

### [](#app-services)App Services

For more information about billing for App Services, see [Billing](../../app-services/billing/billing.md).

### [](#bucket-backups)Bucket Backups

Every clock hour, Capella measures the GiB amount of backup object storage consumed by each operational cluster.

The GiB size of a backup volume is converted into an hourly volume, and multiplied by a $ per GiB rate. This rate varies by region and cloud service provider.

For more information about bucket backups, see [Back Up and Restore Bucket Data](../clusters/backup-restore.md).

### [](#cluster-backups)Cluster Backups

Every day, Capella measures the amount of snapshot storage consumed by each operational cluster. This is multiplied by a $ amount per GiB to calculate total cluster backup credits.

This rate varies by region and cloud service provider.

For more information about storage and size calculations for cluster backups, see [Backup Types](../clusters/cloud-snapshots.md#backup-types).

### [](#data-transfer-charges)Data Transfer Charges

AWS, GCP, and Azure all charge variable rates for data moved between and out of their services.

Capella passes through the cost of data transfer charges, based on the GiB amount and type of data transfer, for each operational cluster. Data transfer charges are in addition to any charges you may receive from a cloud service provider for connecting to Capella services.

Cloud service providers typically charge for the following data transfer types:

| Type                       | Description                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inter-Zone or Intra-Region | Charged for traffic crossing Availability Zones, VPC Peering Connections, or public IP addresses within the same region. In AWS and GCP, these charges are commonly .01 credit per GB, for both ingress and egress. In Azure, this is free of charge, except for VNET peering. These are the most common data transfer charges you'll incur for using Capella.                                                   |
| Inter Region               | Charges for instance traffic crossing regions, within the same cloud service provider. Inter-region traffic rates are specific to both the source regions, or where the data is moving out of, and the destination region, or where the data is moving to. Charges range from .01 credits/GB (between AWS us-east-1 and us-east-2) to .16 credits/GB (between Azure South America regions and other continents). |
| Internet                   | Data transferred out to the Internet, including data transferred to other Infrastructure as a Service (IaaS) providers. These charges are typical .09 credits/GB in North American and European regions, with higher rates in Asia Pacific.                                                                                                                                                                      |

The following data transfers are free of charge:

* Data import into Capella.
* Data transferred between instances in the same Availability Zone.

### [](#private-endpoints)Private Endpoints

If you choose to connect to Capella through [Private Endpoints](../security/private-endpoints.md), Couchbase provisions a single load balancer per operational cluster that enables that connection.

You'll be charged for Private Endpoints based on the following costs:

* A fixed hourly connection cost, with an hourly rate that varies based on the region where the load balancer is deployed. Charges are for each clock hour that the Private Endpoint service is provisioned, regardless of usage or the state of your operational cluster (on or off).
* A per GiB data processing charge for data processed through the load balancer, with a per GiB rate that varies based on the region where the Private Endpoint service is used.

These charges are in addition to any Private Endpoint costs from AWS or Azure for the use of AWS PrivateLink or Azure Private Link.

### [](#data-api)Data API

If you connect to Capella through the [Data API](../data-api-guide/data-api-intro.md), Couchbase provisions a single load balancer per operational cluster to enable that connection.

You'll be charged for Data API access based on the following costs:

* A fixed hourly connection cost, with an hourly rate that varies based on the region where the load balancer is deployed. Charges are for each clock hour that the Data API is enabled, regardless of usage or the state of your operational cluster (on or off).
* A per GiB data processing charge for data processed through the load balancer, with a per GiB rate that varies based on the region where the Data API is used.

> [!IMPORTANT]
> When [VPC Peering](../clouds/private-network.md) support is enabled for the Data API, you'll be charged an incremental extra cost for Data API access, regardless of whether any VPC Peering connections are currently established.
> 
> Enabling private endpoint support with the Data API has no additional cost beyond the regular charges associated with the Data API.

### [](#couchbase-ai-data-plane)Couchbase AI Data Plane

For the AI Data Plane, Couchbase charges you for your usage of the following services:

* [Workflows](#ai:build:data-processing.adoc):

  * [Vectorizing Unstructured Data from External sources](#ai:build:vectorize-unstructured-data.adoc)
  * [Vectorizing Structured Data from External sources](#ai:build:vectorize-structured-data-s3.adoc)
  * [Vectorizing Structured Data from Capella](#build:vectorize-structured-data-capella.adoc)
* The Model Service:

  * [Deploying and using an embedding model](../../ai/build/model-service/deploy-embed-model.md)
  * [Deploying and using an LLM](../../ai/build/model-service/deploy-llm-model.md)

For a limited time, your [AI Functions](../../ai/build/ai-functions.md) usage is free of charge.

#### [](#workflows)Workflows

Couchbase charges you depending on the type of data you upload into your AI Data Plane [Workflows](#ai:build:data-processing.adoc):

| Workflow Type                                                                         | Billing Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Unstructured Data from External sources](#ai:build:vectorize-unstructured-data.adoc) | Capella measures the number of pages processed when you load unstructured data from external sources, such as PDF, JPG, PNG, DOC, or DOCX files, into Capella operational clusters. Each day, Capella totals the number of pages processed and multiplies that by a specific Capella credit amount per 1,000 pages to calculate the total number of Unstructured Data Workflow credits. The credit amount per 1,000 pages varies by region and cloud service provider (CSP) where the linked cluster is deployed. For document types where a page is not applicable, Couchbase applies a conversion factor of 100 KiB per 1 page. |
| [Structured Data from External sources](#ai:build:vectorize-structured-data-s3.adoc)  | Capella measures the number of GiB processed when you load structured data from external sources, such as JSON files from S3, into Capella operational clusters. Every day, Capella totals the number of GiB processed and multiplies that by a specific Capella credit amount per GiB to calculate the total number of structured workflow credits. The credit amount per GiB varies by region and cloud service provider (CSP) where the linked cluster is deployed.                                                                                                                                                            |
| [Data from Capella](#build:vectorize-structured-data-capella.adoc)                    | Couchbase does not charge you when you load structured data from a Capella operational cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

#### [](#model-service)Model Service

Couchbase charges by the clock hour for the Model Service. It bases this hourly rate on:

* The cloud service provider (CSP) and region where your model is deployed.
* The model compute size, determined by:

  * Number of GPUs
  * Number of vCPUs
  * Amount of RAM
* Whether your model is On or Off.

The Model Service only becomes billable once a Capella hosted model deploys and is in a running state.

> [!IMPORTANT]
> Billing for the Model Service follows the [Enterprise Plan pricing](https://www.couchbase.com/pricing). If your account uses a different plan, Couchbase bills your Model Service usage with Enterprise [On-Demand credits](#pay-as-you-go-credits).

Integrated LLM Cache

If you enable any of the following **Value Adds** when [deploying your Capella-hosted models](../../ai/build/model-service/deploy-llm-model.md#procedure), Couchbase charges an additional fixed hourly cache fee on top of your regular Model Service costs:

* [Caching](../../ai/get-started/intro.md#llm-caching)
* [Async Processing](#ai:build:model-service:configure-embed-performance.adoc#async-processing)

This integrated cache fee is per tenant per region, and applies for every cloud service provider (CSP) region which has at least 1 model with these **Value Adds** enabled. For example, Couchbase bills 2 models that have caching enabled in AWS regions `us-east-1` and `us-west-2` an additional 1 credit per hour, which is 0.5 credit per hour for each region.

Couchbase bills the integrated cache fee according to the [Enterprise Plan](#enterprise) rates and pricing.

#### [](#ai-functions)AI Functions

As a limited time promotional offer, Couchbase does not charge you for [AI Functions](../../ai/build/ai-functions.md) as a stand-alone service.

## [](#billing-system)Billing System

Couchbase Capella bills you for your operational cluster usage with a credit-based system. For every resource you consume, Capella bills you in credits. You can choose between 2 different kinds of credits:

* [Pre-paid credits](#pre-paid-credits)
* [Pay-as-you-go or on-demand credits](#pay-as-you-go-credits)

Every Couchbase Capella [Support Plan](#support-plans) has different pricing and rates for these credits. For more information, see [Capella Plans and Pricing](https://www.couchbase.com/pricing).

> [!NOTE]
> If you [deploy a new paid operational cluster](../clusters/create-database.md) that does not have a credit balance for your chosen [Support Plan](#support-plans), Capella automatically bills you under the pay-as-you-go system. Capella will [warn you before you deploy a new cluster if you choose a Support Plan that could incur pay-as-you-go charges](#low-credits) within your first 30 days of usage.

### [](#pre-paid-credits)Pre-Paid (Up-Front) Credits

With pre-paid credits, you purchase a set number of credits upfront, which are then used over time to cover your cluster usage based on resource consumption. Capella automatically draws from your available credit balance for your cluster usage. You can monitor your remaining credits and purchase more at any time.

Capella displays the available pre-paid credit balance you have for each [Support Plan](#support-plans) when you [deploy a new paid operational cluster](../clusters/create-database.md).

You can buy pre-paid credits through [the Couchbase Sales team with a direct invoice](#direct-invoice) or your [cloud service provider (CSP)](#marketplaces).

### [](#low-credits)Low Credit Warning Calculations

To help with managing costs and getting the best use out of your prepaid credits, Capella tries to estimate your credit usage for new clusters. Capella displays warnings when you [create a new cluster](../clusters/create-database.md) or [change a cluster's Support Plan](change-support-plan.md), if your projected credit usage would be greater than your available prepaid credit balance and cause pay-as-you-go charges.

Capella looks at your credit usage from the last 7-30 days to project how long credits for a new cluster will last, based on an average daily credit burn rate, and the fixed costs for a new cluster.

If your projected usage will consume all of your available pre-paid credits in the next 30 days, Capella warns you that you do not have enough credits to avoid pay-as-you-go charges.

You can still choose to deploy a cluster and accrue pay-as-you-go charges.

If you do not have at least 7 days of usage data for a cluster, Capella does not show any low credit warnings for new clusters.

### [](#pay-as-you-go-credits)Pay-As-You-Go (On-Demand) Credits

With pay-as-you-go credits, you're billed for your real-time cluster usage. Couchbase calculates the number of credits your clusters and resources have consumed periodically and bills for your consumption during that time.

You can choose to pay for pay-as-you-go credits through [the Couchbase Sales team with a direct invoice](#direct-invoice), your [CSP](#marketplaces), or by [credit card](#credit-cards).

## [](#payment-options)Payment Options

Your payment options and final usage calculations depend on how you want to pay for your Capella usage:

* [Direct Invoice from Couchbase Sales](#direct-invoice)
* [CSP Marketplaces](#marketplaces)
* [Credit Card Payments](#credit-cards)

### [](#direct-invoice)Direct Invoice from Couchbase Sales

You can choose to pay for your Couchbase Capella usage through a monthly direct invoice. Your monthly usage periods are used for reporting and billing purposes. Your credit balance updates once every calendar day and reflects the previous day's cumulative usage across all operational clusters in your organization.

For [pre-paid credits](#pre-paid-credits), you can choose to purchase credits ahead of time to pay for your Capella usage through a contract with Couchbase Sales. If you use more than your pre-purchased credit balance during a calendar month, you'll be billed through Capella's pay-as-you-go system for the additional usage. You must pay this bill in arrears.

For [pay-as-you-go](#pay-as-you-go-credits), you can choose to pay for those credits through a monthly invoice from Couchbase Capella.

> [!NOTE]
> If you currently pay for your usage with a [credit card](#credit-cards), you can switch to the direct invoice payment method at any time. After you have switched to paying for your credits with a sales agreement, you cannot switch back to credit card payments.

To enable credit purchases for your organization, you must add an [Activation ID](#billing/upgrade-account.adoc) to your account. Contact [Couchbase Sales](https://info.couchbase.com/Capella-Contact.html) to get an Activation ID and start using paid operational clusters through the direct invoice payment option.

Your credits expire if they're not used within 12 months.

Your organization's billing contact receives an invoice for the purchased credits based on the currency equivalent outlined in your purchase agreement.

### [](#marketplaces)CSP Marketplaces

You can choose to pay for your usage through your CSP. Go through 1 of Capella's cloud service provider (CSP) marketplaces to get started with paying for your [credits](#billing-system). You'll receive an invoice through your CSP for your previous month's usage on Capella.

All invoices and payments are managed through your CSP's account.

To pay for your credits with your cloud service provider, go to:

* [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-xrhx5zgue5c26)
* [GCP Marketplace](https://console.cloud.google.com/marketplace/product/couchbase-public/couchbase-capella-database-as-a-service?pli=1)
* [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/couchbase.couchbase%5Fcapella%5Fdbaas?tab=overview)

For [pre-paid credits](#pre-paid-credits), you can choose to purchase preset credit packages through your CSP to pay for your Capella usage. If you use more than your pre-purchased credit balance during a calendar month, you'll be billed through Capella's pay-as-you-go system for the additional usage, through your CSP. You must pay this bill in arrears.

For [pay-as-you-go](#pay-as-you-go-credits), you can choose to pay for those credits through a monthly invoice managed by your CSP.

After you purchase credits through your CSP, you must add an [Activation ID](#billing/upgrade-account.adoc) to your account to start using paid operational clusters.

> [!NOTE]
> If you currently pay for your usage with a [credit card](#credit-cards), you can switch to the CSP payment method at any time. After you have switched to paying credits with your CSP, you cannot switch back to credit card payments through Capella.

### [](#credit-cards)Credit Card Payments

You can choose to add a credit card to your organization to get billed directly for your Capella usage, instead of purchasing [pre-paid credits](#pre-paid-credits) through [Couchbase Sales](#direct-invoice) or a supported [cloud provider's marketplace](#marketplaces). Couchbase bills your credit card for any usage in the previous calendar month, similar to [pay-as-you-go credits](#pay-as-you-go-credits).

If you choose to pay for your Capella usage through a credit card, you can deploy clusters and services on a [Basic](#basic) or [Developer Pro](#dev-pro) Support Plan.

> [!TIP]
> You can switch your payment method from credit card billing to a contract with [Couchbase Sales](https://info.couchbase.com/Capella-Contact.html) at any time. You must have a contract to deploy clusters and services on the [Enterprise](#enterprise) Support Plan.

All usage charges are billed in USD ($). All payments are automatic.

#### [](#managing-credit-cards)Managing Credit Cards

You can add up to 5 credit cards to your organization as saved credit cards. The first card you add to your organization is marked as your default card. You can [change your default credit card at any time](manage-billing.md#update-default-cc).

Couchbase will only charge the credit card marked as the default in your organization.

If the card set as the default in your organization is close to its expiry date, Capella sends reminder emails to update your credit card details. Emails are sent 30 days, 7 days, and 1 day before your default credit card expires.

If your default credit card expires and payment cannot be processed, you might lose access to your paid clusters and services. For more information about how to update a saved credit card, see [Edit a Saved Credit Card](manage-billing.md#edit-saved-cc).

If you need to dispute a charge or have any questions related to credit card billing, [create a support ticket](../support/manage-support.md) with the **Billing** category.

#### [](#credit-card-payment-schedule)Credit Card Payment Schedule

The default credit card in your organization will be charged on the seventh day of every month, based on your previous month's usage.

If your payment fails to process, Couchbase tries to bill your default credit card again for 3 days. If by the fourteenth day of the month, Couchbase still has not processed a payment on your default credit card, all paid services and clusters in your organization are paused.

If no payment is received by the end of the calendar month after you incurred usage charges on Capella, all services and clusters will be deleted from your organization.

## [](#see-also)See Also

* [Manage Billing Information](manage-billing.md)
* [Manage Billing Alerts](manage-billing-alerts.md)
* [View Capella Usage and Invoices](usage-invoices.md)
* [Upgrade Your Account](upgrade-account.md)
* [Change a Cluster's Plan and Support Timezone](change-support-plan.md)
* [Request Prompt Action for Cluster Recovery](support-pre-auth.md)