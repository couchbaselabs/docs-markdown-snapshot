---
title: Stream Data from Couchbase Server
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sources/pages/remote-cb-server.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:analytics:sources:remote-cb-server.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/sources/remote-cb-server.html)

# Stream Data from Couchbase Server

> To continuously update a Capella Analytics collection with data hosted on Couchbase Server, create a remote link and collection. 

> [!TIP]
> For an example, see [Create Remote beer-sample Collections](../intro/examples.md#beer-sample).

## [](#encryption)Requirements

Your Capella Analytics account must have either the [Project Owner](../admin/auth/auth-ui.md#project-owner-role) or [Project Manager](../admin/auth/auth-ui.md#project-cluster-manager-role) role to be able to create a link and its associated collection.

You need to take the following steps on your Couchbase Server database:

* Configure your Couchbase Server cluster’s network to allow access from Capella Analytics. The steps you must take depend on how and where you deployed your Couchbase Server database. For example, suppose you deployed a self-managed Couchbase Server in AWS. Then to allow Capella Analytics to connect, create a VPC peering connection between the VPCs for your Capella Analytics database and the Couchbase Server cluster.
* Create a user and password for Capella Analytics to use when connecting. Give this user read/write permissions for all buckets and scopes you want to stream. See [Manage Users, Groups, and Roles](../../server/current/manage/manage-security/manage-users-and-roles.md).
* Get the hostname or external IP address for one of the Couchbase Server nodes. You supply this value to Capella Analytics as the connection string.
* Save a copy of the Couchbase Server’s cluster certificate. You can get the certificate from two places:

  * Copy the certificate from the Couchbase Server Web Console’s **Security** **Certificate** page under the **Trusted Root Certificate**.
  * Get the certificate by calling Couchbase Server’s [/pools/default/trustedCAs REST API](../../server/current/rest-api/get-trusted-cas.md).
* Note the names of the bucket, scope, and collection you want to stream to Capella Analytics.

## [](#link)Create a Link to a Couchbase Server Database

To create a remote link to a Couchbase Server database:

1. In the Capella UI, select the **Capella Analytics** tab.
2. Click a cluster name. The workbench opens.
3. Use the explorer to explore the existing databases, scopes, and collections. You can add a database and scope if necessary: see [Manage Capella Analytics Services Databases](manage-databases.md).
4. Select **Create** **Data Link**. The **Create Link for <cluster name> Cluster** dialog opens.
5. Select **Couchbase Server/Capella** then click **Continue**.
6. Under **Link Type**, Select **Couchbase Server**.
7. In the **Couchbase Link Name** field, enter a name for the link.
8. In the **Connection String** field, enter the hostname or IP address of one of the Couchbase Server nodes.
9. Supply the authentication details. You may need to scroll to enter all required values.
10. Select one of the encryption options. If you select either **Half** or **Full**, also paste Couchbase Server’s trusted root certificate in the **Remote Cluster Certificate** field.
11. Click **Save & Continue**. The link does not automatically connect to the remote source system. See [Connect or Disconnect a Remote Link](connect-link.md).

You can now create a collection associated with the link.

## [](#create-a-collection-for-data-streamed-from-couchbase-server)Create a Collection for Data Streamed from Couchbase Server

Once you have created a link, create a remote collection to receive the data from Couchbase Server:

1. In the **Create Link for <cluster name> Cluster** dialog, click **Create Linked Collection**  
> [!NOTE]  
> If you closed the **Create Link for <cluster name> Cluster** dialog by clicking **Complete Later**, then under **Links** move your pointer over the name of the link and choose **⋮ (More)** **Create Linked Collection**.
2. Select the Capella Analytics database and scope for the new collection and supply a name in the **Collection Name** field.
3. In the **Source** fields, enter the names of the Couchbase **Bucket**, **Scope**, and **Collection** you want to shadow.
4. Optionally, enter an expression in the **WHERE clause** field to filter the documents in the source collection. Do not include the `WHERE` keyword, and supply only a deterministic expression. For example, `activity = "eat"`.
5. Click **Create Collection**. Your collection appears in the explorer’s **Data** section underneath its database and scope.

You can choose to create additional linked collections by clicking **Create Another Collection**.

To create a remote collection using a `CREATE COLLECTION` statement, see [CREATE a Remote Collection](../sqlpp/5%5Fddl%5Fremote.md).

## [](#connect-the-link)Connect the Link

To have Capella Analytics start streaming data from Couchbase Server, you must connect the link by either:

* Clicking **Connect Link** in the **Create Link for <cluster name> Cluster** dialog.
* Under **Links**, move your pointer over the name of the link and choose **⋮ (More)** **Connect**.

## [](#see-also)See Also

* [Query and Explore with the Workbench](../query/workbench.md)
* [Connect or Disconnect a Remote Link](connect-link.md)
* [Access Data](../intro/examples.md)