---
title: Data Modelling
description: <em>Couchbase Sync Gateway's</em> data model; for secure
  cloud-to-edge synchronization of enterprise data.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.1/modules/ROOT/pages/data-modeling.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.1@sync-gateway::data-modeling.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.1/data-modeling.html)

# Data Modelling

> _Couchbase Sync Gateway's_ data model; for secure cloud-to-edge synchronization of enterprise data.  

## [](#introduction)Introduction

The guidance and constraints documented here relate to the design of data buckets and documents that you require, or may potentially require, to replicate using Sync Gateway functionality. They do not necessarily align with constraints on the local storage and use of such documents.

## [](#property-naming)Property Naming

You can use an underscore prefix (`_`, ASCII `&#095`) for property naming, but your name cannot match any of the _Document_ system properties reserved by Sync Gateway:

* `_sync`
* `_id`
* `_rev`
* `_deleted`
* `_attachments`
* `_revisions`
* `_exp`
* `_purged`
* `_removed`

Any document that matches the reserved property names listed will be rejected by Sync Gateway — see [Example 1](#error-code) for the error details.

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

You may encounter the error in the following deployment situations:

* In Mobile-to-Web Data Sync with [Node.js Server SDK](../../nodejs-sdk/current/hello-world/start-using-sdk.md) and [Ottoman.js](http://ottomanjs.com/) (the Node.js ODM for Couchbase), where the rule conflicts with the `_type` property that is automatically added by _Ottoman.js_.  
A suggested workaround in this scenario is to fork the _Ottoman.js_ library, perform a search-replace for the `_type` property and replace it without a leading underscore.

> [!NOTE]
> For versions 2.x of Sync Gateway, you can encounter the following error:
> 
> * In Mobile-to-Web Data Sync with Field-level Encryption enabled, because the rule conflicts with the default [field encryption format](../../java-sdk/current/concept-docs/encryption.md#format)

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
This JSON object is a collection of key/value pairs. The values may be numbers, strings, arrays, or even nested objects. As a result, documents can represent complex data structures in a readily parsable and self-organizing manner.
* a binary object (also known as a _blob_ or _attachment_)  
These attachments provide a means to store large media files or any other non-textual data. Couchbase Lite supports attachments of unlimited size, although the Sync Gateway imposes a 20MB limit for attachments synced to it.

## [](#document-attributes)Document Attributes

Each _Document_ has the following attributes:

* A document ID
* A current revision ID (which changes when the document is updated)
* A history of past revision IDs (usually linear, but will form a branching tree if the document has or has had conflicts)
* A body in the form of a JSON object (a set of key/value pairs)
* Zero or more named binary attachments

## [](#document-change-history)Document Change History

Couchbase Lite tracks the change history of every document as a series of revisions, like version control systems such as Git or Subversion. Its main purpose is to enable the replicator to determine which data to sync and any conflicts arising.

Each document change is assigned a unique revision ID. The IDs of past revisions are available. The content of past revisions may be available if the revision was created locally and the database has not yet been compacted.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](#sync-function-overview.adoc)
* [Import filter](import-processing.md)

###### [](#-3)

Reference material …​

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)