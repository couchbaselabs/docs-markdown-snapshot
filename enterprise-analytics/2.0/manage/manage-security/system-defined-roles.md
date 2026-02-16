[View original HTML](/enterprise-analytics/2.0/manage/manage-security/system-defined-roles.html)

> For authorizing users, Enterprise Analytics has some pre-built roles with predefined sets of privileges that can be assigned to users. 

System defined roles are pre-built permission sets that provide standardized access control for Enterprise Analytics users. These roles simplify security management by offering ready-to-use privilege combinations that administrators can assign without custom configuration.

These roles:

* Ensure consistency across user permissions and simplify the management of access control.
* Provide a straightforward approach to assigning permissions, particularly for users who may not have in-depth knowledge of Enterprise Analytics access control mechanisms.
* Help reduce the risk of unauthorized access and potential security vulnerabilities.
* Are useful if users access Enterprise Analytics through client applications (Power BI, Tableau) that cannot modify access privileges nor set roles.

## [](#available-system-defined-roles)Available System Defined Roles

The following system defined roles are available in Enterprise Analytics:

### [](#sys%5Fview%5Freader)sys\_view\_reader

`sys_view_reader` Role allows access to all the views (View and Tabular Analytics View (TAV)) globally. This role is useful for BI Tools like Tableau and Power BI, where the connection is at database level. Users with the `sys_view_reader` role have access to all the TAVs and need not GRANT access for TAVs explicitly.

#### [](#privileges)Privileges

The `sys_view_reader` role includes the following privilege:

* SELECT

### [](#sys%5Fdata%5Freader)sys\_data\_reader

`sys_data_reader` is the role that allows read access to data globally.

| Capability           | Description                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------- |
| Global Read Access   | Can read any accessible object globally (not specific to any object type).                  |
| Role Inheritance     | Inherits privileges of the sys\_view\_reader role via system role hierarchy.                |
| Object Accessibility | Access applies only to relevant objects. For example, SELECT on collections, not databases. |

#### [](#privileges-2)Privileges

The `sys_data_reader` role includes the following privilege:

* SELECT (inherited from `sys_view_reader` Role)

### [](#sys%5Fdata%5Fadmin)sys\_data\_admin

`sys_data_admin` is the role that allows access to data globally. This is not for any specific object type but a user with a `sys_data_admin` role can access any accessible object globally.

#### [](#privileges-3)Privileges

The `sys_data_admin` role includes the following privileges:

* SELECT (inherited from sys\_data\_reader Role)
* INSERT
* UPSERT
* DELETE
* ANALYZE
* EXECUTE
* CONNECT
* DISCONNECT
* COPY TO
* COPY FROM

### [](#sys%5Fsecurity%5Fadmin)sys\_security\_admin

`sys_security_admin` is the role that manages any object grant/revoke globally, as well as `create/drop` roles.

| Capability                | Description                                                                                                                                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Grant/Revoke Management   | Can GRANT/REVOKE any privilege on any object to/from any user and role.                                                                                                                                            |
| Role Management           | Can create/drop roles and GRANT/REVOKE privileges to/from custom roles.                                                                                                                                            |
| Default Object Privileges | Doesn’t have any privileges on objects by default. For example, user with sys\_security\_admin role can grant select on object to another user, but cannot query the object itself, but can be granted privileges. |
| Role Assignment Authority | Can grant sys\_data\_admin, sys\_data\_reader and sys\_view\_reader roles.                                                                                                                                         |

#### [](#privileges-4)Privileges

The `sys_security_admin` role includes the following privileges:

* CREATE
* DROP
* GRANT\_OPTION

### [](#sys%5Froot)sys\_root

The `sys_root` role is the highest privilege role in Enterprise Analytics. It provides full access to all resources and operations within the system and should be granted only to a limited number of users.

The `sys_root` role maps to the following database-specific administrative roles:

#### [](#privileges-5)Privileges

The `sys_root` role includes the following privileges:

| Privilege  | Description                                                    |
| ---------- | -------------------------------------------------------------- |
| CREATE     | Inherited from sys\_security\_admin Role, data\_reader\_writer |
| DROP       | Inherited from sys\_security\_admin Role                       |
| SELECT     | Inherited from sys\_data\_admin Role                           |
| INSERT     | Inherited from sys\_data\_admin Role                           |
| UPSERT     | Inherited from sys\_data\_admin Role                           |
| DELETE     | Inherited from sys\_data\_admin Role                           |
| ANALYZE    | Inherited from sys\_data\_admin Role                           |
| EXECUTE    | Inherited from sys\_data\_admin Role                           |
| CONNECT    | Inherited from sys\_data\_admin Role                           |
| DISCONNECT | Inherited from sys\_data\_admin Role                           |
| COPY TO    | Inherited from sys\_data\_admin Role                           |
| COPY FROM  | Inherited from sys\_data\_admin Role                           |