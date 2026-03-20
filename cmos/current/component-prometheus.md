---
title: Prometheus
editUrl: https://github.com/couchbaselabs/observability/edit/0.2.x/docs/modules/ROOT/pages/component-prometheus.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cmos::component-prometheus.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cmos/current/component-prometheus.html)

# Prometheus

> Prometheus server in CMOS stack helps to scrape Couchbase Server metrics and generate alerts on them. 

## [](#overview)Overview

[Prometheus](https://prometheus.io) is a leading open-source monitoring solution which has become the industry standard for metrics collection and alert generation on cloud platforms. With Prometheus, multi-dimensional metric data can be collected from multiple endpoints and stored as time series data along with optional labels.

In a distributed environment, metrics need to be collected in real-time from various sources and alerts need to be triggered based on data trends and threshold deviations. As part of the Couchbase Monitoring and Observability Stack (CMOS), Prometheus Server comes with a set of built-in standard rules to create alerts on metrics scraped from Couchbase Server and other CMOS components.

![component prometheus](_images/component-prometheus.png) 

Figure 1\. Prometheus server in CMOS

From Couchbase Server 7, detailed metric endpoints are exposed via a [Prometheus instance](https://docs.couchbase.com/server/current/introduction/whats-new.html#scalable-statistics) built into the server. Using a CMOS Prometheus Server that sits outside of the Couchbase Cluster, monitoring can be easily accomplished at scale. The CMOS Prometheus Server, when configured, scrapes metrics from Couchbase Server targets along with other components in the stack. Alerts are generated based on standard alerting rules that are forwarded to the Alert Manager instance running in the CMOS stack.

## [](#get-started)Get Started

The CMOS Prometheus Server is included and enabled by default in CMOS. It ships with a default set of Couchbase specific standard alerting rules that trigger alerts, allowing administrators to quickly and easily take actions to mitigate issues. Prometheus in CMOS can be deployed [on premise](tutorial-onpremise.md) or using [kubernetes](tutorial-kubernetes.md). Check out the reference [Couchbase Monitoring Observability Stack](architecture.md)(CMOS) architecture to learn more. Learn more about how to further customize Prometheus to scrape metrics from other targets and create new rules in the [first steps](https://prometheus.io/docs/introduction/first%5Fsteps).

## [](#links)Links

* On Premise Tutorial: [Deploy CMOS on Premise](tutorial-onpremise.md)
* Kubernetes Tutorial: [Deploy CMOS on Kubernetes](tutorial-kubernetes.md)
* Prometheus: [First Steps](https://prometheus.io/docs/introduction/first%5Fsteps)