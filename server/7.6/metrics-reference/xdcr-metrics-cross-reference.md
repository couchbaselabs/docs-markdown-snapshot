---
title: XDCR Metrics Cross Reference
description: A cross-referenced table of the metrics provided by XDCR as named
  by various generations of reporting tools.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/metrics-reference/pages/xdcr-metrics-cross-reference.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:metrics-reference:xdcr-metrics-cross-reference.adoc[]
---

[View original HTML](/server/7.6/metrics-reference/xdcr-metrics-cross-reference.html)

# XDCR Metrics Cross Reference

> A cross-referenced table of the metrics provided by XDCR as named by various generations of reporting tools. 

See [XDCR Metrics](xdcr-metrics.md) for full description of all the XDCR metrics.

The following table lets you lookup a metric name you may know from an alternative supported or legacy reporting tool.

__Table 1\. XDCR Metrics Cross Reference__
| Couchbase Server pre-7.0        | Couchbase Server 7.0+                        |
| ------------------------------- | -------------------------------------------- |
| add\_docs\_cas\_changed         | xdcr\_add\_docs\_cas\_changed\_total         |
| add\_docs\_written              | xdcr\_add\_docs\_written\_total              |
| changes\_left                   | xdcr\_changes\_left\_total                   |
| data\_merged                    | xdcr\_data\_merged\_bytes                    |
| data\_replicated                | xdcr\_data\_replicated\_bytes                |
| datapool\_failed\_gets          | xdcr\_datapool\_failed\_gets\_total          |
| dcp\_datach\_length             | xdcr\_dcp\_datach\_length\_total             |
| dcp\_dispatch\_time             | xdcr\_dcp\_dispatch\_time\_seconds           |
| deletion\_docs\_cas\_changed    | xdcr\_deletion\_docs\_cas\_changed\_total    |
| deletion\_docs\_written         | xdcr\_deletion\_docs\_written\_total         |
| deletion\_failed\_cr\_source    | xdcr\_deletion\_failed\_cr\_source\_total    |
| deletion\_filtered              | xdcr\_deletion\_filtered\_total              |
| deletion\_received\_from\_dcp   | xdcr\_deletion\_received\_from\_dcp\_total   |
| deletion\_target\_docs\_skipped | xdcr\_deletion\_target\_docs\_skipped\_total |
| docs\_checked                   | xdcr\_docs\_checked\_total                   |
| docs\_cloned                    | xdcr\_docs\_cloned\_total                    |
| docs\_failed\_cr\_source        | xdcr\_docs\_failed\_cr\_source\_total        |
| docs\_filtered                  | xdcr\_docs\_filtered\_total                  |
| docs\_merge\_cas\_changed       | xdcr\_docs\_merge\_cas\_changed\_total       |
| docs\_merged                    | xdcr\_docs\_merged\_total                    |
| docs\_opt\_repd                 | xdcr\_docs\_opt\_repd\_total                 |
| docs\_processed                 | xdcr\_docs\_processed\_total                 |
| docs\_received\_from\_dcp       | xdcr\_docs\_received\_from\_dcp              |
| docs\_rep\_queue                | xdcr\_docs\_rep\_queue\_total                |
| docs\_unable\_to\_filter        | xdcr\_docs\_unable\_to\_filter\_total        |
| docs\_written                   | xdcr\_docs\_written\_total                   |
| expiry\_docs\_merge\_failed     | xdcr\_expiry\_docs\_merge\_failed\_total     |
| expiry\_docs\_merged            | xdcr\_expiry\_docs\_merged\_total            |
| expiry\_docs\_written           | xdcr\_expiry\_docs\_written\_total           |
| expiry\_failed\_cr\_source      | xdcr\_expiry\_failed\_cr\_source\_total      |
| expiry\_filtered                | xdcr\_expiry\_filtered\_total                |
| expiry\_merge\_cas\_changed     | xdcr\_expiry\_merge\_cas\_changed\_total     |
| expiry\_received\_from\_dcp     | xdcr\_expiry\_received\_from\_dcp\_total     |
| expiry\_stripped                | xdcr\_expiry\_stripped\_total                |
| expiry\_target\_docs\_skipped   | xdcr\_expiry\_target\_docs\_skipped\_total   |
| num\_checkpoints                | xdcr\_num\_checkpoints\_total                |
| num\_failedckpts                | xdcr\_num\_failedckpts\_total                |
| resp\_wait\_time                | xdcr\_resp\_wait\_time\_seconds              |
| set\_docs\_cas\_changed         | xdcr\_set\_docs\_cas\_changed\_total         |
| set\_docs\_written              | xdcr\_set\_docs\_written\_total              |
| set\_failed\_cr\_source         | xdcr\_set\_failed\_cr\_source\_total         |
| set\_filtered                   | xdcr\_set\_filtered\_total                   |
| set\_received\_from\_dcp        | xdcr\_set\_received\_from\_dcp\_total        |
| set\_target\_docs\_skipped      | xdcr\_set\_target\_docs\_skipped\_total      |
| size\_rep\_queue                | xdcr\_size\_rep\_queue\_bytes                |
| target\_docs\_skipped           | xdcr\_target\_docs\_skipped\_total           |
| throttle\_latency               | xdcr\_throttle\_latency\_seconds             |
| throughput\_throttle\_latency   | xdcr\_throughput\_throttle\_latency\_seconds |
| time\_committing                | xdcr\_time\_committing\_seconds              |
| wtavg\_docs\_latency            | xdcr\_wtavg\_docs\_latency\_seconds          |
| wtavg\_get\_doc\_latency        | xdcr\_wtavg\_get\_doc\_latency\_seconds      |
| wtavg\_merge\_latency           | xdcr\_wtavg\_merge\_latency\_seconds         |
| wtavg\_meta\_latency            | xdcr\_wtavg\_meta\_latency\_seconds          |