---
title: Administer Queries and Indexes
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/n1ql/pages/n1ql-manage/index.adoc
  xref: xref:server:n1ql:n1ql-manage/index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/n1ql/n1ql-manage/index.html)

# Administer Queries and Indexes

## Get System Information

SQL++ has a system namespace that stores metadata about data containers, the Query service, and the system as a whole. You can query the system namespace to get this information.

* [Get System Information](../n1ql-intro/sysinfo.md)

## Manage Queries

You can monitor and manage queries using the Couchbase Web Console, the command line interface, or the REST API.

* [Monitor Queries in the Couchbase Web Console](../../tools/query-monitoring.md)
* [Manage and Monitor Queries](monitoring-n1ql-query.md)
* [Automatic Workload Repository](query-awr.md)

## Manage Primary and Secondary Indexes

You can monitor and manage primary and secondary indexes using the Couchbase Web Console, the command line interface, or the REST API.

* [Monitor Indexes](../../manage/monitor/monitoring-indexes.md)
* [Manage Indexes](../../manage/manage-indexes/manage-indexes.md)

## Settings and Parameters

You can configure the Query service using cluster-level query settings, node-level query settings, and request-level query parameters.

* [Configure Queries](query-settings.md)