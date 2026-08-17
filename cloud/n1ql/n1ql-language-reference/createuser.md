---
title: CREATE USER
description: The CREATE USER statement enables you to create a user.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/createuser.adoc
  xref: xref:cloud:n1ql:n1ql-language-reference/createuser.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/n1ql/n1ql-language-reference/createuser.html)

# CREATE USER

> The CREATE USER statement enables you to create a user. 

## [](#purpose)Purpose

Creating a user is an essential step in managing access to your Couchbase environment. You can use the CREATE USER statement to define a new local user in the Couchbase Server Role-Based Access Control (RBAC) system. By default, Couchbase Server assigns the user to the local authentication domain.

When you create a user, you can specify their basic attributes such as username, password, full name, and assign them to one or more groups. If you do not specify a group, the user is not assigned to any group by default.

## [](#prerequisites)Prerequisites

To execute this statement in the Capella UI, you must have one of the following roles:

* [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner)
* [Project Owner](../../projects/project-roles.md#project-owner-role)
* [Data Writer](../../projects/project-roles.md#project-cluster-data-reader-writer)

> [!NOTE]
> You cannot execute this statement using [cluster access credentials](../../clusters/cluster-rbac.md).

## [](#syntax)Syntax

```ebnf
create-user ::= 'CREATE' 'USER' ( 'IF' 'NOT' 'EXISTS' )? username 'PASSWORD' password 
                ( 'WITH' name )? 
                ( 'GROUP' group | 'GROUPS' group ( ',' group )* | 'NO' 'GROUPS' )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/create-user.png) 

| username | (Required) The unique identifier for the new local user.                                          |
| -------- | ------------------------------------------------------------------------------------------------- |
| password | (Required) A quoted string containing the user's password. It must be at least 6 characters long. |
| name     | (Optional) A quoted string containing the user's full name.                                       |
| group    | (Optional) The group you want to assign the user to.                                              |

> [!NOTE]
> When creating a user, you can assign them to groups using one of the following options: `GROUP`, `GROUPS`, or `NO GROUPS`. You can specify only one of these options per statement.
> 
> * `GROUP` assigns the user to a single group.
> * `GROUPS` assigns the user to multiple groups (the names must be separated by commas).
> * `NO GROUPS` creates a user without assigning any groups. This option has no effect during user creation.

### [](#if-not-exists)IF NOT EXISTS Clause

The optional `IF NOT EXISTS` clause enables the statement to complete successfully when the specified user already exists. If a user with the same username already exists, then:

* If this clause is not present, an error is generated.
* If this clause is present, the statement does nothing and completes without error.

## [](#examples)Examples

Example 1\. Create a user and specify their full name and password

```sqlpp
CREATE USER Hilary PASSWORD "password123" WITH "Hilary Smith";
```

Example 2\. Create a user and assign them to a single group

```sqlpp
CREATE USER Alice PASSWORD "password123" GROUP agents;
```

Example 3\. Create a user and assign them to multiple groups

```sqlpp
CREATE USER Bob PASSWORD "P@ssw0rd" GROUPS agents, tourguides, support;
```

Example 4\. Create a user with no group assignments

```sqlpp
CREATE USER Charlie PASSWORD "securePass" NO GROUPS;
```

Example 5\. Create a user if they do not already exist

```sqlpp
CREATE USER IF NOT EXISTS David PASSWORD "davidPass" WITH "David Trantow";
```

## [](#related-links)Related Links

* To update an existing user, see [ALTER USER](alteruser.md).
* To delete a user, see [DROP USER](dropuser.md).
* To create a new group, see [CREATE GROUP](creategroup.md).
* To grant roles and privileges to a user, see [GRANT](grant.md).