---
title: Manage Node-to-Node Encryption
description: Network traffic between the individual nodes of an Enterprise
  Analytics cluster can be encrypted, in order to optimize cluster-internal
  security.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/manage/pages/manage-nodes/apply-node-to-node-encryption.adoc
  xref: xref:enterprise-analytics:manage:manage-nodes/apply-node-to-node-encryption.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/manage/manage-nodes/apply-node-to-node-encryption.html)

# Manage Node-to-Node Encryption

> Network traffic between the individual nodes of an Enterprise Analytics cluster can be encrypted, in order to optimize cluster-internal security. 

## [](#understanding-node-to-node-encryption)Understanding Node-to-Node Encryption

Enterprise Analytics supports _node-to-node encryption_, whereby network traffic between the individual nodes of a cluster is encrypted.

Node-to-node encryption is managed by means of the Couchbase CLI. This page provides a sequence of calls, to exemplify how a cluster can be secured by means of node-to-node encryption. For a complete conceptual overview, see [Node-to-Node Encryption](../../../../server/current/learn/clusters-and-availability/nodes.md#node-to-node-encryption).

## [](#set-up-node-to-node-encryption)Set Up Node-to-Node Encryption

The following sequence demonstrates how to set up node-to-node encryption for a cluster, using the Couchbase CLI. The sequence assumes:

* The reader's familiarity with the information provided at [Node-to-Node Encryption](../../../../server/current/learn/clusters-and-availability/nodes.md#node-to-node-encryption).
* A pre-existing cluster of two nodes, `node1-devcluster.com` and `node2-devcluster.com`, both running the latest version of Enterprise Analytics Enterprise Edition.
* Node-to-node encryption initially disabled.
* Auto-failover initially enabled.

Note that node-to-node encryption-enablement can also be performed when a cluster is being created. See [Create a Cluster](create-cluster.md).

Proceed as follows:

1. Turn off auto-failover. Use the `setting-autofailover` CLI command, as follows:  
/opt/enterprise-analytics/bin/couchbase-cli setting-autofailover \
-c http://node1-devcluster.com:8091 \
-u Administrator \
-p password \
--enable-auto-failover 0  
The value of `0` assigned to the `--enable-auto-failover` flag specifies that auto-failover be switched off. If the command is successful, the following output is displayed:  
SUCCESS: Auto-failover settings modified
2. Enable node-to-node encryption for the cluster. Use the `node-to-node-encryption` CLI command:  
/opt/enterprise-analytics/bin/couchbase-cli node-to-node-encryption \
-c http://node1-devcluster.com:8091 \
-u Administrator \
-p password \
--enable  
The `--enable` flag enables node-to-node encryption for the cluster, at the default level of `control`. If the command is successful, the following output is displayed:  
Turned on encryption for node: http://node1-devcluster.com:8091  
Turned on encryption for node: http://node2-devcluster.com:8091  
SUCCESS: Switched cluster encryption on  
The output indicates that encryption has been successfully enabled for each node in the cluster.
3. Establish an appropriate encryption-level for the cluster. This is achieved by the `setting-security` CLI command, specifying the `--cluster-encryption-level` parameter. Its value can be `control`, meaning that server-management information passed between nodes is passed in encrypted form; `all`, meaning that all information passed between nodes, including data handled by services, is passed in encrypted form; or `strict`, meaning `all` with only encrypted communication permitted between nodes and between the cluster and external clients. (Note, however, that after `strict` has been specified, communication that occurs entirely on a single node using the _loopback_ interface — whereby the machine is identified as either `localhost` or `127.0.0.1` — is still permitted in non-encrypted form.)  
For example:  
/opt/enterprise-analytics/bin/couchbase-cli setting-security \
-c http://node1-devcluster.com:8091 \
-u Administrator \
-p password \
--set \
--cluster-encryption-level all  
Passed as the value for the `--cluster-encryption-level` flag, `all` is specified as the new encryption-level for the cluster. If the command is successful, the following output is displayed:  
SUCCESS: Security settings updated
4. Turn on auto-failover. Use the `setting-autofailover` CLI command, as follows:  
/opt/enterprise-analytics/bin/couchbase-cli setting-autofailover \
-c http://node1-devcluster.com:8091 \
-u Administrator \
-p password \
--enable-auto-failover 1 \
--auto-failover-timeout 120 \
--max-failovers 2 \
--can-abort-rebalance 1  
The parameter values specify that auto-failover be enabled with a timeout of 120 seconds; with a maximum of two, sequential automated failovers able to occur, prior to administrator intervention being required, and automatic failovers can abort a rebalance.  
If the command succeeds, and the settings are successfully modified, the following output is displayed:  
SUCCESS: Auto-failover settings modified
5. Confirm that node-to-node encryption is enabled, using the `--get` parameter to `node-to-node-encryption`:  
/opt/enterprise-analytics/bin/couchbase-cli node-to-node-encryption \
-c http://node1-devcluster.com:8091 \
-u Administrator \
-p password \
--get  
If the command is successful, the following output is displayed:  
Node-to-node encryption is enabled
6. Confirm the established encryption-level, using the `--get` parameter to `setting-security`. Note that this call his here piped to the [jq](http://stedolan.github.io/) program, to optimize output-readability:  
/opt/enterprise-analytics/bin/couchbase-cli setting-security \
-c http://node1-devcluster.com:8091 \
-u Administrator \
-p password \
--get | jq '.'  
If successful, the command returns a JSON document that contains the current security settings for the cluster. The first part of the output may be as follows:  
{  
  "disableUIOverHttp": false,  
  "disableUIOverHttps": false,  
  "disableWWWAuthenticate": false,  
  "responseHeaders": [],  
  "tlsMinVersion": "tlsv1.2",  
  "cipherSuites": [],  
  "honorCipherOrder": true,  
  "clusterEncryptionLevel": "all",  
  "allowNonLocalCACertUpload": false,  
...  
These contents include information about the cluster's _UI disablement settings_, _TLS minimum version_, and _ciper suites_ (listed per service). The output also contains the current encryption-level setting, which is shown here as `_all_`.

For information about UI disablement, see [Manage Console Access](../manage-security/manage-console-access.md).

This concludes the sequence of commands.