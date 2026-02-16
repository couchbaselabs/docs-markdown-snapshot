[View original HTML](/analytics/sources/manage-scopes.html)

> Scopes are intermediary containers within a database to group related objects like collections, indexes, links, and functions. You can add or delete scopes using the UI or SQL++ for Capella Analytics statements. 

## [](#prerequisites)Prerequisites

To use the Capella Analytics UI to manage scopes, you need one of the following Capella roles:

* [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner)
* [Project Owner](../admin/auth/auth-ui.md#project-owner-role) for the project holding the cluster you’re working with.
* [Data Writer](../admin/auth/auth-ui.md#project-cluster-data-reader-writer) for the project holding the cluster you’re working with.

## [](#scope)Create a Scope

To create a scope:

1. In the Capella UI, select the **Capella Analytics** tab.
2. Click a cluster name. The workbench opens.
3. Use the explorer to locate the database where you want to add the scope.
4. Move your cursor over the name of the database and then choose **⋮ (More)** **Add Scope**. The Configure New Scope dialog opens.
5. Enter a name for your scope. The name must start with a letter and contain only upper- and lower-case letters (A-Z, a-z), numbers (0-9), or underscore (\_) and dash (-) characters. See [Requirements for Identifiers](../sqlpp/1a%5Fentities.md#names).
6. Click **Create**. Your scope appears under the database in the explorer.

You can also use an SQL++ for Capella Analytics statement to create a scope. See [CREATE SCOPE Statements](../sqlpp/5%5Fddl%5Fscope.md).

## [](#view-metadata-for-a-scope)View Metadata for a Scope

Each time you add a scope, Capella Analytics records its metadata in the `System.Metadata.Dataverse` collection. To view metadata for a scope, you query this collection. See [Querying Metadata](../sqlpp/5%5Fddl%5Fmetadata.md).

## [](#delete-a-scope)Delete a Scope

When you delete a scope, Capella Analytics deletes all of the collections and other objects in that scope.

|  | You cannot delete the system-supplied Default scope. |
|  | ---------------------------------------------------- |

1. In the Capella UI, select the **Capella Analytics** tab.
2. Click a cluster name. The workbench opens.
3. Move your cursor over the name of the scope and then choose **⋮ (More)** **Delete Scope**. The Delete Scope dialog opens.
4. To confirm this action, type `delete` and then click **Delete**.

You can also use an SQL++ for Capella Analytics statement to delete a scope. See [DROP Statements](../sqlpp/5%5Fddl%5Fdrop.md).

## [](#next-steps)Next Steps

* [Stream Data from Remote Sources](manage-remote.md)
* [Set Up an External Data Source](manage-external.md)
* [Set Up a Standalone Collection](manage-columnar.md)