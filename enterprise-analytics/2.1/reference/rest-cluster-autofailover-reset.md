---
title: Resetting Auto-Failover
description: Auto-failover is reset by means of the <code>POST
  /settings/autoFailover/resetCount</code> HTTP method and URI.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/reference/pages/rest-cluster-autofailover-reset.adoc
  xref: xref:2.1@enterprise-analytics:reference:rest-cluster-autofailover-reset.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/reference/rest-cluster-autofailover-reset.html)

# Resetting Auto-Failover

> Auto-failover is reset by means of the `POST /settings/autoFailover/resetCount` HTTP method and URI. 

## [](#http-method-and-uri)HTTP method and URI

Resets the number of nodes that Enterprise Analytics has automatically failed over. A request can be sent to reset the auto-failover number to 0\. This is a global setting, which applies to all nodes in the cluster. Authentication is required to change this setting. No parameters are required.

```bourne
POST /settings/autoFailover/resetCount
```

## [](#syntax)Syntax

```bourne
curl -X POST -i -u [admin]:[password] \
  http://localhost:8091/settings/autoFailover/resetCount
```

## [](#example)Example

Curl request example:

```bourne
curl -X POST -i -u Administrator:password \
  http://10.5.2.54:8091/settings/autoFailover/resetCount
```

Raw HTTP request example:

```bourne
POST /settings/autoFailover/resetCount HTTP/1.1
Host: localhost:8091
Content-Type: application/x-www-form-urlencoded
Authorization: Basic YWRtaW46YWRtaW4=
```

## [](#response-codes)Response codes

```bourne
HTTP/1.1 200 OK
```

Possible errors include:

```bourne
This endpoint isn't available yet.
401 Unauthorized
```