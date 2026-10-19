---
title: Tagging Clusters
description: Tagging your clusters makes it easier to identify and group them.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Fleet Manager
    version: "1.0"
  topic_type: how-to
antora:
  editUrl: https://github.com/couchbaselabs/docs-fleetmanager/edit/main/modules/ROOT/pages/tagging-clusters.adoc
  xref: xref:fleet-manager::tagging-clusters.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/fleet-manager/current/tagging-clusters.html)

# Tagging Clusters

> Tagging your clusters makes it easier to identify and group them. 

## [](#overview)Overview

You can label the clusters that form your Couchbase network. This makes it easier to attach meaningful names to your clusters and group them by functional areas (such as HR, Finance, and so on).

## [](#tagging-your-clusters)Tagging Your Clusters

1. When you have loaded a new subscription document into your portal(see [Managing Subscriptions](subscriptions.md)), return to the **Overview** screen. Near the top of the page, you'll see a button for tagging clusters:  
![tag cluster button](_images/tag-cluster-button.png)  
Figure 1\. The Tag Cluster button  
> [!NOTE]  
> If the button is not shown, you can still reach the cluster tagging function by selecting **Clusters** from the main menu.
2. Click on the **Tag Cluster** button. This takes you to the **Clusters** screen.
3. Click on the cluster you want to tag from the displayed list. This takes you to the **Cluster** details screen:  
![cluster details](_images/cluster-details.png)  
Figure 2\. Cluster details screen
4. Click on the **Edit tagging** button.
5. From the **Tag Cluster** screen, you can add details for your cluster:

| Cluster name     | Give your cluster a name that makes it easier to identify in reports and alerts. (For example, main or backup)                                                                                                                                                                                                                                                                                                 |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Environment type | Select the environment type from a list of configurable values. (For example, development or production.) The environment type of the cluster must match classification given in your subscription file. This ensures that Fleet Manager can match your subscription to your usage. Otherwise, you may see unmatched subscription errors. For more information, see [Managing Subscriptions](subscriptions.md) |
| Business unit    | A string that can be used to group the clusters into a business function. Marketing or Finance, for example.                                                                                                                                                                                                                                                                                                   |
6. Check that your clusters match against the information in the subscription file.

> [!NOTE]
> Subscriptions incorrect?
> 
> If the subscription information is still incorrect after you have tagged your clusters, then contact your Couchbase account manager or contact [Couchbase Support](../../server/current/introduction/contact-couchbase.md).