---
title: Manage Scopes and Collections
description: Create, view, and delete scopes and collections to categorize and
  organize documents within a bucket in a Capella operational cluster.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/data-service/scopes-collections.adoc
  xref: xref:cloud:clusters:data-service/scopes-collections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/data-service/scopes-collections.html)

# Manage Scopes and Collections

> Create, view, and delete scopes and collections to categorize and organize documents within a bucket in a Capella operational cluster. 

Scopes and collections categorize and organize documents within a bucket. A collection is a data container within a bucket. A scope is a mechanism that groups multiple collections. Each cluster can hold up to 1000 scopes and up to 1000 collections. For a complete overview, see [Buckets, Scopes, and Collections](about-buckets-scopes-collections.md).

## [](#prerequisites)Prerequisites

To create, modify, or delete scopes and collections in a cluster, you need:

* The [Project Owner](../../projects/project-roles.md#project-owner-role) or [Cluster Manager](../../projects/project-roles.md#project-cluster-manager-role) role for your cluster's project. If you have the [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner) role, you have `Project Owner` access.

## [](#create-scope-collection)Create a Scope or Collection

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Data Tools**.
4. In the side pane, expand **Data** to open the **Data Insights** area.
5. Choose between creating a **Scope** or a **Collection**:

  * Scope
  * Collection

  1. In the **Data Insights** area, find the bucket where you want to create a scope.
  2. Next to the bucket name where you want to create a scope, go to **More Options (⋮)** **Add Scope**.
  3. In the **Scope Name** field, enter a scope name.  
  A scope name can only contain the `A-Z`, `a-z`, and `0-9` characters as well as the `-`, `_`, and `%` symbols. It cannot start with either the `_` or `%` symbols. It cannot be longer than 251 characters in length and is case-sensitive.
  4. Click **Create Scope**.

  1. In the **Data Insights** area, find the bucket and scope where you want to create a collection.
  2. Next to the scope name where you want to create a collection, go to **More Options (⋮)** **Add Collection**.
  3. In the **Collection Name** field, enter a collection name.  
  A collection name can only contain the `A-Z`, `a-z`, and `0-9` characters as well as the `-`, `_`, and `%` symbols. It cannot start with either the `_` or `%` symbols. It cannot be longer than 251 characters in length and is case-sensitive.
  4. In the **TTL** field, enter an expiration time in seconds for the new collection. By default, the TTL for collections is `0`, meaning it uses its bucket's TTL value. To prevent the bucket's TTL from setting a default expiration for your collection's documents, set the TTL value to `-1`.  
  For information about collection expiration, see [Expiration](../../../server/current/learn/data/expiration.md).
  5. Click **Create Collection**.

## [](#view-scopes-and-collections)View Scopes and Collections

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Data Tools**.
4. In the side pane, expand **Data** to open the **Data Insights** area.
5. In the **Data Insights** area, explore the tree structure to view your buckets, scopes and collections.

## [](#delete-scope-collection)Delete a Scope or Collection

> [!CAUTION]
> * Deleting a **Scope** deletes all of the collections and documents in that scope from the cluster. You can restore them from a previous backup.
> * Deleting a **Collection** deletes all of the documents within it from the cluster. You can restore these documents from a previous backup.

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Data Tools**.
4. In the side pane, expand **Data** to open the **Data Insights** area.
5. Choose between deleting a **Scope** or a **Collection**:

  * Scope
  * Collection

  1. In the **Data Insights** area, find the bucket where you want to delete a scope.
  2. Next to the scope name you want to delete, go to **More Options (⋮)** **Delete Scope**.
  3. Confirm that you want to delete the scope and click **Delete**.

  1. In the **Data Insights** area, find the bucket and scope where you want to delete a collection.
  2. Next to the collection name you want to delete, go to **More Options (⋮)** **Delete Collection**.
  3. Confirm that you want to delete the collection and click **Delete**.

## [](#see-also)See Also

* [Buckets, Scopes, and Collections](about-buckets-scopes-collections.md)
* [Manage Buckets](manage-buckets.md)
* [Manage Documents with the Capella UI](manage-documents.md)
* [Manage Bucket Backups](../manage-backup.md)