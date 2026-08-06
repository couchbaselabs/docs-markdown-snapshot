---
title: Access Control
description: An overview of fine-grained access control for downstream edge
  clients in Couchbase Edge Server, including keyspace patterns, permissions,
  and enforcement behavior.
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.1/modules/access-control/pages/access-control-concept.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:couchbase-edge-server:access-control:access-control-concept.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-edge-server/current/access-control/access-control-concept.html)

# Access Control

Fine-grained access control lets you define read and write permissions for downstream edge clients at the database, scope, and collection level. This enables multiple applications to share a single Couchbase Edge Server instance while keeping each application's data isolated.

## [](#overview)Overview

By default, all configured users have unrestricted read and write access to all collections in a database. Fine-grained access control is opt-in. When you enable it at the server level using `enable_user_access_control`, Couchbase Edge Server enforces the access permissions you define for each user before allowing any REST operation.

Fine-grained access control applies to downstream edge clients accessing Couchbase Edge Server over the REST API or via Couchbase Lite sync. It does not affect upstream replication credentials used to sync with Sync Gateway or Capella App Services.

## [](#keyspace-patterns)Keyspace Patterns

Permissions are defined using keyspace patterns. A keyspace pattern identifies a target database, scope, and collection using dot notation.

__Table 1\. Keyspace Pattern Syntax__
| Pattern                                              | Target                                                    |
| ---------------------------------------------------- | --------------------------------------------------------- |
| database.scope.collection                            | A specific collection within a specific scope.            |
| database.scope.\*                                    | All collections within a specific scope.                  |
| database.\*                                          | All collections within the database, including \_default. |
| database                                             | The \_default.\_default collection of the database.       |
| database.\_default.collection or database.collection | A named collection within the \_default scope.            |

## [](#permissions)Permissions

Each keyspace pattern is assigned an array of one or more permissions.

__Table 2\. Permissions__
| Permission | Effect                                                                                                                                             |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| read       | The user can read documents from the targeted keyspace.                                                                                            |
| write      | The user can create, update, and delete documents in the targeted keyspace. Write-only access to a collection is supported for drop-box scenarios. |

## [](#enforcement-behavior)Enforcement Behavior

When `enable_user_access_control` is set to `true` on a database, Couchbase Edge Server checks the requesting user's permissions against the target keyspace for every REST call.

The following table describes how enforcement applies to each operation type.

__Table 3\. Access Control Enforcement by Operation__
| Operation Type       | REST Operations                                                        | Access Requirement                                                                                                                                                                            |
| -------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| General access       | Any REST call                                                          | The user must have read or write access to the targeted keyspace.                                                                                                                             |
| Data visibility      | GET /\_all\_dbs, GET /db, GET /{keyspace}/{docId}                      | The user must have read access to the targeted database or collection. Responses are filtered to show only databases and collections the user has explicit access to.                         |
| Data mutation        | POST /{keyspace}/, PUT /{keyspace}/{docId}, DELETE /{keyspace}/{docId} | The user must have write access to the targeted keyspace.                                                                                                                                     |
| Query execution      | GET /{keyspace}/\_query/{name}                                         | The user must have access to the named query, as determined by the query's access configuration. See [configuration:configure-query-access.adoc](#configuration:configure-query-access.adoc). |
| Data synchronization | GET /{keyspace}/\_blipsync                                             | Pull requires read access per collection. Push requires both read and write access per collection.                                                                                            |
| Administrative tasks | /\_replicate, /\_active\_tasks                                         | Requires the replicate or admin role.                                                                                                                                                         |

> [!NOTE]
> Unauthorized requests and requests targeting keyspaces that do not exist both return `403 Forbidden`. This prevents users from discovering keyspaces they are not authorized to access.

## [](#backwards-compatibility)Backwards Compatibility

If `enable_user_access_control` is not set, or is set to `false`, Couchbase Edge Server behaves as in previous releases. All configured users have unrestricted read and write access to all collections. Existing deployments are not affected by upgrading to {version}.

## [](#see-also)See Also

* [configuration:configure-access-control.adoc](#configuration:configure-access-control.adoc)
* [configuration:configure-query-access.adoc](#configuration:configure-query-access.adoc)
* [Authentication](../configuration/authentication.md)