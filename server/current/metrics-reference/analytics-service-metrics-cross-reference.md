---
title: Analytics Service Metrics Cross Reference
description: A cross-referenced table of the metrics provided by the Analytics
  Service as named by various generations of reporting tools.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/metrics-reference/pages/analytics-service-metrics-cross-reference.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:metrics-reference:analytics-service-metrics-cross-reference.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/metrics-reference/analytics-service-metrics-cross-reference.html)

# Analytics Service Metrics Cross Reference

> A cross-referenced table of the metrics provided by the Analytics Service as named by various generations of reporting tools. 

See [Analytics Service Metrics](analytics-service-metrics.md) for full description of all the Analytics Service metrics.

The following table lets you lookup a metric name you may know from an alternative supported or legacy reporting tool.

__Table 1\. Analytics Service Metrics Cross Reference__
| Couchbase Server pre-7.0                  | Couchbase Exporter        | Couchbase Server 7.0+                   |
| ----------------------------------------- | ------------------------- | --------------------------------------- |
| cbas\_disk\_used                          | cbcbas\_disk\_used        | cbas\_disk\_used\_bytes\_total          |
| failed\_at\_parser\_records\_count\_total | N/A                       | cbas\_failed\_to\_parse\_records\_count |
| cbas\_gc\_count                           | cbcbas\_gc\_count         | cbas\_gc\_count\_total                  |
| cbas\_gc\_time                            | cbcbas\_gc\_time          | cbas\_gc\_time\_milliseconds\_total     |
| cbas\_heap\_used                          | cbcbas\_heap\_used        | cbas\_heap\_memory\_used\_bytes         |
| incoming\_records\_count                  | N/A                       | cbas\_incoming\_records\_count          |
| cbas\_io\_reads                           | cbcbas\_io\_reads         | cbas\_io\_reads\_total                  |
| cbas\_io\_writes                          | cbcbas\_io\_writes        | cbas\_io\_writes\_total                 |
| cbas\_system\_load\_average               | cbcbas\_system\_load\_avg | cbas\_system\_load\_average             |
| cbas\_thread\_count                       | cbcbas\_thread\_count     | cbas\_thread\_count                     |