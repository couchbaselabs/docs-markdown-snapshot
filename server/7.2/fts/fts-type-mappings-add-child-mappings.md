---
title: Add Child Mapping
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-type-mappings-add-child-mappings.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:fts:fts-type-mappings-add-child-mappings.adoc[]
---

[View original HTML](/server/7.2/fts/fts-type-mappings-add-child-mappings.html)

# Add Child Mapping

The option **insert child mapping** specifies a document-field whose value is a JSON object. Selecting this option displays the following:

![fts type mappings child mapping dialog](_images/fts-type-mappings-child-mapping-dialog.png) 

The following interactive field and checkbox are displayed:

* **{}**: The name of a field whose value is a JSON object. Note that an analyzer for the field, by means of the pull-down menu.
* **only index specified fields**: When checked, only fields explicitly specified are added to the index. Note that the JSON object specified as the value for **{}** has multiple fields of its own. Checking this box ensures that all or a subset of these can be selected for indexing.

When completed, this panel might look as follows (note that `reviews` is a field within the `hotel`\-type documents of the `travel-sample` bucket whose value is a JSON object):

![fts type mappings child mapping dialog complete](_images/fts-type-mappings-child-mapping-dialog-complete.png) 

Save by left-clicking **OK**. The field is now displayed as part of the `hotel` type mapping. Note that by hovering over the `reviews` row with the mouse, the **Edit** and **+** buttons are revealed: the **+** button is present because `reviews` is an object that contains child-fields; which can now themselves be individually indexed. Left-click on this, and a child-field, such as `content`, can be specified:

![fts type mappings child mapping add field](_images/fts-type-mappings-child-mapping-add-field.png)