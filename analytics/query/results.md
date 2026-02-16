[View original HTML](/analytics/query/results.html)

> The query results pane of the workbench provides options for displaying, copying, downloading, and otherwise working with the results of a query. 

## [](#prerequisites)Prerequisites

To use the workbench for Capella Analytics:

* You must have the [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) role in your organization, or one of the following [project roles](../../cloud/projects/project-roles.md) for the project that contains your cluster:

  * [Project Owner](../../cloud/projects/project-roles.md#project-owner-role)
  * [Database Data Reader/Writer](../../cloud/projects/project-roles.md#project-cluster-data-reader-writer) (Allows queries that read and write data)
  * [Database Data Reader](../../cloud/projects/project-roles.md#project-cluster-data-reader) (Allows read-only queries)

## [](#results)Review JSON Formatted Results

When you execute a query, the results display in the query results pane. By default, the **JSON** tab displays in the query results pane, showing the results in JSON format.

You can expand and collapse objects and array values using the small arrow icons next to the line numbers.

## [](#review-tabular-formatted-results)Review Tabular Formatted Results

The **Table** tab presents the results in a tabular format. Capella Analytics converts the JSON documents to HTML tables for this display, and presents sub-objects and sub-arrays as sub-tables.

This format works well for queries that return an array of objects.

## [](#download-or-copy-results)Download or Copy Results

When you view query results on the **JSON** tab, icons give you options to:

* Download the results in JSON format.
* Copy the results in JSON format.

When you view results on the **Table** tab, icons give you options to:

* Download the results in JSON format.
* Copy the results in TSV format.

You can then use the file with the query results as needed, or paste the results into another tool such as a spreadsheet.

## [](#see-also)See Also

The query results pane also offers these options for working with results:

* [Visualize Results in Charts](charts.md)
* [View the Query Plan](metrics-plan.md#plan)
* [Save Views or Tabular Views](views-tavs.md)