---
title: Public REST API
description: Description of the Sync Gateway REST API
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/rest-api.adoc
pubDate: 2026-03-28T05:05:12.980Z
link: xref:3.0@sync-gateway::rest-api.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/rest-api.html)

# Public REST API

> Description of the Sync Gateway REST API  

Related _REST API_ topics: [Admin REST API](rest-api-admin.md) | [Metrics REST API](rest-api-metrics.md)

> [!IMPORTANT]
> Content Blocking
> 
> Couchbase Mobile's API documentation utilizes [Swagger UI](https://swagger.io/tools/swagger-ui/)to deliver an interactive and dynamic user experience. The page will not function correctly if your organization's security policies restricts access to this type of content — instead see the alternate statics page [Public REST API (Static Page)](rest%5Fapi%5Fpublic%5Fstatic.md)

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

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](#)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](configuration-schema-bootstrap.md)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)