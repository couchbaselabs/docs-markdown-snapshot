[View original HTML](/cloud/n1ql/n1ql-language-reference/dropgroup.html)

> The DROP GROUP statement enables you to delete a group. 

## [](#purpose)Purpose

You can use this statement to clean up groups that are no longer needed.

Deleting a group removes all roles and privileges associated with the group. Users in the deleted group no longer inherit the roles granted to it.

## [](#rbac-privileges)RBAC Privileges

To execute the DROP GROUP statement, you must be an [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner) or [Project Owner](../../projects/project-roles.md#project-owner-role).

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