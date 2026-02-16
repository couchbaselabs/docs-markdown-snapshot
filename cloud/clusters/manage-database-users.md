[View original HTML](/cloud/clusters/manage-database-users.html)

> Cluster access credentials provide programmatic and application-level access to data on a cluster. Only cluster access credentials can access data. 

This page provides information about cluster access credentials and how they work. You’ll also find procedures for creating and managing cluster access credentials for a cluster through the Capella UI, allowing you to provide programmatic and application-level access to data.

|  | Capella Management API You can also configure your cluster access credentials using the [Capella Management REST API](../management-api-reference/index.md#tag/Database-Credentials). |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#about-database-credentials)About Cluster Access Credentials

Cluster access credentials are separate from [organization roles](../organizations/organization-user-roles.md) and [project roles](../projects/project-roles.md). Your Capella user account’s organization and project roles control your access to areas of the Capella UI, while cluster access credentials control programmatic and application-level access to data.

Cluster access credentials are specific to a cluster and consist of a cluster access name, password, and a set of [bucket, scope, and collection access levels](#about-database-user-permissions).

|  | Cluster access credentials are distinct and not associated with a particular user. They do not control access to data tools, like the Query tab in the Capella UI. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### [](#about-database-user-permissions)Cluster Access Credentials and Access

In the Capella UI, you assign cluster access credentials on a per-bucket, per-scope, and per-collection basis. For example, you could assign cluster access credentials access to all buckets and scopes in a cluster, assign different access levels to individual buckets, or assign access to just a single collection. This system allows you to mix and match access levels to different buckets, scopes, and collections in a cluster to satisfy your application and security requirements.

The following table describes the available bucket access options and their associated privileges.

__Table 1\. Cluster Access Privileges__
| Access         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Read**       | Grants the privileges of the following Couchbase roles: [data\_reader](../../server/current/learn/security/roles.md#data-reader) [data\_dcp\_reader](../../server/current/learn/security/roles.md#data-dcp-reader) [data\_monitoring](../../server/current/learn/security/roles.md#data%5Fmonitor) [fts\_searcher](../../server/current/learn/security/roles.md#search-reader) [query\_select](../../server/current/learn/security/roles.md#query-select) [analytics\_reader](../../server/current/learn/security/roles.md#analytics-reader) [query\_execute\_global\_functions](../../server/current/learn/security/roles.md#execute-global-functions) [query\_execute\_global\_external\_functions](../../server/current/learn/security/roles.md#execute-global-external-functions) [analytics\_select](../../server/current/learn/security/roles.md#analytics-select) [external\_stats\_reader](../../server/current/learn/security/roles.md#external-stats-reader) \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] [query\_execute\_functions](../../server/current/learn/security/roles.md#execute-scope-functions) [query\_execute\_external\_functions](../../server/current/learn/security/roles.md#execute-scope-external-functions) [query\_use\_sequences](../../server/current/learn/security/roles.md#query-use-sequences) [1](#%5Ffootnoteref%5F1). The external\_stats\_reader role is only granted when cluster access credentials are given read access to _all_ buckets in a cluster. |
| **Write**      | Grants the privileges of the following Couchbase roles: [data\_writer](../../server/current/learn/security/roles.md#data-writer) [fts\_admin](../../server/current/learn/security/roles.md#search-admin) [query\_insert](../../server/current/learn/security/roles.md#query-insert) [query\_update](../../server/current/learn/security/roles.md#query-update) [query\_delete](../../server/current/learn/security/roles.md#query-delete) [query\_manage\_index](../../server/current/learn/security/roles.md#query-manage-index) [replication\_target](../../server/current/learn/security/roles.md#xdcr-inbound) [analytics\_admin](../../server/current/learn/security/roles.md#analytics-admin) [query\_manage\_global\_functions](../../server/current/learn/security/roles.md#manage-global-functions) [query\_manage\_global\_external\_functions](../../server/current/learn/security/roles.md#manage-global-external-functions) [analytics\_manager](../../server/current/learn/security/roles.md#analytics-manager) [scope\_admin](../../server/current/learn/security/roles.md#manage-scopes) [query\_manage\_functions](../../server/current/learn/security/roles.md#manage-scope-functions) [query\_manage\_external\_functions](../../server/current/learn/security/roles.md#manage-scope-external-functions) [query\_manage\_sequences](../../server/current/learn/security/roles.md#query-manage-sequences)                                                                           |
| **Read/Write** | Grants the privileges of the following Couchbase roles: All the privileges of [Read](#database-role-read). All the privileges of [Write](#database-role-write).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## [](#accessing-database-credentials)View Cluster Access Credentials

The **Cluster Access** page lists existing cluster access credentials for a cluster in a table format, with sortable columns and rows for each entry. You can also create, modify, and delete cluster access credentials from this page.

Each cluster access credentials row contains the following information:

Cluster Access Name

The name that identifies the cluster access credentials.

Created By

The organization user who created the cluster access credentials.

Created On

The creation date and age of the cluster access credentials. The color-coded status indicator in this column uses age to help identify older credentials that need rotation:

* Green: Under 90 days old
* Yellow: 90—​180 days old
* Red: Over 180 days old

### [](#prerequisites)Prerequisites

To view the **Cluster Access** page, you need the following:

* One of the following project roles for the project containing the cluster:

  * [Project Owner](../projects/project-roles.md#project-owner-role)
  * [Cluster Viewer](../projects/project-roles.md#project-cluster-viewer-role)
  * [Data Reader](../projects/project-roles.md#project-cluster-data-reader)
  * [Data Writer](../projects/project-roles.md#project-cluster-data-reader-writer)

### [](#procedure)Procedure

1. Open the **Cluster Access** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your cluster access credentials.
  3. Go to **Settings** **Cluster Access**.

## [](#create-database-credentials)Create Cluster Access Credentials

Use cluster access credentials to read or write bucket data using the Couchbase SDK and other supported tools.

### [](#prerequisites-2)Prerequisites

To create cluster access credentials, you need the following:

* The [Project Owner](../projects/project-roles.md#project-owner-role) role for the project containing the cluster where you’re creating the cluster access credentials.

### [](#procedure-2)Procedure

1. Open the **Cluster Access** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your cluster access credentials.
  3. Go to **Settings** **Cluster Access**.
2. Click **Create Access**
3. Specify the cluster access name and password:  
Cluster Access Name  
The cluster access name cannot exceed 35 characters in length and can’t contain the following characters: `( ) < > @ , ; : \ " / [ ] ? = { }`  
Password  
Passwords must be at least eight characters in length. They need one or more uppercase letters, lowercase letters, numbers, and special characters: `` ^ $ ( ) ? " ! @ # % , ' : _ ~ ` = + - ``  
Selecting **Auto-generate password** generates a random password that meets the requirements. Copy this password to a secure location, as you’re unable to view it again after creating the cluster access credentials.
4. Select bucket-level access.  
In the **Bucket Level Access** section, use the **Bucket** drop-down menu to specify a bucket you want these cluster access credentials to access. To grant access to all current and future buckets in the cluster, choose the **All Buckets** option.
5. Select scope-level access.  
Use the **Scope** drop-down menu to specify the scope you want your cluster access credentials to access. To grant access to all current and future scopes in the selected bucket, choose the **All Scopes** option.
6. Select collection-level access.  
Use the **Collection** drop-down menu to specify a collection you want your cluster access credentials to access. To grant access to all current and future collections in the selected scope, choose the **All Collections** option.
7. Select access level.  
Use the **Access** drop-down menu to specify Read, Write, or Read/Write access to the chosen bucket and scope selection.
8. (Optional) Add another level of access.  
Cluster access credentials can access a selection of multiple buckets, scopes, and collections in a cluster.

  1. Click **Add Another Selection**.  
  The **Bucket Level Access** section adds another line where you can select another bucket, scope, and collection for these cluster access credentials.
9. Once you have finished configuring the levels of access, click **Create Cluster Access**.

## [](#modify-database-credentials)Modify Cluster Access Credentials

After creating cluster access credentials, you can change the password or the levels of bucket access.

### [](#prerequisites-3)Prerequisites

To modify cluster access credentials, you need the following:

* The [Project Owner](../projects/project-roles.md#project-owner-role) role for the project with the cluster access credentials.

### [](#procedure-3)Procedure

1. Open the **Cluster Access** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your cluster access credentials.
  3. Go to **Settings** **Cluster Access**.
2. Click the access name of the cluster access credentials you’re modifying.
3. Using the **Change Password** button, you can change the password for the cluster access credentials.  
See [access selection](#passwords) for password requirement information.

|  | To maintain cluster access for any applications using these credentials, you must update your applications to use the new password. |
|  | ----------------------------------------------------------------------------------------------------------------------------------- |
4. In the **Bucket Level Access** section, change any existing levels of access or add more.  
See the [access selection](#bucket-level-access) steps for creating cluster access credentials for details on choosing bucket, scope, and collection access levels.
5. Once you have made your changes, click **Apply**.

## [](#delete-database-credentials)Delete Cluster Access Credentials

|  | Deleting cluster access credentials can cause an application that’s using them to stop functioning. Always make sure that you have updated your application to use new credentials before deleting cluster access credentials. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### [](#prerequisites-4)Prerequisites

To delete cluster access credentials, you need the following:

* The [Project Owner](../projects/project-roles.md#project-owner-role) role for the project with the cluster access credentials you’re deleting.

### [](#procedure-4)Procedure

1. Open the **Cluster Access** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your cluster access credentials.
  3. Go to **Settings** **Cluster Access**.
2. At the end of the row for the cluster access credentials you want to delete, click the Trash icon .  
This opens the **Delete Cluster Access** dialog.
3. Type `delete` into the provided field and click **Delete Cluster Access**.  
A small notification indicates that Capella successfully deleted the cluster access credentials.

## [](#manage-database-users-vault)Manage Cluster Access with Hashicorp Vault

The Couchbase Capella [Hashicorp Vault plug-in](https://github.com/couchbasecloud/vault-plugin-database-couchbasecapella) can serve as a centralized hub for secrets management. In addition to managing existing credentials, Vault’s Cluster Secrets Engine generates dynamic, short-lived cluster access credentials. This streamlines the management of cluster connections and roles, and you can customize permissions and TTL settings.

For more information, see the [Hashicorp Vault plug-in for Capella](https://github.com/couchbasecloud/vault-plugin-database-couchbasecapella).