---
title: Manage Enterprise Analytics Scopes
description: Scopes are intermediary containers within a database to group
  related objects like collections, indexes, and functions.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/sources/pages/manage-scopes.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.0@enterprise-analytics:sources:manage-scopes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/sources/manage-scopes.html)

# Manage Enterprise Analytics Scopes

> Scopes are intermediary containers within a database to group related objects like collections, indexes, and functions. 

## [](#prerequisites)Prerequisites

To use the Enterprise Analytics UI to manage scopes, you need the `**Enterprise Analytics Access**` role along with specific privileges.

## [](#scope)Create a Scope

1. In the UI, select the **Workbench** tab.
2. On an existing database, click **\+ scope**.
3. Enter a name for your scope. The name must start with a letter and contain only upper- and lower-case letters (A-Z, a-z), numbers (0-9), or underscore (\_) and dash (-) characters. See [Requirements for Identifiers](../sqlpp/1a%5Fentities.md#names).
4. Click **Create**.

You can also use an SQL++ for Enterprise Analytics statement to create a scope. See [CREATE SCOPE Statements](../sqlpp/5%5Fddl%5Fscope.md).

## [](#view-metadata-for-a-scope)View Metadata for a Scope

Each time you add a scope, Enterprise Analytics records its metadata in the `System.Metadata.Dataverse` collection. To view metadata for a scope, you query this collection. See [Querying Metadata](../sqlpp/5%5Fddl%5Fmetadata.md).

## [](#delete-a-scope)Delete a Scope

When you delete a database, Enterprise Analytics deletes all of the scopes, collections, and other objects in that database.

1. In the UI, select the **Workbench** tab.
2. Browse to the scope you want to delete and click the Recycle Bin icon.
3. To confirm that you want to delete the scope, click **OK**.

You can also use an SQL++ for Enterprise Analytics statement to delete a scope. See [DROP Statements](../sqlpp/5%5Fddl%5Fdrop.md).

## [](#next-steps)Next Steps

* [Stream Data from Remote Sources](manage-remote.md)
* [Set Up an External Data Source](manage-external.md)