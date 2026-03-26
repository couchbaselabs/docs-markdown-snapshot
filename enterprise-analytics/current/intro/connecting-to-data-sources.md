---
title: Connecting to Data Sources
description: You can import datasets from multiple sources to work with sample
  data in Enterprise Analytics.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/intro/pages/connecting-to-data-sources.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:enterprise-analytics:intro:connecting-to-data-sources.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/intro/connecting-to-data-sources.html)

# Connecting to Data Sources

> You can import datasets from multiple sources to work with sample data in Enterprise Analytics. 

This section provides a quick guide to getting started with data streaming from diverse sources in Enterprise Analytics.

The tutorial covers:

* how to import sample datasets
* how to set up standalone collections
* how to create remote collections

It details procedures for working with sample datasets, including a `Commerce` example dataset and the `travel-sample` and `beer-sample` datasets. Following these steps provides practice in setting up database objects within Enterprise Analytics for different data sources. For comprehensive information about database objects and advanced data management, refer to the [Access and Organize Data in Enterprise Analytics](../sources/database-objects.md) section.

* Directly [import the travel-sample data](#import-the-travel-sample-collections) into a new database object within your Enterprise Analytics cluster.
* Set up [standalone collections and populate them by inserting the Commerce dataset](#install-the-commerce-dataset-in-standalone-collections).
* Set up a [remote link in Enterprise Analytics](#create-remote-collections-for-beer-sample) to Couchbase Capella. Define remote collections that shadow data from a Capella collection, the beer-sample dataset.

## [](#import-the-travel-sample-collections)Import the travel-sample Collections

The `travel-sample` dataset is available to import from directly inside the workbench and consists of 5 collections of JSON documents: `airline`, `airport`, `landmark`, `hotel`, and `route`.

To import the `travel-sample` into your Enterprise Analytics cluster:

1. In the UI, select the **Workbench** tab, and click **Samples** tab.
2. Select the **travel-sample** checkbox.
3. Click **Load Sample Data**.

Enterprise Analytics creates a new database, travel-sample, with the inventory scope and all 5 collections.

## [](#install-the-commerce-dataset-in-standalone-collections)Install the Commerce Dataset in Standalone Collections

The Commerce dataset consists of two collections:

* `customers`, with the primary key `custid` which has string values
* `orders`, with the primary key `orderno` which has integer values

To work with this dataset in Enterprise Analytics you create a standalone collection for each one. Then, you use INSERT INTO statements to populate them with data.

### [](#create-a-standalone-collection)Create a Standalone Collection

To create a standalone collection:

1. In the Enterprise Analytics UI, select the Workbench tab.
2. Under Databases, click + database. The Create Database dialog box opens.
3. In the Database Name field, enter `sampleAnalytics`.
4. In the Scope Name, enter `Commerce`.
5. Click **Create**.
6. In the Explorer, click + standalone collection. The Add Collection dialog box opens.
7. In the Collection Name field, enter `customers`.
8. In database.scope, choose newly created database `sampleAnalytics` and scope `Commerce`.
9. For the Collection Primary Key, in the Field Name, enter `custid`.
10. In the Field Type list, select string.
11. Click **Save**.

### [](#populate-a-standalone-collection)Populate a Standalone Collection

1. Use the query editor's Query Context lists to select the `sampleAnalytics` database and `Commerce` scope.
2. In the query editor, begin an INSERT INTO statement as follows:  
```sql  
INSERT INTO customers (  
```
3. [Open the customers data](https://docs.couchbase.com/server/current/analytics/%5Fattachments/CommerceCustomers.json), select the contents of the page and copy it.
4. To complete the statement, return to the query editor and paste the JSON document in between the parentheses. You'll need to add the closing parenthesis ) if you used copy and paste to supply the `INSERT INTO` statement.
5. Run the query to populate the `customers` collection.
6. To verify that the collection contains data now, run the following query:  
```sql  
SELECT * FROM customers LIMIT 1;  
```

Create another standalone collection for `orders`, which uses the **Field Name** `orderno` and a **Field Type** of **int** as a primary key. Use the [orders data](https://docs.couchbase.com/server/current/analytics/%5Fattachments/CommerceOrders.json) to select and copy the data for this collection, then populate it using another INSERT INTO statement.

## [](#create-remote-collections-for-beer-sample)Create Remote Collections for beer-sample.

You can import the Couchbase `beer-sample` dataset into a Capella operational cluster or self-managed Couchbase Server cluster. This dataset consists of a single collection, which contains data on beers and breweries.

Set up [remote collections](../sources/manage-remote.md) to hold shadow copies of the `beer-sample` data in Enterprise Analytics. Use WHERE clauses to create multiple collections on Enterprise Analytics, instead of creating only a single collection to match what's in your remote data source in your Capella operational cluster or Couchbase Server.

Any Enterprise Analytics collections that use a WHERE clause apply that clause on an ongoing basis to continuously filter the incoming data event stream. Only documents that meet the WHERE clause criteria are upserted into your Enterprise Analytics collection.

### [](#prepare-to-ingest-data-from-the-remote-system)Prepare to Ingest Data from the Remote System

To prepare your Capella operational cluster for creating a remote collection in Enterprise Analytics, first [Import the beer-sample sample data](../../../cloud/clusters/data-service/import-data-documents.md#import-sample-data) in the Capella cluster. After you have imported the sample data, you can set up your Capella operational cluster as a remote data source in Enterprise Analytics.

To establish a remote link from Enterprise Analytics to a Capella operational, some details must be retrieved from the Capella operational cluster. For more details, refer [Requirements for Couchbase Capella Links](../sources/remote-cb-capella.md#encryption)

### [](#create-a-data-source-for-remote-data)Create a Data Source for Remote Data

1. In the Enterprise Analytics UI, select the **Workbench** tab.
2. Under Databases, click + database. The Create Database dialog box opens.
3. In the Database Name field, enter `remoteCapella`.
4. In the Scope Name, enter `remoteBeer`.
5. Click **Create**.
6. In the Explorer, Select + new link. The Add Link dialog opens.
7. In the Link Name field, enter `capellaLink`.
8. In the Link Type field, select Couchbase.
9. In the Remote Connection String field, select the hostname or IP address of a node in the remote cluster you want to link.
10. In the Encryption Type field, select Full. Enter **Remote Username**, **Remote Password** and **Remote Cluster Certificate**.
11. Select the **Prevents Redirects** checkbox to prevent HTTP connections for the remote link.
12. Click **Save**. The remote link to Capella `capellaLink` is created.
13. In the Explorer, Select + collection next to the newly created `capellaLink`. The Add Remote Collection dialog opens.
14. In the Collection Name field,enter `brewBelgium`.
15. In the Database list, select database `remoteCapella` and in the Scope select `remoteBeer` to specify the destination for your remote collection.
16. In the Source bucket.scope.collection field, select the beer-sample bucket, and \_default scope and collection.
17. In the provided field, enter a WHERE clause for the documents in the collection to filter required data for ingestion:  
```sql  
country = "Belgium"  
```
18. Click **Save**. Your collection appears under `remoteCapella.remoteBeer` in the Explorer.
19. Connect the link `capellaLink` by clicking on the connect link icon or running:  
```none  
CONNECT LINK capellaLink;  
```
20. Verify that your `brewBelgium` collection now contains a shadow copy of the data sourced from Capella by running the following query, with your query context set to `remoteCapella` and `remoteBeer`:  
```sql  
SELECT * FROM brewBelgium LIMIT 1;  
```

## [](#next-steps)Next Steps

You can continue to expand your data landscape by creating more collections using the same remote link to your Capella operational cluster. For those preferring programmatic setup, DDL statements are also available for creating remote Couchbase collections. Refer to the examples in [Create a Remote Couchbase Collection](../sqlpp/5%5Fddl%5Fremote.md).

With your data established, the next step is analysis. Consult the [SQL++ Reference](../sqlpp/1%5Fintro.md) to learn how to query and explore your data.