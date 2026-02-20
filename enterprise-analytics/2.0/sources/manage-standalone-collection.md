---
title: Set Up a Standalone Collection
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/sources/pages/manage-standalone-collection.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:2.0@enterprise-analytics:sources:manage-standalone-collection.adoc[]
---

[View original HTML](/enterprise-analytics/2.0/sources/manage-standalone-collection.html)

# Set Up a Standalone Collection

> You can gather documents from one or more existing Enterprise Analytics collections into a standalone collection. You customize the content of your standalone collections by querying other collections. 

> [!TIP]
> For an example of creating standalone collections and populating them using queries, see [Import the travel-sample Collections](../intro/connecting-to-data-sources.md).

## [](#prerequisites)Prerequisites

Role

To use the Enterprise Analytics UI to setup a standalone collection, you need the `**Enterprise Analytics Access**` role along with specific privileges.

Primary key

You must identify a primary key and its data type when you set up a standalone collection, so you must be familiar with the data you plan to insert into the collection. You supply the primary key as the name of the corresponding field or key in the data and its data type. Each document inserted into the collection must have a field with this name and a value of this type.

As another option, you can choose to have Enterprise Analytics auto-generate values for the primary key. You supply a name for the primary key and a data type of `UUID`. For each document inserted into the collection, Enterprise Analytics generates a universally unique identifier and adds it with this key.

## [](#create-standalone)Create a Standalone Collection

To create a standalone collection:

1. In the UI, select the **Workbench** tab.
2. Click **\+ standalone collection**.
3. In the **Collection Name** field, enter a name for the collection.
4. In the **database.scope** list, select a **Database** and the relevant **Scope** gets updated by default, or verify the supplied database and scope if you’re adding it to a specific scope. If you do not want to specify the primary key, make sure **Auto Generate UUID** is selected. If you want to specify the primary key, clear **Auto Generate UUID**, add the name in the **Name** field, select the type and click **Save**.
5. Click **Save**.

## [](#work-with-a-standalone-collection)Work with a Standalone Collection

Standalone collections give you the flexibility to build a new dataset to store in Enterprise Analytics by querying other collections.

For example, you can copy in data from an external collection. Or, you can build a separate, long-lasting archive for documents from a remote Couchbase collection by periodically adding timestamped deltas.

* To populate a standalone collection, you can use queries to `INSERT INTO`, `COPY INTO`, and otherwise select data from other collections.
* To manipulate the documents in the standalone collection to meet your needs, you use queries to `SELECT`, `INSERT INTO`, `UPSERT INTO`, `DELETE`, and so on.

For more information about using these SQL++ statements to write queries in Enterprise Analytics, see [DML Statements](../sqlpp/5%5Fdml.md).

## [](#view-metadata-for-a-collection)View Metadata for a Collection

Each time you add a collection, Enterprise Analytics records its metadata in the `System.Metadata.Dataset` collection. To view metadata for a collection, query this system collection. See [Querying Metadata](../sqlpp/5%5Fddl%5Fmetadata.md).

## [](#see-also)See Also

* [Connecting to Data Sources](../intro/connecting-to-data-sources.md)
* [Query and Explore with the Workbench](../query/workbench.md)
* [DML Statements](../sqlpp/5%5Fdml.md)