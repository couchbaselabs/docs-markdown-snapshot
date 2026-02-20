---
title: Links
editUrl: https://github.com/couchbaselabs/docs-style-guide/edit/main/styleguide/modules/ROOT/pages/links.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:styleguide::links.adoc[]
---

[View original HTML](/styleguide/links.html)

# Links

Follow the [Google Developer Style Guide](https://developers.google.com/style/link-text)'s guidance on how to write link text. In general, make it clear where a user ends up after they click a link.

> [!NOTE]
> This does not mean to just use the URL as the displayed link text. Try to write effective and useful link text for all links.

Introduce all links with `For more information, see {link}.`Do not use `Refer to`, `For more details`, or other constructions. If you need to use another construction, try to have a good justification for that specific use case, and still try to keep the `For x, see y` construction.

Keep the following formatting and conventions in mind for [Internal Links](#internal) and [External Links](#external) in the Couchbase Documentation.

## [](#internal)Internal Links

Use the `xref` syntax for all links to content within the documentation repositories. For more information about the `xref` syntax in Antora, see [Cross References](#home:contribute:cross-references.adoc) in the Contributing to the Documentation guide.

You can leave the link text for an `xref` blank to get Antora to use the <h1> heading of the linked page as the link.

### [](#sdk-references-and-api-references)SDK References and API References

Where possible, when linking to an SDK or API reference, use an evergreen link. Evergreen links help cut down on maintenance when tooling for references and other resources change. For a list of evergreen links, see the [rewrites.conf file](https://github.com/couchbase/docs-site/blob/master/etc/nginx/snippets/rewrites.conf).

Format evergreen links as external links. For an example of using an evergreen link, see the [entries in the References section in the nav.adoc file](https://raw.githubusercontent.com/couchbase/docs-sdk-java/release/3.3/modules/ROOT/nav.adoc) for the Java SDK documentation.

## [](#external)External Links

For links to third-party websites, follow the guidance in [Links to other sites](https://developers.google.com/style/links-external) in the Google Developer Style Guide. Use their guidance for when and how to link.

For more information about external link syntax in Antora, see [URLs](#home:contribute:basics.adoc#urls) in the Contributing to the Documentation guide.