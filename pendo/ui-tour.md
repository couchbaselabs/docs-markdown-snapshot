---
title: UI Tour Guides
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-style-guide/edit/main/pendo/modules/ROOT/pages/ui-tour.adoc
  xref: xref:pendo::ui-tour.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/pendo/ui-tour.html)

# UI Tour Guides

Use the following guidance to write text for a UI Tour Guide.

A UI Tour takes a user through a series of Steps to showcase a particular area of the UI:

![The UI Tour Guide template from the Pendo Designer. The top of the dialog has the template text 'STEP X OF Y'. The title is 'Target/Task name'. The body text states 'Provide a brief instruction or explanation about this Step or feature in the walkthrough. What can the user do or achieve with this?' The bottom of the dialog contains the standard Next and Back buttons.](_images/walkthrough-guide.png) 

## [](#guide-name)Guide Name

Start the Guide Name with **UI Tour -**.

Use the Guide Goal that you identified when writing your Guide Plan to create the Guide Name.

| Acceptable                | Not Acceptable                                                          |
| ------------------------- | ----------------------------------------------------------------------- |
| UI Tour - Document Viewer | Document Viewer UI Document tour Documents Tour Document Viewer UI Tour |

## [](#guide-layout)Guide Layout

Use the following layouts based on the Step you need to create in the UI Tour Guide:

* First Step
* Next Step
* Final Step

## [](#guide-category)Guide Category

All UI Tours must be assigned the **Education > Onboarding** Guide Category.

## [](#guide-settings)Guide Settings

Use the following guidelines for UI Tour Guide settings.

> [!NOTE]
> You must configure the [Styling](#styling), [Location](#location) and [Behavior](#behavior) settings for each Step in a UI Tour.

### [](#styling)Styling

Use the following guidelines for Styling settings.

| Setting                            | Description                                                                                                                                                           |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Theme                              | Do not change the Theme for a UI Tour without a good reason and express permission.                                                                                   |
| Step 1 Name                        | Add a name to each Step for a UI Tour. Try to provide a descriptive name that describes what element of the UI you're showing in that Step. For example, Bucket list. |
| Caret                              | If your UI Tour Step is positioned relative to an element, enable the Caret.                                                                                          |
| Backdrop                           | For every Step except the first and final Steps of a UI tour, enable the Backdrop.                                                                                    |
| Show target element above backdrop | If **Backdrop** is enabled, always enable **Show target element above backdrop**.                                                                                     |
| Close Button                       | Enable the Close Button.                                                                                                                                              |
| Dimensions                         | You should not need to change the default Width dimension for a UI Tour Step.                                                                                         |
| ARIA Label - Accessible Name       | Use your Step Name to provide an accessible name for the UI Tour Step, with the phrase helper dialog. For example, Bucket list helper dialog.                         |
| Role                               | Leave the Role as **Dialog**.                                                                                                                                         |
| Autofocus this Step                | Leave **Autofocus this step** enabled.                                                                                                                                |
| ARIA Label - Close Button          | Leave as Close.                                                                                                                                                       |

### [](#location)Location

Use the following guidelines for Location settings.

| Setting                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Position On Page                                     | Position on Page depends on the UI Tour Step: First Step: **Relative to Element** or **Bottom Right Aligned** Subsequent Step: **Relative to Element** Final Step: **Centered**                                                                                                                                                                                                                                                   |
| Offset                                               | For **Bottom Right Aligned** steps, leave the Offset as 20px by 20px.                                                                                                                                                                                                                                                                                                                                                             |
| Position to Element (Relative to Element Steps Only) | Use **Auto**, or choose the location that provides the best visual result. Make sure the Step is fully visible and legible.                                                                                                                                                                                                                                                                                                       |
| Anchor To Element (Relative to Element Steps Only)   | The **Suggested Match** option after you select an element with **Anchor To Element** will rarely be specific enough for reliable Guide display. You will need to edit the CSS with the **Custom CSS** option. For some tips on syntax to try and use for targeting, see [Using CSS Selectors in Feature Tagging](https://support.pendo.io/hc/en-us/articles/360031863612-What-CSS-selectors-are-supported-for-feature-tagging-). |
| Page Location                                        | Set according to the needs of the UI Tour. Usually, this should be **Only on this page**. Some Guides may need to be displayed **Sitewide**.                                                                                                                                                                                                                                                                                      |

### [](#behavior)Behavior

Use the following guidelines for Step Behavior.

| Setting                  | Description                                                                                                            |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| Close Button             | Do not change or remove the Close Button action.                                                                       |
| Advance on Element Click | Delete the **Advance on Element Click** action. Keep all other actions. Never delete the **Next** or **Back** buttons. |

### [](#activation)Activation

UI Tours can use any of the Activation types:

* Automatically
* [Badge](#badge-settings)
* [Target Element](#target-element-settings)

#### [](#badge-settings)Badge Settings

Use the following guidelines for Badge Styling and Behavior.

| Setting                                | Description                                                                                                                                                                                                                                                                             |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Styling > Badge Icon                   | Use the ![A black circle with a white question mark inside.](_images/preferred-badge-icon.png) badge icon. If the badge needs to display on a button that's the same color as the badge, use the ![A white circle with a black question mark inside.](_images/alt-badge-icon.png) icon. |
| Styling > Position                     | For accessibility, always set Position to **Inline Right**.                                                                                                                                                                                                                             |
| Styling > Offset                       | Set the Offset to achieve the best visual result. Keep the badge close to the specific element, but leave some breathing room.                                                                                                                                                          |
| Styling > Color                        | Set the color to Capella's primary color: #0266C2.                                                                                                                                                                                                                                      |
| Styling > Z-Index                      | You should not need to change the badge's Z-Index.                                                                                                                                                                                                                                      |
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

Every UI Tour Guide should contain a progress tracker at the top of the Guide dialog.

> [!TIP]
> Finalize the progress tracker when you're finished designing the rest of your guide.

Fill in the template with the Step number the user is currently on, out of the total number of Steps, for each Step.

For example, `STEP 1 OF 10`.

Write in all capital letters, for aesthetic reasons.

### [](#titles)Titles

The content style for a title changes based on what Step you're writing in the UI Tour.

#### [](#first-steps)First Steps

In the title for the first Step of a UI Tour:

| Description                                                                                                                                      | Do                                                                                  | Don't                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Write the title as a question, based on **Want a quick tour of ?**. Try to make the question specific to the goal of the UI Tour. Keep it short. | Want a quick tour of the Document Viewer? Want a quick tour of the Query Workbench? | Want help? Need help getting started with this?                                                                                                                           |
| Write in sentence case.                                                                                                                          | Want a quick tour of the Databases page?                                            | Want A Quick Tour Of The Databases Page?                                                                                                                                  |
| Don't use any other punctuation aside from a question mark.                                                                                      | Want a quick tour of the Settings page?                                             | Want a quick tour of the Connect page, for how to add an allowed IP address, database access credentials, and connect to your database? Want some help to get this done?! |

#### [](#subsequent-steps)Subsequent Steps

In the title for any subsequent Steps of a UI Tour:

| Description                                                                                                                                                   | Do                                                              | Don't                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------- |
| Write the title as a noun or imperative phrase, stating the UI element name or what the user can do with the UI element. Try not to just restate the obvious. | Limit box Search for documents Bucket list Create new documents | This is the Limit box Get Documents button Filter by ID |
| Write in sentence case, but capitalize named UI elements.                                                                                                     | Set Query Context Set database password                         | Add Your IP Address                                     |
| Don't use any other punctuation aside from commas, where needed.                                                                                              | Set bucket, scope, and access Set document limit                | Add an allowed IP address. Change your password!        |

#### [](#final-steps)Final Steps

In the title for the final Step of a UI Tour:

| Description                                                            | Do                                                       | Don't                                                                 |
| ---------------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------- |
| Write the title as an imperative phrase, starting with an action verb. | Explore other database features a                        | Want to explore other database features? Do you know what to do next? |
| Write in sentence case, but capitalize named UI elements.              | Upload documents to your database Explore the Playground | Upload Documents To Your Database Explore the playground              |
| Keep it short, but encourage the user to keep going after the UI Tour. | Go to the Documents Viewer                               | You're done!                                                          |

### [](#body-text)Body Text

The content style for a body text changes based on what Step you're writing in the UI Tour.

#### [](#first-steps-2)First Steps

In the body text for the first Step of a UI Tour:

| Description                                                                                                        | Do                                                                                                    | Don't                                                                                   |
| ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Clearly state what the user can do with the feature area you're trying to demonstrate. Try to stick to 1 sentence. | Use the Document Viewer to explore the documents in your database.                                    | The Document Viewer shows you documents. Follow along with a quick tour to get started. |
| Include the phrase "Let's show you some other key features!"                                                       | Use the Query Workbench to run SQL++ queries in your browser. Let's show you some other key features! | The Query Workbench has some key features. Let's show you those features.               |

#### [](#subsequent-steps-2)Subsequent Steps

In the body text for any subsequent Steps of a UI Tour:

| Description                                                                                                              | Do                                                                                                                                                                        | Don't                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Avoid lengthy explanations about a specific UI element in a Step. Stick to 1 or 2 sentences about the what and why.      | Use the **Filter by** toggle to add a filter to the documents in the Document Viewer. You can filter by a document ID value, a range of IDs, or use a SQL++ WHERE clause. | Use the **Filter by** toggle to filter the documents in the Document Viewer. If you set the toggle to **ID**, you can enter an ID value as a filter. If you set the toggle to **ID Range**, you can set a range of ID values as a filter. If you set the toggle to \*SQL WHERE\*, you can enter a SQL WHERE clause to find specific documents. |
| Don't mention the Next and Back buttons in your Step text. Never remove the **Next** and **Back** buttons for a UI Tour. | Use the **Bucket** list to choose the bucket where you want to load documents. The Document Viewer will only show documents from this bucket.                             | Click **Next** to go to the next step in this guide. Click **Back** to go to the previous step.                                                                                                                                                                                                                                                |
| Use links to give the user additional context and explanation through the documentation.                                 | To create an App Service, create a compatible database. For more details, see the [Couchbase Documentation](#).                                                           | If you don't have any compatible databases where you can create an App Service, you will need to create a database. The database must have the Data, Index, and Query services. It must have at least one bucket, and not have an App Service currently linked to it.                                                                          |
| Use **bold** to emphasize UI element names.                                                                              | **Database Access**                                                                                                                                                       | _Database Access_                                                                                                                                                                                                                                                                                                                              |

#### [](#final-steps-2)Final Steps

In the body text for the final Step of a UI Tour:

| Description                                                                                                                                            | Do                                                                                                                   | Don't                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stick to 1 or 2 sentences about some suggestions for what the user can do after they have completed the UI Tour. Encourage the user to stay in the UI. | Check out the other Data Tools to keep exploring your data inside Capella.                                           | Use the other Data Tools to keep exploring your data inside Capella. You can use the Query tab to open the Query Workbench and run SQL++ queries from right inside your browser. You can use the Search tab to create Search indexes and add full-text search capabilities to your database. You can also check out the Playground for interactive examples with the Couchbase SDKs and the Data API. You can access the Playground at any time. Go check out the Couchbase Documentation for more details. |
| Don't mention the Finish and Back buttons in your Step text.                                                                                           | Keep running queries in the query editor, explore the Playground, or explore other Data Tools and database features. | Click **Finish** to close this guide. Click **Back** to go to the previous step.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Use **bold** to emphasize UI element names.                                                                                                            | **Database Access**                                                                                                  | _Database Access_                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |