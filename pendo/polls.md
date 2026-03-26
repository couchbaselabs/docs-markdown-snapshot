---
title: Poll Guides
editUrl: https://github.com/couchbaselabs/docs-style-guide/edit/main/pendo/modules/ROOT/pages/polls.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:pendo::polls.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/pendo/polls.html)

# Poll Guides

Use the following guidance to write text for a Poll Guide.

A Poll asks a user for feedback on a numeric scale or with an open-ended text field.

## [](#guide-name)Guide Name

Start the Guide Name with **Poll -**.

Use the Guide Goal that you identified when writing your Guide Plan to create the Guide Name.

| Acceptable                | Not Acceptable                                                 |
| ------------------------- | -------------------------------------------------------------- |
| Poll - Playground Feature | Playground Poll Playground Question Questionnaire - Playground |

## [](#guide-layout)Guide Layout

Use the following layouts depending on the type of Poll you want to create:

* Open Text Poll
* Numeric Rating Poll

## [](#guide-category)Guide Category

All Polls must be assigned the **Research > Poll** Guide Category.

## [](#guide-settings)Guide Settings

Use the following guidelines for Poll Guide settings.

### [](#styling)Styling

Use the following guidelines for Styling settings.

| Setting                      | Description                                                                                           |
| ---------------------------- | ----------------------------------------------------------------------------------------------------- |
| Theme                        | Do not change the Theme for a Poll without a good reason and express permission.                      |
| Step 1 Name                  | Adding a name to the Step for a Poll is optional.                                                     |
| Caret                        | Polls do not use a caret.                                                                             |
| Backdrop                     | Do not enable the Backdrop for a Poll.                                                                |
| Close Button                 | Enable the Close Button.                                                                              |
| Dimensions                   | You should not need to change the default Width dimension for a Poll.                                 |
| ARIA Label - Accessible Name | Use your Guide Name to provide an accessible name for the Poll. For example, Playground Feature Poll. |
| Role                         | Leave the Role as **Dialog**.                                                                         |
| Autofocus this step          | Leave **Autofocus this step** enabled.                                                                |
| ARIA Label - Close Button    | Leave as Close.                                                                                       |

### [](#location)Location

Use the following guidelines for Location settings.

| Setting           | Description                                                                                                                               |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Position On Page  | Set to **Bottom Right Aligned**. If you really want to emphasize a Poll, **Centered** is also acceptable.                                 |
| Anchor To Element | Do not anchor a Poll to an element.                                                                                                       |
| Page Location     | Set according to the needs of the Poll. Usually, this should be **Only on this page**. Some Guides may need to be displayed **Sitewide**. |

### [](#activation)Activation

All Polls should be set to activate **Automatically**.

## [](#guide-content)Guide Content

Use the following guidelines for developing Guide content.

### [](#titles)Titles

The main title for a Poll can be either **How did we do?** or **What do you think?**

Titles must be in bold.

### [](#subtitles)Subtitles

In the subtitle for a Poll:

| Description                                                                                      | Do                                                                                          | Don't                                                                                                                     |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Write the subtitle as a specific question, asking the user to rate or provide specific feedback. | **How would you rate the Playground?** **What did you think of the new Import experience?** | Please provide a rating. Let us know how we did. Rate your experience?                                                    |
| Write in sentence case.                                                                          | **What did you think of the new Query Workbench?**                                          | How Would You Rate The New Data Tools?                                                                                    |
| Write subtitles in bold font.                                                                    | **How would you rate the Data API tutorial?**                                               | How would you rate the Data API tutorial?                                                                                 |
| Don't use any other punctuation aside from a question mark.                                      | **How would you rate the new Connect page?**                                                | How would you rate the new Connect page for SDKs, Couchbase Shell, and Import and Export tools. We want to hear from you! |

### [](#hint-text)Hint Text

Hint text provides guidance on what the user needs to enter or what they're selecting on a Poll.

Don't change the default hint text for a Poll guide.

### [](#action-button)Action Button

The action button for a Poll guide should always be **Submit Feedback**.