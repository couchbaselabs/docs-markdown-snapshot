---
title: Manage Scopes and Collections
description: Scopes and collections, which allow documents to be categorized and
  organized within a bucket, can be created and deleted within the Capella UI.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/data-service/scopes-collections.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:clusters:data-service/scopes-collections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/data-service/scopes-collections.html)

# Manage Scopes and Collections

> Scopes and collections, which allow documents to be categorized and organized within a bucket, can be created and deleted within the Capella UI. 

Scopes and collections categorize and organize documents within a bucket. A collection is a data container within a bucket. A scope is a mechanism that groups multiple collections. Each cluster can hold up to 1000 scopes and up to 1000 collections. For a complete overview, see [Buckets, Scopes, and Collections](about-buckets-scopes-collections.md).

## [](#accessing-scopes-and-collections-in-the-couchbase-capella-ui)Accessing Scopes and Collections in the Couchbase Capella UI

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Data Tools**.
4. In the side pane, expand **Data** to open the **Data Insights** area.
5. In the **Data Insights** area, explore the tree structure to view your buckets, scopes and collections.

## [](#create-scope)Create a Scope

To create a scope, you need the [Project Owner or Cluster Manager role for the project with the cluster where you’re creating the scope. ](../../projects/project-roles.md#project-owner-role)

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Data Tools**.
4. In the side pane, expand **Data** to open the **Data Insights** area.
5. In the **Data Insights** area, find the bucket where you want to create a scope.
6. Next to the bucket name where you want to create a scope, go to **More Options (⋮)** **Add Scope**.
7. In the **Scope Name** field, enter a scope name.  
A scope name can only contain the `A-Z`, `a-z`, and `0-9` characters as well as the `-`, `_`, and `%` symbols. It cannot start with either the `_` or `%` symbols. It cannot be longer than 251 characters in length and is case-sensitive.
8. Click **Create Scope**.

## [](#delete-a-scope)Delete a Scope

To delete a scope, you need the [Project Owner or Cluster Manager role for the project with the cluster where you’re deleting a scope. ](../../projects/project-roles.md#project-owner-role)

> [!CAUTION]
> Deleting a scope deletes all of the collections and documents in that scope from the cluster. You can only restore them from a previous backup.

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Data Tools**.
4. In the side pane, expand **Data** to open the **Data Insights** area.
5. In the **Data Insights** area, find the bucket where you want to delete a scope.
6. Next to the scope name you want to delete, go to **More Options (⋮)** **Delete Scope**.
7. Confirm that you want to delete the scope.
8. Click **Delete**

## [](#create-collection)Create a Collection

To create a collection, you need the [Project Owner or Cluster Manager role for the project with the cluster where you’re creating the collection. ](../../projects/project-roles.md#project-owner-role)

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Data Tools**.
4. In the side pane, expand **Data** to open the **Data Insights** area.
5. In the **Data Insights** area, find the bucket and scope where you want to create a collection.
6. Next to the scope name where you want to create a collection, go to **More Options (⋮)** **Add Collection**.
7. In the **Collection Name** field, enter a collection name.  
A collection name can only contain the `A-Z`, `a-z`, and `0-9` characters as well as the `-`, `_`, and `%` symbols. It cannot start with either the `_` or `%` symbols. It cannot be longer than 251 characters in length and is case-sensitive.
8. In the **TTL** field, enter an expiration time in seconds for the new collection. By default, the TTL for collections is `0`, meaning it uses its bucket’s TTL value. To prevent the bucket’s TTL from setting a default expiration for your collection’s documents, set the TTL value to `-1`.  
For information about collection expiration, see [Expiration](../../../server/current/learn/data/expiration.md).
9. Click **Create Collection**.

## [](#delete-a-collection)Delete a Collection

To delete a collection, you need the [Project Owner or Cluster Manager role for the project with the cluster where you’re deleting the collection. ](../../projects/project-roles.md#project-owner-role)

> [!CAUTION]
> Deleting a collection deletes all of the documents within it from the cluster. You can restore these documents from a previous backup.

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Data Tools**.
4. In the side pane, expand **Data** to open the **Data Insights** area.
5. In the **Data Insights** area, find the bucket and scope where you want to delete a collection.
6. Next to the collection name you want to delete, go to **More Options (⋮)** **Delete Collection**.
7. Confirm that you want to delete the collection.
8. Click **Delete**.