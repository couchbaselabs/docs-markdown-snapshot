---
title: Writing Procedures
editUrl: https://github.com/couchbaselabs/docs-style-guide/edit/main/styleguide/modules/ROOT/pages/writing-procedures.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:styleguide::writing-procedures.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/styleguide/writing-procedures.html)

# Writing Procedures

A procedure can be:

A how-to guide 

How-to guides explain to the user how to accomplish a goal without a specific, defined end result. The specifics of the end result will vary depending on the individual user's goal. For example, a how-to guide could explain how to create a database by explaining the different options and customizations the user can make.

A tutorial 

Tutorials explain to the user how to accomplish a goal that has a defined end result. All users that follow the tutorial will have the same result. For example, a tutorial could explain how to create a specific kind of database that would support a specific use case for the user.

## [](#description-attribute)Description Attribute

Before the [Prerequisites section](#prerequisites), you should have a brief explanation of the goal of the procedure, or what the user can hope to accomplish once they've completed the procedure.

This goal should be part of the `:description:` attribute that you need to add to the beginning of every topic.

If you need to add links to your brief explanation, put them outside of the `:description:` attribute.

## [](#required-sections)Required Sections

All procedures should contain 3 section headers:

1. [Prerequisites](#prerequisites)
2. [Procedure](#procedure)
3. [Next Steps](#next-steps)

### [](#prerequisites)Prerequisites

The **Prerequisites** section should be an H2 level heading.

It contains an [unordered list](unordered-list.md) of things the user must do or have before they can proceed with the content in [Procedure](#procedure).

> [!NOTE]
> There will always be something the user can do.

Add links where appropriate, following the appropriate [link formatting guidance](links.md).

> [!TIP]
> If prerequisites change based on the user's choice of environment, consider if [tabs-set.adoc](#tabs-set.adoc) would help present the information.

### [](#procedure)Procedure

The **Procedure** section should be an H2 level heading that follows the [Prerequisites section](#prerequisites).

It contains an [ordered list](ordered-list.md) of steps the user must take to complete the specific goal of the page.

Steps in a **Procedure** section should:

* List only 1 action per step, with the exception of using an [Menu UI Macro](menu-ui-macro.md) for menu navigation steps.
* Start with the location where the following action or actions need to occur. This could be the start of the step, or the start of the procedure itself, with menu navigation.
* Use [button macros](button-macro.md) for all [Buttons](buttons.md).
* Use [keyboard macros](keyboard-macro.md) for all keyboard interactions.
* Use [monospace font](monospace-highlight.md) for all code outside of code blocks, SQL++ commands, function names, file paths, filenames, and text the user must input.
* Use [Bold](bold.md) for single menu items, tab names, and dialog names.

> [!TIP]
> If steps in a procedure change based on the user's choice of environment, consider if [tabs-set.adoc](#tabs-set.adoc) would help present the information.

Steps in a **Procedure** section should not:

* List the result of an action, if the result is obvious. For example, the **Create Project** window appears after you click **Create Project**.
* Contain lengthy explanations for the reason behind a step. Link to explanatory documentation, such as a concept, where necessary.

### [](#next-steps)Next Steps

The **Next Steps** section should be an H2 level heading that follows the [Procedure section](#procedure).

It contains either an:

* [Unordered list](unordered-list.md) of links.
* Running text that describes the next procedure or action the user can take.

The **Next Steps** section is where additional procedures in a series or links to additional reading on other documentation pages should live.

Always add links to a **Next Steps** section.

Do not call the section **See Also**, **Additional Resources**, or similar. There's always some action the user can take after they complete a procedure.