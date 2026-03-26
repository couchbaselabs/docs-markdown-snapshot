---
title: CREATE GROUP
description: The CREATE GROUP statement enables you to create a group.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/creategroup.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:cloud:n1ql:n1ql-language-reference/creategroup.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/n1ql/n1ql-language-reference/creategroup.html)

# CREATE GROUP

> The CREATE GROUP statement enables you to create a group. 

## [](#purpose)Purpose

Use the CREATE GROUP statement to define a new group within the Couchbase Server Role-Based Access Control (RBAC) system. You can specify the group's name, description, and assign it one or more roles.

By creating groups, you can organize users and assign roles collectively. When you add users to a group, they automatically inherit the roles assigned to that group.

## [](#prerequisites)Prerequisites

To execute this statement in the Capella UI, you must have one of the following roles:

* [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner)
* [Project Owner](../../projects/project-roles.md#project-owner-role)
* [Data Writer](../../projects/project-roles.md#project-cluster-data-reader-writer)

> [!NOTE]
> You cannot execute this statement using [cluster access credentials](../../clusters/cluster-rbac.md).

## [](#syntax)Syntax

```ebnf
create-group ::= 'CREATE' 'GROUP' ( 'IF' 'NOT' 'EXISTS' )? name 
                 ( 'WITH' description )? 
                 ( 'ROLE' rbac-role | 'ROLES' rbac-role ( ',' rbac-role )* | 'NO' 'ROLES' )
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/create-group.png) 

| name        | (Required) The unique identifier for the new group.                  |
| ----------- | -------------------------------------------------------------------- |
| description | (Optional) A quoted string containing the description for the group. |
| rbac-role   | (Required) [Add Roles](#roles)                                       |

> [!NOTE]
> When creating a group, you can grant roles to them using one of the following options: `ROLE`, `ROLES`, or `NO ROLES`. You can specify only one of these options per statement.
> 
> * `ROLE` assigns a single role to the group.
> * `ROLES` assigns multiple roles to group (the names must be separated by commas).
> * `NO ROLES` creates a group with no roles assigned. This option has no effect during group creation.

### [](#if-not-exists)IF NOT EXISTS Clause

The optional `IF NOT EXISTS` clause enables the statement to complete successfully when the specified group already exists. If a group with the same name already exists, then:

* If this clause is not present, an error is generated.
* If this clause is present, the statement does nothing and completes without error.

### [](#roles)Add Roles

```ebnf
rbac-role ::= role ( 'ON' keyspace-ref )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/rbac-role.png) 

| role         | One of the [RBAC role names predefined](../../clusters/manage-database-users.md) by Couchbase Server. For the following roles, you can use their short forms as well: query\_select → select query\_insert → insert query\_update → update query\_delete → delete |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| keyspace-ref | [Keyspace Reference](#keyspace-ref)                                                                                                                                                                                                                               |

#### [](#keyspace-ref)Keyspace Reference

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

Use keyspace reference to specify the target keyspace. For more information about each element, see the [Keyspace Reference](from.md#from-keyspace-ref) section in the FROM clause.

## [](#examples)Examples

Example 1\. Create a group `sales` and assign it the `query_select` role

```sqlpp
CREATE GROUP sales ROLE query_select ON `travel-sample`.`inventory`.`airline`;
```

Example 2\. Create a group `travelagents` and assign it multiple roles

```sqlpp
CREATE GROUP travelagents
WITH "Sample travel agents group"
ROLES data_reader ON `travel-sample`.`inventory`.`airline`,
select ON `travel-sample`.`inventory`.`landmark`;
```

Example 3\. Create a group `support` if it does not already exist

```sqlpp
CREATE GROUP IF NOT EXISTS support ROLE query_update
ON `travel-sample`.`inventory`.`airport`;
```

## [](#related-links)Related Links

* To create a new user, see [CREATE USER](createuser.md).
* To update an existing group, see [ALTER GROUP](altergroup.md).
* To delete a group, see [DROP GROUP](dropgroup.md).