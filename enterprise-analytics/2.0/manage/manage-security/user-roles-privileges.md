---
title: User Roles and Privileges
description: Learn how to manage user access through Enterprise Analytics'
  role-based security system with predefined roles and granular privileges.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/manage/pages/manage-security/user-roles-privileges.adoc
  xref: xref:2.0@enterprise-analytics:manage:manage-security/user-roles-privileges.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/manage/manage-security/user-roles-privileges.html)

# User Roles and Privileges

> Learn how to manage user access through Enterprise Analytics' role-based security system with predefined roles and granular privileges. 

Enterprise Analytics uses Role-Based Access Control (RBAC) to secure your data and operations. Use predefined roles for quick setup or assign specific privileges to create custom access patterns that match your organization's security requirements.

Enterprise Analytics provides predefined roles and privileges to manage user access control effectively.

RBAC metadata for Enterprise Analytics is stored in the `Metadata`.`Role`, `Metadata`.`AssignedRole`, and `Metadata`.`Privilege` collections.

Privileges can be applied at different levels to control access granularity:

* Database Level
* Scope Level
* Collection Level

![Diagram](../_images/diag-b78445bb0a67b6342af0e78ab183441ae5df07d4.svg) 

## [](#available-roles)Available Roles

Enterprise Analytics provides predefined roles categorized into administrative and non-administrative types to streamline user access management. Choose administrative roles for cluster management tasks or non-administrative roles for standard data access and operations.

### [](#administrative-roles)Administrative Roles

The following administrative roles are available in Enterprise Analytics:

__Table 1\. Administrative Roles__
| Role                           | Capabilities                                                                                                                                                                           |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Full Admin**                 | Can manage all cluster features (including security).Can access the web console.Can read and write all data.                                                                           |
| **Read-Only Admin**            | Can view all cluster statistics.Can access the web console.Cannot read security related settings.                                                                                      |
| **Security Admin**             | Can view all cluster statistics, manage certificates, and manage security related settings.Can access the web console.Cannot read data.                                                |
| **Local User Admin**           | Can view all cluster statistics and manage local user roles, but not grant Full Admin or Security Admin roles to other users or itself.Can access the web console.Cannot read data.    |
| **Local User Admin**           | Can view all cluster statistics and manage local user roles, but not grant Full Admin or Security Admin roles to other users or itself.Can access the web console.Cannot read data.    |
| **External User Admin**        | Can view all cluster statistics and manage external user roles, but not grant Full Admin or Security Admin roles to other users or itself.Can access the web console.Cannot read data. |
| **Cluster Admin**              | Can manage all cluster features except security and users.Can access the web console.Cannot read data.                                                                                 |
| **External Stats Reader**      | Access to /metrics endpoint for Prometheus integration.Can read all stats for all services.Cannot access the web console.                                                              |
| **Enterprise Analytics Admin** | Can access Enterprise Analytics service administrative APIs (i.e. <host>:8095/api/v1/\*).Can assign and modify RBAC privileges.Can read and write all data.                            |

### [](#non-administrative-roles)Non-Administrative Roles

The following non-administrative roles are available in Enterprise Analytics:

__Table 2\. Non-Administrative Roles__
| Role                            | Capabilities                                                                                                                             |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Enterprise Analytics Access** | Provides access to Enterprise Analytics metadata required to use the service.Can access the web console.Does not provide access to data. |

## [](#target-object-privileges)Target Object Privileges

| Target Object | Privileges                                                             |
| ------------- | ---------------------------------------------------------------------- |
| Database      | create, drop                                                           |
| Scope         | create, drop                                                           |
| Collection    | select, insert, upsert, delete, analyze, create, drop                  |
| View          | select, create, drop                                                   |
| Index         | create, drop                                                           |
| Function      | execute, create, drop                                                  |
| Link          | connect, disconnect, copy to, copy from, create, drop, alter, describe |
| Role          | create, drop                                                           |
| Synonym       | create, drop                                                           |

## [](#users-function)Users Function

The `users()` function is a SQL++ built-in function that returns a list the cluster's current users.

### [](#example)Example:

If a user named `user1` has been created and granted the `analytics_access` role, you can retrieve user information using the `users()` function as follows:

select * from `users()` u;

The output:

[
  {
    "u": {
      "id": "user1",
      "domain": "local",
      "roles": [
        {
          "role": "analytics_access",
          "origins": [
            {
              "type": "user"
            }
          ]
        }
      ],
      "groups": [],
      "external_groups": [],
      "name": "",
      "uuid": "1b480a02-68d9-4fff-96bd-d87fd5ea5a1f",
      "password_change_date": "2025-08-06T21:32:11+05:30",
      "locked": false,
      "temporary_password": false
    }
  }
]