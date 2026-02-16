[View original HTML](/enterprise-analytics/2.0/manage/manage-security/user-defined-role.html)

> Learn how to create custom roles in Enterprise Analytics to implement granular access control that matches your organization’s specific security requirements. 

Enterprise Analytics allows you to create custom roles tailored to your organization’s specific access control needs. Create user-defined roles to group privileges logically and assign them to multiple users for consistent security management across your database environment.

This information is stored in the `Metadata`.`Role` collection.

## [](#create-role)Create Role

The `CREATE ROLE` statement creates a new role for use within an Enterprise Analytics instance.

**Create Role Diagram** 

![create_role ::= 'CREATE' 'ROLE' role](../../sqlpp/_images/create_role.png) 

Role names are global within an Enterprise Analytics instance. They must be unique across databases and scopes or else the create attempt fails.

## [](#drop-role)Drop Role

The `DROP ROLE` statement drops an existing role from an Enterprise Analytics instance.

**Drop Role Diagram** 

![drop_role ::= ](../../sqlpp/_images/drop_role.png) 

The role dropped must not be in use, otherwise the drop attempt returns an error.

## [](#example)Example

The following example creates a user-defined role named `roleName` with specific privileges:

```sqlpp
CREATE ROLE roleName;
DROP ROLE roleName
```