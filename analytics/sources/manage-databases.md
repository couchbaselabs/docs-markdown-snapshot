---
title: Manage Capella Analytics Services Databases
description: In a Capella Analytics cluster, a database is the top-level
  container for organizing related information. You can add or delete databases
  using the UI or SQL++ for Capella Analytics statements.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sources/pages/manage-databases.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/analytics/sources/manage-databases.html)

# Manage Capella Analytics Services Databases

> In a Capella Analytics cluster, a database is the top-level container for organizing related information. You can add or delete databases using the UI or SQL++ for Capella Analytics statements. 

## [](#prerequisites)Prerequisites

To use the Capella Analytics UI to manage databases, you need one of the following Capella roles:

* [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner)
* [Project Owner](../admin/auth/auth-ui.md#project-owner-role) for the project holding the cluster you’re working with.
* [Data Writer](../admin/auth/auth-ui.md#project-cluster-data-reader-writer) for the project holding the cluster you’re working with.

## [](#database)Create a Database

To create a database:

1. In the Capella UI, select the **Capella Analytics** tab.
2. Click a cluster name. The workbench opens.  
If the Add Data Source dialog opens, click the X icon to close it.
3. At the top of the explorer, click **Create** **New Database**. The Configure New Database dialog opens.
4. Enter a name for your database. The name must start with a letter and contain only upper- and lower-case letters (A-Z, a-z), numbers (0-9), or underscore (\_) and dash (-) characters. See [Requirements for Identifiers](../sqlpp/1a%5Fentities.md#names).
5. Click **Create Database**. Your database appears in the explorer.

You can also use an SQL++ statement to create a database. See [CREATE DATABASE Statements](../sqlpp/5%5Fddl%5Fdatabase.md).

## [](#view-metadata-for-a-database)View Metadata for a Database

Each time you add a database, Capella Analytics records its metadata in the `System.Metadata.Database` collection. To view metadata for a database, you query this collection. See [Querying Metadata](../sqlpp/5%5Fddl%5Fmetadata.md).

## [](#delete-a-database)Delete a Database

When you delete a database, Capella Analytics deletes all of the scopes, collections, and other objects in that database.

> [!TIP]
> You cannot delete the system-supplied `Default` database.

1. In the Capella UI, select the **Capella Analytics** tab.
2. Click a cluster name. The workbench opens.
3. Move your cursor over the name of the database and then choose **⋮ (More)** **Delete Database**. The Delete Database dialog opens.
4. To confirm this action, type `delete` and then click **Delete**.

You can also use an SQL++ statement to delete a database. See [DROP Statements](../sqlpp/5%5Fddl%5Fdrop.md).

## [](#next-steps)Next Steps

* [Manage Capella Analytics Services Scopes](manage-scopes.md)
* [Stream Data from Remote Sources](manage-remote.md)
* [Set Up an External Data Source](manage-external.md)
* [Set Up a Standalone Collection](manage-columnar.md)