---
title: Add a Capella Cluster to a Prometheus Server
description: Connect a Prometheus server to your Couchbase Capella cluster and
  collect metrics.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/monitoring/prometheus.adoc
pubDate: 2026-05-12T05:41:22.753Z
link: xref:cloud:clusters:monitoring/prometheus.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/monitoring/prometheus.html)

# Add a Capella Cluster to a Prometheus Server

> Connect a Prometheus server to your Couchbase Capella cluster and collect metrics. 

Each Capella cluster contains a native [Prometheus](https://prometheus.io) target enabling you to connect to Prometheus metrics. You can collect metrics in Capella using HTTP Service Discovery.

Use the following procedure to add a Capella cluster to your Prometheus server, and use a sample configuration file to start collecting metrics.

## [](#prerequisites)Prerequisites

You need the following prerequisites for each Capella cluster that you want to collect metrics from:

* Copy the Public Connection String to specify the Capella cluster endpoint for your client connection. For more information, see [Connect To Your Cluster](../../get-started/connect.md).
* Create or get cluster access credentials with Read access to all buckets and scopes in your cluster. For more information, see [Manage Cluster Access Credentials](../manage-database-users.md).
* Download the security certificate for your cluster and copy it into your Prometheus directory. For more information, see [Capella Root Certificates](../../security/security-certificates.md).
* Add a list of allowed IP addresses for your cluster. For more information, see [Configure Allowed IP Addresses](../allow-ip-address.md).
* Have a Prometheus server running. For more information, see [Collecting Cluster Metrics Blog](https://www.couchbase.com/blog/scraping-database-metrics-from-couchbase-capella-with-prometheus/) and [Configure Prometheus to Collect Couchbase Metrics](../../../server/current/manage/monitor/set-up-prometheus-for-monitoring.md).

## [](#define-collection-metrics-configuration)Define Collection Metrics Configuration

To define a collection metrics configuration:

1. Create a collection [configuration file](#configuration-file) in your Prometheus directory.  
For more information, see the [Collecting Cluster Metrics Blog](https://www.couchbase.com/blog/scraping-database-metrics-from-couchbase-capella-with-prometheus/) and [Configure Prometheus to Collect Couchbase Metrics](../../../server/current/manage/monitor/set-up-prometheus-for-monitoring.md).

> [!NOTE]
> To collect metrics over a private endpoint, see [Enable Metrics over Private Endpoints](#metrics-pe).

### [](#configuration-file)Use the Sample Configuration File

To start collecting metrics, use the following sample configuration file:

```yaml
- job_name: "capella-plmvshfqolmyxvpt"
  basic_auth:
    username: "metrics_user"
    password: "metrics_Passw0rd"
  tls_config:
    ca_file: "certs/couchbase-cloud-root-certificate.pem"
  scheme: https
  http_sd_configs:
  - url: https://<public-connection-string>:18091/prometheus_sd_config
    basic_auth:
      username: "metrics_user"
      password: "metrics_Passw0rd"
    tls_config:
      ca_file: "certs/couchbase-cloud-root-certificate.pem"
```

The sample configuration file contains the following information:

| Field     | Description                                                                                                            |
| --------- | ---------------------------------------------------------------------------------------------------------------------- |
| job\_name | Job name to collect metrics. This is the name Prometheus assigns to the process retrieving data from the target nodes. |
| username  | Cluster username.                                                                                                      |
| password  | Password of the cluster user.                                                                                          |
| ca\_file  | Cluster security certificate.                                                                                          |
| scheme    | Protocol scheme to configure requests.                                                                                 |
| url       | Concatenation of the Public Connection String, REST API, and REST endpoint.                                            |

### [](#metrics-pe)Collect Metrics over Private Endpoints

> [!NOTE]
> Collecting Prometheus metrics over private endpoints is only available upon request from Capella Support. To open a Support ticket, see [Create a Support Ticket](../../support/manage-support.md#create-support-ticket).

To collect metrics over a private endpoint connection, your cluster's configuration must meet specific requirements. If your configurations do not meet the requirements, use [VPC Peering](../../clouds/private-network.md).

Collecting metrics over a [private endpoint](../../security/private-endpoints.md) is only available with the following conditions:

| Supported Clusters                                                                      | Additional Requirements                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clusters deployed on [AWS](../../reference/aws.md)                                      | Clusters deployed on [AWS](../../reference/aws.md) can only have a maximum of 20 nodes. If you previously contacted Capella Support to map Query nodes separately with 1:1 node mapping over private endpoints, enabling metrics over private endpoints limits your cluster to a maximum of 13 nodes.\[[1](#footnote-1)\] |
| Clusters deployed on [GCP](../../reference/gcp.md) or [Azure](../../reference/azure.md) | There are no additional requirements for GCP or Azure clusters.                                                                                                                                                                                                                                                           |

\[[1](#node-caution)\] Enabling both 1:1 Query mapping and metrics requires the Data and Query Services to have dedicated listeners on each node, which reduces the number of nodes you can have to 13\. For more information, contact [Capella Support](../../support/manage-support.md#create-support-ticket).

#### [](#enable-private-endpoints-for-metrics)Enable Private Endpoints for Metrics

To enable private endpoints for Prometheus metrics:

1. Enable metrics with the [Management REST API](../../management-api-reference/index.md#tag/Private-Endpoint-Service).

  1. If you're enabling the private endpoint service for the first time, use the [POST v4/organizations/{organizationId}/projects/{projectIs}/clusters/{clusterId}/privateEndpointService](../../management-api-reference/index.md#tag/Private-Endpoint-Service/operation/enablePrivateEndpointService) endpoint.
  2. If you want to enable metrics after enabling the private endpoint service, use the [PUT /v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/privateEndpointService](../../management-api-reference/index.md#tag/Private-Endpoint-Service/operation/updatePrivateEndpointService) endpoint.
2. In your Prometheus directory, set the URL in your [configuration file](#configuration-file) as the concatenation of the Private Endpoint DNS URL, REST API, and Prometheus service discovery endpoint. For example:

```text
https://<private-endpoint-DNS-URL>:18091/prometheus_sd_config?network=external
```

## [](#see-also)See Also

* [Capella App Services Metrics API Reference](../../../app-services/references/rest%5Fapi%5Fmetric.md)
* [Prometheus Metrics](../../../sync-gateway/current/manage/stats-monitoring-prometheus.md)
* [Metrics Reference](../../metrics-reference/metrics-reference.md)