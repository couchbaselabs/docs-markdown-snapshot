---
title: Save Views or Tabular Views
description: You can save the results of queries that use selection syntax in a
  view or tabular view.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/query/pages/views-tavs.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/analytics/query/views-tavs.html)

# Save Views or Tabular Views

> You can save the results of queries that use selection syntax in a view or tabular view. 

## [](#prerequisites)Prerequisites

To use the workbench for Capella Analytics:

* You must have the [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) role in your organization, or one of the following [project roles](../../cloud/projects/project-roles.md) for the project that contains your cluster:

  * [Project Owner](../../cloud/projects/project-roles.md#project-owner-role)
  * [Database Data Reader/Writer](../../cloud/projects/project-roles.md#project-cluster-data-reader-writer) (Allows queries that read and write data)
  * [Database Data Reader](../../cloud/projects/project-roles.md#project-cluster-data-reader) (Allows read-only queries)

## [](#save-results-as-a-view)Save Results as a View

To save results in a view, select **Save Query as View**. After you supply a name for the view, it appears in the explorer under a **Views** heading.

Example

To access the `travel-sample` data used in this example from Capella Analytics, see [Import the travel-sample Collections](../intro/examples.md#travel-sample).

For example, you enter the following query:

```SQL++
  SELECT * FROM travel-sample.inventory.airline
  WHERE country = "FRANCE";
```

You then select **Save as View** and save the results in a `FrenchAirlines` view.

You can then query your view:

```SQL++
  SELECT * FROM travel-sample.inventory.FrenchAirlines;
```

The results show that a new top-level `"FrenchAirlines"` object contains the selected `"airline"` objects.

## [](#TAV)Save Results as a Tabular View

To make data in JSON format usable by relational tools such as Tableau and Power BI, you save query results in a tabular view. Tabular views are also referred to as tabular analytics views (TAV).

Capella Analytics uses a normalization process to convert nested objects into tabular form. When you create a tabular view, you:

* Flatten any objects that themselves contain a nested object.
* Select the keys to include as columns in the table.
* Specify the data types for the columns.
* Identify the field or fields that make up the primary key.
* Specify the name of the foreign view for any fields that are foreign keys.

Example

To access the `travel-sample` data used in this example from Capella Analytics, see [Import the travel-sample Collections](../intro/examples.md#travel-sample).

For example, you enter the following query:

```SQL++
  SELECT * FROM travel-sample.inventory.airline LIMIT 25;
```

After you select **Save as View**, you click **Annotate for Tabular View**.

Initially, your query results in the error "Tabular views can’t work with object or array fields. No view-usable fields found." Capella Analytics suggests query syntax to flatten the `"airline"` object.

You re-try the query with the suggested syntax:

```SQL++
  SELECT airline.* FROM travel-sample.inventory.airline LIMIT 25;
```

Now you specify the primary key, select which keys to include as columns, and can make any adjustments to the data types Capella Analytics supplies.

For more information about the normalization process, see [Tabular Views](../sqlpp/5a%5Fviews.md#TAV). For more information about connecting to data visualization tools, see [Use Business Intelligence Tools](bi.md).

## [](#see-also)See Also

* [Access Data](../intro/examples.md)
* [Use Business Intelligence Tools](bi.md)