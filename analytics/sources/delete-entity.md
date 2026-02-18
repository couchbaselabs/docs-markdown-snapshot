---
title: Delete a Collection or Link
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sources/pages/delete-entity.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/analytics/sources/delete-entity.html)

# Delete a Collection or Link

> This topic describes how you remove collections and links from Capella Analytics. 

## [](#remove-collection)Delete a Collection

You can delete any collection that you no longer need.

1. For a remote collection, [disconnect](connect-link.md#stop-stream) the collection’s link to stop the data event stream.
2. In the UI, move your cursor over the name of the collection and then choose **Delete**.

You can also use an SQL++ for Capella Analytics statement to delete a collection. See [DROP Statements](../sqlpp/5%5Fddl%5Fdrop.md).

## [](#remove-link)Delete a Link

1. For a remote link, [disconnect](connect-link.md#stop-stream) the link to stop the data event stream.
2. Delete every collection from the link.
3. In the UI, move your cursor over the name of the link and then choose **⋮ (More)** **Delete**.

## [](#see-also)See Also

* [Manage Capella Analytics Services Databases](manage-databases.md)
* [Manage Capella Analytics Services Scopes](manage-scopes.md)