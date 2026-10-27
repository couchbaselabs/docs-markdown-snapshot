---
title: Manage Scopes and Collections
description: Create, view, and delete scopes and collections to categorize and
  organize documents within a bucket in a Capella operational cluster.
pubDate: 2026-10-27T04:30:23.844Z
meta:
  component:
    title: Capella Operational
    version: ""
  topic_type: guide
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/data-service/scopes-collections.adoc
  xref: xref:cloud:clusters:data-service/scopes-collections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/data-service/scopes-collections.html)

# Manage Scopes and Collections

> Create, view, and delete scopes and collections to categorize and organize documents within a bucket in a Capella operational cluster. 

Scopes and collections categorize and organize documents within a bucket. A collection is a data container within a bucket. A scope is a mechanism that groups multiple collections. Each cluster can hold up to 1,000 scopes and up to 1,000 collections. For more information, see [Buckets, Scopes, and Collections](about-buckets-scopes-collections.md).

## [](#prerequisites)Prerequisites

To create, view, or delete scopes and collections in a cluster, you need:

* The [Project Owner](../../projects/project-roles.md#project-owner-role) or [Cluster Manager](../../projects/project-roles.md#project-cluster-manager-role) role for your cluster's project. If you have the [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner) role, you have `Project Owner` access.

## [](#create-scope-collection)Create a Scope or Collection

To create a scope or collection:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Choose 1 of the following options:

  * To create a single scope or collection, go to **Data Tools**.
  * To create multiple scopes and collections at once, go to **Buckets**.

  * Data Tools
  * Buckets

  1. In the side pane, choose whether to create a **Scope** or a **Collection**:

    * To create a **Scope**, find the bucket where you want to create a scope.

      1. Next to the name of the bucket where you want to create a scope, go to **More Options (⋮)** **Add Scope**.
      2. In the **Scope Name** field, enter a scope name.  
            A scope name can contain only the `A-Z`, `a-z`, and `0-9` characters as well as the `-`, `_`, and `%` symbols. It cannot start with `_` or `%`. It cannot be longer than 251 characters and is case-sensitive.  
            > [!CAUTION]  
            > You cannot change a scope's name after you create it.
      3. Click **Create Scope**.
    * To create a **Collection**, find the bucket and scope where you want to create a collection.

      1. Next to the name of the scope where you want to create a collection, go to **More Options (⋮)** **Add Collection**.
      2. In the **Collection Name** field, enter a collection name.  
            A collection name can contain only the `A-Z`, `a-z`, and `0-9` characters as well as the `-`, `_`, and `%` symbols. It cannot start with `_` or `%`. It cannot be longer than 251 characters and is case-sensitive.  
            > [!CAUTION]  
            > You cannot change a collection's name after you create it.
      3. In the **TTL** field, enter a time to live (TTL) in seconds for the new collection. By default, the TTL for collections is `0`, meaning it uses its bucket's TTL value. To prevent the bucket's TTL from setting a default expiration for your collection's documents, set the TTL value to `-1`.  
            For more information about collection expiration, see [Expiration](../../../server/current/learn/data/expiration.md).
      4. Click **Create Collection**.

  1. In the **Buckets** list, next to the name of the bucket where you want to create a scope or collection, click ![Expand icon](../_images/angle-down-icon.png).
  2. Choose whether to create a **Scope** or a **Collection**:

    * To create a **Scope**, go to the end of the bucket's scope list and click **Add scope**.

      1. In the **Scope name** field, enter a scope name.  
            A scope name can contain only the `A-Z`, `a-z`, and `0-9` characters as well as the `-`, `_`, and `%` symbols. It cannot start with `_` or `%`. It cannot be longer than 251 characters and is case-sensitive.  
            > [!CAUTION]  
            > You cannot change a scope's name after you create it.
      2. Click **Create**.
      3. (Optional) Create another scope.
      4. When you're done, click **Cancel**.
    * To create a **Collection**, next to the name of the scope where you want to create a collection, click ![Expand icon](../_images/angle-down-icon.png).

      1. At the end of the scope's collection list, click **Add collection**.
      2. In the **Collection name** field, enter a collection name.  
            A collection name can contain only the `A-Z`, `a-z`, and `0-9` characters as well as the `-`, `_`, and `%` symbols. It cannot start with `_` or `%`. It cannot be longer than 251 characters and is case-sensitive.  
            > [!CAUTION]  
            > You cannot change a collection's name after you create it.
      3. In the **Document expiry** list, choose how long documents in the collection exist before they expire:

        * **Inherit from bucket**: Use the bucket's time to live (TTL) setting. This is the default.
        * **Never expire**: Keep documents until you delete them.
        * **Expire after…**: Enter a TTL for the new collection.
      4. Click **Create**.
      5. (Optional) Create another collection in the same scope.
      6. When you're done, click **Cancel**.

## [](#view-scopes-collections)View Scopes and Collections

To view scopes and collections:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Choose 1 of the following options:

  * For a quick overview of your bucket's scopes and collections, go to **Data Tools**.
  * To view details and statistics for all of your cluster's buckets, scopes, and collections, go to **Buckets**.

  * Data Tools
  * Buckets  
In the side pane, explore the tree structure to view your buckets, scopes, and collections.

  1. In the **Buckets** list, view the following statistics for each bucket:

    * **Documents**: The number of documents in the bucket.
    * **Type**: Whether the bucket stores data in-memory and on disk, or in-memory only. This column appears only if Memory Only buckets are available to your organization.
    * **Storage**: The bucket's storage backend, Couchstore or Magma.
    * **Ops/Sec**: The number of operations per second on the bucket.
    * **Resident Ratio**: The percentage of the bucket's data held in-memory.
    * **Disk Used**: The amount of disk space the bucket uses.
    * **RAM Used/Quota**: The amount of memory the bucket uses, compared to its total memory quota across all data nodes.
  2. Next to the name of the bucket you want to view, click ![Expand icon](../_images/angle-down-icon.png).  
  The bucket's scopes appear in alphabetical order, with the `_default` and `_system` scopes last. Each scope shows the number of collections it holds.
  3. Next to the name of the scope you want to view, click ![Expand icon](../_images/angle-down-icon.png).  
  The scope's collections appear with the following statistics:

    * **Documents**: The number of documents in the collection.
    * **Memory used**: The amount of memory the collection uses.
    * **Disk utilization**: The amount of disk space the collection uses.
    * **Ops/sec**: The number of operations per second on the collection.
    * **Document expiry (TTL)**: Whether the collection inherits the bucket's time to live (TTL) setting, never expires, or expires after a set amount of time.  
      > [!NOTE]  
      > A dash (`-`) means a statistic is not available yet.

## [](#delete-scope-collection)Delete a Scope or Collection

> [!CAUTION]
> * You cannot delete:
> 
>   * The `_default` scope or collection.
>   * The `_system` scope or its collections.
>   * A collection that's linked to an App Endpoint.  
>   To delete a collection that's linked to an App Endpoint, remove the link first.
> * Deleting a **Scope** or **Collection** deletes all of its documents from the cluster. You can restore your collections and documents from a previous backup. For more information, see [Restore a Bucket Backup](../manage-restore.md).

To delete a scope or collection:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Choose 1 of the following options:

  * Go to **Data Tools**.
  * Go to **Buckets**.

  * Data Tools
  * Buckets

  1. In the side pane, choose whether to delete a **Scope** or a **Collection**:

    * To delete a **Scope**, in the side pane, find the bucket where you want to delete a scope.

      1. Next to the name of the scope you want to delete, go to **More Options (⋮)** **Delete Scope**.
      2. Confirm that you want to delete the scope and click **Delete**.
    * To delete a **Collection**, in the side pane, find the bucket and scope where you want to delete a collection.

      1. Next to the name of the collection you want to delete, go to **More Options (⋮)** **Delete Collection**.
      2. Confirm that you want to delete the collection and click **Delete**.

  1. In the **Buckets** list, next to the name of the bucket where you want to delete a scope or collection, click ![Expand icon](../_images/angle-down-icon.png).
  2. Choose whether to delete a **Scope** or a **Collection**:

    * To delete a **Scope**, click the trash can icon ().

      1. Confirm that you want to delete the scope and click **Delete**.
    * To delete a **Collection**, click the trash can icon ().

      1. Confirm that you want to delete the collection and click **Delete**.

## [](#see-also)See Also

* [Buckets, Scopes, and Collections](about-buckets-scopes-collections.md)
* [Manage Buckets](manage-buckets.md)
* [Manage Documents with the Capella UI](manage-documents.md)
* [Manage Bucket Backups](../manage-backup.md)