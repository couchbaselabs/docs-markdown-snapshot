---
title: Set Up Amazon S3 External Source
description: To provide query access to OLAP data in an Amazon S3 bucket, you
  create an external link and associate it with an external collection.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sources/pages/setup-aws-s3-external-source.adoc
pubDate: 2026-03-27T05:16:21.194Z
link: xref:analytics:sources:setup-aws-s3-external-source.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/sources/setup-aws-s3-external-source.html)

# Set Up Amazon S3 External Source

> To provide query access to OLAP data in an Amazon S3 bucket, you create an external link and associate it with an external collection. 

## [](#prerequisites)Prerequisites

Your Capella Analytics account must have either the [Project Owner](../admin/auth/auth-ui.md#project-owner-role) or [Project Manager](../admin/auth/auth-ui.md#project-cluster-manager-role) role to be able to create a link for the external data.

* If you want to access private data from an S3 bucket, you need credentials that can list and read data from that bucket. For more information, see [Credentials](external-s3.md#credentials).
* You have the path to the data you want to access from your S3 bucket. For more information, see [Location Path](external-s3.md#prefix).

## [](#create)Create a Link for Amazon S3

To create a link to an Amazon S3 bucket:

1. In the Capella UI, select the **Capella Analytics** tab.
2. Click a cluster name.
3. Use the explorer to explore the existing databases, scopes, and collections. You can add a database and scope if necessary: see [Create a Database](database-objects.md#database).
4. Select **Create** **Data Link**.
5. Select **Amazon S3** then click **Continue**.
6. In the **Link Name** field, enter a name for the link.
7. From **Region**, select the region where your Amazon S3 data is stored.
8. If accessing an S3-compatible object store provider, in the **Endpoint** field enter the URL for that provider.
9. From **Authentication Method**, select one of the following options:

  * Credential Login
  * Anonymous login
  * Trust Account Authentication

  * If the S3 bucket is private, add your credentials to the **Access Key** and **Secret Access** key fields.
  * If you have temporary access to the bucket, in the **Session Token** field enter an Amazon S3 session token.  
Select this option to access a public S3 bucket that does not require credentials. Capella uses the region you selected in the previous step to access the bucket.  
Select this option to use role-based authentication to access a private S3 bucket.

**Create Trusted Role in AWS**

  1. Navigate to the AWS IAM console and go to **Access Management** **Roles** **Create Role**.
  2. In the **Select trusted entity** step, choose **Custom Trust Policy** as the trusted entity type. This allows you to define which external accounts and users can assume this role, providing fine-grained security control.
  3. Copy the provided `Trust Policy JSON` from the Analytics UI and paste it into the trust policy editor in the AWS console. This JSON policy specifically authorizes Capella Analytics to assume the role using the external ID for additional security verification. A sample trust policy is provided in the collapsible section below.

**Sample Trust Policy JSON**  
  ```json  
  {  
    "Version": "2012-10-17",  
    "Statement": [  
      {  
        "Sid": "Sid0",  
        "Effect": "Allow",  
        "Action": [  
          "sts:AssumeRole"  
        ],  
        "Principal": {  
          "AWS": "arn:aws:iam::264138468394:role/14c63b0b-1022-46a8-a4fe-b5ac9e1db5bf_couchbase"  
        },  
        "Condition": {  
          "StringEquals": {  
            "sts:ExternalId": "<external-id>"  
          }  
        }  
      }  
    ]  
  }  
  ```  
  > [!NOTE]  
  > Use your own `external-id` or replace this placeholder with the auto-generated `external-id` provided by Analytics after link creation. The external ID prevents the [confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) by adding an additional security layer to cross-account role assumptions.

**Configure Role Permissions**

  1. Navigate to the AWS IAM console and go to **Access Management** **Policies** **Create Policy**.
  2. In the Policy Editor interface, select the **JSON** tab. This allows you to paste the pre-defined policy JSON directly.
  3. Copy the following complete `Sample S3 Read Access Policy` JSON from the collapsible section and paste it into the AWS console JSON editor. This policy grants the minimum required permissions for Capella Analytics to read data from your S3 bucket.

**Sample S3 Read Access Policy**  
  ```json  
  {  
    "Version": "2012-10-17",  
    "Statement": [  
      {  
        "Sid": "Sid0",  
        "Effect": "Allow",  
        "Action": [  
          "s3:ListBucket"  
        ],  
        "Resource": [  
          "arn:aws:s3:::<bucket-name>"  
        ]  
      },  
      {  
        "Sid": "Sid1",  
        "Effect": "Allow",  
        "Action": [  
          "s3:GetObject"  
        ],  
        "Resource": [  
          "arn:aws:s3:::<bucket-name>/*"  
        ]  
      }  
    ]  
  }  
  ```  
  > [!NOTE]  
  > Replace `<bucket-name>` with the name of your S3 bucket. For more information about read and write permissions, see [Cloud Read/Write Permissions for AWS](required-permissions-aws.md).

**Authentication Details**

  1. In the **Assumed Role ARN** field, enter the Amazon Resource Name (ARN) of the role you created in your AWS account.
  2. (Optional) In the **External ID** field, enter the external ID you specified when creating the trusting role in your AWS account.
10. Click **Save & Continue**.

Capella Analytics creates the link to the S3 data source.

## [](#create-a-collection-for-s3-data)Create a Collection for S3 Data

You must create a collection for the data before you can query it in Capella Analytics. After you create the link to an S3 bucket, Capella Analytics prompts you to create a collection for your data. You can create the collection by clicking **Create Linked Collection**. If you want to create the collection later, click **Complete Later**. When you're ready to create the collection, hover over the link name's under **Links** and select **More Options (⋮)** **Create Linked Collection**.

To complete creating the collection:

1. On the **Create Collection Linked to <S3 link name>** dialog, select the database and scope and enter a name for the collection.
2. In the **S3 Bucket** field, enter the name of an Amazon S3 bucket. Enter only the name of the bucket, not a URL.
3. In the **S3 Path** field, enter one or more prefixes separated by slashes `/` to identify the location of the files you want to query. Do not include filenames in the path. To query files located at the top-most or bucket level, leave the path blank. See [Design a Location Path](dynamic-prefixes.md).
4. Choose the **File Format** of the files at that destination. Depending on the format you select, you may see additional fields:

  * CSV and TSV
  * Parquet

  * Define the data types for the fields in the files as a comma-separated list of `<field-name> <datatype>` values. The `<datatype>` is one of the [primitive data types](../../server/current/analytics/10%5Fdata%5Ftype.md). If the field's value does not match the data type, Capella Analytics ignores the record. You can also specify `NOT UNKNOWN` flag after the data type to have Capella Analytics ignore the record if the value is `missing` or `null`. For example:  
  id BIGINT NOT UNKNOWN, firstname STRING, lastname STRING
  * Clear **File includes header row** if the first line of your CSV file is not a list of the columns in the file.
  * If your data uses a value other than an empty string (`""`) to indicate a null value, select **Use custom string as Null** and enter the value.  
Choose whether Capella Analytics should parse embedded JSON data and convert decimal values to doubles.
5. (Optional) Use either the **Include** or **Exclude** field to specify files to include in, or exclude from, queries. You can use the following wildcards:

  * `*` matches any character or characters.
  * `?` matches any single character.
  * `[ sequence ]` matches any characters in the supplied sequence.
  * `[! sequence ]` matches any characters not in the supplied sequence.  
  For example, if the bucket stores both JSON and Parquet files, you can enter `*.JSON` in the **Include** field to query only the files that are in JSON format.
6. Click **Create Collection**. Your link and collection appear under the scope in the explorer.

The link is now available to provide your credentials whenever you query data in the external data source.

> [!NOTE]
> Because the data in an external collection is not ingested into Capella Analytics and remains on the external host, Capella Analytics cannot index it.

## [](#see-also)See Also

* [Query and Explore with the Workbench](../query/workbench.md)
* [Access and Organize Data in Capella Analytics Services](database-objects.md)
* [Access Data](../intro/examples.md)