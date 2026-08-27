---
title: Manage Index Lifecycle
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-manage-index-lifecycle.adoc
  xref: xref:7.2@server:fts:fts-manage-index-lifecycle.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-manage-index-lifecycle.html)

# Manage Index Lifecycle

Full Text Indexes, once created can be cloned, edited and/or deleted. They are accessed from the **Search** tab: left-click on this to display the **Full Text Search** panel, which contains a tabular presentation of currently existing indexes, with a row for each index.

(See [Searching from the UI](fts-searching-from-the-UI.md) for a full illustration.)

To manage an index, left-click on its row. The row expands, as follows:

![fts index management ui](_images/fts-index-management-ui.png) 

## [](#edit-index)Edit Index

* **Edit** brings up the **Edit Index** screen, which allows the index to be modified. Saving modifications cause the index to be rebuilt.

"Quick Edit" that goes to the quick editor for an index definition also results in the same functionalities.

> [!NOTE]
> Both the **Edit Index** and **Clone Index** screens are in most respects the same as the **Add Index** screen, which was itself described in [Searching from the UI](fts-searching-from-the-UI.md).

## [](#delete-index)Delete Index

* **Delete** causes the current index to be deleted. Index deletion is an asynchronous process run in the background.

## [](#clone-index)Clone Index

* **Clone** button click brings up the **Clone Index** screen, which allows a copy of the current index to be modified as appropriate and required, and saved under a new name.