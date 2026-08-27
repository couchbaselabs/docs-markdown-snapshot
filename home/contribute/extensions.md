---
title: Site Extensions
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/contribute/pages/extensions.adoc
  xref: xref:home:contribute:extensions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/contribute/extensions.html)

# Site Extensions

Test and document your Asciidoctor.js or Antora extensions here.

## [](#markdown-block)Markdown Block

```asciidoc
[markdown]
--
Filter some text with [Markdown](https://commonmark.org/help/) syntax.
--
```

Results in:

Filter some text with [Markdown](https://commonmark.org/help/) syntax.

> [!NOTE]
> This is not implemented with a full Markdown parser. See [issue](https://github.com/asciidoctor/kramdown-asciidoc/issues/7)with a link to the "naive series of regexes" used as starting point.
> 
> (And note that we use Open [structural context](https://docs.asciidoctor.org/asciidoc/latest/blocks/delimited/#summary-of-structural-containers), with `--` delimiters, and headings don't work inside these.)
> 
> This feature is intended for handling OpenAPI specs, which can contain Markdown, however openapi-generator has [poor Asciidoc handling](https://github.com/OpenAPITools/openapi-generator/issues/11396), so instead we add the block delimiters in the template, and let the block filter handle it.