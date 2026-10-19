---
title: Managing Subscriptions
description: The Subscriptions page manages your licensing and support subscriptions.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Fleet Manager
    version: "1.0"
  topic_type: how-to
antora:
  editUrl: https://github.com/couchbaselabs/docs-fleetmanager/edit/main/modules/ROOT/pages/subscriptions.adoc
  xref: xref:fleet-manager::subscriptions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/fleet-manager/current/subscriptions.html)

# Managing Subscriptions

## [](#overview)Overview

The Subscriptions page shows a complete record of your license and support entitlements across your Couchbase clusters. The Subscriptions document contains 1 or more subscriptions, each of which details your support level and license limitations for that subscription.

Fleet Manager checks subscription entitlements by comparing your running tagged clusters with the subscriptions document uploaded to Fleet Manager. The portal alerts you if you're running Couchbase services that fall outside your subscriptions.

### [](#the-subscriptions-file)The Subscriptions File

Before you can begin monitoring your entitlements, you must first load a subscription file into Fleet Manager.

The file encodes your subscribed entitlements, which Fleet Manager uses to display your consumed and contracted entitlements.

> [!IMPORTANT]
> The subscription file does not contain any information related to pricing.

### [](#getting-the-subscriptions-file)Getting the Subscriptions File

If you have a Couchbase Account Manager, then contact them to get your subscription file.

If you do not have an account manager, then contact [Couchbase Support](../../server/current/introduction/contact-couchbase.md).

> [!CAUTION]
> You should not attempt to edit or change your subscription file.

### [](#installing-subscription-file)Installing the Subscription File

1. Use your web browser to log into Fleet Manager.
2. From the navigation menu, select **Subscriptions** to open the Subscriptions screen.
3. Click on the **Subscriptions** tab.
4. Click on the **Replace Subscription** button.
5. Import your entitlement document by dragging the subscriptions document into the window.
6. If the document is valid, your subscription details are displayed in the window.  
![replace subscription](_images/replace-subscription.png)  
Figure 1\. Replace Subscriptions screen
7. Click on the **Replace Subscription** button to load the subscriptions document.
8. The Subscriptions screen is shown with your new subscriptions.  
![subscriptions list](_images/subscriptions-list.png)  
Figure 2\. Fleet Manager Subscriptions page
9. If you have a contract, then verify that the listed subscription information matches the subscription information in the contract. (Check against the products purchased, the purchase dates, and the number of licenses).

### [](#updating-your-subscription-file)Updating Your Subscription File

You can replace the subscription file (you may have received a contract renewal, for example), at any time by running through the same process shown in [Installing the Subscription File](#installing-subscription-file).

### [](#mismatched-subscription-information)Mismatched Subscription Information

If subscription information does not match your contract, then contact your account manager or [Couchbase Support](../../server/current/introduction/contact-couchbase.md).

> [!IMPORTANT]
> Tagging your clusters
> 
> The `classification` and `supportLevel` information in the subscription file must match the `tagging` information you attach to your clusters through Fleet Manager. Read the [Tagging Clusters](tagging-clusters.md) section next.

> [!IMPORTANT]
> Fleet Manager does not store or transmit any data related to pricing.
> 
> Furthermore, telemetry is **not** transmitted back to Couchbase.