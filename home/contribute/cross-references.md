---
title: Cross References
editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/contribute/pages/cross-references.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:home:contribute:cross-references.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/contribute/cross-references.html)

# Cross References

To create links between pages inside the Couchbase Documentation, you must use the cross reference (xref) macro.

You need the resource ID of the page you want to link to before you can create an xref. The number of attributes you need to specify in the resource ID depends on where the page you want to link to is located in relation to your current page. Closer pages need fewer attributes.

For a good overview about resource IDs, see [the Antora documentation](https://docs.antora.org/antora/latest/page/resource-id-coordinates/).

To understand some of the key terms associated with resource IDs and creating xrefs, see [About Couchbase Documentation Repositories](repositories.md#dir-structure).

## [](#link-to-a-page-in-the-same-module)Link to a Page in the Same Module

A page is in the same module as another page if they're in the same `<module-name>/pages` folder.

To link to a page in the same module as the current page, all you need to know is the page's filename.

Start with the `xref:` macro, and add the full filename, including the extension. End with a set of square brackets (`[]`). Put text inside the square brackets to add link text, or leave it blank to use the title of the file.

For example:

```asciidoc
xref:name-of-file.adoc[link text]
```

To use an example from this Writer's Guide, to link to the `basics.adoc` file, which is in the same module as this page on cross references, you would write:

```asciidoc
xref:basics.adoc[This links to the AsciiDoc Basics page].
```

It would render in the finished documentation as:

[This links to the AsciiDoc Basics page](basics.md).

### [](#link-to-a-page-in-the-same-module-but-in-a-topic-folder)Link to a Page in the Same Module But in a Topic Folder

If you want to link to a page that's inside a topic folder, or a subfolder of the `<module-name>/pages` folder, you just need to add the folder name, followed by a backslash (`/`) in front of the file name.

For example:

```asciidoc
xref:concept/index.adoc[Key Concepts]
```

### [](#link-to-a-page-in-the-same-module-but-in-a-different-version)Link to a Page in the Same Module But in a Different Version

If you want to link to a page that's inside the same `<module-name>/pages` folder but in a different version of the documentation, add the version number, followed by an `@`, in front of the filename.

For example:

```asciidoc
xref:3.3@error-handling.adoc#message-list[error messages]
```

## [](#link-to-a-page-in-a-different-module-but-the-same-component)Link to a Page in a Different Module But the Same Component

To link to a page in the same component as the current page, but in a different module, you need to know the filename of the page and the module name.

Add the module name (folder name), followed by a colon (`:`), in front of the filename.

For example:

```asciidoc
xref:module-name:name-of-file.adoc[link text]
```

To use an example from this Writer's Guide, to link to the `index.adoc` file in the `ROOT` module, you would write:

```asciidoc
Let's go to the xref:ROOT:index.adoc[documentation home page].
```

It would render in the finished documentation as:

Let's go to the [documentation home page](../index.md).

## [](#component-coordinate)Link to a Page in a Different Component

To link to a page in a different component, you need to know the page's component name, module name, and filename:

* Start with the component name, followed by a colon (`:`).
* Add the module name, followed by a colon (`:`).
* Add the filename, including the file extension.

For example:

```asciidoc
xref:component-name:module-name:name-of-file.adoc[link text]
```

If you're not sure of the component name for your xref, you can check the `antora.yml` file inside the Documentation repository that holds that file.

The `antora.yml` should always be found in the top-most level of the repository's files. Look for the `name` attribute inside the `antora.yml` file.

The following is an example `antora.yml` file for version 5.5 of the Couchbase Server documentation:

```yaml
name: server
title: Couchbase Server
version: '5.5'
start_page: introduction:intro.adoc
nav:
- modules/ROOT/nav.adoc
```

The `name` attribute is `server`.

To link from this page in the Writer's Guide to the What's New? page in the `server` component, you would write:

```asciidoc
xref:server:introduction:whats-new.adoc[What's new] in Couchbase Server?
```

It would render in the finished documentation as:

[What's new](../../server/current/introduction/whats-new.md) in Couchbase Server?

## [](#link-to-element)Link to an Element in a Page

You can link to a specific element, such as a heading, table entry, and more, by assigning or knowing that element's ID and adding it to your xref.

This is known as an [anchor link](#styleguide:anchor-links.adoc).

After the filename and extension, add a hash (`#`), then the element ID.

For example, you can link from this page to the **Images** heading in the AsciiDoc Basics page by writing:

```asciidoc
See xref:basics.adoc#images[Images].
```

The heading in the AsciiDoc Basics page looks like this in the source AsciiDoc file:

## [](#images)Images

The xref would render in the finished documentation as:

See [Images](basics.md#images).

## [](#cross-reference-best-practices)Cross Reference Best Practices

* [Create attributes](attributes-and-roles.md) for long page ID coordinates to improve the source readability for other contributors.
* [Create attributes](attributes-and-roles.md) for page ID coordinates used several times on the same page.
* Make sure to always assign link text to xrefs when linking to an element on a page with an anchor link. Try to write [good link text](#styleguide:links.adoc).
* Leave the link text blank when you're not linking with an anchor link. This keeps link text up-to-date and accurate if a page title changes.

## [](#learn-more)Learn More

* For more information about how to assign IDs to elements on a page, see [Element IDs and Same-Page Cross References](ids.md).
* For more information about how to create and work with attributes in the documentation, see [Attributes](attributes-and-roles.md).

## [](#additional-resources)Additional Resources

* [Why is the page ID important?](https://docs.antora.org/antora/latest//page/xref/)
* [More xref usage examples](https://docs.antora.org/antora/latest//asciidoc/page-to-page-xref/)