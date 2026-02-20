---
title: Information Dialogs
editUrl: https://github.com/couchbaselabs/docs-style-guide/edit/main/ui-ux/modules/ROOT/pages/info-dialogs.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:ui-ux::info-dialogs.adoc[]
---

[View original HTML](/ui-ux/info-dialogs.html)

# Information Dialogs

An information dialog is a window that appears that a user needs to dismiss to get back to the UI.

They can provide information about a complication or recommended course of action, but do not perform or confirm an action. See [Decision Dialogs](decision-dialogs.md), instead.

An information dialog can contain an [error message](error-messages.md).

## [](#add-a-title-thats-a-statement)Add a Title That’s a Statement

The title of an information dialog is a statement. It should tell the user what the system did or what happened.

Do not add punctuation.

## [](#leave-context-and-explanations-to-the-documentation)Leave Context and Explanations to the Documentation

Keep the body text of an information dialog short and direct. Tell the user what happened and what they need to do next, if anything.

Make sure to write in full sentences.

Any lengthy explanations or context should stay in the larger UI or the documentation.

For more information about how to write an effective error message, see [Error Messages](error-messages.md).

## [](#close-vs-done)Close vs. Done

Use **Done** when the user is finished with a process, and clicking **Done** will bring them back to another page.

Use **Close** when the user is just dismissing a dialog or a side sheet, but not leaving their current page or process.