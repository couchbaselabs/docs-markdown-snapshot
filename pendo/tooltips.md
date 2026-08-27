---
title: Tooltip Guides
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-style-guide/edit/main/pendo/modules/ROOT/pages/tooltips.adoc
  xref: xref:pendo::tooltips.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/pendo/tooltips.html)

# Tooltip Guides

Use the following guidance to write text for a Tooltip Guide.

A Tooltip can be either:

* [An Additional Information Tooltip](#additional): Provides a user with additional information about an element in the UI.
* [A Prerequisite Tooltip](#prereq): Directs a user to another location in the UI to complete a prerequisite task.

While Guide content changes based on the Tooltip type, some Guide configuration does not change:

* [Guide Name](#guide-name)
* [Guide Layout](#guide-layout)
* [Guide Category](#guide-category)
* [Guide Settings](#guide-settings)

## [](#guide-name)Guide Name

Start the Guide Name with **Tooltip -**.

Use the Guide Goal that you identified when writing your Guide Plan to create the Guide Name.

| Acceptable                  | Not Acceptable                                                      |
| --------------------------- | ------------------------------------------------------------------- |
| Tooltip - Set Query Context | Query Tooltip Query Context Tooltip Query Context Set Query Context |

## [](#guide-layout)Guide Layout

Use the following layouts depending on the type of Tooltip you want to create:

* Additional Info Tooltip
* Prereq Tooltip

## [](#guide-category)Guide Category

All Tooltips must be assigned the **Education > Education** Guide Category.

## [](#guide-settings)Guide Settings

Use the following guidelines for Tooltip Guide settings.

### [](#styling)Styling

Use the following guidelines for Styling settings.

| Setting                      | Description                                                                                                |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Theme                        | Do not change the Theme for a Tooltip without a good reason and express permission.                        |
| Step 1 Name                  | Adding a name to the Step for a Tooltip is optional.                                                       |
| Caret                        | Enable the Caret.                                                                                          |
| Backdrop                     | Do not enable the Backdrop for a Tooltip.                                                                  |
| Close Button                 | Enable the Close Button.                                                                                   |
| Dimensions                   | You should not need to change the default Width dimension for a Tooltip.                                   |
| ARIA Label - Accessible Name | Use your Guide Name to provide an accessible name for the Tooltip. For example, Set Query Context Tooltip. |
| Role                         | Leave the Role as **Dialog**.                                                                              |
| Autofocus this step          | Leave **Autofocus this step** enabled.                                                                     |
| ARIA Label - Close Button    | Leave as Close.                                                                                            |

### [](#location)Location

Use the following guidelines for Location settings.

| Setting             | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Position On Page    | Set to **Relative to Element**.                                                                                                                                                                                                                                                                                                                                                                                                   |
| Position to Element | Use **Auto**, or choose the location that provides the best visual result. Make sure the Tooltip is fully visible and legible.                                                                                                                                                                                                                                                                                                    |
| Anchor To Element   | The **Suggested Match** option after you select an element with **Anchor To Element** will rarely be specific enough for reliable Guide display. You will need to edit the CSS with the **Custom CSS** option. For some tips on syntax to try and use for targeting, see [Using CSS Selectors in Feature Tagging](https://support.pendo.io/hc/en-us/articles/360031863612-What-CSS-selectors-are-supported-for-feature-tagging-). |
| Page Location       | Set according to the needs of the Tooltip. Usually, this should be **Only on this page**. Some Guides may need to be displayed **Sitewide**.                                                                                                                                                                                                                                                                                      |

### [](#activation)Activation

All Tooltips should be set to activate through a **Badge**.

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

## [](#guide-content)Guide Content

Use the following guidelines for developing Guide content.

Guide content differs based on whether you are creating an [Additional Information Tooltip](#additional) or [Prerequisite Tooltip](#prereq).

### [](#additional)Additional Information Tooltips

Additional Information Tooltips should only contain:

* [A title](#add-title)
* [Body text](#add-body)

Don't add an action button to Additional Information Tooltips.

#### [](#title)Title

The title for an Additional Information Tooltip should be **What's this feature?** or **What does this mean?**

Titles must be in bold.

#### [](#add-body)Body Text

In the body text for an Additional Information Tooltip:

| Description                                                                                                                              | Do                                                                                                                                                                                                                     | Don't                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Avoid lengthy explanations for the target UI element. If you find yourself going over more than 2 short paragraphs, rethink the Tooltip. | Choose a database type: **Provisioned**: Have greater control over your deployment, with features designed for heavier workloads. **Serverless**: Let Couchbase manage your deployment while you focus on development. | Use a Provisioned database to manage all aspects of your Couchbase Capella database deployment. You can choose the combination of nodes and services that suits your workload needs, as well as the support plan you need for your database. Use a Serverless database to let Couchbase manage most aspects of your deployment for you.                                                                                                  |
| Use links to give the user additional context and explanation through the documentation.                                                 | Use a project to organize the databases in your organization. For more details, see the [Couchbase Documentation](#).                                                                                                  | Projects organize and control access to databases and App Services in your organization. You can view the projects available to you on the **Projects** tab. You can create a project if you have the **Project Creator** or **Organization Owner** role. If you don't have the **Project Creator** or **Organization Owner** role, you can only access and create databases and App Services in existing projects in your organization. |
| Use **bold** to emphasize UI element names.                                                                                              | **Database Access**                                                                                                                                                                                                    | _Database Access_                                                                                                                                                                                                                                                                                                                                                                                                                        |

### [](#prereq)Prerequisite Tooltips

Prerequisite Tooltips should contain:

* [A title](#prereq-title)
* [Body text](#prereq-body)
* [An action button](#prereq-action)

#### [](#prereq-title)Title

In the title for a Prerequisite Tooltip:

| Description                                                            | Do                                                                     | Don't                                                       |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------- |
| Write the title as an imperative phrase, starting with an action verb. | Set bucket, scope, and access Configure database access credentials    | Buckets, scopes, collections Query Context                  |
| Write in sentence case, but match capitalization of named UI elements. | Set Query Context Add a new bucket                                     | Add Your Database Access Credentials Add api key and secret |
| Don't use any other punctuation aside from commas, where needed.       | Set database name and region Get API Key, API Secret, and API endpoint | Set your database name! Are you sure you want to continue?  |

#### [](#prereq-body)Body Text

In the body text for a Prerequisite Tooltip:

| Description                                                                                            | Do                                                                                                              | Don't                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Avoid lengthy explanations about the how and why for the Tooltip. Stick to 1 or 2 sentences.           | To create a database, you need to create a project.                                                             | You need to create a project before you can create a database. All databases in Capella need to exist inside a project. You can select an existing project from the list, or you can go to the **Projects** tab to create a new project.                                               |
| Clearly state the goal or benefit to the user, followed by where the Tooltip will take them in the UI. | To connect to your database, go to **Database Access** and add database access credentials.                     | Click **Let's go!** to connect to your database.                                                                                                                                                                                                                                       |
| Use links to give the user additional context and explanation through the documentation.               | To create an App Service, create a compatible database. For more details, see the [Couchbase Documentation](#). | You don't have any compatible databases where you can create an App Service. You need to create a database to create an App Service. The database must have the Data, Index, and Query services. It must have at least one bucket, and not have an App Service currently linked to it. |
| Use **bold** to emphasize UI element names.                                                            | **Database Access**                                                                                             | _Database Access_                                                                                                                                                                                                                                                                      |

#### [](#prereq-action)Action Button

Prerequisite Tooltips must have an action button.

The action button should always say **Let's go!**.

Above the action button, make sure you add a code block with the following JavaScript, replacing the variables with the appropriate values:

```javascript
if(!pendo.designerEnabled){
function getUrl(url) {
  // Get the query string from the current URL
  const queryParams = window.location.search;

  // Append the query string to the specified URL, and add an optional permalink to another Pendo Guide at the destination URL
  const newUrl = url + queryParams + '$OPTIONAL_PENDO_PERMALINK';

  // Open the new URL in a new window
  window.open(newUrl, '_blank');
}

// Replace $PARTIAL_URL with everything after https://cloud.couchbase.com/, stopping before the ? in the URL you want to go to
pendo.dom('._pendo-button-primaryButton')[0].addEventListener("click", function () {
    	getUrl('$PARTIAL_URL');
});
}
```