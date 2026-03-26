---
title: Data Modelling
description: <em>Couchbase Sync Gateway's</em> data model; for secure
  cloud-to-edge synchronization of enterprise data.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/data-modeling.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@sync-gateway::data-modeling.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/data-modeling.html)

# Data Modelling

> _Couchbase Sync Gateway's_ data model; for secure cloud-to-edge synchronization of enterprise data.  

## [](#introduction)Introduction

The guidance and constraints documented here relate to the design of data buckets and documents that you require, or may potentially require, to replicate using sync gateway functionality. They do not necessarily align with constraints on the local storage and use of such documents.

## [](#property-naming)Property Naming

What to avoid

You should avoid designing user property names prefixed with an underscore character (`_`, ASCII `&#095`).

Why it's an issue

The underscore character (`_`) is a **reserved prefix** for _Document_ system properties, for example: the document's identifier (`_id`) and revision property (`_rev`).

Any document which does contain user properties with a leading underscore will be rejected by Sync Gateway — see [Example 1](#error-code) for the error details.

Example 1\. Property prefix error message

```text
"{"error":"Bad Request","reason":"user defined top level properties beginning with '_' are not allowed in document body"}"
```

Where it applies

This rule applies to writes performed through:

* Couchbase Lite SDKs
* Sync Gateway REST APIs
* Couchbase Server SDKs when [shared bucket access](sync-with-couchbase-server.md) is enabled.

When you might encounter the error

You are especially likely to encounter the error in the following deployment situations:

* In Mobile-to-Web Data Sync with Field-level Encryption enabled, because the rule conflicts with the default [field encryption format](../../java-sdk/current/concept-docs/encryption.md#format)
* In Mobile-to-Web Data Sync with [Node.js Server SDK](../../nodejs-sdk/current/hello-world/start-using-sdk.md) and [Ottoman.js](http://ottomanjs.com/) (the Node.js ODM for Couchbase), where the rule conflicts with the `_type` property that is automatically added by _Ottoman.js_.  
A suggested workaround in this scenario is to fork the _Ottoman.js_ library, perform a search-replace for the `_type` property and replace it without a leading underscore.

How to avoid the error

You should change any top-level user properties that have a key with a leading underscore , by either:

* Renaming them to remove the underscore, or,
* Wrapping them inside another object with a key that doesn't have a leading underscore.

## [](#document-structure)Document Structure

Couchbase's unit of data is a document, this is the NOSQL equivalent of a row or record.

Documents are stored as a key-value pair, which comprises a unique and immutable key, the _Id_, and a value representing the users' data (a JSON-object or binary blob).

### [](#key)Key

The document key, the _Id_, is:

* A UTF-8 string with no spaces, although it may contain special characters, such as (, %, /, ", and \_
* No longer than 250 bytes
* Unique within the bucket
* Automatically generated (as a UUID) or be set by the user or application when saved
* Immutable; that is, once saved the _Id_ cannot be changed.

### [](#value)Value

The document value is either:

* A JSON value, termed a _Document_.  
This JSON object is itself collection of key/value pairs, where the values may be numbers, strings, arrays or even nested objects themselves. As a result documents can represent highly-complex data structures in a readily parsable and self-organizing manner.
* a binary object (also known as a _blob_ or _attachment_)  
These attachments provide a means to store large media files or any other non-textual data. Couchbase Lite supports attachments of unlimited size, although the Sync Gateway currently imposes a 20MB limit for attachments synced to it.

## [](#document-attributes)Document Attributes

Each _Document_ has the following attributes:

* A document ID
* A current revision ID (which changes every time the document is updated)
* A history of past revision IDs (usually linear, but will form a branching tree if the document has or has had conflicts)
* A body in the form of a JSON object, i.e. a set of key/value pairs
* Zero or more named binary attachments

## [](#document-change-history)Document Change History

Couchbase Lite tracks the change history of every document as a series of revisions, like version control systems such as Git or Subversion. Its main purpose being to enable the replicator to determine the data to sync and any conflicts arising.

Each document change is assigned a unique revision ID. The IDs of past revisions are available. The content of past revisions may be available if the revision was created locally and the database has not yet been compacted.

## [](#related-content)Related Content

###### [](#)

Learn more …​

* [Sync Function](../current/access-control/sync-function/sync-function.md)
* [Import filter](../current/sync/import-processing.md)

###### [](#-2)

Reference material …​

* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)