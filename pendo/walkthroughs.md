---
title: Walkthrough Guides
editUrl: https://github.com/couchbaselabs/docs-style-guide/edit/main/pendo/modules/ROOT/pages/walkthroughs.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:pendo::walkthroughs.adoc[]
---

[View original HTML](/pendo/walkthroughs.html)

# Walkthrough Guides

Use the following guidance to write text for a Walkthrough Guide.

A Walkthrough takes a user through a series of Steps to complete a specific task in the UI:

![The Walkthrough Guide template from the Pendo Designer. The top of the dialog has the template text 'STEP X OF Y'. The title is 'Target/Task name'. The body text states 'Provide a brief instruction or explanation about this Step or feature in the walkthrough. What can the user do or achieve with this?' The bottom of the dialog contains the standard Next and Back buttons.](_images/walkthrough-guide.png) 

## [](#guide-name)Guide Name

Start the Guide Name with **Walkthrough -**.

Use the Guide Goal that you identified when writing your Guide Plan to create the Guide Name.

| Acceptable                                                       | Not Acceptable                                                                                                           |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Walkthrough - Connect Database Walkthrough - Database Connection | Connect Database Guide Connect guide Connection guide Database connection walkthrough guide Connect Database Walkthrough |

## [](#guide-layout)Guide Layout

Use the following layouts based on the Step you need to create in the Walkthrough Guide:

* First Step
* Next Step
* Final Step

## [](#guide-category)Guide Category

All Walkthroughs must be assigned the **Education > Onboarding** Guide Category.

## [](#guide-settings)Guide Settings

Use the following guidelines for Walkthrough Guide settings.

> [!NOTE]
> You must configure the [Styling](#styling), [Location](#location) and [Behavior](#behavior) settings for each Step in a Walkthrough.

### [](#styling)Styling

Use the following guidelines for Styling settings.

| Setting                      | Description                                                                                                                                                          |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Theme                        | Do not change the Theme for a Walkthrough without a good reason and express permission.                                                                              |
| Step 1 Name                  | Add a name to each Step for a Walkthrough. Try to provide a descriptive name that describes what the user needs to do for that Step. For example, Set Query Context. |
| Caret                        | If your Walkthrough Step is positioned relative to an element, enable the Caret.                                                                                     |
| Backdrop                     | Do not enable the Backdrop for a Walkthrough Step.                                                                                                                   |
| Close Button                 | Enable the Close Button.                                                                                                                                             |
| Dimensions                   | You should not need to change the default Width dimension for a Walkthrough Step.                                                                                    |
| ARIA Label - Accessible Name | Use your Step Name to provide an accessible name for the Walkthrough Step, with the phrase helper dialog. For example, Set Query Context helper dialog.              |
| Role                         | Leave the Role as **Dialog**.                                                                                                                                        |
| Autofocus this Step          | Leave **Autofocus this step** enabled.                                                                                                                               |
| ARIA Label - Close Button    | Leave as Close.                                                                                                                                                      |

### [](#location)Location

Use the following guidelines for Location settings.

| Setting                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Position On Page                                     | Position on Page depends on the Walkthrough Step: First Step: **Relative to Element** or **Bottom Right Aligned** Subsequent Step: **Relative to Element** Final Step: **Centered**                                                                                                                                                                                                                                               |
| Offset                                               | For **Bottom Right Aligned** steps, leave the Offset as 20px by 20px.                                                                                                                                                                                                                                                                                                                                                             |
| Position to Element (Relative to Element Steps Only) | Use **Auto**, or choose the location that provides the best visual result. Make sure the Step is fully visible and legible.                                                                                                                                                                                                                                                                                                       |
| Anchor To Element (Relative to Element Steps Only)   | The **Suggested Match** option after you select an element with **Anchor To Element** will rarely be specific enough for reliable Guide display. You will need to edit the CSS with the **Custom CSS** option. For some tips on syntax to try and use for targeting, see [Using CSS Selectors in Feature Tagging](https://support.pendo.io/hc/en-us/articles/360031863612-What-CSS-selectors-are-supported-for-feature-tagging-). |
| Page Location                                        | Set according to the needs of the Walkthrough. Usually, this should be **Only on this page**. Some Guides may need to be displayed **Sitewide**.                                                                                                                                                                                                                                                                                  |

### [](#behavior)Behavior

Use the following guidelines for Step Behavior.

| Setting                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Close Button             | Do not change or remove the Close Button action.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Advance on Element Click | The actions for a Step depend on the purpose of the Step: If the user must put text or another input into the current UI element to complete the next Steps in your Walkthrough, delete the **Advance on Element Click** action. Keep all other actions. If the user must click the current element UI to complete the next Steps in your Walkthrough, keep the **Advance on Element Click** action and delete all other actions. If the Step is more informational or does not require a user interaction, delete the **Advance on Element Click** action. Keep all other actions. |

### [](#activation)Activation

Walkthroughs can use any of the Activation types:

* Automatically
* [Badge](#badge-settings)
* [Target Element](#target-element-settings)

#### [](#badge-settings)Badge Settings

Use the following guidelines for Badge Styling and Behavior.

| Setting                                | Description                                                                                                                                                                                                                                                                             |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Styling > Badge Icon                   | Use the ![A black circle with a white question mark inside.](_images/preferred-badge-icon.png) badge icon. If the badge needs to display on a button that’s the same color as the badge, use the ![A white circle with a black question mark inside.](_images/alt-badge-icon.png) icon. |
| Styling > Position                     | For accessibility, always set Position to **Inline Right**.                                                                                                                                                                                                                             |
| Styling > Offset                       | Set the Offset to achieve the best visual result. Keep the badge close to the specific element, but leave some breathing room.                                                                                                                                                          |
| Styling > Color                        | Set the color to Capella’s primary color: #0266C2.                                                                                                                                                                                                                                      |
| Styling > Z-Index                      | You should not need to change the badge’s Z-Index.                                                                                                                                                                                                                                      |
| Styling > ARIA Label - Accessible Name | Set to <Element Name> tooltip badge.                                                                                                                                                                                                                                                    |
| Behavior > Guide Behavior              | Set to **Show only on badge click**.                                                                                                                                                                                                                                                    |
| Behavior > Badge Behavior              | Set to **Always show badge**.                                                                                                                                                                                                                                                           |
| Behavior > Frequency                   | Set to **Show every time**.                                                                                                                                                                                                                                                             |

#### [](#target-element-settings)Target Element Settings

Use the following guidelines for Target Element Location and Behavior.

| Setting                     | Description                                                                                 |
| --------------------------- | ------------------------------------------------------------------------------------------- |
| Location > Element Location | Set to **Inherit from Step 1**. Your first Step must be positioned **Relative to Element**. |
| Behavior > Guide Behavior   | Set to **Show only on element click**.                                                      |
| Behavior > Frequency        | Set to **Show only once**.                                                                  |

## [](#guide-content)Guide Content

Use the following guidelines for developing Guide content.

### [](#progress-tracker)Progress Tracker

Every Walkthrough Guide should contain a progress tracker at the top of the Guide dialog.

> [!TIP]
> Finalize the progress tracker when you’re finished designing the rest of your guide.

Fill in the template with the Step number the user is currently on, out of the total number of Steps, for each Step.

For example, `STEP 1 OF 10`.

Write in all capital letters, for aesthetic reasons.

### [](#titles)Titles

The content style for a title changes based on what Step you’re writing in the Walkthrough.

#### [](#first-steps)First Steps

In the title for the first Step of a Walkthrough:

| Description                                                                                      | Do                                                                       | Don’t                                                                                                                                        |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Write the title as a question. Try to make the question specific to the goal of the Walkthrough. | Want some help creating credentials? Want some help creating a database? | Want help? Need help getting started with this?                                                                                              |
| Write in sentence case.                                                                          | Want some help creating a project?                                       | Want Some Help Creating a Project?                                                                                                           |
| Don’t use any other punctuation aside from a question mark.                                      | Want some help adding an allowed IP address?                             | Want some help adding an allowed IP address, database access credentials, and connecting to your database? Want some help to get this done?! |

#### [](#subsequent-steps)Subsequent Steps

In the title for any subsequent Steps of a Walkthrough:

| Description                                                            | Do                                               | Don’t                                            |
| ---------------------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------ |
| Write the title as an imperative phrase, starting with an action verb. | Set bucket, scope, and access                    | Want help? Need to change your project name?     |
| Write in sentence case, but capitalize named UI elements.              | Set Query Context Set database password          | Add Your IP Address                              |
| Don’t use any other punctuation aside from commas, where needed.       | Set bucket, scope, and access Set document limit | Add an allowed IP address. Change your password! |

#### [](#final-steps)Final Steps

In the title for the final Step of a Walkthrough:

| Description                                                                | Do                                                       | Don’t                                                                 |
| -------------------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------- |
| Write the title as an imperative phrase, starting with an action verb.     | Explore other database features a                        | Want to explore other database features? Do you know what to do next? |
| Write in sentence case, but capitalize named UI elements.                  | Upload documents to your database Explore the Playground | Upload Documents To Your Database Explore the playground              |
| Keep it short, but encourage the user to keep going after the Walkthrough. | Go to the Documents Viewer                               | You’re done!                                                          |

### [](#body-text)Body Text

The body text goals for a Walkthrough Step change based on whether you’re writing for the first Step or a subsequent Step.

#### [](#first-steps-2)First Steps

In the body text for the first Step of a Walkthrough:

| Description                                                                                                                                  | Do                                                                                                  | Don’t                                                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clearly state what the user will learn after they complete the Walkthrough. Start the sentence with "Follow along with a brief tutorial to". | Follow along with a brief tutorial to create database access credentials for your Capella database. | Follow along with this brief tutorial to get started. Use this tutorial to get started.                                                                                                                                                      |
| Avoid writing more than 1 sentence. Keep the goal brief and straightforward.                                                                 | Follow along with a brief tutorial to add an allowed IP address for your Capella database.          | Follow along with a brief tutorial to create an API Key for your Capella database. You can use an API Key to connect to your database with the Data API. Use the Data API to work with scopes and collections, documents, and SQL++ queries. |

#### [](#subsequent-steps-2)Subsequent Steps

In the body text for any subsequent Steps of a Walkthrough:

| Description                                                                                                                                                                                                                                                                                                                                                                                                                                     | Do                                                                                                              | Don’t                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Avoid lengthy explanations about the how and why for the Step. Stick to 1 or 2 sentences.                                                                                                                                                                                                                                                                                                                                                       | To create a database, you need to create a project. Go to the **Projects** tab.                                 | You need to create a project before you can create a database. All databases and App Services in Capella need to exist inside a project. Projects exist at the organization level. Go to the **Projects** tab to create a new project.                                                 |
| If the Step requires the user to interact with the UI, remove the Next and Back buttons from the Step. Make it clear that the user needs to interact with the UI to advance the guide. If the interaction you need the user to take requires their keyboard, keep the Next and Back buttons. Don’t let the guide advance when the user clicks the element, so they can type the required text. For more information, see [Behavior](#behavior). | Go to **Database Access**.                                                                                      | The **Database Access** page lets you add database access credentials.                                                                                                                                                                                                                 |
| Don’t mention the Next and Back buttons in your Step text.                                                                                                                                                                                                                                                                                                                                                                                      | Click **Create Database**.                                                                                      | Click **Next** to go to the next step in this guide. Click **Back** to go to the previous step.                                                                                                                                                                                        |
| Use links to give the user additional context and explanation through the documentation.                                                                                                                                                                                                                                                                                                                                                        | To create an App Service, create a compatible database. For more details, see the [Couchbase Documentation](#). | You don’t have any compatible databases where you can create an App Service. You need to create a database to create an App Service. The database must have the Data, Index, and Query services. It must have at least one bucket, and not have an App Service currently linked to it. |
| Use **bold** to emphasize UI element names.                                                                                                                                                                                                                                                                                                                                                                                                     | **Database Access**                                                                                             | _Database Access_                                                                                                                                                                                                                                                                      |

#### [](#final-steps-2)Final Steps

In the body text for the final Step of a Walkthrough:

| Description                                                                                                                                                | Do                                                                                                                   | Don’t                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stick to 1 or 2 sentences about some suggestions for what the user can do after they have completed the Walkthrough. Encourage the user to stay in the UI. | Find more examples for how to work with the Couchbase SDKs in the Playground.                                        | If you want more examples, you can check out the Playground. The Playground contains interactive tutorials that you can use to learn more about Capella without leaving your browser. You can access the Playground at any time. Go check out the Couchbase Documentation for more details. |
| Don’t mention the Finish and Back buttons in your Step text.                                                                                               | Keep running queries in the query editor, explore the Playground, or explore other Data Tools and database features. | Click **Finish** to close this guide. Click **Back** to go to the previous step.                                                                                                                                                                                                            |
| Use **bold** to emphasize UI element names.                                                                                                                | **Database Access**                                                                                                  | _Database Access_                                                                                                                                                                                                                                                                           |