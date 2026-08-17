---
title: Prometheus Discovery API
description: The discovery API generates a list of Enterprise Analytics nodes
  that tools such Prometheus can use to collect metrics.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/reference/pages/rest-discovery-api.adoc
  xref: xref:enterprise-analytics:reference:rest-discovery-api.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/reference/rest-discovery-api.html)

# Prometheus Discovery API

> The discovery API generates a list of Enterprise Analytics nodes that tools such Prometheus can use to collect metrics. 

You can use Prometheus or similar tools to collect statistics and alerts from your Couchbase Database. In order for these tools to collect metrics, they must have a list of nodes in your Enterprise Analytics database. The discovery API provides this list to these tools.

See [Configure Prometheus to Collect Couchbase Metrics](../manage/monitor/set-up-prometheus-for-monitoring.md) for detailed information about using this API with Prometheus.

> [!NOTE]
> This endpoint is a replacement for the earlier `/prometheus_sd-config.yaml` endpoint. That endpoint is now deprecated. See [Replicate the Earlier Discovery API](#old-api) to learn how to call the new discovery API to get he same output as the old API.

## [](#http-method-and-uri)HTTP Method and URI

GET /prometheus_sd_config

## [](#description)Description

By default, the discovery endpoint returns the list of nodes in your database that:

* is in JSON format.
* uses the primary address of the node
* uses the secure port number

## [](#curl-syntax)curl Syntax

```shell
curl --get -u <username:password> \
    http://<ip-address-or-domain-name>:<port-number>/prometheus_sd_config
    -d clusterLabels=[none|uuidAndName|uuidOnly]
    -d disposition=[attachment|inline]
    -d network=[default|external]
    -d port=[insecure|secure]
    -d type=[json|yaml]
```

The username you use to call endpoint must have the [External Stats Reader](#learn:security/roles.adoc#external-stats-reader) role. This is the same role Enterprise Analytics requires to retrieve metrics.

### [](#parameters)Parameters

clusterLabels=\[none|uuidAndName|uuidOnly\]

Controls the inclusion of information labels for the cluster. When set to `none`, no labels are included in the response. When set to `uuidAndName`, both the UUID and the name of the node are added to the response. When set to `uuidOnly`, only the UUID of the node is returned in the response.

disposition=\[attachment|inline\]

Controls how Enterprise Analytics returns the list of nodes in the response. When set to the default `inline`, it returns the list inline within the response. When set to `attachment`, it returns the list as an attachment to the response.

network=\[default|external\]

Controls which network address Enterprise Analytics uses in the list. When set to the default value of `default`, it uses the nodes's default address. When set to `external`, it uses the node's [alternate address](#learn:clusters-and-availability/connectivity.adoc#alternate-addresses).

port=\[insecure|secure\]

Controls which port Enterprise Analytics uses in the list of nodes. When set to the default `secure`, it uses the node's secure port in the list. When set to `insecure`, it uses the node's unencrypted port.

type=\[json|yaml\]

Controls the data format Enterprise Analytics uses for the node list. When set to the default `json`, it returns the list of nodes in JSON format. When set to `yaml`, it returns the list of nodes in YAML format.

## [](#examples)Examples

The following example demonstrates calling the `prometheus_sd_config` endpoint on a node with the hostname `node1` using default values. It pipes the response through the `jq` command to make it readable.

```shell
curl -s --get -u prometheus:password http://node1:8091/prometheus_sd_config \
     | jq
```

The next example shows the response that Enterprise Analytics sends in response to the previous command.

```json
[
  {
    "targets": [
      "node1.:18091",
      "node2.:18091",
      "node3.:18091"
    ]
  }
]
```

Adding the `clusterLabels` parameter to the message payload will add additional node information to the response. For example, this command:

```shell
curl -s --get -u prometheus:password http://node1:8091/prometheus_sd_config \
-d clusterLabels=uuidAndName | jq
```

will send back the following response:

```json
[
  {
    "targets": [
      "node1:18091",
      "node2:18091",
      "node3:18091"
    ],
    "labels": {
      "cluster_uuid": "4798c8f9-89bd-d7bf-4bcf-d93fb3e03e46",
      "cluster_name": "DB1"
    }
  }
]
```

## [](#old-api)Replicate the Earlier Discovery API

The earlier `/prometheus_sd_config.yaml` discovery API endpoint returned a list of nodes in your Enterprise Analytics in a different format than the default output of the `/prometheus_sd_config`. If you have already configured Prometheus using the old endpoint, you can have the new endpoint return the same output by using the following parameters:

```shell
curl -s --get -u prometheus:password http://node1:8091/prometheus_sd_config \
     -d type=yaml \
     -d disposition=attachment \
     -d port=insecure
```

The equivalent encoded URI that you can add to your Prometheus configuration is:

```uri
http://node1:8091/prometheus_sd_config?type=yaml&disposition=attachment&port=insecure
```

The result of running the previous command or getting the URI is:

```yaml
- targets:
    - 'node1.:8091'
    - 'node2.:8091'
    - 'node3.:8091'
```