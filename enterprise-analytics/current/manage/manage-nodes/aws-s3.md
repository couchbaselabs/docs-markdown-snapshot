---
title: Configuring AWS S3 Storage
description: You can set up Couchbase Enterprise Analytics to use Amazon S3 as
  its storage solution.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/manage/pages/manage-nodes/aws-s3.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:enterprise-analytics:manage:manage-nodes/aws-s3.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/manage/manage-nodes/aws-s3.html)

# Configuring AWS S3 Storage

> You can set up Couchbase Enterprise Analytics to use Amazon S3 as its storage solution. Your Enterprise Analytics cluster can then read and store data from an Amazon S3 bucket. Each node in an Enterprise Analytics cluster must have access to the configured bucket either using an AWS access policy or credentials file. 

## [](#configure-s3-access-credentials)Configure S3 Access Credentials

To enable Enterprise Analytics nodes to access your S3 bucket, you need to set up proper authentication credentials. For each node on your cluster:

1. Place the credentials file in the `.aws` directory in the Couchbase user's home directory. For example, `/home/couchbase/.aws/credentials` & `chmod’d` to `600` as a security best practice.
2. Make sure to enter the credentials under the default profile. For more information about how to set configuration and credential files in the AWS CLI, see the [AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).
3. Use the AWS CLI to confirm that each node was properly configured:  
```console  
aws s3 ls s3://bucket/prefix/  
```

If your credentials have not been correctly configured, the CLI returns:

```none
$ aws s3 ls s3://bucket/prefix/
Unable to locate credentials.
You can configure credentials by running "aws configure".
```

If the credentials are incorrect:

```none
$ aws s3 ls s3://bucket/prefix/

An error occurred (InvalidAccessKeyId) when calling the ListObjectsV2 operation. The AWS Access Key Id you provided does not exist in our records.
```

If you correctly configured your credentials, you should see:

```none
$ aws s3 ls s3://bucket/prefix/
                           PRE subdir/
```

## [](#next-steps)Next Steps

* [Initialize a Node](initialize-node.md)