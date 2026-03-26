---
title: Integrating CMOS with Existing Monitoring Stacks
editUrl: https://github.com/couchbaselabs/observability/edit/0.2.x/docs/modules/ROOT/pages/integrating-with-existing-deployments.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:cmos::integrating-with-existing-deployments.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cmos/current/integrating-with-existing-deployments.html)

# Integrating CMOS with Existing Monitoring Stacks

> You can integrate CMOS with your existing Prometheus, Alertmanager, and Grafana monitoring system. This tutorial documents how to configure each component in order to achieve this. 

> [!WARNING]
> Tutorials are provided to demonstrate how a particular problem may be solved. Tutorials are accurate at the time of writing but rely heavily on third party software. The third party software is not directly supported by Couchbase. For further help in the event of a problem, contact the relevant software maintainer.

## [](#pre-requisites)Pre-requisites

The environment you wish to integrate CMOS into must have:

1. At least one **Couchbase Server** node;
2. **Prometheus 2.26 or later**, with **Alertmanager 0.23.0 or later** installed;
3. **Grafana 8.3.0 or later**, configured to use the Prometheus server as a Data Source;

  * **Docker**, to run the Cluster Monitor's Docker image

## [](#installation)Installation

### [](#install-cluster-monitor)Install Cluster Monitor

Currently there is no separate image containing just the Cluster Monitor - you can follow issue [CMOS-351](https://issues.couchbase.com/browse/CMOS-351) for updates on this option. However, it is possible to use the main CMOS container with all other services disabled for this purpose.

Run the Docker container, using the image from Docker Hub:

```console
docker run -d --rm \
  -p 7196:7196 \ (1)
  -e CB_MULTI_ALERTMANAGER_URLS=http://<Alertmanager IP>:9093 \ (2)
  -e CB_MULTI_ADMIN_USER=admin -e CB_MULTI_ADMIN_PASSWORD=password \
  --name cluster_monitor \
  -e DISABLE_PROMETHEUS=true -e DISABLE_GRAFANA=true \
  -e DISABLE_ALERT_MANAGER=true -e DISABLE_LOKI=true \
  -e DISABLE_JAEGER=true -e DISABLE_CMOSCFG=true -e DISABLE_WEBSERVER=true \
  couchbase/observability-stack:latest
```

| **1** | If you are using TLS, you will need to add \-p 7197:7197 to also expose port 7197. |
| ----- | ---------------------------------------------------------------------------------- |
| **2** | If you are not using Alertmanager, set this to a blank value.                      |

> [!NOTE]
> Docker networking [defaults to bridge](https://docs.docker.com/network/#network-drivers), meaning that this container will be able to communicate with any other running Docker containers. If your Grafana, Prometheus / Alertmanager instances are not containerized, ensure that the Cluster Monitor container can communicate with them.

### [](#configure-cluster-monitor)Configure Cluster Monitor

Navigate to the Web GUI, which listens by default on port `7196`. Sign in using the credentials you provided as environment variables when you started the Cluster Monitor earlier (by default, `admin`/`password`).

Then click "Add Cluster" and enter the IP address of a node in the cluster, along with the cluster's configured username and password. Repeat this for every cluster you wish to add to the Cluster Monitor.

## [](#configuration)Configuration

### [](#grafana-plugins)Grafana: Plugins

> [!NOTE]
> The instructions for each plugin offer a Grafana Cloud one-click install, a command-line based install for a running instance, or a `.zip` file which can be unpacked manually into your Grafana plugins directory.

**Currently, we require only [JSON API](https://grafana.com/grafana/plugins/marcusolsson-json-datasource/), which has associated [installation instructions](https://grafana.com/grafana/plugins/marcusolsson-json-datasource/?tab=installation).**

* **Grafana Cloud**: search for the plugin `marcusolsson-json-datasource` and click install
* **Command-line**: `grafana-cli plugins install marcusolsson-json-datasource`
* **Manual download**: _see linked instructions for latest file_

However, if you:

* Configure Grafana (v7.1+) dashboards through the use of provisioning files: [specify the plugins to install in your provisioning configuration file](https://grafana.com/docs/grafana/latest/administration/provisioning/#plugins).
* Are running Grafana in a Docker container: simply pass through an additional environment variable `GF_INSTALL_PLUGINS=$PLUGIN_NAME $VERSION` where the `$PLUGIN_NAME` and latest `$VERSION` can be found on the plugin's homepage (linked under "installation instructions" for each).

### [](#grafana-dashboards)Grafana: Dashboards

The CMOS dashboards can be found in the official GitHub repository under [microlith/grafana/provisioning/dashboards](https://github.com/couchbaselabs/observability/tree/main/microlith/grafana/provisioning/dashboards)/. Download them and copy them to a folder accessible by your Grafana installation.

The relevant setting in the Grafana configuration file, typically named `grafana.ini`, is:

```console
[dashboards]
default_home_dashboard_path = <path to dashboards>/couchbase-inventory.json
```

If you are using [Grafana provisioning](https://grafana.com/docs/grafana/latest/administration/provisioning/), you will need to update the `providers.options.path` argument in your provisioning configuration file (typically named `grafana.yml`) instead. For example:

```console
providers:
    - name: dashboards
      type: file
      ...
      options:
          path: /etc/grafana/provisioning/dashboards/
      ...
```

### [](#grafana-data-sources)Grafana: Data Sources

Now we have the required plugins and dashboards installed, we need to configure Data Sources.

> [!NOTE]
> If adding through the web UI, both Cluster Monitor and Alertmanager will return 404\. This is expected and not an issue - the dashboards use sub-paths of these configured URLs which are themselves valid and exist.

1. **Cluster Monitor (JSON API)**, via the Web UI: click on _Add Data Source_ and select _JSON API_.

  * This must be named `Couchbase Cluster Monitor API`.
  * The URL should point to the Cluster Monitor with a sub-path of `/api/v1`. The port should be `:7196`.
  * Enable `basicAuth`, with the user and password you configured.
2. **Prometheus** \- this should already be configured as a Data Source.
3. **Alertmanager** \- add a new Data Source in the same way as you did for the Cluster Monitor.

  * This should be named _Alertmanager API_, also of type _JSON API_, and the URL should point to your Alertmanager instance.
  * Configure any authentication as needed.

If you are utilizing Grafana provisioning for dashboards, and would instead like to specify this in a configuration file, then your `grafana.yml` should look something like this:

> [!IMPORTANT]
> The names of these two data sources must match the below snippet exactly, otherwise the dashboards may fail to provision.

```console
    - name: Couchbase Cluster Monitor API
      type: marcusolsson-json-datasource
      uid: PD5070BC1AA9F8304
      url: http://<Cluster Monitor URL>:7196/api/v1
      basicAuth: true
      basicAuthUser: <Cluster Monitor Username>
      basicAuthPassword: <Cluster Monitor Password>
    - name: Alertmanager API
      type: marcusolsson-json-datasource
      uid: PC245499EF542F9C5
      url: http://<Alertmanager URL>/api/v2
      # Configure basicAuth as needed.
...
```

### [](#prometheus-scrape-config)Prometheus: Scrape config

You will need to modify your existing Prometheus configuration file (typically named `prometheus.yml`). Add in a `scrape_config` job for your Couchbase Server nodes:

prometheus.yml

```yaml
global:
  scrape_interval: 30s

scrape_configs:
  - job_name: couchbase-server
    basic_auth:
      username: Administrator (1)
      password: password (2)
    static_configs:
      - targets:
          - <Couchbase Server Node 1 IP>:8091 (3)
          - <Couchbase Server Node 2 IP>:8091
          ...
        labels:
          cluster: "Couchbase Server Cluster" (4)
```

| **1** | username should be set to a Couchbase Server user with at least "External Stats Reader" permission.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | password should be the password of the above user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **3** | targets should specify the addresses of all the nodes in your cluster. For a Couchbase Server 7+ cluster the port number needs to be the management port: 8091 by default, or :18091 if you have TLS enabled. For clusters below Couchbase Server 7.0, you should use the port that your Prometheus exporter uses. There are alternative configuration options that do not require hard-coding the addresses - refer to the [Prometheus documentation](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape%5Fconfig) for more details. |
| **4** | Any labels defined here will be added to **all** metrics from this cluster - you may want to configure e.g., environment, datacenter etc.                                                                                                                                                                                                                                                                                                                                                                                                                           |

> [!IMPORTANT]
> The `cluster` label is required, and must match the name the cluster is configured to use in the Web Console.

Add another `scrape_config` job for the previously-installed Cluster Monitor:

prometheus.yml

```yaml
...
- job_name: couchbase-cluster-monitor
  basic_auth:
    username: admin  (1)
    password: password (2)
  metrics_path: /api/v1/_prometheus (3)
  static_configs:
    - targets: [<Cluster Monitor IP>:7196] (4)
...
```

| **1** | username should be the Username you configured for the Cluster Monitor.                                                                                    |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | password should be the Password you configured for the Cluster Monitor.                                                                                    |
| **3** | metrics\_path is the path to the Prometheus server running on the Cluster Monitor. This should not be changed.                                             |
| **4** | targets is a list of Cluster Monitor instances for Prometheus to retrieve metrics from. For now this should be a single server IP, listening on port 7196. |

Restart Prometheus, and navigate to the Web UI. If this was successful you should see your cluster listed on the page `/targets`.

### [](#prometheus-alerting-rules)Prometheus: Alerting Rules

CMOS ships with pre-made alert definitions which can alert you about certain events in your cluster. To take advantage of these, first download the rule definitions to somewhere your Prometheus config can access them:

```console
wget -O prometheus-rules.yaml https://raw.githubusercontent.com/couchbaselabs/observability/main/microlith/prometheus/alerting/couchbase/couchbase-rules.yaml
```

Next, modify your Prometheus configuration file to include this directory. For example, if you downloaded them to `/etc/prometheus/alerting/` then you would add:

prometheus.yml

```yaml
# Insert this at the top level of your prometheus.yml
rule_files:
  - /etc/prometheus/alerting/prometheus-rules.yaml
```

> [!NOTE]
> If you have existing alert definitions, simply add the `prometheus-rules.yaml` file to the same directory, and specify `*.yaml` as the target for `rule_files`.

Restart Prometheus once more, and navigate to the Web UI. You should be able to see the new rules listed on the `/rules` page. You may need to unhide inactive rules.

### [](#alertmanager)Alertmanager

We assume that you have already configured Prometheus to send alerts to Alertmanager, and that Alertmanager has appropriate receivers created and configured.

Therefore, there is no additional configuration required.

## [](#next-steps)Next Steps

Head on over to your Grafana Web UI. Navigate to _Dashboards_, and select _Single Cluster Overview._