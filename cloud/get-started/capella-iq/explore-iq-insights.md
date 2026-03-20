---
title: Explore iQ Insights
description: iQ Insights uses the power of AI to provide you with key insights
  into your query results. Use it to better understand your data with generated
  questions and visualizations.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/get-started/pages/capella-iq/explore-iq-insights.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:get-started:capella-iq/explore-iq-insights.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/get-started/capella-iq/explore-iq-insights.html)

# Explore iQ Insights

> iQ Insights uses the power of AI to provide you with key insights into your query results. Use it to better understand your data with generated questions and visualizations. 

iQ Insights uses the power of Large Language Models (LLMs) to generate valuable insights from your query results. By integrating AI with your data, iQ Insights can automatically generate relevant questions based on your query outcomes. These questions are then answered with descriptions and data visualizations, offering you a deeper analysis of your results to enhance your understanding of your data.

Use [Capella iQ](get-started-with-iq.md) to create SQL++ queries based on your natural language questions and use iQ Insights to get better insights from the data in your query results.

iQ Insights is available on all plans for Capella operational and Capella Analytics clusters. You can find it as a part of Capella’s [query editor](../../clusters/query-service/query-workbench.md) and the Capella Analytics [workbench](../../../analytics/query/workbench.md).

## [](#about-iq-insights)About iQ Insights

iQ Insights uses an LLM to suggest relevant questions based on your query results and generate responses with descriptions and visualizations. It analyzes and extracts the structure of your document schema from the JSON datasets of query results to generate relevant bar charts, line graphs, scatter plots, or other more complex visualizations.

Before you can use Capella iQ or iQ Insights, an [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner) must accept the [Supplemental Terms](https://www.couchbase.com/iQ-terms/). Once the terms and conditions are accepted, all users in an organization can use Capella iQ and iQ Insights in any Capella operational and Analytics clusters.

By accepting the Supplemental Terms for Capella iQ, you also accept the terms for iQ Insights.

> [!IMPORTANT]
> To disable iQ Insights, an `Organization Owner` must disable Capella iQ at the organizational level. Disabling Capella iQ also disables iQ Insights. For more information, see [Turn Capella iQ Off for Your Organization](configure-capellaiq.md#turn-capella-iq-off-for-your-organization).

## [](#prerequisites)Prerequisites

* An organization owner has accepted the iQ Insights Supplemental Terms. For more information, see [Privacy and Security](#privacy-and-security).
* You have deployed a [Capella operational cluster](../../clusters/create-database.md) or a [Capella Analytics cluster](../../../analytics/admin/prepare-project.md). If you’re working with an operational cluster, it must have the Data, Query, and Index Service deployed on at least 1 Service Group.
* Your queries must:

  1. Either use a dataset with clear document names or have clear query projection names. iQ Insights will attempt to auto-infer your data but it needs meaningful data labels to create charts.
  2. Use SELECT statements only. SELECT statements can include WITH and LIMIT clauses. Queries with any other statements or clauses are not supported.
  3. Generate result sets that are within the 6 MB sizing limit and contain more than 1 document.

> [!IMPORTANT]
> If iQ Insights is producing errors, review the prerequisites and make sure your query follows the iQ Insights query guidelines before trying again.

## [](#generate-visualizations-with-iq-insights)Generate Visualizations with iQ Insights

After you run SQL++ queries, select the **iQ Insights** tab in the query results pane and click **Generate Now**. This generates logical questions based on your query results and presents answers with various graphs and charts.

Following the `travel-sample` example from [Generate SQL++ Queries](get-started-with-iq.md#generate-sql-queries), iQ Insights generates the following insights:

![The results of the query rendered as iQ Insights in the query editor results area](../_images/iq/iq-insights-results.png) 

Based on the first generated question, the LLM could infer its response visually through a bar chart. Alongside the description, you can identify which countries have the highest and lowest airline counts.

You can choose and use the visualizations most useful to you. The UI allows you to export charts in PNG format, select areas using lasso or box selection, and zoom in or out of the visualizations.

iQ Insights is available to use with all SELECT queries, including those generated by Capella iQ.

> [!NOTE]
> Capella iQ provides two options for visualizations:
> 
> 1. The **Charts** button, which provides basic charting of results.
> 2. The **iQ Insights** button, which provides insights and visualizations of your results using AI.

### [](#privacy-and-security)Privacy and Security

iQ Insights has the same privacy and security terms as Capella iQ. By accepting the Supplemental Terms for Capella iQ, you also accept the terms for iQ Insights. For more information about using [OpenAI](https://openai.com/) based tools in Couchbase Capella, see [Privacy and Security](work-with-capellaiq.md#privacy-and-security).

Shared responsibility

As a user of iQ Insights, Couchbase would like to remind you that you share a responsibility when using this tool. Users of iQ Insights must keep the following in mind:

* Do not generate a chart using confidential query results, such as personally identifiable information or any confidential information you would not want shared with a third party. See [Privacy and Security](work-with-capellaiq.md#privacy-and-security) for more information.
* Verify the output of iQ Insights before using it. iQ Insights results are a visualization aid. LLMs can experience hallucinations and provide incorrect information from time to time.
* Respect the use policies set out in the [Couchbase Capella iQ Supplemental Terms](https://www.couchbase.com/iQ-terms/).

### [](#rate-limits)Rate Limits

iQ Insights implements rate limits both at the user and organization level. This helps to provide equal access to Capella iQ for all users.

Free tier clusters can generate a maximum of 3 charts per query.

Paid clusters can generate a maximum of 5 charts per query.

## [](#see-also)See Also

* [Work Faster with Capella iQ](work-with-capellaiq.md)
* [Get Started with Capella iQ](get-started-with-iq.md)