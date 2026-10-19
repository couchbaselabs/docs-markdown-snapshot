---
title: Multi-Statement Requests
description: This topic describes how to run more than 1 SQL++ statement in a
  single Analytics Service request.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/multi-statement-requests.adoc
  xref: xref:enterprise-analytics:reference:multi-statement-requests.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/multi-statement-requests.html)

# Multi-Statement Requests

> This topic describes how to run more than 1 SQL++ statement in a single Analytics Service request. 

A request to the [Request](../analytics-rest-service/index.md#operation/post%5Fservice) endpoint can contain more than 1 SQL++ statement, separated by semicolons. Operational Insights runs the statements in the order you submit them. A request with 2 or more statements, other than `USE` or `SET`, returns a separate entry for each statement in a top-level `statements` array, instead of the flat response shape of a single-statement request.

> [!NOTE]
> * A request with 0 (only `USE`/`SET`) or 1 other statement always returns the flat response shape, whatever `multi-statement` is set to.
> * If a later statement fails, Operational Insights does not undo the statements that already ran; their effects persist.

## [](#description)Enabling Multi-Statement Requests

By default, `multi-statement` is `false`. To submit more than 1 statement, separate each statement with a semicolon (`;`) in the `statement` request parameter, and set the `multi-statement` request parameter to `true`.

If a request contains 2 or more statements while `multi-statement` is `false` or absent, Operational Insights rejects the entire request with error `21003`: `This request contains multiple statements; set the request parameter 'multi-statement' to true to execute them in a single request`, and no statements run.

## [](#response-format)Response Format

Whether Operational Insights wraps the response in a `statements` array depends on how many statements the request contains:

| Statements other than USE/SET                 | Response shape                                                                       |
| --------------------------------------------- | ------------------------------------------------------------------------------------ |
| 0 (a request containing only USE/SET) or 1    | Flat, exactly as for a single-statement request, whatever multi-statement is set to. |
| 2 or more, multi-statement is true            | A statements array, with 1 entry for each statement that ran.                        |
| 2 or more, multi-statement is absent or false | Rejected with error 21003. Nothing runs.                                             |

The response shape is decided by the statements that actually start running. If the first statement fails, Operational Insights returns a flat error, not a `statements` array. See [Statement Execution Order, Errors, and HTTP Status](#execution-order-and-errors).

Request-level fields—\`requestID\`, `clientContextID`, `cachedPlan`, `status`, and `metrics`—stay at the top level of the response in both shapes. `cachedPlan` is `true` if any statement in the request used a cached plan. Request-level `metrics` holds only `elapsedTime`, `executionTime`, and `errorCount` (if a statement failed).

Each entry in the `statements` array carries:

* `statementId`: The statement's 1-based position in the request, matching submission order.
* `signature` and `results`: For a statement that returns rows. A statement running in `deferred` mode carries `handle` instead of `results`.
* `plans`: The statement's own execution plans, if you requested them, or `{}` otherwise.
* `status`: `success` or `fatal`.
* `errors`: Present on a failed statement.
* `warnings`: The statement's own warnings. The `max-warnings` budget applies per statement.
* `metrics`: The statement's own `compileTime`, `queueWaitTime`, `resultCount`, `resultSize`, `processedObjects`, `warningCount` (if greater than 0), and `bufferCacheHitRatio`/`bufferCachePageReadCount` (only when the statement read stored data). A statement's `metrics` does not include `elapsedTime`, `executionTime`, or `errorCount`—those are request-level only.

`DDL`, `DML`, `USE`, and `SET` statements carry no `signature` or `results`. `USE` and `SET` each get their own entry in the `statements` array, but only when the request contains 2 or more other statements. When a single other statement is present, a leading `USE` or `SET` still executes and applies, but is folded into that one flat response instead of appearing as its own entry.

## [](#execution-order-and-errors)Statement Execution Order, Errors, and HTTP Status

Operational Insights executes statements in the order you submit them, and stops at the first one that fails. Statements before the failure have already run and their entries are returned; statements after the failure do not run, and the response contains no entry for them. A failed statement's entry carries its `statementId`, `status` of `fatal`, and an `errors` array.

The HTTP status code depends on how much of the request ran:

* `200 OK`, with a `statements` array: at least 2 statements ran (the failed one included), and at least 1 of them succeeded. The top-level `status` is `success`, and `errorCount` is `1`.
* A flat error, with a 4xx status: fewer than 2 statements ran before the failure—for example, the first statement fails, or a request contains 1 other statement plus a `USE` that fails. Nothing that ran is returned.

A syntax error is always a flat error, whatever `multi-statement` is set to, because parsing fails before any statement runs.

## [](#cross-statement-parameters)Request Parameters

Some request parameters apply differently when a request contains multiple statements.

* **timeout**: Applies to the whole request, not to each statement. On timeout, Operational Insights does not return entries for statements that already completed.
* **max-warnings**: Applies separately to each statement. `warningCount` counts every warning a statement raises, even beyond the `max-warnings` cap.
* **readonly**: Applies to the whole request, and is checked before any statement runs.
* **query\_context**: Applies to every statement in the request, and gets no entry of its own.  
An explicit `USE` statement takes precedence over `query_context` for the statements after it, and gets its own entry when the request contains 2 or more other statements. If the scope named in `query_context` does not exist, Operational Insights ignores it and uses `Default.Default` instead. If the scope named in an explicit `USE` statement does not exist, that statement fails.
* **SET**: A `SET` statement applies only to the statements that follow it in the same request, not to statements before it.

Operational Insights plans and costs each statement as if you'd sent it alone, using the same plan and memory estimate either way.

## [](#authorization)Authorization

If the requesting user has no Analytics access at all, Operational Insights refuses the whole request (`401` or `403`), and nothing runs.

Operational Insights checks write and DDL permissions separately for each statement. A statement that fails this check fails with error `20001` in its own entry, and stops the request the same way any other failure does. Earlier statements have already run.

## [](#delivery-modes)Delivery Modes

Operational Insights rejects a multi-statement request submitted with `mode` set to `async`, with error `24320`. A single-statement `async` request is unchanged.

To retrieve results from multiple statements independently, use `mode` set to `deferred` instead. Operational Insights returns 1 `handle` per result-producing statement, and you can fetch each handle in any order.

`EXPLAIN` and `ADVISE` statements are an exception in either mode: Operational Insights always returns their plan or advice directly in `results`, instead of a handle.

## [](#auditing)Auditing

Operational Insights writes 1 audit event for each statement that ran, under that statement's own event type, such as `SELECT` or `UPSERT`, with its own statement text, status, and metrics. All the events from 1 request share that request's `requestId`. Statements that did not run produce no audit event.

A flat request—a single statement, a rejected `21003` request, a syntax error, a first-statement failure, or a timeout—produces 1 audit event covering the whole request text.

## [](#job-tracking)Job Tracking for Active and Completed Requests

Before multi-statement requests, a request created exactly 1 job, and [Active Requests](../analytics-rest-admin/index.md#operation/return%5Factive%5Frequests) and [Completed Requests](../analytics-rest-admin/index.md#operation/completed%5Frequests) each described it directly at the top level. This does not apply to [Open Requests](../analytics-rest-admin/index.md#operation/open%5Frequests). A multi-statement request creates 1 job per result-producing statement. `USE`, `SET`, `EXPLAIN`, and DDL statements create no job, so the `jobs` array can contain fewer entries than the `statements` array—match entries between them by `statementId`, not by array position.

> [!IMPORTANT]
> For a multi-statement request, the top-level job fields summarize the request as a whole, not any single job: `jobId` is `null`; `jobCreateTime` and `jobStartTime` are the first job's; `jobEndTime` is the last job's; `jobQueueTime` is the total across every job; `jobRequiredCPUs` and `jobRequiredMemory` are the peak across every job; and `jobStatus` and `error` report the failed job, if any job failed.

Every request, including a single-statement one, returns a `jobs` array, listing each job's `statementId`, `jobId`, `jobStatus`, and timings.

## [](#cancellation)Cancelling a Multi-Statement Request

Use [Request Cancellation](../analytics-rest-admin/index.md#operation/cancel%5Frequest) to stop a multi-statement request. Because Operational Insights runs statements 1 at a time, at most 1 job is running when you cancel:

* If a cancellable job is running, Operational Insights cancels it, and the request stops—statements after it do not run.
* If the currently running statement cannot be cancelled, such as a `CREATE INDEX`, cancellation is refused with `403 Forbidden`, and the request continues.
* If no job is running when the cancellation arrives—between 2 statements, or while a statement is being compiled—Operational Insights stops the request before the next statement starts.

Jobs from statements that already finished are left alone: cancelling a request does not take away results or deferred handles you already have for statements that already completed.

## [](#fetching-deferred-results)Fetching Deferred Results and Status

For a `deferred` multi-statement request, use [Retrieve Request Result](../analytics-rest-service/index.md#operation/get%5Frequest%5Fresult) and [Request Status](../analytics-rest-service/index.md#operation/get%5Frequest%5Fstatus) to fetch each statement's handle independently, in any order, until you consume it or it expires.

## [](#workbench)Workbench Behavior

The Workbench's Run-Time Preferences dialog, opened from the Settings icon, includes **Support Multiple Statements**, selected by default. Clear **Support Multiple Statements** to reject a request that contains 2 or more statements, other than `USE` or `SET`, the same way `multi-statement: false` does over the REST API.

When you run a multi-statement request in the Workbench:

* Each statement's results appear separately, in the order you submitted them.
* A statement that fails shows its own error, and any statements after it show no results, because they did not run.
* Charts, the graphical query plan, `ADVISE`, and the Index Advisor are not available for a multi-statement request. Each statement's plan is available as text instead.

On the Monitor page, a multi-statement request appears as a single row under Active Requests or Completed Requests. If the request submitted more than 1 job, Operational Insights shows every job's plan for that row. A multi-statement request does not appear under Open Requests.

## [](#examples)Examples

The following examples show common multi-statement request scenarios.

### [](#example-multiple-statements-in-1-request)Example: Multiple statements in 1 request

The following request queries a collection, then queries a literal value.

curl -v -H "Content-Type: application/json" -d '{
    "statement": "SELECT id FROM sampleAnalytics.Commerce.customers LIMIT 1; SELECT 1;",
    "multi-statement": true
}' http://<analytics-host>:8095/api/v1/request

The response contains 1 entry per statement, each identified by its `statementId`.

{
    "requestID": "<uuid>",
    "statements": [
        {
            "statementId": 1,
            "signature": { "*": "*" },
            "results": [ { "id": 1 } ],
            "plans": {},
            "status": "success",
            "metrics": { "compileTime": "...", "queueWaitTime": "...", "resultCount": 1, "resultSize": 8, "processedObjects": 1 }
        },
        {
            "statementId": 2,
            "signature": { "*": "*" },
            "results": [ { "$1": 1 } ],
            "plans": {},
            "status": "success",
            "metrics": { "compileTime": "...", "queueWaitTime": "...", "resultCount": 1, "resultSize": 15, "processedObjects": 0 }
        }
    ],
    "cachedPlan": false,
    "status": "success",
    "metrics": { "elapsedTime": "...", "executionTime": "..." }
}

### [](#example-not-opted-in)Example: Not opted in

The following request contains 2 statements, but does not set `multi-statement`. Operational Insights rejects it, and neither statement runs.

curl -v -H "Content-Type: application/json" -d '{
    "statement": "SELECT 1; SELECT 2;"
}' http://<analytics-host>:8095/api/v1/request

{
    "requestID": "<uuid>",
    "errors": [
        { "code": 21003, "msg": "This request contains multiple statements; set the request parameter 'multi-statement' to true to execute them in a single request" }
    ],
    "status": "fatal",
    "metrics": { "errorCount": 1 }
}

### [](#example-a-later-statement-fails)Example: A later statement fails

The following request queries an existing collection, then a collection that does not exist. Because at least 1 of the 2 statements succeeded, the request returns `200 OK`.

curl -v -H "Content-Type: application/json" -d '{
    "statement": "SELECT id FROM sampleAnalytics.Commerce.customers LIMIT 1; SELECT * FROM sampleAnalytics.Commerce.no_such_collection;",
    "multi-statement": true
}' http://<analytics-host>:8095/api/v1/request

{
    "requestID": "<uuid>",
    "statements": [
        {
            "statementId": 1,
            "signature": { "*": "*" },
            "results": [ { "id": 1 } ],
            "plans": {},
            "status": "success",
            "metrics": { ... }
        },
        {
            "statementId": 2,
            "plans": {},
            "status": "fatal",
            "errors": [
                { "code": 24045, "msg": "Cannot find collection no_such_collection in scope Default.Commerce" }
            ],
            "metrics": { ... }
        }
    ],
    "cachedPlan": false,
    "status": "success",
    "metrics": { "elapsedTime": "...", "executionTime": "...", "errorCount": 1 }
}

### [](#example-the-first-statement-fails)Example: The first statement fails

The following request queries a collection that does not exist, then a literal value. Because the failing statement is the first one, fewer than 2 statements ran, so Operational Insights returns a flat error instead of a `statements` array, and the second statement never runs.

curl -v -H "Content-Type: application/json" -d '{
    "statement": "SELECT * FROM sampleAnalytics.Commerce.no_such_collection; SELECT 1;",
    "multi-statement": true
}' http://<analytics-host>:8095/api/v1/request

{
    "requestID": "<uuid>",
    "errors": [
        { "code": 24045, "msg": "Cannot find collection no_such_collection in scope Default.Commerce" }
    ],
    "status": "fatal",
    "metrics": { "errorCount": 1 }
}

### [](#example-deferred-multi-statement-request)Example: Deferred multi-statement request

The following request retrieves both statements' results as separate handles.

curl -v -H "Content-Type: application/json" -d '{
    "statement": "SELECT id FROM sampleAnalytics.Commerce.customers LIMIT 1; SELECT 1;",
    "multi-statement": true,
    "mode": "deferred"
}' http://<analytics-host>:8095/api/v1/request

{
    "requestID": "<uuid>",
    "statements": [
        {
            "statementId": 1,
            "signature": { "*": "*" },
            "handle": "http://<analytics-host>:8095/api/v1/request/result/<request_id>/0",
            "plans": {},
            "status": "success",
            "metrics": { ... }
        },
        {
            "statementId": 2,
            "signature": { "*": "*" },
            "handle": "http://<analytics-host>:8095/api/v1/request/result/<request_id>/1",
            "plans": {},
            "status": "success",
            "metrics": { ... }
        }
    ]
}

Fetch either handle independently, in any order, using [Retrieve Request Result](../analytics-rest-service/index.md#operation/get%5Frequest%5Fresult).

## [](#see-also)See Also

* [Request REST API](../analytics-rest-service/index.md)
* [Admin REST API](../analytics-rest-admin/index.md)
* [USE Statements](../sqlpp/5%5Fddl%5Fuse.md)