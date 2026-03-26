---
title: ALTER BUCKET
description: The ALTER BUCKET statement enables you to update an existing
  bucket's configuration.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/n1ql/pages/n1ql-language-reference/alterbucket.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:n1ql:n1ql-language-reference/alterbucket.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/n1ql/n1ql-language-reference/alterbucket.html)

# ALTER BUCKET

> The ALTER BUCKET statement enables you to update an existing bucket's configuration. 

## [](#purpose)Purpose

Use the ALTER BUCKET statement to modify the configuration of a bucket in your Couchbase cluster. You can update only a limited set of bucket settings. You cannot change its core properties such as the bucket name and type. For more information, see the [Syntax](#alterbucket-syntax) section.

## [](#rbac-privileges)RBAC Privileges

Only administrators with the following roles can execute the ALTER BUCKET statement:

* Full Admin
* Cluster Admin
* Bucket Admin (if privileges are extended to the specific bucket or all buckets on the cluster)

For more information about roles and privileges, see [Roles](../../learn/security/roles.md).

## [](#alterbucket-syntax)Syntax

```ebnf
alter-bucket ::= 'ALTER' ( 'BUCKET' | 'DATABASE' ) name ( 'WITH' with-fields )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/alter-bucket.png) 

The `BUCKET` and `DATABASE` keywords are synonyms. You can use either of them.

| name        | (Required) An [identifier](identifiers.md) that represents the name of the bucket that you want to update.                                                                                                                                                                      |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| with-fields | (Optional) A JSON object containing a list of name-value pairs that specify additional options for the bucket. For a list of valid fields names and values, see [Bucket Parameter Groups](../../rest-api/rest-bucket-create.md#parameter-groups) in the REST API documentation. |

> [!NOTE]
> You cannot alter the following fields of a bucket: `bucketType`, `storageBackend`, `replicaIndex`, and `conflictResolutionType`.

## [](#example)Example

Example 1\. Alter a bucket and update its memory quota, maximum TTL, and durability level

```sqlpp
ALTER BUCKET `student-records`
WITH {
    "ramQuota": 256,
    "maxTTL": 86400,
    "durabilityMinLevel": "majority"
};
```

## [](#related-links)Related Links

* For an overview of buckets, see [Buckets](../../learn/buckets-memory-and-storage/buckets.md).
* For step-by-step procedures for bucket management, see [Manage Buckets](../../manage/manage-buckets/bucket-management-overview.md).
* For managing buckets with the REST API, see [Buckets API](../../rest-api/rest-bucket-intro.md).