---
title: DROP BUCKET
description: The DROP BUCKET statement enables you to delete a bucket.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/n1ql/pages/n1ql-language-reference/dropbucket.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:n1ql:n1ql-language-reference/dropbucket.adoc[]
---

[View original HTML](/server/current/n1ql/n1ql-language-reference/dropbucket.html)

# DROP BUCKET

> The DROP BUCKET statement enables you to delete a bucket. 

## [](#purpose)Purpose

Use the DROP BUCKET statement to permanently delete an existing bucket from your Couchbase cluster. Dropping a bucket deletes all data in the bucket, including documents, scopes, and collections. It also deletes all associated indexes, metadata, and other bucket resources.

> [!WARNING]
> This operation is irreversible, so use this statement with caution.

## [](#rbac-privileges)RBAC Privileges

Only administrators with the following roles can execute the DROP BUCKET statement:

* Full Admin
* Cluster Admin
* Bucket Admin (if privileges are extended to the specific bucket or all buckets on the cluster)

For more information about roles and privileges, see [Roles](../../learn/security/roles.md).

## [](#syntax)Syntax

```ebnf
drop-bucket ::= 'DROP' ( 'BUCKET' | 'DATABASE' ) ('IF' 'EXISTS' )? name
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/drop-bucket.png) 

The `BUCKET` and `DATABASE` keywords are synonyms. You can use either of them.

| name | (Required) An [identifier](identifiers.md) that represents the name of the bucket that you want to delete. |
| ---- | ---------------------------------------------------------------------------------------------------------- |

### [](#if-exists)IF EXISTS Clause

The optional `IF EXISTS` clause enables the statement to complete successfully when the specified bucket doesn’t exist. If a bucket with the same name does not exist, then:

* If this clause is not present, an error is generated.
* If this clause is present, the statement does nothing and completes without error.

## [](#examples)Examples

Example 1\. Drop a bucket named `student-records`

```sqlpp
DROP BUCKET `student-records`;
```

Example 2\. Drop a bucket named `custom-bucket` if it exists

```sqlpp
DROP BUCKET IF EXISTS `custom-bucket`;
```

## [](#related-links)Related Links

* For an overview of buckets, see [Buckets](../../learn/buckets-memory-and-storage/buckets.md).
* For step-by-step procedures for bucket management, see [Manage Buckets](../../manage/manage-buckets/bucket-management-overview.md).
* For managing buckets with the REST API, see [Buckets API](../../rest-api/rest-bucket-intro.md).