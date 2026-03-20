---
title: Work Faster with Capella iQ
description: Capella iQ is your partner in getting started with Couchbase
  Capella. Use it to create SQL++ queries, sample data, and more.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/get-started/pages/capella-iq/work-with-capellaiq.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:get-started:capella-iq/work-with-capellaiq.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/get-started/capella-iq/work-with-capellaiq.html)

# Work Faster with Capella iQ

> Capella iQ is your partner in getting started with Couchbase Capella. Use it to create SQL++ queries, sample data, and more. 

Capella iQ uses the power of a large language model (LLM) to make it even easier for you to work with Couchbase Capella. It does this by incorporating Couchbase-specific knowledge to produce Couchbase-specific answers.

Capella iQ is available as part of Capella’s [query editor](../../clusters/query-service/query-workbench.md) and the Capella Analytics [workbench](../../../analytics/query/workbench.md).

## [](#what-can-capella-iq-do)What Can Capella iQ Do?

With Capella iQ, you can use natural language prompts to:

* Create SQL++ or [SQL++ for Capella Analytics](../../../analytics/sqlpp/1%5Fintro.md) queries
* Create sample datasets
* Provide index suggestions for clusters
* Get SDK-specific connection code for clusters
* Create [cluster objects](../../../analytics/sources/database-objects.md) in Capella Analytics

For more information about using these capabilities, see [Get Started with Capella iQ](get-started-with-iq.md).

> [!NOTE]
> Some features differ between Capella iQ for operational clusters and Capella iQ for [Capella Analytics](../../../analytics/intro/intro.md). For more information about Capella iQ for Analytics, see [Get Assistance from Capella iQ](../../../analytics/query/iq.md).

### [](#explore-results-with-iq-insights)Explore Results with iQ Insights

After running a Capella iQ query, use iQ Insights to generate a variety of relevant insights of your query results. With the power of AI, iQ Insights generates relevant questions, descriptions, and visualizations, helping you gain a better understanding of your data.

To gain insights on your query results, select the **iQ Insights** tab in the query results pane and click the **Generate Now** button.

To learn more about iQ Insights, see [Explore iQ Insights](explore-iq-insights.md).

## [](#how-does-capella-iq-work)How Does Capella iQ Work?

Capella iQ uses a large-language model (LLM) to generate responses to your natural language prompts. It also incorporates Couchbase-specific knowledge to produce Couchbase-specific answers.

Before you can use Capella iQ, an [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner) must accept the [supplemental terms](https://www.couchbase.com/iQ-terms/). Once the supplemental terms are accepted, all users in that organization can use Capella iQ for Capella clusters and Capella Analytics clusters.

For more information, see [Accept Capella iQ Supplemental Terms](configure-capellaiq.md#T&C).

### [](#privacy-and-security)Privacy and Security

Cluster data is not sent to OpenAI. Capella iQ only shares the following information with OpenAI:

* The schema of a chosen collection
* The user prompt
* Couchbase-provided contextual information
* A unique prompt ID so that OpenAI can associate your successive prompts to Capella iQ

All information is securely sent to OpenAI using the OpenAI API.

Couchbase collects information about your use of Capella iQ to improve the service, including in some cases, records of your user prompts and the responses you receive.

Shared responsibility

As a user of Capella iQ, Couchbase would like to remind you that you share a responsibility when using this tool. Capella iQ users must keep the following in mind:

* Do not send confidential information in a prompt, such as personally identifiable information or any confidential information you would not want shared with a third party. Capella iQ shares prompts with OpenAI.
* Verify the output of Capella iQ before using it. The Capella iQ results are a suggestion. LLMs can experience hallucinations and provide incorrect information from time to time.
* Respect the use policies set out in the [Couchbase Capella iQ Supplemental Terms](https://www.couchbase.com/iQ-terms/).

### [](#rate-limits)Rate Limits

Capella iQ implements rate limits both at the user and organization level. This helps to provide equal access to Capella iQ for all users.

## [](#see-also)See Also

* [Get Started with Capella iQ](get-started-with-iq.md)
* [Configure Capella iQ](configure-capellaiq.md)