---
title: Getting Cluster Rebalance Reason Codes
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/reference/pages/rest-retrieve-cluster-rebalance-reason-codes.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:2.0@enterprise-analytics:reference:rest-retrieve-cluster-rebalance-reason-codes.adoc[]
---

[View original HTML](/enterprise-analytics/2.0/reference/rest-retrieve-cluster-rebalance-reason-codes.html)

# Getting Cluster Rebalance Reason Codes

> When the cluster/bucket/service needs to be rebalanced, you can retrieve the reason for the rebalance using the 'GET /pools/default' method. 

## [](#http-method-and-uri)HTTP method and URI

GET /pools/default

## [](#rest-cluster-rebalance-reason-description)Description

At any point that the service needs rebalancing, you can use this method to obtain a detailed description of the reasons that the rebalance is required.

The reason code(s) can be one or more of the following:

* Service isn’t balanced.
* Servers aren’t balanced.
* The number of replicas has changed.
* The bucket map isn’t balanced.

> [!NOTE]
> The service returns the reason code only if a rebalance is required.

## [](#curl-syntax)Curl Syntax

```none
curl -v -X GET -u [admin]:[password]
  http://[localhost]:8091/pools/default
```

## [](#response)Response

On success, the response code `200 OK` is given, and one or more reason codes are givem in the returned message.

Returned JSON object (truncated)

```json5
{
  "name": "default",

  "rebalanceStatus": "none",
  "rebalanceProgressUri": "/pools/default/rebalanceProgress",
  "stopRebalanceUri": "/controller/stopRebalance?uuid=8a05ca2847bc28ac92a484c9248fb261",
  "nodeStatusesUri": "/nodeStatuses",
  "nodeServicesUri": "/pools/default/nodeServices?v=89141026",
  "maxBucketCount": 30,
  "maxCollectionCount": 1200,
  "maxScopeCount": 1200,
  "minReplicasCount": 0,
  "tasks": {
    "uri": "/pools/default/tasks?v=86199101"
  },

  "servicesNeedRebalance": [
    {
      "code": "service_not_balanced",
      "description": "Service needs rebalance.",
      "services": [
        "kv",
        "n1ql",
        "index",
        "fts",
        "cbas",
        "eventing",
        "backup"
      ]
    }
  ],
  "bucketsNeedRebalance": [
    {
      "code": "servers_not_balanced",
      "description": "Servers of bucket are not balanced.",
      "buckets": [
        "travel-sample"
      ]
    },
    {
      "code": "num_replicas_changed",
      "description": "Number of replicas for bucket has changed.",
      "buckets": ["default", "travel-sample"]
    },

    {
      "code": "servers_not_balanced",
      "description": "Bucket map needs rebalance.",
      "buckets": ["travel-sample"]
    }
  ],
  "serverGroupsUri": "/pools/default/serverGroups?v=20914152"
}
```

## [](#see-also)See Also

For information about rebalancing, see the following:

[REST API – Rebalance](rest-rebalance-overview.md)