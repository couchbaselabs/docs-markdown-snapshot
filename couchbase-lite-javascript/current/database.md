---
title: Databases
description: Working with Couchbase Lite Databases in JavaScript
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-js/edit/release/1.0/modules/ROOT/pages/database.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:couchbase-lite-javascript::database.adoc[]
---

[View original HTML](/couchbase-lite-javascript/current/database.html)

# Databases

> Description — _Working with Couchbase Lite Databases in JavaScript_  
> Related Content — [Encryption](encryption.md) | [Blobs](blob.md) | [Documents](document.md) | [Indexing](indexing.md)

## [](#database-concepts)Database Concepts

Databases created on Couchbase Lite can share the same hierarchical structure as Capella databases. This makes it easier to sync data between browser applications and applications built using Capella.

![Couchbase Lite Database Hierarchy](_images/diag-f3dc650478e74ec95af15693c682bc8e873c4537.svg) 

Figure 1\. Couchbase Lite Database Hierarchy

Although the terminology is different, the structure can be mapped to relational database terms:

__Table 1\. Relational Database → Couchbase__
| Relational database | Couchbase  |
| ------------------- | ---------- |
| Database            | Database   |
| Schema              | Scope      |
| Table               | Collection |

This structure gives you plenty of choices when it comes to partitioning your data. The most basic structure is to use the single default scope with a single default collection; or you could opt for a structure that allows you to split your collections into logical scopes.

![Couchbase Lite Examples](_images/diag-59b138f94b4dd22c39b0bd52d07669f762b80c5a.svg) 

Figure 2\. Couchbase Lite Examples

Storing local configuration

You may not need to sync all the data related for a particular application. You can set up a scope that syncs data, and a second scope that doesn’t.

One reason for doing this is to store local configuration data (such as user preferences or UI state). Since this information only relates to a particular browser or device, there is no need to sync it:

| local data scope   | Contains information pertaining to the browser or device.                                                                |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| syncing data scope | Contains information pertaining to the user, which can be synced back to the cloud for use on the web or another device. |

## [](#browser-storage)Browser Storage

Couchbase Lite JavaScript stores data in the browser’s IndexedDB, a robust client-side storage API.

IndexedDB Characteristics

* Stores data persistently across browser sessions
* Subject to browser storage quotas
* Data is scoped per origin (protocol + domain + port)
* Supports concurrent access from multiple browser tabs
* May be evicted under storage pressure on some browsers

## [](#open-db)Create or Open Database

You can create a new database and-or open an existing database, using the [Database](https://docs.couchbase.com/mobile/1.0.0/couchbase-lite-javascript/classes/Database.html) class. Pass in a database name and a [DatabaseConfig](https://docs.couchbase.com/mobile/1.0.0/couchbase-lite-javascript/interfaces/DatabaseConfig.html) — see [Example 1](#ex-dbopen).

Things to watch for include:

* If the named database does not exist, a new one is created
* The database is stored in the browser’s IndexedDB under the current origin

> [!IMPORTANT]
> Unlike native Couchbase Lite SDKs, collections and their indexes must be declared in the `DatabaseConfig` when opening the database. Collections cannot be created or deleted while the database is open.

Example 1\. Open or create a database

```javascript
const config: DatabaseConfig<AppSchema> = {
    name: 'myapp',
    version: 1,
    collections: {
        tasks: {},
        users: {}
    }
};
const database = await Database.open(config);
console.log('Database opened:', database.name);
```

| **1** | Database configuration with name and version |
| ----- | -------------------------------------------- |
| **2** | Collections configuration (required)         |
| **3** | Open the database                            |

## [](#database-configuration)Database Configuration

The [DatabaseConfig](https://docs.couchbase.com/mobile/1.0.0/couchbase-lite-javascript/interfaces/DatabaseConfig.html) interface provides options for configuring your database:

| Property    | Type              | Description                                                                                              |
| ----------- | ----------------- | -------------------------------------------------------------------------------------------------------- |
| collections | CollectionsConfig | Declares all collections and their configurations. Required.                                             |
| password    | string            | Encryption password for database encryption at rest. See [Database Encryption](encryption.md). Optional. |

Collections Configuration

Each collection can have its own configuration within the `collections` object:

| Property | Type       | Description                                                                                                                                                                                    |
| -------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| indexes  | string\[\] | Index properties for the collection. Indexed properties are not encrypted when database encryption is enabled. See [Indexing](indexing.md) and [Database Encryption](encryption.md). Optional. |

Example 2\. Configure database with encryption

```javascript
const encryptedConfig: DatabaseConfig = {
    name: 'secure-app', (1)
    version: 1,
    password: 'my-secure-password', (2)
    collections: {
        users: {
            indexes: ['username', 'email'] (3)
        }
    }
};

const secureDb = await Database.open(encryptedConfig);
```

| **1** | Database name and version               |
| ----- | --------------------------------------- |
| **2** | Encryption password                     |
| **3** | Unencrypted properties (can be indexed) |

## [](#close-database)Close Database

You are advised to incorporate the closing of all open databases into your application workflow.

To close a database, use [Database.close()](https://docs.couchbase.com/mobile/1.0.0/couchbase-lite-javascript/classes/Database.html#close) — see: [Example 3](#ex-dbclose). This also closes active replications, listeners and-or live queries connected to the database.

> [!NOTE]
> Closing a database soon after starting a replication involving it can cause an exception as the asynchronous replicator may not yet be connected.

> [!TIP]
> Safely Closing a Database
> 
> Before closing, check that any attached listeners (query/replication/change) indicate they are at least at `connected` status before closing — see for example: [Monitor Status](replication.md#lbl-repl-mon).

Example 3\. Close a Database

```javascript
database.close();
console.log('Database closed');
```

## [](#reopen-database)Reopen Database

After closing a database, you can reopen it using the same configuration. If the database was encrypted, you must provide the password when reopening the database — see [Database Encryption](encryption.md) for more information.

## [](#database-encryption)Database Encryption

Couchbase Lite JavaScript supports encrypting databases stored in IndexedDB to secure data at rest.

For complete information on database encryption, including how to enable encryption, manage encryption keys, and understand encryption limitations in browser environments, see [Database Encryption](encryption.md).

## [](#delete-database)Delete Database

To permanently delete a database and all its data from IndexedDB:

Example 4\. Delete a database

```javascript
// Close the database first
database.close();

// Delete the database
await Database.delete('myapp');

console.log('Database deleted');
```

> [!WARNING]
> Deleting a database is permanent and cannot be undone. All data, collections, and indexes are removed from IndexedDB.

## [](#multiple-databases)Multiple Databases

An application can open and use multiple databases simultaneously. Each database is stored separately in IndexedDB.

Example 5\. Using multiple databases

```javascript
// Open multiple databases
const userDb = await Database.open('users', {
  collections: { profiles: {} }
});

const contentDb = await Database.open('content', {
  collections: { articles: {}, comments: {} }
});

const localDb = await Database.open('local-config', {
  collections: { settings: {} }
});

// Use them independently
await userDb.collection.profiles.save({...});
await contentDb.collection.articles.save({...});

// Close when done
await userDb.close();
await contentDb.close();
await localDb.close();
```

## [](#storage-management)Storage Management

Databases in Couchbase Lite JavaScript are subject to browser storage quotas and policies.

> [!IMPORTANT]
> IndexedDB quotas, persistence, and eviction rules vary by browser, so the same app may store different amounts of data across environments. When writes exceed quota, a `QuotaExceededError` is thrown with no automatic retry or cleanup. The application must catch these errors, decide how to free space, or prompt the user. The SDK relies entirely on IndexedDB’s native behavior. See [Browsers and Storage](supported-browsers.md#browser-specific-considerations) for detailed information.

### [](#storage-quotas)Storage Quotas

Browsers enforce storage quotas that vary by platform:

* Desktop browsers: Typically 10% of available disk space
* Mobile browsers: Typically 50-100 MB
* Private browsing: Limited or no persistent storage

For detailed storage limits by browser, see [Browser-Specific Considerations](supported-browsers.md#browser-specific-considerations).

The SDK provides APIs to check available storage:

Example 6\. Check storage quota

```javascript
if (navigator.storage && navigator.storage.estimate) {
  const estimate = await navigator.storage.estimate();

  console.log('Quota:', estimate.quota);
  console.log('Usage:', estimate.usage);
  console.log('Available:', estimate.quota - estimate.usage);

  const percentUsed = (estimate.usage / estimate.quota) * 100;
  console.log(`Storage: ${percentUsed.toFixed(2)}% used`);
}
```

### [](#persistent-storage)Request Persistent Storage

To reduce the risk of storage eviction, request persistent storage:

Example 7\. Request persistent storage

```javascript
if (navigator.storage && navigator.storage.persist) {
  const isPersistent = await navigator.storage.persist();

  if (isPersistent) {
    console.log('Persistent storage granted');
  } else {
    console.log('Persistent storage not granted');
  }
}
```

## [](#database-maintenance)Database Maintenance

From time to time it may be necessary to perform maintenance on your database, such as compacting the database to remove unused documents and blobs.

Couchbase Lite’s API provides the [Database.performMaintenance()](https://docs.couchbase.com/mobile/1.0.0/couchbase-lite-javascript/classes/Database.html#performMaintenance) method. The available maintenance operations include `compact`, `reindex`, and `integrityCheck`.

This is a resource-intensive operation and is not performed automatically. It should be run on-demand using the API.

Example 8\. Compact a database

```javascript
// Compact the database to reclaim space
await database.performMaintenance('compact');

console.log('Database compacted');
```

## [](#inspect-database)Inspect Database

You can inspect the contents of your database using browser developer tools.

### [](#using-devtools)Using Browser DevTools

To view your database in IndexedDB:

1. Open browser DevTools (F12 or Cmd/Ctrl+Shift+I)
2. Go to the **Application** tab (Chrome) or **Storage** tab (Firefox)
3. Expand **IndexedDB** in the sidebar
4. Find your database by name
5. Explore collections and documents

Browser DevTools

* **Chrome DevTools**: Application > Storage > IndexedDB
* **Firefox DevTools**: Storage > IndexedDB
* **Safari DevTools**: Storage > IndexedDB (Enable Develop menu first)
* **Edge DevTools**: Application > Storage > IndexedDB

## [](#change-listeners)Change Listeners

IndexedDB allows concurrent reading from multiple tabs. Write operations are serialized per store/transaction, not per tab. IndexedDB does not have built-in cross-tab change notifications; these must be implemented by the SDK or the app.

The SDK provides two types of change listeners, depending on the granularity your application needs:

### [](#collection-change-listeners)Collection Change Listeners

* Trigger whenever any document in the collection changes
* Useful for keeping UI or state synchronized broadly

Example 9\. Collection Change Listener Example

```javascript
const collection = database.collection.tasks;

// Fires when any document in the collection changes
const token = collection.addChangeListener((changes) => {
  console.log("Changed docs:", changes.documentIDs);
  refreshUI();
});

// Remove listener when done
collection.removeChangeListener(token);
```

### [](#document-change-listeners)Document Change Listeners

* Trigger only when a specific document changes
* Useful when you want focused updates without scanning the whole collection

Example 10\. Document Change Listener Example

```javascript
const collection = database.collection.tasks;
const docId = "task_001";

// Fires only when the given document changes
const token = collection.addDocumentChangeListener(docId, (change) => {
  console.log("Document updated:", change.documentID);
  updateTaskView(docId);
});

// Remove listener when done
collection.removeDocumentChangeListener(token);
```

## [](#troubleshooting)Troubleshooting

You should use browser console logs as your first source of diagnostic information. If the information in the default logging level is insufficient, you can focus it on database errors and generate more verbose messages — see: [Example 11](#ex-logdb).

For more on using Couchbase logs — see: [Using Logs](logging.md).

Example 11\. Increase level of database log messages

```javascript
import { configure, getConsoleSink } from '@logtape/logtape';
import { LogCategory } from '@couchbase/lite-js';

// Configure logging for database operations
await configure({
  sinks: {
    console: getConsoleSink(),
  },
  loggers: [
    {
      category: [LogCategory, 'DB'],
      lowestLevel: 'debug',
      sinks: ['console'],
    }
  ],
});
```

### [](#common-issues)Common Issues

#### [](#quota-exceeded)QuotaExceededError

**Problem:** Database operations fail with `QuotaExceededError`

**Solutions:**

* Request persistent storage
* Reduce data size
* Compact the database
* Delete unnecessary documents

See [troubleshooting-storage.adoc](troubleshooting-storage.md) for more solutions.

#### [](#incorrect-password)EncryptionError

**Problem:** Database fails to open with encryption error

**Solutions:**

* Verify the encryption password is correct
* Check if database was encrypted in the first place
* Ensure password is consistently provided

#### [](#collections-not-accessible)Collections Not Accessible

**Problem:** Cannot access collections after opening database

**Solutions:**

* Verify collections were declared in `DatabaseConfig`
* Close and reopen database with correct configuration
* Check collection names for typos

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)

.

###### [](#-2)

Learn more . . .

* [Databases](#)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.