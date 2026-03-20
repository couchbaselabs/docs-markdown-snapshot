---
title: DROP USER
description: The DROP USER statement enables you to delete a user.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/dropuser.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:n1ql:n1ql-language-reference/dropuser.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/n1ql/n1ql-language-reference/dropuser.html)

# DROP USER

> The DROP USER statement enables you to delete a user. 

This statement permanently removes a user from the Couchbase Server Role-Based Access Control (RBAC) system. It removes the user from all groups and revokes all roles and privileges assigned to that user.

## [](#rbac-privileges)RBAC Privileges

To execute the DROP USER statement, you must be an [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner) or [Project Owner](../../projects/project-roles.md#project-owner-role).

## [](#syntax)Syntax

```ebnf
drop-user ::= 'DROP' 'USER' ( 'IF' 'EXISTS' )? username
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/drop-user.png) 

| username | (Required) The unique identifier of the local user you want to delete. |
| -------- | ---------------------------------------------------------------------- |

### [](#if-exists)IF EXISTS Clause

The optional `IF EXISTS` clause enables the statement to complete successfully when the specified user doesn’t exist. If a user with the same username does not exist, then:

* If this clause is not present, an error is generated.
* If this clause is present, the statement does nothing and completes without error.

## [](#examples)Examples

Example 1\. Delete a user named Bob

```sqlpp
DROP USER Bob;
```

Example 2\. Delete a user named David if they exist

```sqlpp
DROP USER IF EXISTS David;
```

## [](#related-links)Related Links

* To create a user, see [CREATE USER](createuser.md).
* To modify a user, see [ALTER USER](alteruser.md).
* For step by step procedures for managing users, see [Manage Users](#manage:manage-security/manage-users-and-roles.adoc).