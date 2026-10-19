---
title: Getting Information on Nodes
description: information about a cluster's individual nodes can be retrieved, by
  means of the REST API.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-node-get-info.adoc
  xref: xref:enterprise-analytics:reference:rest-node-get-info.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-node-get-info.html)

# Getting Information on Nodes

> information about a cluster's individual nodes can be retrieved, by means of the REST API. 

## [](#http-method-and-uri)HTTP Method and URI

GET /pools/nodes

## [](#description)Description

Returns a JSON object containing an array, each of whose members is a node in the cluster. For each node, returned data includes identifiers for the node, a list of installed services, the settings for encryption and address family, memory and hardware information, rebalance status, and URIs to be used in cluster-management.

For data to be returned, the administrator must authenticate with the Full Admin. the Cluster Admin, or the Read-Only Admin role.

## [](#curl-syntax)Curl Syntax

curl -X GET -u <username>:<password>
  http://<ip-address-or-hostname>:8091/pools/nodes

## [](#responses)Responses

Success returns `200 OK`, and a JSON object containing information about the nodes in the cluster. Failure to authenticate returns `401 Unauthorized`. An incorrectly specified URI returns `404 Object Not Found`.

## [](#example)Example

The following example returns information about the nodes of a two-node cluster.

> [!NOTE]
> The output is piped to the [jq](https://jqlang.org/) program, to enhance output-readability.

curl -u Administrator:password -X GET http://localhost:8091/pools/nodes | jq '.'

Successful execution produces the following output:

{
  "name": "default",
  "nodes": [
    {
      "clusterMembership": "active",
      "recoveryType": "none",
      "status": "healthy",
      "otpNode": "ns_1@10.144.210.101",
      "thisNode": true,
      "hostname": "10.144.210.101:8091",
      "nodeUUID": "b71eeda1078c2dcb903b10ecd7b69d7c",
      "clusterCompatibility": 458761,
      "prod": "analytics",
      "prodName": "Operational Insights",
      "version": "3.0.0-nnnn-operational_insights",
      "os": "x86_64-unknown-linux-gnu",
      "cpuCount": 1,
      "ports": {
        "direct": 11210,
        "httpsMgmt": 18091,
        "distTCP": 21100,
        "distTLS": 21150
      },
      "services": [
        "kv",
        "cbas"
      ],
      "nodeEncryption": false,
      "addressFamilyOnly": true,
      "configuredHostname": "10.144.210.101:8091",
      "addressFamily": "inet",
      "externalListeners": [
        {
          "afamily": "inet",
          "nodeEncryption": false
        }
      ],
      "prodCompatVersion": "2.1.0",
      "serverGroup": "Group 1",
      "encryptionAtRestInfo": {
        "configuration": {
          "dataStatus": "encrypted",
          "dekNumber": 1,
          "issues": [],
          "oldestDekCreationDatetime": "2025-12-06T14:34:33Z"
        },
        "logs": {
          "dataStatus": "unencrypted",
          "dekNumber": 0,
          "issues": []
        },
        "audits": {
          "dataStatus": "unknown",
          "dekNumber": 0,
          "issues": []
        }
      },
      "nodeHash": 39392951,
      "systemStats": {
        "cpu_utilization_rate": 98.7012987012987,
        "cpu_stolen_rate": 0,
        "swap_total": 2047864832,
        "swap_used": 490958848,
        "mem_total": 1032990720,
        "mem_free": 181211136,
        "mem_limit": 1032990720,
        "cpu_cores_available": 1,
        "allocstall": 0
      },
      "uptime": "71151",
      "memoryTotal": 1032990720,
      "memoryFree": 181211136,
      "mcdMemoryReserved": 788,
      "mcdMemoryAllocated": 788
    },
    {
      "clusterMembership": "active",
      "recoveryType": "none",
      "status": "healthy",
      "otpNode": "ns_1@10.144.210.102",
      "hostname": "10.144.210.102:8091",
      "nodeUUID": "def51e43199a09925b867d5853b0587b",
      "clusterCompatibility": 458761,
      "prod": "analytics",
      "prodName": "Operational Insights",
      "version": "3.0.0-nnnn-operational_insights",
      "os": "x86_64-unknown-linux-gnu",
      "cpuCount": 1,
      "ports": {
        "direct": 11210,
        "httpsMgmt": 18091,
        "distTCP": 21100,
        "distTLS": 21150
      },
      "services": [
        "kv",
        "cbas"
      ],
      "nodeEncryption": false,
      "addressFamilyOnly": true,
      "configuredHostname": "10.144.210.102:8091",
      "addressFamily": "inet",
      "externalListeners": [
        {
          "afamily": "inet",
          "nodeEncryption": false
        }
      ],
      "prodCompatVersion": "2.1.0",
      "serverGroup": "Group 1",
      "encryptionAtRestInfo": {
        "configuration": {
          "dataStatus": "encrypted",
          "dekNumber": 1,
          "issues": [],
          "oldestDekCreationDatetime": "2025-12-06T14:34:33Z"
        },
        "logs": {
          "dataStatus": "unencrypted",
          "dekNumber": 0,
          "issues": []
        },
        "audits": {
          "dataStatus": "unknown",
          "dekNumber": 0,
          "issues": []
        }
      },
      "nodeHash": 39392951,
      "systemStats": {
        "cpu_utilization_rate": 6.096256684491979,
        "cpu_stolen_rate": 0,
        "swap_total": 2047864832,
        "swap_used": 43700224,
        "mem_total": 1032990720,
        "mem_free": 306143232,
        "mem_limit": 1032990720,
        "cpu_cores_available": 1,
        "allocstall": 0
      },
      "uptime": "70725",
      "memoryTotal": 1032990720,
      "memoryFree": 306143232,
      "mcdMemoryReserved": 788,
      "mcdMemoryAllocated": 788
    }
  ],
  "alerts": [],
  "alertsSilenceURL": "/controller/resetAlerts?uuid=8ebd144e243c942109c19842bdec9cdd&token=0",
  "controllers": {
    "addNode": {
      "uri": "/controller/addNodeV2?uuid=8ebd144e243c942109c19842bdec9cdd"
    },
    "rebalance": {
      "uri": "/controller/rebalance?uuid=8ebd144e243c942109c19842bdec9cdd"
    },
    "failOver": {
      "uri": "/controller/failOver?uuid=8ebd144e243c942109c19842bdec9cdd"
    },
    "reAddNode": {
      "uri": "/controller/reAddNode?uuid=8ebd144e243c942109c19842bdec9cdd"
    },
    "reFailOver": {
      "uri": "/controller/reFailOver?uuid=8ebd144e243c942109c19842bdec9cdd"
    },
    "ejectNode": {
      "uri": "/controller/ejectNode?uuid=8ebd144e243c942109c19842bdec9cdd"
    },
    "setRecoveryType": {
      "uri": "/controller/setRecoveryType?uuid=8ebd144e243c942109c19842bdec9cdd"
    },
    "clusterLogsCollection": {
      "startURI": "/controller/startLogsCollection?uuid=8ebd144e243c942109c19842bdec9cdd",
      "cancelURI": "/controller/cancelLogsCollection?uuid=8ebd144e243c942109c19842bdec9cdd"
    }
  },
  "rebalanceStatus": "none",
  "rebalanceProgressUri": "/pools/default/rebalanceProgress",
  "stopRebalanceUri": "/controller/stopRebalance?uuid=8ebd144e243c942109c19842bdec9cdd",
  "nodeStatusesUri": "/nodeStatuses",
  "maxBucketCount": 0,
  "tasks": {
    "uri": "/pools/default/tasks?v=37542573"
  },
  "counters": {
    "rebalance_success": 1,
    "rebalance_start": 1
  },
  "serverGroupsUri": "/pools/default/serverGroups?v=50544850",
  "clusterName": "10.144.210.101",
  "balanced": true,
  "checkPermissionsURI": "/pools/default/checkPermissions",
  "memoryQuota": 512,
  "cbasMemoryQuota": 1024,
  "storageTotals": {
    "ram": {
      "total": 2065981440,
      "quotaTotal": 1073741824,
      "quotaUsed": 419430400,
      "used": 1910071296,
      "usedByData": 165666496,
      "quotaUsedPerNode": 209715200,
      "quotaTotalPerNode": 536870912
    },
    "hdd": {
      "total": 264449089536,
      "quotaTotal": 264449089536,
      "used": 10577963580,
      "usedByData": 129100174,
      "free": 253871125956
    }
  }
}

The `nodes` array contains two objects, one each for the nodes `10.144.210.101` and `10.144.210.102`. For each node, a CPU count and a list of ports is provided, and the health of the node is displayed. The services for each node are listed. Address-family and encryption status are listed; as are various statistics related to memory and storage. Various URIs for cluster-management are also displayed.

## [](#see-also)See Also

For step-by-step procedures for node management, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).