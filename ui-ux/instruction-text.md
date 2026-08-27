---
title: Instruction Text
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-style-guide/edit/main/ui-ux/modules/ROOT/pages/instruction-text.adoc
  xref: xref:ui-ux::instruction-text.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ui-ux/instruction-text.html)

# Instruction Text

Instruction text appears in the UI to tell the user what they can do and how to do it.

It can appear around buttons or other UI elements to provide context or explanations:

![An image from the Create a Database screen for Provisioned Capella. It instructs the user to select a Couchbase Server version, then tells them about Service Groups: You may want to customize resources for your Couchbase database. You can add nodes, select compute resources, and customize storage below. This configuration can be changed at anytime and may require a period of rebalancing to take effect. Normal operations are never affected.](_images/InstructionText.png) 

## [](#tell-the-user-what-they-need-to-succeed)Tell the User What They Need to Succeed

Always tell the user of any non-"edge case" limitations in the UI. Leave unusual or edge-case situations in the documentation.

Explain foundational concepts or ideas that are necessary for where the user is in the UI.

Instruct them on how-to, or what a next step is that might be hard to find.

Direct them to required inputs or other critical information.

## [](#keep-it-short)Keep It Short

Try and keep instruction text to under a sentence, where possible.

Link to the documentation when needed.

## [](#do-not-write-out-numbers)Do Not Write Out Numbers

Unlike technical documentation, UI copy should always use numerals for ease of recognition. Use 3 over three.

## [](#use-choose-not-select)Use Choose, Not Select

When you need to tell a user to choose between options in the UI, use **choose**, not **select**.

For example, `Choose your source`.

## [](#write-in-sentence-case)Write in Sentence Case

Write instruction text using sentence case, capitalizing only important nouns or words.