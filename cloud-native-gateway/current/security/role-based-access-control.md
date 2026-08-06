---
title: Role-Based Access Control
description: How Cloud Native Gateway enforces Couchbase Server's role-based
  access control (RBAC) for all operations through the Protostellar and Data API
  interfaces.
editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/security/pages/role-based-access-control.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:cloud-native-gateway:security:role-based-access-control.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/security/role-based-access-control.html)

# Role-Based Access Control

> How Cloud Native Gateway enforces Couchbase Server's role-based access control (RBAC) for all operations through the Protostellar and Data API interfaces. 

## [](#rbac-enforcement-model)RBAC Enforcement Model

Cloud Native Gateway does not implement its own authorization layer. Instead, it leverages the existing Couchbase Server RBAC system to enforce access control for all operations.

The enforcement model works as follows:

1. The client authenticates to Cloud Native Gateway (username/password or TLS client certificate).
2. Cloud Native Gateway validates the credentials against Couchbase Server and identifies the user and their domain such as local and LDAP.
3. For **KV operations**, Cloud Native Gateway forwards the request to the data node using its own cluster credentials with On-Behalf-Of semantics. The data node enforces RBAC based on the On-Behalf-Of user's roles.
4. For **Query, Search, and Analytics operations**, Cloud Native Gateway makes HTTP requests to the backend service using its own credentials with On-Behalf-Of headers. The backend service enforces RBAC for the On-Behalf-Of user.
5. For **Administrative operations** such as bucket management and index management, the same On-Behalf-Of pattern applies. Cloud Native Gateway authenticates on behalf of the user, and the backend enforces the required administrative roles.

This means:

* Users configured in Couchbase Server through UI, REST API, or LDAP integration are automatically available for Cloud Native Gateway access.
* Cloud Native Gateway enforces the roles and permissions assigned to users in Couchbase Server without additional configuration. It does not introduce any new roles or permissions.

## [](#required-roles-by-operation)Required Roles by Operation

The following table summarizes the Couchbase Server roles required for common operations through Cloud Native Gateway.:

| Operation                                  | Required Role                                                            |
| ------------------------------------------ | ------------------------------------------------------------------------ |
| KV Read (Get, Exists, Replicas)            | data\_reader on the target bucket/scope/collection                       |
| KV Write (Insert, Upsert, Replace, Remove) | data\_writer on the target bucket/scope/collection                       |
| KV Sub-Document Read                       | data\_reader on the target bucket/scope/collection                       |
| KV Sub-Document Write                      | data\_writer on the target bucket/scope/collection                       |
| Query (SELECT)                             | query\_select on the target bucket/scope/collection                      |
| Query (INSERT, UPDATE, DELETE)             | query\_insert, query\_update, query\_delete as appropriate               |
| Search Query                               | fts\_searcher on the target index                                        |
| Analytics Query                            | analytics\_reader or appropriate analytics role                          |
| Transactions                               | data\_reader and data\_writer on all involved buckets/scopes/collections |
| Bucket Management                          | cluster\_admin or bucket\_admin on the target bucket                     |
| Collection Management                      | cluster\_admin or bucket\_admin on the parent bucket                     |
| Query Index Management                     | query\_manage\_index on the target bucket                                |
| Search Index Management                    | fts\_admin on the target bucket                                          |

## [](#cloud-native-gateway-service-account)Cloud Native Gateway Service Account

Cloud Native Gateway itself connects to the Couchbase cluster using a service account (the username and password provided in its configuration). This service account requires sufficient privileges to:

* Read cluster configuration and bucket lists.
* Register with Couchbase Server for credential validation.
* Forward requests with On-Behalf-Of semantics.

The Cloud Native Gateway service account typically requires `cluster_admin` level access to support On-Behalf-Of authentication for all user roles. This is because Cloud Native Gateway must be able to perform any operation that any authenticated user might request.

> [!IMPORTANT]
> The Cloud Native Gateway service account credentials are sensitive. In Kubernetes, store them in a Secret and reference them from the pod specification. Never log or expose these credentials.

## [](#capella-specific-considerations)Capella Specific Considerations

In Couchbase Capella, you manage RBAC through the Capella UI and API rather than Couchbase Server directly.

Key differences:

* **Database Credentials** — Capella uses database-scoped credentials (database user/password) rather than cluster-level users. These credentials are configured in the Capella UI.
* **Allowed IP ranges** — Capella enforces IP allow-lists at the ingress level. This provides an additional layer of access control through IP filtering.
* **Organization roles** — Capella's organization and project-level roles control who can manage the cluster and its Cloud Native Gateway configuration. This does not affect data access RBAC.
* **Audit logging** — Capella records all authentication and authorization events in audit logs, including requests that pass through Cloud Native Gateway.

For self-managed deployments, make sure that the Couchbase Server audit log is enabled if you need a record of data access through Cloud Native Gateway. Cloud Native Gateway does not maintain its own audit log; it relies on the Couchbase Server audit system to record operations performed on behalf of users.