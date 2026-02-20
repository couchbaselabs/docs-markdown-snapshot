---
title: Query Service Metrics Cross Reference
description: A cross-referenced table of the metrics provided by the Query
  Service as named by various generations of reporting tools.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/metrics-reference/pages/query-service-metrics-cross-reference.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:metrics-reference:query-service-metrics-cross-reference.adoc[]
---

[View original HTML](/server/current/metrics-reference/query-service-metrics-cross-reference.html)

# Query Service Metrics Cross Reference

> A cross-referenced table of the metrics provided by the Query Service as named by various generations of reporting tools. 

See [Query Service Metrics](query-service-metrics.md) for full description of all the Query Service metrics.

The following table lets you lookup a metric name you may know from an alternative supported or legacy reporting tool.

__Table 1\. Query Service Metrics Cross Reference__
| Couchbase Server pre-7.0   | Couchbase Exporter           | Couchbase Server 7.0+                |
| -------------------------- | ---------------------------- | ------------------------------------ |
| query\_active\_requests    | cbquery\_active\_requests    | n1ql\_active\_requests               |
| query\_avg\_req\_time      | cbquery\_avg\_req\_time      | n1ql\_request\_time / n1ql\_requests |
| query\_avg\_response\_size | cbquery\_avg\_response\_size | n1ql\_result\_size / n1ql\_requests  |
| query\_avg\_result\_count  | cbquery\_avg\_result\_count  | n1ql\_result\_count / n1ql\_requests |
| query\_avg\_svc\_time      | cbquery\_avg\_svc\_time      | n1ql\_service\_time / n1ql\_requests |
| query\_errors              | cbquery\_errors              | n1ql\_errors                         |
| query\_invalid\_requests   | cbquery\_invalid\_requests   | n1ql\_invalid\_requests              |
| query\_queued\_requests    | cbquery\_queued\_requests    | n1ql\_queued\_requests               |
| query\_request\_time       | cbquery\_request\_time       | n1ql\_request\_time                  |
| query\_requests            | cbquery\_requests            | n1ql\_requests                       |
| query\_requests\_1000ms    | cbquery\_requests\_1000ms    | n1ql\_requests\_1000ms               |
| query\_requests\_250ms     | cbquery\_requests\_250ms     | n1ql\_requests\_250ms                |
| query\_requests\_5000ms    | cbquery\_requests\_5000ms    | n1ql\_requests\_5000ms               |
| query\_requests\_500ms     | cbquery\_requests\_500ms     | n1ql\_requests\_500ms                |
| query\_result\_count       | cbquery\_result\_count       | n1ql\_result\_count                  |
| query\_result\_size        | cbquery\_result\_size        | n1ql\_result\_size                   |
| query\_selects             | cbquery\_selects             | n1ql\_selects                        |
| query\_service\_time       | cbquery\_service\_time       | n1ql\_service\_time                  |
| query\_warnings            | cbquery\_warnings            | n1ql\_warnings                       |