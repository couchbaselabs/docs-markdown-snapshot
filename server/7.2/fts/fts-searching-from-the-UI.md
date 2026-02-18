---
title: Searching from the UI
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-searching-from-the-UI.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/fts/fts-searching-from-the-UI.html)

# Searching from the UI

> Full Text Search can be performed from the Couchbase Web Console. 

## [](#prerequisites)Prerequisites

The user interface for Full Text Search is provided by the Couchbase Web Console.

* Ensure that Couchbase Server has the Search service appropriately enabled. The service must be enabled for a given node as part of that node’s initial configuration. Refer to Create a Cluster for information.
* You must have permission to log into the console, load sample data, create indexes, create search indexes, and perform searches. For information on Role-Based Access Control, see [Authorization](../learn/security/authorization-overview.md).
* The example(s) provided assume that you have can load or have loaded the `travel-sample` dataset. You will perform your Search operations on the data under this bucket. For instructions on how to load this sample dataset, see [Sample Buckets](../manage/manage-settings/install-sample-buckets.md).
* The Couchbase Web Console by accessing `http://localhost:8091` or if remote `http://${CB_HOSTNAME}:8091` where **CB\_HOSTNAME** is an environment variable set to a FQDN or an IP address for a node on your Couchbase cluster.

## [](#fts-quick-start)Access the Full Text Search User Interface

To access the **Full Text Search** screen, left-click on the **Search** tab, in the navigation bar at the left-hand side:

![fts select search tab](_images/fts-select-search-tab.png) 

The **Full Text Search** screen now appears, as follows:

![fts search page](_images/fts-search-page.png) 

The console contains areas for the display of _indexes_ and _aliases_: but both are empty, since none has yet been created.

## [](#fts%5Fensure%5Fthere%5Fis%5Fan%5Findex)Make sure you have a Search index

If you don’t have a Search index already you could create one against `travel-sample` as follows:

* Creating a **One Field Index** [via the UI](fts-creating-index-from-UI-classic-editor-onefield.md) or [via the REST API](fts-creating-index-from-REST-onefield.md).
* Creating a **Dynamic Index** [via the UI](fts-creating-index-from-UI-classic-editor-dynamic.md) or [via the REST API](fts-creating-index-from-REST-dynamic.md).
* Creating a **Geopoint Index** [via the UI](fts-creating-index-from-UI-classic-editor-geopoint.md) or [via the REST API](fts-creating-index-from-REST-geopoint.md).

The instructions provided will create an index named something like **travel-sample-index**, **test\_dynamic**, or **test\_geopoint** all indexes will work (the final one will also have the ability to search against geopoints).

## [](#Performing-Queries)Perform a Query

To perform a query, simply type a term into the interactive text-field that appears to the left of the **Search** button on the row for the index you have created. For example, `restaurant`. Then, left-click on the **Search** button:

![fts ui search for term](_images/fts-ui-search-for-term.png) 

A **Search Results** page now appears, featuring documents that contain the specified term:

![fts ui search results page](_images/fts-ui-search-results-page.png) 

By left-clicking on any of the displayed document IDs, you bring up a display that features the entire contents of the document.

## [](#advanced-query-settings-and-other-features-in-the-ui)Advanced Query Settings and Other Features in the UI

On the **Search Results** page, to the immediate right of the **Search** button, at the top of the screen, appears the **show advanced query settings** checkbox. Check this to display the advanced settings:

![fts advanced query settings](_images/fts-advanced-query-settings.png) 

Three interactive text-fields now appear underneath the **Search** panel: **Timeout (msecs)**, **Consistency Level**, and **Consistency Vector**. Additionally, the **JSON for Query Request** panel displays the submitted query in JSON format. Note the **show command-line curl example** checkbox, which when checked, adds to the initial JSON display, to form a completed curl command:

![fts ui curl example](_images/fts-ui-curl-example.png) 

This example can be copied by means of the **Copy to Clipboard** button, pasted (for example) into a standard console-window, and executed against the prompt. This feature therefore provides a useful means of extending experiments initially performed with the UI into a subsequent console-based, script-based, or program-based context. (Note, however, that the addition of credentials for authentication are required for execution of the statement outside the context of the current session within Couchbase Web Console. See [Searching with the REST API](fts-searching-with-curl-http-requests.md) for an example.)

Note also the **Show Scoring** checkbox that appears prior to the entries in the **Results for travel-sample-index** panel. When this is checked, scores for each document in the list are provided. For example:

![fts ui query scores display](_images/fts-ui-query-scores-display.png) 

Finally, note the **query syntax help** link that now appears under the **Search** interactive text-field:

![fts query syntax help link](_images/fts-query-syntax-help-link.png) 

This link takes the user to the documentation on [Supported Queries](fts-supported-queries.md). Such a query can be specified in the **Search** interactive text-field, thereby allowing a search of considerable complexity to be accomplished within Couchbase Web Console.

> [!NOTE]
> Any supported query can be executed from the UI, meaning the UI can accept a valid string (query string syntax) or a JSON object conforming to a supported syntax (query or search request). However the result set will only contain document IDs along with the requested fields and scores (if applicable). Any array positions or facets' results will _NOT_ be displayed.