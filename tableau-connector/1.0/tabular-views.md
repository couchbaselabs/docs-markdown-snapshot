---
title: Couchbase Analytics Tabular Views
editUrl: https://github.com/couchbase/docs-tableau/edit/release/1.0/modules/ROOT/pages/tabular-views.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:1.0@tableau-connector::tabular-views.adoc[]
---

[View original HTML](/tableau-connector/1.0/tabular-views.html)

# Couchbase Analytics Tabular Views

## [](#couchbase-analytics-tabular-views)Couchbase Analytics Tabular Views

Tableau requires its data sources to be in tabular form, accessible by SQL. Couchbase allows users to create tabular relational views from their datasets that can then be used with Tableau operations. The examples in this guide make use of the built-in travel-sample dataset that ships with Analytics tabular views.

### [](#loading-the-sample-bucket)Loading the Sample Bucket

The bucket for this can be set up on your server instance through the Couchbase Web Console. Load the travel-sample bucket by logging in to the console, going to **Buckets** **Load a sample Bucket**, and selecting **travel-sample**.

![Load Travel Sample Bucket](_images/load-travel-sample.png) 

### [](#viewing-analytics-collections)Viewing Analytics Collections

The travel-sample bucket comes with Analytics collections and views enabled. To view the collections, go to the **Analytics** menu in the Couchbase Web Console to see the Analytics collections created for the inventory scope.

![Travel Sample Analytics Collections](_images/view-analytics-collections.png)