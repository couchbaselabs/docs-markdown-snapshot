[View original HTML](/cmos/current/component-grafana.html)

> Grafana helps visualize Couchbase metrics, logs, and alerts. 

## [](#overview)Overview

[Grafana](https://grafana.com) is a multi-platform open source monitoring and visualization tool for large scale cloud-native projects.

In any production environment either deployed in the private or public cloud with distributed services it is essential to proactively monitor and visualize the state of the system at all times. As part of the Couchbase Monitoring and Observability Stack (CMOS), Grafana has a set of dashboards that allow administrators to query the state of the system centrally and take action at any given time.

![component grafana](_images/component-grafana.png) 

Figure 1\. Grafana in CMOS

In CMOS, Grafana is linked to data sources such as [Prometheus](https://prometheus.io) and [Loki](https://grafana.com/Loki). Prometheus scrapes couchbase metrics and stores these data points in the prometheus server. Using dashboards in Grafana, users can visualize metrics from the Prometheus server. Logs from Couchbase are sent to Loki, and then exposed in the Grafana dashboards.

## [](#get-started)Get Started

Grafana is included and enabled by default in the CMOS stack. It ships with a default set of standard dashboards, allowing administrators to quickly and easily get started. Grafana in CMOS can be deployed [on premise](tutorial-kubernetes.md) or using [kubernetes](tutorial-kubernetes.md). Check out the reference [Couchbase Monitoring Observability Stack](architecture.md)(CMOS) architecture to learn more. Learn more about how to further customize Grafana dashboards in CMOS: [additional dashboards](https://grafana.com/docs/grafana/latest/getting-started/getting-started).

## [](#links)Links

* On Premise Tutorial: [Deploy CMOS on Premise](tutorial-onpremise.md)
* Kubernetes Tutorial: [Deploy CMOS on Kubernetes](tutorial-kubernetes.md)
* Grafana: [Creating custom dashboards](https://grafana.com/docs/grafana/latest/getting-started/getting-started)