---
title: Get Assistance from Capella iQ
description: Capella iQ is a service that leverages a large language model to
  help you write queries.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/query/pages/iq.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:analytics:query:iq.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/query/iq.html)

# Get Assistance from Capella iQ

> Capella iQ is a service that leverages a large language model to help you write queries. 

> [!NOTE]
> Remember that Capella iQ harnesses the power of third-party large language models (LLM) to improve your queries. Do not provide sensitive data in the prompt such as personally identifiable information or any confidential information that you would not want shared. Because technology built on LLMs can also suffer from hallucinations from time to time, be sure to review the output.

Capella iQ is your partner in Capella Analytics, allowing you to work faster and assist you directly in the Capella UI. It uses a large language model (LLM) to generate queries based on plain language prompts.

For example, if you [loaded the travel-sample dataset](../intro/examples.md#travel-sample), you could use a prompt like `Show me the flights flying from JFK to SFO` to get Capella iQ to generate a SQL++ for Capella Analytics query using the `airline` and `route` collections. Capella iQ also produces responses based on context - you could refine the query with another prompt, such as `Only show those with the call sign United`, without repeating your first request.

## [](#prerequisites)Prerequisites

* If you're the [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner), accept Capella iQ's supplemental terms and turn it on for your organization. For more information, see [Configure Capella iQ](../../cloud/get-started/capella-iq/configure-capellaiq.md).
* (Optional) Create a data source for Couchbase sample data. For the first example on this page, you need the `travel-sample` dataset. See [Access Data](../intro/examples.md).

## [](#open-capella-iq)Open Capella iQ

Use Capella iQ from the Capella Analytics workbench. For more information about the workbench, see [Query and Explore with the Workbench](workbench.md).

From the **Workbench**, click the **iQ** tab.

## [](#generate-sql-for-capella-analytics-queries)Generate SQL++ for Capella Analytics Queries

You can generate SQL++ for Capella Analytics queries with conversational questions using the sample data or your own data.

1. At the top of the iQ pane, use the lists to choose a database, scope, and at least one collection for your iQ queries.  
After you choose the collection, iQ suggests some sample queries to start working with your data.
2. Run a suggested SQL++ for Capella Analytics query or provide a prompt for a custom query:

  * Click **Run** for a suggestion to have iQ return a related SQL++ for Capella Analytics query.
  * To generate a custom query, type your prompt in the iQ message field. After you review the query that Capella iQ returns, click **Run**.
3. Modify the query using follow-up prompts.

> [!NOTE]
> Always review every query that iQ returns before running it.

### [](#example-generate-a-sql-for-capella-analytics-query-with-travel-sample-sample-data)Example: Generate a SQL++ for Capella Analytics Query with `travel-sample` Sample Data

If you have [loaded the travel-sample dataset](../intro/examples.md#travel-sample) into Capella Analytics, you can try the following with Couchbase iQ to generate SQL++ for Capella Analytics queries:

1. At the top of the iQ pane, use the lists to select the following:

  * The `travel-sample` database
  * The `inventory` scope
  * The `airline` and `route` collections
2. Enter the following prompt:  
Show me airlines that fly from JFK to SFO.
3. Click **Run** and [look at the results](results.md).
4. Enter another prompt to modify and iterate on iQ's first query:  
This should be the number of flights by each airline.
5. Click **Chart** to view the results of the query in [chart format](charts.md), instead.

You can continue iterating on the query and [working with the query results](results.md) inside the workbench.

## [](#visualize-query-results-with-iq-insights)Visualize Query Results with iQ Insights

After running a Capella iQ query, use iQ Insights to generate a variety of relevant insights into your query results. With the power of AI, iQ Insights generates relevant questions, descriptions, and visualizations, helping you gain a better understanding of your data.

To gain insights on your query results, select the **iQ Insights** tab in the query results pane and click the **Generate Now** button.

For more information, see [Explore Results with iQ Insights](iq-insights.md).

## [](#create-database-objects-and-generate-sample-documents)Create Database Objects and Generate Sample Documents

You can also prompt iQ to create new database objects, such as [databases](../sources/database-objects.md#databases), [scopes](../sources/database-objects.md#scopes), and [collections](../sources/database-objects.md#collections). You can choose to turn these collections into standalone collections, and populate them with generated sample documents.

### [](#example-create-database-objects-populate-with-generated-data-and-use-a-join)Example: Create Database Objects, Populate with Generated Data, and Use a JOIN

Try the following to create new database objects and generate sample data:

1. In the iQ pane, enter the following prompt to create a new database:  
Create a new database called "finance".
2. Click **Run** to create the database.
3. With the new `finance` database selected in the lists at the top of the iQ pane, enter another prompt to create a new scope:  
Create a scope called "data".
4. Click **Run** to create the scope.
5. With the new `data` scope also selected in the lists, enter another prompt to create a new collection:  
Create a collection called "customerPersonalData".
6. Click **Run** to create the collection.
7. Enter another prompt to generate sample data:  
Generate 10 documents to be inserted into customerPersonalData with the fields name, age, gender, address, and zipcode.
8. Click **Run** to insert the generated documents.
9. Enter another prompt to create another new collection:  
Create a collection called "customerAccountData".
10. Click **Run** to create the collection.
11. Enter another prompt to generate more sample documents:  
Generate 10 documents to be inserted into customerAccountData. Use the same name values as in customerPersonalData. Add the fields checking account number, checking account balance, savings account number, and savings account balance.
12. Click **Run**.
13. With the `customerPersonalData` and `customerAccountData` collections selected in the lists, enter a prompt for a SQL++ for Capella Analytics query that joins data from the 2 collections:  
Give me the name, age, checking account balance and savings account balance for all customers.
14. Click **Run** and [look at the results](results.md).

Keep iterating on queries with iQ, or explore your own queries and results with the [workbench](workbench.md).

## [](#see-also)See Also

* [Access Data](../intro/examples.md)
* [SELECT Statements](../sqlpp/3%5Fquery.md)
* [Query and Explore with the Workbench](workbench.md)