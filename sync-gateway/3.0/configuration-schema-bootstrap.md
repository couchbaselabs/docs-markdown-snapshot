---
title: Bootstrap Configuration
description: Reference data on the contents of Sync Gateway's bootstrap
  configuration, which determines its run time behavior.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/configuration-schema-bootstrap.adoc
  xref: xref:3.0@sync-gateway::configuration-schema-bootstrap.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/configuration-schema-bootstrap.html)

# Bootstrap Configuration

> Reference data on the contents of Sync Gateway's bootstrap configuration, which determines its run time behavior.  

_Related topics_: [Overview](configuration-overview.md) | Bootstrap | [Database](configuration-schema-database.md) | [Database Security](#configuration-schema-db-security&.adoc#8212;​page}) | [Access Control](configuration-schema-access-control.md) | [Import](configuration-schema-import-filter.md) | [Inter-Sync Gateway Replication](configuration-schema-isgr.md)

> [!IMPORTANT]
> Pre-3.0 Legacy Configuration Equivalents
> 
> This content describes configuration for Sync Gateway 3.0 and higher — for legacy configuration, see: [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

## [](#introduction)Introduction

The _Sync Gateway_ bootstrap configuration is provisioned in a JSON format file. The configuration properties define sync gateway's runtime behavior. See the [schema](#lbl-schema) below for more details on these properties.

Sync gateway will look for the following configuration file unless you direct it otherwise:  
`/home/sync_gateway/sync_gateway.json`

Use the following command to run Sync Gateway with a configuration file:

```bashrc
sync_gateway sync-gateway-bootstrap.json
```

## [](#lbl-schema)Bootstrap Configuration Schema

This schema identifies all the configurable properties.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](#)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)