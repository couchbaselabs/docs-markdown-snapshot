---
title: Get System Information
description: SQL++ has a system namespace that stores metadata about data
  containers, the Query service, and the system as a whole. You can query the
  system namespace to get this information.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/n1ql/pages/n1ql-intro/sysinfo.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:n1ql:n1ql-intro/sysinfo.adoc[]
---

[View original HTML](/server/7.6/n1ql/n1ql-intro/sysinfo.html)

# Get System Information

> SQL++ has a system namespace that stores metadata about data containers, the Query service, and the system as a whole. You can query the system namespace to get this information. 

Within the `system` namespace, the following catalogs are provided. Most catalog names are plural in order to avoid conflicting with SQL++ keywords.

| Data Containers                                                                                                                                                                                                                                                     | Monitoring Catalogs                                                                                                                                                                                                                                                                                                                                                                                           | Security Catalogs                                                                                                                                      | Other                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [system:datastores](#querying-datastores) [system:namespaces](#querying-namespaces) [system:buckets](#querying-buckets) [system:scopes](#querying-scopes) [system:keyspaces](#querying-keyspaces) [system:indexes](#querying-indexes) [system:dual](#querying-dual) | [system:vitals](../n1ql-manage/monitoring-n1ql-query.md#vitals) [system:active\_requests](../n1ql-manage/monitoring-n1ql-query.md#sys-active-req) [system:prepareds](../n1ql-manage/monitoring-n1ql-query.md#sys-prepared) [system:completed\_requests](../n1ql-manage/monitoring-n1ql-query.md#sys-completed-req) [system:completed\_requests\_history](../n1ql-manage/monitoring-n1ql-query.md#sys-history) | [system:my\_user\_info](#sys%5Fmy-user-info) [system:user\_info](#sys-user-info) [system:nodes](#sys-nodes) [system:applicable\_roles](#sys-app-roles) | [system:dictionary](#sys-dictionary) [system:dictionary\_cache](#sys-dictionary-cache) [system:functions](#sys-functions) [system:functions\_cache](#sys-functions-cache) [system:tasks\_cache](#sys-tasks-cache) [system:transactions](#sys-transactions) [system:sequences](#sys-sequences) [system:all-sequences](#sys-all-sequences) |

## [](#authentication-and-client-privileges)Authentication and Client Privileges

Client applications must be authenticated with sufficient privileges to access system keyspaces.

* Users must have the **Query System Catalog** role to access restricted system keyspaces. For more details about user roles, see [Authorization](../../learn/security/authorization-overview.md).
* In addition, users must have permission to access a bucket, scope, or collection to be able to view that item in the system catalog. Similarly, users must have SELECT permission on the target of an index to be able to view that index in the system catalog.
* The following system keyspaces are considered open, that is, all users can access them without any special privileges:

  * `system:dual`
  * `system:datastores`
  * `system:namespaces`

## [](#querying-datastores)Query Datastores

You can query datastores using the `system:datastores` keyspace as follows:

```sqlpp
SELECT * FROM system:datastores
```

This catalog contains the following attributes:

| Name               | Description                    | Schema |
| ------------------ | ------------------------------ | ------ |
| **id** _required_  | ID of the datastore.           | String |
| **url** _required_ | URL of the datastore instance. | String |

## [](#querying-namespaces)Query Namespaces

You can query namespaces using the `system:namespaces` keyspace as follows:

```sqlpp
SELECT * FROM system:namespaces
```

This catalog contains the following attributes:

| Name                         | Description                                         | Schema |
| ---------------------------- | --------------------------------------------------- | ------ |
| **id** _required_            | ID of the namespace.                                | String |
| **name** _required_          | Name of the namespace.                              | String |
| **datastore\_id** _required_ | ID of the datastore to which the namespace belongs. | String |

## [](#querying-buckets)Query Buckets

You can query buckets using the `system:buckets` keyspace as follows:

```sqlpp
SELECT * FROM system:buckets
```

This catalog contains the following attributes:

| Name                         | Description                                      | Schema |
| ---------------------------- | ------------------------------------------------ | ------ |
| **datastore\_id** _required_ | ID of the datastore to which the bucket belongs. | String |
| **name** _required_          | Name of the bucket.                              | String |
| **namespace** _required_     | Namespace to which the bucket belongs.           | String |
| **namespace\_id** _required_ | ID of the namespace to which the bucket belongs. | String |
| **path** _required_          | Path of the bucket.                              | String |

## [](#querying-scopes)Query Scopes

You can query scopes using the `system:scopes` keyspace as follows:

```sqlpp
SELECT * FROM system:scopes
```

This catalog contains the following attributes:

| Name                         | Description                                     | Schema |
| ---------------------------- | ----------------------------------------------- | ------ |
| **bucket** _required_        | Bucket to which the scope belongs.              | String |
| **datastore\_id** _required_ | ID of the datastore to which the scope belongs. | String |
| **name** _required_          | Name of the scope.                              | String |
| **namespace** _required_     | Namespace to which the scope belongs.           | String |
| **namespace\_id** _required_ | ID of the namespace to which the scope belongs. | String |
| **path** _required_          | Path of the scope.                              | String |

> [!NOTE]
> Querying `system:scopes` only returns named scopes — that is, non-default scopes. To return all scopes, including the default scopes, you can query `system:all_scopes`.

## [](#querying-keyspaces)Query Collections

You can query collections using the `system:keyspaces` keyspace as follows:

```sqlpp
SELECT * FROM system:keyspaces
```

This catalog contains the following attributes:

| Name                         | Description                                                                                                                                               | Schema |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **bucket** _optional_        | For a named, non-default collection: Bucket to which the keyspace belongs.                                                                                | String |
| **datastore\_id** _required_ | ID of the datastore to which the keyspace belongs.                                                                                                        | String |
| **id** _required_            | For the default collection in the default scope: ID of the bucket to which the keyspace belongs. For a named, non-default collection: ID of the keyspace. | String |
| **name** _required_          | For the default collection in the default scope: Bucket to which the keyspace belongs. For a named, non-default collection: Name of the keyspace.         | String |
| **namespace** _required_     | Namespace to which the keyspace belongs.                                                                                                                  | String |
| **namespace\_id** _required_ | ID of the namespace to which the keyspace belongs.                                                                                                        | String |
| **path** _required_          | Path of the keyspace.                                                                                                                                     | String |
| **scope** _optional_         | For a named, non-default collection: Scope to which the keyspace belongs.                                                                                 | String |

> [!NOTE]
> Querying `system:keyspaces` only returns non-system keyspaces. To return all keyspaces, including the system keyspaces, you can query `system:all_keyspaces`.

## [](#querying-indexes)Query Indexes

You can query indexes using the `system:indexes` keyspace as follows:

```sqlpp
SELECT * FROM system:indexes
```

This catalog contains the following attributes:

| Name                         | Description                                                                                                                                                                                               | Schema                       |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| **bucket\_id** _optional_    | For an index on a named, non-default collection: ID of the bucket to which the index belongs.                                                                                                             | String                       |
| **condition** _optional_     | Index filter, if present.                                                                                                                                                                                 | String                       |
| **datastore\_id** _required_ | ID of the datastore to which the index belongs.                                                                                                                                                           | String                       |
| **id** _required_            | ID of the index.                                                                                                                                                                                          | String                       |
| **index\_key** _required_    | List of index keys.                                                                                                                                                                                       | String array                 |
| **is\_primary** _required_   | True if the index is a primary index.                                                                                                                                                                     | Boolean                      |
| **keyspace\_id** _required_  | For an index on the default collection in the default scope: ID of the bucket to which the index belongs. For an index on a named, non-default collection: ID of the keyspace to which the index belongs. | String                       |
| **name** _required_          | Name of the index.                                                                                                                                                                                        | String                       |
| **metadata** _required_      | Metadata for the index.                                                                                                                                                                                   | [Metadata](#metadata) object |
| **namespace\_id** _required_ | ID of the namespace to which the index belongs.                                                                                                                                                           | String                       |
| **state** _required_         | State of index. **Example**: online                                                                                                                                                                       | String                       |
| **using** _required_         | Type of index. **Example**: gsi                                                                                                                                                                           | String                       |

**Metadata**

| Name                            | Description                           | Schema                 |
| ------------------------------- | ------------------------------------- | ---------------------- |
| **last\_scan\_time** _required_ | The last scan timestamp of the index. | String                 |
| **num\_replica** _required_     | The index replica count.              | String                 |
| **stats** _required_            | Statistics for the index.             | [Stats](#stats) object |

**Stats**

| Name                                   | Description                                                      | Schema |
| -------------------------------------- | ---------------------------------------------------------------- | ------ |
| **last\_known\_scan\_time** _required_ | The index last scan time from the indexer, in UNIX Epoch format. | Number |

> [!NOTE]
> Querying `system:indexes` only returns indexes on non-system keyspaces. To return all indexes, including indexes on system keyspaces, you can query `system:all_indexes`.

## [](#querying-dual)Query Dual

You can use dual to evaluate constant expressions.

```sqlpp
SELECT 2+5 FROM system:dual
```

The query returns the result of the expression, 7 in this case.

## [](#sys%5Fmy-user-info)Monitor Your User Info

The `system:my_user_info` catalog maintains a list of all information of your profile.

To see your current information, use:

```sqlpp
SELECT * FROM system:my_user_info;
```

This will result in a list similar to:

```json
[
  {
    "my_user_info": {
      "domain": "local",
      "external_groups": [],
      "groups": [],
      "id": "jane",
      "name": "Jane Doe",
      "password_change_date": "2019-05-07T02:31:53.000Z",
      "roles": [
        {
          "origins": [
            {
              "type": "user"
            }
          ],
          "role": "admin"
        }
      ]
    }
  }
]
```

## [](#sys-user-info)Monitor All User Info

The `system:user_info` catalog maintains a list of all current users in your bucket and their information.

To see the list of all current users, use:

```sqlpp
SELECT * FROM system:user_info;
```

This will result in a list similar to:

```json
[
  {
    "user_info": {
      "domain": "local",
      "external_groups": [],
      "groups": [],
      "id": "jane",
      "name": "Jane Doe",
      "password_change_date": "2019-05-07T02:31:53.000Z",
      "roles": [
        {
          "origins": [
            {
              "type": "user"
            }
          ],
          "role": "admin"
        }
      ]
    }
  },
  {
    "user_info": {
      "domain": "ns_server",
      "id": "Administrator",
      "name": "Administrator",
      "roles": [
        {
          "role": "admin"
        }
      ]
    }
  }
]
```

## [](#sys-nodes)Monitor Nodes

The `system:nodes` catalog shows the datastore topology information. This is separate from the Query clustering view, in that Query clustering shows a map of the Query cluster, as provided by the cluster manager, while `system:nodes` shows a view of the nodes and services that make up the actual datastore, which may or may not include Query nodes.

* The dichotomy is important in that Query nodes could be clustered by one entity (e.g. Zookeeper) and be connected to a clustered datastore (e.g. Couchbase) such that each does not have visibility of the other.
* Should SQL++ be extended to be able to concurrently connect to multiple datastores, each datastore will report its own topology, so that `system:nodes` offers a complete view of all the storage nodes, whatever those may be.
* The `system:nodes` keyspace provides a way to report services advertised by each node as well as services that are actually running. This is datastore dependent.
* Query clustering is still reported by the `/admin` endpoints.

To see the list of all current node information, use:

```sqlpp
SELECT * FROM system:nodes;
```

This will result in a list similar to:

```json
[
  {
    "nodes": {
      "name": "127.0.0.1:8091",
      "ports": {
        "cbas": 8095,
        "cbasAdmin": 9110,
        "cbasCc": 9111,
        "cbasSSL": 18095,
        "eventingAdminPort": 8096,
        "eventingSSL": 18096,
        "fts": 8094,
        "ftsSSL": 18094,
        "indexAdmin": 9100,
        "indexHttp": 9102,
        "indexHttps": 19102,
        "indexScan": 9101,
        "indexStreamCatchup": 9104,
        "indexStreamInit": 9103,
        "indexStreamMaint": 9105,
        "kv": 11210,
        "kvSSL": 11207,
        "n1ql": 8093,
        "n1qlSSL": 18093
      },
      "services": [
        "cbas",
        "eventing",
        "fts",
        "index",
        "kv",
        "n1ql"
      ]
    }
  }
]
```

## [](#sys-app-roles)Monitor Applicable Roles

The `system:applicable_roles` catalog maintains a list of all applicable roles and grantee of each bucket.

To see the list of all current applicable role information, use:

```sqlpp
SELECT * FROM system:applicable_roles;
```

This will result in a list similar to:

```json
[
  {
    "applicable_roles": {
      "grantee": "anil",
      "role": "replication_admin"
    }
  },
  {
    "applicable_roles": {
      "bucket_name": "travel-sample",
      "grantee": "anil",
      "role": "select"
    }
  },
  {
    "applicable_roles": {
      "bucket_name": "*",
      "grantee": "anil",
      "role": "select"
    }
  }
]
```

For more examples, take a look at the blog: [Optimize SQL++ performance using request profiling](https://blog.couchbase.com/optimize-n1ql-performance-using-request-profiling/).

## [](#sys-dictionary)Monitor Statistics

The `system:dictionary` catalog maintains a list of the on-disk optimizer statistics stored in the `_query` collection within the `_system` scope.

If you have multiple query nodes, the data retrieved from this catalog will be the same, regardless of the node on which you run the query.

To see the list of on-disk optimizer statistics, use:

```sqlpp
SELECT * FROM system:dictionary;
```

This will result in a list similar to:

```json
[
  {
    "dictionary": {
      "avgDocKeySize": 12,
      "avgDocSize": 278,
      "bucket": "travel-sample",
      "distributionKeys": [
        "airportname",
        "faa",
        "city"
      ],
      "docCount": 1968,
      "indexes": [
        {
          "indexId": "bc3048e87bf84828",
          "indexName": "def_inventory_airport_primary",
          "indexStats": [
            {
              "avgItemSize": 24,
              "avgPageSize": 11760,
              "numItems": 1968,
              "numPages": 4,
              "resRatio": 1
            }
          ]
        },
        // ...
      ],
      "keyspace": "airport",
      "namespace": "default",
      "scope": "inventory"
    }
  },
  // ...
]
```

This catalog contains an array of dictionaries, one for each keyspace for which optimizer statistics are available. Each dictionary gives the following information:

| Name                            | Description                                                              | Schema                    |
| ------------------------------- | ------------------------------------------------------------------------ | ------------------------- |
| **avgDocKeySize** _required_    | Average doc key size.                                                    | Integer                   |
| **avgDocSize** _required_       | Average doc size.                                                        | Integer                   |
| **bucket** _required_           | The bucket for which statistics are available.                           | String                    |
| **keyspace** _required_         | The keyspace for which statistics are available.                         | String                    |
| **namespace** _required_        | The namespace for which statistics are available.                        | String                    |
| **scope** _required_            | The scope for which statistics are available.                            | String                    |
| **distributionKeys** _required_ | Distribution keys for which histograms are available.                    | String array              |
| **docCount** _required_         | Document count.                                                          | Integer                   |
| **indexes** _required_          | An array of indexes in this keyspace for which statistics are available. | [Indexes](#indexes) array |
| **node** _required_             | The query node where this dictionary cache is resident.                  | String                    |

**Indexes**

| Name                      | Description                                                                       | Schema                                |
| ------------------------- | --------------------------------------------------------------------------------- | ------------------------------------- |
| **indexId** _required_    | The index ID.                                                                     | String                                |
| **indexName** _required_  | The index name.                                                                   | String                                |
| **indexStats** _required_ | An array of statistics for each index, with one element for each index partition. | [Index Statistics](#indexStats) array |

**Index Statistics**

| Name                       | Description        | Schema  |
| -------------------------- | ------------------ | ------- |
| **avgItemSize** _required_ | Average item size. | Integer |
| **avgPageSize** _required_ | Average page size. | Integer |
| **numItems** _required_    | Number of items.   | Integer |
| **numPages** _required_    | Number of pages.   | Integer |
| **resRatio** _required_    | Resident ratio.    | Integer |

For further details, see [UPDATE STATISTICS](../n1ql-language-reference/updatestatistics.md).

## [](#sys-dictionary-cache)Monitor Cached Statistics

The `system:dictionary_cache` catalog maintains a list of the in-memory cached subset of the optimizer statistics.

If you have multiple query nodes, the data retrieved from this node shows cached optimizer statistics from all nodes. Individual nodes may have a different subset of cached information.

To see the list of in-memory optimizer statistics, use:

```sqlpp
SELECT * FROM system:dictionary_cache;
```

This will result in a list similar to:

```json
[
  {
    "dictionary_cache": {
      "avgDocKeySize": 12,
      "avgDocSize": 278,
      "bucket": "travel-sample",
      "distributionKeys": [
        "airportname",
        "faa",
        "city"
      ],
      "docCount": 1968,
      "indexes": [
        {
          "indexId": "bc3048e87bf84828",
          "indexName": "def_inventory_airport_primary",
          "indexStats": [
            {
              "avgItemSize": 24,
              "avgPageSize": 11760,
              "numItems": 1968,
              "numPages": 4,
              "resRatio": 1
            }
          ]
        },
        // ...
      ],
      "keyspace": "airport",
      "namespace": "default",
      "node": "172.23.0.3:8091",
      "scope": "inventory"
    }
  },
  // ...
]
```

This catalog contains an array of dictionary caches, one for each keyspace for which optimizer statistics are available. Each dictionary cache gives the same information as the [system:dictionary](#sys-dictionary) catalog.

For further details, see [UPDATE STATISTICS](../n1ql-language-reference/updatestatistics.md).

## [](#sys-functions)Monitor Functions

The `system:functions` catalog maintains a list of all user-defined functions across all nodes. To see the list of all user-defined functions, use:

```sqlpp
SELECT * FROM system:functions;
```

This will result in a list similar to:

```json
[
  {
    "functions": {
      "definition": {
        "#language": "inline",
        "expression": "(((`fahrenheit` - 32) * 5) / 9)",
        "parameters": [
          "fahrenheit"
        ],
        "text": "((fahrenheit - 32) * 5/9)"
      },
      "identity": {
        "bucket": "travel-sample",
        "name": "celsius",
        "namespace": "default",
        "scope": "inventory",
        "type": "scope"
      }
    }
  },
  {
    "functions": {
      "definition": {
        "#language": "javascript",
        "library": "geohash-js",
        "name": "geohash-js",
        "object": "calculateAdjacent",
        "parameters": [
          "src",
          "dir"
        ]
      },
      "identity": {
        "name": "adjacent",
        "namespace": "default",
        "type": "global"
      }
    }
  },
  // ...
]
```

This catalog contains the following attributes:

| Name                      | Description                     | Schema                           |
| ------------------------- | ------------------------------- | -------------------------------- |
| **definition** _required_ | The definition of the function. | [Definition](#definition) object |
| **identity** _required_   | The identity of the function.   | [Identity](#identity) object     |

**Definition**

| Name                      | Description                                                                                                                                 | Schema       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **#language** _required_  | The language of the function. **Example**: inline                                                                                           | String       |
| **parameters** _required_ | The parameters required by the function.                                                                                                    | String array |
| **expression** _optional_ | For inline functions only: the expression defining the function.                                                                            | String       |
| **text** _optional_       | For inline functions: the verbatim text of the function. For SQL++ managed user-defined functions: the external code defining the function. | String       |
| **library** _optional_    | For external functions only: the library containing the function.                                                                           | String       |
| **name** _optional_       | For external functions only: the relative name of the library.                                                                              | String       |
| **object** _optional_     | For external functions only: the object defining the function.                                                                              | String       |

**Identity**

| Name                     | Description                                                    | Schema |
| ------------------------ | -------------------------------------------------------------- | ------ |
| **name** _required_      | The name of the function.                                      | String |
| **namespace** _required_ | The namespace of the function. **Example**: default            | String |
| **type** _required_      | The type of the function. **Example**: global                  | String |
| **bucket** _optional_    | For scoped functions only: the bucket containing the function. | String |
| **scope** _optional_     | For scoped functions only: the scope containing the function.  | String |

## [](#sys-functions-cache)Monitor Cached Functions

The `system:functions_cache` catalog maintains a list of recently-used user-defined functions across all nodes. The catalog also lists user-defined functions that have been called recently, but do not exist. To see the list of recently-used user-defined functions, use:

```sqlpp
SELECT * FROM system:functions_cache;
```

This will result in a list similar to:

```json
[
  {
    "functions_cache": {
      "#language": "inline",
      "avgServiceTime": "3.066847ms",
      "expression": "(((`fahrenheit` - 32) * 5) / 9)",
      "lastUse": "2022-03-09 00:17:59.60659793 +0000 UTC m=+35951.429537902",
      "maxServiceTime": "3.066847ms",
      "minServiceTime": "0s",
      "name": "celsius",
      "namespace": "default",
      "node": "127.0.0.1:8091",
      "parameters": [
        "fahrenheit"
      ],
      "scope": "inventory",
      "text": "((fahrenheit - 32) * 5/9)",
      "type": "scope",
      "uses": 1
    }
  },
  {
    "functions_cache": {
      "#language": "javascript",
      "avgServiceTime": "56.892636ms",
      "lastUse": "2022-03-09 00:15:46.289934029 +0000 UTC m=+35818.007560703",
      "library": "geohash-js",
      "maxServiceTime": "146.025426ms",
      "minServiceTime": "0s",
      "name": "geohash-js",
      "namespace": "default",
      "node": "127.0.0.1:8091",
      "object": "calculateAdjacent",
      "parameters": [
        "src",
        "dir"
      ],
      "type": "global",
      "uses": 4
    }
  },
  {
    "functions_cache": {
      "avgServiceTime": "3.057421ms",
      "lastUse": "2022-03-09 00:17:25.396840275 +0000 UTC m=+35917.199008929",
      "maxServiceTime": "3.057421ms",
      "minServiceTime": "0s",
      "name": "notFound",
      "namespace": "default",
      "node": "127.0.0.1:8091",
      "type": "global",
      "undefined_function": true,
      "uses": 1
    }
  }
]
```

This catalog contains the following attributes:

| Name                               | Description                                                                                                                                 | Schema       |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **#language** _required_           | The language of the function. **Example**: inline                                                                                           | String       |
| **name** _required_                | The name of the function.                                                                                                                   | String       |
| **namespace** _required_           | The namespace of the function. **Example**: default                                                                                         | String       |
| **parameters** _required_          | The parameters required by the function.                                                                                                    | String array |
| **type** _required_                | The type of the function. **Example**: global                                                                                               | String       |
| **scope** _optional_               | For scoped functions only: the scope containing the function.                                                                               | String       |
| **expression** _optional_          | For inline functions only: the expression defining the function.                                                                            | String       |
| **text** _optional_                | For inline functions: the verbatim text of the function. For SQL++ managed user-defined functions: the external code defining the function. | String       |
| **library** _optional_             | For external functions only: the library containing the function.                                                                           | String       |
| **object** _optional_              | For external functions only: the object defining the function.                                                                              | String       |
| **avgServiceTime** _required_      | The mean service time for the function.                                                                                                     | String       |
| **lastUse** _required_             | The date and time when the function was last used.                                                                                          | String       |
| **maxServiceTime** _required_      | The maximum service time for the function.                                                                                                  | String       |
| **minServiceTime** _required_      | The minimum service time for the function.                                                                                                  | String       |
| **node** _required_                | The query node where the function is cached.                                                                                                | String       |
| **undefined\_function** _required_ | Whether the function exists or is undefined.                                                                                                | Boolean      |
| **uses** _required_                | The number of uses of the function.                                                                                                         | Number       |

Each query node keeps its own cache of recently-used user-defined functions, so you may see the same function listed for multiple nodes.

## [](#sys-tasks-cache)Monitor Cached Tasks

The `system:tasks_cache` catalog maintains a list of recently-used scheduled tasks, such as index advisor sessions. To see the list of recently-used scheduled tasks, use:

```sqlpp
SELECT * FROM system:tasks_cache;
```

This will result in a list similar to:

```json
[
  {
    "tasks_cache": {
      "class": "advisor",
      "delay": "1h0m0s",
      "id": "bcd9f8e4-b324-504c-a98b-ace90dba869f",
      "name": "aa7f688a-bf29-438f-888f-eeaead87ca40",
      "node": "10.143.192.101:8091",
      "state": "scheduled",
      "subClass": "analyze",
      "submitTime": "2019-09-17 05:18:12.903122381 -0700 PDT m=+8460.550715992"
    }
  },
  {
    "tasks_cache": {
      "class": "advisor",
      "delay": "5m0s",
      "id": "254abec5-5782-543e-9ee0-d07da146b94e",
      "name": "ca2cfe56-01fa-4563-8eb0-a753af76d865",
      "node": "10.143.192.101:8091",
      "results": [
        // ...
      ],
      "startTime": "2019-09-17 05:03:31.821597725 -0700 PDT m=+7579.469191487",
      "state": "completed",
      "stopTime": "2019-09-17 05:03:31.963133954 -0700 PDT m=+7579.610727539",
      "subClass": "analyze",
      "submitTime": "2019-09-17 04:58:31.821230131 -0700 PDT m=+7279.468823737"
    }
  }
]
```

This catalog contains the following attributes:

| Name                      | Description                                                        | Schema             |
| ------------------------- | ------------------------------------------------------------------ | ------------------ |
| **class** _required_      | The class of the task. **Example**: advisor                        | string             |
| **delay** _required_      | The scheduled duration of the task.                                | string             |
| **id** _required_         | The internal ID of the task.                                       | string             |
| **name** _required_       | The name of the task.                                              | string             |
| **node** _required_       | The node where the task was started.                               | string             |
| **state** _required_      | The state of the task. **Values**: scheduled, cancelled, completed | string             |
| **subClass** _required_   | The subclass of the task. **Example**: analyze                     | string             |
| **submitTime** _required_ | The date and time when the task was submitted.                     | string             |
| **results** _optional_    | Not scheduled tasks: the results of the task.                      | Any array          |
| **startTime** _optional_  | Not scheduled tasks: the date and time when the task started.      | string (date-time) |
| **stopTime** _optional_   | Not scheduled tasks: the date and time when the task stopped.      | string (date-time) |

Refer to [ADVISOR Function](../n1ql-language-reference/advisor.md) for more information on index advisor sessions.

## [](#sys-transactions)Monitor Transactions

The `system:transactions` catalog maintains a list of active Couchbase transactions. To see the list of active transactions, use:

```sqlpp
SELECT * FROM system:transactions;
```

This will result in a list similar to:

```json
[
  {
    "transactions": {
      "durabilityLevel": "majority",
      "durabilityTimeout": "2.5s",
      "expiryTime": "2021-04-21T12:53:48.598+01:00",
      "id": "85aea637-2288-434b-b7c5-413ad8e7c175",
      "isolationLevel": "READ COMMITED",
      "lastUse": "2021-04-21T12:51:48.598+01:00",
      "node": "127.0.0.1:8091",
      "numAtrs": 1024,
      "scanConsistency": "unbounded",
      "status": 0,
      "timeout": "2m0s",
      "usedMemory": 960,
      "uses": 1
    }
  // ...
  }
]
```

This catalog contains the following attributes:

| Name                             | Description                                              | Schema             |
| -------------------------------- | -------------------------------------------------------- | ------------------ |
| **durabilityLevel** _required_   | Durability level for all mutations within a transaction. | string             |
| **durabilityTimeout** _required_ | Durability timeout per mutation within the transaction.  | string (duration)  |
| **expiryTime** _required_        |                                                          | string (date-time) |
| **id** _required_                | The transaction ID.                                      | string             |
| **isolationLevel** _required_    | The isolation level of the transaction.                  | string             |
| **lastUse** _required_           |                                                          | string (date-time) |
| **node** _required_              | The node where the transaction was started.              | string             |
| **numAtrs** _required_           | The total number of active transaction records.          | integer            |
| **scanConsistency** _required_   | The transactional scan consistency.                      | string             |
| **status** _required_            |                                                          | integer            |
| **timeout** _required_           | The transaction timeout duration.                        | string (duration)  |
| **usedMemory** _required_        |                                                          | integer            |
| **uses** _required_              |                                                          | integer            |

Refer to [SQL++ Support for Couchbase Transactions](../n1ql-language-reference/transactions.md) for more information.

## [](#sys-sequences)Monitor Sequences

The `system:sequences` catalog maintains a list of loaded sequences on any node: that is, sequences that have been accessed since the last restart. To see the list of loaded sequences, use:

```sqlpp
SELECT * FROM system:sequences;
```

This will result in a list similar to:

```json
[
  {
    "sequences": {
      "bucket": "travel-sample",
      "cache": 50,
      "cycle": false,
      "increment": 1,
      "max": 9223372036854776000,
      "min": -9223372036854776000,
      "name": "seq1",
      "namespace": "default",
      "namespace_id": "default",
      "path": "`default`:`travel-sample`.`inventory`.`seq1`",
      "scope_id": "inventory",
      "value": {
        "73428daec3c68d8632ae66b09b70f14d": null,
        "~next_block": 0
      }
    }
  },
// ...
]
```

This catalog contains the following attributes:

| Name                         | Description                                           | Schema                  |
| ---------------------------- | ----------------------------------------------------- | ----------------------- |
| **bucket** _required_        | The bucket containing the sequence.                   | string                  |
| **cache** _required_         | The sequence’s cache size.                            | integer                 |
| **cycle** _required_         | Whether the sequence is set to cycle.                 | boolean                 |
| **increment** _required_     | The sequence step value.                              | integer                 |
| **min** _required_           | The minimum value permitted for the sequence.         | integer                 |
| **max** _required_           | The maximum value permitted for the sequence.         | integer                 |
| **name** _required_          | The name of the sequence.                             | string                  |
| **namespace** _required_     | Namespace to which the sequence belongs.              | string                  |
| **namespace\_id** _required_ | ID of the namespace to which the sequence belongs.    | string                  |
| **path** _required_          | The fully qualified sequence name.                    | string                  |
| **scope\_id** _required_     | ID of the scope to which the sequence belongs.        | string                  |
| **value** _required_         | The current value of the sequence on each Query node. | [Values](#value) object |

**Values**

| Name                         | Description                                                                                                                          | Schema  |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| **<UUID>** _required_        | The name of this property is the UUID of a Query node. The value of this property is the current value of the sequence on that node. | Integer |
| **\~next\_block** _optional_ | The starting vale of the next block of values that can be reserved for the sequence.                                                 | Integer |

For further details, see [CREATE SEQUENCE](../n1ql-language-reference/createsequence.md).

## [](#sys-all-sequences)Monitor All Sequences

The `system:all_sequences` catalog maintains a list of all defined sequences. To see the list of all defined sequences, use:

```sqlpp
SELECT * FROM system:all_sequences;
```

This will result in a list similar to:

```json
[
  {
    "sequences": {
      "bucket": "travel-sample",
      "cache": 50,
      "cycle": false,
      "increment": -1,
      "max": 9223372036854776000,
      "min": 0,
      "name": "seq4",
      "namespace": "default",
      "namespace_id": "default",
      "path": "`default`:`travel-sample`.`inventory`.`seq4`",
      "scope_id": "inventory",
      "value": {
        "73428daec3c68d8632ae66b09b70f14d": 10,
        "~next_block": -40
      }
    }
  },
  {
    "sequences": {
      "bucket": "travel-sample",
      "cache": 50,
      "cycle": true,
      "increment": 5,
      "max": 1000,
      "min": 0,
      "name": "seq3",
      "namespace": "default",
      "namespace_id": "default",
      "path": "`default`:`travel-sample`.`inventory`.`seq3`",
      "scope_id": "inventory",
      "value": {
        "73428daec3c68d8632ae66b09b70f14d": 5,
        "~next_block": 255
      }
    }
  },
// ...
]
```

This catalog gives the same information as the [system:sequences](#sys-sequences) catalog.

For further details, see [CREATE SEQUENCE](../n1ql-language-reference/createsequence.md).

## [](#related-links)Related Links

* Refer to [Manage and Monitor Queries](../n1ql-manage/monitoring-n1ql-query.md) for more information on the system namespace.