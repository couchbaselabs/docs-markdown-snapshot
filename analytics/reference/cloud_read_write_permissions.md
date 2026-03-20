---
title: Cloud Read/Write Permissions
description: This page outlines the required read and write permissions when
  copying data to or from external cloud providers.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/reference/pages/cloud_read_write_permissions.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:analytics:reference:cloud_read_write_permissions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/reference/cloud_read_write_permissions.html)

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

## [](#google-cloud-storage)Google Cloud Storage

### [](#read-permissions-2)Read Permissions

Read permissions are needed when reading from cloud storage using External Collections.

To grant the required permissions, follow these steps:

First, create a role that has the desired permissions:

1. Go to the Google Cloud console.
2. From the **Dashboard**, go to **IAM and Admin** and select **Roles**.
3. Select **Create Role**.
4. Fill in the information (Title, Description, … etc).
5. Select **Add Permissions**.
6. Select the following permissions:

  * `storage.objects.get`
  * `storage.objects.list`
7. Select **Add**.
8. Select **Create**.

Next, add the Service Account to the bucket and assign it the created role above:

1. Go to the Google Cloud console.
2. From the **Dashboard**, go to **Cloud Storage** and select **Buckets**.
3. Select the desired bucket.
4. From the **Bucket** page, select the **Permissions** tab.
5. Under **View by Principals**, select **Grant Access**.
6. Under **Add Principal**, add the desired **Service Account**.
7. Under **Assign Roles**, select the **Role** created in the previous steps.

### [](#read-and-write-permissions-2)Read and Write Permissions

Read and write permissions are needed when writing to cloud storage using COPY TO statements.

1. Go to the Google Cloud console.
2. From the **Dashboard**, go to **IAM and Admin** and select **Roles**.
3. Select **Create Role**.
4. Fill in the information (Title, Description, … etc).
5. Select **Add Permissions**.
6. Select the following permissions:

  * `storage.objects.get`
  * `storage.objects.list`
  * `storage.objects.create`
  * `storage.objects.delete`
7. Select **Add**.
8. Select **Create**.

Next, add the Service Account to the bucket and assign it the created role above:

1. Go to the Google Cloud console.
2. From the **Dashboard**, go to **Cloud Storage** and select **Buckets**.
3. Select the desired bucket.
4. From the **Bucket** page, select the **Permissions** tab.
5. Under **View by Principals**, select **Grant Access**.
6. Under **Add Principal**, add the desired **Service Account**.
7. Under **Assign Roles**, select the **Role** created in the previous steps.

You have granted all necessary permissions.