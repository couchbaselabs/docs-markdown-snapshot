---
title: Decision Dialogs
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-style-guide/edit/main/ui-ux/modules/ROOT/pages/decision-dialogs.adoc
  xref: xref:ui-ux::decision-dialogs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ui-ux/decision-dialogs.html)

# Decision Dialogs

A decision dialog is a window that appears when a user needs to confirm an action in the UI. They're given a choice to confirm or cancel that action.

![The Delete API Key decision dialog. The user is prompted to type delete in a text field, and warned that the action can’t be undone. They can click Delete API Key or Cancel.](_images/DecisionDialog.png) 

## [](#add-a-title-thats-a-question)Add a Title That's a Question

A decision dialog has a title that's a specific question that ends in a question mark.

For example, a decision dialog that appears when a user tries to remove a user could be titled **Remove this user?**

## [](#provide-quick-critical-details-in-the-body-text)Provide Quick, Critical Details in the Body Text

The body text of a decision dialog should stick to the quick, critical things that a user needs to know to make their decision.

Avoid length context, explanations, or descriptions of edge cases. You can keep these in the larger UI, or link to documentation, instead.

In general, try to know ahead of time if you have space or character constraints in the UI when you write the decision dialog text.

Write in full and complete sentences inside the body text.

For example, the decision dialog that appears when a user tries to remove a user could simply state "This user is an Organization Owner. Removing this user from the Project will not remove their Project Owner role."

## [](#use-the-same-words-for-the-actions)Use the Same Words for the Actions

The question for the decision dialog and the provided decision buttons should use the same language.

Keep the language literal and descriptive.

For example, if a user tries to remove a user, the question should be **Remove this user?** and the decision button should say **Remove** or **Remove User**. The decision button shouldn't say **Yes** or **Sure**.

### [](#save-vs-apply-vs-update)Save vs. Apply vs. Update

If the user is making a change that they need to save or cancel, the confirmation button should be **Save**, not **Apply** or **Update**.

Ideally, try to make the [action button](action-buttons.md) match the title of the dialog or what the user is actually doing.

### [](#close-vs-done)Close vs. Done

Use **Done** when the user is finished with a process, and clicking **Done** will bring them back to another page.

Use **Close** when the user is just dismissing a dialog or a side sheet, but not leaving their current page or process.

## [](#put-primary-or-positive-actions-on-the-right)Put Primary or Positive Actions on the Right

The primary, positive, or confirming action for a decision dialog should be on the right.

The dismissive or secondary actions for a decision dialog should be on the left.

For example, the dialog to remove a user should have the **Remove** or **Remove User** action on the right of the dialog, and the **Cancel** action on the left.

If one button in a decision dialog has a border, both buttons should have borders.