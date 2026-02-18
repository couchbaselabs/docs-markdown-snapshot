---
title: Prometheus Metrics Reference
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.7/modules/ROOT/pages/reference-prometheus-metrics.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/operator/2.7/reference-prometheus-metrics.html)

# Prometheus Metrics Reference

> This page captures the metrics supplied to Prometheus by the Couchbase Autonomous Operator. 

| Metric                                                                                                                                     | Type      | Unit         | Labels                        | Stability | Added |
| ------------------------------------------------------------------------------------------------------------------------------------------ | --------- | ------------ | ----------------------------- | --------- | ----- |
| in\_place\_upgrade\_failures The number of times in place upgrades have failed                                                             | counter   |              | name                          | committed | 2.7.0 |
| in\_place\_upgrades\_total Total number of in place upgrades performed by operator                                                         | counter   |              | name                          | committed | 2.7.0 |
| pod\_readiness\_duration The time it takes for a pod to enter a ready state                                                                | gauge     | milliseconds | name,serverClass              | committed | 2.7.0 |
| pod\_recoveries\_total Total number of times operator has recovered a pod when the pod has been down                                       | counter   |              | name,podName                  | committed | 2.7.0 |
| pod\_recovery\_failures\_total Total number of times operator has failed to recover a pod                                                  | counter   |              | name,podName                  | committed | 2.7.0 |
| pod\_replacements\_failed Total number of times pods have failed to be recovered by the operator                                           | counter   |              | name                          | committed | 2.7.0 |
| pod\_replacements\_total The amount of times operator has replaced a couchbase server pod due to a change in a couchbase cluster resources | counter   |              | name                          | committed | 2.7.0 |
| reconcile\_failures Total failed reconcile operations performed on a specific cluster                                                      | counter   |              | namespace,name                | committed | 2.3.0 |
| reconcile\_time\_seconds Length of time per reconcile for a specific cluster                                                               | histogram | seconds      | namespace,name                | committed | 2.3.0 |
| reconcile\_total Total reconcile operations performed on a specific cluster                                                                | counter   |              | namespace,name,result         | committed | 2.3.0 |
| server\_http\_request\_codes\_total Total HTTP requests to Couchbase Server for a specific cluster, method and status code returned        | counter   |              | name,method,code,service,host | committed | 2.3.0 |
| server\_http\_request\_failures Total failed HTTP requests to Couchbase Server for a specific cluster                                      | counter   |              | name,method,service,host      | committed | 2.3.0 |
| server\_http\_requests\_time\_milliseconds Length of time per request for a specific cluster                                               | histogram | milliseconds | name,method,service,host      | committed | 2.3.0 |
| server\_http\_requests\_total Total HTTP requests to Couchbase Server for a specific cluster                                               | counter   |              | name,method,service,host      | committed | 2.3.0 |
| swap\_rebalance\_failures Total number of times swap rebalances have failed                                                                | counter   |              | name                          | committed | 2.7.0 |
| swap\_rebalances\_total Total number of swap rebalances performed by the operator                                                          | counter   |              | name                          | committed | 2.7.0 |
| upgrade\_duration The time taken to perform an upgrade                                                                                     |           | milliseconds | name                          | committed | 2.7.0 |
| volume\_expansions\_total Total number of times the size of volumes have been increased under management                                   | counter   |              | name,volumeName               | committed | 2.7.0 |