---
title: Standard Document Structure
editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/contribute/pages/pages.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:home:contribute:pages.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/contribute/pages.html)

# Standard Document Structure

All standard AsciiDoc documents exist in the **pages** directory of a module.

## [](#filenames)Filenames

AsciiDoc documents should be saved as `.adoc` files, with the following filename restrictions:

* All lowercase letters.
* Words separated by hyphens (`-`).
* No symbols or special characters.

> [!WARNING]
> The file's name is used to create its page URL. Changing a file's name will break [cross references (xrefs)](cross-references.md) and incoming links to the page from external websites.

## [](#internal-file-structure)Internal File Structure

A Couchbase AsciiDoc document file should contain the following components:

A Header

Contains the document title and document attributes. Some attributes are required. See [Document Title and Header](#doc-title).

A Body

Contains the written content, other than the title, that displays when a user visits the page on our documentation site. See [Document Body](#doc-body).

### [](#doc-title)Document Title and Header

Put the title of your AsciiDoc document on the first line of the file. Mark the title with one equals sign (`=`), followed by a blank space, and then the title text.

> [!NOTE]
> Every AsciiDoc file stored in a **pages** directory must have a document title.

On the second line and any following lines, you can add [document attributes](attributes-and-roles.md). Each attribute must be entered on its own line, as shown:

= The Title of My Document
:page-topic-type: concept
:description: This is the description of my page! It's short and sweet.
:url-query-tut: https://query-tutorial.couchbase.com/tutorial/#1

[abstract]
{description}

This is the body of my document.
Let's get started with N1QL!

You must include the following document attributes for every AsciiDoc file stored in a **pages** directory:

| Attribute         | Description                                                                                                                                                                                      | Allowed Values                                                                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| :page-topic-type: | The page topic type sets the content type for a page and automatically adds a corresponding badge. These badges help users quickly identify the kind of content they're going to find on a page. | For concepts: concept For tasks: guide For references: reference                                                                               |
| :keywords:        | Use the keywords attribute to add meta keywords to the HTML head for your page.                                                                                                                  | Any applicable keyword, separated by commas (,).                                                                                               |
| :description:     | The page description is used for SEO and provides a brief description of the page, which is displayed using the \[abstract\] attribute on the page.                                              | Enter a quick description of the content on the page. Emphasize what the user would want to know at a glance. Try to keep it to 1-2 sentences. |

A single blank line signals the end of the header. The [document body](#doc-body) starts on the next line that has text.

You can include your own custom document attributes, or make use of some of these other useful attributes, based on your page's content:

| Attribute         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Allowed Values                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| :imagesdir:       | Use the imagesdir attribute to set where Antora should resolve the location of images included in a page. By default, the value of imagesdir is empty, and image paths are resolved relative to the current page. Set the imagesdir to avoid hard-coding image paths when writing an include, as Antora will automatically prefix any path with the set value. For example, the following would become a valid image include: image::name-of-image.png\[\]                                                                                                                        | :imagesdir: ../assets/images Try to keep your images inside the assets/images folder in a module.                                                                                                                                                                                                                                                                                                                         |
| :page-aliases:    | Use the page-aliases attribute when you need to delete or rename a page to avoid breaking links. Antora will resolve any links to the filename(s) you specify in this attribute to redirect to the current page, instead. You should only use page-aliases if it's absolutely necessary. It's not designed to be a general-purpose URL router, and it can get noisy and chaotic to maintain a large number of page-aliases on a page, or across pages. Do your part to keep the AsciiDoc files clean and easy to understand. Try to appropriately name your pages from the start. | A [valid cross reference](cross-references.md) to a page. For a page in the same module: :page-aliases: search-query.adoc For a page in a different module: :page-aliases: ROOT:search-query.adoc For a page in another repository: :page-aliases:7.6@server:develop:integrations.adoc When linking to a repository that has a version, you must specify which version in that repository redirects to your current page. |
| :page-edition:    | If you're writing content that only applies to a specific edition of Couchbase Server, usually the Enterprise Edition, use the page-edition attribute to add a badge to the page that indicates the Edition the content applies to.                                                                                                                                                                                                                                                                                                                                               | page-edition: Enterprise Edition                                                                                                                                                                                                                                                                                                                                                                                          |
| :page-layout:     | Sets the UI layout to assign to a page. By default, pages use the default.hbs template from the [docs-ui repository](https://github.com/couchbase/docs-ui).                                                                                                                                                                                                                                                                                                                                                                                                                       | For the list of all available templates, see [the docs-ui repository](https://github.com/couchbase/docs-ui/tree/master/src/layouts).                                                                                                                                                                                                                                                                                      |
| :page-pagination: | Include the page-pagination attribute to add pagination to the bottom of a page. Set the attribute to prev to allow the user to navigate to the previous and next pages surrounding the current page in the module's table of contents. Set the attribute to next to include only navigation going to the next topic in the table of contents. For an example of page-pagination, see [the Server documentation](../../server/current/guides/insert.md).                                                                                                                          | :page-pagination: prev :page-pagination: next                                                                                                                                                                                                                                                                                                                                                                             |
| :page-partial:    | Allows this page to be included inside another page as a [partial file](includes.md#partial-files). You only need to set this attribute on a page that you add to the pages directory of a module.                                                                                                                                                                                                                                                                                                                                                                                | :page-partial:                                                                                                                                                                                                                                                                                                                                                                                                            |
| :page-role:       | Assign a role to a page to change the default CSS or add new CSS styles to the entire page. The exact behavior depends on the assigned role. The page-role attribute can take multiple values, separated by a single space.                                                                                                                                                                                                                                                                                                                                                       | :page-role: tiles: Arranges and renders H2 headings as tiles, in 2 columns down the page. :page-role: -toc: Removes the in-page table of contents from a page. Useful for landing pages.                                                                                                                                                                                                                                  |
| :page-status:     | If you're writing content that only applies to a beta or specific software version, use the page-status attribute to mark the page with a badge.                                                                                                                                                                                                                                                                                                                                                                                                                                  | Any valid software name and version. For example, :page-status: Couchbase Server 7.2                                                                                                                                                                                                                                                                                                                                      |
| :page-toclevels:  | Use the page-toclevels attribute to control the depth of headings displayed on the in-page table of contents, at the right of the document contents. By default, the in-page table of contents only displays Heading 2 (H2) headings. Set the attribute to any value greater than or equal to 2 to increase the heading depth displayed.                                                                                                                                                                                                                                          | page-toclevels: <Any integer greater than 1>                                                                                                                                                                                                                                                                                                                                                                              |
| :sectids:         | [Unset](attributes-and-roles.md#unsetting-a-document-attribute) the sectids attribute to stop automatically generating section IDs for headings inside an AsciiDoc file. If sectids is left set for a document, section IDs for [cross references](cross-references.md) are generated based on the content of the heading, replacing spaces with dashes. You can always override these automatic IDs by assigning your own.                                                                                                                                                       | :sectids: (set) :!sectids: (unset)                                                                                                                                                                                                                                                                                                                                                                                        |
| :tabs:            | To add the tabs feature to your page and allow tabbed content blocks, you must set the tabs attribute. You can find an example of tabbed content in [the Server documentation](../../server/current/guides/deleting-data.md#deleting-a-document).                                                                                                                                                                                                                                                                                                                                 | :tabs: :!tabs:                                                                                                                                                                                                                                                                                                                                                                                                            |
| :xrefstyle:       | Controls the generated text for [cross references](cross-references.md) in a document, when linking to block content that has a caption set. For more information, see [the AsiiDoc documentation](https://docs.asciidoctor.org/asciidoc/latest/macros/xref-text-and-style/).                                                                                                                                                                                                                                                                                                     | :xrefstyle: full :xrefstyle: short :xrefstyle: basic                                                                                                                                                                                                                                                                                                                                                                      |

### [](#doc-body)Document Body

Write your document body using appropriate [AsciiDoc syntax](basics.md).

Consider making use of:

* [Bold and Code Styles](basics.md#bold-and-code-styles)
* [Button, Keyboard, and Menu UI Macros](basics.md#ui-macros)
* [URLs](basics.md#urls)
* [Description Lists](basics.md#description-lists)
* [Ordered Lists](basics.md#ordered-lists)
* [Unordered Lists](basics.md#unordered-lists)
* [Images](basics.md#images)
* [Admonitions](basics.md#admonitions)
* [Tables](basics.md#tables)

#### [](#ventilate)Ventilated Prose

Write in ventilated prose, putting a single sentence on a single line in your AsciiDoc file. Insert paragraph breaks by adding an empty line between sentences:

This is Sentence 1.
This sentence will display as part of the same paragraph as Sentence 1.
This is proper ventilated prose.

This sentence will start a new paragraph.

Ventilated prose makes reviewing pull request and changes easier for reviewers and maintainers.

#### [](#headings)Headings

Break up your text into sections using headings. Good heading structure makes scanning your documentation easier for readers.

The number of equals signs (`=`) equals the depth of the heading.

Heading 2 titles (indicated by 2 equals signs (`==`)) display in the [On This Page sidebar](nav-menus-and-files.md) on a page. You can change the depth of headings displayed on the On This Page sidebar with the [:page-toclevels: attribute](#page-toclevels).

You must nest section headings in order. Do not put an Heading 4 section inside a Heading 2 section, without a Heading 3 section in between:

== Heading 2 Section Title (H2)

=== Heading 3 Section Title (H3)

==== Heading 4 Section Title (H4)

Vale will flag headings that are not properly ordered inside your document.

You also cannot apply any [inline formatting](basics.md#bold-italic-and-code-styles) to headings.

## [](#learn-more)Learn More

* [AsciiDoc basics](basics.md).
* [Attributes and roles](attributes-and-roles.md).
* [Edit a page](edit-pages.md).