---
title: Public REST API
description: Description of the Sync Gateway Rest API'
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/rest-api.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@sync-gateway::rest-api.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/rest-api.html)

# Public REST API

> Description of the Sync Gateway Rest API'  

Related _REST API_ topics: [Admin REST API](../current/rest-api/rest-api-admin.md) | [Metrics REST API](../current/rest-api/rest-api-metrics.md) | [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

## [](#using-the-api-explorer)Using the API Explorer

The API explorer below groups all the endpoints by functionality. You can click on a label to expand the list of endpoints.

You can also send a request to each endpoint against an instance of Sync Gateway. To use this optional feature, enable _CORS_ by adding the following entry to the configuration file.

```javascript
{
    ...
    "CORS": {
        "Origin":["*"],
        "LoginOrigin":["*"],
        "Headers":["Content-Type"],
        "MaxAge": 1728000
    },
    ...
}
```

## [](#api-explorer)API Explorer

## [](#related-content)Related Content

###### [](#)

API Topics

* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-2)

Reference

* [Configuration Properties](../current/configuration/configuration-properties-legacy.md)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)