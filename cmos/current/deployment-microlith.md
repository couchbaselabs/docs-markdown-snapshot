---
title: Microlith deployment
editUrl: https://github.com/couchbaselabs/observability/edit/0.2.x/docs/modules/ROOT/pages/deployment-microlith.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:cmos::deployment-microlith.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cmos/current/deployment-microlith.html)

# Microlith deployment

To support easy deployment across a variety of targets, we are providing a 'microlith' single container option. This is essentially the various scalable components of the Grafana stack (Loki, Prometheus, Grafana, Alert Manager) and Couchbase binaries for specific data extraction all runnable as a single multi-process container instance.

A single container can then be run on-premise or on a Kubernetes platform very easily with minimal effort.

![microlith runtime](_images/microlith-runtime.png) 

Figure 1\. Microlith overview

Whilst on-premise customers may primarily be using native binaries, all supported OS's for Couchbase Server can run containers easily. This also makes it easier to deploy as a self-contained image and easy to upgrade as well. We could produce an OS-specific package (e.g. RPM) with all necessary dependencies on the container runtime.

## [](#customization)Customization

Areas that support customization:

* Dashboards

  * Support providing bespoke dashboards directly by specifying at runtime.
* Alerting rules

  * Provide custom alert rules and other metric generation (e.g. pre-calculated ones)
  * Tweak the configuration for existing ones deployed
  * Disable or inhibit default rules provided
* Cluster credentials and identities

  * Support adding new cluster nodes easily
  * Support fully dynamic credentials and discovery (no need to restart to pick up a change), e.g. <https://github.com/mrsiano/openshift-grafana/blob/master/prometheus-high-performance.yaml#L292>

In all cases we do not want to have to rebuild anything to customize it, it should just be a runtime configuration. This then supports a Git-ops style deployment with easy upgrade path as we always run the container plus config so you can modify each independently, roll back, etc.

![microlith config](_images/microlith-config.png) 

Figure 2\. Microlith configuration

## [](#prometheus-alerting-rules)Prometheus alerting rules

There are three directories used for alerting rules:

* `/etc/prometheus/alerting/couchbase`: Couchbase preset rules. Do not modify these, as your changes may be overwritten when you upgrade. Instead, use overrides (described below).
* `/etc/prometheus/alerting/overrides`: Space for your overrides of the Couchbase rules. These will be pre-processed with [prometheus-alert-overrider](https://github.com/lablabs/prometheus-alert-overrider), enabling you to customize our rules. For an example, see [our integration tests](https://github.com/couchbaselabs/observability/tree/main/testing/microlith-test/integration/prometheus%5Falert%5Foverrides).
* `/etc/prometheus/alerting/custom`: Space for your own custom rules. These will be loaded by Prometheus but will not be pre-processed in any way.

There is also a fourth directory, `/etc/prometheus/alerting/generated`, where the processed rules file will be written. Do not modify this directory, as your changes may be overwritten as part of the build process.

If you want to disable the pre-processing and use entirely your own ruleset, set the environment variable `DISABLE_ALERTS_PREPARE=true`.

## [](#next-steps)Next steps

* [Architecture overview](architecture.md)
* [On-premise deployment](deployment-onpremise.md)
* [On-premise example](tutorial-onpremise.md)