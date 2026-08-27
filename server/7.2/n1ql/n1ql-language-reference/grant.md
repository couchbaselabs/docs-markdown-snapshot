---
title: GRANT
description: The GRANT statement allows granting any RBAC roles to a specific user.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/grant.adoc
  xref: xref:7.2@server:n1ql:n1ql-language-reference/grant.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/n1ql/n1ql-language-reference/grant.html)

# GRANT

> The GRANT statement allows granting any RBAC roles to a specific user. 

Roles can be of the following two types:

simple

Roles which apply generically to all keyspaces or resources in the cluster.

For example: `ClusterAdmin` or `BucketAdmin`

parameterized by a keyspace

Roles which are defined for the scope of the specified keyspace only. The keyspace name is specified after ON.

For example: `` DataReader ON `travel-sample` ``  
or `` Query_Select ON `travel-sample` ``

> [!NOTE]
> Only Full Administrators can run the GRANT statement. For more details about user roles, see [Authorization](../../learn/security/authorization-overview.md).

## [](#syntax)Syntax

```ebnf
grant ::= 'GRANT' role ( ',' role )* ( 'ON' keyspace-ref ( ',' keyspace-ref )* )?
          'TO' user ( ',' user )*
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/grant.png) 

role

One of the [RBAC role names predefined](../../learn/security/authorization-overview.md) by Couchbase Server.

The following roles have short forms that can be used as well:

* `query_select` → `select`
* `query_insert` → `insert`
* `query_update` → `update`
* `query_delete` → `delete`

user

A user name created by the Couchbase Server RBAC system.

### [](#keyspace-ref)Keyspace Reference

```ebnf
keyspace-ref ::= keyspace-path | keyspace-partial
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-ref.png) 

```ebnf
keyspace-path ::= ( namespace ':' )? bucket ( '.' scope '.' collection )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-path.png) 

```ebnf
keyspace-partial ::= collection
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-partial.png) 

The simple name or fully-qualified name of a keyspace. Refer to the [CREATE INDEX](createindex.md#keyspace-ref) statement for details of the syntax.

## [](#usage)Usage

GRANT statements support legacy systems and have two forms:

1\. Unparameterized Roles

```sqlpp
GRANT Replication Admin, Query External Access
   TO cchaplan, jgleason;

GRANT replication_admin, query_external_access
   TO cchaplan, jgleason;
```

2\. Parameterized Roles

```sqlpp
GRANT Query Select, Views Admin
   ON orders, customers
   TO bill, linda;

GRANT query_select, views_admin
   ON orders, customers
   TO bill, linda;
```

> [!NOTE]
> Mixing of parameterized and unparameterized roles or syntax is not allowed and will create an error.

## [](#examples)Examples

Example 1\. Grant the role of Cluster Administrator to three people

```sqlpp
GRANT ClusterAdmin TO david, michael, robin;
```

Example 2\. Grant the roles of Cluster Administrator and Data Reader in the travel-sample keyspace to Debby

```sqlpp
GRANT ClusterAdmin, DataReader ON `travel-sample` TO debby;
```