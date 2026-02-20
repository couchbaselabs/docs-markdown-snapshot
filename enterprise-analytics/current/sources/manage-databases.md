---
title: Manage Enterprise Analytics Databases
description: In an Enterprise Analytics cluster, a database is the top-level
  container for organizing related information.You can add or delete databases
  using the UI or SQL++ for Enterprise Analytics statements.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sources/pages/manage-databases.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:enterprise-analytics:sources:manage-databases.adoc[]
---

[View original HTML](/enterprise-analytics/current/sources/manage-databases.html)

# Manage Enterprise Analytics Databases

> In an Enterprise Analytics cluster, a database is the top-level container for organizing related information.You can add or delete databases using the UI or SQL++ for Enterprise Analytics statements. 

## [](#prerequisites)Prerequisites

To use the Enterprise Analytics UI to manage databases, you need the `**Enterprise Analytics Access**` role along with specific privileges.

## [](#database)Create a Database

To create a database:

1. In the UI, select the **Workbench** tab.
2. Under **Databases**, click **\+ database**.
3. Enter a name for your database, and optionally, a name for your scope. The name must start with a letter and contain only upper- and lower-case letters (A-Z, a-z), numbers (0-9), or underscore (\_) and dash (-) characters. See [Requirements for Identifiers](../sqlpp/1a%5Fentities.md#names).
4. Click **Create**.

You can also use an SQL++ statement to create a database. See [CREATE DATABASE Statements](../sqlpp/5%5Fddl%5Fdatabase.md).

## [](#view-metadata-for-a-database)View Metadata for a Database

Each time you add a database, Enterprise Analytics records its metadata in the `System.Metadata.Database` collection. To view metadata for a database, you query this collection. See [Querying Metadata](../sqlpp/5%5Fddl%5Fmetadata.md).

## [](#delete-a-database)Delete a Database

When you delete a database, Enterprise Analytics deletes all of the scopes, collections, and other objects in that database.

> [!TIP]
> You cannot delete the system-supplied `Default` database.

1. In the UI, select the **Workbench** tab.
2. Browse to the database you want to delete and click the Recycle Bin icon.
3. To confirm that you want to delete the database, click **OK**.

You can also use an SQL++ statement to delete a database. See [DROP Statements](../sqlpp/5%5Fddl%5Fdrop.md).

## [](#next-steps)Next Steps

* [Stream Data from Remote Sources](manage-remote.md)
* [Manage Enterprise Analytics Scopes](manage-scopes.md)
* [Set Up an External Data Source](manage-external.md)