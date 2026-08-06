---
title: Configure CORS
description: Configure Cross-Origin Resource Sharing (CORS) in Couchbase Edge
  Server to enable browser-based clients and JavaScript SDKs to replicate
  directly with Couchbase Edge Server.
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.1/modules/rest-based-access/pages/cors.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:couchbase-edge-server:rest-based-access:cors.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-edge-server/current/rest-based-access/cors.html)

# Configure CORS

Configure Cross-Origin Resource Sharing (CORS) to allow browser-based clients and JavaScript SDKs to replicate directly with Couchbase Edge Server.

## [](#prerequisites)Prerequisites

* Couchbase Edge Server {version} or later.
* CORS is disabled by default. You must explicitly enable it in the server configuration.

## [](#about-cors-in-couchbase-edge-server)About CORS in Couchbase Edge Server

Modern browsers enforce strict origin validation for cross-site network requests. Without CORS support, browser-based clients, including the Couchbase Lite JavaScript SDK, cannot replicate with Couchbase Edge Server when the client origin differs from the Couchbase Edge Server host.

Couchbase Edge Server supports a single configurable CORS policy defined at the server level. When CORS is enabled, Couchbase Edge Server handles preflight requests and applies the configured origin, header, and age policies to responses.

Authentication and authorization are enforced consistently regardless of whether replication occurs via browser or native clients.

## [](#configure-cors)Configure CORS

Add a `cors` block to the top-level server configuration.

```json
{
  "cors": {
    "origin": ["https://example.com", "https://app.example.com"],
    "headers": ["Content-Type", "Authorization"],
    "max_age": 86400
  },
  "databases": {
    "mydb": { }
  }
}
```

__Table 1\. CORS Configuration Properties__
| Property | Type             | Description                                                                                                                                    |
| -------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| origin   | Array of strings | The list of allowed origins. Use \["\*"\] to allow all origins. Couchbase recommends restricting origins to known client hosts in production.  |
| headers  | Array of strings | The list of HTTP headers that browser clients are allowed to include in requests.                                                              |
| max\_age | Integer          | The duration in seconds that browsers can cache preflight response results. This reduces the number of preflight requests sent by the browser. |

## [](#next-steps)Next Steps

* To configure authentication for browser-based clients, see [Authentication](../configuration/authentication.md).
* To review available REST API operations, see [Edge Server REST API](rest-api-landing.md).