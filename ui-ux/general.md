---
title: General UI Copy Principles
editUrl: https://github.com/couchbaselabs/docs-style-guide/edit/main/ui-ux/modules/ROOT/pages/general.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:ui-ux::general.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ui-ux/general.html)

# General UI Copy Principles

The following are some general principles for UI copy in the Couchbase Style:

* [Write in American English](#american)
* [Write in the Present Tense](#present)
* [Write in Second Person](#second)
* [Use Active Voice](#active)
* [Keep It Plain, Short, and Simple](#simple)
* [Write for the Lowest Common Denominator](#lowest)
* [Explain What’s Critical](#critical)
* [Focus on What the User Can Do](#can-do)
* [Keep It Consistent](#consistent)
* [Do Not Write Out Numbers](#numbers)

For an overview of voice and tone, see [Couchbase UI Voice](voice.md).

## [](#american)Write in American English

Use American English spelling, not British or Canadian English.

If you need to check the spelling of a word, refer to the [Merriam-Webster’s Collegiate Dictionary, Eleventh Edition](https://www.merriam-webster.com/).

## [](#present)Write in the Present Tense

Try to write in present tense wherever possible.

If you need to refer to something that’s happened in the past or will happen in the UI, then using past or future tense is acceptable - but try to avoid it.

| Acceptable                                                    | Not Acceptable                                                                                                                               |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Use a Project to organize the databases in your organization. | You will use a Project to organize the databases in your organization. You’ve used a Project to organize the databases in your organization. |

For more information, see [Present tense](https://developers.google.com/style/tense) in the Google Developer Style Guide.

## [](#second)Write in Second Person

Try to always directly address the user in your UI copy, with "you."

Do not use any third person gendered pronouns.

You can use first-person in specific circumstances. For more information, see [First-Person](first-person.md).

| Acceptable                                                                                            | Not Acceptable                                                                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| You can change the **Description** for your cluster from the **Settings** page.                       | We can change the **Description** for a cluster from the **Settings** page. Let’s change our cluster’s description.                                                                                       |
| A **Project Owner** can create, modify, and delete buckets. You can create a maximum of 30 buckets. a | A **Project Owner** can create, modify, and delete buckets. He can create a maximum of 30 buckets. A **Project Owner** can create, modify, and delete buckets. He/she can create a maximum of 30 buckets. |

## [](#active)Use Active Voice

Passive voice weakens your writing and can make it harder to parse meaning. Stick to the active voice as much as you can.

Start sentences with verbs, or directly address the user to avoid passive voice.

| Acceptable                                                                         | Not Acceptable                                                     |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Couchbase Server uses scopes and collections to categorize and organize documents. | Documents are categorized and organized by scopes and collections. |
| Before you can store any data, you must create a Bucket.                           | Buckets must be created before you can store any data.             |

Try to write in imperatives - give the user instructions, do not just explain features.

### [](#tips-for-active-voice)Tips for Active Voice

Here are some tips to help you with active voice:

* Think about what’s actually _doing_ the action you’re describing. Emphasize the actor.
* Find or push back for more information if you cannot identify the actor. Ask the developer what’s actually doing what in a scenario.
* If the sentence does not make sense in active voice or you lose the correct emphasis, you can use the passive voice.

For more information about active voice, see [Active voice](https://developers.google.com/style/voice) in the Google Developer Style Guide.

## [](#simple)Keep It Plain, Short, and Simple

Plain language means avoiding jargon or overly technical phrases when a simpler word works best.

Always write in full and complete sentences outside of headings.

Keep text short and to the point.

Choose short words - try to stick to 3 syllables or fewer.

Use contractions, with some exceptions. For more information, see [Contractions](contractions.md).

| Acceptable                                                                         | Not Acceptable                                                                        |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| You can set a Bucket name.                                                         | You can configure a Bucket name.                                                      |
| Before you can use your Capella cluster from your VPC, run the following commands. | Before you can access your Capella cluster from your VPC, run the following commands. |
| You cannot connect a hosted zone through the AWS CLI command in Capella.           | You can’t associate the hosted zone via the AWS CLI command in Capella.               |
| Activate your Capella cluster.                                                     | Start your Capella database.                                                          |
| Add additional nodes.                                                              | Add more nodes.                                                                       |
| Adhere to the following character restrictions.                                    | Follow these character limits.                                                        |
| Advise your administrator of the problem.                                          | Tell your administrator about the problem.                                            |
| We appreciate your patience.                                                       | We value your patience.                                                               |
| Associate your credit card with your account.                                      | Connect your credit card to your account.                                             |
| Set the effective date for your schedule.                                          | Set your schedule start date.                                                         |
| Eliminate any unnecessary nodes.                                                   | Remove any unnecessary nodes.                                                         |
| Enable the client to access your database.                                         | Allow the client to use your database.                                                |

## [](#lowest)Write for the Lowest Common Denominator

The golden rule for when to add UI copy or text is simple:

If a lower-level user would struggle or the required action is not obvious, add the text.

We want our UI to be accessible to all users and should always aim to add text to reduce friction.

## [](#critical)Explain What Is Critical

Keep to the most critical and important information when adding UI copy.

Lengthy explanations or unusual situations should be explained in the documentation, not the UI.

## [](#can-do)Focus on What the User Can Do

When writing an [error message](error-messages.md) or any kind of text guiding a user away from an action, do not reveal or focus on their lack of permissions.

Focus on what the user can do in their current situation, unless there’s no other option than to ask an administrator about their permissions.

## [](#consistent)Keep It Consistent

Keep the terminology that you use consistent across the UI.

What’s called a cluster in one part of the UI should not be called a database elsewhere.

## [](#numbers)Do Not Write Out Numbers

Unlike technical documentation, UI copy should always use numerals for ease of recognition. Use 3 over three.

Also aim to add units of measurement for numbers, where applicable.