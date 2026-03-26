---
title: Classic Editor
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-creating-index-from-UI-classic-editor-dynamic.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.2@server:fts:fts-creating-index-from-UI-classic-editor-dynamic.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-creating-index-from-UI-classic-editor-dynamic.html)

# Classic Editor

> The classic editor is the most advanced tool where users can directly configure the index mapping with all capabilities. 

You can build the exact same index via the command line use the REST API, refer to [Creating a Dynamic Index via the REST API](fts-creating-index-from-REST-dynamic.md).

This section introduces index creations via a step by step walk through using the classic editor. The reader should be already familiar with the basic concepts of full-text search

This example [Creating a Dynamic Index](#main) covers creating an index that dynamically indexes every field in a collection.

# [](#main)Creating a Dynamic Index

This section describes creating and Index on a bucket's collection across **all fields in the a collection**.

This is equivalent to the [Creating a Legacy Index](fts-creating-index-from-UI-classic-editor-legacy.md#main).

To create the desired index through the Classic Editor:

* Access the **Couchbase Web Console** \> **Search** page.  
![fts search page](_images/fts-search-page.png)
* Click the **Add Index** link in the upper right of the **Couchbase Web Console** \> **Search** page.  
![fts add initial](_images/fts-add-initial.png)
* To define any index on which Full Text Search a unique name for the index in the **Index Name** field, on the upper-left. Note that only alphanumeric characters, hyphens, and underscores are allowed for index names and the first character of the name must be alphabetic.  
Enter **test\_dynamic** as the name of the Search index you are creating in the **Index Name** text-box.  
![fts index name dynamic](_images/fts-index-name-dynamic.png)
* Select the bucket **travel-sample** from the **Bucket** pull-down menu.  
Use the pull-down menu provided for the Bucket field, on the upper-right, and select a bucket that you are allowed to access to via the cluster's RBAC settings.  
![fts index name and bucket dynamic](_images/fts-index-name-and-bucket-dynamic.png)
* Select the checkbox **\[X\] Use non-default scope/collections**  
This allows your index to stream mutations from one or more non-default collections under the selected bucket and scope.  
![fts select dynamic scope collections](_images/fts-select-dynamic-scope-collections.png)
* You will see a newly visible pull-down menu provided for the **Scope** field, under the **\[X\] Use non-default scope/collections** checkbox, and select a bucket that you are allowed to access to via the cluster's RBAC settings.  
For this example leave the setting as **\_default** which which is used to migrate bucket based data into the collections paradigm.
* Under **Type Mapings**, unselect the checkbox **\[ \] default | dynamic**.  
This is required as this type mapping (the default mapping) is only valid for the <bucket>.\_default.\_default which is typically used to upgrade a 6.X server from a bucket into a more powerful collections paradigm. In this example we will do the equivlent but on a per collections basis.  
![fts uncheck default mapping](_images/fts-uncheck-default-mapping.png)
* Click on the button **\+ Add Type Mapping**

  * A new section with a **Collection** pull-down, **Analyzer** pull-down and a **\[ \] only index specified fields** checkbox will appear.  
  ![fts index menu1 nondefault empty](_images/fts-index-menu1-nondefault-empty.png)
  * Select **\_default** from the **Collection** pull-down, note the pull down will change to a text field prefilled with **\_default.\_default**  
  ![fts index menu1 geopoint filled](_images/fts-index-menu1-geopoint-filled.png)
  * Leave the **\[ \] only index specified fields** checkbox blank or unset.  
  This will index all fields in the scope **\_default** collection **\_default**, howver not this is not recommended for large production datasets.
  * Click on the blue **ok** at the right of the section to save this mapping.
* Save your index, left-click on the **Create Index** button near the bottom of the screen.  
This is all you need to specify in order to create a more advanced index for test and development. No further configuration is required.  
![fts index create button](_images/fts-index-create-button.png)
* If you subsequently Edit your Index it should look like the following:  
![fts edit index dynamic](_images/fts-edit-index-dynamic.png)

> [!NOTE]
> Indexing all fields as above indexes across all fields is not recommended for production environments since it creates indexes that may be unnecessarily large, and therefore insufficiently performant.

## [](#test-the-dynamic-index-with-a-simple-query)Test the Dynamic Index with a simple query

In the **Couchbase Web Console** \> **Search** page.

* Click on the index you just created (named "landmark-content-index") to expand the Index's controls.
* In the text area of the search box enter **+view +food +beach** this will search on all three keywords
* Click on the blue **Search** button. You will get documents from only collection landmark and due to the options you selected you will see highlighted words in your results.  
![fts index dynamic search](_images/fts-index-dynamic-search.png)
* Verify you have some results  
![fts index dynamic search results](_images/fts-index-dynamic-search-results.png)

# [](#advanced-index-settings-and-other-features-in-the-ui)Advanced Index Settings and Other Features in the UI

The complete range of available options for creating Search indexes for any production environment is covered here: [Creating Indexes](fts-creating-indexes.md).

Once you hit the **Create Index** button you will return to the **Couchbase Web Console** \> **Search** page (note, if you tested any index just access the **Couchbase Web Console** \> **Search** page again).

At this point, you are returned to the Full Text Search screen.

A new row now appears for the index you have just created. When left-clicked on, the row opens or expands as follows:

![fts new index progress](_images/fts-new-index-progress.png) 

## [](#index-build-progress)Index Build Progress

Once the new index has been built, it supports Full Text Searches performed by all available means: the Console UI, the Couchbase REST API, and the Couchbase SDK.

### [](#statistic-docs-processed)Statistic: docs processed

The percentage figure appears under the indexing progress column and represents the number of documents present in the index.

* On an initial build this may take a while to process all the documents.
* A mutation to an existing document will not increment this count (unless new items are added).

### [](#statistic-indexing-progress)Statistic: indexing progress

The percentage figure appears under the indexing progress column and is incremented in correspondence with the build-progress of the index. When 100% is reached, the index build is complete.

* However, search queries will be allowed as soon as the index is created, meaning partial results can be expected until the index build is complete.
* If later mutations com in the percentage may actually jump around as batches of documents are processed.
* If one or more of the nodes in the cluster running data service goes down and/or are failed over, indexing progress may show a value > 100%.

## [](#using-the-show-index-definition)Show Index Definition

This expandable section shows the JSON document that describes the current index configuration, as created by means of the user interface.

A checkbox **\[ \] Show curl command to modify this index definition** is set will wrap the index definition with a command line cURL syntax.

You can copy either variant (the cURL mode) and the definitions can be used via the Search REST API or any Couchbase SDK.

![fts show index definition](_images/fts-show-index-definition.png) 

## [](#using-the-index-definition-preview)Using the Index Definition Preview

The _Index Definition Preview_ appears to the right-hand side of the **Add Index** (or an **Edit Index**) screen.

Following index-definition, the upper portion may appear as follows:

![fts index definition preview](_images/fts-index-definition-preview.png) 

This preview (like the **Show Index Definition JSON** from the main Search page) consists of the JSON document that describes the current index configuration, as created by means of the user interface. By left-clicking on the **copy to clipboard** tab, the definition can be saved.

These definitions can be used via the Search REST API or any Couchbase SDK.

# [](#advanced-index-configuration-options)Advanced Index Configuration Options

The complete range of available options for creating Search indexes for any production environment is covered here: [Creating Indexes](fts-creating-indexes.md).