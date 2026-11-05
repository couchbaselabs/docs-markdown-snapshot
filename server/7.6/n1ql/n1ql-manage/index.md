---
title: Administer Queries and Indexes
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/n1ql/pages/n1ql-manage/index.adoc
  xref: xref:7.6@server:n1ql:n1ql-manage/index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/n1ql/n1ql-manage/index.html)

# Administer Queries and Indexes

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

## Get System Information

SQL++ has a system namespace that stores metadata about data containers, the Query service, and the system as a whole. You can query the system namespace to get this information.

* [Get System Information](../n1ql-intro/sysinfo.md)

## Manage Queries

You can monitor and manage queries using the Couchbase Web Console, the command line interface, or the REST API.

* [Monitor Queries in the Couchbase Web Console](../../tools/query-monitoring.md)
* [Manage and Monitor Queries](monitoring-n1ql-query.md)

## Manage Primary and Secondary Indexes

You can monitor and manage primary and secondary indexes using the Couchbase Web Console, the command line interface, or the REST API.

* [Monitor Indexes](../../manage/monitor/monitoring-indexes.md)
* [Manage Indexes](../../manage/manage-indexes/manage-indexes.md)

## Settings and Parameters

You can configure the Query service using cluster-level query settings, node-level query settings, and request-level query parameters.

* [Configure Queries](query-settings.md)