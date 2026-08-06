---
title: Listing Node Services
description: The services running on a specific node can be listed, with their
  respective port numbers, by means of the <code>GET
  /pools/default/nodeServices</code> method and URI.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/reference/pages/rest-list-node-services.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:enterprise-analytics:reference:rest-list-node-services.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/reference/rest-list-node-services.html)

# Listing Node Services

> The services running on a specific node can be listed, with their respective port numbers, by means of the `GET /pools/default/nodeServices` method and URI. 

## [](#http-method-and-uri)HTTP methods and URI

GET /pools/default/nodeServices

## [](#rest-listing-node-services-description)Description

Enterprise Analytics and other essential processes are associated with specific port numbers. A complete list of the associations is provided in [Enterprise Analytics Ports](#install/cb-enterprise-analytics-ports.adoc).

The services and processes currently occupying these port numbers on a given node are listed by means of the `GET /pools/default/nodeServices` method and URI.

## [](#curl-syntax)Curl Syntax

curl -v -X GET -u [admin]:[password]
http://[ip-address]:8091/pools/default/nodeServices

## [](#responses)Responses

Success gives the status `200 OK`, and returns an object containing a list that includes all services and their port numbers, plus any alternate addresses and port numbers that may have been configured.

If an incorrect primary address is specified, a `Could not resolve host: <host-number>` error message is displayed.

If the URI is incorrectly specified, a `404 Object Not Found` error is flagged.

## [](#example)Example

The following example pipes the returned object to the `jq` command, to facilitate readability:

curl -v -X GET -u Administrator:password \
http://10.143.192.101:8091/pools/default/nodeServices | jq

The displayed output is as follows:

{
  "rev": 2142,
  "nodesExt": [
    {
      "services": {
        "cbas": 8095,
        "cbasSSL": 18095,
        "mgmt": 8091,
        "mgmtSSL": 18091,
        "kv": 11210,
        "kvSSL": 11207,
        "projector": 9999
      },
      "thisNode": true,
      "hostname": "10.143.192.101",
      "alternateAddresses": {
        "external": {
          "hostname": "10.10.10.11",
          "ports": {
            "cbas": 9000
          }
        }
      }
    }
  ],
  "clusterCapabilitiesVer": [
    1,
    0
  ],
  "clusterCapabilities": {
    "n1ql": [
      "costBasedOptimizer",
      "indexAdvisor",
      "javaScriptFunctions",
      "inlineFunctions",
      "enhancedPreparedStatements",
      "readFromReplica"
    ],
    "search": [
      "vectorSearch",
      "scopedSearchIndex"
    ]
  },
  "clusterUUID": "0b62493dd7b49e1421134c17c9733682",
  "clusterName": "",
  "prod": "analytics",
  "prodName": "Enterprise Analytics"
}

The output may include information about ports used by:

* REST and HTTP-based management, including Couchbase Web Console (`8091` and `18091`).
* The Data Service (`11210` and `11207`).

## [](#see-also)See Also

A complete list of Couchbase Services and the ports they occupy, along with information about custom port mapping, is provided in [Enterprise Analytics Ports](#install/cb-enterprise-analytics-ports.adoc).