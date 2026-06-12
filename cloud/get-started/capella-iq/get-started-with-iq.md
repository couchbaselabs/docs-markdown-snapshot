---
title: Get Started with Capella iQ
description: Capella iQ is your partner in getting started with Couchbase
  Capella. Use it to generate SQL++ queries, sample data, build indexes, and
  more.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/get-started/pages/capella-iq/get-started-with-iq.adoc
pubDate: 2026-06-12T16:31:57.907Z
link: xref:cloud:get-started:capella-iq/get-started-with-iq.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/get-started/capella-iq/get-started-with-iq.html)

# Get Started with Capella iQ

> [!NOTE]
> Remember that Capella iQ harnesses the power of a third-party large language model (LLM) to improve your queries. Do not provide sensitive data in the prompt such as personally identifiable information or any confidential information that you would not want shared. Because technology built on LLMs can also suffer from hallucinations from time to time, be sure to review the output.

Capella iQ is your partner in Capella, allowing you to work faster and assist you directly in the Capella UI. It uses a large language model (LLM) and Couchbase-specific knowledge to generate SQL++ queries and more based on natural language prompts. For example, you can ask Capella iQ to generate a SQL++ query in a cluster with the travel-sample dataset using the `Count the number of airlines per country` prompt. Capella iQ also produces responses based on the context of a chat session. You can iterate on this query with another prompt, such as `Only count those in the United States.`

> [!NOTE]
> Only questions that relate to your cluster and Couchbase generate a response. The examples on this page relate to operational clusters only. For more information about using iQ with Capella Analytics, see [Get Assistance from Capella iQ](../../../analytics/query/iq.md).

## [](#prerequisites)Prerequisites

* The [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner) has:

  * Accepted the Capella iQ Supplemental Terms. For more information, see [Accept Capella iQ Supplemental Terms](configure-capellaiq.md#T&C).
  * Selected the available model providers for clusters in the organization. You can choose either OpenAI, AWS Bedrock, or both. For more information, see [Select Your Organization's Capella iQ Model Provider](configure-capellaiq.md#select-org-model).
* A cluster with the Data, Index, and Query services. To create a cluster, see [Create A Paid Cluster](../../clusters/create-database.md).
* If you're using Capella iQ to create SDK code, you need [cluster access credentials](../../clusters/manage-database-users.md) to implement it.
* (Optional) Import the Capella [sample data](../../clusters/data-service/import-data-documents.md#import-sample-data). If you're using a free tier operational cluster, it already has the sample data.

## [](#open-capella-iq)Open Capella iQ

Capella iQ is a part of the query editor in Capella's Data Tools. As part of the Capella UI, the query editor is like an IDE you can use to work with data, documents, queries, indexes, and more.

To open Capella iQ:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Operational**.
  * Click your current project name or search for a project and go to **Operational**.
  * Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to work with Capella iQ.
3. Click **Data Tools** **Query**.
4. In the query history area, click **iQ**.

> [!NOTE]
> If it's available in your organization, you can select a [model provider](#work-with-capellaiq.adoc#model-provider) (OpenAI or AWS Bedrock) for Capella iQ in the query editor. For more information, see [Set Your Preferred Model Provider](configure-capellaiq.md#select-cluster-model).

## [](#generate-sql-queries)Generate SQL++ Queries

> [!NOTE]
> Always review every query that Capella iQ returns before running it.

Use sample data to generate SQL++ queries with conversational questions.

To generate SQL++ queries:

1. In the Capella iQ pane, use the lists to choose a bucket, scope, and up to 4 collections.  
After you choose your collections, Capella iQ suggests some sample queries to start working with your data.
2. Generate a SQL++ query using 1 of the following methods:

  * Click a suggestion to have Capella iQ return a SQL++ query relevant to the chosen collections.
  * To generate a custom query, type your prompt in the Capella iQ message field.
3. Review the query that Capella iQ returns.
4. Click **Run** to run the query in the query editor as is, or modify it using follow-up prompts.

### [](#visualizing-results-in-charts)Visualizing Results in Charts

When Capella iQ generates a query it also includes a **Chart** button so you can visualize the query results.

For example, suppose you want a count of the airlines in each country in the travel-sample dataset. To visualize these results in a chart:

1. In the Capella iQ pane, use the lists to choose the following:

  * Bucket: `travel-sample`
  * Scope: `inventory`
  * Collections: `airline`
2. Enter or click the suggested `Count the number of airlines per country` prompt.
3. In the suggested results, click **Chart**.
4. The results display as a chart in the query results pane.  
Like any chart the query editor returns, you can change the chart type and data options. For more information about using charts, see [Chart Format](../../clusters/query-service/query-workbench.md#query-chart).

### [](#explore-results-with-iq-insights)Explore Results with iQ Insights

After running a Capella iQ query, use iQ Insights to generate a variety of relevant insights of your query results. With the power of AI, iQ Insights generates relevant questions, descriptions, and visualizations, helping you gain a better understanding of your data.

To gain insights on your query results, select the **iQ Insights** tab in the query results pane and click the **Generate Now** button.

To learn more about iQ Insights, see [Explore iQ Insights](explore-iq-insights.md).

## [](#create-scopes-and-collections)Create Scopes and Collections

You can create scopes and collections using natural language prompts with Capella iQ.

For example, you could prompt Capella iQ to `create a scope named trains and a collection named operator`. To create this scope and collection:

1. In the Capella iQ pane, choose a bucket.  
Capella iQ suggests a sample query that creates a scope with collections and sample data.
2. Generate a SQL++ query that creates scopes and collections using 1 of the following methods:

  * Click the provided suggestion to have Capella iQ return a related SQL++ query.
  * Enter a custom prompt. For example, `Create a scope named trains and a collection named operator`.
3. Review the query that Capella iQ returns.
4. Run the query as is by clicking **Run**, or modify it using follow-up prompts.  
The query output appears in the query results pane of the query editor. When you create a new scope and collection, Capella iQ shows a suggestion link to select the new collection so you can start working with it.

## [](#generate-sample-data)Generate Sample Data

You can ask Capella iQ to generate realistic sample data and insert it into your cluster. Generating sample data is helpful when testing configurations and learning about Capella.

For example, suppose you're building an application that requires data about national parks in the United States. You can use Capella iQ to populate your cluster with relevant data. To generate this sample data:

> [!TIP]
> The provided prompts are for example purposes. With Capella iQ, you can format your prompts differently to get the same information.

1. Create a new scope and collection for national parks data:

  1. With only a bucket selected, enter the following prompt: `Create a scope named parks and a collection named usaparks`.
  2. Review the query that Capella iQ returns and click **Run**.
2. Insert realistic sample documents into the `usaparks` collection:

  1. Enter the following prompt: `Insert 10 real-looking sample documents of USA national parks in the usaparks collection using uuid() as the key`.
  2. Review the query that Capella iQ returns and refine it with further prompts if needed.
  3. Click **Run**.

## [](#generate-sdk-code-preview)Generate SDK Code (Preview)

To help speed up application development, Capella iQ can generate SDK code based on your prompt:

1. At the top of the Capella iQ pane, use the lists to choose a bucket, scope, and up to 4 collections where applicable.
2. Submit a prompt for a custom query. For example, "create a scope."
3. When the query suggestion appears, click **SDK Preview**.  
> [!NOTE]  
> When clicking **SDK Preview** for the first time, the iQ Settings dialog appears so you can select your preferred SDK language. After choosing a language, the **SDK Preview** button changes to the name of your chosen language.  
In the query results pane, the SDK code appears with an option to copy it.
4. Review any code before using it and replace `your_username` and `your_password` with your [cluster access credentials](../../clusters/manage-database-users.md).  
You cannot iterate on the SDK code that Capella iQ suggests at this time. When you return to the Capella iQ prompt field, you return to SQL++ query generation.

## [](#add-a-query-to-favorites)Add a Query to Favorites

After successfully running a query suggestion from Capella iQ, the prompt response adds the **Favorite** button.

Marking a query as a favorite lets you refer back to it and gives the option to include it as part of your prompts. Including a favorite query in your prompts can improve Capella iQ's accuracy and usability across your chat sessions. For example, this is useful when working with JOINs. If you prompt Capella iQ to use a [JOIN](../../n1ql/n1ql-language-reference/join.md), you can save the successful query so that subsequent queries can reference this JOIN. You can then prompt Capella iQ without having to mention this JOIN.

> [!NOTE]
> Only 1 of your favorite queries can be included in your prompts.

To view all favorite queries, click **Browse favorite queries** (⭒).

You can remove any favorite queries by clearing **Favorite**. Similarly, you can remove a favorite query from future prompts—but keep it as a favorite—by deselecting **Include in prompt**.

## [](#see-also)See Also

* [Work Faster with Capella iQ](work-with-capellaiq.md)
* [Configure Capella iQ](configure-capellaiq.md)
* [Explore iQ Insights](explore-iq-insights.md)
* [Get Assistance from Capella iQ in Analytics](../../../analytics/query/iq.md)