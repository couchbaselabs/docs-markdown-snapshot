---
title: Comparing the Classic Editor, Quick Editor, and the Search REST API
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-creating-index-from-UI-difference-between-classic-quick-editor.adoc
  xref: xref:7.2@server:fts:fts-creating-index-from-UI-difference-between-classic-quick-editor.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-creating-index-from-UI-difference-between-classic-quick-editor.html)

# Comparing the Classic Editor, Quick Editor, and the Search REST API

To perform a Full Text Search, you can create indexes using one of the following methods:

## [](#classic-editor)Classic Editor

To create an index, left-click on the **Add Index** button to invoke the Classic Editor.

![fts add index initial](_images/fts-add-index-initial.png) 

## [](#quick-editor)Quick Editor

To quickly edit an index, left-click on the **Quick Edit** button towards the right-hand side on the Full Text Indexes panel to invoke the Quick Editor.

![fts quick edit screen](_images/fts-quick-edit-screen.png) 

## [](#the-differences)The Differences

* The Classic Editor

  * Exposes the most advanced creation tool in which users directly configure the full range of index mapping options.
  * Intended for power users who are already familiar with the concepts of full-text search.
* The Quick Editor

  * The Quick Editor allows users to configure the mapping by working with sample documents and higher-level abstractions.
  * The Quick Editor it does not support all of the advanced options of the Classic Editor.
  * The Quick Editor is intended for new users who are still learning about full-text search.
* The Search REST API

  * Allows users to instantly configure indexes via JSON payloads.
  * Good for exporting, importing, and porting Search index definitions.
  * Complex syntax typically precludes editing outside of one of the UI editors.