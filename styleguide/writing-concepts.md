---
title: Writing Concepts
editUrl: https://github.com/couchbaselabs/docs-style-guide/edit/main/styleguide/modules/ROOT/pages/writing-concepts.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:styleguide::writing-concepts.adoc[]
---

[View original HTML](/styleguide/writing-concepts.html)

# Writing Concepts

A concept explains to the user the why behind a [procedure](writing-procedures.md) or piece of [reference material](writing-references.md). It explains what things are and introduces the things a user needs to know to be successful at completing a procedure or understanding references.

## [](#description-attribute)Description Attribute

At the beginning of every concept, you should have a brief explanation of the goal of the concept, or what the user can hope to learn from reading this concept.

This goal should be part of the `:description:` attribute that you need to add to the beginning of every topic.

If you need to add links to your brief explanation, put them outside of the `:description:` attribute.

## [](#general-guidelines)General Guidelines

A concept should:

* Explain all technical concepts or jargon, or link to other explanations if there is no space.
* Use headings to break up and highlight important information to the user, to aid scanning and findability.
* Link to related procedures or reference material.
* Explain only 1 focused topic.
* Have paragraphs of 5 sentences or less.

## [](#required-sections)Required Sections

The only required heading and section in a concept is the [See Also section](#see-also).

### [](#see-also)See Also

The **See Also** section in a concept should be an H2 level heading.

It contains an [unordered list](unordered-list.md) of links to tasks, references, or other concepts that the user can read to continue in their learning journey.

> [!NOTE]
> There will always be somewhere the user can go next or view after reading your concept.