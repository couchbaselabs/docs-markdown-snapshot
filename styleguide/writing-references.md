---
title: Writing References
editUrl: https://github.com/couchbaselabs/docs-style-guide/edit/main/styleguide/modules/ROOT/pages/writing-references.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:styleguide::writing-references.adoc[]
---

[View original HTML](/styleguide/writing-references.html)

# Writing References

A reference can be:

API documentation 

API documentation provides detailed breakdowns of all methods, classes, sample requests, and sample responses for an API.

A list of properties or UI options 

A table that lists a st of options or properties that a user can interact with through the UI or API.

## [](#description-attribute)Description Attribute

At the beginning of every reference, you should have a brief explanation of the goal of the reference material, or what the user can hope to find in the topic.

This goal should be part of the `:description:` attribute that you need to add to the beginning of every topic.

If you need to add links to your brief explanation, put them outside of the `:description:` attribute.

## [](#general-guidelines)General Guidelines

A reference should:

* Make use of tables, description lists, and headings to break up information and make it easy to scan.

## [](#required-sections)Required Sections

The only required heading and section in a reference is the [See Also section](#see-also).

### [](#see-also)See Also

The **See Also** section in a reference should be an H2 level heading.

It contains an [unordered list](unordered-list.md) of links to tasks, concepts, or other references that the user can read to continue in their learning journey.

> [!NOTE]
> There will always be somewhere the user can go next or view after reading your reference.