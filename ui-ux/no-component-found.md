---
title: Empty States
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-style-guide/edit/main/ui-ux/modules/ROOT/pages/no-component-found.adoc
  xref: xref:ui-ux::no-component-found.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ui-ux/no-component-found.html)

# Empty States

When the user has not yet created a database component, such as an index or a bucket, the UI should display a message stating **No <components> found** or **No <components>**:

![The Search Service Data Tools. The user has not created a Search index or index alias yet, so two messages appear stating 'No search indexes found' and 'No index aliases found'.](_images/NoComponentFound.png) 

Pluralize the component name and do not add a period at the end of "found."

The component name should exactly match the title of the page, or the title of the section where the empty state appears.

If possible and space allows, add a short message underneath that either tells the user:

* What the component is that they can create on this page. For example, a very brief explanation of App Services.
* What they can do to display a new component in the empty state. For example, `Configure a new type mapping using your document schema to add it to your Search index.`