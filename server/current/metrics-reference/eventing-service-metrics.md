---
title: Eventing Service Metrics
description: A list of the metrics provided by the Eventing Service.
pubDate: 2026-08-18T04:50:45.818Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/metrics-reference/pages/eventing-service-metrics.adoc
  xref: xref:server:metrics-reference:eventing-service-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/metrics-reference/eventing-service-metrics.html)

# Eventing Service Metrics

> A list of the metrics provided by the Eventing Service. 

The following Eventing Service metrics can be queried by means of the REST APIs described in [Statistics](../rest-api/rest-statistics.md).

> [!TIP]
> * The x.y.z badge shows the Couchbase Server version the metric was added in.
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

`eventing_analytics_op_exception_count`

7.6.0 counter The total number of analytics query exceptions

`eventing_bkt_ops_cas_mismatch_count`

7.0.0 counter The total number of Key-Value CAS mismatches

`eventing_bucket_op_exception_count`

7.0.0 counter The total number of Key-Value exceptions

`eventing_dcp_backlog`

7.0.0 gauge The total number of events not yet processed by eventing function

`eventing_dcp_delete_msg_counter`

7.0.0 counter The total number of delete events processed by worker

`eventing_dcp_deletion_sent_to_worker`

7.0.0 counter The total number of delete events sent to worker to be processed by OnDelete function

`eventing_dcp_deletion_suppressed_counter`

7.0.0 counter The total number of suppressed delete events

`eventing_dcp_expiry_sent_to_worker`

7.0.0 counter The total number of expiry events sent to worker to be processed by OnDelete function

`eventing_dcp_mutation_sent_to_worker`

7.0.0 counter The total number of insert or update events sent to worker to be processed by OnUpdate function

`eventing_dcp_mutation_suppressed_counter`

7.0.0 counter The total number of suppressed inserts or updates events

`eventing_dcp_mutations_msg_counter`

7.0.0 counter The total number of insert or update events processed by worker

`eventing_n1ql_op_exception_count`

7.0.0 counter The total number of Query exceptions

`eventing_on_delete_failure`

7.0.0 counter The total number of failed OnDelete calls

`eventing_on_delete_success`

7.0.0 counter The total number of successful OnDelete calls

`eventing_on_update_failure`

7.0.0 counter The total number of failed OnUpdate calls

`eventing_on_update_success`

7.0.0 counter The total number of successful OnUpdate calls

`eventing_timeout_count`

7.0.0 counter The total number of JavaScript executions exceeding execution timeout

`eventing_timer_callback_failure`

7.0.0 counter The total number of failed timer callback invocations

`eventing_timer_callback_missing_counter`

7.0.0 counter The total number of undefined timer callback functions

`eventing_timer_callback_success`

7.0.0 counter The total number of successful timer callback invocations

`eventing_timer_cancel_counter`

7.0.0 counter The total number of successful CancelTimer call

`eventing_timer_context_size_exception_counter`

7.0.0 counter The total number of timer\_create\_failure due to payload exceeding timer\_context\_size

`eventing_timer_create_counter`

7.0.0 counter The total number of successful CreateTimer call

`eventing_timer_create_failure`

7.0.0 counter The total number of failed CreateTimer call

`eventing_timer_msg_counter`

7.0.0 gauge The total number of timer callbacks processed