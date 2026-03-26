---
title: CORS Configuration
description: Couchbase Lite JavaScript -- CORS Configuration for Replication
  with Sync Gateway
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-js/edit/release/1.0/modules/ROOT/pages/cors-configuration.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:couchbase-lite-javascript::cors-configuration.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite-javascript/current/cors-configuration.html)

# CORS Configuration

> Description — _Couchbase Lite JavaScript — CORS Configuration for Replication with Sync Gateway_  
> Related Content — [Remote Sync Gateway](replication.md) | [Handling Data Conflicts](conflict.md)

## [](#overview)Overview

Cross-Origin Resource Sharing (CORS) configuration is essential for enabling Couchbase Lite JavaScript to communicate and sync data with Sync Gateway from browser applications. Due to browser security restrictions, web applications must be explicitly allowed to make cross-origin requests to Sync Gateway.

This page explains the CORS requirements for Couchbase Lite JavaScript, how to configure Sync Gateway properly.

## [](#cors-configuration)CORS Configuration

> [!WARNING]
> Configuring CORS settings for Sync Gateway is a prerequisite for enabling data syncronization with the JavaScript SDK. The CORS configuration should be done in the [Sync Gateway Bootstrap Configuration](../../sync-gateway/current/configuration/configuration-schema-bootstrap.md#lbl-schema).

### [](#minimum-cors-settings)Minimum CORS Settings

Sync Gateway must be configured with CORS settings that allow your web application's origin.

Example 1\. Sync Gateway CORS Configuration

```json
{
  "databases": {
    "mydb": {
      "cors": {
        "origin": ["https://mywebsite.com"],
        "login_origin": ["https://mywebsite.com"],
        "headers": ["Authorization"]
      }
    }
  }
}
```

**Required CORS Properties:**

* `origin` \- Specify the exact `origin` (Access-Control-Allow-Origin) of your front-end application. Avoid using the wildcard `*`, as authentication requires explicit origins.
* `login_origin` \- Specify the exact `login_origin` of your front-end application. Avoid using the wildcard `*`, as authentication requires explicit origins.
* `headers` \- Must include `"Authorization"` header

## [](#related-content)Related Content

### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)

.

### [](#-2)

Learn more . . .

* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)
* [Databases](database.md)

.

### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.