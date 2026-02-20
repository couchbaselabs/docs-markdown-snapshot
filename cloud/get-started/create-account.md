---
title: Create an Account and Deploy Your Free Tier Operational Cluster
description: Create an account and start managing your data with Couchbase Capella.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/get-started/pages/create-account.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:get-started:create-account.adoc[]
---

[View original HTML](/cloud/get-started/create-account.html)

# Create an Account and Deploy Your Free Tier Operational Cluster

> Create an account and start managing your data with Couchbase Capella. 

To get started with Couchbase Capella, create an account and use it to deploy a forever free tier operational cluster. This account provides you with an environment where you can explore and learn about Capella with no time constraint.

With a perpetual offering, you have the freedom to work with your active free tier operational cluster at your own pace and try out the Couchbase Capella software.

With an active and working free tier operational cluster, there is no pressure of expiration dates or incurring additional costs.

> [!NOTE]
> You cannot deploy a free tier cluster in Capella Analytics. This free tier offering is only available in Capella Operational.

## [](#sign-up-free-tier)Create an Account

To create an account, go to the [Couchbase Capella Sign-up page](https://cloud.couchbase.com/sign-up) and choose one of the following sign-up options:

* Email Address
* GitHub Account
* Google Account

Procedure

1. Enter the following information:

  * Your **Full Name**
  * Your **Email Address**
  * A **Password** that contains:

    * At least eight characters
    * Uppercase characters (A-Z)
    * Lowercase characters (a-z)
    * Numbers (0-9)
    * Special characters, such as @, #, or $
2. Click **Get Started**. Couchbase sends an email to the email address you provided with a confirmation code for your account.
3. Enter the confirmation code into the provided field.
4. Review and agree to the [Terms of Service](https://www.couchbase.com/capella-terms) and the [Privacy Policy](https://www.couchbase.com/privacy-policy).
5. (Optional) Subscribe to offers, products, and services from Couchbase.
6. Click **Create Account**.

Prerequisites

* In GitHub, make sure that your primary email address is [verified](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/verifying-your-email-address).
* In GitHub, make sure your primary email address is public.  
To set a public GitHub email address:

  1. Log into GitHub, and on your profile menu, click **Settings**.  
  Your Public profile page should display.
  2. In the navigation pane, click **Emails**.
  3. Clear **Keep my email addresses private**.
  4. Return to the **Public Profile** page and select your primary email address from the **Public email** list.

    1. Click **Update profile** to save the changes.

Procedure

1. Click **GitHub**.
2. Follow the GitHub prompts to sign in to your GitHub account.
3. Review and agree to the [Terms of Service](https://www.couchbase.com/capella-terms) and the [Privacy Policy](https://www.couchbase.com/privacy-policy).
4. (Optional) Subscribe to offers, products, and services from Couchbase.
5. Click **Create Account**.

Prerequisites

* If your Google account uses a non-Google email, make sure that your account is [verified](https://support.google.com/accounts/answer/63950?sjid=12585803331733388295-NA).

Procedure

1. Click **Google**.
2. Follow the Google prompts to sign in to your Google Account.
3. Review and agree to the [Terms of Service](https://www.couchbase.com/capella-terms) and the [Privacy Policy](https://www.couchbase.com/privacy-policy).
4. (Optional) Subscribe to offers, products, and services from Couchbase.
5. Click **Create Account**.

> [!NOTE]
> For 30-day Capella free trial users:
> 
> * If your free trial account has not yet expired, your account is automatically converted to the free tier plan after your 30-day trial period if over. To deploy a free tier operational cluster, go to **Operational** and [create and deploy your free tier operational cluster](#getting-started).
> * If your free trial account has already expired, log in to your account and click **Activate Free Tier**. Proceed to deploy a free tier operational cluster or [upgrade to a paid plan](#upgrade-to-paid-account) to continue using Capella operational.

## [](#choose-your-setup-method)Choose Your Setup Method

Couchbase Capella offers two ways to deploy your free tier operational cluster:

1. [Guided Setup](#guided-setup) \- Recommended for new users with step-by-step guidance and sample data.
2. [Getting Started](#getting-started) \- For users who prefer to configure settings manually.

## [](#guided-setup)Get Started with Guided Setup

If you’re new to Capella and want to see how operational clusters work with App Services, Capella provides an interactive guided setup that provisions both infrastructure types with sample data.

The guided setup creates:

* A free tier operational cluster with sample data.
* App Services infrastructure.
* A working demonstration of both services integrated together.

Follow the guided setup:

1. Go to **App Services**.
2. Click **Start Guided Setup**.
3. Click **Create Free Tier Operational Cluster** to deploy a cluster.
4. Select **Import sample data** into the cluster.
5. Click **Create App Service** to proceed to the App Services page. In the **Create App Services** page:
6. Add an **App Service User Name** and **App Endpoint Name**.
7. In the **App User Credentials** section, enter a username and password for the App Service.
8. Click **Create App Service**. On the **Guided Setup** page, click **Connect** to finish your setup.

After completing the guided setup, you can connect your App Endpoint to your application. For more information about connecting mobile applications, see [Connect App Services Endpoint](../../app-services/get-started/configuring-app-services.md#access-endpoint).

> [!NOTE]
> The guided setup creates a cluster with pre-configured travel-sample data and optimized settings for new users. If you prefer to set up a cluster manually or import your own data, see [Create and Deploy Your Free Tier Operational cluster](#getting-started).

## [](#getting-started)Create and Deploy Your Free Tier Operational cluster

After you create your account, Couchbase creates your organization and sets a default project labeled **My First Project**.

> [!NOTE]
> Only 1 free tier operational cluster is available per organization and it automatically turns off after 72 hours of inactivity. For more information, see [Turn Operational Cluster On and Off](#turn-cluster-on-off).

Create and deploy your first operational cluster:

1. Click **Create Cluster**.
2. Select **My First Project** as the project for your cluster.
3. Under **Cluster Option**, select **Free**.
4. In the **Name** field, enter a name for your cluster or accept the default option.
5. (Optional) Provide a description of your cluster.
6. Select one of the available cloud service providers:

  * [AWS](../reference/aws.md)
  * [Google Cloud](../reference/gcp.md)
  * [Azure](../reference/azure.md)
7. Select an available geographic region for your cluster.
8. Enter a **CIDR Block** for your cluster, or accept the default. For more information about how to configure a CIDR block, see [Cloud Service Provider, Region, and CIDR Block](../clusters/databases.md#cloud-provider).
9. Click **Create Cluster** to deploy your free tier operational cluster with Capella.

> [!NOTE]
> Accounts with a paid plan can deploy a free tier operational cluster alongside their paid operational clusters.

### [](#turn-cluster-on-off)Turn Your Operational Cluster On and Off

If there’s no activity in your free tier operational cluster for more than 72 hours, Couchbase turns off the cluster and any linked App Services. This removes the cluster’s compute resources, but preserves it’s data and state. This also removes any linked App Service nodes and associated infrastructure, but preserves the state.

You can also turn off your free tier operational cluster using the UI:

1. In the **Operational** tab, find your free tier cluster:

  1. Click **︙**.
  2. Click **Turn Off**
2. Confirm the cluster turn off request:

  1. In the confirmation field, type `yes`.
  2. Click **Yes, Proceed** to turn off your cluster.

To turn your free tier operational cluster back on, go to **Operational** **Home** and click **Turn On Cluster**.

When you resume activity in your operational cluster, any linked App Services are also turned back on. If you’re unable to resume activity in your cluster, [contact Couchbase support](https://www.couchbase.com/contact/).

To create or turn on an operational cluster, you must have the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) or [Project Creator](../organizations/organization-user-roles.md#organization-role-project-creator) role.

### [](#monitor-your-free-tier-operational-cluster)Monitor Your Free Tier Operational Cluster

You can monitor your free tier operational cluster in Capella using the built-in Monitoring Dashboards. These tools help you identify performance issues and analyze runtime outliers. You can adjust the metric timeframes and resolutions according to your monitoring needs.

To view your monitoring dashboards, go to **Monitoring** and select 1 of the dashboards:

* Cluster Overview
* Workload Monitoring

  * Data Service
  * Index Service
  * Query Service
  * Node Overview
* Metrics Explorer

For more information, see [View Monitoring Dashboards](../clusters/monitoring/metrics-dashboard.md).

> [!NOTE]
> The Health Advisor dashboard is not available for free tier operational clusters. [Upgrade](../billing/upgrade-account.md) to a \*Developer Pro or Enterprise plan to get expert advice on your cluster.

### [](#delete-your-free-tier-operational-cluster)Delete Your Free Tier Operational Cluster

If there’s no activity in your free tier operational cluster for more than 30 days, Couchbase deletes the operational cluster and any linked App Services. Couchbase sends periodic emails after 72 hours of inactivity warning you that your free tier cluster is turned off and will delete after 30 days.

To recreate your free tier operational cluster, see [create and deploy your free tier operational cluster](#getting-started).

## [](#app-services)Deploy Capella Free Tier App Services

You can use Capella App Services to:

* Sync your data between Capella operational buckets and mobile or edge devices running [Couchbase Lite](../../couchbase-lite/current/index.md).
* Authenticate and manage mobile and edge users

To deploy free tier App Services for mobile development:

1. In the **App Services** tab, click **Create App Service**.
2. Enter a name for your App Service.
3. Select your free tier operational cluster to link to your App Service.
4. Click **Create App Service**.

> [!NOTE]
> Your free tier App Service automatically links to your free tier operational cluster.

For more information about how to configure App Services, see [Configure Your Free Tier App Services (Mobile sync)](../../app-services/get-started/configuring-app-services.md).

## [](#upgrade-to-paid-account)Upgrade to a Paid Account

You need to [add an activation ID](../billing/upgrade-account.md#add-activation-id) to upgrade to a paid Support plan and gain access to all the Capella operational features. For more information about the available Support Plans for Couchbase Capella, see [About Cluster and Service Support Plans](../billing/billing.md#paid-plan).

Free tier operational clusters do not automatically migrate to paid operational clusters after an the upgrade. Capella allows only one free tier operational cluster per organization at any time.

> [!WARNING]
> When upgrading from a free tier plan to a paid Support plan, Couchbase deletes your existing free tier operational cluster.

When you upgrade to a paid Support plan, you can choose to deploy another free tier operational cluster alongside your provisioned operational cluster. To back up and transfer your data from your existing free tier operational cluster to a new free tier or paid operational cluster, you must use the `cbbackupmgr` tool.

For more information about using the `cbbackupmgr` tool, see [Backup a Free Tier Capella Operational Cluster](../clusters/cli-backup-restore.md#backup-free-cluster).

## [](#free-tier-plan-features)Free Tier Plan Features

For more information, use the Capella UI to learn more about the free tier features and compare to other Couchbase Capella plans:

1. In the **Operational** tab, choose your operational cluster to go to your cluster’s page.
2. Click the **Settings** tab.
3. In the navigation menu, click **Plan**.
4. Select, compare and review your Couchbase Capella plan.

## [](#next-steps)Next Steps

After you create an account and deploy an operational cluster, you can:

* [Configure Your Free Tier App Services (Mobile sync)](../../app-services/get-started/configuring-app-services.md)
* [Run your first query](run-first-queries.md)
* [Try out Couchbase SDKs](sdk-playground.md)
* [Import your own data](../clusters/data-service/import-data-documents.md)