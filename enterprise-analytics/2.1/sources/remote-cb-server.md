---
title: Stream Data from Couchbase Server
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sources/pages/remote-cb-server.adoc
  xref: xref:2.1@enterprise-analytics:sources:remote-cb-server.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/sources/remote-cb-server.html)

# Stream Data from Couchbase Server

> To continuously update an Enterprise Analytics collection with data hosted on Couchbase Server, create a remote link and collection. 

> [!TIP]
> For an example, see [Create Remote Collections for beer-sample](../intro/connecting-to-data-sources.md#create-remote-collections-for-beer-sample).

## [](#encryption)Requirements

Your Enterprise Analytics account must have the `**Enterprise Analytics Access**` role along with specific privileges to be able to create a link and its associated collection.

You need to take the following steps on your Couchbase Server cluster:

1. Configure your Couchbase Server cluster's network to allow access from Enterprise Analytics. The steps you must take depend on how and where you deployed your Couchbase Server cluster. For example, suppose you deployed a self-managed Couchbase Server in AWS. To allow Enterprise Analytics to connect, create a VPC peering connection between the VPCs for your Enterprise Analytics and the Couchbase Server cluster.
2. Create a user and password for Enterprise Analytics to use when connecting. Give this user read permissions for all buckets and scopes you want to stream. See [Manage Users, Groups, and Roles](../../../server/current/manage/manage-security/manage-users-and-roles.md).
3. Get the hostname or external IP address for 1 of the Couchbase Server nodes. You supply this value to Enterprise Analytics as the connection string.
4. Save a copy of the Couchbase Server's cluster certificate. You can get the certificate from 2 places:

  * Copy the certificate from the Couchbase Server Web Console's **Security** **Certificate** page under the **Trusted Root Certificate**.
  * Get the certificate by calling Couchbase Server's [/pools/default/trustedCAs REST API](../../../server/current/rest-api/get-trusted-cas.md).
5. Note the names of the bucket, scope, and collection you want to stream to Enterprise Analytics.

## [](#link)Create a Link to a Couchbase Server

1. In the UI, select the **Workbench** tab.
2. Select **\+ new link**.
3. In the **Link Name** field, enter a name for the link.
4. In the **Link Type** field, select **Couchbase**.
5. In the **Remote IP/Hostname** list, select the hostname or IP address of a node in the remote cluster you want to link. IPv6 addresses need to be enclosed in square brackets.
6. In the **Encryption Type** field, select 1 of the following options:

  * None (password is not secured)
  * Half (secure password with SCRAM-SHA)
  * Full (using credentials)
  * Full (using client certificate(s))
  * Full (using encrypted client certificate password)

| **Remote Username** | Enter the required username. |
| ------------------- | ---------------------------- |
| **Remote Password** | Enter the required password. |

| **Remote Username** | Enter the required username. |
| ------------------- | ---------------------------- |
| **Remote Password** | Enter the required password. |

| **Remote Username**               | Enter the required username.      |
| --------------------------------- | --------------------------------- |
| **Remote Password**               | Enter the required password.      |
| **Remote Cluster Certifcates(s)** | Paste a trusted root certificate. |

| **Remote Cluster Certificate(s)** | Paste a trusted root certificate.                                      |
| --------------------------------- | ---------------------------------------------------------------------- |
| **Client Certificate**            | Paste the certificate used to identify the user on the remote cluster. |
| **Client Key**                    | Paste the private key for the above client certificate.                |

| **Remote Cluster Certificate(s)** | Paste a trusted root certificate.                                      |
| --------------------------------- | ---------------------------------------------------------------------- |
| **Client Certificate**            | Paste the certificate used to identify the user on the remote cluster. |
| **Encrypted Client Key**          | Paste the encrypted private key for the above client certificate.      |
| **Passphrase Type**               | Select **Plain** or **REST**.                                          |
| **Password**                      | Select a password.                                                     |  
For more information, see [Load Root Certificates](../../../server/current/rest-api/load-trusted-cas.md).
7. Select **Prevents Redirects** to prevent HTTP connections for the remote link.
8. Click **Save**.

You can now create a collection associated with the link.

## [](#create-a-collection-for-data-streamed-from-couchbase-server)Create a Collection for Data Streamed from Couchbase Server

Once you have created a link, create a collection to receive the data from Couchbase Server:

1. In the UI, select the **Workbench** tab.
2. Next to the link you created in [Create a Link to a Couchbase Server](#link), click **\+ collection**.
3. In the **Collection Name** field, enter a name for the collection.
4. In the **Database** list, select the required database and in the **Scope** list, select the required scope or verify the supplied database and scope if you're adding it to a specific scope.
5. In the **Source bucket.scope.collection** field, select the source bucket, scope and collection.
6. In the **Where (optional)** field, you can add an optional WHERE clause to filter documents in the dataset. Make sure you do not include the WHERE keyword.
7. Click **Save**. Your collection appears under the scope in the explorer.

To create a remote collection using a `CREATE COLLECTION` statement, see [CREATE a Remote Collection](../sqlpp/5%5Fddl%5Fremote.md).

## [](#connect-the-link)Connect the Link

To have Enterprise Analytics start streaming data from the Couchbase Server:

1. In the explorer, locate the link you want to connect.
2. Click **Link**.

## [](#see-also)See Also

* [Query and Explore with the Workbench](../query/workbench.md)
* [Connect or Disconnect a Remote Link](connect-link.md)
* [Connecting to Data Sources](../intro/connecting-to-data-sources.md)