---
title: Assign Roles for UI Access
description: Your level of access to the Capella UI is controlled using
  organization and project roles.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/admin/pages/auth/auth-ui.adoc
  xref: xref:analytics:admin:auth/auth-ui.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/admin/auth/auth-ui.html)

# Assign Roles for UI Access

> Your level of access to the Capella UI is controlled using organization and project roles. 

To interact with Capella Analytics using the Capella UI, you need an [organization role](#org-col-roles) and one or more [project roles](#proj-col-roles).

## [](#prerequisites)Prerequisites

* You need to be the [Organization Owner](../../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) to invite new users to your organization and assign organization roles.
* To add collaborators to a project and assign project roles, you need to be a [Project Owner](#project-owner-role) for that project. If you're the [Organization Owner](../../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner), you already have this role.

## [](#assign-organization-and-project-roles)Assign Organization and Project Roles

To assign organization and project roles, complete the following steps:

1. [Add the user to your organization](../../../cloud/organizations/manage-organization-users.md#invite-organization-users).

  1. Assign the user one or more [organization roles](../../../cloud/organizations/organization-user-roles.md).
2. [Add the user as a collaborator to your project](../../../cloud/projects/manage-project-users.md#add-users-to-project).

  1. Assign the user one or more [project roles](#proj-col-roles).

### [](#org-col-roles)Organization Roles and Capella Analytics

Every user account in Couchbase Capella has an organization role that determines their privileges when working with the Capella UI at the organization level. For example, a user who's an Organization Member cannot view any of the billing information inside the Capella UI, while an Organization Owner can.

Organization roles can control your level of access to both Capella Analytics and operational resources in an organization. A user with the Organization Owner role automatically has [Project Owner](#project-owner-role) privileges and is a collaborator for all projects in the organization. A user with the Project Creator role automatically has [Project Owner](#project-owner-role) privileges and is a collaborator for all projects they create. You can only view and work with projects where you're a collaborator.

### [](#proj-col-roles)Project Roles and Capella Analytics

Project roles are separate from [organization roles](#organizations:organization-user-roles.adoc), which grant overall privileges to Couchbase Capella. Project roles apply only at the project level and control your privileges in a project [where you're a collaborator](../../../cloud/projects/manage-project-users.md#add-users-to-project).

Project roles control your level of access to both Capella Analytics and operational resources in a project.

The following table describes the available project roles and their privileges as they apply to Capella Analytics. To see project roles as they apply to Capella operational, see [Project Roles](../../../cloud/projects/project-roles.md).

__Table 1\. Project roles in Capella Analytics__
| Role                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Project Owner**               | Provides complete Capella Analytics cluster-management access. Users with this role can access data in any Capella Analytics cluster in a project using the UI. A Project Owner has the following privileges when working with Capella Analytics: Create and manage Capella Analytics clusters Edit Capella Analytics cluster configurations and settings Create and manage Capella Analytics links Create, manage, and restore backups Create and manage private endpoints Create and manage vpc-peering Turn Capella Analytics clusters on or off View and configure cluster monitoring Configure allowed IP addresses Read and write data within any cluster in the project A user with the [Organization Owner](../../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) role automatically has [Project Owner](#project-owner-role) privileges for all projects in the organization. |
| **Project Manager**             | Provides access to management actions for all Capella Analytics clusters in a project. This role does not provide access to data. A Project Manager has the following privileges when working with Capella Analytics: Create and manage Capella Analytics clusters Edit Capella Analytics cluster configurations and settings Create and manage Capella Analytics links Turn Capella Analytics clusters on or off View and configure cluster monitoring Configure allowed IP addresses                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Project Viewer**              | Provides read-only access to view all Capella Analytics clusters in a project where you're a collaborator. This role does not provide access to data. A Project Viewer has the following privileges for a project where you're a collaborator: View all Capella Analytics clusters in the project View Capella Analytics configuration details and settings View allowed IP addresses View access control accounts and roles View Capella Analytics links View cluster monitoring Configure allowed IP addresses                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Database Data Reader**        | Provides read-only access to view data in any Capella Analytics cluster in a project where you're a collaborator. This role allows the use of the Workbench to read data, but it cannot modify or write data. A Database Data Reader has the following privileges for a project where you're a collaborator: Read data within any Capella Analytics cluster in the project                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Database Data Reader/Writer** | Provides read and write access to data in any Capella Analytics cluster in a project where you're a collaborator. This role allows the use of the Workbench to read and write data. A Database Data Reader/Writer has the following privileges for a project where you're a collaborator: Read and write data within any cluster in the project                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## [](#next-steps)Next Steps

* To programmatically access data on a Capella Analytics cluster, see [Manage Access to Cluster Data](auth-data.md).
* To set up single sign-on (SSO) for your organization, see [Add SSO Authentication](../../../cloud/organizations/ui-auth/add-sso-auth.md).