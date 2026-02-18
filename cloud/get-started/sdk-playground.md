---
title: Explore the Playground
description: Use the Playground to practice and learn more about SQL++.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/get-started/pages/sdk-playground.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/get-started/sdk-playground.html)

# Explore the Playground

> Use the Playground to practice and learn more about SQL++. 

The Playground lets you try out SQL++ code examples through interactive tutorials inside the Couchbase Capella UI.

## [](#how-playground-works)How the Playground Works

The code examples in the Playground run in a remote execution environment deployed in the USA, which imposes limits to the runtime of each programming language. The remote environment has a firewall that prevents access to domains or networks outside of the Couchbase Cloud environment.

When you run a code example on the Playground, Couchbase Capella:

* Generates a temporary credential for you with read and write access to the bucket you used for the code example. This temporary credential is destroyed after your code example request is executed.
* Provides the remote execution environment with temporary network access to your cluster. This temporary network access is automatically revoked after 1 hour.

## [](#playground-prerequisites)Prerequisites

Before you use the Playground, make sure that you have access to the `travel-sample` bucket on your cluster.

If you do not have access to the `travel-sample` bucket, [import the sample data](../clusters/data-service/import-data-documents.md) or [open a support ticket](../support/manage-support.md).

## [](#use-the-playground)Use the Playground

To use the Playground:

1. Go to **Playground** and select 1 of the following tutorials:

  * **Understand the Power of SQL++** to explore different SQL++ queries and experiment with data.
2. In the tutorial home page, you can do the following:

  * Click **Run** to execute the example code and generate the response in the **Response** field.
  * Click **Next** to go to the next chapter of the tutorial.
  * Click **Prev** to return to the previous chapter of the tutorial.
  * Select a chapter from the **Chapter** list to go to a specific chapter.
  * Click **Exit Playground** to return to the Capella home page.

## [](#disable-the-playground)Turn Off the Playground

To turn off the Playground:

1. Go to **Clusters**.
2. Select the cluster you want to turn off the Playground for.
3. Go to **Settings** **General**.
4. In the **Playground** section, select **Disable Playground**.
5. Click **Save**.

## [](#next-steps)Next Steps

After you explore the Playground, you can:

* [Import your own data](../clusters/data-service/import-data-documents.md)
* [Configure App Services for your free tier operational cluster](../../app-services/get-started/configuring-app-services.md)

If you want to connect to your cluster:

1. [Generate your cluster credentials](../clusters/manage-database-users.md) to connect and control access to you cluster.
2. [Add your current IP address as an allowed IP for you cluster](../clusters/allow-ip-address.md).
3. [Generate a code snippet](connect.md) to connect your cluster to your application.
4. Choose and install a [Couchbase SDK](#home:ROOT:sdk.adoc).
5. (Optional) Download the security certificate for your cluster and add it to your application’s server machine or IDE:

  1. In the **Operational** tab, select a cluster.
  2. Go to **Settings** **Security Certificate**.
  3. Click **Download**.