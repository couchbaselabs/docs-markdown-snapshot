---
title: Writing Documentation Overview
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/contribute/pages/asciidoc-overview.adoc
  xref: xref:home:contribute:asciidoc-overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/contribute/asciidoc-overview.html)

# Writing Documentation Overview

> [!NOTE]
> This documentation is out of date

## [](#asciidoc-and-asciidoctor)AsciiDoc and Asciidoctor

The Couchbase documentation is written using AsciiDoc. AsciiDoc is a lightweight markup language that supports the structural and semantic elements necessary for writing web-first, technical documentation. You can write an AsciiDoc document using Atom, VS Code, or your preferred plain text editor.

If a document contains incorrect AsciiDoc syntax, you'll see a warning message that starts with `asciidoctor` when you build the site.

asciidoctor: WARNING: backup-and-restore.adoc: line 12: invalid style for listing block: code

Asciidoctor is the AsciiDoc parser. It reports the syntax errors it encounters when converting the documents to HTML.

## [](#predefined-attributes-and-roles)Predefined Attributes and Roles

The Couchbase documentation uses a number of predefined AsciiDoc attributes and roles. These attributes and roles add custom metadata and special processing or styling behaviors to certain pages.

## [](#learn-more)Learn More

* [Learn how to name and structure an AsciiDoc document](pages.md).
* [Mark up common content elements, like lists and tables, with AsciiDoc](basics.md).
* [Insert an image](basics.md#images).
* [Create document-to-document cross references](cross-references.md).
* [Add source code examples to a document](code-blocks.md).
* [Create a tabs set](tabs.md).

## [](#additional-resources)Additional Resources

The [Asciidoctor project](https://asciidoctor.org/) maintains and releases AsciiDoc under the MIT license.