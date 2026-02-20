---
title: GRANT
description: The GRANT statement allows granting any RBAC roles to a specific user or group.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/n1ql/pages/n1ql-language-reference/grant.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:n1ql:n1ql-language-reference/grant.adoc[]
---

[View original HTML](/server/current/n1ql/n1ql-language-reference/grant.html)

# GRANT

> The GRANT statement allows granting any RBAC roles to a specific user or group. 

Roles can be of the following two types:

simple

Roles which apply generically to all keyspaces or resources in the cluster.

For example: `cluster_admin` or `bucket_admin`

parameterized by a keyspace

Roles which are defined for the context of the specified keyspace only. Specify the keyspace name after the keyword ON.

For example: `` data_reader ON `travel-sample` ``  
or `` query_select ON `travel-sample`.`inventory`.`airline` ``

> [!NOTE]
> Only Full Administrators can run the GRANT statement. For more details about user roles, see [Authorization](../../learn/security/authorization-overview.md).

## [](#syntax)Syntax

```ebnf
grant ::= grant-user | grant-group
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/grant.png) 

```ebnf
grant-user ::= 'GRANT' role ( ',' role )* ( 'ON' keyspace-ref ( ',' keyspace-ref )* )?
          'TO' ( 'USER' | 'USERS' )? user ( ',' user )*
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/grant-user.png) 

```ebnf
grant-group ::= 'GRANT' role ( ',' role )* ( 'ON' keyspace-ref ( ',' keyspace-ref )* )?
          'TO' ( 'GROUP' | 'GROUPS' ) group ( ',' group )*          
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/grant-group.png) 

| role         | One of the [RBAC role names predefined](../../learn/security/authorization-overview.md) by Couchbase Server. For the following roles, you can use their short forms as well: query\_select → select query\_insert → insert query\_update → update query\_delete → delete |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| keyspace-ref | [Keyspace Reference](#keyspace-ref)                                                                                                                                                                                                                                      |
| user         | A user name created by the Couchbase Server RBAC system.                                                                                                                                                                                                                 |
| group        | A group name created by the Couchbase Server RBAC system.                                                                                                                                                                                                                |

> [!NOTE]
> When granting roles to users, the keyword `USER` or `USERS` is optional. However, when granting roles to groups, you must include the keyword `GROUP` or `GROUPS`. You can use either the singular or plural form of these keywords as this does not affect the number of users or groups the role applies to.

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

The simple name or fully qualified name of a keyspace. For more information about the syntax, see the [CREATE INDEX](createindex.md#keyspace-ref) statement.

## [](#usage)Usage

GRANT statements have two forms:

1\. Unparameterized Roles

```sqlpp
GRANT replication_admin, query_external_access
   TO cchaplan, jgleason;
```

2\. Parameterized Roles

```sqlpp
GRANT query_select, views_admin
   ON orders, customers
   TO bill, linda;
```

> [!NOTE]
> Mixing of parameterized and unparameterized roles or syntax is not allowed and will create an error.

## [](#examples)Examples

Example 1\. Grant the role of Cluster Admin to multiple users

```sqlpp
GRANT cluster_admin TO david, michael, robin;
```

Example 2\. Grant Query Select and Data Reader roles on the `travel-sample` keyspace to a specific user

```sqlpp
GRANT query_select, data_reader ON `travel-sample` TO debby;
```

Example 3\. Grant the role of Data Reader on the `travel-sample` keyspace to a specific group

```sqlpp
GRANT data_reader ON `travel-sample` TO GROUP sales;
```