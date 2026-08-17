---
title: Manage Documents in the Couchbase Web Console
description: Couchbase Web Console provides a graphical interface that you can
  use to view and edit documents.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/manage/pages/manage-documents/manage-documents.adoc
  xref: xref:7.6@server:manage:manage-documents/manage-documents.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/manage/manage-documents/manage-documents.html)

# Manage Documents in the Couchbase Web Console

> Couchbase Web Console provides a graphical interface that you can use to view and edit documents. 

## [](#access-the-documents-workbench)Access the Documents Workbench

You can use the **Documents** workbench to view and manage documents in a database.

![The Documents workbench with documents displayed](../_images/manage-ui/documentsScreenWithDocuments.png) 

To display the **Documents** workbench, do one of the following:

* In the Couchbase Web Console, choose **Documents** **Workbench**.
* Alternatively, choose **Buckets**, then click the **Documents** link for any bucket, scope, or collection.

## [](#retrieve-documents)Retrieve Documents

You can use the **Documents** workbench to retrieve and view the individual documents contained within a bucket, scope, or collection on the database. The retrieved documents are summarized in a table format, with a row for each retrieved document. Document retrieval controls at the top of the summary control the retrieval and display of documents.

The **Documents** workbench has the following controls:

* **Keyspace**: A set of three related drop-down menus:

  * A drop-down menu that displays the name of the bucket whose documents are shown. You can use the drop-down menu to select from a list of buckets in the current database.
  * A drop-down menu that displays the name of the scope whose documents are shown. The `_default` scope is the default. You can use the drop-down menu to select from a list of all the scopes within the current bucket.
  * A drop-down menu that displays the name of the collection whose documents are shown. The `_default` collection is the default. You can use the drop-down menu to select from a list of all the collections within the current scope.
* **Limit**: The maximum number of rows (documents) to retrieve and display at once.
* **Offset**: The number of documents in the entire set of the current bucket that is skipped, before display begins.
* **Document ID**: Accepts the ID value of a specific document. Leave this field blank to retrieve documents based on **Limit** and **Offset**.
* **show range**: Enables you to enter starting ID and ending ID values to specify a range of ID values.
* **N1QL WHERE**: Accepts a SQL++ query — specifically, a WHERE clause which determines the subset of documents to show.

To retrieve a set of documents:

1. Use the **Keyspace** drop-down menus to specify the location of the documents you want to view. The set of retrieved documents is automatically updated based on your selections.
2. (Optional) Use **Limit**, **Offset**, **Document IT**, or **N1QL WHERE** to specify a set of documents, then click **Retrieve Docs** to retrieve the documents based on your configuration.
3. (Optional) To view successive sets of documents, use the **next batch >** and **< prev batch** controls.

## [](#view-and-edit-existing-documents)View and Edit Existing Documents

To view and edit a document:

1. [Retrieve](#retrieve-documents) a set of documents.
2. Click on a document name, or click the pencil icon  next to the document name.
3. (Optional) Click **Data** to view the document data. This comprises a series of key-value pairs in JSON format, which may be nested. You can make modifications to the document data.  
![The Edit Document dialog showing document data](../_images/manage-ui/editDocumentData.png)
4. (Optional) Click **Metadata** to view the [document metadata](../../learn/data/data.md#metadata). It's not possible to edit a document's metadata. Couchbase Server generates metadata when the document is saved.  
![The Edit Document dialog showing document metadata](../_images/manage-ui/editDocumentMetaData.png)
5. Click **Save** to save your changes.

## [](#edit-existing-documents-in-spreadsheet-view)Edit Existing Documents in Spreadsheet View

When spreadsheet view is enabled, you can edit an existing document directly in the results area.

To edit existing documents in spreadsheet view:

1. [Retrieve](#retrieve-documents) the document to display it in the results area.
2. Click **enable field editing** so that the switch is enabled.
3. Edit any of the existing fields in the document.
4. Click the save icon  next to the document name.

## [](#copy-existing-documents)Copy Existing Documents

To create a copy of an existing document:

1. [Retrieve](#retrieve-documents) the document to display it in the results area.
2. Click the copy icon  next to the document name.
3. Enter a document **ID** and edit the contents of the document.
4. Click **Save** to create the document.

## [](#create-new-documents)Create New Documents

To create a new document:

1. Click **Add Document**.
2. Enter a document **ID** and edit the contents of the document.
3. Click **Save** to create the document.

## [](#delete-documents)Delete Documents

To delete a document:

1. [Retrieve](#retrieve-documents) the document to display it in the results area.
2. Click the trash icon  next to the document name.
3. Click **Continue** to delete the document.

## [](#related-links)Related Links

To import a set of JSON documents or a CSV file, see [Import Documents with the Couchbase Web Console](../import-documents/import-documents.md).