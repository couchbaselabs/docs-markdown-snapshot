---
title: Role Based Access Control (RBAC)
description: For authorizing users, Enterprise Analytics provides <em>Role-Based
  Access Control</em>.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/manage/pages/manage-security/rbac-overview.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:enterprise-analytics:manage:manage-security/rbac-overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/manage/manage-security/rbac-overview.html)

# Role Based Access Control (RBAC)

> For authorizing users, Enterprise Analytics provides _Role-Based Access Control_. 

Enterprise Analytics uses Role-Based Access Control (RBAC) to manage access to system resources. In this model, privileges are assigned to fixed roles, which can then be granted to users—either directly or through user groups. Users can represent individuals, administrators, or applications.

RBAC in Enterprise Analytics supports multiple predefined roles, allowing for fine-grained access control. Privileges can be granted both to roles and directly to users, providing flexible and secure permission management.

## [](#example-scenarios)Example Scenarios

Enterprise Analytics RBAC provides a secure solution for each of the following scenarios:

* An application consists of several services, each of which has a different purpose. Compliance demands that each service be given a different set of read and write privileges, in order to constrain its activities to those absolutely required.
* An application is available to several different classes of user. Each user-class has a different set of requirements for reading and writing data. Compliance demands that each user-class be given no more than the minimum privileges for supporting its requirements.
* Test and production environments respectively require different degrees of constraint to be applied to read and write access. Administrators, developers, applications, and services should therefore each be granted one set of privileges for the test environment, and another (more restrictive) for the production.

## [](#rbac-concepts)RBAC Concepts

The following concepts are essential to an understanding of Enterprise Analytics RBAC:

* _Resource_: An entity the access to which must be controlled. A resource can be specified either individually, by name; or as a group for example, all databases, by means of a wildcard character. The complete list of resources to which RBAC is applied is provided in [System Defined Roles](system-defined-roles.md).
* _Privilege_: The right, assigned by Enterprise Analytics, to apply an action to a resource. Possible actions include _read_, _write_, and _execute_. The associations of privileges to resources and roles are explained in [User Role Privileges](user-roles-privileges.md).
* _Role_: An entity associated with a fixed set of privileges. The association of privileges to roles is described in [User Defined Roles](user-defined-role.md).
* _User_: An identity, recognized by Enterprise Analytics, based on the passing of a _username_ and _password_. A user can be assigned one or more _roles_: the privileges associated with each assigned role determine the resource-access granted the user. Users can be _local_ (defined on Enterprise Analytics) or _external_ (defined on a remote, network-accessible system). Each user might be an administrator or an application. For information about how to manage users, see [Manage Users and Roles](manage-users-and-roles.md).

## [](#rbac-security-model)RBAC Security Model

Couchbase RBAC controls access to cluster-resources. Resources can only be accessed by users. A user may be an administrator or an application.

Users can be added to Enterprise Analytics by the Full Administrator. Each user must be defined with a username and password. When attempting to access resources, each user must authenticate by means of these credentials.

A user can be assigned one or more roles by the Full Administrator. Each role is itself associated with a subset of privileges; a privilege being a form of action, such as Read, Write, Execute, or Manage. Each privilege is associated with a resource.

For example, the Data Reader role features the Read privilege, which is applied to the data of a database. When a user has been assigned the Data Reader role, and attempts to gain read-access to the database’s data by submitting their credentials, Enterprise Analytics identifies the user, recognises their assigned role and privilege, and duly authorises read-access.

> [!NOTE]
> Resource-access can optionally be specified by means of _parameterisation_. This means that a wildcard character has been used, during role-assignment, to specify that a privilege applies to all resource-instances within a resource-class: for example, to all databases.

## [](#defining-users-and-groups)Defining Users and Groups

Enterprise Analytics allows users to be defined individually, on the cluster. Each user so defined is of one of the following kinds:

* A _local user_. The username and password are defined and maintained on Enterprise Analytics.
* An _external user_. The username is recorded on Enterprise Analytics. However, the username and password are defined and maintained outside the cluster: for example, on a remote LDAP server.

Couchbase-Server roles can be assigned both to local and to external users. Roles can be assigned in either or both of the following ways:

* _Directly_. The user is associated directly with one or more Couchbase-Server roles.
* _By Group_. A Couchbase-Server _user-group_ is defined, and roles are assigned to the user-group. The user is made a member of the user-group, and thereby inherits all the roles of the group. A user can be a member of any number of groups.

> [!NOTE]
> By means of _LDAP Group Support_, the roles assigned to a Couchbase-Server user-group can be inherited by users not defined on Enterprise Analytics. For a detailed account, see [Authentication Domains](configure-ldap.md).

See [Manage Users, Groups, and Roles](manage-users-and-roles.md), for details on creating users and assigning roles.