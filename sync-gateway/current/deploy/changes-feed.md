[View original HTML](/sync-gateway/current/deploy/changes-feed.html)

> Integrating Sync Gateway with other servers  
> This content describes how to use the changes feed to integrate Sync Gateway with other servers to build services that react to document changes.

Related _integration_ topics: [Webhooks](webhooks.md) | [Prometheus Integration](stats-prometheus.md)

## [](#introduction)Introduction

_Sync Gateway_ provides the ability to extend the replication process and build responsive services that react to changes in documents, adding value to the end to end process.

For example, you can initiate the sending of notifications, or specialist audit processes, when certain document changes are detected. This can be done using either the changes feed or [Webhooks](webhooks.md)\-- see [Table 1](#tbl-scenarios) for a comparison of these scenarios.

__Table 1\. Changes Feed vs Webhooks__
| Scenario                      | Changes feed (pull) | Webhooks (push) |
| ----------------------------- | ------------------- | --------------- |
| Sequence/Ordered              | Yes                 | No              |
| User Access Control           | Fine Grain          | Limited         |
| Scalable                      | Yes                 | No              |
| Data Stream replay on Failure | Yes                 | No              |

## [](#changes-feed)Changes Feed

The changes-feed for the receiver returns a sorted list of changes made to documents in the keyspace.

This article describes using the changes feed API to integrate sync gateway with other backend processes. For instance, if you have a channel called 'needs-email', you could have a bot that sends an email and then saves the document with a flag to keep it out of the 'needs-email' channel.

## [](#lbl-endpoint)Endpoint

The changes feed API is a REST API endpoint ([/{keyspace}/\_changes](../rest-api/rest%5Fapi%5Fpublic.md#tag/Database-Management/operation/get%5Fkeyspace-%5Fchanges)) that returns a sorted list of changes made to documents in the database. It permits applications to implement business logic that reacts to changes in documents.

## [](#lbl-methods)Methods

There are several methods of connecting to the changes feed (also know as the feed type). The first three methods (`polling`, `longpoll` and `continuous`) are based on the CouchDB API. The last method (`websocket`) is specific to sync gateway.

[polling](http://guide.couchdb.org/draft/notifications.html#polling) (default)

Returns the list of changes immediately. A new request must be sent to get the next set of changes.

[longpolling](http://guide.couchdb.org/draft/notifications.html#long)

In addition to regular polling, if the request is sent with a special `last_seq` parameter, it will stay open until a new change occurs and is posted.

[continuous](http://guide.couchdb.org/draft/notifications.html#continuous)

The continuous changes API allows you to receive change notifications as they come, in a single HTTP connection. You make a request to the continuous changes API and both you and sync gateway will hold the connection open “forever.”

[WebSockets](#lbl-websockets)

The WebSocket mode is conceptually the same as continuous mode but it should avoid issues with proxy servers and gateways that cause continuous mode to fail in many real-world mobile use cases.

## [](#lbl-websockets)WebSockets

In this section

[Specifying Options](#lbl-options) | [Messages](#lbl-messages) | [Compressed Feed](#lbl-compressed)

Continuous streaming HTTP responses may not be suitable for all deployments. Some proxy servers perform chunked-mode response parsing, which waits for the entire response to be buffered before sending it on. So, since the continuous feed response never ends, nothing is ever sent through to the client. This problem can be avoided using the WebSocket method.

The client requests WebSockets by setting the `_changes` URL’s feed query parameter to `websocket`, and opening a WebSocket connection to that URL — see: [Example 1](#ex-getfeed).

Example 1\. Changes Feed Request

```html
GET /db/_changes?feed=websocket HTTP/1.1
Connection: Upgrade
Upgrade: websocket
...
```

### [](#lbl-options)Specifying Options

After the connection opens, the client MUST send a single textual message to the server, specifying the feed options. This message is identical to the body of a regular HTTP POST to `_changes`, i.e. it’s a JSON object whose keys are the parameters (for example, `{"since": 112233, "include_docs": true}`). Depending on which client you use, make sure that options are sent as binary.

### [](#lbl-messages)Messages

Once the server receives the options, it will begin to send text-format messages. The messages are JSON; each contains one or more change notifications (in the same format as the regular feed) wrapped in an array — see: [Example 2](#ex-msg).

Example 2\. Sample Message

```bash
[ {"seq":1022,"id":"beer_Indiana_Amber","changes":[{"rev":"1-e8f6b2e1f220fa4c8a64d65e68469842"}]},
  {"seq":1023,"id":"beer_Iowa_Pale_Ale","changes":[{"rev":"1-db962c6d93c3f1720cc7d3b6e50ac9df"}]}
]
```

(The current server implementation sends at most one notification per message, but this could change. Clients should accept any number.)

An empty array is a special case: it denotes that at this point the feed has finished sending the backlog of existing revisions, and will now wait until new revisions are created. It thus indicates that the client has "caught up" with the current state of the database.

The `websocket` mode behaves like the `continuous` mode: after the backlog of notifications (if any) is sent, the connection remains open and new notifications are sent as they occur.

### [](#lbl-compressed)Compressed Feed

For efficiency, the feed can be sent in compressed form; this greatly reduces the bandwidth and is highly recommended.

To signal that it accepts a compressed feed, the client adds `"accept_encoding":"gzip"` to the feed options in the initial message it sends.

Compressed messages are sent from the server as binary. This is of course necessary as they contain gzip data, and it also lets the client distinguish them from uncompressed messages. (The server will only ever send one kind.)

The compressed messages sent from the server constitute a single stream of gzip-compressed data. They cannot be decompressed individually! Instead, the client should open a gzip decompression session when the feed opens, and write each binary message to it as input as it arrives. The output from the decompressor consists of a sequence of JSON arrays, each of which has the same interpretation as a text message (above).

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](../access-control/sync-function/sync-function.md)
* [Import filter](../sync/import-processing.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
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