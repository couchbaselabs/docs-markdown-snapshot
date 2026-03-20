---
title: Manage Replications
description: Use the procedures on this page to create and manage XDCR (Cross
  Data Center Replication) with Capella operational clusters.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/xdcr/manage-xdcr-replications.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:clusters:xdcr/manage-xdcr-replications.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/xdcr/manage-xdcr-replications.html)

# Manage Replications

> Use the procedures on this page to create and manage XDCR (Cross Data Center Replication) with Capella operational clusters. 

Configure XDCR to replicate data between source and destination buckets. XDCR continuously replicates bucket data from a specified bucket on a source cluster to a specified bucket on a target cluster. For general information about XDCR in Capella and how it works, see [Cross Data Center Replication (XDCR)](xdcr.md).

## [](#prerequisites)Prerequisites

* To view and manage replications on a cluster, you need the [Project Owner](../../projects/project-roles.md#project-owner-role) role for your source cluster.
* To delete or create a new replication, you need the [Project Owner](../../projects/project-roles.md#project-owner-role) role for the projects that contain your source cluster and destination cluster.
* You have created a single node or multi-node cluster that you want to use for replication, either as a source or destination cluster.

> [!IMPORTANT]
> Replication on single node clusters is only supported for development or test use cases.

## [](#view-your-replications)View Your Replications

To view and manage replications:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to view and manage replications.
3. Go to **Settings** **Replication**.

If you have not set up a replication for your cluster, you can click **Set Up Replication**. For more information about adding **Self-Managed Targets**, see [Create a Replication from Capella to a Self-Managed Cluster](#from-capella-to-self-managed).

If you have already created replications for your cluster, you’ll see a summary of your replications in a table. For an example, see [Observe an Ongoing Replication](#observing).

## [](#create-replication)Create a Replication

> [!IMPORTANT]
> Source and destination buckets must have the same [conflict resolution method](xdcr.md#conflict-resolution) configured. If your source and destination buckets use different conflict resolution methods, then you cannot create a replication.

Data replication can be between:

* [2 operational clusters](#between-capella-dbs).
* [A self-managed cluster to an operational cluster](#from-on-prem-to-capella).
* [An operational cluster to a self-managed cluster](#replicate-to-self-managed-target). A self-managed cluster can be in an on-premises datacenter or in your own cloud.

Clusters hosted by Couchbase Capella support the following replications:

* Capella Hosted (AWS) ←→ Capella Hosted (AWS)
* Capella Hosted (AWS) ←→ Own Cloud (AWS, GCP, or Azure)
* Capella Hosted (AWS) ←→ On-Premises
* Capella Hosted (GCP) ←→ Capella Hosted (GCP)
* Capella Hosted (GCP) ←→ Own Cloud (GCP, AWS, or Azure)
* Capella Hosted (GCP) ←→ On-Premises
* Capella Hosted (Azure) ←→ Capella Hosted (Azure)
* Capella Hosted (Azure) ←→ Own Cloud (Azure, AWS, or GCP)
* Capella Hosted (Azure) ←→ On-Premises

### [](#between-capella-dbs)Create a Replication Between Operational Clusters

> [!NOTE]
> Replication Security
> 
> Replications between Capella operational clusters are secured by default.

To create a replication between 2 operational clusters:

1. On the **Replication** page, click **Set Up Replication**.
2. Choose to create a **One-way** or a **Two-way** replication. A one-way replication replicates data only from the source to the target. A two-way replication replicates data both from the source to the target, and from the target to the source.
3. Choose your target cluster from the **Target Cluster** menu. Your target cluster must be within the same cloud service provider (CSP) as your destination cluster.
4. Under **Select Buckets**, choose the **Source Bucket** and **Target Bucket** to use in the replication.
5. To enable bi-directional replication with Sync Gateway (App Services), select **Enable Active-Active XDCR with App Services**.  
This option allows creating a replication with App Services 4.0+ app endpoints linked to both source and target buckets. When creating the replication, Capella:

  * Enables the bucket property [Cross Cluster Versioning](../../../server/current/learn/clusters-and-availability/xdcr-overview.md#cross-cluster-versioning) on both source and target buckets, if it’s not already set.
  * Sets the replication flag `mobile` to `Active` for all legs of the replication.  
  This option is only available when both source and target clusters use Couchbase Server version 7.6.6+ and linked App Services use version 4.0+.
6. To add a filter to your replication, under **Filter Replication**, click **Enable**:

  1. In the **Filter Expression** field, enter a regex pattern or SQL++ statement to use to filter documents from your replication.  
  For example, to only replicate documents that contain the value `France` for the key `country`, enter the expression `REGEXP_CONTAINS(country, "France")`.  
  The expression must contain at least 2 keys.
  2. Click **Check Syntax** to verify the syntax of your expression.
7. (Optional) If you added a filter expression, use the **Test Document** panel to test your filter:

  1. From your source bucket, choose a scope, collection, and enter a document ID value for a document you want to use in your test.
  2. Click **Test Document** to run the test.
8. Choose your **Deletion Filters**.  
For more information about deletion filters, see [Deletion Filters](../../../server/current/manage/manage-xdcr/filter-xdcr-replication.md#deletion-filters) in the Server documentation.
9. If your operational cluster is on Couchbase Server version 7.2.2 or later, choose whether to **Filter Binary Documents**.  
For more information about filtering binary documents from XDCR, see [Filtering Binary Documents](../../../server/current/manage/manage-xdcr/filter-xdcr-replication.md#filtering-binary-documents) in the Server documentation.
10. Choose a **High**, **Medium**, or **Low** Replication Priority. For more information about each option, see [XDCR Priority](../../../server/current/learn/clusters-and-availability/xdcr-overview.md#xdcr-priority). A setting only takes effect if there are multiple replications with different priorities.
11. To set a network usage limit, under **Set Network Usage Limit**, click **Enable**. Enter a limit in MiB per second for the maximum network usage of this replication.  
> [!NOTE]  
> This limit applies to all replications for your source cluster.
12. (Optional) If you want to replicate all scopes and collections on your source cluster to your target cluster, under **Replicate All Scopes and Collections**, click **Yes**.  
> [!NOTE]  
> To replicate your scopes and collections, each scope and collection must already exist with the same name on the source and target buckets. If you want to replicate documents to a different target scope and collection from your source, click **No**.

  1. In the **Source Name** list, choose a scope and then a specific collection on your source cluster to replicate.
  2. In the **Target Name** list, choose the scope and specific collection on your target cluster to receive the replicated documents.
  3. (Optional) To add another scope and collection pairing on your source and target clusters, click **Add Source and Target**.
13. To start the replication, click **Setup Replication**.

It may take some time for your replication to be set up and start replicating documents.

> [!IMPORTANT]
> Bi-directional XDCR with Sync Gateway requires Server versions 7.6.6+, and Sync Gateway (App Services) versions 4.0+.

### [](#from-on-prem-to-capella)Create a Replication to Capella from a Self-Managed Cluster

Replicate your data to an operational cluster from a self-managed cluster that’s in an on-premises datacenter or a non-Capella cloud.

To set up XDCR from a self-managed cluster to an operational cluster:

1. [Create a cluster access credential in your operational cluster](#access-credential).
2. [Secure your replication](#secure-replication).
3. [Get the hostname to use in the XDCR remote cluster reference](#get-hostname).
4. [Copy the security certificate from the operational cluster](#security-certificate).
5. [Set up XDCR remote reference](#xdcr-remote-ref).

#### [](#access-credential)Create a Cluster Access Credential in Your Operational Cluster

To create a cluster access credential in your operational cluster, see [Configure Cluster Access Credentials](../manage-database-users.md#create-database-credentials).

#### [](#secure-replication)Secure Your Replication

Replication security varies based on your source and destination cluster deployment configurations. For more information, see [Manage Replication Security](manage-xdcr-security.md).

To secure your replication, choose to connect using 1 of the following options:

* Public Internet
* VPC Peering
* Private Endpoint

To route your replication through the public Internet, you must add the IP address of the self-managed cluster Data Service nodes to the **Allowed IP** list of the operational cluster.

To add the public IP of the VM to the **Allowed IP** list of your operational cluster:

1. Get the public IP from your VM:

  1. `ssh` into the VM where Couchbase Server is running.  
  ```console  
  # dig +short myip.opendns.com @resolver1.opendns.com  
  ```  
  ```console
67.212.150.204  
  ```
2. Add an Allowed IP address to your operational cluster. For more information, see [Add an Allowed IP Address](../allow-ip-address.md#add-allowed-ip).

To route your replications through a peered VPC network:

1. Configure a VPC Peering Connection. For more information, see [Configure a VPC Peering Connection](../../clouds/private-network.md).

For more information about routing your replication through a peered VPC network, see [Replicate Data Over a VPC Peering Connection](manage-xdcr-security.md#vpc-peering).

> [!NOTE]
> XDCR over private endpoints is only available upon request from [Support](../../support/manage-support.md#create-support-ticket).

To route your replication through a private endpoint connection, see [Replicate Data Over a Private Endpoint](manage-xdcr-security.md#private-endpoints).

#### [](#get-hostname)Get the Hostname to Use in the XDCR Remote Cluster Reference

To get the hostname to use in the XDCR remote cluster reference:

1. In the Capella UI, go to **Operational** and select your cluster name.
2. Choose 1 of the following options. If your replication is traveling through:

  1. A peered VPC network or the public Internet, go to **Connect** **SDKs** and copy the Public Connection String without the `couchbases://` prefix. The public connection string is also the DNS SRV of the cluster.  
  > [!NOTE]  
  > Although the connection string is sometimes referred to as the "public connection string," if you have VPC peering set up the connection string resolves to private addresses. For more information, see [Configure a VPC Peering Connection](../../clouds/private-network.md).
  2. A private endpoint, go to **Settings** **Private Endpoints** and copy the **Private Endpoint DNS**.

#### [](#copy-certificate)Copy Your Operational Cluster’s Security Certificate

To copy your operational cluster’s security certificate:

1. In the Capella UI, go to **Operational** and select your cluster name.
2. Go to **Settings** **Security Certificate**.
3. Click **Copy**.

#### [](#xdcr-remote-ref)Set Up XDCR Remote Reference

> [!NOTE]
> XDCR compatibility can vary between different versions of Couchbase Enterprise Server. To view and confirm compatibility, see [XDCR Compatibility](../../../server/current/learn/clusters-and-availability/xdcr-overview.md#xdcr-compatibility).

To set up your XDCR remote reference, choose the Couchbase Server version of your self-managed cluster:

* Couchbase Server 8.X or later
* Couchbase Server 7.X

To setup an XDCR remote reference:

1. Go to the Couchbase Server Web Console.
2. Go to **XDCR** and click **Add Replication**.
3. Enter the following information for each field:

|                                 |                                                                                                                                                                                                                                                                                                          |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cluster Name**                | Any name                                                                                                                                                                                                                                                                                                 |
| **IP/Hostname**                 | The connection string from [Get the Hostname to Use in the XDCR Remote Cluster Reference](#get-hostname). As the hostname saves as a DNS SRV string in Couchbase Server 7.X and later, you do not need to specify a port. If you’re using the Public Connection String, remove the couchbases:// prefix. |
| **Username for Remote Cluster** | Cluster credentials from [Create a Cluster Access Credential in Your Operational Cluster](#access-credential).                                                                                                                                                                                           |
| **Password**                    | Cluster credentials from [Create a Cluster Access Credential in Your Operational Cluster](#access-credential).                                                                                                                                                                                           |
| **Certificate**                 | Paste the security certificate copied in [Copy Your Operational Cluster’s Security Certificate](#copy-certificate).                                                                                                                                                                                      |
| **Network Type**                | If your replication is traveling through: The public Internet or a peered VPC network, select **Auto**. A private endpoint, select **Force using alternate address**.                                                                                                                                    |
4. Complete the setup for your replication.  
For more information about how to set up a replication in Couchbase Server, see [Create a Replication](../../../server/current/manage/manage-xdcr/create-xdcr-replication.md) in the Couchbase Server documentation.

> [!NOTE]
> If you’re [securing your replication over a private endpoint](#cluster:xdcr/manage-xdcr-security.adoc#xdcr-pe-limits), you can only setup the XDCR remote reference using the [REST API](../../../server/current/rest-api/rest-xdcr-create-ref.md). In your [curl Syntax](../../../server/current/rest-api/rest-xdcr-create-ref.md#curl-syntax), you must set the hostname as the **Private Endpoint DNS** and network type as `network_type=external`.

To setup an XDCR remote reference:

1. Go to the Couchbase Server Web Console.
2. Go to **XDCR** and click **Add Replication**.
3. Enter the following information for each field:

|                                 |                                                                                                                                                                                                                                                                                                          |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cluster Name**                | Any name                                                                                                                                                                                                                                                                                                 |
| **IP/Hostname**                 | The connection string from [Get the Hostname to Use in the XDCR Remote Cluster Reference](#get-hostname). As the hostname saves as a DNS SRV string in Couchbase Server 7.X and later, you do not need to specify a port. If you’re using the Public Connection String, remove the couchbases:// prefix. |
| **Username for Remote Cluster** | Cluster credentials from [Create a Cluster Access Credential in Your Operational Cluster](#access-credential).                                                                                                                                                                                           |
| **Password**                    | Cluster credentials from [Create a Cluster Access Credential in Your Operational Cluster](#access-credential).                                                                                                                                                                                           |
| **Certificate**                 | Paste the security certificate copied in [Copy Your Operational Cluster’s Security Certificate](#copy-certificate).                                                                                                                                                                                      |
4. Complete the setup for your replication.  
For more information about how to set up a replication in Couchbase Server, see [Create a Replication](../../../server/current/manage/manage-xdcr/create-xdcr-replication.md) in the Couchbase Server documentation.

### [](#from-capella-to-self-managed)Create a Replication from Capella to a Self-Managed Cluster

Replicate your data from an operational cluster to a self-managed cluster that’s in an on-premises datacenter or a non-Capella cloud.

> [!NOTE]
> Replication Security
> 
> Security options for self-managed XDCR replications vary based on the source and destination cluster deployment configurations. For replications from a Capella operational cluster to a self-managed cluster, you can choose to connect through:
> 
> * [The public Internet](manage-xdcr-security.md#public-internet).
> * [VPC Peering](manage-xdcr-security.md#vpc-peering).
> 
> For more information, see [Manage Replication Security](manage-xdcr-security.md).

To configure the replication, the Capella administrator must have the following:

* The CA of the self-managed cluster.
* Either of the following:

  * The username and password for the self-managed cluster.
  * A client certificate and private key provided for client access to the self-managed cluster.

Additionally, the self-managed cluster must be network-accessible to Capella. Ensure that:

* The target cluster is accessible via the SSL ports 18091, 18092, and 11207.
* Each Data Service node on the operational cluster can connect to each Data Service node on the self-managed target.
* All target-cluster firewalls allow access to the Capella Data Service nodes.

To replicate data from Capella to a self-managed cluster:

1. [Add the self-managed cluster as a target](#add-self-managed-cluster).
2. [Select the self-managed cluster to be the target for a specific replication](#replicate-to-self-managed-target).

> [!NOTE]
> If you want to view your self-managed target over a private network, set up VPC Peering for the connection before adding your self-managed target. For information, see [Configure a Private Network](../../clouds/private-network.md).

#### [](#add-self-managed-cluster)Add a Self-Managed Target

To add a self-managed target:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to set up a self-managed replication target.
3. Go to **Settings** **Replication**.
4. Click **Add Self-Managed Target**.
5. Review the configuration information for setting up a self-managed target.
6. In the **Target Name** field, enter a name for the self-managed target.
7. In the **IP/Hostname** field, enter the IP address or Fully Qualified Domain Name of the self-managed target.
8. (Optional) If you want to authenticate through a username and password, in the **Username for Self-Managed Target** and **Password** fields, enter your admin username and password for the self-managed target.  
You must add a username and password unless you authenticate with a client certificate and private key.
9. Choose the **Network Type** for your connection.  
You can use either the alternate or internal network address for your self-managed target, or let Capella decide based on your provided hostname.  
For information about specifying internal and alternate addresses, see [Using Alternate Addresses](../../../server/current/xdcr-reference/xdcr-security-and-networking.md#using-alternate-addresses) and [Specifying Addresses](../../../server/current/xdcr-reference/xdcr-security-and-networking.md#specifying-addresses).
10. In the **TLS Certificate** field, paste the CA of the self-managed target.
11. (Optional) If you want Capella to authenticate through a client certificate and private key, click **Use Client Certificate Authentication**.

  1. In the **Client Certificate** field, paste your client certificate from your self-managed target.
  2. In the **RSA Private Key** field, paste the RSA private key.
12. (Optional) To verify the connection to your self-managed target using your provided information, click **Check Connection**.
13. Click **Add Self-Managed Target**.

#### [](#replicate-to-self-managed-target)Replicate to a Self-Managed Target

To configure a replication from Capella to a self-managed target:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to set up a new replication.
3. Go to **Settings** **Replication**.
4. Click **Setup Replication**.
5. Choose a **One-Way** replication direction. You cannot use Two-Way replication with a self-managed target.
6. In the **Target Clusters** list, select your self-managed target cluster. Clusters in the menu are divided into two groups: **Self-Managed** and **Capella Managed**.
7. Under **Select Buckets**, choose the **Source Bucket** and **Target Bucket** to use in the replication.
8. Configure other settings for your replication, such as **Filter Documents**, **Select Replication Priority**, **Set Network Usage Limit**, and **Replicate All Scopes and Collections**.
9. Click **Set Up Replication**.

## [](#observing)Observe an Ongoing Replication

You can view the details for a current replication at any time from **Settings** **Replication** on your cluster.

## [](#pause-resume-replication)Pause and Resume a Replication

Pausing an XDCR replication temporarily suspends the replication of data from the source to the target. Pausing a replication always occurs on the source cluster. You can resume a paused replication at any time.

When pausing a bidirectional replication, only the replication from the current cluster will be paused. To pause both directions of a bidirectional replication, you’ll need to pause the replication on both clusters individually.

To pause or resume a replication:

1. On the **Replications** page, click the **Active** replication you want to pause, or the **Paused** replication you want to resume.
2. Under **Pause Replication**, click **Pause Replication** or **Resume Replication**.

## [](#modify-a-replication)Modify a Replication

You can modify specific replication settings after creation. You cannot change:

* The replication direction.
* The source cluster, source provider and region, source type, or source bucket.
* The target cluster, target provider and region, target type, or target bucket.

To modify your replication:

1. On the **Replications** page, click the replication you want to modify.
2. Modify the following settings:

  * Enable or disable filter replication.
  * Select **High**, **Medium**, or **Low** replication priority.
  * Enable or disable the network usage limit.
  * Choose to replicate all scopes and collections.
3. Click **Save**.

## [](#delete-replication)Delete a Replication

Deleting an XDCR replication stops the replication of data, and removes the defined replication from the cluster. The replication process retains all replicated data.

If the replication is bidirectional, deleting the replication on the source cluster removes both directions of the replication from the **Replications** tab of both clusters.

To delete a replication:

1. On the **Replications** page, click the replication you want to delete.
2. Under **Delete Replication**, click **Delete Replication**.
3. Confirm that you want to delete the replication.
4. Click **Delete Replication**.

## [](#error-and-other-notifications)Errors and Other Notifications

If a connectivity issue occurs while replicating to a self-managed target, you’ll see an error under **Self-Managed Targets** on the **Replication** page. Connectivity errors appear in the **Connectivity Status** column.

For all replication types, any errors, warnings, or informational messages can be viewed in more detail from the **Errors** column under **Replications**. Click the icon in the **Errors** column for a listed replication to view error details.