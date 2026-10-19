---
title: Query Plan Cache
description: This topic describes how the query plan cache reduces compilation
  time for repeated read queries.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/sqlpp/pages/5d-query-plan-cache.adoc
  xref: xref:enterprise-analytics:sqlpp:5d-query-plan-cache.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/sqlpp/5d-query-plan-cache.html)

# Query Plan Cache

> This topic describes how the query plan cache reduces compilation time for repeated read queries. 

Every time Operational Insights runs a query, it compiles the query text into an execution plan before running it. Compiling a plan involves parsing the query and optimizing it, and optimization is typically the most expensive part of compilation.

The query plan cache stores the optimized plan for a query that Operational Insights has already compiled. The next time the same query arrives, Operational Insights reuses the stored plan instead of optimizing the query again.

Applications and dashboards often run the same queries repeatedly, such as to populate dashboard filters. The query plan cache removes the repeated cost of optimization for these queries, so they start executing faster. Operational Insights skips only the optimization step. It still prepares and executes every query against live data, so results are always current.

The reduction in compilation time is more significant when the cost-based optimizer (CBO) is enabled, since plan enumeration and costing, which dominate compile time under CBO, are bypassed entirely when a cached plan is reused. For more information, see [Cost-Based Optimizer](5b%5Fcbo.md).

> [!NOTE]
> * Operational Insights caches plans only for `SELECT` statements. Operational Insights does not cache data definition statements, such as `CREATE` and `DROP`. It also does not cache data modification statements, such as `INSERT`, `UPSERT`, and `DELETE`.
> * Automatic cache invalidation clears the entire cache, even if an operation could invalidate only 1 cached plan. The affected queries re-optimize on their next run.
> * Operational Insights caches a plan as soon as it compiles successfully, before execution. A runtime error does not prevent caching. Only a compilation error prevents caching.

## [](#how-it-works)How It Works

Operational Insights shares the query plan cache across the cluster. The capacity of the query plan cache is configurable through the `queryPlanCacheCapacity` service-level parameter, which specifies the maximum number of plans the cache retains. The default is `1000`. When the cache is full, Operational Insights evicts the least recently used plan to make room for a new one. Setting the capacity to `0` disables the query plan cache. A capacity change takes effect immediately, without requiring a restart.

The first time Operational Insights runs a query, that's a cache miss: it compiles and optimizes the query as usual, runs it, and stores the resulting plan in the cache. The next time the same query runs, that's a cache hit: Operational Insights reuses the stored plan and skips optimization, then prepares and executes the query against live data as normal.

## [](#changing-the-cache-capacity)Changing the Cache Capacity

Use the Service Config API to change the query plan cache capacity for the cluster.

```console
curl -v -u $USER:$PASSWORD -X PUT \
     -d queryPlanCacheCapacity=2000 \
     http://$ANALYTICS_HOST:8095/analytics/config/service
```

## [](#cache-key)Cache Key

Operational Insights reuses a cached plan only when an incoming request matches a previous request on all of the following:

* The query text, exactly as submitted. A different whitespace character or a changed literal produces a different query.
* The query settings. Any request parameter that can affect the optimized plan counts as part of the query.
* The default namespace, that's, the database and scope that unqualified names resolve against. Because you can set this outside the query text using the REST `query_context` request parameter, identical queries run under different `query_context` values key differently.
* The requesting user. Operational Insights never reuses a plan compiled for one user on a request from a different user.
* The max-warnings limit for the request.

If any of these differ from a previous request, Operational Insights optimizes the query fresh instead of reusing a cached plan.

### [](#parameterized-queries)Parameterized Queries

For a parameterized query, Operational Insights binds the cached plan to the specific parameter values used during execution. Running the query again with identical parameter values produces a cache hit. Any variation in parameter values produces a cache miss and a new plan. As a result, Operational Insights reuses a plan only when the query text and every parameter value match exactly. This applies to both rule-based and cost-based optimization, so Operational Insights never applies a plan optimized for 1 set of values to another.

## [](#checking-whether-a-query-used-the-cache)Checking Whether a Query Used the Cache

The query response includes a top-level `cachedPlan` field that reports whether Operational Insights used the cache for the request, as in the following example:

```SQL++
{
    "requestID": "...",
    "signature": { "*": "*" },
    "results": [ ... ],
    "cachedPlan": true,
    "metrics": { ... },
    "status": "success"
}
```

`cachedPlan` is `true` when Operational Insights reused a cached plan, and `false` when it optimized the query fresh. If you run the same query twice, the first response reports `false` and the second reports `true`.

The `compileTime` field in the response `metrics` is also a useful signal. On a cache hit, Operational Insights skips optimization, so `compileTime` can drop noticeably compared to the first run.

## [](#skipping-the-cache-for-a-request)Skipping the Cache for a Request

To optimize a query fresh without looking up or storing a cached plan, send the request parameter `skip-plan-cache=true`. Operational Insights leaves the cache untouched for that request. Use this parameter to force a clean optimization for a single run without affecting other requests.

To disable the cache entirely for a request instead, use the `compiler.query.plan.cache` parameter. For more information, see [Query Plan Cache Parameter](appendix%5F2%5Fparameters.md#Query%5Fplan%5Fcache%5Fparameter).

## [](#automatic-cache-invalidation)Automatic Cache Invalidation

Operational Insights automatically clears the entire query plan cache whenever an operation runs that could change the optimal plan for a query. You do not need to clear the cache manually after a schema change.

The following operations clear the cache:

* `CREATE_INDEX`
* `INDEX_DROP`
* `DATABASE_DROP`
* `DATAVERSE_DROP`
* `DATASET_DROP`
* `CREATE_VIEW`
* `VIEW_DROP`
* `CREATE_FUNCTION`
* `FUNCTION_DROP`
* `CREATE_LIBRARY`
* `LIBRARY_DROP`
* `SYNONYM_DROP`
* `ANALYZE`
* `ANALYZE_DROP`

A cluster topology change also clears the cache, as does creating, altering, or dropping a Link.

## [](#see-also)See Also

* [Query Plan Cache Parameter](appendix%5F2%5Fparameters.md#Query%5Fplan%5Fcache%5Fparameter)
* [Cost-Based Optimizer](5b%5Fcbo.md)
* [Index Advisor](5c-index-advisor.md)