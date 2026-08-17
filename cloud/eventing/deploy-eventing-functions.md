---
title: Deploy Eventing Functions
description: Use the Capella UI to deploy and undeploy Eventing Functions in your cluster.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/eventing/pages/deploy-eventing-functions.adoc
  xref: xref:cloud:eventing:deploy-eventing-functions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/eventing/deploy-eventing-functions.html)

# Deploy Eventing Functions

> Use the Capella UI to deploy and undeploy Eventing Functions in your cluster. 

## [](#deploy-function)Deploy an Eventing Function

When you add an Eventing Function to your cluster, the Function is saved in an undeployed state. To activate an Eventing Function, you must deploy it.

Deploying a Function:

* Lets the handler to receive and process events or mutations
* Creates necessary metadata
* Spawns worker processes
* Calculates initial partitions
* Initiates checkpointing of processed stream data

> [!NOTE]
> You cannot edit the JavaScript source code of a deployed Eventing Function.

To deploy an Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **More Options (⋮)** next to the Function you want to deploy.
3. Click **Deploy** to deploy your Function.

## [](#undeploy-function)Undeploy an Eventing Function

You can undeploy a deployed Eventing Function to deactivate it. After a Function is undeployed, you can edit the JavaScript source code.

To undeploy an Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **More Options (⋮)** next to the Function you want to undeploy.
3. Click **Undeploy** to undeploy your Function.

## [](#deployment-statistics)Check the Deployment Statistics

You can check the deployment statistics for your deployed Function by clicking the expand arrow next to it.

| Type    | Description                                                        |
| ------- | ------------------------------------------------------------------ |
| Success | The number of processed Functions.                                 |
| Failure | The number of failures while processing the Function handler code. |
| Timeout | The number of Functions that have timed out.                       |
| Backlog | The number of mutations to be processed by a Function.             |

## [](#next-steps)Next Steps

After you deploy Eventing Functions, you can [manage them](manage-eventing-functions.md).