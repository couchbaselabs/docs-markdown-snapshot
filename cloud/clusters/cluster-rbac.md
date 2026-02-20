---
title: Cluster Access
description: Cluster-level role-based access control (RBAC) defines cluster
  access permissions for programmatic access to your
  xref:clusters:databases.adoc[clusters].
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/cluster-rbac.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:clusters:cluster-rbac.adoc[]
---

[View original HTML](/cloud/clusters/cluster-rbac.html)

# Cluster Access

> Cluster-level role-based access control (RBAC) defines cluster access permissions for programmatic access to your [clusters](databases.md). 

Cluster access credentials provide programmatic and application-level access to data on a cluster. These credentials are separate from [organization roles](../organizations/organization-user-roles.md) and [project roles](../projects/project-roles.md). Your Capella user account’s organization and project roles control your access to the Capella UI, while cluster access credentials control programmatic and application-level access to data.

Cluster access credentials are specific to a cluster and consist of a cluster access name, password, and a set of access levels or roles, depending on the chosen credential type.

## [](#cluster-access-credential-types)Cluster Access Credential Types

The available access credential types are:

[Basic access credentials](#basic-access-credentials)

Read, write, or read/write access at the bucket, scope, and collection level.

[Advanced access credentials](#advanced-access-credentials)

Custom combinations of fine-grained privileges and access roles.

When choosing between basic and advanced access credentials, consider the following:

|                    | Basic Access Credentials                                                                        | Advanced Access Credentials                                                                                                                                                        |
| ------------------ | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Availability**   | All plans                                                                                       | Paid plans only                                                                                                                                                                    |
| **Access Control** | Predefined permission sets: Read Write Read/Write                                               | Fine-grained privileges and custom access roles with precise control over individual operations                                                                                    |
| **Reusability**    | Permissions configured individually for each credential                                         | Create reusable access roles that you can assign to multiple advanced credentials                                                                                                  |
| **Best For**       | Standard read/write operations Quick setup and deployment Straightforward security requirements | Least-privilege security models Providing specific operation access, such as query only Compliance and audit requirements Standardized access patterns across multiple credentials |

> [!IMPORTANT]
> You cannot convert basic access credentials to advanced access credentials, or advanced access credentials to basic access credentials. If you need to change credential types, you must [create new credentials](manage-database-users.md#create-database-credentials) with the desired type and migrate your applications to use them. A cluster may have both credential types active simultaneously.

## [](#basic-access-credentials)Basic Access Credentials

When using basic access credentials, you can assign cluster access credentials on a per-bucket, per-scope, and per-collection basis. For example, you can grant access to all buckets and scopes in a cluster, assign different access levels to individual buckets, or grant access to just a single collection. This system allows you to mix and match access levels to different buckets, scopes, and collections in a cluster to match your application and security requirements.

The following table outlines the access levels available for basic access credentials and their corresponding privileges.

| Access         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Read**       | Grants the privileges of the following Couchbase roles: [data\_reader](../../server/current/learn/security/roles.md#data-reader) [data\_dcp\_reader](../../server/current/learn/security/roles.md#data-dcp-reader) [data\_monitoring](../../server/current/learn/security/roles.md#data%5Fmonitor) [fts\_searcher](../../server/current/learn/security/roles.md#search-reader) [query\_select](../../server/current/learn/security/roles.md#query-select) [analytics\_reader](../../server/current/learn/security/roles.md#analytics-reader) [query\_execute\_global\_functions](../../server/current/learn/security/roles.md#execute-global-functions) [query\_execute\_global\_external\_functions](../../server/current/learn/security/roles.md#execute-global-external-functions) [analytics\_select](../../server/current/learn/security/roles.md#analytics-select) [external\_stats\_reader](../../server/current/learn/security/roles.md#external-stats-reader) (granted only when you assign Read access to all buckets) [query\_execute\_functions](../../server/current/learn/security/roles.md#execute-scope-functions) [query\_execute\_external\_functions](../../server/current/learn/security/roles.md#execute-scope-external-functions) [query\_use\_sequences](../../server/current/learn/security/roles.md#query-use-sequences)                                                                           |
| **Write**      | Grants the privileges of the following Couchbase roles: [data\_writer](../../server/current/learn/security/roles.md#data-writer) [fts\_admin](../../server/current/learn/security/roles.md#search-admin) [query\_insert](../../server/current/learn/security/roles.md#query-insert) [query\_update](../../server/current/learn/security/roles.md#query-update) [query\_delete](../../server/current/learn/security/roles.md#query-delete) [query\_manage\_index](../../server/current/learn/security/roles.md#query-manage-index) [replication\_target](../../server/current/learn/security/roles.md#xdcr-inbound) [analytics\_admin](../../server/current/learn/security/roles.md#analytics-admin) [query\_manage\_global\_functions](../../server/current/learn/security/roles.md#manage-global-functions) [query\_manage\_global\_external\_functions](../../server/current/learn/security/roles.md#manage-global-external-functions) [analytics\_manager](../../server/current/learn/security/roles.md#analytics-manager) [scope\_admin](../../server/current/learn/security/roles.md#manage-scopes) [query\_manage\_functions](../../server/current/learn/security/roles.md#manage-scope-functions) [query\_manage\_external\_functions](../../server/current/learn/security/roles.md#manage-scope-external-functions) [query\_manage\_sequences](../../server/current/learn/security/roles.md#query-manage-sequences) |
| **Read/Write** | Grants the privileges of the following Couchbase roles: All the privileges of [Read](#database-role-read). All the privileges of [Write](#database-role-write).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## [](#advanced-access-credentials)Advanced Access Credentials

Advanced access credentials use access roles. Access roles are reusable collections of [preconfigured privileges](#table-database-privileges) applied at the container level, which you can assign to 1 or more advanced cluster credentials.

Advanced access credentials have no predefined access roles, instead you need to [create custom access roles](manage-database-users.md#access-roles) for your access requirements. Access roles simplify permission management when multiple users or applications require the same set of privileges. By creating access roles that match common access patterns in your organization, you can:

* Maintain consistent security policies across multiple credentials.
* Simplify credential management by updating role definitions rather than individual credentials.
* Document intended access patterns for different user types or applications.

The following diagram illustrates the relationship between credentials, access roles, and privileges:

![Diagram](_images/diag-d6c85d380c22f8bcc16b1e9b33817562311c33a0.svg) 

### [](#privilege-levels-and-data-containers)Privilege Levels and Data Containers

Each privilege applies at a specific data container level. For example, a global privilege applies across the entire cluster, while a collection-level privilege applies to a specific collection.

Privileges have the following levels:

Global

Applies across all buckets in the entire cluster.

Bucket

Applies to all or specified buckets.

Bucket/Scope

Applies to all or specified scopes within a bucket.

Bucket/Scope/Collection

Applies to all or specified collections within a bucket and scope.

When you assign a non-global privilege, you can choose to use the default and apply it to all data containers at its privilege level or to specific ones. This flexibility lets you implement least-privilege security models tailored to your application architecture.

### [](#privileges-for-advanced-access-credentials)Privileges for Advanced Access Credentials

The following table lists the available privileges for advanced access credentials, their mapping to Couchbase Server roles, and data container access levels.

| Privilege               | Server Role                                                                                                                                                                                                                              | Access Level            |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| **Global**              |                                                                                                                                                                                                                                          |                         |
| Global Function Execute | [query\_execute\_global\_functions](../../server/current/learn/security/roles.md#execute-global-functions) [query\_execute\_global\_external\_functions](../../server/current/learn/security/roles.md#execute-global-external-functions) | Global                  |
| Query Catalog           | [query\_system\_catalog](../../server/current/learn/security/roles.md#query-system-catalog)                                                                                                                                              | Global                  |
| Global Function Manage  | [query\_manage\_global\_functions](../../server/current/learn/security/roles.md#manage-global-functions) [query\_manage\_global\_external\_functions](../../server/current/learn/security/roles.md#manage-global-external-functions)     | Global                  |
| Analytics Read          | [analytics\_reader](../../server/current/learn/security/roles.md#analytics-reader)                                                                                                                                                       | Global                  |
| Analytics Admin         | [analytics\_admin](../../server/current/learn/security/roles.md#analytics-admin)                                                                                                                                                         | Global                  |
| Stats Read              | [external\_stats\_reader](../../server/current/learn/security/roles.md#external-stats-reader)                                                                                                                                            | Global                  |
| Query Manage Catalog    | [query\_manage\_system\_catalog](../../server/current/learn/security/roles.md#query%5Fmanage%5Fsystem%5Fcatalog)                                                                                                                         | Global                  |
| Query Curl Access       | [query\_external\_access](../../server/current/learn/security/roles.md#query-curl-access)                                                                                                                                                | Global                  |
| **Analytics**           |                                                                                                                                                                                                                                          |                         |
| Analytics Manage        | [analytics\_manager](../../server/current/learn/security/roles.md#analytics-manager)                                                                                                                                                     | Bucket                  |
| Analytics Select        | [analytics\_select](../../server/current/learn/security/roles.md#analytics-select)                                                                                                                                                       | Bucket/Scope/Collection |
| **Data**                |                                                                                                                                                                                                                                          |                         |
| Data Read               | [data\_reader](../../server/current/learn/security/roles.md#data-reader) [data\_dcp\_reader](../../server/current/learn/security/roles.md#data-dcp-reader)                                                                               | Bucket/Scope/Collection |
| Data Manage             | [data\_writer](../../server/current/learn/security/roles.md#data-writer)                                                                                                                                                                 | Bucket/Scope/Collection |
| Data Monitor            | [data\_monitoring](../../server/current/learn/security/roles.md#data-monitor)                                                                                                                                                            | Bucket/Scope/Collection |
| **Eventing**            |                                                                                                                                                                                                                                          |                         |
| Eventing Manage         | [eventing\_manage\_functions](../../server/current/learn/security/roles.md#eventing-manage-functions)                                                                                                                                    | Bucket/Scope            |
| **Search**              |                                                                                                                                                                                                                                          |                         |
| FTS Manage              | [fts\_admin](../../server/current/learn/security/roles.md#search-admin)                                                                                                                                                                  | Bucket                  |
| FTS Read                | [fts\_searcher](../../server/current/learn/security/roles.md#search-reader)                                                                                                                                                              | Bucket/Scope/Collection |
| **Query**               |                                                                                                                                                                                                                                          |                         |
| Query Insert            | [query\_insert](../../server/current/learn/security/roles.md#query-insert)                                                                                                                                                               | Bucket/Scope/Collection |
| Query Update            | [query\_update](../../server/current/learn/security/roles.md#query-update)                                                                                                                                                               | Bucket/Scope/Collection |
| Query Index             | [query\_manage\_index](../../server/current/learn/security/roles.md#query-manage-index)                                                                                                                                                  | Bucket/Scope/Collection |
| Query Read              | [query\_select](../../server/current/learn/security/roles.md#query-select)                                                                                                                                                               | Bucket/Scope/Collection |
| Query Manage            | [query\_manage\_functions](../../server/current/learn/security/roles.md#manage-scope-functions) [query\_manage\_external\_functions](../../server/current/learn/security/roles.md#manage-scope-external-functions)                       | Bucket/Scope            |
| Query Delete            | [query\_delete](../../server/current/learn/security/roles.md#query-delete)                                                                                                                                                               | Bucket/Scope/Collection |
| Query Execute           | [query\_execute\_functions](../../server/current/learn/security/roles.md#execute-scope-functions) [query\_execute\_external\_functions](../../server/current/learn/security/roles.md#execute-scope-external-functions)                   | Bucket/Scope            |
| Query Use Sequences     | [query\_use\_sequences](../../server/current/learn/security/roles.md#query%5Fuse%5Fsequences)                                                                                                                                            | Bucket/Scope            |
| Query Manage Sequences  | [query\_manage\_sequences](../../server/current/learn/security/roles.md#query%5Fmanage%5Fsequences)                                                                                                                                      | Bucket/Scope            |

## [](#managing-cluster-rbac)Managing Cluster RBAC

For detailed instructions on implementing cluster RBAC, see:

* [Manage Cluster Access Credentials](manage-database-users.md)

## [](#see-also)See Also

* [Organizations and Organization Users Overview](../organizations/organizations.md)
* [Organization Roles](../organizations/organization-user-roles.md)
* [Projects Overview](../projects/projects.md)
* [Project Roles](../projects/project-roles.md)
* [Manage Cluster Access Credentials](manage-database-users.md)
* [Configure Allowed IP Addresses](allow-ip-address.md)