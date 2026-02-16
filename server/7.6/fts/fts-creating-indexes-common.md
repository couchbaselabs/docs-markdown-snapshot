[View original HTML](/server/7.6/fts/fts-creating-indexes-common.html)

# [](#classic-editor)Classic Editor

> A classic editor is an advanced tool where users can directly configure the index mapping. 

To quickly become familiarized with the Search service, try one of the step by step index creation (and query) examples against the `travel-sample` sample dataset:

* Collections

* Creating a **One Field Index** [via the UI](#fts-creating-index-from-UI-classic-editor-onefield.adoc) (or [via the REST API](../search/create-search-index-rest-api.md)), followed by a sample Search query.
* Creating a **Dynamic Index** [via the UI](../search/create-search-index-ui.md) (or [via the REST API](../search/create-search-index-rest-api.md)), followed by a sample Search query.
* Creating a **Geopoint Index** [via the UI](../search/geo-search-ui.md) (or [via the REST API](../search/geo-search-rest-api.md)), followed by a sample Search query.

Bucket Compatibility

Creating a **Legacy Index** [via the UI](../search/create-search-index-ui.md) (or [via the REST API](../search/create-search-index-rest-api.md)), followed by a sample Search query.

The above Legacy Index is used for compatibility after an upgrade from buckets to collections uses the old bucket style "**default \_mapping** which only works on the _default scope and \_default collection where buckets are upgraded into. The preferred method as of version 7.0 is shown in [Creating a Dynamic Index](../search/create-search-index-ui.md) above._ 

For a more detailed explanation of the available index creation, including index creation by means of the Couchbase REST API, refer to [Creating Search Indexes](../search/create-search-indexes.md).

To install the `travel-sample` sample dataset, refer to [Install Sample Buckets with the UI ](../manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui).