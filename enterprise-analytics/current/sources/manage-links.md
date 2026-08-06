---
title: Managing Enterprise Analytics Links
description: This page describes how to manage remote links and external links
  using the Analytics Workbench.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/sources/pages/manage-links.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:enterprise-analytics:sources:manage-links.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sources/manage-links.html)

# Managing Enterprise Analytics Links

The Analytics Workbench enables you to create or edit remote links and external links:

* A remote link is a link to a remote Couchbase cluster.
* An external link is a link to an external data source, such as Amazon S3, S3-compatible storage, Azure Blob Storage, or Google Cloud Storage.
* Links are also used to authenticate access to [Apache Iceberg catalogs](../sqlpp/5%5Fddl%5Ficeberg.md) and their underlying data files in object storage.

After you have created a remote link or an external link, you must create an Analytics collection on that link to query the data.

A remote link is disconnected by default. When you create a new Analytics collection on a disconnected link, data ingestion to that collection does not begin immediately. You must connect the remote link to start data ingestion to the Analytics collections on that link.

An external link cannot be connected or disconnected. An external Analytics collection is available for query as soon as you create it. Remote links and external links are displayed in the insights sidebar of the Analytics Workbench.

In the insights sidebar, links are labeled as follows:

* External links to Amazon S3 or S3-compatible storage — `S3`
* External links to Azure Blob Storage — `Azure Blob`
* External links to Google Cloud Storage — `GCS`
* Remote links — `cb remote`
* Kafka links — `KAFKA`

## [](#creating-a-link)Creating a Link

* To create a remote link, see [Stream Data from Remote Sources](manage-remote.md)
* To create an external link, see [Set Up an External Data Source](manage-external.md)

## [](#editing-a-link)Editing a Link

To edit a remote link:

1. In the UI, select the **Workbench** tab and browse to the link you want to edit.
2. Select the required link. NOTE: You must disconnect the link before you can edit it.
3. Edit the details of the link as required.  
> [!NOTE]  
> You cannot change the name of the link or the link type. Make sure that you enter the password in the **Remote Password** field.  
For information about the available options, see:

  * [Stream Data from Remote Sources](manage-remote.md)
  * [Set Up an External Data Source](manage-external.md)
4. Click **Save** to update the link.

You can also edit a remote link or external link using the command-line interface or the REST API. See the [enterprise-analytics-link-setup](../cli/couchbase-cli-enterprise-analytics-link-setup.md) or [Analytics Links REST API](../analytics-rest-links/index.md).

To edit an external link:

1. In the UI, select the **Workbench** tab and browse to the link you want to edit.
2. Select the required link.
3. Edit the details of the link as required.  
> [!NOTE]  
> You cannot change the name of the link or the link type. Make sure that you enter the access key, if it's provided, in the **Secret Access Key** field. For more information about the available options, see:

  * [Stream Data from Remote Sources](manage-remote.md)
  * [Set Up an External Data Source](manage-external.md)
4. Click **Save** to update the link.

You can also edit a remote link or external link using the command-line interface or the REST API. See [enterprise-analytics-link-setup](../cli/couchbase-cli-enterprise-analytics-link-setup.md) or [Analytics Links REST API](../analytics-rest-links/index.md).

## [](#deleting-a-link)Deleting a Link

To delete a remote link or an external link:

1. In the UI, select the **Workbench** tab and browse to the link you want to edit.
2. Select the required link.
3. Choose **Drop Link**.
4. To confirm that you want to delete the link, click **OK**.

You can also delete a remote link or external link using the command-line interface or the REST API. See [enterprise-analytics-link-setup](../cli/couchbase-cli-enterprise-analytics-link-setup.md) or [Analytics Links REST API](../analytics-rest-links/index.md).