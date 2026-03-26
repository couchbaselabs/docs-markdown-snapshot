---
title: Sync Function
description: About Sync Gateway <em>Roles</em> and their part in secure
  cloud-to-edge enterprise data synchronization.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/access-control/pages/sync-function/sync-function.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:sync-gateway:access-control:sync-function/sync-function.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/access-control/sync-function/sync-function.html)

# Sync Function

> About Sync Gateway _Roles_ and their part in secure cloud-to-edge enterprise data synchronization.  
> Here we introduce the concept of _Roles_ and the part they play in assuring secure access control within _Sync Gateway_.

_Related Topics_: [Concepts](../access-control-concepts.md) | [How-to](../access-control-how.md) | [Sync Function](sync-function.md) | [Use XATTRs for Access Grants](../access-control-how-use-xattrs-for-access-grants.md)

## [](#concept)Concept

The sync function is crucial to the security of your application. It is in charge of data validation, access control and routing. The function executes every time a new revision/update is made to a document.

![Sync Function Context](../../_images/sync-function-context.png) 

The sync function should be a focus of any security review of your application.

## [](#use)Use

The Sync Function exposes a number of helper functions to control access — see reference information in [Sync Function API](sync-function-api.md). For example, to grant a user access to a channel use the [access()](sync-function-api-access-cmd.md) helper function in the Sync Function.

The `access()` function can also operate on roles. If a user name string begins with role: then the remainder of the string is interpreted as a role name. There's no ambiguity here, because ":" is an illegal character in a user or role name.

Because anonymous requests are authenticated as the user "GUEST", you can make a channel and its documents public by calling access with a username of GUEST.

You will likely need to include a check for deleted documents and to treat these differently when validating. A deletion is just a revision with a "\_deleted": true property; and usually nothing else.

Any validation checks will probably fail because of the missing properties, so build -in a check for `doc._deleted == true`.

## [](#ex-sync-function)Sync Function Examples

Couchbase Sync Gateway defines a Sync Function at the `collection` level. Defining at this level helps simplify data management and improve data reliability. Each collection in the system allows for only one Sync Function, which enables the specification of Access Control rules.

> [!NOTE]
> The Sync Function uses the [ES5 standard](https://ecma-international.org/wp-content/uploads/ECMA-262%5F5.1%5Fedition%5Fjune%5F2011.pdf) of JavaScript syntax.

Example 1\. Default Sync Function

```javascript
function (doc, oldDoc, meta) {
   channel(CollectionName);

}
```

Here the function then calls the `channel` and passes in the name of the collection `(CollectionsName)` as an argument.

By default, every document in the collection is automatically assigned to a channel with the same name as the collection. This system automatically creates a channel with the collection's name. The assignment of all documents to the collection channel is functionally similar to assigning them to the [All Documents Channel](../access-control-concepts.md#lbl-alldocs-channel).

To override this, use a custom sync function or a Specified Default Sync Function.

Example 2\. Upgraded Default Sync Function

```javascript
function (doc, oldDoc, meta) {
   channel(doc.channels);

}
```

Here is the default Sync Function when you have upgraded; it remains the same as the previous version.

## [](#lbl-args)Arguments

The sync function arguments are:

| Name            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| doc             | This object references the content of the document that is being saved. It matches the JSON saved by the Couchbase Lite application and replicated to Sync Gateway. The document's \_id property contains the document ID The document's \_rev property is the new revision ID. If the document is being deleted, it will have a \_deleted property with the value true.                                                                                                              |
| oldDoc          | If the document has been saved before, this object references the revision being replaced; otherwise it is null. **Note:** In the case of a document with conflicts, the current provisional winning revision is passed in oldDoc. Your implementation of the sync function can omit the oldDoc parameter if you do not need it (JavaScript ignores extra parameters passed to a function).                                                                                           |
| meta (optional) | From 3.0 the Sync Function includes support for a new meta argument. This argument references the user defined XATTR that you can use to hold access grant data. The referenced object can include items such as channels or roles. So instead of embedding channel information directly within the document body, users can specify the user-defined XATTR associated with the document — see [Use XATTRs for Access Grants](../access-control-how-use-xattrs-for-access-grants.md). |

## [](#configuration)Configuration

If you don't supply a sync function, Sync Gateway uses the [default Sync Function](../../configuration/configuration-schema-database.md#database-sync).

Example 3\. Configuring a Sync Function

* Version 3.x
* All Versions

Here we use the Database Configuration API to provision our Sync Function — see: [Database Configuration](../../configuration/configuration-schema-database.md)

The example uses _CURL_ to do this, but you may use a mechanism of your choice.

```bash
curl --location --request PUT 'http://localhost:4985/getting-started-db.foo.bar/_config' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "sync": ` /* sync function code */ `  (1)
        }'
```

> [!NOTE]
> Users running version v3.0+ must run with `disable_persistent_config=true`

Here we embed our Sync Function in our Sync Gateway configuration file.

```json
  //  ... may be preceded by additional configuration data as required by the user ...
  "databases": {
    "getting-started-db": {
      "name": "getting-started-db",
      "bucket": "getting-started-bucket",
      "import_docs": true,
      "index": {
        "num_replicas": 0
      },
      "sync": `/* sync function code */` (1)
  }
}
```

| **1** | Insert the Sync Function code, for example from [Example 4](#ex-sample-function) here. Note the sync function is enclosed in backticks. |
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

Example 4\. Sync Function Example

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

## [](#lbl-access)access()

Function

access(username, channelname)

### [](#purpose)Purpose

Use the `access()` function to grant a user access to a channel.

### [](#arguments)Arguments

| Argument | Description                                                                                                                                                                                                                                                           |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| username | Must be a string identifying a user, or an array of strings identifying multiple users; the function is applied to each user in the array. If the value resolves to null the function result is a no-op.                                                              |
| channels | Must be a string identifying a channel name, or an array of strings to specify multiple channel names (for example: (\['channel1', 'channel2'\]); the function is applied to each element in the array. If the value resolves to null the function result is a no-op. |

> [!NOTE]
> As a convenience, the resolved value of either argument may be `null` or `undefined`, in which case nothing happens.

### [](#context)Context

You can invoke this function multiple times from within your Sync Function.

> [!TIP]
> Prefix the `username` argument value with `role:` to apply this function to a role rather than a user. This grants access to the specified channel(s) for all users assigned that role.

The effects of all access calls by all active documents are effectively combined in a union, so if _any_ document grants a user access to a channel, that user has access to the channel.

> [!NOTE]
> The sync function `access()` call does not support the wildcard ('**\***') for granting access to all channels. To grant a user access to all channels, use the REST API channel grant endpoint.

### [](#use-2)Use

Example 5\. access(username, channel)

This example shows some valid ways to call `access()`:

```javascript
access ("jchris", "mtv"); (1)
access ("jchris", ["mtv", "mtv2", "vh1"]); (2)
access (["snej", "jchris", "role:admin"], "vh1"); (3)
access (["snej", "jchris"], ["mtv", "mtv2", "vh1"]); (4)
access (null, "hbo");  (5)
access ("snej", null);
```

| **1** | Allow access of single channel to single user       |
| ----- | --------------------------------------------------- |
| **2** | Allow access of multiple channels to single user    |
| **3** | Allow access of single channel to multiple users    |
| **4** | Allow access of multiple channels to multiple users |
| **5** | The null arguments mean these are treated as no-ops |

> [!WARNING]
> If you invoke the `access()` function multiple times to grant the same user access to the same channel, you could see negative performance effects, such as large fetches or request timeouts.

## [](#lbl-channel)channel()

### [](#function-call)Function Call

channel(channelname)

### [](#purpose-2)Purpose

Use the `channel()` function to route the document to the named channel(s).

### [](#arguments-2)Arguments

| Argument | Description                                                                                                                                                                                                                                                           |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| channels | Must be a string identifying a channel name, or an array of strings to specify multiple channel names (for example: (\['channel1', 'channel2'\]); the function is applied to each element in the array. If the value resolves to null the function result is a no-op. |

### [](#ex-sync-function-API-channel)Sync Function Examples

Couchbase Sync Gateway defines a Sync Function at the `collection` level. Defining at this level helps simplify data management and improve data reliability. Each collection in the system allows for only one Sync Function, which enables the specification of Access Control rules.

Example 6\. Default Sync Function

```javascript
function (doc, oldDoc, meta) {
   channel(CollectionName);

}
```

Here the function then calls the `channel` and passes in the name of the collection `(CollectionsName)` as an argument.

By default, every document in the collection is automatically assigned to a channel with the same name as the collection. This system automatically creates a channel with the collection's name. The assignment of all documents to the collection channel is functionally similar to assigning them to the [Star Channel](#2.7@sync-gateway-channels.adoc#star-channel).

To override this, use a custom sync function or a Specified Default Sync Function.

Example 7\. Upgraded Default Sync Function

```javascript
function (doc, oldDoc, meta) {
   channel(doc.channels);

}
```

Here is the default Sync Function when you have upgraded; it remains the same as the previous version.

### [](#context-2)Context

The channel function can be called zero or more times from the sync function, for any document.

> [!NOTE]
> Channels don't have to be predefined.  
> A channel implicitly comes into existence when a document is routed to it.

Routing changes have no effect until the document is actually saved in the database, so if the sync function first calls `channel()` or `access()`, but then rejects the update, the channel and access changes will not occur.

> [!TIP]
> As a convenience, it is legal to call `channel` with a `null` or `undefined` argument; it simply does nothing.  
> This allows you to do something like `channel(doc.channels)` without having to first check whether `doc.channels` exists.

### [](#use-3)Use

Example 8\. channel(channelname)

This example routes all "published" documents to the "public" channel:

```javascript
function (doc, oldDoc, meta) {
   if (doc.published) {
      channel("public");
   }
}
```

## [](#lbl-expiry)expiry()

Function

expiry(value)

### [](#purpose-3)Purpose

Use `expiry(value)` to set the expiry value (TTL) on the document.

### [](#arguments-3)Arguments

| Argument | Description                                                                                                                                                                                                                    |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| value    | The value can be specified in two ways: As an **ISO-8601 format:** date string — or example the 6th of July 2016 at 17:00 in the BST timezone would be 2016-07-06T17:00:00+01:00; As a numeric Couchbase Server expiry value 1 |

1 Couchbase Server expiries are specified as Unix time, and if the desired TTL is below 30 days then it can also represent an interval in seconds from the current time (for example, a value of 5 will remove the document 5 seconds after it is written to Couchbase Server).

### [](#context-3)Context

Under the hood, the expiration time is set and managed on the Couchbase Server document (TTL is not supported for databases in walrus mode).

#### [](#impact)Impact

The impact on the resulting document when the expiry value is reached depends on the setting of shared-bucket-access:

Enabled

The **active** revision of the document is tombstoned.

If there is another non-tombstoned revision for this document (i.e a conflict) it will become the active revision.

The tombstoned revision will be purged when the server's metadata purge interval is reached.

Disabled

The document will be purged from the database.

As with the existing explicit purge mechanism, this applies only to the local database; it has nothing to do with replication.

This expiration time is not propagated when the document is replicated.

The purge of the document does not cause it to be deleted on any other database.

#### [](#inspect-a-document-expiry-value)Inspect a Document Expiry Value

You can retrieve a document's expiration time, as it is returned in the response of GET [/{keyspace}/{docid}](../../rest-api/rest%5Fapi%5Fpublic.md#tag/Document/operation/get%5Fkeyspace-docid) using `show_exp=true` as the querystring.

```bash
curl -X GET "http://localhost:4985/ourdb/ourdoc?show_exp=true" -H "accept: application/json"
```

### [](#use-4)Use

Example 9\. expiry(value)

```javascript
expiry("2022-06-23T05:00:00+01:00") (1)
```

| **1** | Sets the expiry date to 5am on the 23rd June 2022. |
| ----- | -------------------------------------------------- |

## [](#lbl-require-access)requireAccess()

Function

requireAccess(channels)

### [](#purpose-4)Purpose

Use the `requireAccess()` function to reject document updates that are not made by the a user with access to at least one of the given channels, as shown in [Example 10](#ex-requireaccess)

### [](#arguments-4)Arguments

| Argument | Description                                                                                                                                                                                                                                                           |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| channels | Must be a string identifying a channel name, or an array of strings to specify multiple channel names (for example: (\['channel1', 'channel2'\]); the function is applied to each element in the array. If the value resolves to null the function result is a no-op. |

### [](#context-4)Context

The function signals rejection by throwing an exception, so the rest of the sync function will not be run.

Note that `requireAccess()` will only recognize grants made explicitly using a channel name (not by a wildcard).

So, if a user was granted access using only the [all channels wildcard](../channels.md#lbl-all-channels)\] (`*`), then `requireAccess('anychannelname')'` will fail because the user wasn't granted access to that channel (only to the `*` channel).

### [](#use-5)Use

Example 10\. requireAccess(channels)

```javascript
requireAccess("events"); (1)

if (oldDoc) {
    requireAccess(oldDoc.channels); (2)
}
```

| **1** | Throw an exception unless the user has access to read the "events" channel:                                   |
| ----- | ------------------------------------------------------------------------------------------------------------- |
| **2** | Throw an exception unless the user can read one of the channels in the previous revision's channels property: |

## [](#lbl-require-admin)requireAdmin()

Function

requireAdmin()

### [](#purpose-5)Purpose

Use the `requireAdmin()` function to reject document updates that are not made by the Sync Gateway Admin REST API.

### [](#arguments-5)Arguments

There are no arguments.

### [](#use-6)Use

Example 11\. requireadmin

```javascript
requireAdmin(); (1)
```

| **1** | Throw an exception unless the request is sent to the Admin REST API |
| ----- | ------------------------------------------------------------------- |

## [](#lbl-require-role)requireRole()

Function

requireRole(rolename)

### [](#purpose-6)Purpose

Use the `requireRole()` function to reject document updates that are not made by user with the specified role or roles, as shown in [Example 12](#ex-requirerole).

### [](#arguments-6)Arguments

| Argument | Description                                                                                                                                                                                                                                                                                                                               |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| rolename | Must be a string identifying a role, or an array of strings identifying multiple roles; the function is applied to each role in the array. If the value resolves to null the function result is a no-op. **Note** — Role names must always be prefixed with role:; an exception is thrown if a role name doesn't conform with this rule.. |

### [](#context-5)Context

The function requires that the user has at least one of the specified roles. If that is not the case it signals rejection by throwing an exception. The rest of the sync function will not be run.

### [](#use-7)Use

Example 12\. requireRole(rolename)

```javascript
requireRole("admin"); (1)

requireRole(["admin", "old-timer"]); (2)
```

| **1** | Throw an error unless the user has the "admin" role:           |
| ----- | -------------------------------------------------------------- |
| **2** | Throw an error unless the user has one or more of those roles: |

## [](#lbl-require-user)requireUser()

Function

requireUser(username)

### [](#purpose-7)Purpose

Use the `requireUser()` function to reject document updates that are not made by the specified user or users.

### [](#arguments-7)Arguments

| Argument | Description                                                                                                                                                                                              |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| username | Must be a string identifying a user, or an array of strings identifying multiple users; the function is applied to each user in the array. If the value resolves to null the function result is a no-op. |

### [](#context-6)Context

The function signals rejection by throwing an exception, so the rest of the sync function will not be run.

When validating a document, you should treat all properties of the `doc` parameter as _untrusted_. That is because it **is** the object that you're validating. This may sound obvious, but it can be easy to make mistakes, like calling `requireUser(doc.owners)` instead of `requireUser(oldDoc.owners)`.

When using one document property to validate another, look up that property in `oldDoc`, not `doc`!

### [](#use-8)Use

Example 13\. requireUser(username)

```javascript
requireUser("snej"); (1)

requireUser(["snej", "jchris", "tleyden"]); (2)
```

| **1** | Throw an error if the user is not "snej":                 |
| ----- | --------------------------------------------------------- |
| **2** | Throw an error if user's name is not in the list username |

## [](#lbl-role)role()

Function

role(username, rolename)

### [](#lbl-role)Purpose

Use the `role()` function to add a role to a user. This indirectly gives them access to any channels assigned to that role.

> [!NOTE]
> Roles, like users, have to be explicitly created by an administrator.

### [](#arguments-8)Arguments

| Argument | Description                                                                                                                                                                                                                                                                                                                               |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| rolename | Must be a string identifying a role, or an array of strings identifying multiple roles; the function is applied to each role in the array. If the value resolves to null the function result is a no-op. **Note** — Role names must always be prefixed with role:; an exception is thrown if a role name doesn't conform with this rule.. |
| username | Must be a string identifying a user, or an array of strings identifying multiple users; the function is applied to each user in the array. If the value resolves to null the function result is a no-op.                                                                                                                                  |

### [](#context-7)Context

This function affects the user's ability to revise documents, if the access function requires role membership to validate certain types of changes. Its use is similar to `access`.

Nonexistent roles don't cause an error, but have no effect on the user's access privileges.

> [!TIP]
> You can create roles retrospectively. As soon as a role is created, any pre-existing references to it take effect.

### [](#use-9)Use

Example 14\. role(username, rolename)

```javascript
role ("jchris", "role:admin"); (1)
role ("jchris", ["role:portlandians", "role:portlandians-owners"]); (2)
role (["snej", "jchris", "traun"], "role:mobile"); (3)
role ("ed", null);  (4)
```

| **1** | The role admin is assigned to the user             |
| ----- | -------------------------------------------------- |
| **2** | Both the named roles are assigned to the user      |
| **3** | The role mobile is assigned to all the named users |
| **4** | No op                                              |

## [](#lbl-throw)throw()

Function

throw()

### [](#purpose-8)Purpose

Use `throw()` to prevent a document from persisting or syncing to any other users.

### [](#arguments-9)Arguments

No arguments

### [](#context-8)Context

You enforce the validity of document structure by checking the necessary constraints and throwing an exception if they're not met.

In validating a document, you'll often need to compare the new revision to the old one, to check for illegal changes in state. For example, some properties may be immutable after the document is created, or may be changeable only by certain users, or may only be allowed to change in certain ways. That's why the current document contents are given to the sync function, as the `oldDoc` parameter.

We recommend that you not create invalid documents in the first place. As much as possible, your app logic and validation function should prevent invalid documents from being created locally. The server-side sync function validation should be seen as a fail-safe and a guard against malicious access.

### [](#use-10)Use

Example 15\. throw(forbidden:)

In this example the sync function disallows all writes to the database it is in.

```javascript
function(doc) {

   throw({forbidden: "read only!"}) (1)

}
```

| **1** | The document update will be rejected with an HTTP 403 "Forbidden" error code, with the value of the forbidden: property being the HTTP status message.This is the preferred way to reject an update. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](sync-function.md)
* [Import filter](../../sync/import-processing.md)
* [Access Control](../../configuration/configuration-schema-access-control.md)
* [Add/Update Sync Function](../../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-sync)
* [Sync Function Overview](sync-function.md)

###### [](#-3)

Reference material …​

* [Public REST API](../../rest-api/rest-api.md)
* [Admin REST API](../../rest-api/rest-api-admin.md)
* [Metrics REST API](../../rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)