---
title: Prometheus Metrics Reference
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.9/modules/ROOT/pages/reference-prometheus-metrics.adoc
  xref: xref:operator::reference-prometheus-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/current/reference-prometheus-metrics.html)

# Prometheus Metrics Reference

> This page captures the metrics supplied to Prometheus by the Couchbase Kubernetes Operator and links reference pages of a number of additional metrics that are exported by third party libraries. 

## [](#operator-metrics)Operator Metrics

| Metric                                                                                                                                     | Type      | Unit         | Labels                        | Optional Labels             | Stability | Added |
| ------------------------------------------------------------------------------------------------------------------------------------------ | --------- | ------------ | ----------------------------- | --------------------------- | --------- | ----- |
| backup\_jobs\_created\_total Total number of backup jobs that have been created by the operator                                            | counter   |              | namespace,backup\_type        | cluster\_uuid,cluster\_name | committed | 2.8.0 |
| cluster\_manual\_intervention Indicates whether manual intervention is required for the cluster                                            | gauge     |              | namespace,name                | cluster\_uuid,cluster\_name | committed | 2.9.0 |
| cpu\_under\_management Total cpu requests for operator managed pods in k8s cpu units                                                       | gauge     |              | namespace,name                | cluster\_uuid,cluster\_name | committed | 2.8.0 |
| in\_place\_upgrade\_failures The number of times in place upgrades have failed                                                             | counter   |              | name                          | cluster\_uuid,cluster\_name | committed | 2.7.0 |
| in\_place\_upgrades\_total Total number of in place upgrades performed by operator                                                         | counter   |              | name                          | cluster\_uuid,cluster\_name | committed | 2.7.0 |
| kubernetes\_api\_request\_failures Total failed requests to the Kubernetes API by the operator                                             | counter   |              | method,host                   |                             | committed | 2.8.0 |
| kubernetes\_api\_requests\_time\_milliseconds Length of time per request to the Kubernetes API                                             | histogram | milliseconds | method,host                   |                             | committed | 2.8.0 |
| kubernetes\_api\_requests\_total Total requests made to the Kubernetes API by the operator                                                 | counter   |              | method,host                   |                             | committed | 2.8.0 |
| memory\_under\_management\_bytes Total memory requests for operator managed pods in bytes                                                  | gauge     | bytes        | namespace,name                | cluster\_uuid,cluster\_name | committed | 2.8.0 |
| pod\_readiness\_duration The time it takes for a pod to enter a ready state                                                                | gauge     | milliseconds | name,serverClass              | cluster\_uuid,cluster\_name | committed | 2.7.0 |
| pod\_recoveries\_total Total number of times operator has recovered a pod when the pod has been down                                       | counter   |              | name,podName                  | cluster\_uuid,cluster\_name | committed | 2.7.0 |
| pod\_recovery\_failures\_total Total number of times operator has failed to recover a pod                                                  | counter   |              | name,podName                  | cluster\_uuid,cluster\_name | committed | 2.7.0 |
| pod\_replacements\_failed Total number of times pods have failed to be recovered by the operator                                           | counter   |              | name                          | cluster\_uuid,cluster\_name | committed | 2.7.0 |
| pod\_replacements\_total The amount of times operator has replaced a couchbase server pod due to a change in a couchbase cluster resources | counter   |              | name                          | cluster\_uuid,cluster\_name | committed | 2.7.0 |
| reconcile\_failures Total failed reconcile operations performed on a specific cluster                                                      | counter   |              | namespace,name                | cluster\_uuid,cluster\_name | committed | 2.3.0 |
| reconcile\_time\_seconds Length of time per reconcile for a specific cluster                                                               | histogram | seconds      | namespace,name                | cluster\_uuid,cluster\_name | committed | 2.3.0 |
| reconcile\_total Total reconcile operations performed on a specific cluster                                                                | counter   |              | namespace,name,result         | cluster\_uuid,cluster\_name | committed | 2.3.0 |
| server\_http\_request\_codes\_total Total HTTP requests to Couchbase Server for a specific cluster, method and status code returned        | counter   |              | name,method,code,service,host | name,namespace              | committed | 2.3.0 |
| server\_http\_request\_failures Total failed HTTP requests to Couchbase Server for a specific cluster                                      | counter   |              | name,method,service,host      | name,namespace              | committed | 2.3.0 |
| server\_http\_requests\_time\_milliseconds Length of time per request for a specific cluster                                               | histogram | milliseconds | name,method,service,host      | name,namespace              | committed | 2.3.0 |
| server\_http\_requests\_total Total HTTP requests to Couchbase Server for a specific cluster                                               | counter   |              | name,method,service,host      | name,namespace              | committed | 2.3.0 |
| swap\_rebalance\_failures Total number of times swap rebalances have failed                                                                | counter   |              | name                          | cluster\_uuid,cluster\_name | committed | 2.7.0 |
| swap\_rebalances\_total Total number of swap rebalances performed by the operator                                                          | counter   |              | name                          | cluster\_uuid,cluster\_name | committed | 2.7.0 |
| upgrade\_duration The time taken to perform an upgrade                                                                                     |           | milliseconds | name                          | cluster\_uuid,cluster\_name | committed | 2.7.0 |
| volume\_expansions\_total Total number of times the size of volumes have been increased under management                                   | counter   |              | name,volumeName               | cluster\_uuid,cluster\_name | committed | 2.7.0 |
| volume\_size\_under\_management\_bytes Total memory claimed by volumes under management by the operator in bytes                           | gauge     | bytes        | namespace,name                | cluster\_uuid,cluster\_name | committed | 2.8.0 |

## [](#additional-metrics)Additional Metrics

* [Kubebuilder](https://book.kubebuilder.io/reference/metrics-reference)