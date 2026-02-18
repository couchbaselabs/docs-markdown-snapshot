---
title: Manage Documents with the Capella UI
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/data-service/manage-documents.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/clusters/data-service/manage-documents.html)

# Manage Documents with the Capella UI

> The Couchbase Capella UI provides the Documents tool that you can use to view and edit documents. 

This page describes how you can manage documents in a Couchbase cluster using the Documents tool in the Capella UI.

> [!IMPORTANT]
> Permissions Required
> 
> To use the document editor in the Capella UI, you need the appropriate [project role](../../projects/project-roles.md).
> 
> * To _view_ the documents within a cluster, you must have the [Data Reader](../../projects/project-roles.md#project-cluster-data-reader) project role for the project containing the cluster.
> * To _view_, _create_, _edit_, and _delete_ documents in a cluster, you must have the [Data Writer](../../projects/project-roles.md#project-cluster-data-reader-writer) project role for the project containing the cluster.

## [](#accessing-documents-in-the-capella-ui)Accessing Documents in the Capella UI

You can use the **Documents** tool to view and manage documents in a cluster.

To open the **Documents** tool:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to use the **Documents** tool.
3. Go to **Data Tools** **Documents**.

## [](#retrieve-documents)Retrieve Documents

You can use the **Documents** tool to retrieve and view the individual documents contained within a bucket, scope, or collection on the cluster. The retrieved documents are summarized in a table format, with a row for each retrieved document. Document retrieval controls at the top of the summary control the retrieval and display of documents.

The **Documents** tool has the following controls:

* **Bucket**: A drop-down menu that displays the name of the bucket whose documents are shown. You can use the drop-down menu to select from a list of buckets in the current cluster.
* **Scope**: A drop-down menu that displays the name of the scope whose documents are shown. The `_default` scope is the default. You can use the drop-down menu to select from a list of all the scopes within the current bucket.
* **Collection**: A drop-down menu that displays the name of the collection whose documents are shown. The `_default` collection is the default. You can use the drop-down menu to select from a list of all the collections within the current scope.
* **Limit**: The maximum number of rows—​documents—​to retrieve and display at once.
* **Offset**: The number of documents in the entire set of the current bucket that is skipped, before display begins.
* **Filter By**: This field is enabled if the [Query Service](../../n1ql/query.md) is running on the cluster.  
You can toggle the following options in the **Filter By** field:

  * **ID**: Accepts the ID value of a specific document. Leave this field blank to retrieve documents based on **Limit** and **Offset**.
  * **ID Range**: Accepts the **Starting ID** and **Ending ID** values to specify the ID range.
  * **SQL++ WHERE**: Accepts a SQL++ query. A WHERE clause which determines the subset of documents to show.

## [](#view-and-edit-existing-documents)View and Edit Existing Documents

When you use **Bucket**, **Scope**, or **Collection**, the set of retrieved documents is automatically updated based on your selections.

To view and edit documents:

1. [Retrieve](#retrieve-documents) a set of documents.
2. When using **Limit**, **Offset**, **Filter BY**, or **SQL++ WHERE**, click **Get Documents** to retrieve a new set of documents based on your new configuration.
3. Click on a document name in the results area to view and edit the document.  
Toggle the following tabs:

| Tab          | Description                                                                                                                                                                                                                                                               |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **JSON**     | Comprises a series of key-value pairs sometimes expressed as name-value pairs. You can make modifications to key-values.                                                                                                                                                  |
| **Metadata** | View the document’s metadata. It’s not possible to edit a document’s metadata as Couchbase Capella generates it in association with each document when they’re saved. For more information, see [document metadata](../../../server/current/learn/data/data.md#metadata). |
4. Click **Save Document** to save your changes.

## [](#create-documents)Create Documents

To create a document:

1. Click **Create Document**.
2. Enter the **Document ID** and edit the **JSON** contents of the document.
3. Click **Save Document** to create the document.

## [](#delete-documents)Delete Documents

To delete a document:

1. [Retrieve](#retrieve-documents) the document to display it in the results area.
2. Click the Trash icon  at the end of the row on the right side.
3. In the confirmation field, type `delete`.
4. Click **Delete Document**.

## [](#related-links)Related Links

To import a set of JSON documents or a CSV file, see [Import Data with the Capella UI](import-data-documents.md).