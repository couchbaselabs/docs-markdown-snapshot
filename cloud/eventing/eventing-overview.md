---
title: Run a Function on Data Change
description: Use the Eventing Service to handle data changes that happen when
  code is executed in response to document mutations or as scheduled by Timers.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/eventing/pages/eventing-overview.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/eventing/eventing-overview.html)

# Run a Function on Data Change

> Use the Eventing Service to handle data changes that happen when code is executed in response to document mutations or as scheduled by Timers. 

## [](#eventing-service)Eventing Service

The Eventing Service executes user-defined business logic and responds in real time whenever applications interact and cause your data to change. This change in data is known as a document mutation, and includes operations such as insert, delete, update, and expiration.

You can use the Eventing Service to:

* Monitor specific parameters in a document
* Set alerts in a document when a preconfigured threshold is breached
* Propagate data changes inside a database
* Enrich documents in real time
* Cascade deletes to avoid orphaned documents

## [](#eventing-functions)Eventing Functions

The Eventing Service can run one or more Eventing Functions in your database to handle data changes according to a real-time Event-Condition-Action model. Eventing Functions are standalone JavaScript fragments that trigger in real time as a response to document mutations.

Eventing Functions allow you to:

* Integrate with the Data Service to:

  * Read, write, and delete documents
  * Work with Atomic Counters, CAS, and TTLS
* Integrate with the Query Service to use inline SQL++ queries or statements
* Enable a Timer to schedule functions to run in the future
* Interact with external REST endpoints through cURL functionality

You can access Eventing Functions by going to **Data Tools** **Eventing**. The Eventing Functions table includes the following:

| Feature           | Description                                                                                                                                                                                                                                                                                                     |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Function Name     | The name of the Function.                                                                                                                                                                                                                                                                                       |
| Source Bucket     | The source bucket of the events or mutations.                                                                                                                                                                                                                                                                   |
| Source Scope      | The source scope of the events or mutations.                                                                                                                                                                                                                                                                    |
| Source Collection | The source collection of the events or mutations.                                                                                                                                                                                                                                                               |
| Log               | [View and debug with Function Logs.](manage-eventing-functions.md#function-logs)                                                                                                                                                                                                                                |
| View JavaScript   | [View and edit the Function’s JavaScript.](manage-eventing-functions.md#edit-javascript)                                                                                                                                                                                                                        |
| Settings          | [View and edit the Function’s settings.](manage-eventing-functions.md#edit-settings)                                                                                                                                                                                                                            |
| Status            | The status of the Function. The status can be either in a stable state of **Deployed**, **Undeployed**, or **Paused**, or in a transitory state of **Deploying**, **Undeploying**, or **Pausing**.                                                                                                              |
| More options (⋮)  | Used to [deploy](deploy-eventing-functions.md#deploy-function), [undeploy](deploy-eventing-functions.md#undeploy-function), [export](manage-eventing-functions.md#export-function), [pause](manage-eventing-functions.md#pause-function), or [delete](manage-eventing-functions.md#delete-function) a Function. |