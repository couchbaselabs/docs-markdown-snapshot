[View original HTML](/server/7.2/install/install-ports.html)

> Couchbase Server uses multiple TCP ports to facilitate communication between server components, as well as with Couchbase clients. These ports must be open for Couchbase Server to operate correctly. 

## [](#ports-overview)Ports Overview

This page describes the TCP ports that are used by Couchbase Server for network communication. Some ports, such as those used for cluster management, are required to be open on every node because they are essential to how Couchbase Server communicates with itself. Other ports are used by individual [Couchbase Services](../learn/services-and-indexes/services/services.md), and are only required to be open on the nodes where those services are running.

Couchbase Server uses a default set of port numbers for all ports that it requires. The [Couchbase Cluster Manager](../learn/clusters-and-availability/cluster-manager.md) on each node is responsible for port management, and will open and close these ports on the host as necessary, as well as automatically switch to using encrypted ports if the cluster is configured to use TLS. Most port numbers can be [remapped](#map-custom-ports) to fit the requirements of your network environment, but some port numbers cannot be changed.

|  | If other software on the same host is using any of the ports that are required by Couchbase Server, then Couchbase Server will not function properly and may fail to start. Refer to [Port Availability](#port-availability) below. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#ephemeral-ports)Ephemeral Ports

An _ephemeral_ port is one temporarily allocated by a server’s operating system, as the source for an outgoing communication. Each operating system provides a default range of port numbers that can be assigned to ephemeral ports, when necessary. For Linux distributions, the typical range is 32768-61000\. Couchbase Server relies on the _full_ default range provided by each operating system: therefore, the default range should _not_ be reduced by the administrator; since the resulting lack of ephemeral ports may result in outgoing communications using _well-known_ ports instead (for example, _8091_); thereby preventing Couchbase-Server processes from binding to the well-known ports to which they are assigned.

### [](#couchbase-server-communication-paths)Couchbase Server Communication Paths

Couchbase Server components and services connect to each port over one or more _communication paths_. These paths are defined as:

* _Node-local_: A Couchbase service running on a node connects to the port on localhost, and communication happens entirely within the node itself.
* _Node-to-node_: A Couchbase service connects to the port on other nodes in the cluster.
* _Client-to-node_: A Couchbase client, such as an application using the Couchbase SDK, connects to the port on the node that it requires access to.
* _XDCR (cluster-to-cluster)_: A source node connects to the port on a destination node of another cluster as part of an [XDCR replication stream](../manage/manage-xdcr/prepare-for-xdcr.md). (This is very similar to the client-to-node communication path.)  
As of Couchbase Server Version 7.0, the XDCR protocol Version 2 (_XMEM_), which uses the Memcached Binary protocol, is the only XDCR protocol supported. Version 1 (_CAPI_), which used the REST protocol, is no longer supported. Refer to [XDCR Advanced Settings](../xdcr-reference/xdcr-advanced-settings.md) for information about the XDCR protocol version and other advanced settings.
* _cbbackupmgr_ (backup client): This Couchbase backup client connects to the cluster services using the ports for the service.

Each communication path used by a required port must remain open and unblocked by firewalls or other such mechanisms.

### [](#port-availability)Port Availability

Neither the [Cluster Manager](../learn/clusters-and-availability/cluster-manager.md) nor any of the Couchbase [Services](../learn/services-and-indexes/services/services.md) will start if unable to listen on all required ports. Note that the cluster manager and all services attempt to bind to required ports using the IP address family that the Couchbase Server cluster is configured to use (see [Manage Address Families](../manage/manage-nodes/manage-address-families.md)). Therefore, if the Couchbase Server cluster is configured to use IPv6, the cluster manager and all services attempt to bind to required ports using IPv6; and if the cluster is configured to use IPv4, the cluster manager and all services attempt to bind to required ports using IPv4\. If the cluster manager or service is unable to bind to one or more required ports using the configured IP address family, it will not start.

Refer to the [Detailed Port Description](#detailed-port-description), below, for a list of the ports required by each service.

## [](#ports-listed-by-communication-path)Ports Listed by Communication Path

The following table lists all port numbers, grouped by category of communication path.

__Table 1\. All Couchbase Server Ports, Listed by Communication Path__
| Communication Path                    | Default Ports                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| _Node-local only_                     | **Unencrypted**: 9119, 9998, 11213, 21200, 21300 **Encrypted**: 21250 \[[1](#%5Ffootnotedef%5F1 "View footnote.")\], 21350 \[[2](#%5Ffootnotedef%5F2 "View footnote.")\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| _Node-to-node_                        | **Unencrypted**: 4369, 8091-8094, 9100-9105, 9110-9118, 9120-9122, 9130, 9999, 11209-11210, 21100 **Encrypted**: 9999, 9124, 11206, 11207, 18091-18094, 19102, 19130, 21150                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| _Client-to-node_                      | **Unencrypted**: 8091-8097, 9123, 9140 \[[3](#%5Ffootnotedef%5F3 "View footnote.")\], 11210, 11280 **Encrypted**: 11207, 18091-18095, 18096, 18097                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| _XDCR (cluster-to-cluster)_           | Version 2 (XMEM) **Unencrypted**: 8091, 8092, 11210 **Encrypted**: 11207, 18091, 18092 If enforcing TLS encryption, these ports may be blocked outside of a Couchbase Server cluster but need to remain open between nodes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| _cbbackupmgr (backup/restore client)_ | **Unencrypted**: 8091-8096, 9102, 11210 **Encrypted**: 11207, 18091-18096, 19102 cbbackupmgr, the backup client, connects to the Couchbase Server using the ports listed above. You can find detailed information about the server ports in the [Detailed Port Description](#detailed-port-description). Below is a summary of the services cbbackupmgr is accessing via the ports. rest\_port / ssl\_rest\_port 8091 / 18091 (Cluster admin/management) cbas\_http\_port/ cbas\_ssl\_port 8095 / 18095 (Analytics service) memcached\_port / memcached\_ssl\_port 11210 / 11207 (Data service) eventing\_http\_port / eventing\_ssl\_port 8096/18096 (Eventing service) indexer\_http\_port / indexer\_https\_port 9102 / 19102 (GSI Indexes) query\_port / ssl\_query\_port 8093 / 18093 (Query) fts\_http\_port / fts\_ssl\_port 8094 / 18094 (Search) capi\_port / ssl\_capi\_port 8092 / 18092 (Views) |

|  | Certain support and diagnostic requests may run against ports other than the administration port (8091). These are expected to execute locally on a node and so do not require external access. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#detailed-port-description)Detailed Port Description

The following table contains a detailed description of each port used by Couchbase Server.

__Table 2\. All Couchbase Server Ports, Listed by Service__
| Port name                                                                 | Default port number(un / encrypted) | Description                                                                                                                               | Node-to-node | Client-to-node | XDCR (cluster-to-cluster) |
| ------------------------------------------------------------------------- | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------- | ------------------------- |
| epmd \[[4](#%5Ffootnotedef%5F4 "View footnote.")\]                        | 4369                                | Erlang Port Mapper Daemon                                                                                                                 | Yes          | No             | No                        |
| rest\_port / ssl\_rest\_port                                              | 8091 / 18091                        | Cluster administration REST/HTTP traffic, including Couchbase Web Console                                                                 | Yes          | Yes            | Version 2                 |
| capi\_port / ssl\_capi\_port                                              | 8092 / 18092                        | Views and XDCR access                                                                                                                     | Yes          | Yes            | Version 2                 |
| query\_port / ssl\_query\_port                                            | 8093 / 18093                        | Query service REST/HTTP traffic                                                                                                           | Yes          | Yes            | No                        |
| fts\_http\_port / fts\_ssl\_port                                          | 8094 / 18094                        | Search Service REST/HTTP traffic                                                                                                          | Yes          | Yes            | No                        |
| cbas\_http\_port / cbas\_ssl\_port                                        | 8095 / 18095                        | Analytics service REST/HTTP traffic                                                                                                       | No           | Yes            | No                        |
| eventing\_http\_port / eventing\_ssl\_port                                | 8096 / 18096                        | Eventing service REST/HTTP traffic                                                                                                        | No           | Yes            | No                        |
| backup\_http\_port / backup\_ssl\_port                                    | 8097 / 18097                        | Backup service REST/HTTP traffic                                                                                                          | No           | Yes            | No                        |
| indexer\_admin\_port                                                      | 9100                                | Indexer service                                                                                                                           | Yes          | No             | No                        |
| indexer\_scan\_port                                                       | 9101                                | Indexer service                                                                                                                           | Yes          | No             | No                        |
| indexer\_http\_port                                                       | 9102                                | Indexer service                                                                                                                           | Yes          | No             | No                        |
| indexer\_https\_port                                                      | 19102                               | Indexer service                                                                                                                           | Yes          | No             | No                        |
| indexer\_stinit\_port                                                     | 9103                                | Indexer service                                                                                                                           | Yes          | No             | No                        |
| indexer\_stcatchup\_port                                                  | 9104                                | Indexer service                                                                                                                           | Yes          | No             | No                        |
| indexer\_stmaint\_port                                                    | 9105                                | Indexer service                                                                                                                           | Yes          | No             | No                        |
| cbas\_admin\_port                                                         | 9110                                | Analytics service                                                                                                                         | Yes          | No             | No                        |
| cbas\_cc\_http\_port                                                      | 9111                                | Analytics service                                                                                                                         | Yes          | No             | No                        |
| cbas\_cc\_cluster\_port                                                   | 9112                                | Analytics service                                                                                                                         | Yes          | No             | No                        |
| cbas\_cc\_client\_port                                                    | 9113                                | Analytics service                                                                                                                         | Yes          | No             | No                        |
| cbas\_console\_port                                                       | 9114                                | Analytics service                                                                                                                         | Yes          | No             | No                        |
| cbas\_cluster\_port                                                       | 9115                                | Analytics service                                                                                                                         | Yes          | No             | No                        |
| cbas\_data\_port                                                          | 9116                                | Analytics service                                                                                                                         | Yes          | No             | No                        |
| cbas\_result\_port                                                        | 9117                                | Analytics service                                                                                                                         | Yes          | No             | No                        |
| cbas\_messaging\_port                                                     | 9118                                | Analytics service                                                                                                                         | Yes          | No             | No                        |
| cbas\_auth\_port                                                          | 9122                                | Analytics service (node-local only)                                                                                                       | No           | No             | No                        |
| cbas\_replication\_port                                                   | 9120                                | Analytics service                                                                                                                         | Yes          | No             | No                        |
| cbas\_metadata\_port                                                      | 9121                                | Analytics service (node-local only)                                                                                                       | Yes          | No             | No                        |
| cbas\_metadata\_callback\_port                                            | 9119                                | Analytics service (node-local only)                                                                                                       | Yes          | No             | No                        |
| prometheus\_http\_port                                                    | 9123                                | Cluster management traffic and communication                                                                                              | No           | Yes            | No                        |
| backup\_grpc\_port                                                        | 9124                                | Backup Service gRPC                                                                                                                       | Yes          | No             | No                        |
| fts\_grpc\_port / fts\_grpc\_ssl\_port                                    | 9130 / 19130                        | Search Service gRPC port used for [scatter-gather](../learn/services-and-indexes/services/search-service.md) operations between FTS nodes | Yes          | No             | No                        |
| eventing\_debug\_port \[[3](#%5Ffootnotedef%5F3 "View footnote.")\]       | 9140                                | Eventing Service Debugger                                                                                                                 | No           | Yes            | No                        |
| xdcr\_rest\_port                                                          | 9998                                | XDCR REST port (node-local only)                                                                                                          | No           | No             | No                        |
| projector\_port                                                           | 9999 / 9999                         | Indexer service                                                                                                                           | Yes          | No             | No                        |
| memcached\_dedicated\_port / memcached\_dedicated\_ssl\_port              | 11209 / 11206                       | Data Service and ns\_server. Used for important control-commands; e.g. creation of buckets and vBuckets, and compaction.                  | Yes          | No             | No                        |
| memcached\_port / memcached\_ssl\_port                                    | 11210 / 11207                       | Data Service                                                                                                                              | Yes          | Yes            | Version 2                 |
| memcached\_prometheus                                                     | 11280                               | Data Service                                                                                                                              | No           | Yes            | No                        |
| Cluster Management Exchange                                               | 21100 / 21150                       | Cluster management traffic and communication                                                                                              | Yes          | No             | No                        |
| Cluster Management Exchange \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] | 21200 / 21250                       | Cluster management traffic and communication (node-local only)                                                                            | No           | No             | No                        |
| Cluster Management Exchange \[[2](#%5Ffootnotedef%5F2 "View footnote.")\] | 21300 / 21350                       | Cluster management traffic and communication (node-local only)                                                                            | No           | No             | No                        |

## [](#map-custom-ports)Custom Port Mapping

Most, but not all, port numbers used by Couchbase Server can be remapped from their defaults to fit the requirements of your network environment. Refer to [Table 2](#table-ports-detailed) for details about default ports and whether or not they can be remapped.

Changing the port mappings will require a reset and reconfiguration of any Couchbase Server node.

|  | Changing port mappings should only be done at the time of initial node/cluster setup as the required reset and reconfiguration will also purge all data on the node. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

To Change Port Mapping

1. [Install Couchbase Server](install-intro.md).
2. [Stop the Couchbase Server service](startup-shutdown.md).
3. For most ports, you’ll need to edit the Couchbase Server _static\_config_ file. (This will be wherever you put the path to _/couchbase/etc/couchbase/static\_config_ in multi-node installations.)  
```console  
vi /opt/couchbase/etc/couchbase/static_config  
```  
If you’re remapping the CAPI port (8092 / 18092) you’ll need to edit the _/opt/couchbase/etc/couchdb/default.d/capi.ini_ file and replace 8092 with the new port number.
4. Add each custom port map entry on its own line, using the following format (enclosed in braces and terminated by a period):  
```console  
{port-name, port-number}.  
```  
For example, to change the REST API port from 8091 to 9000, you would add the following line:  
```console  
{rest_port, 9000}.  
```  
Once you’ve added all of your custom port mappings, save the file and close your text editor.
5. If Couchbase Server was previously configured, you’ll need to delete the _/opt/couchbase/var/lib/couchbase/config/config.dat_ file and files in the _/opt/couchbase/var/lib/couchbase/config/chronicle/_ directory to remove the old configuration.  
```console  
rm -rf /opt/couchbase/var/lib/couchbase/config/config.dat  
rm -rf /opt/couchbase/var/lib/couchbase/config/chronicle/*  
```
6. [Start Couchbase Server](startup-shutdown.md).

Any ports not given a custom mapping in the _static\_config_ file will continue to be assigned their defaults, which are listed in [Table 2](#table-ports-detailed).

---

[1](#%5Ffootnoteref%5F1). The Cluster Management Exchange encrypted port 21250 is not currently used, but is reserved for future use. 

[2](#%5Ffootnoteref%5F2). The Cluster Management Exchange encrypted port 21350 is not currently used, but is reserved for future use. 

[3](#%5Ffootnoteref%5F3). The Eventing Service Debugger port `eventing_debug_port` (9140) is an internal port and is not supported for external access outside of the cluster. You should only use this port in your development environments. 

[4](#%5Ffootnoteref%5F4). This port cannot be remapped.