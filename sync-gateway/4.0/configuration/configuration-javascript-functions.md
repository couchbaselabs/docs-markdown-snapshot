---
title: Using External Javascript Functions
description: How to use Javascript functions to customize data sync between cloud-and-edge.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/configuration/pages/configuration-javascript-functions.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:4.0@sync-gateway:configuration:configuration-javascript-functions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/4.0/configuration/configuration-javascript-functions.html)

# Using External Javascript Functions

> How to use Javascript functions to customize data sync between cloud-and-edge.  

Topic Group

[Configuration Schema](configuration-properties-legacy.md)| [Javascript Functions](configuration-javascript-functions.md)| [Environment Variables](configuration-environment-variables.md)| [REST API](configuration-rest-api.md)| [Persistent Configuration](configuration-overview.md)

## [](#introduction)Introduction

Sync Gateway supports the use of Javascript functions to customize the sync process. These functions are referenced from within the Sync Gateway Configuration and may be provided either as:

* An inline Javascript function
* An external Javascript file
* An external HTTP/HTTPS endpoint serving a JS function \[[1](#%5Ffootnotedef%5F1 "View footnote.")\].

## [](#operation)Operation

During database setup, Sync Gateway inspects the database configuration to identify and provision:

* Any inline JavaScript defined against any of the eligible configuration options
* Any external file or HTTP/S endpoint specified against any of the eligible configuration options that resolves to a Javascript function.

## [](#eligible-options)Eligible Options

Inline or external Javascript functions can be provided for any or all of the following configurable options:

* Sync Function
* Import Filter
* Custom Conflict Resolver
* Webhook Filter

## [](#configuration)Configuration

> [!NOTE]
> Sync gateway 3.x configuration of Javascript functions is done using the [Admin REST API](../rest-api/rest-api-admin.md); specifically the [Authentication](../rest-api/rest%5Fapi%5Fadmin.md#tag/Authentication) and [/{keyspace}/\_config/import\_filter](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-import%5Ffilter) endpoints.

Prior to this, configuration was done within the database configuration file — see: [Example 1](#ex-jsfunc-opts)

* Inline Javascript functions provided within the database configuration must be enclosed by a backtick pair (\`\`).
* To use an external Javascript function for any of the eligible options, you need to specify the absolute path to the Javascript. The format and content of the external Javascript is the same as that provided inline.  
> [!NOTE]  
> You must register a CA certificate for the appropriate server if external Javascript functions are hosted on HTTPS endpoints.  
> [!TIP]  
> For testing purposes you may use the unsupported configuration option `[unsupported.remote_config_tls_skip_verify](configuration-schema-database.md#database-unsupported-remote%5Fconfig%5Ftls%5Fskip%5Fverify     )`. Setting this `true` will side-step essential security checks. Do not use in Production deployments.

Example 1\. Configuring a Javascript Sync Function

This example shows the different ways you might provide a Javascript Sync Function. Although the example uses the Sync Function, the same approach applies wherever a Javascript function is valid (including with Import Filter, Webhook and Custom Conflict Resolver).

```json
curl -X PUT 'http://localhost:4985/db1/_config' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
         "sync": "/opt/couchbase-sync-gateway/sync.js" (1)
      },
    }
}'


  curl -X PUT 'http://localhost:4985/db2/_config' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
         "sync": "https://localhost/sync/func2" (2)
      }
   }
}


curl -X PUT 'http://localhost:4985/db3/_config' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
         "sync": `function(doc,oldDoc, meta){ if (doc.published) { channel("public");} }`
      } (3)
   }
}
```

| **1** | Here we specify an external file sync.js as containing the external function to be provisioned                |
| ----- | ------------------------------------------------------------------------------------------------------------- |
| **2** | Here we specify a HTTPS endpoint as resolving to a Javascript function to be provisioned                      |
| **3** | Here we specify inline Javascript (surrounded by a pair of backticks (\`\`) as the function to be provisioned |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](../access-control/sync-function/sync-function.md)
* [Import filter](../sync/import-processing.md)
* [Access Control](configuration-schema-access-control.md)
* [Add/Update Sync Function](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-sync)
* [Sync Function Overview](../access-control/sync-function/sync-function.md)

###### [](#-3)

Reference material …​

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)

---

[1](#%5Ffootnoteref%5F1). Sync Gateway 3.x