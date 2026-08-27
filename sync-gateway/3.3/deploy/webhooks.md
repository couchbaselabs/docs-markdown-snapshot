---
title: Webhooks
description: Introducing Sync Gateway events and event handling with Webhooks
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.3/modules/deploy/pages/webhooks.adoc
  xref: xref:3.3@sync-gateway:deploy:webhooks.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.3/deploy/webhooks.html)

# Webhooks

> Introducing Sync Gateway events and event handling with Webhooks  
> You can configure webhooks to detect document\_changed events and post the changed documents to specified URLs.

Related _integration_ topics: [Changes Feed](changes-feed.md) | [Prometheus Integration](stats-prometheus.md)

> [!CAUTION]
> Caveats
> 
> Webhooks post your application's data, which might include user data, to URLs. Consider the security implications.

## [](#introduction)Introduction

Sync Gateway provides the ability to extend the replication process and build responsive services that react to changes in documents, adding value to the end to end process.

For example, by initiating the sending of notifications, or specialist audit processes, when certain document changes are detected.

This can be done using either the [changes feed](changes-feed.md) or `document_changed` events — see [Table 1](#tbl-scenarios) for a comparison of these scenarios.

Sync Gateway's **_webhook_** event handlers perform both document filtering, and HTTP POST operations, asynchronously.

In addition to providing the opportunity to integrate with external systems, this minimizes:

* The performance impact on Sync Gateway's regular processing
* The amount of Sync Gateway node CPU resources consumed by slow response times from the HTTP POST operations.

## [](#behavior)Behavior

Webhooks work on the push-cycle of a replication.

If a _webhook_ event handler is defined:

* Sync Gateway adds a `document_changed` event to the _event queue_ \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] whenever it updates a document in a Couchbase Server bucket. These changes \[[2](#%5Ffootnotedef%5F2 "View footnote.")\] can arise from Sync Gateway's Public REST API and-or Couchbase Lite push replications.
* Whenever the _event queue_ contains a _data\_changed_ event, Sync Gateway spawns a process to:

  * FILTER — decide which changed documents to post.  
  The event process executes the _webhook's_ event handler (the `filter`) on the associated document. The filter determines which documents need to be POSTed.  
  If there is no filter all document changes are passed to POST.
  * POST — send selected changed documents to the URL endpoint.  
  HTTP/HTTPS is used to POST the document changes selected by the filter to the defined _url_.

__Table 1\. Changes Feed vs Webhooks__
| Scenario                      | Changes feed (pull) | Webhooks (push) |
| ----------------------------- | ------------------- | --------------- |
| Sequence/Ordered              | Yes                 | No              |
| User Access Control           | Fine Grain          | Limited         |
| Scalable                      | Yes                 | No              |
| Data Stream replay on Failure | Yes                 | No              |

## [](#definition)Definition

You can define _Webhooks_ using the Admin Rest API [Database Configuration](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration) endpoints. For Pre-3.0 Legacy configurations, see the [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md) at the database level.

Sync Gateway supports the use of Javascript functions to customize the sync process. These functions are referenced from within the Sync Gateway Configuration and may be provided either as:

* An inline Javascript function
* An external Javascript file
* An external HTTP/HTTPS endpoint serving a JS function \[[3](#%5Ffootnotedef%5F3 "View footnote.")\].

Learn more about this property ($db.event\_handlers) in the Configuration Schema Reference — see: [database.event\_handlers](../configuration/configuration-schema-database.md#database-event%5Fhandlers).

> [!NOTE]
> Sync gateway 3.x configuration of Javascript functions is done using the [Admin REST API](../rest-api/rest-api-admin.md); specifically the [Authentication](../rest-api/rest%5Fapi%5Fadmin.md#tag/Authentication) and [/{keyspace}/\_config/import\_filter](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-import%5Ffilter) endpoints.

Prior to this, configuration was done within the database configuration file — see: [Example 1](#ex-jsfunc-opts)

* Inline Javascript functions provided within the database configuration must be enclosed by a backtick pair (\`\`).
* To use an external Javascript function for any of the eligible options, you need to specify the absolute path to the Javascript. The format and content of the external Javascript is the same as that provided inline.  
> [!NOTE]  
> You must register a CA certificate for the appropriate server if external Javascript functions are hosted on HTTPS endpoints.  
> [!TIP]  
> For testing purposes you may use the unsupported configuration option `[unsupported.remote_config_tls_skip_verify](../configuration/configuration-schema-database.md#database-unsupported-remote%5Fconfig%5Ftls%5Fskip%5Fverify     )`. Setting this `true` will side-step essential security checks. Do not use in Production deployments.

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

You can define multiple webhook event handlers. For example, you could define webhooks with different filtering criteria to post changed documents to different URLs — see: [Example 2](#ex-definitions).

### [](#document-change-properties)Document Change Properties

Each event handler definition comprises the following properties:

A Filter

Property name: [database.event\_handlers.document\_changed.filter](../configuration/configuration-schema-database.md#database-event%5Fhandlers-document%5Fchanged-filter)

The filter is a JavaScript function used to determine which documents to post. It accepts the document body as input and returns a boolean value.

* If the filter function returns true, then Sync Gateway posts the document.
* If the filter function returns false, then Sync Gateway does not post the document.
* If no filter function is defined, then Sync Gateway posts all changed documents.

Filtering only determines which documents to post. It does not extract specific content from documents and post only that.

An event handler type

Property name: [database.event\_handlers.document\_changed.handler](../configuration/configuration-schema-database.md#database-event%5Fhandlers-document%5Fchanged-handler)

Sets the event handler's type; currently, this must be `webhook`.

A timeout value

Property name: [database.event\_handlers.document\_changed.timeout](../configuration/configuration-schema-database.md#database-event%5Fhandlers-document%5Fchanged-timeout)

Sets the time (in seconds) to wait for a response to the POST operation. It ensures that slow-running POST operations don't cause the webhook event queue to back up. When the timeout limit is reached, Sync Gateway stops listening for a response and discards the operation.

You should not need to adjust the default setting to tune performance.

URL

Property name: [database.event\_handlers.document\_changed.url](../configuration/configuration-schema-database.md#database-event%5Fhandlers-document%5Fchanged-url)

Sets the address to which documents are posted.

Example 2\. Sample Webhook Definitions

* Simple Webhook
* Multiple Webhooks

In this simple example of a `webhook` event handler we define a single instance with no filter. It simply listens for the `document_changed` event and immediately sends the changed document to the URL `http://someurl.com`.

```javascript
"event_handlers": {
    "document_changed": [
        {
            "handler": "webhook",
            "url": "http://someurl.com"
        }
    ]
}
```

In this example we define two `webhook` event handlers, both of which use filters to decide how to process the changed document.

The `filter` function in the first handler recognizes documents with `doc.type` equal to `A` and posts the documents to the URL `http://someurl.com/type_A`.

The `filter` function in the second handler recognizes documents with `doc.type` equal to B and posts the documents to the URL `http://someurl.com/type_B`.

```javascript
"event_handlers": {
      "document_changed": [
        {"handler": "webhook",
         "url": "http://someurl.com/type_A",
         "filter": `function(doc) {
              if (doc.type == "A") {
                return true;
              }
              return false;
            }`
         },
        {"handler": "webhook",
         "url": "http://someurl.com/type_B",
         "filter": `function(doc) {
              if (doc.type == "B") {
                return true;
              }
              return false;
            }`
        }
     ]
  }
```

### [](#event-processing-properties)Event Processing Properties

Limited Concurrent Processes

Property name: [database.event\_handlers.max\_processes](../configuration/configuration-schema-database.md#database-event%5Fhandlers-max%5Fprocesses)

Sets the maximum number of events that can be processed concurrently. The default value should work well in the majority of cases. You should not need to adjust it to tune performance. However, if you wish to ensure that most webhook posts are sent, you can set it to sufficiently high value.

Limited Full-Queue Wait Time

Property name: [database.event\_handlers.wait\_for\_process](../configuration/configuration-schema-database.md#database-event%5Fhandlers-wait%5Ffor%5Fprocess)

Sets the maximum time (milliseconds) that event processing will wait for a free process, if an event is received whilst the event queue is full. You should not need to adjust it to tune performance.

To avoid blocking standard Sync Gateway processing, set a zero value. Any events arriving whilst the queue is full are then immediately discarded — see also [Logging](#lbl-evlog).

## [](#lbl-evlog)Logging

Sync Gateway creates a log whenever an event is discarded, and not added to the event queue.

You can configure the console logging of events using the configuration file and-or the ADMIN Rest API — see [Logging](../manage/logging.md). The `log_key` you need to include is `Event`; or `Events+` for more verbose output.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](../configuration/configuration-schema-bootstrap.md)
* [Database](../configuration/configuration-schema-database.md)
* [Database Security](../configuration/configuration-schema-db-security.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Import Filter](../configuration/configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](../configuration/configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

---

[1](#%5Ffootnoteref%5F1). An asynchronous event-processing queue 

[2](#%5Ffootnoteref%5F2). Creations, updates, and deletions 

[3](#%5Ffootnoteref%5F3). Sync Gateway 3.x