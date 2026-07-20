---
title: Application Telemetry
description: You can enable application telemetry to have Couchbase Server
  periodically collect telemetry from your clients that use the Couchbase SDK.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/application-telemetry.adoc
pubDate: 2026-07-20T13:54:32.914Z
link: xref:server:rest-api:application-telemetry.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/rest-api/application-telemetry.html)

# Application Telemetry

> You can enable application telemetry to have Couchbase Server periodically collect telemetry from your clients that use the Couchbase SDK. 

## [](#description)Description

Having Couchbase Server collect telemetry from your applications can help you troubleshoot client issues. This visibility into metrics data from the application's point of view is useful to diagnose issues such as poor performance or timeouts.

![Telemetry Architecture](_images/diag-adcaf9fcded364fc485c5699f432f36452c5f0a8.svg) 

Figure 1\. Telemetry Architecture

When you enable application telemetry, Couchbase Server advertises to SDK clients that it can collect telemetry data. When an SDK client connects to a cluster with application telemetry enabled, it opens a WebSocket connection to a node in the cluster.  
The clients send metrics to any node in the cluster — the cluster forwards the metrics on to other nodes.  
Couchbase Server uses this connection to periodically gather telemetry data from the client in Prometheus format.

> [!NOTE]
> Application telemetry is off by default in Couchbase Server 8.0\. Future versions of Couchbase Server may enable it by default.

Couchbase Server reports the telemetry data it collects through the same Prometheus metrics endpoint it uses to publish its own metrics. Couchbase Server reports aggregated application telemetry metrics instead of reporting metrics on a per-client basis. See [Configure Prometheus to Collect Couchbase Metrics](../manage/monitor/set-up-prometheus-for-monitoring.md) to learn how to set up Prometheus to collect metrics from your Couchbase Server cluster.

### [](#prerequisites)Prerequisites

Your Couchbase Server cluster and your clients must meet the following requirements to use application telemetry:

* A Couchbase Server cluster only supports application telemetry when all of its nodes are running version 8.0 or later. Earlier versions of Couchbase Server do not support application telemetry. You cannot enable application telemetry if your cluster is running in mixed mode where all nodes are not running the same version of Couchbase Server.
* Your applications must use a recent SDK version that supports application telemetry. The following table lists the SDKs that support application telemetry along with the version where they added support.

| SDK                                                            | Minimum Version with Application Telemetry Support |
| -------------------------------------------------------------- | -------------------------------------------------- |
| [.NET](../../../dotnet-sdk/current/hello-world/overview.md)    | 3.8                                                |
| [C++](../../../cxx-sdk/current/hello-world/overview.md)        | 1.2                                                |
| [Go](../../../go-sdk/current/hello-world/overview.md)          | 2.11                                               |
| [Java](../../../java-sdk/current/hello-world/overview.md)      | 3.9                                                |
| [Kotlin](../../../kotlin-sdk/current/hello-world/overview.md)  | 3.9                                                |
| [Node.js](../../../nodejs-sdk/current/hello-world/overview.md) | 4.6                                                |
| [PHP](../../../php-sdk/current/hello-world/overview.md)        | 4.4                                                |
| [Python](../../../python-sdk/current/hello-world/overview.md)  | 4.5                                                |
| [Ruby](../../../ruby-sdk/current/hello-world/overview.md)      | 3.7                                                |
| [Scala](../../../scala-sdk/current/hello-world/overview.md)    | 3.9                                                |
* Your clients must be able to connect to the node's management port to create the WebSocket connection for telemetry data collection. The default management port is 8091 for unencrypted connections and 18091 for encrypted connections. Make sure any firewall rules between your clients and the nodes allow traffic on the management port.

> [!IMPORTANT]
> Enabling telemetry
> 
> Telemetry is turned off by default on Couchbase Server.
> 
> Use the following `curl` command to view the telemetry state on your server:
> 
> ```bash
> curl -u Administrator:password -X GET http://localhost:8091/settings/appTelemetry | jq
> ```
> 
> This returns a JSON object that contains the telemetry state as `true` or `false`.
> 
> ```json
> {
>   "enabled": false,
>   "maxScrapeClientsPerNode": 1024,
>   "scrapeIntervalSeconds": 60
> }
> ```
> 
> Execute the following `curl` command to enable telemetry on your cluster.
> 
> ```bash
> curl -u Administrator:password -X POST \
> http://localhoast:8091/settings/appTelemetry \
> -d enabled=true
> ```

## [](#http-methods)HTTP Methods

This API endpoint supports the following methods:

* [Get Application Telemetry Status](#get-status)
* [Configure Application Telemetry](#configure-telemetry)

## [](#get-status)Get Application Telemetry Status

The following method gets the current application telemetry settings the cluster.

GET /settings/appTelemetry

### [](#curl-syntax)curl Syntax

```bash
curl -sS -u $USER:$PASSWORD \
     -X GET 'http[s]://{host}:{port}/settings/appTelemetry'
```

#### [](#path-and-curl-parameters)Path and curl Parameters

`USER`

The name of a user who has 1 of the roles listed in [Required Privileges](#get-privs).

`PASSWORD`

The password for the `user`.

`host`

Hostname or IP address of a Couchbase Server node.

`port`

Port number for the REST API. Defaults are 8091 for unencrypted and 18901 for encrypted connections.

### [](#get-privs)Required Privileges

Your user account must have at least 1 of the following roles to get the application telemetry settings:

* [Full Admin](../learn/security/roles.md#full-admin)
* [Cluster Admin](../learn/security/roles.md#cluster-admin)
* [Read-Only Admin](../learn/security/roles.md#read-only-admin)

### [](#get-status-responses)Responses

`200 OK`

Returned when the call is successful. The response body contains a JSON object with the following fields:

* `enabled`: whether application telemetry is enabled or not.
* `maxScrapeClientsPerNode`: the maximum number of clients a single node can scrape telemetry data from at the same time.
* `scrapeIntervalSeconds`: how often Couchbase Server scrapes telemetry data from the clients, in seconds.

`403 Forbidden`

Returned if you do not have the proper roles to call this API. See [Required Privileges](#get-privs).

### [](#get-state-example)Examples

The following example gets the cluster's current application telemetry setting from the local node and pipes the result through `jq`.

```bash
 curl -sX GET -u Administrator:password \
      'http://localhost:8091/settings/appTelemetry' | jq
```

Running the previous command returns a JSON object similar to the following:

```json
{
  "enabled": false,
  "maxScrapeClientsPerNode": 1024,
  "scrapeIntervalSeconds": 60
}
```

## [](#configure-telemetry)Configure Application Telemetry

By sending a POST request to the `/settings/appTelemetry` endpoint, you can:

* Turn application telemetry on or off.
* Set the limit on the number of clients a single node can scrape telemetry data from at the same time.
* Set how often the nodes scrape telemetry data from clients.

Configure Application Telemetry

POST /settings/appTelemetry

### [](#curl-syntax-2)curl Syntax

```bash
curl -sS -u $USER:$PASSWORD \
  -X POST http://{host}:{port}/settings/appTelemetry \
  [-d enabled=[true|false]] \
  [-d maxScrapeClientsPerNode=<integer>] \
  [-d scrapeIntervalSeconds=<integer>]
```

#### [](#path-and-curl-parameters-2)Path and curl Parameters

`USER`

The name of a user who has 1 of the roles listed in [Required Privileges](#config-privs).

`PASSWORD`

The password for the `user`.

`host`

Hostname or IP address of a Couchbase Server node.

`port`

Port number for the REST API. Defaults are 8091 for unencrypted and 18901 for encrypted connections.

#### [](#rest-parameters)REST Parameters

`enabled` (Boolean, optional)

Set to `true` to enable application telemetry or `false` to turn it off.

Defaults to `false` (off). When you enable application telemetry, Couchbase Server advertises to SDK clients that it can collect telemetry data.

> [!NOTE]
> Future versions of Couchbase Sever may enable application telemetry by default.

`maxScrapeClientsPerNode` (integer, optional)

Sets the maximum number of clients a single node can scrape telemetry data from at the same time. If the number of client telemetry connections reaches this threshold, the node rejects new telemetry connections until the number of connected clients drops.

Valid values are from `1` to `1024`.

The default value is `1024`. You can set `maxScrapeClientsPerNode` to a lower value to reduce the number of clients that can connect to each node. Reducing the number of clients can potentially reduce the overhead of collecting telemetry data on your nodes if you have a large number of clients.

If a node reaches this limit, it starts rejecting new telemetry connections. Rejected clients can attempt to connect to another node in the cluster.

If all nodes in the cluster reach this limit, newly connected clients are not able to connect to a node to have their telemetry collected.

> [!NOTE]
> You can monitor the number of application telemetry connections by viewing the `cm_app_telemetry_curr_connections` metric. See [Metrics Reference](../metrics-reference/metrics-reference.md) and [Configure Prometheus to Collect Couchbase Metrics](../manage/monitor/set-up-prometheus-for-monitoring.md) for more information about metrics.

`scrapeIntervalSeconds` (integer, optional)

Sets how often the nodes scrape telemetry data from clients in seconds.

Valid values are `60` to `600`.

The default value is `60`.

You can increase this value to reduce the overhead of collecting telemetry data on your nodes. However, increasing this value means Couchbase Server misses collecting more telemetry data from clients before they disconnect. For example, suppose you set this value to `300`. Then Couchbase Server could lose up to 5 minutes of telemetry data from a client that disconnects just before the next scheduled telemetry collection.

If your applications have short-lived client connections to the cluster, consider keeping this value low to increase the chances of collecting telemetry before the clients disconnect.

### [](#config-privs)Required Privileges

Your user account must have at least 1 of the following roles to configure application telemetry:

* [Full Admin](../learn/security/roles.md#full-admin)
* [Cluster Admin](../learn/security/roles.md#cluster-admin)

### [](#responses)Responses

`200 OK`

Returned when the call is successful. A successful call also returns a JSON object with the new application telemetry settings. This object has the same format as the [response from the GET method](#get-status-responses).

`400 Bad Request`

Returned if you attempt to enable application telemetry on a cluster that's running in mixed mode where some nodes are running a version earlier than 8.0\. All the nodes in the cluster must be running version 8.0 or later to enable application telemetry. See [Prerequisites](#prerequisites) for more requirements.

`403 Forbidden`

Returned if you do not have the proper roles to call this API. See [Required Privileges](#config-privs) for a list of the required roles.

`404 Not Found`

Returned if you attempt to call the endpoint on a version of Couchbase Server earlier than 8.0.

### [](#config-examples)Examples

The following example enables telemetry, limits the node to scraping data from `512` clients, and sets the scrape interval to `90` seconds. It pipes the result through `jq` to make it easier to read.

```bash
curl -X POST -u Administrator:password \
     http://localhost:8091/settings/appTelemetry \
     -d enabled=true \
     -d maxScrapeClientsPerNode=512 \
     -d scrapeIntervalSeconds=90 | jq
```

If successful, the previous command returns the following JSON object containing the new application telemetry settings for the cluster:

```json
{
  "enabled": true,
  "maxScrapeClientsPerNode": 512,
  "scrapeIntervalSeconds": 90
}
```

## [](#see-also)See Also

* [Configure Prometheus to Collect Couchbase Metrics](../manage/monitor/set-up-prometheus-for-monitoring.md)
* See the SDK Telemetry from the Server section of the Collecting Information and Logging page in the documentation for the SDK you use. For example:

  * [C++ SDK](../../../cxx-sdk/current/howtos/collecting-information-and-logging.md#sdk-telemetry-from-the-server)
  * [Go SDK](../../../go-sdk/current/howtos/collecting-information-and-logging.md#sdk-telemetry-from-the-server)
  * [Java SDK](../../../java-sdk/current/howtos/collecting-information-and-logging.md#sdk-telemetry-from-the-server)
  * [Python SDK](../../../python-sdk/current/howtos/collecting-information-and-logging.md#sdk-telemetry-from-the-server)