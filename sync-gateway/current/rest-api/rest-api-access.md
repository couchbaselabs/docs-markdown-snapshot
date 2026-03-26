---
title: Secure API Access
description: Sync Gateway REST API Access
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/rest-api/pages/rest-api-access.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:sync-gateway:rest-api:rest-api-access.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/rest-api/rest-api-access.html)

# Secure API Access

> Sync Gateway REST API Access  
> Shows how to access Sync Gateway APIs

Related _REST API_ topics: [Public REST API](rest-api.md) | [Admin REST API](rest-api-admin.md) | [Metrics REST API](rest-api-metrics.md)

## [](#overview)Overview

Sync Gateway provides secure access to its REST APIs, namely the:

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md) — for the administration and configuration of sync gateway
* [Metrics REST API](rest-api-metrics.md) — for the monitoring of sync gateway performance metrics

Each REST API is accessed through a different, [user-specifiable](#lbl-port-cfg), TCP port. This makes it easy to control their physical exposure, perhaps to keep the Admin REST API secure behind your firewall.

Sync gateway 4.0.0 brings additional optional but default layers of security through [enforcing TLS encryption](../security/secure-sgw-access.md) for all API traffic and Couchbase Server Role-Based Access Control (RBAC) authorization and authentication for all [Admin and Metrics API users](#lbl-secure-users).

RBAC user authentication enables [Secure Administration](#lbl-secure-users) of sync gateway clusters. This is critical in cloud native deployments. The use of different RBAC roles for uses also provides secure and fine-grained access control — for more on the available roles see [Available Server RBAC Roles on Sync Gateway](#lbl-rbac-roles)

## [](#tls)TLS

TLS is enforced by default for all Couchbase Server connections in 3.0\. For more on TLS, see: [enforcing TLS encryption](../security/secure-sgw-access.md).

## [](#lbl-secure-users)Secure Administration

Secure Administration is **on** by default.

In order to submit Admin or Metrics REST API requests you should create specific Couchbase Server users for that purpose. You will then provide a valid set of Couchbase Server credentials for these RBAC-users in each API request.

Authenticated users will have access to Admin and-or Metrics API functionality, application data and configuration settings.

## [](#lbl-rbac-roles)Available Server RBAC Roles on Sync Gateway

Couchbase Server makes a number of RBAC roles available for Sync Gateway use. Each user's access-level will depend on its allocated role.

The currently available roles will vary depending on the Couchbase Server release version — see: [Table 1](#tbl-ee-svr-sgw-roles).  

When referencing the [Admin REST API](rest-api-admin.md) you will see that each endpoint states the role (or roles) able to use it — you can find a cross-reference of endpoints and required roles in [RBAC Role - Endpoint Cross-Reference](rest-api-access-rbac-roles.md).

Note that the only role available for community-edition users is the **Full Admin** role.

__Table 1\. Sync gateway role availability by release__
| Role                               | Capability                                                                                                                       | 7.1.0+                     | 7.0.2 DP[1](#more-on-developer-previews) | 6.1 - 7.0                  |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | ---------------------------------------- | -------------------------- |
| Sync Gateway Architect             | Can manage Sync Gateway databases and users, and access Sync Gateway's metrics endpoint. This user cannot read application data. | ![yes](../_images/yes.png) | ![yes](../_images/yes.png)               | ![no](../_images/no.png)   |
| Sync Gateway Application           | Can manage Sync Gateway users and roles, and read and write application data through Sync Gateway.                               | ![yes](../_images/yes.png) | ![yes](../_images/yes.png)               | ![no](../_images/no.png)   |
| Sync Gateway Application Read Only | Can read Sync Gateway users and roles, and read application data through Sync Gateway.                                           | ![yes](../_images/yes.png) | ![yes](../_images/yes.png)               | ![no](../_images/no.png)   |
| Sync Gateway Replicator            | Can manage Inter-Sync Gateway Replications.This user cannot read application data.                                               | ![yes](../_images/yes.png) | ![yes](../_images/yes.png)               | ![no](../_images/no.png)   |
| Sync Gateway Dev Ops               | Can manage Sync Gateway node-level configuration, and access Sync Gateway's /metrics endpoint for Prometheus integration.        | ![yes](../_images/yes.png) | ![yes](../_images/yes.png)               | ![no](../_images/no.png)   |
| Sync-Gateway Role                  | Can access DB / bucket scoped operations                                                                                         | ![no](../_images/no.png)   | ![no](../_images/no.png)                 | ![yes](../_images/yes.png) |
| Application Access                 | Can access DB / bucket scoped operations                                                                                         | ![no](../_images/no.png)   | ![no](../_images/no.png)                 | ![yes](../_images/yes.png) |
| Bucket Full Access                 | Can access DB / bucket scoped operations                                                                                         | ![no](../_images/no.png)   | ![no](../_images/no.png)                 | ![yes](../_images/yes.png) |
| Full Admin                         | Can access all operations                                                                                                        | ![no](../_images/no.png)   | ![no](../_images/no.png)                 | ![yes](../_images/yes.png) |

For more information on older, end-of-life versions, see [legacy version role availability](#3.0@rest-api-access.adoc).

1For more information on Developer Previews, see [Developer Preview Mode and Features](../../../server/current/developer-preview/preview-mode.md)

For more on creating Couchbase Server users see the Couchbase Server content here [Server — Manage Users and Roles](../../../server/current/manage/manage-security/manage-users-and-roles.md).

## [](#lbl-optout)Secure Administration Opt-out

You can choose to disable Secure Administration by using these bootstrap configuration settings or CLI flags:

* [Bootstrap Configuration](../configuration/configuration-schema-bootstrap.md)

  * [api.api.admin\_interface\_authentication](../configuration/configuration-schema-bootstrap.md#api-admin%5Finterface%5Fauthentication)
  * [api.metrics\_interface\_authentication](../configuration/configuration-schema-bootstrap.md#api-metrics%5Finterface%5Fauthentication)
* [Command Line Options](../deploy/command-line-options.md)

  * `-admin_interface_authentication=false`.
  * `-metrics_interface_authentication=false`.

## [](#ldap-authentication)LDAP Authentication

Authentication against an external system such as LDAP is possible through Couchbase Server.

However, this can increase the risk of performance and or connection issues — for more on this see the Couchbase Server documentation [LDAP Users and Authentication](../../../server/current/learn/security/authentication-domains.md#ldap-users-and-applications)

## [](#lbl-port-cfg)Port Configuration

You can change the ports used for any of the interface types by editing its bootstrap configuration property, for example, [api.admin\_interface](../configuration/configuration-schema-bootstrap.md#api-admin%5Finterface) — as shown in [Example 1](#ex-port-cfg) — and restarting the sync gateway node. The default ports are shown in [Table 2](#network-ports).

Example 1\. Configuring ports

* Admin
* Metrics
* Public

```json
  api: {
    "admin_interface": ":4985", (1)
    "admin_interface_authentication": true,

    // ... additional group properties

  },
```

```json
  api: {
    "metrics_interface": ":4986", (1)
    "metrics_interface_authentication": true,

    // ... additional group properties

  },
```

```json
  api: {
    "public_interface": ":4984", (1)

    // ... additional group properties

  },
```

| **1** | The value of the _interface_ property is a string consisting of a colon followed by a port number (for example, :4985). You can also include a host name or numeric IP address before the colon to bind only to that network interface. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

As a useful special case, the IP address 127.0.0.1 binds to the loopback interface, making the port unreachable from any other host. This is the default setting for the admin interface.

Network Port Requirements

Sync Gateway uses specific ports for communication with the outside world, mostly Couchbase Lite databases replicating to and from Sync Gateway — see [Table 2](#network-ports) for details.

__Table 2\. Sync Gateway Network Port Requirements__
| Port | Description                                                                                                                                                                                                                                                                                                                                                                                 |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 4984 | Public port. External HTTP port used for replication with Couchbase Lite databases and other applications accessing the REST API on the Internet. The Public REST API is used for client replication. The default port for the Public REST API is 4984.                                                                                                                                     |
| 4985 | Admin port. Internal HTTP port for unrestricted access to the database and to run administrative tasks. The Admin REST API is used to administer user accounts and roles. It can also be used to look at the contents of databases in superuser mode. The default port for the Admin REST API is 4985\. By default, the Admin REST API is reachable only from localhost for safety reasons. |
| 4986 | Metrics port. By default 4986 is the internal HTTP port designated for providing access to Sync Gateway's Metrics REST API. Like the admin port, it is bound to 127.0.0.1 by default. The Metrics REST API returns Sync Gateway metrics, in JSON and-or Prometheus-compatible formats, for performance monitoring and-or diagnostic purposes,                                               |

For more on configuration see [api.admin\_interface](../configuration/configuration-schema-bootstrap.md#api-admin%5Finterface)

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](../configuration/configuration-schema-bootstrap.md)
* [Database](../configuration/configuration-schema-database.md)
* [Database Security](../configuration/configuration-schema-db-security.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Import Filter](../configuration/configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](../configuration/configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)