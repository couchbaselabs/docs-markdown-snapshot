---
title: Retrieving Cluster Information
description: Cluster information is retrieved with <code>GET /pools</code> HTTP
  method and URI.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-cluster-get.adoc
  xref: xref:enterprise-analytics:reference:rest-cluster-get.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-cluster-get.html)

# Retrieving Cluster Information

> Cluster information is retrieved with `GET /pools` HTTP method and URI. 

## [](#syntax)Syntax

Curl request syntax:

curl -u [admin]:[password] http://[localhost]:8091/pools

HTTP request syntax:

GET /pools
Host: localhost:8091
Authorization: Basic xxxxxxxxxxxxxxxxxxx
Accept: application/json

A _pool_ represents computing resources (machines, memory, CPU, disks) that are used by the cluster. Operational Insights clusters currently support only a single pool named `default`.

## [](#http-method-and-uri)HTTP method and URI

One of the first ways to discover the URI endpoints for the REST API is to find the available clusters. To find the available clusters, provide the Operational Insights IP address, port number, and append `/pools`.

GET /pools

## [](#example)Example

To send a request for cluster information using curl:

curl -u Administrator:password http://10.5.2.117:8091/pools

## [](#response)Response

Operational Insights returns only one cluster per group of systems and the cluster typically has a default name. Operational Insights returns the build number for the server in `implementationVersion` and the specifications supported are in `componentsVersion`. The product is identified by `prod` and `prodName`, and the configuration profile by `configProfile`. The services that nodes in the cluster run are listed in `allowedServices`.

The corresponding HTTP response contains a JSON document describing the cluster configuration.

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1037  100  1037    0     0  64294      0 --:--:-- --:--:-- --:--:-- 69133
{
    "allowedServices": [
        "kv",
        "cbas"
    ],
    "componentsVersion": {
        "ale": "3.0.0-1209-rel-enterprise",
        "asn1": "2.0.4",
        "compiler": "4.9.4",
        "couch": "2.1.1r-432-gc2af28d",
        "couch_index_merger": "2.1.1r-432-gc2af28d",
        "couch_set_view": "2.1.1r-432-gc2af28d",
        "couch_view_parser": "1.0.0",
        "crypto": "3.2",
        "inets": "5.9.8",
        "kernel": "2.16.4",
        "lhttpc": "1.3.0",
        "mapreduce": "1.0.0",
        "mochiweb": "2.4.2",
        "ns_server": "3.0.0-1209-rel-enterprise",
        "oauth": "7d85d3ef",
        "os_mon": "2.2.14",
        "public_key": "0.21",
        "sasl": "2.3.4",
        "ssl": "5.3.3",
        "stdlib": "1.19.4",
        "syntax_tools": "1.6.13",
        "xmerl": "1.3.6"
    },
    "configProfile": "analytics",
    "implementationVersion": "3.0.0-1209-rel-enterprise",
    "isAdminCreds": true,
    "isEnterprise": true,
    "isROAdminCreds": false,
    "pools": [
        {
            "name": "default",
            "streamingUri": "/poolsStreaming/default?uuid=995618a6a6cc9ac79731bd13240e19b5",
            "uri": "/pools/default?uuid=995618a6a6cc9ac79731bd13240e19b5"
        }
    ],
    "prod": "analytics",
    "prodName": "Operational Insights",
    "uuid": "995618a6a6cc9ac79731bd13240e19b5"
}