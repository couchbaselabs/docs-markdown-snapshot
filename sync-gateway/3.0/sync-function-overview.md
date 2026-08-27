---
title: Sync Function Overview
description: Use Sync Gateway's Sync Functions to implement effective data
  routing and access control in the cloud-to-edge synchronization of enterprise
  data.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/sync-function-overview.adoc
  xref: xref:3.0@sync-gateway::sync-function-overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/sync-function-overview.html)

# Sync Function Overview

> Use Sync Gateway's Sync Functions to implement effective data routing and access control in the cloud-to-edge synchronization of enterprise data.  

_Related Concepts_: [Access Control Model](access-control-model.md) | [Channels](channels.md) | [Roles](roles.md) | Sync Function | [Users](users.md)

_Other Topics_: [Sync Function API](sync-function-api.md)

## [](#concept)Concept

The sync function is crucial to the security of your application. It is in charge of data validation, access control and routing. The function executes every time a new revision/update is made to a document.

![Sync Function Context](_images/sync-function-context.png) 

The sync function should be a focus of any security review of your application.

## [](#use)Use

The Sync Function exposes a number of helper functions to control access — see reference information in [Sync Function API](sync-function-api.md). For example, to grant a user access to a channel use the [access()](sync-function-api-access-cmd.md) helper function in the Sync Function.

The `access()` function can also operate on roles. If a user name string begins with role: then the remainder of the string is interpreted as a role name. There's no ambiguity here, because ":" is an illegal character in a user or role name.

Because anonymous requests are authenticated as the user "GUEST", you can make a channel and its documents public by calling access with a username of GUEST.

You will likely need to include a check for deleted documents and to treat these differently when validating. A deletion is just a revision with a "\_deleted": true property; and usually nothing else.

Any validation checks will probably fail because of the missing properties, so build -in a check for `doc._deleted == true`.

## [](#sync-function-prototype)Sync Function Prototype

Example 1\. Prototype Sync Function

* Version 3.x
* All Versions

```javascript
function (doc, oldDoc, meta) { (1)
   channel(doc.channels); (2)

}
```

| **1** | In version 3.x we can use XATTR contents to drive access control. To support this, an additional optional argument meta is exposed — see [Arguments](#lbl-args) |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | \[This prototype shows the default Sync Function — see [Arguments](#lbl-args) for more on the arguments.\]                                                      |

```javascript
function (doc, oldDoc) {
   channel(doc.channels); (1)
}
```

| **1** | \[This prototype shows the default Sync Function — see [Arguments](#lbl-args) for more on the arguments.\] |
| ----- | ---------------------------------------------------------------------------------------------------------- |

## [](#lbl-args)Arguments

The sync function arguments are:

| Name            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| doc             | This object references the content of the document that is being saved. It matches the JSON saved by the Couchbase Lite application and replicated to Sync Gateway. The document's \_id property contains the document ID The document's \_rev property is the new revision ID. If the document is being deleted, it will have a \_deleted property with the value true.                                                                                                           |
| oldDoc          | If the document has been saved before, this object references the revision being replaced; otherwise it is null. **Note:** In the case of a document with conflicts, the current provisional winning revision is passed in oldDoc. Your implementation of the sync function can omit the oldDoc parameter if you do not need it (JavaScript ignores extra parameters passed to a function).                                                                                        |
| meta (optional) | From 3.0 the Sync Function includes support for a new meta argument. This argument references the user defined XATTR that you can use to hold access grant data. The referenced object can include items such as channels or roles. So instead of embedding channel information directly within the document body, users can specify the user-defined XATTR associated with the document — see [Use XATTRs for Access Grants](access-control-how-use-xattrs-for-access-grants.md). |

## [](#configuration)Configuration

If you don't supply a sync function, Sync Gateway uses the [default Sync Function](configuration-schema-database.md#database-sync).

Example 2\. Configuring a Sync Function

* Version 3.x
* All Versions

Here we use the Database Configuration API to provision our Sync Function — see: [Database Configuration](configuration-schema-database.md)

The example uses _CURL_ to do this, but you may use a mechanism of your choice.

```bash
curl --location --request PUT 'http://localhost:4985/getting-started-db/_config' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "sync": ` /* sync function code */ `  (1)
        }'
```

> [!NOTE]
> Users running version v3.0+ must run with `disable-persistent-configuration=true`

Here we embed our Sync Function in our Sync Gateway configuration file.

```json
  //  ... may be preceded by additional configuration data as required by the user ...
  "databases": {
    "getting-started-db": {
      "name": "getting-started-db",
      "bucket": "getting-started-bucket",
      "import_docs": true,
      "num_index_replicas": 0,
      "sync": `/* sync function code */` (1)
  }
}
```

| **1** | Insert the Sync Function code, for example from [Example 3](#ex-sample-function) here. Note the sync function is enclosed in backticks. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------- |

## [](#example)Example

When you come to build your Sync Function you will need to decide the access control and document distribution requirements. For example:

* The document types it will process
* The users it will serve
* Which users need to access which document types
* What constraints are to be be placed on creating, updating and-or deleting documents

Our requirements for this example are:

| **1** | That all documents have the following properties: _creator_, _writers_, _title_ _channels_                           |
| ----- | -------------------------------------------------------------------------------------------------------------------- |
| **2** | That we allow only create and-or delete access to users with the role editor                                         |
| **3** | That we only allow changes, including deletions, to be made by users identified in the document's _writers_ property |
| **4** | That the _creator_ is immutable                                                                                      |
| **5** | That we will assign the document to the channel(s) identified within the documents contents or metadata (v3.0+).     |

Example 3\. Sync Function Example

* Version 3.x
* All Versions

You can use XATTR contents to drive access control.

```javascript
// Note the new (3.0), optional, argument `meta`
function (doc, oldDoc, meta) {
  if (doc._deleted) {
    // Only editors with write access can delete documents:
    requireRole("role:editor"); (2)
    requireUser(oldDoc.writers); (3)
    // Skip other validation because a deletion has no other properties:
    return;
  }
  // Required properties:
  if (!doc.title || !doc.creator ||
        !doc.channels || !doc.writers) { (1)
    throw({forbidden: "Missing required properties"});
  } else if (doc.writers.length == 0) {
    throw({forbidden: "No writers"});
  }
  if (oldDoc == null) {
    // Only editors can create documents:
    requireRole("role:editor"); (2)
    // The 'creator' property must match the user creating the document:
    requireUser(doc.creator)
  } else {
    // Only users in the existing doc's writers list can change a document:
    requireUser(oldDoc.writers); (3)
    // The "creator" property is immutable:
    if (doc.creator != oldDoc.creator) {
            throw({forbidden: "Can't change creator"}); (4)
    }
  }
  // Finally, assign the document to the channels in the list:
  channel(meta.xattrs.[xattrName]); (5)
}
```

Here we will use the document content to drive the channels to be accessed — using `doc.channels`

```javascript
function (doc, oldDoc) {
  if (doc._deleted) {
    // Only editors with write access can delete documents:
    requireRole("role:editor"); (2)
    requireUser(oldDoc.writers); (3)
    // Skip other validation because a deletion has no other properties:
    return;
  }
  // Required properties:
  if (!doc.title || !doc.creator ||
        !doc.channels || !doc.writers) { (1)
    throw({forbidden: "Missing required properties"});
  } else if (doc.writers.length == 0) {
    throw({forbidden: "No writers"});
  }
  if (oldDoc == null) {
    // Only editors can create documents:
    requireRole("role:editor"); (2)
    // The 'creator' property must match the user creating the document:
    requireUser(doc.creator)
  } else {
    // Only users in the existing doc's writers list can change a document:
    requireUser(oldDoc.writers); (3)
    // The "creator" property is immutable:
    if (doc.creator != oldDoc.creator) {
            throw({forbidden: "Can't change creator"}); (4)
    }
  }
  // Finally, assign the document to the channels in the list:
  channel(doc.channels); (5)
}
```

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](#)
* [Import filter](import-filter.md)
* [Access Control](configuration-schema-access-control.md)
* [Add/Update Sync Function](#rest-api-admin.html#/Access%5FControl/update%5Fsync%5Ffunction)
* [Sync Function Overview](#)

###### [](#-3)

Reference material …​

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)