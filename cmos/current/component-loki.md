---
title: Loki
editUrl: https://github.com/couchbaselabs/observability/edit/0.2.x/docs/modules/ROOT/pages/component-loki.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cmos::component-loki.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cmos/current/component-loki.html)

# Loki

> Loki can be used to process and store Couchbase logs. 

## [](#overview)Overview

[Loki](https://grafana.com/Loki) is a [Prometheus](https://prometheus.io/)\-inspired open source, multi-tenant log aggregation system. Loki is used to process and store collected Couchbase logs.

![component loki](_images/component-loki.png) 

Figure 1\. Loki in CMOS

Couchbase cluster generates logs of various operations which is important for monitoring and investigation purposes. Loki provides the option to parse the logs enabling search and aggregation based on keys. Logs are pushed to Loki by various tools, we recommend [Fluent Bit](deployment-fluentbit.md) and provide a method to deploy it.

## [](#get-started)Get Started

Loki is managed by the [Couchbase Monitoring Observability Stack](architecture.md)(CMOS). Loki is enabled by default in the CMOS, however, Fluent Bit needs to be configured for the logs to reach Loki. Depending upon the type of deployment you need to enable Fluent Bit.

### [](#links)Links

* Kubernetes Tutorial: [Deploy CMOS on Kubernetes](tutorial-kubernetes.md)
* On Premise Tutorial: [Deploy CMOS on Premise](tutorial-onpremise.md)
* Fluent Bit Deployment: [Fluent Bit Deployment for Couchbase](deployment-fluentbit.md)