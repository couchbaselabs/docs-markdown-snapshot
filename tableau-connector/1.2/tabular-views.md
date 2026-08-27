---
title: Couchbase Analytics Tabular Views
description: Create Tabular Analytics Views (TAVs) from Couchbase datasets for
  use with Tableau.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-tableau/edit/release/1.2/modules/ROOT/pages/tabular-views.adoc
  xref: xref:1.2@tableau-connector::tabular-views.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tableau-connector/1.2/tabular-views.html)

# Couchbase Analytics Tabular Views

> Create Tabular Analytics Views (TAVs) from Couchbase datasets for use with Tableau. 

Tableau requires data sources to be in tabular form and accessible through SQL. To meet this requirement, Couchbase provides Tabular Analytics Views (TAVs).

A TAV is a type of Analytics view that enables Couchbase Analytics to interact with software tools designed for relational databases. TAVs present data as a table with uniform rows and columns and a well-defined schema.

To prepare tabular analytics views, see:

* [Tabular Analytics Views](../../analytics/sqlpp/5a%5Fviews.md#TAV) for Capella Analytics
* [Tabular Analytics Views](../../server/current/analytics/5a%5Fviews.md#tabular-analytics-views) for Couchbase Server or Capella Operational

The following example shows how to create a TAV.

## [](#step-1-load-the-sample-bucket)Step 1: Load the Sample Bucket

This example uses the `travel-sample` bucket, which comes with predefined Analytics collections and tabular views.

To load the bucket:

1. Open the Couchbase Server Web Console.
2. Go to **Settings** **Sample Buckets**.
3. Select `travel-sample`.
4. Click **Load Sample Data**.

## [](#step-2-create-a-tabular-analytics-view)Step 2: Create a Tabular Analytics View

While the `travel-sample` dataset includes default Tabular Analytics Views (TAVs), you can also create custom ones.

To create a TAV:

1. Open Couchbase Server Web Console and go to **Analytics**.
2. In the **Analytics Workbench**, set the scope to `travel-sample.inventory`.
3. Run the following statement in the **Query Editor**.  
```sqlpp  
CREATE OR REPLACE ANALYTICS VIEW hotel_custom_view (  
    id STRING,  
    name STRING,  
    city STRING,  
    country STRING  
)  
DEFAULT NULL  
PRIMARY KEY (id) NOT ENFORCED  
AS  
   SELECT meta().id AS id,  
          name,  
          city,  
          country  
   FROM hotel;  
```  
This statement creates a TAV named `hotel_custom_view` in the `travel-sample.inventory` scope. The view includes the `id`, `name`, `city`, and `country` fields from the `hotel` collection.

## [](#step-3-verify-analytics-collections-and-tabular-views)Step 3: Verify Analytics Collections and Tabular Views

Before connecting to Tableau, verify that your Analytics collections and tabular views are available.

1. Open Couchbase Server Web Console and go to **Analytics**.
2. In the **Analytics Scopes** pane, confirm that the default and custom views appear in the list.
3. Click the drop-down arrow next to a view name to see its schema.