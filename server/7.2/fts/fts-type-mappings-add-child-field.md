---
title: Add Child Field
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-type-mappings-add-child-field.adoc
  xref: xref:7.2@server:fts:fts-type-mappings-add-child-field.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-type-mappings-add-child-field.html)

# Add Child Field

The option **insert child field** allows a field to be individually included for (or excluded from) indexing, provided that it contains a single value or an array rather than a JSON object. Selecting this option displays the following:

![fts type mappings child field dialog](_images/fts-type-mappings-child-field-dialog.png) 

The interactive fields and checkboxes are:

* [Field Name](fts-type-mappings-add-child-field-field-name.md)
* [Field Type](fts-type-mappings-add-child-field-field-type.md)
* [Field Searchable As](fts-type-mappings-add-child-field-field-searchable-as.md)
* [Analyzer](fts-type-mappings-add-child-field-analyzer.md)
* [Index](fts-type-mappings-add-child-field-index.md)
* [Store](fts-type-mappings-add-child-field-store.md)
* [Include term vectors](fts-type-mappings-add-child-field-include-term-vectors.md)
* [Include in \_all field](fts-type-mappings-add-child-field-include-in-all-field.md)
* [DocValues](fts-type-mappings-add-child-field-docvalues.md)

The dialog, when completed, might look as follows:

![fts type mappings child field dialog complete](_images/fts-type-mappings-child-field-dialog-complete.png) 

Left-click on **OK**. The field is saved, and its principal attributes displayed on a new row:

![fts type mappings child field saved](_images/fts-type-mappings-child-field-saved.png) 

Note that when this row is hovered over with the mouse, an **Edit** button appears, whereby updates to the definition can be made.