---
title: Cloud Read/Write Permissions for AWS
description: This page outlines the required read and write permissions when
  copying data to or from external cloud providers.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sources/pages/required-permissions-aws.adoc
  xref: xref:analytics:sources:required-permissions-aws.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/sources/required-permissions-aws.html)

# Cloud Read/Write Permissions for AWS

> This page outlines the required read and write permissions when copying data to or from external cloud providers. 

Exclusive permissions are required when reading from cloud storage using External Collections or writing to cloud storage using COPY TO statements.

## [](#prerequisites)Prerequisites

Before granting permissions, ensure you have the following:

* An AWS account with the necessary administrative privileges.
* Access to the AWS Management Console.
* The name of the S3 bucket you want to access.

## [](#read-permissions)Read Permissions

You need Read permissions when reading from cloud storage using External Collections.

To create a policy and grant read permissions to your AWS S3 cloud storage:

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

## [](#read-and-write-permissions)Read and Write Permissions

Read and write permissions are needed when writing to cloud storage using COPY TO statements.

To create a policy and grant read and write permissions to your AWS S3 cloud storage:

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

## [](#see-also)See Also

* [Query and Explore with the Workbench](../query/workbench.md)
* [Access and Organize Data in Capella Analytics Services](database-objects.md)
* [Set Up Amazon S3 External Source](setup-aws-s3-external-source.md)