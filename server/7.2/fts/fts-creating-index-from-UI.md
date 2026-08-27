---
title: Creating Index from UI
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-creating-index-from-UI.adoc
  xref: xref:7.2@server:fts:fts-creating-index-from-UI.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-creating-index-from-UI.html)

# Creating Index from UI

The user interface for Full Text Search is provided by the Couchbase Web Console. To proceed, you must have permission to log into the console, create indexes, and perform searches. For information on Role-Based Access Control, see Authorization.

The example provided in this section assumes that you have also loaded the `travel-sample bucket:` you will perform your Full Text Search operations on the data in this bucket. For instructions on how to load this sample bucket, see [Sample Buckets](../manage/manage-settings/install-sample-buckets.md).

Once you have the appropriate credentials and have loaded the `travel-sample bucket`, access the Couchbase Web Console by typing `http://localhost:8094` into the address field at the top of your browser and then hitting return.

The login screen appears as follows:

![fts login screen](_images/fts-login-screen.png) 

Enter your username and password, and left-click on the **Sign In** button. The Couchbase Web Console now appears, with the Dashboard for the cluster displayed:

![fts console initial](_images/fts-console-initial.png) 

> [!NOTE]
> The appearance of the main panel of the Dashboard varies in accordance with customizations that have been performed. For information, see [Manage Statistics](../manage/manage-statistics/manage-statistics.md).

To access the Full Text Search screen, left-click on the **Search** tab in the navigation bar on the left-hand side:

![fts select search tab](_images/fts-select-search-tab.png) 

The Full Text Search screen now appears as follows:

![fts fts console initial](_images/fts-fts-console-initial.png) 

The console contains areas for displaying indexes and aliases: but both are empty since none has yet been created.

## [](#add-index)Add Index

To create an index, left-click on the **Add Index** button towards the right-hand side.

The Add Index screen appears:

![fts add index initial](_images/fts-add-index-initial.png) 

To define a basic index on which Full Text Search can be performed, begin by entering a unique name for the index into the Name field, on the upper-left: for example, travel-sample-index. (Note that only alphanumeric characters, hyphens, and underscores are allowed for index names. Also note that the first character of the name must be alphabetic.) Then, use the pull-down menu provided for the Bucket field, at the upper-right, to specify the travel-sample bucket:

![fts index name and bucket](_images/fts-index-name-and-bucket.png) 

This is all you need to specify to create a basic index for test and development. No further configuration is required.

> [!NOTE]
> Such default indexing is not recommended for production environments since it creates indexes that may be unnecessarily large, and therefore insufficiently performant.

### [](#using-non-default-scope-collections)Using Non Default Scope/Colle

![fts select non default scope collections](_images/fts-select-non-default-scope-collections.png) 

Select this checkbox if you want the index to stream data from a non-default scope and/or non-default collection(s) on the source bucket.

To specify the non-default scope, click the scope drop-down list and select the required scope.

![fts non default scope collections1](_images/fts-non-default-scope-collections1.png) 

To review the wide range of available options for creating indexes appropriate for production environments, see Creating Indexes.

To save your index, left-click on the **Create Index** button near the bottom of the screen:

At this point, you are returned to the Full Text Search screen. In the Full Text Indexes panel, a row now appears for the index you have created. When left-clicked on, the row opens as follows:

![fts new index progress](_images/fts-new-index-progress.png) 

> [!NOTE]
> This percentage figure appears under the indexing progress column and is incremented in correspondence with the build-progress of the index. When 100% is reached, the index build is said to be complete. However, search queries will be allowed as soon as the index is created, meaning partial results can be expected until the index build is complete.

Once the new index has been built, it supports Full Text Searches performed by all available means: the Console UI, the Couchbase REST API, and the Couchbase SDK.

> [!NOTE]
> If one or more of the nodes in the cluster running data service goes down and/or are failed over, indexing progress may show a value > 100%.