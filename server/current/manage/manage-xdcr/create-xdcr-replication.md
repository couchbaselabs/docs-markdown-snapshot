---
title: Create a Replication
description: An XDCR replication allows data to be replicated continuously from
  a specified bucket on the source cluster to a specified bucket on the target.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/manage/pages/manage-xdcr/create-xdcr-replication.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/manage/manage-xdcr/create-xdcr-replication.html)

# Create a Replication

> An XDCR replication allows data to be replicated continuously from a specified bucket on the source cluster to a specified bucket on the target. 

## [](#understanding-replications)Understanding Replications

An XDCR replication is created on the cluster that is to be the source of the data-replication. Each replication uses a single _reference_, which has already been created. (See [Create a Reference](create-xdcr-reference.md).) To create the replication, you specify:

* The local, source bucket from which data is to be replicated; and, potentially, the scopes and collections within that bucket.
* The remote cluster to which data is to be replicated. This cluster must already be registered on the local cluster as a _reference_.
* The bucket on the remote cluster to which data is to be replicated; and, potentially, the scopes and collections within that bucket.
* Whether _filtering_ should be used in replication, and if so, according to what regular expression.
* Other _Advanced Replication Settings_, which can be used to optimize replication-performance.

Note that multiple _replications_ (each using a different source-target bucket combination) can be created using a single _reference_ (which refers to a target cluster, but not to any specific bucket on it).

## [](#examples-on-this-page-create-replication)Examples on This Page

The examples in the subsections below show how to create the same replication; using the [UI](#create-an-xdcr-replication-with-the-ui), the [CLI](#create-an-xdcr-replication-with-the-cli), and the [REST API](#create-an-xdcr-replication-with-the-rest-api) respectively. As their starting-point, the examples assume the scenario that concluded the page [Create a Reference](create-xdcr-reference.md), this being:

* Two clusters already exist; each containing a single node. These are named after their IP addresses: `10.144.210.101` and `10.144.210.102`.
* Each cluster contains a single bucket, which is the `travel-sample` bucket.
* Each cluster has the Full Administrator username of `Administrator`, and password of `password`.
* Cluster `10.144.210.101` now has a reference that specifies its own `travel-sample` bucket as a source, and the `travel-sample` bucket on `10.144.210.102` as a target.

## [](#create-an-xdcr-replication-with-the-ui)Create an XDCR Replication with the UI

Proceed as follows:

1. Access Couchbase Web Console. Left-click on the **XDCR** tab, in the left-hand navigation menu.  
![left click on xdcr tab](../_images/manage-xdcr/left-click-on-xdcr-tab.png)  
This displays the **XDCR Replications** screen, which lists the following:

  * **Remote Clusters**: Lists the remote clusters that have been registered as references on the current cluster.
  * **Outgoing Replications**: Lists the details of replications created on the current cluster.
  * **Incoming Replications**: Lists the details of replications created on the remote clusters, which are incoming to the current cluster.  
  > [!NOTE]  
  > If the remote cluster is the same as the current cluster, the replications are not listed in the Incoming Replications section. For information about incoming replications, see [Incoming Replications](incoming-xdcr-replications.md).  
  ![xdcr outgoing replications initial](../_images/manage-xdcr/xdcr-outgoing-replications-initial.png)
2. To start creating a replication, left-click on the **ADD REPLICATION** button:  
![left click on add replication button](../_images/manage-xdcr/left-click-on-add-replication-button.png)  
The **XDCR Add Replication** screen is now displayed:  
![xdcr add replication screen](../_images/manage-xdcr/xdcr-add-replication-screen.png)  
The fields in the upper area of the screen — **Replicate From Bucket**, **Remote Bucket**, and **Remote Cluster** — allow a replication to be defined that specifies source and target bucket only. The remaining fields allow _scopes_ and _collections_ — within source and/or target buckets — to be additionally specified; and allow **Advanced Settings** to be used.  
The example on this page will not configure **Advanced Settings**; and will specify source and target bucket only — each bucket being specified as the sample bucket `travel-sample`.  
Note that since the data within `travel-sample` is contained within multiple _scopes_ and _collections_, the path to each collection — known as a _keyspace_, and always being of the form `scope-name.collection-name` — is necessarily identical on each cluster. XDCR’s default behavior is always to replicate data between corresponding keyspaces: for example, data in `inventory.airline` on the source is replicated to `inventory.airline` on the target. When a keyspace on the source does **not** have a corresponding keyspace on the target, XDCR’s default behavior is **not** to replicate data from that source keyspace. This is known as replication by _implicit mapping_.  
Detailed examples of _explicitly_ specifying scopes and collections (and so, potentially, establishing mappings between dissimilar keyspaces) are provided later, in [Replicate Using Scopes and Collections](replicate-using-scopes-and-collections.md).  
Note that when a replication is defined only as _bucket to bucket_ (as in the current example), and thereby makes no reference to a scope or collection, the documents to be replicated are understood by XDCR to reside in the `_default` collection, which resides within the `_default` scope, of the source bucket. The documents will duly be replicated to the `_default` collection, in the `_default` scope, of the _target_ bucket. For more information , see [Default Scope and Collection](../../learn/data/scopes-and-collections.md#default-scope-and-collection).  
An account of **Advanced Settings** is provided in [Advanced Replication Settings with the UI](#xdcr-advanced-settings-pointer), below.  
The practical steps required for establishing filters are explained in [Filter a Replication](filter-xdcr-replication.md).  
Information about [Replication Settings for XDCR Conflict Logging](#xdcr-ui-settings-for-conflict-logging) is provided in a later section.
3. Enter appropriate information into the upper fields of the **Add Replication** screen. Specify `10.144.210.102` as the target cluster, and `travel-sample` as both source and target bucket. The fields in the upper area of the screen now appear as follows.  
![xdcr add replication screen upper fields complete](../_images/manage-xdcr/xdcr-add-replication-screen-upper-fields-complete.png)
4. Left-click on the **Save Replication** button, at the bottom of the screen:  
![saveReplicationButton](../_images/manage-xdcr/saveReplicationButton.png)  
The **XDCR Replications** screen is now redisplayed, with the appearance of the **Outgoing Replications** panel as follows:  
![xdcr outgoing replications with replication2](../_images/manage-xdcr/xdcr-outgoing-replications-with-replication2.png)  
This indicates that a replication is now in progress: from `travel-sample` on this cluster, to `travel-sample` on cluster `10.144.210.102`.

This concludes creation of the replication. Note that by left-clicking on the row for the replication, additional controls can be displayed:

![xdcr outgoing replications with replication opened](../_images/manage-xdcr/xdcr-outgoing-replications-with-replication-opened.png) 

When conflict logging is enabled, Outgoing Replications panel displays the Conflict Logging Rules panel, which shows the conflict collection mapping that you have chosen. Also, the bucket indicates Conflict Logging Enabled.

![xdcr outgoing with conflict logging](../_images/manage-xdcr/xdcr-outgoing-with-conflict-logging.png) 

Use of the **Pause** control is described in [Pause a Replication](pause-xdcr-replication.md); use of the **Delete** control in [Delete a Replication](delete-xdcr-replication.md); and use of the **Edit** control in [Editing Filters](filter-xdcr-replication.md#editing-filters).

### [](#monitor-current-replications)Monitor Current Replications

All current replications can be monitored, by left-clicking on the **XDCR Stats** tab, at the left of the **XDCR Replications** screen. The panel appears as follows.

![xdcr statistics](../_images/manage-xdcr/xdcr-statistics.png) 

For information on how to read the interactive charts now displayed, see [Manage Statistics](../manage-statistics/manage-statistics.md).

### [](#xdcr-advanced-settings-pointer)Advanced Replication Settings with the UI

Left-click on the **Advanced Replication Settings** control, in the **Add Replication** dialog. The UI expands vertically, to reveal the following:

![xdcr advanced settings](../_images/manage-xdcr/xdcr-advanced-settings.png) 

The values displayed in the fields are defaults, which can be modified interactively, and saved: this may help in achieving optimal replication-performance. For details on the significance of each field, see the [XDCR Reference](../../xdcr-reference/xdcr-reference-intro.md).

### [](#xdcr-ui-settings-for-conflict-logging)Replication Settings for XDCR Conflict Logging

The **XDCR Add Replication** page displays additional settings, which are specific to logging conflicts during an XDCR replication.

> [!NOTE]
> To configure and enable XDCR Conflict Logging, you must enable the bucket property `enableCrossClusterVersioning` on all buckets of the XDCR topology. This bucket property cannot be disabled once it is enabled. For more information about the bucket property `enableCrossClusterVersioning`, see [XDCR enableCrossClusterVersioning](../../learn/clusters-and-availability/xdcr-enable-crossclusterversioning.md).

The additional settings are as follows:

Specify collections for storing conflict logs and documents

Use this setting to enable choosing conflict collections for storing conflict logs and documents. This setting allows you to specify the bucket, scope, and collection where conflict logs and documents will be stored during XDCR conflict logging process. Conflict Logging Rules panel displays the mapping of conflict collections that you have specified.

Enable Conflict Logging

Use this setting to enable or disable conflict logging for the replication. When enabled, XDCR starts logging conflicts in the specified bucket, scope, and collection.

Default Conflict Log Collection

Use this setting to specify the default bucket, scope, and collection for conflict logging. If a custom collection is not specified, the default collection is used.

> [!NOTE]
> By default, conflicts are logged in the bucket, scope, and collection of the **Default Conflict Log Collection**. Use **Customise Conflict Logging at scope level** and **Customise Conflict Logging at collection level** to override the default settings.

Customise Conflict Logging at scope level

Use this setting to specify the scope for a custom conflict collection.

![customise conflict logging at scope](../_images/manage-xdcr/customise-conflict-logging-at-scope.png) 

Customise Conflict Logging at collection level

Use this setting to specify a custom collection to store conflict logs. You can choose a custom conflict collection that overrides the default conflict collection. Choose one of the following collection types:

* **Default collection**: To set the collection to the default collection of the bucket.
* **Parent collection**: To set the collection to that of the scope.
* **Custom collection**: To set the collection to a custom collection that you specify.
* **Do not log**: To disable conflict logging for this collection.  
![customise conflict logging collection](../_images/manage-xdcr/customise-conflict-logging-collection.png)

For more information, see [Enabling and Configuring Conflict Logging](../../learn/clusters-and-availability/xdcr-conflict-logging-feature.md#configure-conflictlogging-settings).

For more information about XDCR Conflict Logging, see [XDCR Conflict Logging](../../learn/clusters-and-availability/xdcr-conflict-logging-feature.md).

For more information about creating collections, see [Manage Scopes and Collections](../manage-scopes-and-collections/manage-scopes-and-collections.md).

### [](#error-notifications)Error Notifications

If, while a replication is in progress, errors occur, a notification appears adjacent to the status displayed on the row for the replication:

![xdcr error notification](../_images/manage-xdcr/xdcr-error-notification.png) 

Left-click on the orange icon, to display a full account of problems:

![xdcr error notification full](../_images/manage-xdcr/xdcr-error-notification-full.png) 

Note that in this window, in Couchbase-Server versions 7.1 and later, a message such as the following may appear: `Performing PeerToPeer communication with the following VBs:[…]`. This message may appear when XDCR is communicating with nodes during replication-startup, when cluster topology-changes are occurring, and possibly in other situations: the message is purely informational, and does not signify an error.

### [](#rebalance-information)Rebalance Information

XDCR provides information on cluster-rebalance status. An error message may be displayed, to indicate that the rate of replication has been affected; and to provide an estimated time of pipeline-restart. The error message may convey status on a rebalance occurring either on the target side:

![xdcr target rebalance notification](../_images/manage-xdcr/xdcr-target-rebalance-notification.png)

Or on the source side:

![xdcr source rebalance notification](../_images/manage-xdcr/xdcr-source-rebalance-notification.png)

## [](#create-an-xdcr-replication-with-the-cli)Create an XDCR Replication with the CLI

Staring from the scenario defined above, in [Examples on This Page](#examples-on-this-page-create-replication), use the CLI `xdcr-replicate` command to create an XDCR replication, as follows:

couchbase-cli xdcr-replicate -c 10.144.210.101 \
-u Administrator \
-p password \
--create \
--xdcr-cluster-name 10.144.210.102 \
--xdcr-from-bucket travel-sample \
--xdcr-to-bucket travel-sample \
--xdcr-replication-mode xmem

If successful, this provides the following response:

SUCCESS: XDCR replication created

For more information, see the complete reference for the [xdcr-replicate](../../cli/cbcli/couchbase-cli-xdcr-replicate.md) command. Note that this includes descriptions of all flags that support the [Advanced Settings](#xdcr-advanced-settings-pointer), described above.

## [](#create-an-xdcr-replication-with-the-rest-api)Create an XDCR Replication with the REST API

Starting from the scenario defined above, in [Examples on This Page](#examples-on-this-page-create-replication), using the REST API’s `POST /controller/createReplication` HTTP method and URI, create an XDCR reference as follows:

curl -v -X POST -u Administrator:password \
http://10.144.210.101:8091/controller/createReplication \
-d fromBucket=travel-sample \
-d toCluster=10.144.210.102 \
-d toBucket=travel-sample \
-d replicationType=continuous \
-d enableCompression=1

If successful, this provides the following response:

{"id":"82026f90f5f573b5e50ec8b7a7012ab1/travel-sample/travel-sample"}

For more information, see [Creating a Replication](../../rest-api/rest-xdcr-create-replication.md). For information on REST-driven configuration of the [Advanced Settings](#xdcr-advanced-settings-pointer) described above, see [Managing Advanced Settings](../../rest-api/rest-xdcr-adv-settings.md).

## [](#create-an-xdcr-replication-with-mobile-as-active)Create an XDCR Replication with mobile=Active

To create or update an XDCR replication with `mobile=Active`, do one of the following:

* Create an XDCR replication with `mobile=Active` or update an existing replication. For information about _creating_ (new) an XDCR replication with `mobile=Active`, see [Greenfield deployment](../../learn/clusters-and-availability/xdcr-active-active-sgw.md#xdcr-active-active-sgw-greenfield-deployment), and for information about _updating_ an existing replication with `mobile=Active`, see [Upgrade an existing setup](../../learn/clusters-and-availability/xdcr-active-active-sgw.md#xdcr-active-active-sgw-upgrade).
* Create or update an XDCR replication with `mobile=Active` option using the REST API, starting from Server 7.6.6 version. See [Creating a Replication](../../rest-api/rest-xdcr-create-replication.md).
* Create or update a XDCR replication with `mobile=Active` option from the UI, starting from Server 7.6.6 version. See [Create an XDCR Replication with the UI](#create-an-xdcr-replication-with-the-ui).

The pre-requisite to use `mobile=Active` is to set the bucket property `enableCrossClusterVersioning`. For more information about the bucket property `enableCrossClusterVersioning`, see [XDCR enableCrossClusterVersioning](../../learn/clusters-and-availability/xdcr-enable-crossclusterversioning.md).

To enable the bucket property `enableCrossClusterVersioning` using REST API, see [Modify the bucket property enableCrossClusterVersioning](../../learn/clusters-and-availability/xdcr-enable-crossclusterversioning.md#modify-enablecrossclusterversioning) or [Example: Turning on enableCrossClusterVersioning, when Editing](../../rest-api/rest-bucket-create.md#example-enablecrossclusterversioning-edit).

## [](#next-xdcr-steps-after-create-replication)Next Steps

Once a replication has been defined and is therefore running, you can opt to _pause_ it, in order to perform system maintenance. See [Pause a Replication](pause-xdcr-replication.md).