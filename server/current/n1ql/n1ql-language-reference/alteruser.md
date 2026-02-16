[View original HTML](/server/current/n1ql/n1ql-language-reference/alteruser.html)

> The ALTER USER statement enables you to alter the details of an existing user. 

## [](#purpose)Purpose

Use the ALTER USER statement to update a local user’s attributes, such as their password, full name, and group. You can add the user to new groups or remove them from all existing groups.

This statement helps manage access control and keeps user information up to date within Couchbase Server.

|  | When you add new groups to a user, the ALTER USER statement replaces the user’s existing group assignments with the new ones you provide. It updates the entire group list, so any existing groups not included in the new list will be removed. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#rbac-privileges)RBAC Privileges

To execute the ALTER USER statement, you must have either the Full Admin or the Security Admin role. For more information about user roles, see [Authorization](../../learn/security/authorization-overview.md).

## [](#syntax)Syntax

```ebnf
alter-user ::= 'ALTER' 'USER' username ( 'PASSWORD' password )? 
                ( 'WITH' name )? 
                ( 'GROUP' group | 'GROUPS' group ( ',' group )* | 'NO' 'GROUPS' )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/alter-user.png) 

| username | (Required) The unique identifier of the local user.                                                   |
| -------- | ----------------------------------------------------------------------------------------------------- |
| password | (Optional) A quoted string containing the user’s new password. It must be at least 6 characters long. |
| name     | (Optional) A quoted string containing the user’s updated name.                                        |
| group    | (Optional) The group you want to assign the user to.                                                  |

|  | When altering a user, you can update their group using one of the following options: GROUP, GROUPS, or NO GROUPS. You can specify only one of these options per statement. GROUP assigns the user to a single group. GROUPS assigns the user to multiple groups (the names must be separated by commas). NO GROUPS removes the user from all groups. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#examples)Examples

Example 1\. Change a user’s password and full name

```sqlpp
ALTER USER Hilary PASSWORD "newpassword" WITH "Hilary Chloe";
```

Example 2\. Assign a user to a new group

```sqlpp
ALTER USER Alice GROUP support;
```

Example 3\. Remove a user from existing groups

```sqlpp
ALTER USER Bob NO GROUPS;
```

## [](#related-links)Related Links

* To create a new user, see [CREATE USER](createuser.md).
* To delete a user, see [DROP USER](dropuser.md).
* To create a new group, see [CREATE GROUP](creategroup.md).