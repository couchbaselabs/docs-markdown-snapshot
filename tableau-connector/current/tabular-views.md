---
title: Couchbase Analytics Tabular Views
description: Create Tabular Analytics Views (TAVs) from Couchbase datasets for
  use with Tableau.
editUrl: https://github.com/couchbase/docs-tableau/edit/release/2.0/modules/ROOT/pages/tabular-views.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:tableau-connector::tabular-views.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tableau-connector/current/tabular-views.html)

# Couchbase Analytics Tabular Views

> Create Tabular Analytics Views (TAVs) from Couchbase datasets for use with Tableau. 

Tableau requires data sources to be in tabular form and accessible through SQL. To meet this requirement, Couchbase provides Tabular Analytics Views (TAVs).

A TAV is a type of analytics view that enables Couchbase to interact with software tools designed for relational databases. TAVs present data as a table with uniform rows and columns and a well-defined schema.

To prepare tabular analytics views for Enterprise Analytics, see [Tabular Analytics Views](../../enterprise-analytics/current/sqlpp/5a%5Fviews.md#TAV).

The following example shows how to create a TAV.

## [](#step-1-load-the-sample-bucket)Step 1: Load the Sample Bucket

This example uses the `travel-sample` bucket, which comes with predefined Analytics collections and tabular views.

To load the bucket:

1. Open the Enterprise Analytics Web Console.
2. Go to **Workbench** **Samples**.
3. Select `travel-sample`.
4. Click **Load Sample Data**.

## [](#step-2-create-a-tabular-analytics-view)Step 2: Create a Tabular Analytics View

While the `travel-sample` dataset includes default Tabular Analytics Views (TAVs), you can also create custom ones.

To create a TAV:

1. Open Enterprise Analytics Web Console and go to **Workbench**.
2. In the **Query Editor**, set the scope to `travel-sample.inventory`.
3. Run the following statement in the **Query Editor**.  
```sqlpp  
CREATE OR REPLACE ANALYTICS VIEW airline_custom_view (  
    id STRING,  
    name STRING,  
    iata STRING,  
    callsign STRING,  
    country STRING  
)  
DEFAULT NULL  
PRIMARY KEY (id) NOT ENFORCED  
AS  
   SELECT meta().id AS id,  
          name,  
          iata,  
          callsign,  
          country  
   FROM airline;  
```  
This statement creates a TAV named `airline_custom_view` in the `travel-sample.inventory` scope. The view includes the `id`, `name`, `iata`, `callsign`, and `country` fields from the `airline` collection.

## [](#step-3-verify-analytics-collections-and-tabular-views)Step 3: Verify Analytics Collections and Tabular Views

Before connecting to Tableau, verify that your Analytics collections and tabular views are available.

1. Open Enterprise Analytics Web Console and go to **Workbench**.
2. In the right-hand pane, confirm that the default and custom views appear in the **Databases** list.