---
title: REST API Access
description: Sync Gateway REST API Access
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/rest-api-access.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@sync-gateway::rest-api-access.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/rest-api-access.html)

# REST API Access

> Sync Gateway REST API Access  
> Shows how to access Sync Gateway APIs

Related _REST API_ topics: [Public REST API](../current/rest-api/rest-api.md) | [Admin REST API](../current/rest-api/rest-api-admin.md) | [Metrics REST API](../current/rest-api/rest-api-metrics.md) | [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

Sync Gateway REST APIs are accessed on different TCP ports. This makes it easy to expose the Public REST API and Metrics REST API (if activated) to endpoints while keeping the Admin REST API secure behind your firewall.

If you want to change the ports, you can do that in the configuration file, so:

* To change the Public REST API port, set the `interface` property in the configuration file.
* To change the Metric REST API port, set the `metricsInterface` property in the configuration file.
* To change the Admin REST API port, set the `adminInterface` property in the configuration file.

The value of the property is a string consisting of a colon followed by a port number (for example, `:4985`). You can also include a host name or numeric IP address before the colon to bind only to that network interface.

As a useful special case, the IP address 127.0.0.1 binds to the loopback interface, making the port unreachable from any other host. This is the default setting for the admin interface.

Network Port Requirements

Sync Gateway uses specific ports for communication with the outside world, mostly Couchbase Lite databases replicating to and from Sync Gateway — see [Table 1](#network-ports) for details.

__Table 1\. Sync Gateway Network Port Requirements__
| Port | Description                                                                                                                                                                                                                                                                                                                                                                                 |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 4984 | Public port. External HTTP port used for replication with Couchbase Lite databases and other applications accessing the REST API on the Internet. The Public REST API is used for client replication. The default port for the Public REST API is 4984.                                                                                                                                     |
| 4985 | Admin port. Internal HTTP port for unrestricted access to the database and to run administrative tasks. The Admin REST API is used to administer user accounts and roles. It can also be used to look at the contents of databases in superuser mode. The default port for the Admin REST API is 4985\. By default, the Admin REST API is reachable only from localhost for safety reasons. |
| 4986 | Metrics port. By default 4986 is the internal HTTP port designated for providing access to Sync Gateway's Metrics REST API. Like the admin port, it is bound to 127.0.0.1 by default. The Metrics REST API returns Sync Gateway metrics, in JSON and-or Prometheus-compatible formats, for performance monitoring and-or diagnostic purposes,                                               |

## [](#related-content)Related Content

###### [](#)

API Topics

* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-2)

Reference

* [Configuration Properties](../current/configuration/configuration-properties-legacy.md)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)