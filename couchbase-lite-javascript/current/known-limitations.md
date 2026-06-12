---
title: Known Limitations
description: Couchbase Lite JavaScript -- known limitations and constraints
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-js/edit/release/1.0/modules/ROOT/pages/known-limitations.adoc
pubDate: 2026-06-12T16:31:57.907Z
link: xref:couchbase-lite-javascript::known-limitations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite-javascript/current/known-limitations.html)

# Known Limitations

> Description — _Couchbase Lite JavaScript — known limitations and constraints_  
> _Abstract — This content identifies specific limitations and constraints when using Couchbase Lite JavaScript, including backend compatibility requirements and browser environment restrictions._  
> Related Content — [Compatibility](compatibility.md) | [Supported Browsers](supported-browsers.md)

## [](#overview)Overview

This page documents known limitations and constraints specific to Couchbase Lite JavaScript that affect deployment and usage in production environments.

## [](#backend-compatibility)Backend Compatibility

**Does not work with Couchbase Lite Edge Server**

CBL-JS clients cannot connect to Edge Server, which is designed only for native Couchbase Lite platforms (C, Swift, Java, Android, .NET, Objective-C).

CORS configuration is required for data synchronization using Sync Gateway or Capella App Services — see [Prerequisites](gs-prereqs.md#prerequisites).

## [](#browser-environment)Browser Environment Constraints

**Multiple browser tabs**

Opening the same database in multiple tabs simultaneously is not recommended and may cause data inconsistencies. The SDK does not provide cross-tab synchronization or locking.

**Private browsing limitations**

Sync behavior may be limited in private/incognito modes:

* Storage quotas are smaller
* Data may be cleared when session ends
* IndexedDB persistence is not guaranteed

## [](#missing-features)Missing Features (Not Yet Available)

The following features are planned but not currently available:

**No Peer-to-Peer (P2P) sync**

Direct device-to-device replication not supported; must sync through Sync Gateway or App Services.

**No intra-database sync (dbreplica)**

Cannot replicate between local databases on same device.

**No vector search indexes**

`EUCLIDEAN_DISTANCE()` and `COSINE_DISTANCE()` functions work but without index optimization, causing poor performance on large datasets.

**No full-text search (FTS) indexes**

`MATCH()` function not available; cannot perform efficient text search. See [Feature Limitations](compatibility.md#feature-limitations) for workaround options.

**Limited indexing capabilities**

No partial indexes, expression indexes, or multi-property compound indexes.

**Query limitations**

No `UNION`, `INTERSECT`, `EXCEPT`, `RIGHT OUTER JOIN`, `NEST`/`UNNEST`, `COLLATE`, or `EXISTS` operators. For complete query limitations, see [SQL++ Query Limitations](query-n1ql-mobile.md#limitations).

## [](#related-content)Related Content

* [Compatibility](compatibility.md)
* [Feature Limitations](compatibility.md#feature-limitations)
* [Supported Browsers](supported-browsers.md)
* [Troubleshooting Queries](#troubleshooting-queries.adoc)