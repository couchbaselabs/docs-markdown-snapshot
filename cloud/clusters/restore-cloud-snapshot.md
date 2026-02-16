[View original HTML](/cloud/clusters/restore-cloud-snapshot.html)

> You can restore a cluster backup in a disaster recovery situation to restore your cluster to a previous point in time. 

|  | If your cluster uses Couchbase Server version 7.6.6 or later and is deployed on AWS or Azure, you can choose to replicate your backups to 2 regions, other than the region where your cluster is deployed. You can restore a replicated backup like any other backup for your cluster. Cluster backups for GCP clusters cannot be replicated to additional regions. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#prerequisites)Prerequisites

* You have the **Project Owner** role for the project with the cluster you want to restore. If you have the **Organization Owner** role, you have Project Owner permissions.  
For more information about roles in Capella, see [Manage Organizations and Access](../organizations/organization-projects-overview.md).
* You have [previously taken or scheduled](take-cloud-snapshot.md) a cluster backup.
* If you use [Customer Managed Encryption Keys (CMEK)](../security/cmek.md) on your cluster:

  * The Capella CMEK ID must still be available in your organization.
  * The Key ID for the backup you want to restore must be available and enabled in your Key Management System (KMS).  
To view the CMEK ID and Key IDs used by your backups, go to **Backup** **Cluster Backups** and expand the entry for a backup.

## [](#procedure)Procedure

You can restore a cluster backup from:

* [Your cluster’s **Backup** tab](#cluster), to restore a backup to the same cluster.
* [Your project’s **Backup** tab](#project), to restore a backup to a different cluster.

|  | Restoring a cluster backup also deletes all cluster access credentials and allowed IP addresses on your cluster. Before you restore a cluster backup, use version 4 of the Management API to [get a list of all available cluster access credentials](../management-api-reference/index.md#tag/Database-Credentials/operation/listDatabaseCredentials) and [get a list of all allowed IP addresses](../management-api-reference/index.md#tag/Allowed-CIDRs-%28Cluster%29/operation/listAllowedCidrs) on your cluster. You can use the list to recreate your cluster access credentials and allowed IP addresses later. If the number of nodes deployed in your cluster changed between your backup and restore operations, Capella reverts your cluster configuration to the number of nodes present in the backup. Take care when restoring backups to make sure you do not lose necessary node configuration changes. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

|  | To restore a cluster backup from the Capella Management API, see [Restore Backup](../management-api-reference/index.md#tag/Cloud-Snapshot-Backups-and-Restore/operation/restore). |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#cluster)Restore a Cluster Backup From the Cluster Backup Tab

If you restore from your cluster’s **Backup** tab, you can restore your backup to the same cluster.

To restore a cluster backup to the same cluster:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to restore a backup.
3. Go to **Backup** **Cluster Backups**.
4. In the list of cluster backups, find the backup you want to restore.
5. Click **Restore**.
6. Confirm that you want to restore the backup.
7. Click **Restore**.

### [](#project)Restore a Cluster Backup From the Project Backups Tab

If you restore from your project’s **Backups** tab, you can restore your backup to the same or a different cluster in your project.

To restore a backup to the same or a different cluster:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Projects**. Select the project where you want to restore a backup.
  2. Click your current project name or expand the project breadcrumb to select another project.
2. Go to the **Backups** tab.
3. For the cluster that has the backup you want to restore, click **See All Versions**.
4. For the specific backup you want to restore, click **Restore**.
5. (Cross-Region Backups Only) If your cluster backup was a cross-region backup, in the **Restore from** list, select the specific region that you want to use for your restore.
6. Do 1 of the following:

  1. To restore your backup to a new cluster, click **Restore To New Cluster** and enter a cluster name, description, CIDR block, and choose your Availability Zone configuration.  
  For more information about cluster configuration settings, see [Configure Your Cluster](databases.md).

|  | When restoring a backup that has cross-region copies, if you choose a different region in **Restore from** than the region where you want to deploy a new cluster, Capella tries to restore a copy from the same region as the new cluster, first. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  2. To restore to an existing cluster, in the **Restore To** list, choose the cluster you want to restore to.
7. Click **Restore**.
8. Confirm that you want to restore the backup.
9. Click **Submit**.

|  | You can only restore a backup to a different compatible cluster if both clusters are currently running Couchbase Server version 7.6.6 or later. If a cluster is running an earlier version of Couchbase Server, you cannot restore its backups to another cluster. For example, if you have 2 clusters, with the first cluster on Couchbase Server version 7.6.5 and the second on Couchbase Server version 7.6.6, you cannot restore a backup from the 7.6.5 cluster to the 7.6.6 cluster until you upgrade the 7.6.5 cluster. If you do upgrade a 7.6.5 cluster to a later version of Couchbase Server, backups taken while the cluster was on version 7.6.5 can still be restored to that same cluster. Restoring a backup taken on version 7.6.5 will temporarily restore the cluster to Couchbase Server version 7.6.5\. You can run an upgrade to restore the cluster back to a later version at any point after the restore. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#next-steps)Next Steps

Capella starts the restore process for your cluster backup on your cluster. Your cluster will be unavailable until the restore completes, and this can take some time.

All existing data on your cluster will be lost. Your cluster configuration may change to match the configuration of the cluster stored in the backup.

The time it takes to restore your cluster is not considered to be downtime based on the [Capella Cloud Service Availability agreement](https://www.couchbase.com/capellasla/).

You can view the details and status for all your cluster backup restores on the **Cluster Backup Restores** page.

|  | The **Size** of the cluster used size at the time of your backup is only an estimate. Capella calculates the cluster size information for a backup at the start of the backup process, based on the current size of your cluster. The actual size of a restored cluster may be different from this initial estimate. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |