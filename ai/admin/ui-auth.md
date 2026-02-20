---
title: Manage Roles for UI Access
description: Your level of access to Capella AI Services using the Capella UI is
  determined by your organization and project roles.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/admin/pages/ui-auth.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:ai:admin:ui-auth.adoc[]
---

[View original HTML](/ai/admin/ui-auth.html)

# Manage Roles for UI Access

> Your level of access to Capella AI Services using the Capella UI is determined by your organization and project roles. 

To interact with Capella AI Services using the Capella UI, you need an organization role and 1 or more project roles.

## [](#prerequisites)Prerequisites

* You need to be the [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) to invite new users to your organization and assign organization roles.
* To add collaborators to a project and assign project roles, you need to be a [Project Owner](../../cloud/projects/project-roles.md) for that project. If you’re the [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner), you already have this role.

## [](#assign-organization-and-project-roles)Assign Organization and Project Roles

To assign organization and project roles, complete the following steps:

1. [Add the user to your organization](../../cloud/organizations/manage-organization-users.md#invite-organization-users).

  1. Assign the user 1 or more [organization roles](../../cloud/organizations/organization-user-roles.md).
2. [Add the user as a collaborator to your project](../../cloud/projects/manage-project-users.md#add-users-to-project).

  1. Assign the user 1 or more [project roles](../../cloud/projects/project-roles.md).

## [](#organization-and-project-role-permissions-for-ai-services)Organization and Project Role Permissions for AI Services

The permissions for Capella AI Services are driven by both your organization and project roles. Some services, such as the Model Service, only depend on your organization role. Most services, such as Workflows and AI Functions, depend on both your organization and project roles because they require interaction with a Capella operational cluster.

For more information about project roles and how they apply to operational clusters, see [Project Roles](../../cloud/projects/project-roles.md).

### [](#platform-permissions)Platform Permissions

Your organization role determines how you configure AI Services platform-level features. The following table describes the organization roles as they apply to platform-level features:

__Table 1\. Organization roles and platform features__
| Organization Role   | Add and Manage Integrations | View Integrations | Add Private Endpoints for Models | View Private Endpoints for Models |
| ------------------- | --------------------------- | ----------------- | -------------------------------- | --------------------------------- |
| Organization Owner  | ✔                           | ✔                 | ✔                                | ✔                                 |
| Project Creator     | ✖                           | ✖                 | ✖                                | ✖                                 |
| Organization Member | ✖                           | ✖                 | ✖                                | ✖                                 |

### [](#model-service-permissions)Model Service Permissions

The [Model Service](../build/model-service/model-service.md) operates at the organization level, so only your organization role determines your level of access to it.

The following table describes the organization roles as they apply to the Model Service:

__Table 2\. Organization roles and the Model Service__
| Organization Role   | Create and manage models | Add and View Model API Keys | View models |
| ------------------- | ------------------------ | --------------------------- | ----------- |
| Organization Owner  | ✔                        | ✔                           | ✔           |
| Project Creator     | ✖                        | ✖                           | ✔           |
| Organization Member | ✖                        | ✖                           | ✔           |

### [](#workflows-permissions)Workflows Permissions

Both organization and project roles determine your level of access to [Workflows](../build/vectorization-service/data-processing.md). When determining project roles, keep in mind that you must be a collaborator on the same project with the operational cluster that your Workflows interacts with.

The following table describes the organization roles as they apply to Workflows:

__Table 3\. Organization roles and Workflows__
| Organization Role   | Create workflows | Edit workflows | Delete workflows | Run workflows | View workflows |
| ------------------- | ---------------- | -------------- | ---------------- | ------------- | -------------- |
| Organization Owner  | ✔                | ✔              | ✔                | ✔             | ✔              |
| Project Creator     | ✖                | ✖              | ✖                | ✖             | ✖              |
| Organization Member | ✖                | ✖              | ✖                | ✖             | ✖              |

The following table describes the project roles as they apply to Workflows, for projects containing the operational cluster that your Workflows interacts with:

__Table 4\. Project roles and Workflows__
| Project Role            | Create workflows | Edit workflows | Delete workflows | Run workflows | View workflows |
| ----------------------- | ---------------- | -------------- | ---------------- | ------------- | -------------- |
| Project Owner           | ✔                | ✔              | ✔                | ✔             | ✔              |
| Project Cluster Manager | ✔                | ✔              | ✔                | ✖             | ✔              |
| Project Cluster Viewer  | ✖                | ✖              | ✖                | ✖             | ✔              |
| Project Data Writer     | ✖                | ✖              | ✖                | ✔             | ✔              |
| Project Data Reader     | ✖                | ✖              | ✖                | ✖             | ✔              |

### [](#ai-functions-permissions)AI Functions Permissions

Both organization and project roles determine your level of access to [AI Functions](../build/ai-functions.md). When determining project roles, keep in mind that you must be a collaborator on the same project that has the operational cluster where you’re interacting with AI Functions.

The following table describes the organization roles as they apply to AI Functions:

__Table 5\. Organization roles and AI Functions__
| Organization Role   | Enable AI Functions | Run AI Functions | Update AI Functions | View AI Functions |
| ------------------- | ------------------- | ---------------- | ------------------- | ----------------- |
| Organization Owner  | ✔                   | ✔                | ✔                   | ✔                 |
| Project Creator     | ✖                   | ✖                | ✖                   | ✔                 |
| Organization Member | ✖                   | ✖                | ✖                   | ✔                 |

The following table describes the project roles as they apply to AI Functions, for projects containing the operational cluster where you’re enabling and interacting with AI Functions:

__Table 6\. Project roles and AI Functions__
| Project Role            | Enable AI Functions | Run AI Functions | View AI Functions | View AI Functions Examples |
| ----------------------- | ------------------- | ---------------- | ----------------- | -------------------------- |
| Project Owner           | ✔                   | ✔                | ✔                 | ✔                          |
| Project Cluster Manager | ✖                   | ✖                | ✔                 | ✔                          |
| Project Cluster Viewer  | ✖                   | ✖                | ✔                 | ✔                          |
| Project Data Writer     | ✖                   | ✖                | ✔                 | ✔                          |
| Project Data Reader     | ✖                   | ✖                | ✔                 | ✔                          |

## [](#agent-catalog-permissions)Agent Catalog Permissions

Both organization and project roles determine your level of access to Agent Catalog - specifically [Agent Tracer](../build/agent-tracer/agent-tracer.md) and the [Tools and Prompts Hub](../build/tools-prompts-hub.md). When determining project roles, keep in mind that you must be a collaborator on the same project that has the operational cluster supporting Agent Catalog.

> [!NOTE]
> Programmatic Access
> 
> The Agent Catalog uses programmatic access to read and write data to your Capella operational cluster. Any user with cluster access credentials for your Agent Catalog bucket has programmatic access to your Agent Catalog data. For example, if a user has cluster access credentials that provide read and write access to your Agent Catalog bucket, they can read and write data in the Agent Catalog regardless of their organization or project roles.
> 
> For more information about Cluster Access Credentials, see [Manage Cluster Access Credentials](../../cloud/clusters/manage-database-users.md).

The following table describes the organization roles as they apply to Agent Catalog:

__Table 7\. Organization roles and Agent Catalog__
| Organization Role   | View Tools Hub | View Prompts Hub | View Tracer UI |
| ------------------- | -------------- | ---------------- | -------------- |
| Organization Owner  | ✔              | ✔                | ✔              |
| Project Creator     | ✖              | ✖                | ✖              |
| Organization Member | ✖              | ✖                | ✖              |

The following table describes the project roles for projects containing the operational cluster that’s supporting Agent Catalog:

__Table 8\. Project roles and Agent Catalog__
| Project Role            | View Tools Hub | View Prompts Hub | View Tracer UI |
| ----------------------- | -------------- | ---------------- | -------------- |
| Project Owner           | ✔              | ✔                | ✔              |
| Project Cluster Manager | ✖              | ✖                | ✖              |
| Project Cluster Viewer  | ✔              | ✔                | ✔              |
| Project Data Writer     | ✖              | ✖                | ✖              |
| Project Data Reader     | ✔              | ✔                | ✔              |

## [](#next-steps)Next Steps

* To access and manage AI Services using APIs, see [Get Started with AI Services APIs](../api-guide/api-start.md).
* To set up single sign-on (SSO) for your organization, see [Add SSO Authentication](../../cloud/organizations/ui-auth/add-sso-auth.md).