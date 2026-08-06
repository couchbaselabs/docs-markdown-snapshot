---
title: Cloud Read/Write Permissions
description: This page outlines the required read and write permissions when
  copying data to or from external cloud providers.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/reference/pages/cloud_read_write_permissions.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:2.1@enterprise-analytics:reference:cloud_read_write_permissions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/reference/cloud_read_write_permissions.html)

# Cloud Read/Write Permissions

> This page outlines the required read and write permissions when copying data to or from external cloud providers. 

Exclusive permissions are required when reading from cloud storage using External Collections or writing to cloud storage using COPY TO statements.

## [](#aws-simple-storage-service-s3)AWS Simple Storage Service (S3)

### [](#read-permissions)Read Permissions

Read permissions are needed when reading from cloud storage using External Collections. To grant the required permissions, follow these steps:

First, create a policy that has the desired permissions:

1. Go to the AWS Console.
2. From the **Dashboard**, select **IAM**.
3. Select **Policies**.
4. Select **Create Policy**.
5. In the **Policy Editor**, select **JSON**.
6. Paste the following policy:

  * `s3:ListBucket permission`
  * `s3:GetObject permission`  
  ```SQL++  
    {  
      "Version": "2012-10-17",  
      "Statement": [  
          {  
              "Effect": "Allow",  
              "Action": [  
                  "s3:GetObject"  
              ],  
              "Resource": "arn:aws:s3:::your-bucket-name/*"  
          },  
          {  
              "Effect": "Allow",  
              "Action": "s3:ListBucket",  
              "Resource": "arn:aws:s3:::your-bucket-name"  
          }  
      ]  
  }  
  ```
7. Give the policy a name and create the policy.
8. Attach the policy to the desired IAM User or Role.  
It grants the selected permissions to the selected resources in the policy.

### [](#read-and-write-permissions)Read and Write Permissions

Read and write permissions are needed when writing to cloud storage using COPY TO statements.

1. Go to the AWS Console.
2. From the **Dashboard**, select **IAM**.
3. Select **Policies**.
4. Select **Create Policy**.
5. In the **Policy Editor**, select **JSON**.
6. Paste the following policy:

  * `s3:ListBucket permission`
  * `s3:GetObject permission`
  * `s3:PutObject permission`
  * `s3:DeleteObject permission`  
```SQL++  
  {  
    "Version": "2012-10-17",  
    "Statement": [  
        {  
            "Effect": "Allow",  
            "Action": [  
                "s3:GetObject",  
                "s3:PutObject",  
                "s3:DeleteObject"  
            ],  
            "Resource": "arn:aws:s3:::your-bucket-name/*"  
        },  
        {  
            "Effect": "Allow",  
            "Action": "s3:ListBucket",  
            "Resource": "arn:aws:s3:::your-bucket-name"  
        }  
    ]  
}  
```

You have granted all necessary permissions.

## [](#microsoft-azure-blob-storage)Microsoft Azure Blob Storage

To grant the required permissions for using the resources in Azure Blob Storage, select the desired role:

* `Storage Blob Data Reader` grants read-only permissions. This allows for only reading blobs. For more information, see [Storage Blob Data Reader role](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/storage#storage-blob-data-reader).
* `Storage Blob Data Contributor` grants read/write permissions. This allows reading, writing, or deleting blobs. For more information, see [Storage Blob Data Contributor role](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/storage#storage-blob-data-contributor).

For more information about assigning permissions, see the [Microsoft Azure documentation](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal).