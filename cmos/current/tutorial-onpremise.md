---
title: Configure CMOS for On-premises deployment
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/observability/edit/0.2.x/docs/modules/ROOT/pages/tutorial-onpremise.adoc
  xref: xref:cmos::tutorial-onpremise.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cmos/current/tutorial-onpremise.html)

# Configure CMOS for On-premises deployment

> [!WARNING]
> Tutorials are provided to demonstrate how a particular problem may be solved. Tutorials are accurate at the time of writing but rely heavily on third party software. The third party software is not directly supported by Couchbase. For further help in the event of a problem, contact the relevant software maintainer.

## [](#overview)Overview

Couchbase Monitoring and Observability Stack (also known as CMOS) is a simple, out-of-the-box solution built using industry standard tooling to observe the state of a Couchbase cluster. CMOS can be deployed using Docker or any container runtime.

![microlith runtime](_images/microlith-runtime.png) 

Figure 1\. Microlith runtime image

### [](#installation)Installation

At this moment, we only support deployment of CMOS using containers. Use docker to start the CMOS container. Alternatively, you can also use Linux container tools such as [Podman](https://podman.io). To install CMOS run the command below:

```console
docker run --name=cmos --rm -d -P couchbase/observability-stack:latest
```

#### [](#port-configuration)Port Configuration

CMOS contains multiple services, each running on their own default port such as Grafana (3000), Prometheus (9090), Alertmanager (9093), Landing page (8080), and Loki (3100). You can also access different services using path-based routing through the landing page.

### [](#verification)Verification

You can verify whether the CMOS container is up and running by navigating to the CMOS landing page on port 8080.

To check the port mapping in your host, run the command below:

```console
docker container port cmos 8080
```

# output
0.0.0.0:55124
:::55124

![cmos landing](_images/cmos-landing.png) 

Figure 2\. CMOS landing image

#### [](#add-cluster)Add Cluster

If you don't have an existing Couchbase cluster setup, you can install it from [here](https://docs.couchbase.com/server/current/install/getting-started-docker.html#section%5Fjvt%5Fzvj%5F42b). To monitor a Couchbase cluster, you can add it using the add cluster option on the landing page.

![add cluster vm](_images/add-cluster-vm.png) 

Figure 3\. Add cluster image

As soon as you add a cluster, you will see a Grafana URL where you can view inventory and metrics of Couchbase server clusters.

![couchbase inventory vm](_images/couchbase-inventory-vm.png) 

Figure 4\. Couchbase inventory image

#### [](#prometheus)Prometheus

From the landing page, you can go to the prometheus target page and check if the added cluster target is up or down.

![prometheus target vm](_images/prometheus-target-vm.png) 

Figure 5\. Prometheus target image

#### [](#grafana)Grafana

From the landing page, you can go to Grafana and check the graphs. CMOS comes with pre-installed dashboards to monitor the Couchbase cluster. Dashboards with tag `couchbase-7` are relevant for Couchbase server version 7+. For more information, check the Grafana configuration section.

![couchbase cluster overview vm](_images/couchbase-cluster-overview-vm.png) 

Figure 6\. Couchbase cluster overview image

#### [](#alerts)Alerts

CMOS comes with pre-installed alert rules to monitor the Couchbase cluster. Navigate to the Prometheus UI to see the rules, or Alertmanager to see the alerts. For more information check the prometheus and alerting configuration section.

![prometheus alert rules](_images/prometheus-alert-rules.png) 

Figure 7\. Alert rules image

![prometheus alerts](_images/prometheus-alerts.png) 

Figure 8\. Alerts image

#### [](#loki)Loki

Loki, which is shipped with Grafana, allows access to logs of various components. You can configure it via Configuration > Data sources > Loki > Explore.

> [!NOTE]
> You will need to install and configure Fluent Bit on your Couchbase Server nodes before logs will be sent to Loki. Refer to the [Fluent Bit install guidance](deployment-fluentbit.md).

![loki explore dashboard](_images/loki-explore-dashboard.png) 

Figure 9\. Loki explore dashboard image

From the Log browser, you can enter a custom Loki query or select appropriate labels to see the logs.

![loki log browser](_images/loki-log-browser.png) 

Figure 10\. Loki log browser image

After that select the "Show logs" to view logs. You can also build [custom Grafana dashboards](https://grafana.com/docs/grafana/latest/getting-started/getting-started/#step-3-create-a-dashboard) based on your needs.

![loki logs](_images/loki-logs.png) 

Figure 11\. Loki logs image

### [](#next-steps)Next steps

* [Architecture overview](architecture.md)
* [Microlith container deployment](deployment-microlith.md)
* [Couchbase Cluster Monitor component](cluster-monitor.md)