---
title: Include Examples and Partials
editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/contribute/pages/includes.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:home:contribute:includes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/contribute/includes.html)

# Include Examples and Partials

> [!NOTE]
> This documentation is out of date

## [](#example-files)Example Files

Examples are non-AsciiDoc files that contain reusable content, such as source code or programmatic output, that is often inserted into [code blocks](code-blocks.md). They’re saved in the [_examples_ directory of a module](component-configuration.md#examples-dir). Regardless of an example’s source module, it can be inserted into any standard page in your documentation site using the include directive and the example file’s resource ID.

Include directive and example resource ID structure

include::version@component:module:example$file.ext[]

## [](#partial-files)Partial Files

Partials are AsciiDoc files that contain reusable snippets of content. They’re saved in the [_partials_ directory of a module](component-configuration.md#partials-dir). Regardless of a partial’s source module, it can be inserted into any standard page in your documentation site using the include directive and the partial file’s resource ID.

Include directive and partial resource ID structure

include::version@component:module:partial$file.adoc[]

## [](#insert-an-example-or-a-partial)Insert an Example or a Partial

An entire example or partial (or a portion of) is inserted into a page using the include directive and file’s resource ID. A [resource ID](https://docs.antora.org/antora/2.0/page/resource-id/) is just like a page ID, but it has an extra coordinate, `family$`. The family coordinate for examples is `example$` and `partial$` for partials. Like the [page ID in an xref](cross-references.md), the more a page and the partial or example are related, the less coordinates you have to specify.

Include from the same module

include::example$output/query-max.json[]

include::partial$cli-options.adoc[]

Include from the same component, different modules

include::ROOT:example$HelloWorld.java[]

include::security:partial$mode-definitions.adoc[]

Include from different components

include::4.5@tree::example$extension.js[]

include::catalog::partial$ref/definitions.adoc[]

## [](#tag-region)Insert Tagged Content from an Example or Partial

To include a snippet of content from an example or partial (instead of the whole file), use the `tag` directive.

Tagging content in a partial file

This page discusses how to develop Couchbase applications to function in times of node or network failure.

// tag::failover-definition[] **(1)** **(2)**
--
Failover is the means by which a node is removed from the cluster and all its owned vBuckets are immediately:

* Transferred to a replica node (if there are replica nodes)
* Marked offline (if there are no replica nodes).
--
// end::failover-definition[] **(3)** **(4)**

| **1** | To indicate the start of a tagged region, insert a comment line (//) in the file.                                                                              |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Assign a unique name to the region in the tag directive, followed by a set of square brackets (\[\]). In this example the tag is called _failover-definition_. |
| **3** | Insert a comment line where you want the tagged region to end.                                                                                                 |
| **4** | Assign the name of the region you want to terminate to the end directive.                                                                                      |

To insert a tagged region into a page, enter the resource ID and tag attribute in the include directive.

Include a tagged region of a partial into a page in another component

If you received this error message, you might have a failover condition.

include::6.0@sdk-common:shared:partial$env-errors.adoc[tag=failover-definition]

Code regions in example files can be tagged using the language’s comment syntax before `tag` and `end`. For example, if you tag code in a YAML file, place a hash (`#`) before the tag directive.

```yaml
# tag::expire[]
  artifacts:
    expire_in: 1 week
# end::expire[]
    paths:
    - public/
```

## [](#couchbase-documentation-partials)Couchbase Documentation Partials

### [](#developer-preview-partial)Developer Preview Partial

To call out a section of a page as Developer Preview, use the `developer-preview` partial. Otherwise if the whole page is Developer Preview content, you can use the [page-status](attributes-and-roles.md#custom-page-attributes) attribute.

include::home:ROOT:partial$developer-preview.adoc[]

Renders as:

> [!CAUTION]
> This is a Developer Preview feature, intended for development purposes only. Do not use this feature in production. No Enterprise Support is provided for Developer Preview features.

## [](#learn-more)Learn More

* [Insert examples into code blocks with the include directive](code-blocks.md#include-code).
* Browse the source files in the SDK language and common components on GitHub for numerous examples of partial includes and tagging.

## [](#additional-resources)Additional Resources

The Antora and Asciidoctor documentation provide more information about including partials, examples, and standard pages as well as optional attributes such as `indent` and `leveloffset`.

* [Antora resource ID structure](https://docs.antora.org/antora/2.0/page/resource-id/)
* [Insert examples with the include directive](https://docs.antora.org/antora/2.0/asciidoc/include-example/)
* [Insert partials with the include directive](https://docs.antora.org/antora/2.0/asciidoc/include-partial/)
* [The page-partial attribute and inserting a standard page with the include directive](https://docs.antora.org/antora/2.0/asciidoc/include-page/)
* [Select code regions with the tag directive](https://asciidoctor.org/docs/user-manual/#by-tagged-regions)
* [Normalize block indentation with the indent attribute](https://asciidoctor.org/docs/user-manual/#normalize-block-indentation)
* [Offset section headings with leveloffset](https://asciidoctor.org/docs/user-manual/#include-partitioning)