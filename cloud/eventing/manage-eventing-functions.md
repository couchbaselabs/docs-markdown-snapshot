---
title: Manage Eventing Functions
description: Use the Capella UI to manage the Eventing Functions in your cluster.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/eventing/pages/manage-eventing-functions.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:cloud:eventing:manage-eventing-functions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/eventing/manage-eventing-functions.html)

# Manage Eventing Functions

> Use the Capella UI to manage the Eventing Functions in your cluster. 

## [](#pause-function)Pause a Function

You can pause an Eventing Function to checkpoint the Function and stop processing document mutations. This checkpoint saves a specific point in the processing stream and helps you not miss any mutations when you resume the Function.

You can edit the JavaScript code of a paused Function.

> [!NOTE]
> You can only pause an Eventing Function when that Function has already been deployed.

To pause an Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Next to the Function you want to pause, click **More Options (⋮)** .
3. Click **Pause**.

## [](#resume-function)Resume a Function

You can resume a paused Eventing Function to reactivate and continue processing the Function.

When you resume a Function:

* The Function starts running from the checkpoint that was saved when you previously paused the Function. This makes sure that no document mutations are missed.
* All backlogged mutations are processed.
* All backlogged Timers fire as soon as possible, making sure no Timers are lost.

You cannot edit the JavaScript code of a resumed Function.

To resume an Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **More Options (⋮)** next to the Function you want to resume.
3. Click **Resume** to resume your Function. A resumed Function enters a deployed state and resumes processing mutations.

## [](#export-function)Export a Function

You can export an Eventing Function to open and edit the Function with your code editor. The Function exports in JSON format.

To export an Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **More Options (⋮)** next to the Function you want to export.
3. Click **Export** to export your Function.
4. Go to the **Downloads** folder on your computer.
5. Open the exported JSON file with your code editor.

## [](#function-logs)Debug with Function Logs

You can use Function logs to identify and capture activities and errors related to your business logic through user-defined messages specific to each Eventing Function.

The content of the Function logs depends on the logic of the `log(…​)` statements you added inside the Function handler's JavaScript code.

To check the logs of your deployed Function:

1. Go to **Data Tools** **Eventing**.
2. Click the **Log** icon next to the Function you want to check the logs for.
3. In the **Logs** page, you can:

  * Filter the log content
  * Reorder the log file
  * Refresh the log data
  * Copy the log data to your clipboard

## [](#edit-javascript)Edit a Function's JavaScript Code

> [!NOTE]
> You can only edit the JavaScript code of an Eventing Function when that Function is paused or undeployed.

To edit the JavaScript code of an Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **View JavaScript** next to the Function you want to edit.
3. In the code editor page, edit your business logic.
4. Click **Save** to commit your changes.

## [](#edit-settings)Edit Function Settings

To edit the settings of your Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **Settings** next to the Function you want to edit the settings for.
3. Edit the available settings. You can also edit the Function's bindings and JavaScript code.
4. Click **Save**.

If your Eventing Function is in a deployed state, you can only edit some of its settings. To edit a larger number of your Function's settings, undeploy or pause your Function.

| Field                             | Description                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------ |
| Name                              | Cannot be edited.                                                                          |
| Source Bucket                     | Cannot be edited.                                                                          |
| Source Scope                      | Cannot be edited.                                                                          |
| Source Collection                 | Cannot be edited.                                                                          |
| Metadata Bucket                   | Cannot be edited.                                                                          |
| Metadata Scope                    | Cannot be edited.                                                                          |
| Metadata Collection               | Cannot be edited.                                                                          |
| Description                       | Can be edited at any time.                                                                 |
| N1QL Consistency                  | Can be edited at any time.                                                                 |
| Workers                           | Can be edited at any time.                                                                 |
| Script Timeout                    | Can be edited at any time.                                                                 |
| Deployment Feed Boundary          | Can only be edited when the Function is in an undeployed or paused state.                  |
| Timer Context Max Size            | Can only be edited when the Function is in an undeployed or paused state.                  |
| Language Compatibility            | Can only be edited when the Function is in an undeployed or paused state.                  |
| Enable App Services Compatibility | Can only be edited when the Function does not share the same collection as an App Service. |

## [](#delete-function)Delete a Function

> [!NOTE]
> You can only delete an Eventing Function if the Function is undeployed.

To delete an Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **More Options (⋮)** next to the Function you want to delete.
3. Click **Delete**.
4. In the **Delete function** dialog, type delete to confirm your action.
5. Click **Delete**.