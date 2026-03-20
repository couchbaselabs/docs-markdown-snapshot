---
title: Access Data
description: You can set up different data sources to work with sample data in
  Capella Analytics.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/intro/pages/examples.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:analytics:intro:examples.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/intro/examples.html)

# Access Data

> You can set up different data sources to work with sample data in Capella Analytics. 

This Capella Analytics guide includes example statements and queries that refer to sample datasets, including a `Commerce` example dataset and the Couchbase `travel-sample` and `beer-sample` datasets.

Use the procedures on this page to create Capella Analytics collections for these datasets. Each section gives you practice setting up database objects in Capella Analytics so that you can work with data from different sources. For more information about Capella Analytics database objects, see [Access and Organize Data in Capella Analytics Services](../sources/database-objects.md).

* Set up [standalone collections and populate them by inserting the Commerce dataset](#install).
* Directly [import the travel-sample data](#travel-sample) into a new database object in your Capella Analytics cluster.
* Set up a [remote data source—a link and a set of remote collections—to shadow beer-sample data](#beer-sample) in a Capella collection.  
> [!NOTE]  
> The `beer-sample` example requires you to set up a Capella operational cluster as a remote data source for Capella Analytics. The `Commerce` dataset and `travel-sample` do not require a Capella operational cluster or other remote data source to set up.

## [](#prerequisites)Prerequisites

* If you’re just getting started with Capella Analytics, make sure that you [created a Couchbase Capella account](../../cloud/get-started/create-account.md#sign-up-free-trial).
* Create a project and Capella Analytics cluster. For more information about how to set up your project and cluster in Capella Analytics, see [Create a Cluster](../admin/prepare-project.md).
* If you want to work with the [beer-sample dataset](#beer-sample), you must have a Capella operational cluster deployed. This cluster is the remote data source for the sample data in the example. For more information about how to create a Capella operational cluster, see [Create A Paid Cluster](../../cloud/clusters/create-database.md).
* To follow along with the examples on this page, you must have the [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) role in your organization, or one of the following [project roles](../../cloud/projects/project-roles.md) for the project that contains your cluster:

  * [Project Owner](../../cloud/projects/project-roles.md#project-owner-role)
  * [Database Data Reader/Writer](../../cloud/projects/project-roles.md#project-cluster-data-reader-writer)

## [](#install)Install the Commerce Dataset in Standalone Collections

The Commerce dataset consists of two collections:

* `customers`, with the primary key `custid` which has string values
* `orders`, with the primary key `orderno` which has integer values

To work with this dataset in Capella Analytics you create a standalone collection for each one. Then, you use INSERT INTO statements to populate them with data.

### [](#create-a-standalone-collection)Create a Standalone Collection

1. In the Capella UI, select the **Capella Analytics** tab and then click a cluster name. The workbench opens.
2. In the explorer, go to **Create** **Database**.
3. In the **Database Name** field, enter `sampleAnalytics`.
4. Click **Add Scope to New Database** to create a scope named `Commerce`.
5. Click **Create**.
6. In the explorer, point to the **Commerce** scope and go to **More Options (⋮)** **Add Standalone Collection**.
7. In the **Collection Name** field, enter `customers`.
8. For the **Collection Primary Key**, in the **Field Name**, enter `custid`.
9. In the **Field Type** list, select **string**.
10. Click **Create**.

### [](#populate-a-standalone-collection)Populate a Standalone Collection

1. Use the query editor’s **Query Context** lists to select the `sampleAnalytics` database and `Commerce` scope.
2. In the query editor, begin an INSERT INTO statement as follows:  
```SQL++  
  INSERT INTO customers (  
```  
> [!TIP]  
> If you type in the statement instead of copying and pasting this example, the query editor automatically supplies the closing parenthesis `)`.
3. [Open the customers data](https://docs.couchbase.com/server/current/analytics/%5Fattachments/CommerceCustomers.json), select the contents of the page and copy it.
4. To complete the statement, return to the query editor and paste the JSON document in between the parentheses. You’ll need to add the closing parenthesis `)` if you used copy and paste to supply the `INSERT INTO` statement.
5. Run the query to populate the `customers` collection.
6. To verify that the collection contains data now, run the following query:  
```SQL++  
  SELECT * FROM customers LIMIT 1;  
```

Create another standalone collection for `orders`, which uses the **Field Name** `orderno` and a **Field Type** of **int** as a primary key. Use the [orders data](https://docs.couchbase.com/server/current/analytics/%5Fattachments/CommerceOrders.json) to select and copy the data for this collection, then populate it using another `INSERT INTO` statement.

> [!TIP]
> You can also populate standalone collections by importing data from a file. After you create a standalone collection, point to the collection name, and go to **More Options (⋮)** **Import Data to Collection** to upload a CSV, TSV, JSON, or JSONL file. You can configure import filters or create a new collection for your import.

## [](#travel-sample)Import the `travel-sample` Collections

The Couchbase `travel-sample` dataset is available to import from directly inside the Capella Analytics workbench. The `travel-sample` consists of 5 collections of JSON documents: `airline`, `airport`, `landmark`, `hotel`, and `route`.

To import the `travel-sample` into your Capella Analytics cluster:

1. In the explorer, click **Import**.
2. Click **Sample**.
3. Click **Import**.

Capella Analytics creates a new database, `travel-sample`, with the `inventory` scope and all 5 collections.

After the import finishes, you can choose to import sample queries to work with the `travel-sample` dataset.

## [](#beer-sample)Create Remote Collections for `beer-sample`

You can import the Couchbase `beer-sample` dataset into a Capella operational cluster or self-managed Couchbase Server cluster. This dataset consists of a single collection, which contains data on beers and breweries.

Set up [remote collections](../sources/manage-remote.md) to hold shadow copies of the `beer-sample` data in Capella Analytics. Use WHERE clauses to create multiple collections on Capella Analytics, instead of creating only a single collection to match what’s in your remote data source in your Capella operational cluster or Couchbase Server.

Any Capella Analytics collections that use a WHERE clause apply that clause on an ongoing basis to continuously filter your incoming data event stream. Only documents that meet the WHERE clause criteria are upserted into your Capella Analytics collection.

### [](#prep)Prepare to Ingest Data from the Remote System

> [!NOTE]
> Make sure the Capella operational cluster you want to use as a remote data source belongs to the same organization as your Capella Analytics cluster.

To prepare your Capella operational cluster for creating a remote collection in Capella Analytics:

1. [Import the beer-sample sample data.](../../cloud/clusters/data-service/import-data-documents.md#import-sample-data)

After you have imported the sample data, you can set up your Capella operational cluster as a remote data source in Capella Analytics.

### [](#remotecoll)Create a Data Source for Remote Data

1. In the Capella UI, click the Couchbase Capella icon and from the **Capella Analytics** tab select your cluster to open the workbench.
2. In the explorer, go to **Create** **Cluster**.
3. In the **Database Name** field, enter `remoteCapella`.
4. Click **Add Scope to New Cluster** to create a scope named `remoteBeer`.
5. Click **Create**.
6. In the explorer, go to **Create** **Data Link**.
7. Click **Couchbase Capella**.
8. Click **Continue**.
9. In the **Link Name** field, enter `capellaLink`.
10. Select the cluster where you imported the `beer-sample` dataset and click **Save & Continue**.  
Capella creates the link between your Capella Analytics cluster and your operational cluster.
11. Click **Create Linked Collection**.
12. In the lists, select your **remoteCapella** cluster and **remoteBeer** scope.
13. In the **Collection Name** field, enter the name for the first collection, `brewBelgium`.
14. In the **Configure Data Details** section, select the **beer-sample** bucket, and **\_default** scope and collection.
15. In the provided field, enter a WHERE clause for the documents in the collection to shadow:  
country = "Belgium"
16. Click **Create Collection**.
17. (Optional) Click **Create Another Collection** and use the following WHERE clause to shadow data for French beers and breweries:  
country = "France"
18. To start shadowing data from your Capella operational cluster in Capella Analytics, click **Connect Link**.  
> [!NOTE]  
> You’ll incur charges for usage after you connect this link.
19. Click **Yes, Continue**.
20. Close the link creation pane.
21. Verify that your `brewBelgium` collection now contains a shadow copy of the data sourced from Capella by running the following query, with your query context set to **remoteCapella** and **remoteBeer**:  
```SQL++  
  SELECT * FROM brewBelgium LIMIT 1;  
```

### [](#next-steps)Next Steps

You can create more collections using the same remote link to your Capella operational cluster.

In the explorer, expand **Links** and go to **More Options (⋮)** **Create Linked Collection** to add another collection. Use WHERE clauses to shadow different subsets of the data: `brewGermany` for `country = "Germany"`, `brewUS` for `country = "United States"` and so on.

You can also use the example DDL statements for creating remote Couchbase collections as guidelines for using SQL++ queries instead of the user interface controls. See the examples for [Create a Remote Couchbase Collection](../sqlpp/5%5Fddl%5Fremote.md#createcb).