---
title: Classic Editor Examples
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-creating-indexes-common.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:fts:fts-creating-indexes-common.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-creating-indexes-common.html)

# Classic Editor Examples

# [](#classic-editor)Classic Editor

> A classic editor is an advanced tool where users can directly configure the index mapping. 

To quickly become familiarized with the Search service, try one of the step by step index creation (and query) examples against the `travel-sample` sample dataset:

* Collections

* Creating a **One Field Index** [via the UI](fts-creating-index-from-UI-classic-editor-onefield.md) (or [via the REST API](fts-creating-index-from-REST-onefield.md)), followed by a sample Search query.
* Creating a **Dynamic Index** [via the UI](fts-creating-index-from-UI-classic-editor-dynamic.md) (or [via the REST API](fts-creating-index-from-REST-dynamic.md)), followed by a sample Search query.
* Creating a **Geopoint Index** [via the UI](fts-creating-index-from-UI-classic-editor-geopoint.md) (or [via the REST API](fts-creating-index-from-REST-geopoint.md)), followed by a sample Search query.

Bucket Compatibility

Creating a **Legacy Index** [via the UI](fts-creating-index-from-UI-classic-editor-legacy.md) (or [via the REST API](fts-creating-index-from-REST-legacy.md)), followed by a sample Search query.

The above Legacy Index is used for compatibility after an upgrade from buckets to collections uses the old bucket style "**default \_mapping** which only works on the _default scope and \_default collection where buckets are upgraded into. The preferred method as of version 7.0 is shown in [Creating a Dynamic Index](fts-creating-index-from-UI-classic-editor-dynamic.md) above._ 

For a more detailed explanation of the available index creation, including index creation by means of the Couchbase REST API, refer to [Creating Search Indexes](fts-creating-indexes.md).

To install the `travel-sample` sample dataset, refer to [Install Sample Buckets with the UI ](../manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui).