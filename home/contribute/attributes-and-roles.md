---
title: Attributes and Roles
editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/contribute/pages/attributes-and-roles.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:home:contribute:attributes-and-roles.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/contribute/attributes-and-roles.html)

# Attributes and Roles

Use attributes and roles to insert content or CSS styles into your pages.

## [](#setting-and-referencing-document-attributes)Setting and Referencing Document Attributes

Use an AsciiDoc attribute to hold names, URLs, and reusable content phrases.

An attribute consists of a key-value pair set in a page header or in the playbook file for the documentation site. Some attributes are built-in to Asciidoctor. Others are defined especially for the Couchbase documentation or by the writer.

Adding an attribute to a document header makes an attribute available to an entire page and all of its includes. Each attribute must be entered on a separate line, known as an attribute entry. The syntax of an attribute entry as follows:

 :name: value

In this case, `name` is the name of the attribute and `value` is the optional value. The following example shows a document header with multiple included attributes:

Examples of document attributes

```asciidoc
= Page Title
:page-topic-type: concept (1)
:source-language: javascript (2)
:url-downloads: https://www.couchbase.com/downloads (3)
:tabs: (4)

Download Sync Gateway from the {url-downloads}[Couchbase downloads page]. (5)

[source] (6)
----
Snippet of javascript source code
----
```

| **1** | Attribute names that start with page- are specially handled by Antora.                                                               |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | A value can be assigned to a built-in attribute in the document header.                                                              |
| **3** | Writers can set and define their own attributes.                                                                                     |
| **4** | Some attributes are assigned an implicit value. In this case, the tabs feature is turned on by setting tabs.                         |
| **5** | Reference an attribute in the body of the document by entering the attribute name inside a set of curly brackets ({attribute-name}). |
| **6** | Code blocks are assigned the source language javascript.                                                                             |

## [](#required-document-attributes)Required Document Attributes

The following document attributes must be included for every AsciiDoc file stored in a **pages** directory:

| Attribute         | Description                                                                                                                                                                                      | Allowed Values                                                                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| :page-topic-type: | The page topic type sets the content type for a page and automatically adds a corresponding badge. These badges help users quickly identify the kind of content they’re going to find on a page. | For concepts: concept For tasks: guide For references: reference                                                                               |
| :keywords:        | Use the keywords attribute to add meta keywords to the HTML head for your page.                                                                                                                  | Any applicable keyword, separated by commas (,).                                                                                               |
| :description:     | The page description is used for SEO and provides a brief description of the page, which is displayed using the \[abstract\] attribute on the page.                                              | Enter a quick description of the content on the page. Emphasize what the user would want to know at a glance. Try to keep it to 1-2 sentences. |

## [](#optional-document-attributes)Optional Document Attributes

You can also use the following optional attributes:

| Attribute         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Allowed Values                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| :imagesdir:       | Use the imagesdir attribute to set where Antora should resolve the location of images included in a page. By default, the value of imagesdir is empty, and image paths are resolved relative to the current page. Set the imagesdir to avoid hard-coding image paths when writing an include, as Antora will automatically prefix any path with the set value. For example, the following would become a valid image include: image::name-of-image.png\[\]                                                                                                                        | :imagesdir: ../assets/images Try to keep your images inside the assets/images folder in a module.                                                                                                                                                                                                                                                                                                                         |
| :page-aliases:    | Use the page-aliases attribute when you need to delete or rename a page to avoid breaking links. Antora will resolve any links to the filename(s) you specify in this attribute to redirect to the current page, instead. You should only use page-aliases if it’s absolutely necessary. It’s not designed to be a general-purpose URL router, and it can get noisy and chaotic to maintain a large number of page-aliases on a page, or across pages. Do your part to keep the AsciiDoc files clean and easy to understand. Try to appropriately name your pages from the start. | A [valid cross reference](cross-references.md) to a page. For a page in the same module: :page-aliases: search-query.adoc For a page in a different module: :page-aliases: ROOT:search-query.adoc For a page in another repository: :page-aliases:7.6@server:develop:integrations.adoc When linking to a repository that has a version, you must specify which version in that repository redirects to your current page. |
| :page-edition:    | If you’re writing content that only applies to a specific edition of Couchbase Server, usually the Enterprise Edition, use the page-edition attribute to add a badge to the page that indicates the Edition the content applies to.                                                                                                                                                                                                                                                                                                                                               | page-edition: Enterprise Edition                                                                                                                                                                                                                                                                                                                                                                                          |
| :page-layout:     | Sets the UI layout to assign to a page. By default, pages use the default.hbs template from the [docs-ui repository](https://github.com/couchbase/docs-ui).                                                                                                                                                                                                                                                                                                                                                                                                                       | For the list of all available templates, see [the docs-ui repository](https://github.com/couchbase/docs-ui/tree/master/src/layouts).                                                                                                                                                                                                                                                                                      |
| :page-pagination: | Include the page-pagination attribute to add pagination to the bottom of a page. Set the attribute to prev to allow the user to navigate to the previous and next pages surrounding the current page in the module’s table of contents. Set the attribute to next to include only navigation going to the next topic in the table of contents. For an example of page-pagination, see [the Server documentation](../../server/current/guides/insert.md).                                                                                                                          | :page-pagination: prev :page-pagination: next                                                                                                                                                                                                                                                                                                                                                                             |
| :page-partial:    | Allows this page to be included inside another page as a [partial file](includes.md#partial-files). You only need to set this attribute on a page that you add to the pages directory of a module.                                                                                                                                                                                                                                                                                                                                                                                | :page-partial:                                                                                                                                                                                                                                                                                                                                                                                                            |
| :page-role:       | Assign a role to a page to change the default CSS or add new CSS styles to the entire page. The exact behavior depends on the assigned role. The page-role attribute can take multiple values, separated by a single space.                                                                                                                                                                                                                                                                                                                                                       | :page-role: tiles: Arranges and renders H2 headings as tiles, in 2 columns down the page. :page-role: -toc: Removes the in-page table of contents from a page. Useful for landing pages.                                                                                                                                                                                                                                  |
| :page-status:     | If you’re writing content that only applies to a beta or specific software version, use the page-status attribute to mark the page with a badge.                                                                                                                                                                                                                                                                                                                                                                                                                                  | Any valid software name and version. For example, :page-status: Couchbase Server 7.2                                                                                                                                                                                                                                                                                                                                      |
| :page-toclevels:  | Use the page-toclevels attribute to control the depth of headings displayed on the in-page table of contents, at the right of the document contents. By default, the in-page table of contents only displays Heading 2 (H2) headings. Set the attribute to any value greater than or equal to 2 to increase the heading depth displayed.                                                                                                                                                                                                                                          | page-toclevels: <Any integer greater than 1>                                                                                                                                                                                                                                                                                                                                                                              |
| :sectids:         | [Unset](#unsetting-a-document-attribute) the sectids attribute to stop automatically generating section IDs for headings inside an AsciiDoc file. If sectids is left set for a document, section IDs for [cross references](cross-references.md) are generated based on the content of the heading, replacing spaces with dashes. You can always override these automatic IDs by assigning your own.                                                                                                                                                                              | :sectids: (set) :!sectids: (unset)                                                                                                                                                                                                                                                                                                                                                                                        |
| :tabs:            | To add the tabs feature to your page and allow tabbed content blocks, you must set the tabs attribute. You can find an example of tabbed content in [the Server documentation](../../server/current/guides/deleting-data.md#deleting-a-document).                                                                                                                                                                                                                                                                                                                                 | :tabs: :!tabs:                                                                                                                                                                                                                                                                                                                                                                                                            |
| :xrefstyle:       | Controls the generated text for [cross references](cross-references.md) in a document, when linking to block content that has a caption set. For more information, see [the AsiiDoc documentation](https://docs.asciidoctor.org/asciidoc/latest/macros/xref-text-and-style/).                                                                                                                                                                                                                                                                                                     | :xrefstyle: full :xrefstyle: short :xrefstyle: basic                                                                                                                                                                                                                                                                                                                                                                      |

Antora also assigns several page attributes on each page to provide information about the component, version, and module where a page is located. You can find a list of these attributes in the [Antora documentation](https://docs.antora.org/antora/latest/page/intrinsic-attributes/).

See the [production](https://github.com/couchbase/docs-site/blob/master/antora-playbook.yml) and [staging](https://github.com/couchbase/docs-site/blob/master/antora-playbook-staging.yml) Antora playbooks to review which AsciiDoc attributes are currently set and unset for all of the Couchbase documentation pages.

## [](#unsetting-a-document-attribute)Unsetting a Document Attribute

Some built-in attributes are set (turned on) by default and set for all of the Couchbase document in the playbook.

For example, the `sectids` attribute is turned on by default and automatically generates section IDs for all Couchbase documentation pages. To unset (turn off) an attribute on a page, prefix the name with a bang (`!`):

```asciidoc
= Page Title
:!sectids:
```

## [](#using-roles)Using Roles

A role applies alternative or additional CSS styles to a document, block, or phrase. The styles for each role are defined by the code in the [docs-ui repository](https://github.com/couchbase/docs-ui).

### [](#inline-roles)Inline Roles

Add a role to a block or phrase by prefixing the role name with a dot and inserting it between a set of square brackets:

```asciidoc
[.role-name]`I'm a phrase with an assigned role!`
```

As stated in the [AsciiDoc documentation](https://docs.asciidoctor.org/asciidoc/latest/attributes/role/), inline elements must be surrounded by formatting syntax to be assigned a role.

You can add multiple roles to a single block or phrase by separating each role name with a period (`.`):

```asciidoc
[.role1 .role2]*I'm a phrase with an assigned role!*

[.role1 .role2]
\----
I'm a block with an assigned role!
\----
```

### [](#inline-roles-for-editions-versions-and-deprecation)Inline Roles for Editions, Versions, and Deprecation

Couchbase Documentation created inline page roles for marking sections of documentation as deprecated, for a specific Couchbase Server version, or for marking sections as applying to a specific product edition - similar to [the :page-edition: attribute](#page-edition).

You can use the following inline roles to mark sections of text in your documentation:

| Role                                | Example                                                                                                                    |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| \[.edition\]#{enterprise}#          | [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) This text applies to Couchbase Server Enterprise Edition |
| \[.edition\]#{community}#           | [COMMUNITY EDITION](https://www.couchbase.com/products/editions) This text applies to Couchbase Server Community Edition   |
| \[.status\]#Couchbase Server x.x.x# | Couchbase Server 7.6.2 This text applies to Couchbase Server version 7.6.2                                                 |
| \[.deprecated\]#Deprecated#         | Deprecated This text applies to a deprecated feature                                                                       |

The `[ENTERPRISE EDITION](https://www.couchbase.com/products/editions)` and `[COMMUNITY EDITION](https://www.couchbase.com/products/editions)` edition attributes are defined in the Antora playbook and automatically add a link to details about the different Couchbase Server editions.

When adding badges to text, try to always add the badge on a single line, by itself, following the heading of the section where it applies. Otherwise, place the badge as close to the edition, version, or deprecated content as possible.

### [](#page-roles)Page Roles

Assigning a role to a page applies that role to the entire page, rather than a specific block or phrase. `page-role` is an example of a [page attribute](#using-page-attributes). It must be defined in the document header.

Unlike with blocks and phrases, page roles are not prefixed with a dot and must be separated by a single space (following the same rules as CSS classes).

The Couchbase documentation currently supports two page roles:

* `tiles`
* `-toc`

These roles are often combined, as you can see in this example:

```asciidoc
= Document Title
:page-role: tiles -toc

Page contents.
```

You can see the `tiles -toc` page role combination in action on the [Starter Kits page](../../server/current/getting-started/starter-kits.md). The tiles role arranges the secondary section titles as tiles (in two columns). The -toc role tells the UI template not to add a table of contents (TOC) to the page.

## [](#using-page-attributes)Using Page Attributes

Certain document attribute names are reserved specifically for use with Antora. These are know as page attributes. All page attributes begin with the `page-` prefix. The prefix is removed and the remainder is passed on to the UI as metadata. For the most part, it’s up to the UI to decide how to use this information.

Antora has several [built-in page attributes](https://docs.antora.org/antora/latest/page/intrinsic-attributes/), and some other attributes have been added to the Couchbase UI.

> [!WARNING]
> Do not create your own attributes that conflict with the names of any built-in page attributes or page attributes that are already in use.

### [](#custom-page-attributes)Custom Page Attributes

Use custom page attributes to pass information from the document to the UI. Use the [docs-ui repository](https://github.com/couchbase/docs-ui) to control what these attributes actually do with the contents of a page.