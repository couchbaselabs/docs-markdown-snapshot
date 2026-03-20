---
title: Managing Links
description: Managing Remote Links and External Links with the Analytics Workbench.
editUrl: https://github.com/couchbase/docs-analytics/edit/release/7.2/modules/analytics/pages/manage-links.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:analytics:manage-links.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/analytics/manage-links.html)

# Managing Links

The Analytics Workbench enables you to create or edit remote links and external links. Refer to [Remote Links and External Links](5%5Fddl.md#Remote%5Fexternal%5Flinks) for further details on remote links and external links.

Local links, remote links, and external links are displayed in the insights sidebar of the Analytics Workbench. Each link is listed below the heading for the Analytics scope which contains it.

![The insights sidebar with links displayed](_images/workbench-insights-links.png) 

In the insights sidebar, links are labeled as follows:

* Local links — `cb local`
* External links to Microsoft Azure Blob storage — `AZUREBLOB`
* External links to Google Cloud Storage — `GCS`
* External links to the Amazon S3 service — `S3`
* Remote links — `cb remote`

## [](#creating-a-remote-link)Creating a Remote Link

To create a link to a remote Couchbase cluster:

1. In the insights sidebar, click **\+ remote link** next to the Analytics scope where you want to create the link.  
The **Add Link to _Scope_** dialog is displayed, where **_Scope_** is the name of the scope.
2. In the **Link Name** box, enter a name for the link.
3. Open the **Link Type** drop-down list and select **Couchbase**.  
The **Couchbase** link options are displayed.  
![The Add Link dialog with remote link options displayed](_images/link-add-remote.png)
4. In the **Remote IP / Hostname** box, enter the hostname or IP address of the remote Couchbase cluster, including the port number — by default, `8091`.
5. Open the **Encryption Type** drop-down list and select the type of encryption:

  * **None (password is not secured)**
  * **Half (secure password with SCRAM-SHA)**
  * **Full (using credentials)**
  * **Full (using client certificate)**
  * **Full (using encrypted client certificate)**
6. Depending on the type of encryption you specified, enter the required authentication details:

  * If you specified no encryption, or half encryption:

    1. In the **Remote Username** box, enter the remote username.
    2. In the **Remote Password** box, enter the remote password.
  * If you specified full encryption using credentials:

    1. In the **Remote Username** box, enter the remote username.
    2. In the **Remote Password** box, enter the remote password.
    3. In the **Remote Cluster Certificate(s)** box, enter the content of the target cluster root certificate. (To enter further target cluster certificates, click the **+** button.)
  * If you specified full encryption using a client certificate:

    1. In the **Remote Cluster Certificate(s)** box, enter the content of the target cluster root certificate. (To enter further target cluster certificates, click the **+** button.)
    2. In the **Client Certificate** box, enter the content of the client certificate.
    3. In the **Client Key** box, enter the content of the client key.
  * If you specified full encryption using an encrypted client certificate:

    1. In the **Remote Cluster Certificate(s)** box, enter the content of the target cluster root certificate. (To enter further target cluster certificates, click the **+** button.)
    2. In the **Client Certificate** box, enter the content of the client certificate.
    3. In the **Encrypted Client Key** box, enter the content of the encrypted client key.
    4. Select the **Passphrase Type**: **Plain** or **REST**.

      * For a plain passphrase, enter the **Password**.
      * For a REST passphrase:

        1. Enter the **URL** and the **Timeout** value.
        2. To specify a HTTP header, enter the **Name** and **Value**. (To enter further HTTP headers, click the **+** button.)
7. Choose **Save** to create the link, or **Cancel** to cancel.

When creating or altering a remote link using an alternate address, note the following:

* At least one node in the remote cluster must expose the `mgmt` port (`rest_port`, default 8091) or the `mgmtSSL` port (`ssl_rest_port`, default 18091).
* Furthermore, _all_ data nodes in the remote cluster must expose the `kv` port (`memcached_port`, default 11210) or the `kvSSL` port (`memcached_ssl_port`, default 11207).

Failure to do so will result in an error.

> [!NOTE]
> The SSL ports are required when the encryption mode is set to **Full**; the non-SSL ports are required otherwise.

You can also create a remote link using the command-line interface or the REST API. Refer to [couchbase-cli analytics-link-setup](../cli/cbcli/couchbase-cli-analytics-link-setup.md) or [Analytics Links REST API](rest-links.md).

## [](#s3)Creating an External Link to Amazon S3

To create an external link to the Amazon S3 service:

1. In the insights sidebar, click **\+ remote link** next to the Analytics scope where you want to create the link.  
The **Add Link to _Scope_** dialog is displayed, where **_Scope_** is the name of the scope.
2. In the **Link Name** box, enter a name for the link.
3. Open the **Link Type** drop-down list and select **S3**.  
The **S3** link options are displayed.  
![The Add Link dialog with S3 external link options displayed](_images/link-add-s3.png)
4. In the **Access Key ID** box, enter the Amazon S3 access key ID.
5. In the **Secret Access Key** box, enter the Amazon S3 secret access key.
6. If want the link to have temporary access, in the **Session Token** box, enter the Amazon S3 session token.  
(Specifying this parameter indicates that the access key ID and secret access key are temporary credentials. The Amazon S3 service validates the session token with each request to check whether the provided credentials have expired or are still valid.)
7. Open the **Region** drop-down list and select the Amazon S3 region.
8. If necessary, in the **Endpoint** box, enter the Amazon S3 service endpoint.
9. Choose **Save** to create the link, or **Cancel** to cancel.

> [!CAUTION]
> When creating an external link, be sure to follow best practices for security. Root account credentials should never be used. It is recommended to grant the minimum possible permissions to perform the required operations, and only to allow access to the required data and resources.

You can also create an external link to the Amazon S3 service using the command-line interface or the REST API. Refer to [couchbase-cli analytics-link-setup](../cli/cbcli/couchbase-cli-analytics-link-setup.md) or [Analytics Links REST API](rest-links.md).

## [](#azure-blob)Creating an External Link to Microsoft Azure Blob

To create an external link to Microsoft Azure Blob storage:

1. In the insights sidebar, click **\+ remote link** next to the Analytics scope where you want to create the link.  
The **Add Link to _Scope_** dialog is displayed, where **_Scope_** is the name of the scope.
2. In the **Link Name** box, enter a name for the link.
3. Under **Link Type**, select **Azure Blob**.  
The **Azure Blob** link options are displayed.  
![The Add Link dialog with Azure Blob link options displayed](_images/link-add-azure.png)
4. In the **Endpoint** box, enter the Azure Blob endpoint.
5. Open the **Authentication Method** drop-down list and select the type of authentication:

  * **Anonymous (No credentials / authentication)**
  * **Shared Key**
  * **Shared Access Signature**
  * **Managed Identity ID**
  * **Client Secret**
  * **Client Certificate**
6. If necessary, depending on the type of authentication you specified, enter the required details:

  * If you specified shared key authentication:

    1. In the **Account Name** box, enter the account name.
    2. In the **Account Key** box, enter the account key.
  * If you specified shared access signature:  
  In the **Shared Access Signature** box, enter a token that can be used for authentication.
  * If you specified managed identity authentication:  
  In the **Managed Identity ID** box, enter the managed identity ID.  
  (This method of authentication is only available if the application is running on an Azure instance, such as an Azure virtual machine.)
  * If you specified client secret authentication for Azure Active Directory:

    1. In the **Client ID** box, enter the client ID for the registered application.
    2. In the **Client Secret** box, enter the client secret for the registered application.
    3. In the **Tenant ID** box, enter the tenant ID where the registered application is created.
  * If you specified client certificate authentication for Azure Active Directory:

    1. In the **Client ID** box, enter the client ID for the registered application.
    2. In the **Client Certificate** box, enter the client certificate for the registered application.
    3. In the **Tenant ID** box, enter the tenant ID where the registered application is created.
    4. If the client certificate is password-protected:

      1. Check the **Certificate Password** box.
      2. In the **Client Certificate Password** box, enter the client certificate password for the registered application.
7. Choose **Save** to create the link, or **Cancel** to cancel.

> [!CAUTION]
> When creating an external link, be sure to follow best practices for security. Root account credentials should never be used. It is recommended to grant the minimum possible permissions to perform the required operations, and only to allow access to the required data and resources.

You can also create an external link to Microsoft Azure Blob storage using the command-line interface or the REST API. Refer to [couchbase-cli analytics-link-setup](../cli/cbcli/couchbase-cli-analytics-link-setup.md) or [Analytics Links REST API](rest-links.md).

## [](#gcs)Creating an External Link to Google Cloud Storage

To create an external link to Google Cloud Storage:

1. In the insights sidebar, click **\+ remote link** next to the Analytics scope where you want to create the link.  
The **Add Link to _Scope_** dialog is displayed, where **_Scope_** is the name of the scope.
2. In the **Link Name** box, enter a name for the link.
3. Under **Link Type**, select **Google Cloud Storage**.  
The **Google Cloud Storage** link options are displayed.  
![The Add Link dialog with Google Cloud Storage link options displayed](_images/link-add-gcs.png)
4. Open the **Authentication Method** drop-down list and select the type of authentication:

  * **Anonymous (No credentials / authentication)**
  * **Application Default Credentials**
  * **JSON Credentials**
5. If you specified JSON Credentials authorization, in the **JSON Credentials** box, enter the JSON credentials.
6. Choose **Save** to create the link, or **Cancel** to cancel.

> [!CAUTION]
> When creating an external link, be sure to follow best practices for security. Root account credentials should never be used. It is recommended to grant the minimum possible permissions to perform the required operations, and only to allow access to the required data and resources.

You can also create an external link to Google Cloud Storage using the command-line interface or the REST API. Refer to [couchbase-cli analytics-link-setup](../cli/cbcli/couchbase-cli-analytics-link-setup.md) or [Analytics Links REST API](rest-links.md).

## [](#editing-a-link)Editing a Link

You can edit a remote link or an external link. You cannot edit a local link.

To edit a remote link or an external link:

1. Under the heading for the required Analytics scope, click the name of the link.  
The **Edit Link** dialog is displayed. This contains the same options as the **Add Link To _Scope_** dialog.
2. Edit the details of the link as required. Note that you cannot change the name of the link or the link type. For details of the options, refer to the relevant section on this page:

  * [Creating a Remote Link](#creating-a-remote-link)
  * [Creating an External Link to Amazon S3](#s3)
  * [Creating an External Link to Microsoft Azure Blob](#azure-blob)
  * [Creating an External Link to Google Cloud Storage](#gcs)
3. Choose **Save** to update the link, or **Close Dialog** to cancel.

You can also edit a remote link or external link using the command-line interface or the REST API. Refer to [couchbase-cli analytics-link-setup](../cli/cbcli/couchbase-cli-analytics-link-setup.md) or [Analytics Links REST API](rest-links.md).

## [](#deleting-a-link)Deleting a Link

You can delete a remote link or an external link. You cannot delete a local link.

To delete a remote link or an external link:

1. Under the heading for the required Analytics scope, click the name of the link.  
The **Edit Link** dialog is displayed.
2. Choose **Drop Link**.  
The **Confirm Drop Link** dialog is displayed.
3. Choose **Continue** to delete the link, or **Cancel** to cancel.

You can also delete a remote link or external link using the command-line interface or the REST API. Refer to [couchbase-cli analytics-link-setup](../cli/cbcli/couchbase-cli-analytics-link-setup.md) or [Analytics Links REST API](rest-links.md).