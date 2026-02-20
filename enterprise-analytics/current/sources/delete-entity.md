---
title: Delete a Collection or Link
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sources/pages/delete-entity.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:enterprise-analytics:sources:delete-entity.adoc[]
---

[View original HTML](/enterprise-analytics/current/sources/delete-entity.html)

# Delete a Collection or Link

> This topic describes how you remove collections and links from Enterprise Analytics. 

## [](#remove-collection)Delete a Collection

You can delete any collection that you no longer need.

1. For a remote collection, [disconnect](connect-link.md#stop-stream) the collection’s link to stop the data event stream.
2. In the UI, point to the name of the collection and then choose **Delete**.

You can also use an SQL++ for Enterprise Analytics statement to delete a collection. See [DROP Statements](../sqlpp/5%5Fddl%5Fdrop.md).

## [](#remove-link)Delete a Link

1. For a remote link, [disconnect](connect-link.md#stop-stream) the link to stop the data event stream.
2. Delete every collection from the link.
3. In the UI, point to the name of the name of the link and then choose **⋮ (More)** **Delete**.

## [](#see-also)See Also

* [Manage Enterprise Analytics Databases](manage-databases.md)
* [Manage Enterprise Analytics Scopes](manage-scopes.md)