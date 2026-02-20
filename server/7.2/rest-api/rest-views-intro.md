---
title: Views API
description: The Views REST API is used to index and query JSON documents.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/rest-views-intro.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:rest-api:rest-views-intro.adoc[]
---

[View original HTML](/server/7.2/rest-api/rest-views-intro.html)

# Views API

> The Views REST API is used to index and query JSON documents. 

## [](#description)Description

Views are functions written in JavaScript that can serve several purposes in your application. You can use them to: find all the documents in your database, create a copy of data in a document and present it in a specific order, create an index to efficiently find documents by a particular value or by a particular structure in the document, represent relationships between documents, and perform calculations on data contained in documents.

> [!NOTE]
> View functions are stored in a design document as JSON. You can use the REST API to manage your design documents.

__Table 1\. Views endpoints__
| HTTP method | URI path                                                        | Description                                                       | Admin Role          |
| ----------- | --------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------- |
| GET         | _/\[bucket\_name\]/\_design/\[ddoc-name\]_                      | Retrieves all views design documents.                             | Full, Cluster, View |
| GET         | _/\[bucket\_name\]/\_design/\[ddoc-name\]/\_view/\[view-name\]_ | Retrieves views.                                                  | Full, Cluster, View |
| PUT         | _/\[bucket\_name\]/\_design/\[ddoc-name\]_                      | Creates a new design document with one or more views.             | Full, Cluster       |
| DELETE      | _/\[bucket\_name\]/\_design/\[ddoc-name\]_                      | Deletes design documents.                                         | Full, Cluster       |
| POST        | _/internalSettings_                                             | Changes the number of simultaneous requests each node can accept. | Full, Cluster       |