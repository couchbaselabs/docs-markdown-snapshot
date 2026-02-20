---
title: Searching Full Text Indexes/Aliases
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-searching-full-text-indexes-aliases.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:fts:fts-searching-full-text-indexes-aliases.adoc[]
---

[View original HTML](/server/7.2/fts/fts-searching-full-text-indexes-aliases.html)

# Searching Full Text Indexes/Aliases

> Full Text indexes, are available under the **Search** tab of the Couchbase Web Console. 

Full Text indexes are special-purpose indexes that contain targets derived from the textual contents of the documents within one or more buckets or collections from the buckets. For more information about different types of indexes, see [Indexes](../learn/services-and-indexes/indexes/indexes.md).

You can access the Full Text Indexes from the **Search** tab. Left-click on this to display the **Full Text Search** panel, which contains a tabular presentation of currently existing indexes, with a row for each index. (See [Searching from the UI](fts-searching-from-the-UI.md) for a full illustration.)

On the same **Search** tab, you can create aliases for one or more indexes. So, if you perform the searches on the the aliases, you can get the result not just from one index but from more indexes associated with the aliases.

To manage an index, left-click on its row. The row expands, as follows:

![fts index management ui](_images/fts-index-management-ui.png) 

To manage alias, left-click on the alias row. The row expands, as follows:

![fts alias management ui](_images/fts-alias-management-ui.png) 

The following buttons are displayed:

* **Search** searches the specified term in the designated index or alias.
* **Delete** causes the current index to be deleted.
* **Clone** brings up the **Clone Index** screen, which allows a copy of the current index to be modified as appropriate and saved under a new name.
* **Edit** brings up the **Edit Index** screen, which allows the index to be modified. Saving modifications cause the index to be rebuilt.  
> [!NOTE]  
> Both the **Edit Index** and **Clone Index** screens are in most respects the same as the **Add Index** screen, which was itself described in [Searching from the UI](fts-searching-from-the-UI.md).