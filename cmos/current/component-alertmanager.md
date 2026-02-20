---
title: Alertmanager
editUrl: https://github.com/couchbaselabs/observability/edit/0.2.x/docs/modules/ROOT/pages/component-alertmanager.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cmos::component-alertmanager.adoc[]
---

[View original HTML](/cmos/current/component-alertmanager.html)

# Alertmanager

> Alertmanager handles and routes alerts from CMOS Prometheus server. 

## [](#overview)Overview

[Alertmanager](https://prometheus.io/docs/alerting/alertmanager) is an open source tool which has become the industry standard for alert management on cloud platforms. The CMOS Prometheus Server triggers alerts whenever certain rules are met and sends these alerts to the Alertmanager. The Alertmanager takes care of de-duplicating, grouping and routing these alerts to the correct receiver using integration such as e-mail, Slack and PagerDuty.

With multiple sources generating the same alert, distributed environments can be noisy. In these cases, the alerts should be de-duplicated and grouped by their nature, origin, and severity before being routed to the receiver. The Alertmanager can also suppress and mute alerts if required.

As part of the Couchbase Monitoring and Observability Stack (CMOS), Alertmanager comes with a set of built-in standard rules to handle alerts generated for Couchbase Server and other CMOS components.

![component alertmanager](_images/component-alertmanager.png) 

Figure 1\. Alertmanager in CMOS

Based on a predefined set of rules, the CMOS Prometheus Server generates alerts depending on the metrics it collects from Couchbase Server and other targets. By default, these alerts are forwarded to CMOS Alertmanager. The Alertmanager can be configured to route these alerts to a user-defined receiver integration such as e-mail, Slack, PagerDuty or other API-based endpoints to notify the user.

## [](#get-started)Get Started

In CMOS, the Alertmanager is included and enabled by default. It ships with a set of standard built-in rules to group alerts based on multiple alert parameters. Additionally, it can be customized to send notifications to different [receiver](https://prometheus.io/docs/alerting/configuration) endpoints.

The CMOS Alertmanager can be deployed [on premise](tutorial-onpremise.md) or using [Kubernetes](tutorial-kubernetes.md). Check out the reference [Couchbase Monitoring and Observability Stack](architecture.md) (CMOS) architecture to learn more.

## [](#links)Links

* On Premise Tutorial: [Deploy CMOS on Premise](tutorial-onpremise.md)
* Kubernetes Tutorial: [Deploy CMOS on Kubernetes](tutorial-kubernetes.md)
* Alertmanager: [Configuration](https://prometheus.io/docs/alerting/latest/configuration)