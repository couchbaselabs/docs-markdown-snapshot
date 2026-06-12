---
title: Configure Capella iQ
description: Capella iQ harnesses the power of a third-party large language
  model (LLM) to improve your queries. You can turn this tool on or off for your
  organization.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/get-started/pages/capella-iq/configure-capellaiq.adoc
pubDate: 2026-06-12T16:31:57.907Z
link: xref:cloud:get-started:capella-iq/configure-capellaiq.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/get-started/capella-iq/configure-capellaiq.html)

# Configure Capella iQ

> Capella iQ harnesses the power of a third-party large language model (LLM) to improve your queries. You can turn this tool on or off for your organization. 

## [](#prerequisites)Prerequisites

* You must have the [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner) role to:

  * [Accept Capella iQ's supplemental terms](#T&C).
  * [Select the model providers available to your organization](#select-org-model). You can choose either OpenAI, AWS Bedrock, or both.
  * [Turn Capella iQ on or off](#turn-iq-on-off).
* If available, you must have the [Cluster Manager](../../organizations/organization-user-roles.md#cluster-role-cluster-manager) or [Cluster Data Reader/Writer](../../organizations/organization-user-roles.md#cluster-role-cluster-data-reader-writer) role to [select a model provider for Capella iQ at the cluster level](#select-cluster-model).

## [](#T&C)Accept Capella iQ Supplemental Terms

Before anyone in an organization can use Capella iQ, an [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner) must accept the Capella Supplemental Terms. If the terms are not yet accepted, the iQ button is still visible in the query editor. If the supplemental terms have not been accepted and a user without the [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner) role clicks the iQ button, they're informed that Capella iQ is disabled. If a user with the [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner) role clicks the iQ button, they can instead review and accept the terms for the current organization.

To accept the Capella iQ supplemental terms:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Operational**.
  * Click your current project name or search for a project and go to **Operational**.
  * Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to configure Capella iQ.
3. Click **Data Tools** **Query**.
4. Click **iQ**.
5. In the prompt, review and accept the [Capella iQ Supplemental Terms](https://www.couchbase.com/capella-feature-specific-terms/).
6. Click **Continue**.  
Capella iQ is now available to all your organization's users, who can use it with all of your organization's clusters.

> [!NOTE]
> Accepting the terms for Capella iQ enables iQ for both operational clusters and [Capella Analytics clusters](../../../analytics/intro/intro.md). While iQ helps you write SQL++ queries in an operational cluster, iQ for Capella Analytics helps you write [SQL++ for Capella Analytics queries and statements](../../../analytics/sqlpp/1%5Fintro.md).

## [](#select-model-provider)Select Your Capella iQ Model Provider

Capella iQ supports 2 model providers:

* [OpenAI](https://openai.com/)
* [AWS Bedrock](https://aws.amazon.com/bedrock/)

Model provider selections made at the organization level are automatically applied at the cluster level. For example, if the [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner) enables only OpenAI, all current and new clusters would use OpenAI as their model provider.

If your organization enables both model providers, the [default model provider](work-with-capellaiq.md#model-provider) assigned to a cluster depends on the cluster's deployment location. Users can also choose which available model provider to use for a specific cluster.

> [!NOTE]
> The model provider you select in iQ also applies to [iQ Insights](explore-iq-insights.md), ensuring consistent responses across both services.

### [](#select-org-model)Select Your Organization's Capella iQ Model Provider

[Organization Owners](../../organizations/organization-user-roles.md#organization-role-organization-owner) can make 1 or both model providers (OpenAI and AWS Bedrock) available to your organization. If both providers are enabled, anyone in the organization with the [Cluster Manager](../../organizations/organization-user-roles.md#cluster-role-cluster-manager) or [Cluster Data Reader/Writer](../../organizations/organization-user-roles.md#cluster-role-cluster-data-reader-writer) role can choose their preferred model provider [at the cluster level](#select-cluster-model) directly in the Capella iQ panel.

To select the model providers for Capella iQ in your organization:

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **Settings**.
3. In **Capella iQ**, under **Model Provider**, select 1 or both of the available model providers:

  * **OpenAI**
  * **AWS Bedrock**
4. Click **Save**.  
The selected model providers are now available to all clusters in the organization.

### [](#select-cluster-model)Set Your Preferred Model Provider

If the [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner) has enabled both model providers (OpenAI and AWS Bedrock), users with the [Cluster Manager](../../organizations/organization-user-roles.md#cluster-role-cluster-manager) or [Cluster Data Reader/Writer](../../organizations/organization-user-roles.md#cluster-role-cluster-data-reader-writer) role can choose their preferred model provider directly in the Capella iQ panel for a specific cluster. If only 1 model provider is enabled at the organization level, all clusters must use that model for all iQ actions.

> [!IMPORTANT]
> Capella saves the model provider selection per user. Each user on the same cluster can have a different model provider selected. For example, 1 user can use AWS Bedrock while another uses OpenAI on the same cluster.

To select the model provider for Capella iQ at the cluster level:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Operational**.
  * Click your current project name or search for a project and go to **Operational**.
  * Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to configure Capella iQ.
3. Click **Data Tools** **Query**.
4. Click **iQ**.
5. In the iQ Chat window, select your preferred model provider for this cluster:

  * **OpenAI**
  * **AWS Bedrock**  
Capella iQ uses your selected provider for all of your subsequent queries on this cluster.

## [](#iq-on-off)Turn Capella iQ Off for Your Organization

Capella iQ is on by default and you control it at the organization level. To turn Capella iQ on or off for your organization, you need to navigate to your organization's general settings page:

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **Settings** **General**.
3. Select or deselect **Enable Capella iQ** and click **Save**.  
If Capella iQ is turned off for an organization, the iQ button is still visible in the query editor. Any user who clicks this button sees a message that Capella iQ is disabled.

> [!CAUTION]
> When you disable Capella iQ, you also disable [iQ Insights](explore-iq-insights.md).

## [](#next-steps)Next Steps

* [Get Started with Capella iQ](get-started-with-iq.md)
* [Work Faster with Capella iQ](work-with-capellaiq.md)
* [Explore iQ Insights](explore-iq-insights.md)