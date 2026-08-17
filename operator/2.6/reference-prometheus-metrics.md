---
title: Prometheus Metrics Reference
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.6/modules/ROOT/pages/reference-prometheus-metrics.adoc
  xref: xref:2.6@operator::reference-prometheus-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.6/reference-prometheus-metrics.html)

# Prometheus Metrics Reference

> This page captures the metrics supplied to Prometheus by the Couchbase Autonomous Operator. 

| Metric                                                                                                                              | Type      | Unit         | Labels                        | Stability | Added |
| ----------------------------------------------------------------------------------------------------------------------------------- | --------- | ------------ | ----------------------------- | --------- | ----- |
| reconcile\_failures Total failed reconcile operations performed on a specific cluster                                               | counter   |              | namespace,name                | committed | 2.3.0 |
| reconcile\_time\_seconds Length of time per reconcile for a specific cluster                                                        | histogram | seconds      | namespace,name                | committed | 2.3.0 |
| reconcile\_total Total reconcile operations performed on a specific cluster                                                         | counter   |              | namespace,name,result         | committed | 2.3.0 |
| server\_http\_request\_codes\_total Total HTTP requests to Couchbase Server for a specific cluster, method and status code returned | counter   |              | name,method,code,service,host | committed | 2.3.0 |
| server\_http\_request\_failures Total failed HTTP requests to Couchbase Server for a specific cluster                               | counter   |              | name,method,service,host      | committed | 2.3.0 |
| server\_http\_requests\_time\_milliseconds Length of time per request for a specific cluster                                        | histogram | milliseconds | name,method,service,host      | committed | 2.3.0 |
| server\_http\_requests\_total Total HTTP requests to Couchbase Server for a specific cluster                                        | counter   |              | name,method,service,host      | committed | 2.3.0 |