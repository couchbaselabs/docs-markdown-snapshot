[View original HTML](/enterprise-analytics/2.0/install/cb-enterprise-analytics-ports.html)

> Enterprise Analytics uses multiple TCP ports for communication between components and with Couchbase clients. You must leave these ports open to use Enterprise Analytics. 

## [](#ports-listed-by-communication-path)Ports Listed by Communication Path

The following table lists all port numbers, grouped by category of communication path.

__Table 1\. All Enterprise Analytics Ports, Listed by Communication Path__
| Communication Path | Default Ports                                                                                                                                               |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Node-local only    | **Unencrypted**: 9119, 21200, 21300 **Encrypted**: 21250 \[[1](#%5Ffootnotedef%5F1 "View footnote.")\], 21350 \[[2](#%5Ffootnotedef%5F2 "View footnote.")\] |
| Node-to-node       | **Unencrypted**: 4369, 8091, 9110-9118, 9120, 11209-11210, 21100 **Encrypted**: 11206, 11207, 18091, 21150                                                  |
| Client-to-node     | **Unencrypted**: 8091, 8095, 9123, 11210, 11280 **Encrypted**: 18091, 18095, 11207                                                                          |

|  | Certain support and diagnostic requests might run against ports other than the administration port (8091). These requests execute locally on a node and do not require external access. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#detailed-port-description)Detailed Port Description

The following table contains a detailed description of each port used by Enterprise Analytics.

__Table 2\. All Enterprise Analytics Ports, Listed by Application__
| Port name                                                                 | Default port number(unencrypted / encrypted) | Description                                                                          | Node-to-node | Client-to-node |
| ------------------------------------------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------ | ------------ | -------------- |
| epmd \[[3](#%5Ffootnotedef%5F3 "View footnote.")\]                        | 4369                                         | Erlang Port Mapper Daemon                                                            | Yes          | No             |
| rest\_port / ssl\_rest\_port                                              | 8091 / 18091                                 | Cluster administration REST/HTTP traffic, including Enterprise Analytics Web Console | Yes          | Yes            |
| cbas\_http\_port / cbas\_ssl\_port                                        | 8095 / 18095                                 | Analytics Service REST/HTTP traffic                                                  | No           | Yes            |
| cbas\_admin\_port                                                         | 9110                                         | Analytics Service                                                                    | Yes          | No             |
| cbas\_cc\_http\_port                                                      | 9111                                         | Analytics Service                                                                    | Yes          | No             |
| cbas\_cc\_cluster\_port                                                   | 9112                                         | Analytics Service                                                                    | Yes          | No             |
| cbas\_cc\_client\_port                                                    | 9113                                         | Analytics Service                                                                    | Yes          | No             |
| cbas\_cluster\_port                                                       | 9115                                         | Analytics Service                                                                    | Yes          | No             |
| cbas\_data\_port                                                          | 9116                                         | Analytics Service                                                                    | Yes          | No             |
| cbas\_result\_port                                                        | 9117                                         | Analytics Service                                                                    | Yes          | No             |
| cbas\_messaging\_port                                                     | 9118                                         | Analytics Service                                                                    | Yes          | No             |
| cbas\_auth\_port                                                          | 9119                                         | Analytics Service (node-local only)                                                  | No           | No             |
| cbas\_replication\_port                                                   | 9120                                         | Analytics Service                                                                    | Yes          | No             |
| prometheus\_http\_port                                                    | 9123                                         | Cluster management traffic and communication                                         | No           | Yes            |
| memcached\_dedicated\_port / memcached\_dedicated\_ssl\_port              | 11209 / 11206                                | Memcached and ns\_server. Used for important control-commands                        | Yes          | No             |
| memcached\_port / memcached\_ssl\_port                                    | 11210 / 11207                                | Memcached (SDK Cluster Topology & Auditing)                                          | Yes          | Yes            |
| memcached\_prometheus                                                     | 11280                                        | Memcached                                                                            | No           | Yes            |
| Cluster Management Exchange                                               | 21100 / 21150                                | Cluster management traffic and communication                                         | Yes          | No             |
| Cluster Management Exchange \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] | 21200 / 21250                                | Cluster management traffic and communication (node-local only)                       | No           | No             |
| Cluster Management Exchange \[[2](#%5Ffootnotedef%5F2 "View footnote.")\] | 21300 / 21350                                | Cluster management traffic and communication (node-local only)                       | No           | No             |

## [](#map-custom-ports)Custom Port Mapping

Most, but not all, port numbers used by Enterprise Analytics can be remapped from their defaults to fit the requirements of your network environment. See [Table 2](#table-ports-detailed) for details about default ports and whether or not they can be remapped.

Changing the port mappings requires a reset and reconfiguration of any Enterprise Analytics node.

|  | You should change port mappings at the time of initial node and cluster setup. The required reset and reconfiguration also deletes all data on the node. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#change-a-port-mapping)Change a Port Mapping

1. [Install Enterprise Analytics](introduction-linux-installation.md).
2. [Stop Enterprise Analytics](start-stop-cb-enterprise-analytics.md).
3. For most ports, you’ll need to edit the Enterprise Analytics `_staticconfig_` file. This file will be wherever you put the path to `_/opt/enterprise-analytics/etc/couchbase/staticconfig_` in a multi-node installation.  
```txt  
vi /opt/enterprise-analytics/etc/couchbase/static_config  
```  
If you’re remapping the CAPI port (8092 / 18092) you’ll need to edit the `_/opt/enterprise-analytics/etc/couchdb/default.d/capi.ini_` file and replace 8092 with the new port number.
4. Add each custom port map entry on its own line, using the following format. Enclose the port name and number in braces (`{}`) and end each entry with a period (`.`):  
```txt  
{port-name, port-number}.  
```  
For example, to change the REST API port from 8091 to 9000, you would add the following line:  
```txt  
{rest_port, 9000}.  
```  
After you have added all of your custom port mappings, save the file and close your text editor.
5. If you already configured Enterprise Analytics, you’ll need to delete the `_/opt/enterprise-analytics/var/lib/couchbase/config/config.dat_` file and files in the `_/opt/enterprise-analytics/var/lib/couchbase/config/chronicle/_` directory to remove the old configuration.  
```txt  
rm -rf /opt/enterprise-analytics/var/lib/couchbase/config/config.dat  
rm -rf /opt/enterprise-analytics/var/lib/couchbase/config/chronicle/*  
```
6. [Start Enterprise Analytics](start-stop-cb-enterprise-analytics.md).

If you do not give a custom mapping to ports in the `_staticconfig_` file, Enterprise Analytics automatically assigns defaults. See the default port mappings in [Table 2](#table-ports-detailed).

---

[1](#%5Ffootnoteref%5F1). The Cluster Management Exchange encrypted port 21250 is reserved for future use. 

[2](#%5Ffootnoteref%5F2). The Cluster Management Exchange encrypted port 21350 is reserved for future use. 

[3](#%5Ffootnoteref%5F3). You cannot remap this port.