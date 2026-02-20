---
title: Creating Full Text Aliases
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/fts/pages/fts-create-index-aliases.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:fts:fts-create-index-aliases.adoc[]
---

[View original HTML](/server/current/fts/fts-create-index-aliases.html)

# Creating Full Text Aliases

> Full Text Alias is the name that can be used in place of the actual full text index name. You can perform the searches across multiple buckets and multiple scopes by means of index aliases. 

An index alias points to one or more Full Text Indexes or to additional aliases: its purpose is therefore somewhat comparable to that of a symbolic link in a filesystem. Queries on an index alias are performed on all ultimate targets, and merged results are provided.

The use of index aliases permits indirection in naming, whereby applications refer to an alias-name that never changes, leaving administrators free to change the identity of the real index pointed to by the alias.

This may be particularly useful when an index needs to be updated. To avoid down-time, a clone of the current index can be created, modified, and tested, while the current index remains in service.

Then, when the clone is ready, the existing alias can be retargeted so that the clone becomes the current index; and the (now) previous index can be removed.

The following process explains how to create an index alias in Couchbase:

Access the couchbase application. In the left pane, click **Search**. The Full Text Aliases panel is shown at the bottom of the page.

![fts full text aliases panel](_images/fts-full-text-aliases-panel.png) 

Now, click **\+ Add Alias** to add new alias. The Add Alias page opens.

![fts add alias screen](_images/fts-add-alias-screen.png) 

In the Add Alias page, add the alias name in the **Index Name** field. After that select one or more indexes from the **Target Indexes** list for which you want to add an alias. The selected index is highlighted in a separate color.

Finally, click **Create Index Alias**. The new index alias is added to the list in the Full Text Aliases panel.

![fts full text aliases page with alias](_images/fts-full-text-aliases-page-with-alias.png)