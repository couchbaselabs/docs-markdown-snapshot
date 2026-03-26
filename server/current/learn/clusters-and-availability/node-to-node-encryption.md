---
title: Node-to-Node Encryption
description: Network traffic between the individual nodes of a Couchbase-Server
  cluster can be encrypted, in order to optimize cluster-internal security.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/learn/pages/clusters-and-availability/node-to-node-encryption.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:learn:clusters-and-availability/node-to-node-encryption.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/learn/clusters-and-availability/node-to-node-encryption.html)

# Node-to-Node Encryption

Network traffic between the individual nodes of a Couchbase-Server cluster can be encrypted, in order to optimize cluster-internal security.

## [](#node-to-node-encryption)Node-to-Node Encryption

Couchbase Server supports _node-to-node encryption_, whereby network traffic between the individual nodes of a cluster is encrypted, in order to optimize cluster-internal security.

Node-to-node encryption is supported for _all_ Couchbase services.

Node-to-node encryption can be established on the following levels:

* _Control_. Cluster-management information passed between nodes by the Cluster Manager and related low-level processes is encrypted. However, the data that is passed between nodes by Couchbase Services continues to be passed in the clear. When node-to-node encryption is first enabled, this is the default.
* _All_. Both cluster-management information and data is passed in encrypted form. Node-to-node encryption can be supported by means of either the Couchbase-provided certificates with which nodes are protected by default; or certificates installed by the administrator.
* _Strict_. This means _All_ with only encrypted communication permitted between nodes and between the cluster and external clients. Note, however, that after _Strict_ has been specified, communication that occurs entirely on a single node using the _loopback_ interface (whereby the machine is identified as either `::1` or `127.0.0.1`) is still permitted in non-encrypted form.  
Applying _Strict_ as the `clusterEncryptionLevel` has a number of significant consequences, which should be fully understood before proceeding. See [Enforcing TLS](../../rest-api/rest-setting-security.md#enforcing-tls).

For practical steps towards set-up, see [Manage Node-to-Node Encryption](../../manage/manage-nodes/apply-node-to-node-encryption.md).

### [](#using-node-to-node-encryption)Using Node-to-Node Encryption

Node-to-node encryption is disabled by default. Note that auto-failover must be switched off both for a change to be made to the cluster's address-family, and for encryption to be enabled or disabled: auto-failover can be switched back on after the necessary changes have been made. (This requirement prevents nodes that are undergoing changes from being determined unresponsive during the process, and unnecessarily failed over.)

Note also that all Eventing functions must be _paused_ before node-to-node encryption for the cluster is enabled, disabled, or is established at a new level: this prevents loss of mutations. All paused Eventing functions should then be _resumed_, once changes to node-to-node encryption are complete. For information, see [eventing-function-setup](../../cli/cbcli/couchbase-cli-eventing-function-setup.md).

Node-to-node encryption is managed by means of the Couchbase CLI. The typical sequence of commands and other activities is summarized below.

1. Change address family. Both IPV4 and IPV6 addresses are supported: one or the other must be selected. The selected setting is applied to every node in the cluster. The address family is changed by means of the [ip-family](../../cli/cbcli/couchbase-cli-ip-family.md) CLI command.
2. Pause all Eventing functions.
3. Enable cluster encryption. Cluster encryption must be specifically enabled: by default, it is disabled. To enable or disable cluster encryption, or to determine the current setting, use the [node-to-node-encryption](../../cli/cbcli/couchbase-cli-node-to-node-encryption.md) CLI command.
4. Establish cluster encryption-level. This determines whether only cluster-management information or both cluster-management information and data will be passed in encrypted form: these are respectively the _control_ and _all_ encryption levels. Use the [setting-security](../../cli/cbcli/couchbase-cli-setting-security.md) CLI command to specify or to get the current setting.
5. Resume all previously paused Eventing functions.
6. If required, re-enable auto-failover.

For a more detailed account of this sequence, see [Manage Node-to-Node Encryption](../../manage/manage-nodes/apply-node-to-node-encryption.md).

### [](#certificate-rotation-and-node-to-node-encryption)Certificate Management and Node-to-Node Encryption

Prior to Couchbase Server Version 7.1, node-to-node encryption, which is managed by means of the Couchbase CLI, needed to be _disabled_ before management of either _root_ or _intermediate_ certificates could be performed. This restriction is lifted in version 7.1: therefore, root and intermediate certificates _can_ now be managed while node-to-node encryption is enabled.