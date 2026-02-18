---
title: Couchbase Search Node API
description: The Search Node Configuration REST API is provided by the Search
  Service. This API enables you to manage and monitor your Search nodes.
editUrl: https://github.com/couchbaselabs/cb-swagger/edit/release/7.6/docs/modules/fts-rest-nodes/pages/index.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/fts-rest-nodes/index.html)

# Couchbase Search Node API

## [](#overview)Overview

The Search Node Configuration REST API is provided by the Search service. This API enables you to manage and monitor your Search nodes.

### Version information

**Version:** 7.6

### Host information

{scheme}://{host}:{port}

The URL scheme, host, and port are as follows.

| Component  | Description                                                                              |
| ---------- | ---------------------------------------------------------------------------------------- |
| **scheme** | The URL scheme. Use https for secure access. **Values:** http, https                     |
| **host**   | The host name or IP address of a node running the Search Service. **Example:** localhost |
| **port**   | The Search Service REST port. Use 18094 for secure access. **Values:** 8094, 18094       |

## [](#resources)Resources

This section describes the operations available with this REST API. The operations are grouped in the following categories.

[Configuration](#tag-Configuration)  
[Diagnostics](#tag-Diagnostics)  
[Management](#tag-Management)  
[Monitoring](#tag-Monitoring)

### [](#tag-Configuration)Configuration

Operations for node configuration.

[Get Cluster Configuration](#getClusterConfig)  
[Replan Resource Assignments](#managerKick)  
[Get Node Capabilities](#managerMeta)  
[Refresh Node Configuration](#refreshClusterConfig)

#### [](#getClusterConfig)Get Cluster Configuration

GET /api/cfg

##### [](#getClusterConfig-description)Description

Returns the node's current view of the cluster's configuration as JSON.

Produces

* application/json

##### [](#getClusterConfig-responses)Responses

| HTTP Code | Description                                        | Schema                                  |
| --------- | -------------------------------------------------- | --------------------------------------- |
| 200       | A JSON object containing the node's configuration. | [Cluster Configuration](#clusterConfig) |

##### [](#getClusterConfig-security)Security

| Type         | Name                                                 |
| ------------ | ---------------------------------------------------- |
| http (basic) | [readClusterSettings](#security-readClusterSettings) |

##### [](#getClusterConfig-ex-response)Example HTTP Response

Response 200

```json
{
  "indexDefs" : {
    "implVersion" : "4.0.0",
    "indexDefs" : {
      "myFirstIndex" : {
        "name" : "myFirstIndex",
        "params" : "",
        "planParams" : {
          "hierarchyRules" : null,
          "maxPartitionsPerPIndex" : 0,
          "nodePlanParams" : null,
          "numReplicas" : 0,
          "planFrozen" : false
        },
        "sourceName" : "",
        "sourceParams" : "",
        "sourceType" : "nil",
        "sourceUUID" : "",
        "type" : "blackhole",
        "uuid" : "6cc599ab7a85bf3b"
      }
    },
    "uuid" : "6cc599ab7a85bf3b"
  },
  "indexDefsCAS" : 3,
  "indexDefsErr" : null,
  "nodeDefsKnown" : {
    "implVersion" : "4.0.0",
    "nodeDefs" : {
      "78fc2ffac2fd9401" : {
        "container" : "",
        "extras" : "",
        "hostPort" : "0.0.0.0:8094",
        "implVersion" : "4.0.0",
        "tags" : null,
        "uuid" : "78fc2ffac2fd9401",
        "weight" : 1
      }
    },
    "uuid" : "2f0d18fb750b2d4a"
  },
  "nodeDefsKnownCAS" : 1,
  "nodeDefsKnownErr" : null,
  "nodeDefsWanted" : {
    "implVersion" : "4.0.0",
    "nodeDefs" : {
      "78fc2ffac2fd9401" : {
        "container" : "",
        "extras" : "",
        "hostPort" : "0.0.0.0:8094",
        "implVersion" : "4.0.0",
        "tags" : null,
        "uuid" : "78fc2ffac2fd9401",
        "weight" : 1
      }
    },
    "uuid" : "72d6750878551451"
  },
  "nodeDefsWantedCAS" : 2,
  "nodeDefsWantedErr" : null,
  "planPIndexes" : {
    "implVersion" : "4.0.0",
    "planPIndexes" : {
      "myFirstIndex_6cc599ab7a85bf3b_0" : {
        "indexName" : "myFirstIndex",
        "indexParams" : "",
        "indexType" : "blackhole",
        "indexUUID" : "6cc599ab7a85bf3b",
        "name" : "myFirstIndex_6cc599ab7a85bf3b_0",
        "nodes" : {
          "78fc2ffac2fd9401" : {
            "canRead" : true,
            "canWrite" : true,
            "priority" : 0
          }
        },
        "sourceName" : "",
        "sourceParams" : "",
        "sourcePartitions" : "",
        "sourceType" : "nil",
        "sourceUUID" : "",
        "uuid" : "64bed6e2edf354c3"
      }
    },
    "uuid" : "6327debf817a5ec7",
    "warnings" : {
      "myFirstIndex" : [ ]
    }
  },
  "planPIndexesCAS" : 5,
  "planPIndexesErr" : null,
  "status" : "ok"
}
```

#### [](#managerKick)Replan Resource Assignments

POST /api/managerKick

##### [](#managerKick-description)Description

Forces the node to replan resource assignments, (by running the planner, if enabled) and update its runtime state to reflect the latest plan (by running the janitor, if enabled).

##### [](#managerKick-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |

##### [](#managerKick-security)Security

| Type         | Name                                                   |
| ------------ | ------------------------------------------------------ |
| http (basic) | [writeClusterSettings](#security-writeClusterSettings) |

#### [](#managerMeta)Get Node Capabilities

GET /api/managerMeta

##### [](#managerMeta-description)Description

Returns information on the node's capabilities, including available indexing and storage options as JSON. This operation is intended to help management tools and web UIs to be more dynamically metadata driven.

Produces

* application/json

##### [](#managerMeta-responses)Responses

| HTTP Code | Description                                       | Schema |
| --------- | ------------------------------------------------- | ------ |
| 200       | A JSON object containing the node's capabilities. | Object |

##### [](#managerMeta-security)Security

| Type         | Name                                                   |
| ------------ | ------------------------------------------------------ |
| http (basic) | [writeClusterSettings](#security-writeClusterSettings) |

#### [](#refreshClusterConfig)Refresh Node Configuration

POST /api/cfgRefresh

##### [](#refreshClusterConfig-description)Description

Requests the node to refresh its configuration from the configuration provider.

##### [](#refreshClusterConfig-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |

##### [](#refreshClusterConfig-security)Security

| Type         | Name                                                   |
| ------------ | ------------------------------------------------------ |
| http (basic) | [writeClusterSettings](#security-writeClusterSettings) |

### [](#tag-Diagnostics)Diagnostics

Operations for node diagnostics.

[Capture CPU Profiling Information](#captureCpuProfile)  
[Capture Memory Profiling Information](#captureMemoryProfile)  
[Get Diagnostics](#getDiagnostics)  
[Get Node Logs](#getLogs)  
[Get Node Runtime Arguments](#getRuntimeArgs)  
[Get Node Runtime Information](#getRuntimeInfo)

#### [](#captureCpuProfile)Capture CPU Profiling Information

POST /api/runtime/profile/cpu

##### [](#captureCpuProfile-description)Description

Requests the node to capture local CPU usage profiling information.

##### [](#captureCpuProfile-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |

##### [](#captureCpuProfile-security)Security

| Type         | Name                                     |
| ------------ | ---------------------------------------- |
| http (basic) | [manageCluster](#security-manageCluster) |

#### [](#captureMemoryProfile)Capture Memory Profiling Information

POST /api/runtime/profile/memory

##### [](#captureMemoryProfile-description)Description

Requests the node to capture local memory usage profiling information.

##### [](#captureMemoryProfile-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |

##### [](#captureMemoryProfile-security)Security

| Type         | Name                                     |
| ------------ | ---------------------------------------- |
| http (basic) | [manageCluster](#security-manageCluster) |

#### [](#getDiagnostics)Get Diagnostics

GET /api/diag

##### [](#getDiagnostics-description)Description

Returns the full set of diagnostic information from the node as JSON. The response is the union of the responses from the node's other REST API diagnostic and monitoring endpoints.

For example, for a 3 node cluster, you could capture diagnostics for each node with something like:

```shell
curl http://cbft-01:8094/api/diag > cbft-01.json
curl http://cbft-02:8094/api/diag > cbft-02.json
curl http://cbft-03:8094/api/diag > cbft-03.json

```

The response JSON object can be quite large, 100s of KB or much more.

The motivation for this operation is to simplify working with the Couchbase community, forums, technical support, and other engineers, by making data capture from each Search node a single step.

Produces

* application/json

##### [](#getDiagnostics-responses)Responses

| HTTP Code | Description                                      | Schema |
| --------- | ------------------------------------------------ | ------ |
| 200       | A JSON object containing the node's diagnostics. | Object |

##### [](#getDiagnostics-security)Security

| Type         | Name                                         |
| ------------ | -------------------------------------------- |
| http (basic) | [readClusterLogs](#security-readClusterLogs) |

#### [](#getLogs)Get Node Logs

GET /api/log

##### [](#getLogs-description)Description

Returns recent log messages and key events for the node as JSON.

Produces

* application/json

##### [](#getLogs-responses)Responses

| HTTP Code | Description                               | Schema                   |
| --------- | ----------------------------------------- | ------------------------ |
| 200       | A JSON object containing the node's logs. | [Log Messages](#logInfo) |

##### [](#getLogs-security)Security

| Type         | Name                                         |
| ------------ | -------------------------------------------- |
| http (basic) | [readClusterLogs](#security-readClusterLogs) |

##### [](#getLogs-ex-response)Example HTTP Response

Response 200

```json
{
  "events" : [ ],
  "messages" : [ ]
}
```

#### [](#getRuntimeArgs)Get Node Runtime Arguments

GET /api/runtime/args

##### [](#getRuntimeArgs-description)Description

Returns information on the node's command-line, parameters, environment variables, and OS process values as JSON.

Produces

* application/json

##### [](#getRuntimeArgs-responses)Responses

| HTTP Code | Description                                            | Schema |
| --------- | ------------------------------------------------------ | ------ |
| 200       | A JSON object containing the node's runtime arguments. | Object |

##### [](#getRuntimeArgs-security)Security

| Type         | Name                                                 |
| ------------ | ---------------------------------------------------- |
| http (basic) | [readClusterSettings](#security-readClusterSettings) |

#### [](#getRuntimeInfo)Get Node Runtime Information

GET /api/runtime

##### [](#getRuntimeInfo-description)Description

Returns information on the node's software, such as version strings and slow-changing runtime settings, as JSON.

Produces

* application/json

##### [](#getRuntimeInfo-responses)Responses

| HTTP Code | Description                                              | Schema                              |
| --------- | -------------------------------------------------------- | ----------------------------------- |
| 200       | A JSON object containing the node's runtime information. | [Runtime Information](#runtimeInfo) |

##### [](#getRuntimeInfo-security)Security

| Type         | Name                                                 |
| ------------ | ---------------------------------------------------- |
| http (basic) | [readClusterSettings](#security-readClusterSettings) |

##### [](#getRuntimeInfo-ex-response)Example HTTP Response

Response 200

```json
{
  "arch" : "amd64",
  "go" : {
    "GOMAXPROCS" : 1,
    "GOROOT" : "/usr/local/go",
    "compiler" : "gc",
    "version" : "go1.4"
  },
  "numCPU" : 8,
  "os" : "darwin",
  "versionData" : "4.0.0",
  "versionMain" : "v0.3.1"
}
```

### [](#tag-Management)Management

Operations for node management.

[Perform Garbage Collection](#performGC)

#### [](#performGC)Perform Garbage Collection

POST /api/runtime/gc

##### [](#performGC-description)Description

Requests the node to perform a garbage collection.

##### [](#performGC-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |

##### [](#performGC-security)Security

| Type         | Name                                     |
| ------------ | ---------------------------------------- |
| http (basic) | [manageCluster](#security-manageCluster) |

### [](#tag-Monitoring)Monitoring

Operations for node monitoring.

[Get Memory Statistics](#getMemoryStats)  
[Get Runtime Statistics](#getRuntimeStats)

#### [](#getMemoryStats)Get Memory Statistics

GET /api/runtime/statsMem

##### [](#getMemoryStats-description)Description

Returns information on the node's low-level garbage collection and memory-related runtime stats as JSON.

Produces

* application/json

##### [](#getMemoryStats-responses)Responses

| HTTP Code | Description                                            | Schema |
| --------- | ------------------------------------------------------ | ------ |
| 200       | A JSON object containing the node's memory statistics. | Object |

##### [](#getMemoryStats-security)Security

| Type         | Name                                     |
| ------------ | ---------------------------------------- |
| http (basic) | [manageCluster](#security-manageCluster) |

#### [](#getRuntimeStats)Get Runtime Statistics

GET /api/runtime/stats

##### [](#getRuntimeStats-description)Description

Returns information on the node's low-level runtime stats as JSON.

Produces

* application/json

##### [](#getRuntimeStats-responses)Responses

| HTTP Code | Description                                                       | Schema |
| --------- | ----------------------------------------------------------------- | ------ |
| 200       | A JSON object containing the node's low-level runtime statistics. | Object |

##### [](#getRuntimeStats-security)Security

| Type         | Name                                     |
| ------------ | ---------------------------------------- |
| http (basic) | [manageCluster](#security-manageCluster) |

## [](#models)Definitions

This section describes the properties consumed and returned by this REST API.

[Cluster Configuration](#clusterConfig)  
[Index Definitions](#clusterConfigIndexes)  
[Known Nodes](#clusterConfigNodesKnown)  
[Wanted Nodes](#clusterConfigNodesWanted)  
[Node Definitions Wrapper](#clusterConfigNodesWrapper)  
[Node Definition](#clusterConfigNodesWrapperNode)  
[Plan Partitions](#clusterConfigPlan)  
[Plan Partitions Wrapper](#clusterConfigPlanWrapper)  
[Plan Partition](#GetIndexResponsePIndex)  
[Partition Nodes Wrapper](#GetIndexResponsePIndexNodesWrapper)  
[Partition Node](#GetIndexResponsePIndexNodesWrapperNode)  
[Plan Warnings Wrapper](#GetIndexResponsePlanWrng)  
[Plan Warnings](#GetIndexResponsePlanWrngIndex)  
[Index Definitions Wrapper](#GetIndexesResponseIndexesWrapper)  
[Index Definition](#IndexDefinition)  
[Plan Parameters](#IndexDefinitionPlanParams)  
[Log Messages](#logInfo)  
[Runtime Information](#runtimeInfo)  
[Go Runtime Information](#runtimeInfoGo)

### [](#clusterConfig)Cluster Configuration

 Object

| Property                      |                                                                        | Schema                                     |
| ----------------------------- | ---------------------------------------------------------------------- | ------------------------------------------ |
| **indexDefs**optional         | An object containing Search index definitions and related information. | [Index Definitions](#clusterConfigIndexes) |
| **indexDefsCAS**optional      | Search index definition concurrency (compare and swap) value.          | Integer                                    |
| **indexDefsErr**optional      | Search index definition error. **Nullable:** yes                       | String                                     |
| **nodeDefsKnown**optional     | An object containing known node definitions and related information.   | [Known Nodes](#clusterConfigNodesKnown)    |
| **nodeDefsKnownCAS**optional  | Known node definition concurrency (compare and swap) value.            | Integer                                    |
| **nodeDefsKnownErr**optional  | Known node definition error. **Nullable:** yes                         | String                                     |
| **nodeDefsWanted**optional    | An object containing wanted node definitions and related information.  | [Wanted Nodes](#clusterConfigNodesWanted)  |
| **nodeDefsWantedCAS**optional | Wanted node definition concurrency (compare and swap) value.           | Integer                                    |
| **nodeDefsWantedErr**optional | Wanted node definition error. **Nullable:** yes                        | String                                     |
| **planPIndexes**optional      | An object containing Search index partitions and related information.  | [Plan Partitions](#clusterConfigPlan)      |
| **planPIndexesCAS**optional   | Search index partition concurrency (compare and swap) value.           | Integer                                    |
| **planPIndexesErr**optional   | Search index partition error. **Nullable:** yes                        | String                                     |
| **status**optional            | The status of the operation.                                           | String                                     |

#### Index Definitions

 Object

| Property                |                                                          | Schema                                                         |
| ----------------------- | -------------------------------------------------------- | -------------------------------------------------------------- |
| **implVersion**optional |                                                          | String                                                         |
| **indexDefs**optional   | An object containing 1 or more Search index definitions. | [Index Definitions Wrapper](#GetIndexesResponseIndexesWrapper) |

#### Known Nodes

 Object

| Property                |                                                          | Schema                                                 |
| ----------------------- | -------------------------------------------------------- | ------------------------------------------------------ |
| **implVersion**optional |                                                          | String                                                 |
| **nodeDefs**optional    | An object containing the definitions of 1 or more nodes. | [Node Definitions Wrapper](#clusterConfigNodesWrapper) |
| **uuid**optional        |                                                          | String                                                 |

#### Wanted Nodes

 Object

| Property                |                                                          | Schema                                                 |
| ----------------------- | -------------------------------------------------------- | ------------------------------------------------------ |
| **implVersion**optional |                                                          | String                                                 |
| **nodeDefs**optional    | An object containing the definitions of 1 or more nodes. | [Node Definitions Wrapper](#clusterConfigNodesWrapper) |
| **uuid**optional        |                                                          | String                                                 |

#### Node Definitions Wrapper

 Object

| Property           |                                                                                                         | Schema                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| additionalproperty | An object containing the definition of a single node. The name of the property is the UUID of the node. | [Node Definition](#clusterConfigNodesWrapperNode) |

#### Node Definition

 Object

| Property                |                   | Schema  |
| ----------------------- | ----------------- | ------- |
| **container**optional   |                   | String  |
| **extras**optional      |                   | String  |
| **hostPort**optional    |                   | String  |
| **implVersion**optional |                   | String  |
| **tags**optional        | **Nullable:** yes | String  |
| **uuid**optional        |                   | String  |
| **weight**optional      |                   | Integer |

#### Plan Partitions

 Object

| Property                 |                                                                                                           | Schema                                               |
| ------------------------ | --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| **implVersion**optional  |                                                                                                           | String                                               |
| **planPIndexes**optional | An object containing information about 1 or more Search index partitions.                                 | [Plan Partitions Wrapper](#clusterConfigPlanWrapper) |
| **uuid**optional         |                                                                                                           | String                                               |
| **warnings**optional     | An object containing 0, 1, or more nested objects, each containing warnings that apply to a Search index. | [Plan Warnings Wrapper](#GetIndexResponsePlanWrng)   |

#### Plan Partitions Wrapper

 Object

| Property           |                                                                         | Schema                                    |
| ------------------ | ----------------------------------------------------------------------- | ----------------------------------------- |
| additionalproperty | An object containing information about a single Search index partition. | [Plan Partition](#GetIndexResponsePIndex) |

#### Plan Partition

 Object

| Property                     |                                                                                                                                                         | Schema                                                         |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **indexName**optional        | The name of the Search index. For more information, see [Initial Settings](../search/search-index-params.html#initial).                                 | String                                                         |
| **indexParams**optional      | The Search index's type identifier, type mappings, and analyzers. For more information, see [Params Object](../search/search-index-params.html#params). | Object                                                         |
| **indexType**optional        | The type of the Search index. For more information, see [Initial Settings](../search/search-index-params.html#initial).                                 | String                                                         |
| **indexUUID**optional        | The UUID of the Search index. For more information, see [Initial Settings](../search/search-index-params.html#initial).                                 | String                                                         |
| **name**optional             | The name of the Search index partition.                                                                                                                 | String                                                         |
| **nodes**optional            | An object containing information about 1 or more Search index partition nodes.                                                                          | [Partition Nodes Wrapper](#GetIndexResponsePIndexNodesWrapper) |
| **sourceName**optional       | The name of the bucket where the Search index is stored. For more information, see [Initial Settings](../search/search-index-params.html#initial).      | String                                                         |
| **sourceParams**optional     | Advanced settings for Search index behavior. For more information, see [Initial Settings](../search/search-index-params.html#initial).                  | Object                                                         |
| **sourcePartitions**optional |                                                                                                                                                         | String                                                         |
| **sourceType**optional       | The type of the bucket where the Search index is stored. For more information, see [Initial Settings](../search/search-index-params.html#initial).      | String                                                         |
| **sourceUUID**optional       | The UUID of the bucket where the Search index is stored. For more information, see [Initial Settings](../search/search-index-params.html#initial).      | String                                                         |
| **uuid**optional             | The UUID of the Search index partition.                                                                                                                 | String                                                         |

#### Partition Nodes Wrapper

 Object

| Property           |                                                                                                                         | Schema                                                    |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| additionalproperty | An object containing information about a single Search index partition node. The name of the property is the node UUID. | [Partition Node](#GetIndexResponsePIndexNodesWrapperNode) |

#### Partition Node

 Object

| Property             |  | Schema  |
| -------------------- |  | ------- |
| **canRead**optional  |  | Boolean |
| **canWrite**optional |  | Boolean |
| **priority**optional |  | Integer |

#### Plan Warnings Wrapper

 Object

| Property           |                                                                                 | Schema                                          |
| ------------------ | ------------------------------------------------------------------------------- | ----------------------------------------------- |
| additionalproperty | An array of warnings. The name of the property is the name of the Search index. | [Plan Warnings](#GetIndexResponsePlanWrngIndex) |

#### Plan Warnings

 Array

An array of warnings. The name of the property is the name of the Search index.

Schema

String array

#### Index Definitions Wrapper

 Object

| Property           |                                                                                                                                                  | Schema                               |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------ |
| additionalproperty | The full Search index definition. For a detailed list of all parameters, see [Search Index JSON Properties](../search/search-index-params.html). | [Index Definition](#IndexDefinition) |

#### Index Definition

 Object

| Property                  |                                                                                                                                                                  | Schema                                        |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **name**required          | The name of the Search index. For more information, see [Initial Settings](../search/search-index-params.html#initial).                                          | String                                        |
| **type**required          | The type of the Search index. For more information, see [Initial Settings](../search/search-index-params.html#initial).                                          | String                                        |
| **sourceName**required    | The name of the bucket where the Search index is stored. For more information, see [Initial Settings](../search/search-index-params.html#initial).               | String                                        |
| **sourceUUID**optional    | The UUID of the bucket where the Search index is stored. For more information, see [Initial Settings](../search/search-index-params.html#initial).               | String                                        |
| **sourceParams**optional  | Advanced settings for Search index behavior. For more information, see [Initial Settings](../search/search-index-params.html#initial).                           | Object                                        |
| **sourceType**required    | The type of the bucket where the Search index is stored. For more information, see [Initial Settings](../search/search-index-params.html#initial).               | String                                        |
| **params**required        | The Search index's type identifier, type mappings, and analyzers. For more information, see [Params Object](../search/search-index-params.html#params).          | Object                                        |
| **planParams**required    | The Search index's partitioning and replication settings. For more information, see [Plan Params Object](../search/search-index-params.html#planParams).         | [Plan Parameters](#IndexDefinitionPlanParams) |
| **prevIndexUUID**optional | The UUID of the previous index. Intended for clients that want to check that they are not overwriting the Search index definition updates of concurrent clients. | String                                        |
| **uuid**optional          | The UUID of the Search index. For more information, see [Initial Settings](../search/search-index-params.html#initial).                                          | String                                        |

#### Plan Parameters

 Object

| Property                           |                                                                                                                                                | Schema  |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **hierarchyRules**optional         | **Nullable:** yes                                                                                                                              | String  |
| **maxPartitionsPerPIndex**optional | This setting is deprecated. Use indexPartitions instead.                                                                                       | Integer |
| **indexPartitions**optional        | The number of partitions to split the Search index into, across the nodes you have available in your database with the Search Service enabled. | Integer |
| **nodePlanParams**optional         | **Nullable:** yes                                                                                                                              | String  |
| **numReplicas**optional            | The number of replicas the Search Service creates for the Search index to ensure high availability.                                            | Integer |
| **planFrozen**optional             |                                                                                                                                                | Boolean |

### [](#logInfo)Log Messages

 Object

| Property             |  | Schema       |
| -------------------- |  | ------------ |
| **events**optional   |  | Object array |
| **messages**optional |  | Object array |

### [](#runtimeInfo)Runtime Information

 Object

| Property                |                                   | Schema                                   |
| ----------------------- | --------------------------------- | ---------------------------------------- |
| **arch**optional        | The architecture of the node.     | String                                   |
| **go**optional          |                                   | [Go Runtime Information](#runtimeInfoGo) |
| **numCPU**optional      | The number of CPUs on the node.   | Integer                                  |
| **os**optional          | The operating system of the node. | String                                   |
| **versionData**optional |                                   | String                                   |
| **versionMain**optional |                                   | String                                   |

#### Go Runtime Information

 Object

| Property               |  | Schema  |
| ---------------------- |  | ------- |
| **GOMAXPROCS**optional |  | Integer |
| **GOROOT**optional     |  | String  |
| **compiler**optional   |  | String  |
| **version**optional    |  | String  |

## [](#security)Security

The Search REST APIs support HTTP basic authentication. Pass your credentials through HTTP headers.

### [](#security-manageCluster)manageCluster

You must have the **Full Admin** or **Cluster Admin** role, with permissions to manage the cluster.

**Type:** http

### [](#security-readClusterSettings)readClusterSettings

You must have the **Full Admin** or **Cluster Admin** role, with permission to read cluster settings.

**Type:** http

### [](#security-readClusterLogs)readClusterLogs

You must have the **Full Admin** or **Cluster Admin** role, with permission to read cluster logs.

**Type:** http

### [](#security-writeClusterSettings)writeClusterSettings

You must have the **Full Admin** or **Cluster Admin** role, with permission to write cluster settings.

**Type:** http

For more information, see [Roles](../learn/security/roles.md).