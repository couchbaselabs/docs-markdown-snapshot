---
title: Manage Cluster Access Credentials
description: Cluster access credentials provide programmatic and
  application-level access to data on a cluster.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/manage-database-users.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/clusters/manage-database-users.html)

# Manage Cluster Access Credentials

> Cluster access credentials provide programmatic and application-level access to data on a cluster. 

Cluster access credentials are distinct from organization roles and project roles, and are specific to a cluster. Each cluster access credential consists of a cluster access name, password, and a set of access levels or roles, depending on the chosen credential type. Use cluster access credentials to read or write bucket data using the Couchbase SDK and other supported tools.

For more information about cluster access credentials, see [Cluster Access](cluster-rbac.md).

> [!TIP]
> Capella Management API
> 
> In addition to the UI, you can configure your cluster access credentials using the [Capella Management REST API](../management-api-reference/index.md#tag/Database-Credentials).

## [](#prerequisites)Prerequisites

To manage cluster access credentials, you need the following:

* An existing Couchbase Capella cluster.
* One of the following project roles for the project containing the cluster:

  * [Project Owner](../projects/project-roles.md#project-owner-role)
  * [Cluster Manager](../projects/project-roles.md#project-cluster-manager-role)
* To use [advanced access credentials](cluster-rbac.md#advanced-access-credentials) and access roles, you must have a paid plan.

## [](#accessing-database-credentials)View Cluster Access Credentials and Access Roles

The **Access Control** page lists all the cluster access credentials and available access roles for the current cluster. You can manage existing cluster access credentials and access roles from this page or create new ones.

To view the **Access Control** page:

1. Open the **Cluster Access** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your cluster access credentials.
  3. Go to **Settings** **Cluster Access**.

## [](#create-database-credentials)Create Cluster Access Credentials

To create new cluster access credentials:

1. Open the **Cluster Access** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your cluster access credentials.
  3. Go to **Settings** **Cluster Access**.
2. Click **Create Access**.
3. Specify the access name and password:  
Cluster Access Name  
The cluster access name cannot exceed 35 characters in length or contain the following characters: `( ) < > @ , ; : \ " / [ ] ? = { }`  
Password  
Passwords must be at least 8 characters in length. They need 1 or more uppercase letters, lowercase letters, numbers, and special characters: `` ^ $ ( ) ? " ! @ # % , ' : _ ~ ` = + - ``  
Selecting **Auto-generate password** generates a random password that meets the requirements. Copy this password to a secure location, as you’re unable to view it again after creating the cluster access credentials.
4. Choose and configure basic or advanced access credentials:

  * Basic Access Credentials
  * Advanced Access Credentials

  1. Select **Basic Bucket Level Access**.
  2. Choose which bucket these cluster access credentials can access.  
  To grant access to all current and future buckets in the cluster, choose **All Buckets**.
  3. Select scope-level access.  
  Choose which scope these cluster access credentials can access.  
  To grant access to all current and future scopes in the selected bucket, choose **All Scopes**.
  4. Select collection-level access.  
  Choose which collection these cluster access credentials can access.  
  To grant access to all current and future collections in the selected scope, choose **All Collections**.
  5. Select access level.  
  Specify **Read**, **Write**, or **Read/Write** access to the chosen bucket, scope, and collection selections.
  6. (Optional) Add another level of access.  
  Click **Add Another Selection**.  
  Another line appears where you can select another bucket, scope, and collection for these cluster access credentials.

  1. Select **Advanced Role Based Access**.
  2. Select 1 or more predefined roles from the **Roles** list.  
  If there are no roles that meet your needs, you can create custom roles. For more information, see [Create Access Roles](#access-roles).
5. After configuring your cluster access credentials, click **Create Cluster Access**.

## [](#modify-database-credentials)Edit Cluster Access Credentials

To edit existing cluster access credentials:

1. Open the **Cluster Access** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your cluster access credentials.
  3. Go to **Settings** **Cluster Access**.
2. Click the cluster access credentials you’re modifying.
3. Edit the desired settings:

  1. You can change the password of any cluster access credential type by clicking **Change Password**.  
  > [!WARNING]  
  > To maintain cluster access for any applications using these access credentials, you must update your applications to use the new password.
  2. **Basic Access Credentials** allow you to change the bucket, scope, and collection action levels or add another selection.  
  For more information about choosing bucket, scope, and collection access levels, see [Basic Access Credentials](#bucket-level-access).
  3. **Advanced Access Credentials** allow you to change the assigned roles or [create new ones](#access-roles).  
  For more information about configuring access roles, see [Create Access Roles](#access-roles).
4. After making any changes, click **Save**.

## [](#delete-database-credentials)Delete Cluster Access Credentials

> [!WARNING]
> Deleting cluster access credentials can cause an application that’s using them to stop functioning. Always make sure that you have updated your application to use new credentials before deleting cluster access credentials.

To delete existing cluster access credentials:

1. Open the **Cluster Access** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your cluster access credentials.
  3. Go to **Settings** **Cluster Access**.
2. At the end of the row for the cluster access credentials you want to delete, click the Trash icon .
3. Confirm that you want to delete your cluster access credentials.
4. Click **Delete Cluster Access**.

## [](#access-roles)Create Access Roles

You can create access roles that bundle specific privileges together to simplify access assignments to your cluster. For more information about access roles, see [Advanced Access Credentials](cluster-rbac.md#Advanced Access Credentials).

> [!TIP]
> You can also create an access role while creating advanced cluster access credentials by clicking **Add New Role** on the **Create Cluster Access** page.

To create a new access role:

1. Open the **Cluster Access** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your cluster access credentials.
  3. Go to **Settings** **Cluster Access**.
2. Click the **Roles** tab.
3. Click **Create Role**.
4. Enter a role name and optional description.
5. Click **Assign Privileges**.
6. Select 1 or more privileges to assign to this role.  
The **Privileges** list organizes privileges into groups based on scope and functionality. For more information about each privilege, see [Privileges for Advanced Access Credentials](cluster-rbac.md#table-database-privileges).
7. After selecting all the privileges you want to assign to this role, review what resources each privilege has access to and adjust as needed.  
For example, some privileges default to **All Scopes** access, but you can change this to a specific scope. Global privileges have **All Buckets** access, which you cannot change.
8. Click **Assign**.
9. Click **Create Role**.

## [](#edit-access-roles)Edit Access Roles

You can edit access roles to modify their assigned privileges and resource access levels.

To edit an access role:

1. Open the **Cluster Access** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your cluster access credentials.
  3. Go to **Settings** **Cluster Access**.
2. Click the **Roles** tab.
3. Click the name of the role you want to edit.
4. Click **\+ Add Privilege**.  
You can add more privileges, remove existing ones, or change resource access levels for an assigned privilege.
5. After making any changes, click **Assign** and then **Save Role**.

## [](#delete-access-roles)Delete Access Roles

> [!CAUTION]
> You must remove an access role from all cluster access credentials before you can delete it. Deleting an access role is irreversible.

To delete an access role:

1. Open the **Cluster Access** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your cluster access credentials.
  3. Go to **Settings** **Cluster Access**.
2. Click the **Roles** tab.
3. At the end of the row for the access role you want to delete, click the Trash icon .
4. Confirm that you want to delete the role and click **Delete Role**.

## [](#manage-database-users-vault)Manage Cluster Access with Hashicorp Vault

The Couchbase Capella [Hashicorp Vault plug-in](https://github.com/couchbasecloud/vault-plugin-database-couchbasecapella) can serve as a centralized hub for secrets management. In addition to managing existing credentials, Vault’s Cluster Secrets Engine generates dynamic, short-lived cluster access credentials. This streamlines the management of cluster connections and roles, and you can customize permissions and TTL settings.

For more information, see the [Hashicorp Vault plug-in for Capella](https://github.com/couchbasecloud/vault-plugin-database-couchbasecapella).