---
title: REVOKE
description: The REVOKE statement allows revoking of any RBAC roles from specific users.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/n1ql/pages/n1ql-language-reference/revoke.adoc
  xref: xref:7.6@server:n1ql:n1ql-language-reference/revoke.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/n1ql/n1ql-language-reference/revoke.html)

# REVOKE

> The REVOKE statement allows revoking of any RBAC roles from specific users. 

Roles can be of the following two types:

simple

Roles which apply generically to all keyspaces/resources in the cluster.

For example: `cluster_admin` or `bucket_admin`

parameterized by a keyspace

Roles which are defined for the scope of the specified keyspace only. The keyspace name is specified after ON.

For example: `` data_reader ON `travel-sample` ``  
or `` query_select ON `travel-sample` ``

> [!NOTE]
> Only Full Administrators can run the REVOKE statement. For more details about user roles, see [Authorization](../../learn/security/authorization-overview.md).

## [](#syntax)Syntax

```ebnf
revoke ::= 'REVOKE' role ( ',' role )* ( 'ON' keyspace-ref ( ',' keyspace-ref )* )?
           'FROM' user ( ',' user )*
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/revoke.png) 

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

## [](#examples)Examples

Example 1\. Revoke the role of Cluster Admin from three people

```sqlpp
REVOKE cluster_admin FROM david, michael, robin
```

Example 2\. Revoke the roles of Cluster Admin and Query Update in the travel-sample keyspace from Debby

```sqlpp
REVOKE query_select, query_update
    ON `travel-sample`
  FROM debby
```