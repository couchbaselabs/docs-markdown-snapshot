---
title: Stream Data from Couchbase Capella
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sources/pages/remote-cb-capella.adoc
  xref: xref:analytics:sources:remote-cb-capella.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/sources/remote-cb-capella.html)

# Stream Data from Couchbase Capella

> To continuously update Capella Analytics with data hosted on a Couchbase Capella operational cluster, create a remote link and collection. 

> [!TIP]
> For an example, see [Create Remote beer-sample Collections](../intro/examples.md#beer-sample).

## [](#encryption)Requirements for Couchbase Capella Links

The Capella operational cluster must be in the same organization as your Capella Analytics cluster. You must have RBAC access to the operational database to be able to create a link to it. See [Eventing Access Control](../../cloud/eventing/eventing-rbac.md).

Your Capella Analytics account must have either the [Project Owner](../admin/auth/auth-ui.md#project-owner-role) or [Project Manager](../admin/auth/auth-ui.md#project-cluster-manager-role) role to be able to create a link and its associated collection.

## [](#link)Create a Link to Couchbase Capella

To create a remote link to a Couchbase Capella operational cluster:

1. In the Capella UI, select the **Capella Analytics** tab.
2. Click a cluster name. The workbench opens.
3. Use the explorer to explore the existing databases, scopes, and collections. You can add a database and scope to hold the collection for the streamed data if necessary: see [Manage Capella Analytics Services Databases](manage-databases.md).
4. Select **Create** **Data Link**. The **Create Link for <cluster name> Cluster** dialog opens.
5. Select **Couchbase Server/Capella** then click **Continue**.
6. Under **Link Type**, select **Couchbase Capella**.
7. In the **Couchbase Link Name** field, enter a name for the link.
8. In the **Source Database** list, select the source Capella operational cluster.
9. Click **Save & Continue**. Capella Analytics creates the link.

You can now create a collection associated with that link.

## [](#create-a-collection-for-a-couchbase-data-service)Create a Collection for a Couchbase Data Service

To create a remote collection to receive data from a Couchbase Capella operational cluster:

1. In the **Create Link for <cluster name> Cluster** dialog, click **Create Linked Collection**. The **Create Collection Linked to <link name>** dialog opens.  
> [!NOTE]  
> If you closed the **Create Link for <cluster name> Cluster** dialog by clicking **Complete Later**, then under **LINKS** move your pointer over the name of the link and choose **⋮ (More)** **Create Linked Collection**.
2. In the **Collection Name** field, enter a name for your Capella Analytics collection.
3. In the **Configure Data Details** fields, select the names of the **Bucket**, **Scope**, and **Collection** you want to shadow.
4. Optionally, enter an expression in the **WHERE clause** field to filter the documents in the source collection. Do not include the `WHERE` keyword, and supply only a deterministic expression. For example, `activity = "eat"`.
5. Click **Create Collection**. Your collection appears in the explorer's **Data** section underneath its database and scope.

To create a remote collection using a `CREATE COLLECTION` statement, see [CREATE a Remote Collection](../sqlpp/5%5Fddl%5Fremote.md).

## [](#connect-the-link)Connect the Link

To have Capella Analytics start streaming data from the Couchbase Capella operational cluster, you must connect the link by either:

* Clicking **Connect Link** in the **Create Link for <cluster name> Cluster** dialog.
* Under **Links**, move your pointer over the name of the link and choose **⋮ (More)** **Connect**.

## [](#see-also)See Also

* [Query and Explore with the Workbench](../query/workbench.md)
* [Connect or Disconnect a Remote Link](connect-link.md)
* [Access Data](../intro/examples.md)