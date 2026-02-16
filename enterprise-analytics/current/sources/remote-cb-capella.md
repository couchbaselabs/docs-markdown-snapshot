[View original HTML](/enterprise-analytics/current/sources/remote-cb-capella.html)

> To continuously update Enterprise Analytics with data hosted on a Couchbase Capella operational cluster, create a link and collection. 

|  | For an example, see [Create Remote beer-sample Collections](../intro/connecting-to-data-sources.md#create-remote-collections-for-beer-sample). |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#encryption)Requirements for Couchbase Capella Links

You need to take the following steps on your Couchbase Capella operational cluster:

* To allow Enterprise Analytics to connect to a Couchbase Capella operational cluster, you must add the IP address of the Enterprise Analytics server to the Capella cluster’s "Allowed IP" list. For more information, see [Add an Allowed IP Address](../../../cloud/clusters/allow-ip-address.md).
* Get the hostname or external IP address for 1 of the Couchbase Capella cluster nodes. You supply this value to Enterprise Analytics as the hostname/IP address.
* Create a user and password for Enterprise Analytics to use when connecting. Give this user read/write permissions for all buckets and scopes you want to stream. For more information, see [Create Cluster Access Credentials](../../../cloud/clusters/manage-database-users.md#create-database-credentials).
* Save a copy of the Couchbase Capella cluster root certificate. You can find the certificate on the Capella UI at the **Security Certificate** page under **Settings**.
* Note the names of the bucket, scope, and collection you want to stream to Enterprise Analytics.

## [](#link)Create a Link to Couchbase Capella

1. In the UI, select the **Workbench** tab.
2. . Select **\+ new link**.
3. In the **Link Name** field, enter a name for the link.
4. In the **Link Type** field, select **Couchbase**.
5. In the **Remote IP/Hostname** list, select the hostname or IP address of a node in the remote cluster you want to link. IPv6 addresses need to be enclosed in square brackets.
6. In the **Encryption Type** field, select **Full**:  
Full (using credentials)

| **Remote Username**               | Enter the required username.      |
| --------------------------------- | --------------------------------- |
| **Remote Password**               | Enter the required password.      |
| **Remote Cluster Certifcates(s)** | Paste a trusted root certificate. |  
For more information, see [Use Your Capella Root Certificate](../../../cloud/security/security-certificates.md#use-your-capella-root-certificate) and [Create Cluster Access Credentials](../../../cloud/clusters/manage-database-users.md#create-database-credentials).
7. Select **Prevents Redirects** to prevent HTTP connections for the remote link.
8. Click **Save**.

## [](#create-a-collection)Create a Collection

1. In the UI, select the **Workbench** tab.
2. Next to the link you created in [Create a Link to Couchbase Capella](#link), click **\+ collection**.
3. In the **Collection Name** field, enter a name for the collection.
4. In the **Database** list, select the required database and in the **Scope** list, select the required scope or verify the supplied database and scope if you’re adding it to a specific scope.
5. In the **Source bucket.scope.collection** field, select the source bucket, scope and collection.
6. In the **Where (optional)** field, you can add an optional WHERE clause to filter documents in the dataset. Make sure you do not include the WHERE keyword.
7. Click **Save**.

To create a remote collection using a `CREATE COLLECTION` statement, see [CREATE a Remote Collection](../sqlpp/5%5Fddl%5Fremote.md).

## [](#connect-the-link)Connect the Link

To start streaming data from your Couchbase Capella operational cluster to Enterprise Analytics, use the explorer and locate the link you want to connect. Click the link icon.

## [](#see-also)See Also

* [Query and Explore with the Workbench](../query/workbench.md)
* [Connect or Disconnect a Remote Link](connect-link.md)
* xref: intro:connecting-to-data-sources.adoc\[\]