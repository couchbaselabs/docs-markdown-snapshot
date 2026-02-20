---
title: Analytics Links
description: In the Analytics Workbench, you can create and manage external links.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/analytics-service/analytics-links.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:clusters:analytics-service/analytics-links.adoc[]
---

[View original HTML](/cloud/clusters/analytics-service/analytics-links.html)

# Analytics Links

> In the Analytics Workbench, you can create and manage external links. These enable you to access data from outside the local Couchbase cluster. 

An external link is a link to an external data source, such as Amazon S3, Google Cloud Storage, or Azure Blob. Each link exists within an Analytics scope.

## [](#prerequisites)Prerequisites

To use all of the functionality in the Analytics Workbench, you must have the [Project Owner](../../projects/project-roles.md#project-owner-role) or [Cluster Data / Reader](../../projects/project-roles.md#project-cluster-data-reader-writer) project role.

## [](#view-links)View Links

The Analytics Scopes area shows all Analytics scopes, and any links that exist within each scope. This includes information about the type of link, their connection status, and a Trash button () that allows you to drop each remote link.

![The links in the Analytics Scopes area.](../_images/analytics-scopes-working-area.png) 

> [!NOTE]
> It is not possible to modify an existing link. If you want to modify an existing link, you must delete it and recreate it.

## [](#s3)Create an Amazon S3 Link

To create an S3 link:

1. Click the **Add Remote Link** button (+) next to the Analytics scope where you want to create the link.  
The **Add Link** flyout is shown.
2. Click the **S3** option.
3. In the **Name** field, enter a name for the link.
4. In the **Access Key ID** field, enter the access AWS key ID you are using to access Amazon S3.
5. In the **Secret Access Key** field, enter the secret access key you are using to access Amazon S3.
6. Using the **Region** drop-down menu, choose the AWS region where your S3 bucket resides.
7. (Optional) In the **Service Endpoint** field, enter a service endpoint to connect to rather than the default S3 endpoint.
8. Click **Create** to create the link.  
The new link is displayed within the Analytics Scopes area.

If you close the Add Link flyout without creating the link, any information you have entered in the Add Link flyout is not preserved.

> [!CAUTION]
> When creating a link to the Amazon S3 service, be sure to follow best practices for security. AWS root account credentials should never be used. The policy for the created IAM User roles should be as strict as possible and only allow access to the required data and required resources. You only need to know the access key ID and the secret access key for the created IAM User role to access the S3 service. The link will be able to access whatever is permitted to the IAM User, since it will be using the IAM User credentials to interact with the AWS S3 service.

## [](#gcs)Create a Google Cloud Storage Link

To create a Google Cloud Storage link:

1. Click the **Add Remote Link** button (+) next to the Analytics scope where you want to create the link.  
The **Add Link** flyout is shown.
2. Click the **Google Cloud Storage** option.
3. In the **Name** field, enter a name for the link.
4. (Optional) In the **Service Endpoint** field, enter a service endpoint to connect to rather than the default Google Cloud Storage endpoint.
5. In the **Authentication Method** field, select the type of authentication:

  * **Anonymous** (No credentials / authentication)
  * **JSON Credentials**
6. If you specified **JSON Credentials** authorization, enter the JSON credentials in the box provided.
7. Click **Create** to create the link.  
The new link is displayed within the Analytics Scopes area.

If you close the Add Link flyout without creating the link, any information you have entered in the Add Link flyout is not preserved.

## [](#azure-blob)Create an Azure Blob Link

To create an Azure Blob link:

1. Click the **Add Remote Link** button (+) next to the Analytics scope where you want to create the link.  
The **Add Link** flyout is shown.
2. Click the **Azure Blob** option.
3. In the **Name** field, enter a name for the link.
4. (Optional) In the **Service Endpoint** field, enter a service endpoint to connect to rather than the default Google Cloud Storage endpoint.
5. In the **Authentication Method** field, select the type of authentication, then enter any required information in the provided fields.

  * **Anonymous** (No credentials / authentication)
  * **Shared Key**

    1. In the **Account Name** box, enter the account name.
    2. In the **Account Key** box, enter the account key.
  * **Shared Access Signature**

    1. In the **Shared Access Signature** box, enter a token that can be used for authentication.
  * **Client Secret**

    1. In the **Client ID** box, enter the client ID for the registered application.
    2. In the **Client Secret** box, enter the client secret for the registered application.
    3. In the **Tenant ID** box, enter the tenant ID where the registered application is created.
  * **Client Certificate**

    1. In the **Client ID** box, enter the client ID for the registered application.
    2. In the **Client Certificate** box, enter the client certificate for the registered application.
    3. In the **Tenant ID** box, enter the tenant ID where the registered application is created.
    4. If the client certificate is password-protected:

      1. Check the **Certificate Password** box.
      2. In the **Client Certificate Password** box, enter the client certificate password for the registered application.
6. Click **Create** to create the link.  
The new link is displayed within the Analytics Scopes area.

If you close the Add Link flyout without creating the link, any information you have entered in the Add Link flyout is not preserved.

## [](#delete-a-link)Delete a Link

To delete a link:

1. In the list of existing links, click on the Trash icon () next to the link entry.  
A flyout appears, asking if you are sure that you want to delete the link.
2. In the provided field, type the name of the link you’re deleting and click **Drop**.