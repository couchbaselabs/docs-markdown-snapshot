---
title: DROP GROUP
description: The DROP GROUP statement enables you to delete a group.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/dropgroup.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:cloud:n1ql:n1ql-language-reference/dropgroup.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/n1ql/n1ql-language-reference/dropgroup.html)

# DROP GROUP

> The DROP GROUP statement enables you to delete a group. 

## [](#purpose)Purpose

You can use this statement to clean up groups that are no longer needed.

Deleting a group removes all roles and privileges associated with the group. Users in the deleted group no longer inherit the roles granted to it.

## [](#prerequisites)Prerequisites

To execute this statement in the Capella UI, you must have one of the following roles:

* [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner)
* [Project Owner](../../projects/project-roles.md#project-owner-role)
* [Data Writer](../../projects/project-roles.md#project-cluster-data-reader-writer)

> [!NOTE]
> You cannot execute this statement using [cluster access credentials](../../clusters/cluster-rbac.md).

## [](#syntax)Syntax

```ebnf
drop-group ::= 'DROP' 'GROUP' ('IF' 'EXISTS' )? groupname
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/drop-group.png) 

| groupname | (Required) The unique identifier of the group you want to delete. |
| --------- | ----------------------------------------------------------------- |

### [](#if-exists)IF EXISTS Clause

The optional `IF EXISTS` clause enables the statement to complete successfully when the specified group doesn’t exist. If a group with the same name does not exist, then:

* If this clause is not present, an error is generated.
* If this clause is present, the statement does nothing and completes without error.

## [](#examples)Examples

Example 1\. Delete a group named `sales`

```sqlpp
DROP GROUP sales;
```

Example 2\. Delete a group named `support` if it exists

```sqlpp
DROP GROUP IF EXISTS support;
```

## [](#related-links)Related Links

* To create a group, see [CREATE GROUP](creategroup.md).
* To alter a group, see [ALTER GROUP](altergroup.md).
* For step-by-step procedures for managing groups, see [Manage Groups](#manage:manage-security/manage-users-and-roles.adoc).