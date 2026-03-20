---
title: Flush a Bucket
description: <em>Flushing</em> deletes every object that a bucket contains.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/manage/pages/manage-buckets/flush-bucket.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:manage:manage-buckets/flush-bucket.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/manage/manage-buckets/flush-bucket.html)

# Flush a Bucket

> _Flushing_ deletes every object that a bucket contains. 

## [](#enable-flushing)Enable Flushing

To edit an existing bucket-configuration, access Couchbase Web Console, and left-click on the **Buckets** tab, in the vertical navigation-bar at the left-hand side.

![accessBucketTab](../_images/manage-buckets/accessBucketTab.png) 

The **Buckets** screen now appears, showing the buckets that have already been defined for your system:

![bucketsViewInitialEdit](../_images/manage-buckets/bucketsViewInitialEdit.png) 

To edit the settings for a particular bucket, left-click on the bucket’s row in the UI; then, when the **Edit** button appears, left-click on it:

This displays the **Edit Bucket Settings** dialog, which permits changes to be made to a subset of existing settings. All the settings contained here are described in detail for the **Add Data Bucket** dialog, in the section [Create a Bucket](create-bucket.md)

Left-click on the **Show advanced bucket settings** tab. This causes the **Add Data Bucket** dialog to expand vertically; and thereby display additional information. Navigate to the bottom of the expanded dialog, and locate the **Flush** panel. This provides a checkbox, the checking of which enables flushing for the current bucket:

![flushOptionEnabled](../_images/manage-buckets/flushOptionEnabled.png)

Note that flushing can also be enabled during bucket-creation. See [Create a Bucket](create-bucket.md) for details.

Once enabled, flushing can be performed by means of Couchbase Web Console: with the **Buckets** screen displayed, left-click on the row of a bucket for which flushing has been enabled. The displayed options now include the **Flush** button.

Note that flushing _cannot_ be performed while the bucket is the source for an outgoing _XDCR_ replication. For an introduction to XDCR, see [Cross Data Center Replication (XDCR)](../../learn/clusters-and-availability/xdcr-overview.md).

![flushBucketButton](../_images/manage-buckets/flushBucketButton.png)

When the **Flush** button is left-clicked on, flushing of the bucket occurs. This causes all items in the bucket to be deleted by the system at the earliest opportunity. Note that for this reason, you are recommended _not_ to run with the **Flush** setting enabled in production; due to the danger of all a bucket’s data being inadvertently lost.

## [](#providing-authorization)Providing Authorization

To flush a bucket, an administrator must have one of the the following roles:

* Full administrator
* Cluster administrator
* Bucket administrator

See [Authorization](../../learn/security/authorization-overview.md), for information on users and roles.

## [](#using-the-cli-and-rest-api)Using the CLI and REST API

You can also enable flushing by means of the CLI command [bucket-flush](../../cli/cbcli/couchbase-cli-bucket-flush.md), and the REST API method [rest-bucket-flush.](../../rest-api/rest-bucket-flush.md)