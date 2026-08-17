---
title: Delete a Reference
description: Deleting an XDCR <em>reference</em> ensures that the previously
  specified remote cluster and bucket are no longer available to receive
  replicated data.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/manage/pages/manage-xdcr/delete-xdcr-reference.adoc
  xref: xref:7.2@server:manage:manage-xdcr/delete-xdcr-reference.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/manage/manage-xdcr/delete-xdcr-reference.html)

# Delete a Reference

> Deleting an XDCR _reference_ ensures that the previously specified remote cluster and bucket are no longer available to receive replicated data. 

## [](#examples-on-this-page-delete-xdcr-reference)Examples on This Page

The examples in the subsections below show how to delete a replication; using the [UI](#delete-an-xdcr-reference-with-the-ui), the [CLI](#delete-an-xdcr-reference-with-the-cli), and the [REST API](#delete-an-xdcr-reference-with-the-rest-api) respectively. As their starting-point, the examples assume the scenario that concluded the page [Delete a Replication](delete-xdcr-replication.md).

## [](#delete-an-xdcr-reference-with-the-ui)Delete an XDCR Reference with the UI

Proceed as follows:

1. Access Couchbase Web Console. Left-click on the **XDCR** tab, in the left-hand navigation menu.  
![left click on xdcr tab](../_images/manage-xdcr/left-click-on-xdcr-tab.png)  
This brings up the **XDCR Replications** screen. The upper panel, **Remote Clusters**, features a single reference, as follows:  
![xdcr replications screen with reference](../_images/manage-xdcr/xdcr-replications-screen-with-reference.png)
2. To delete the reference, left-click on the row for the reference. When the **Delete** button appears, left-click on it:  
![left click on delete replication tab](../_images/manage-xdcr/left-click-on-delete-replication-tab.png)  
The following confirmation dialog is now displayed:  
![xdcr confirm delete reference](../_images/manage-xdcr/xdcr-confirm-delete-reference.png)
3. Left-click on **Delete Reference**, to confirm. The **Remote Clusters** panel now reappears, showing no replications:  
![xdcr replications screen initial](../_images/manage-xdcr/xdcr-replications-screen-initial.png)

The reference has now been deleted.

## [](#delete-an-xdcr-reference-with-the-cli)Delete an XDCR Reference with the CLI

From the starting-point defined above, in [Examples on This Page](#examples-on-this-page-delete-xdcr-reference), use the `xdcr-setup` command to delete an XDCR reference, specifying the `--delete` and `--xdcr-cluster-name` flags, as follows:

couchbase-cli xdcr-setup -c 10.142.180.101 \
-u Administrator \
-p password \
--delete \
--xdcr-cluster-name 10.142.180.102

If successful, this returns the following:

SUCCESS: Cluster reference deleted

The reference has been deleted.

## [](#delete-an-xdcr-reference-with-the-rest-api)Delete an XDCR Reference with the REST API

From the starting-point defined above, in [Examples on This Page](#examples-on-this-page-delete-xdcr-reference), use the REST API to delete an XDCR reference as follows:

curl -X DELETE -u Administrator:password \
http://10.142.180.101:8091/pools/default/remoteClusters/10.142.180.102

If successful, this returns `"ok"`: the reference has been deleted.

For further information, see [Deleting a Reference](../../rest-api/rest-xdcr-delete-ref.md).

## [](#next-xdcr-steps-after-delete-reference)Next Steps

A replication can be configured securely. See [Secure a Replication](secure-xdcr-replication.md).