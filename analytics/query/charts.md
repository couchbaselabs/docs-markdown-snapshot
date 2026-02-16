[View original HTML](/analytics/query/charts.html)

> After you run a query, you can visualize its results in graphical format. 

## [](#prerequisites)Prerequisites

To use the workbench for Capella Analytics:

* You must have the [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) role in your organization, or one of the following [project roles](../../cloud/projects/project-roles.md) for the project that contains your cluster:

  * [Project Owner](../../cloud/projects/project-roles.md#project-owner-role)
  * [Database Data Reader/Writer](../../cloud/projects/project-roles.md#project-cluster-data-reader-writer) (Allows queries that read and write data)
  * [Database Data Reader](../../cloud/projects/project-roles.md#project-cluster-data-reader) (Allows read-only queries)

## [](#configure-graph-settings)Configure Graph Settings

When you select the **Chart** tab in the query results pane, you can visualize query results in graphical format.

You select the type of graph, and then choose the fields—JSON keys—to include. For example, to populate a bar or pie chart:

* For the first, x-axis selection you choose a field with a string-type value
* For the second, y-axis selection you choose a number-type value.

For an X-Y graph, on the other hand, both fields must have number-type values.

In this example for the travel-sample’s airport collection, a bar chart plots the results of a query. The x-axis plots the country and the number of airports is on the y-axis.

![A chart with 3 bars showing the relative number of airports in the US, France, and the UK](_images/chart_example.png)

For more information about working with sample datasets, see [Access Data](../intro/examples.md).

### [](#visualize-results-using-ai-with-iq-insights)Visualize Results Using AI with iQ Insights

The **iQ Insights** tab lets you leverage the power of AI to generate relevant questions, descriptions, and visualizations of your query results. You can choose from any of the generated insights and select those that best represent your data.

For more information about iQ Insights, see [Explore Results with iQ Insights](iq-insights.md).

## [](#see-also)See Also

* [SELECT Statements](../sqlpp/3%5Fquery.md)
* [Use Business Intelligence Tools](bi.md)
* [Explore Results with iQ Insights](iq-insights.md)