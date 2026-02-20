---
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/fts/pages/fts-creating-index-specifying-advanced-settings.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:fts:fts-creating-index-specifying-advanced-settings.adoc[]
---

[View original HTML](/server/current/fts/fts-creating-index-specifying-advanced-settings.html)

# undefined

## [](#specifying-advanced-settings)Specifying Advanced Settings

Advanced settings can be specified by means of the **Advanced** panel. When opened, this appears as follows:

![fts advanced panel](_images/fts-advanced-panel.png) 

The following, interactive fields are displayed:

* **Default Type**: The default type for documents in this bucket. The default value is `_default`.
* **Default Analyzer**: The default analyzer to be used for this bucket. The default value is `standard`. A list of available options can be displayed and selected from, by means of the pull-down menu at the right-hand side of the field.
* **Default Date/Time Parser**: The default date/time parser to be used for this bucket. The default value is `dateTimeOptional`. A list of available options can be displayed and selected from, by means of the pull-down menu at the right-hand side of the field.
* **Default Field**: The default field for this bucket. the default value is `_all`.
* **Store Dynamic Fields**: When checked, ensures inclusion of field-content in returned results. When unchecked, no such inclusion occurs.
* **Index Dynamic Fields**: When checked, ensures dynamic fields are indexed. When unchecked, they are not indexed.