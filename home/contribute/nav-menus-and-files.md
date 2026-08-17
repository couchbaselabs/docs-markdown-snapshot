---
title: Navigation Menus and Files
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/contribute/pages/nav-menus-and-files.adoc
  xref: xref:home:contribute:nav-menus-and-files.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/contribute/nav-menus-and-files.html)

# Navigation Menus and Files

> [!NOTE]
> This documentation is out of date

## [](#component-selector-menu)Component Selector Menu

The products and services listed in the custom component selector dropdown menu are provided by the _header-content.hbs_ template in the site's [UI project](https://github.com/couchbase/docs-ui).

## [](#component-version-selector-menu)Component Version Selector Menu

The component name and version numbers listed in the version selector menu are generated from the [title and version keys](component-configuration.md#config) in the _antora.yml_ file corresponding to that component version.

## [](#component-menu)Component Menu

A component menu is the navigation displayed on the left side of the page when a visitor enters the documentation for a component. This menu is created from the [Navigation Files](#nav-file) registered in that component's _antora.yml_ file. The order the files are registered is the order their contents are displayed in the menu.

### [](#breadcrumbs)Breadcrumbs

The breadcrumbs listed at the top of a page are computed from the parent entry link text in the navigation file.

## [](#on-this-page-sidebar)On This Page Sidebar

A page's [heading 2 section titles](pages.md#document-sections) are displayed in the **On This Page** sidebar located on the right side of the page.

## [](#nav-file)Navigation Files

When you want visitors to locate a page using the [Component Menu](#component-menu), you must add a cross reference (`xref`) to that page in the appropriate navigation file. A navigation file can also include links to external URLs and other content, such as icons and normal text.

### [](#requirements-best-practices-and-styles)Requirements, Best Practices, and Styles

* A module can have no navigation file, one navigation file, or many navigation files.
* If a module does have one or more navigation files, store the file(s) at the base of the module, e.g., _modules/ROOT/nav.adoc_, _modules/contribute/nav.adoc_.
* In order to be published in a component menu, a navigation file must be registered in a component descriptor (_antora.yml_).
* A navigation file must use the AsciiDoc file extension and is typically named `nav.adoc`.
* A navigation file must contain at least one unordered AsciiDoc list.
* The Couchbase documentation starts each list with a category title. See [Update a Navigation File](update-nav.md) to learn how to create category titles and list items.

  * Use title case for category titles. Write "and" as an ampersand (**&**).
* Use the cross reference macro (`xref`) to link to documentation pages. See [Xrefs](update-nav.md#xrefs) for navigation xref and link text examples.

  * Use title case for the link text in list items. Write "and" as **and**.

## [](#learn-more)Learn More

[Update a navigation file](update-nav.md).