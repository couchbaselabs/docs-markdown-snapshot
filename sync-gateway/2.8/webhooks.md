---
title: Webhooks
description: Introducing Sync Gateway events and event handling with Webhooks
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/webhooks.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@sync-gateway::webhooks.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/webhooks.html)

# Webhooks

> Introducing Sync Gateway events and event handling with Webhooks  
> You can configure webhooks to detect document\_changed events and post the changed documents to specified URLs.

Related _integration_ topics: [Changes Feed](server-integration.md) | [External Stores](integrating-external-stores.md) | [Prometheus Integration](../current/deploy/stats-prometheus.md)

> [!CAUTION]
> Caveats
> 
> Webhooks post your application's data, which might include user data, to URLs. Consider the security implications.

## [](#introduction)Introduction

Sync Gateway provides the ability to extend the replication process and build responsive services that react to changes in documents, adding value to the end to end process.

For example, by initiating the sending of notifications, or specialist audit processes, when certain document changes are detected.

This can be done using either the [changes feed](server-integration.md) or `document_changed` events — see [Table 1](#tbl-scenarios) for a comparison of these scenarios.

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

Define _Webhooks_ in Sync Gateway's [Configuration Properties](../current/configuration/configuration-properties-legacy.md) using the database level [this\_db.event\_handlers](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-event%5Fhandlers) properties.

You can define multiple webhook event handlers. For example, you could define webhooks with different filtering criteria, which post changed documents to different URLs — see: [Example 1](#ex-definitions).

Each event handler definition comprises the following properties:

### [](#document-change-properties)Document Change Properties

A Filter

Property name: [this\_db.event\_handlers.document\_changed.filter](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-event%5Fhandlers-document%5Fchanged-filter)

The filter is a JavaScript function used to determine which documents to post. It accepts the document body as input and returns a boolean value.

* If the filter function returns true, then Sync Gateway posts the document.
* If the filter function returns false, then Sync Gateway does not post the document.
* If no filter function is defined, then Sync Gateway posts all changed documents.

Filtering only determines which documents to post. It does not extract specific content from documents and post only that.

An event handler type

Property name: [this\_db.event\_handlers.document\_changed.handler](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-event%5Fhandlers-document%5Fchanged-handler)

Sets the event handler's type; currently, this must be `webhook`.

A timeout value

Property name: [this\_db.event\_handlers.document\_changed.timeout](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-event%5Fhandlers-document%5Fchanged-timeout)

Sets the time (in seconds) to wait for a response to the POST operation. It ensures that slow-running POST operations don't cause the webhook event queue to back up. When the timeout limit is reached, Sync Gateway stops listening for a response and discards the operation.

You should not need to adjust the default setting to tune performance.

URL

Property name: [this\_db.event\_handlers.document\_changed.url](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-event%5Fhandlers-document%5Fchanged-url)

Sets the address to which documents are posted.

Example 1\. Sample Webhook Definitions

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

Property name: [this\_db.event\_handlers.max\_processes](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-event%5Fhandlers-max%5Fprocesses)

Sets the maximum number of events that can be processed concurrently. The default value should work well in the majority of cases. You should not need to adjust it to tune performance. However, if you wish to ensure that most webhook posts are sent, you can set it to sufficiently high value.

Limited Full-Queue Wait Time

Property name: [this\_db.event\_handlers.wait\_for\_process](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-event%5Fhandlers-wait%5Ffor%5Fprocess)

Sets the maximum time (milliseconds) that event processing will wait for a free process, if an event is received whilst the event queue is full. You should not need to adjust it to tune performance.

To avoid blocking standard Sync Gateway processing, set a zero value. Any events arriving whilst the queue is full are then immediately discarded — see also [Logging](#lbl-evlog).

## [](#lbl-evlog)Logging

Sync Gateway creates a log whenever an event is discarded, and not added to the event queue.

You can configure the console logging of events using the configuration file and-or the ADMIN Rest API — see [Use the Logging API](../current/manage/logging.md). The `log_key` you need to include is `Event`; or `Events+` for more verbose output.

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

---

[1](#%5Ffootnoteref%5F1). An asynchronous event-processing queue 

[2](#%5Ffootnoteref%5F2). Creations, updates, and deletions