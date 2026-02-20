---
title: Manage Scopes and Collections
description: Scopes and collections allow you to organize your documents within a database.
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-js/edit/release/1.0/modules/ROOT/pages/scopes-collections-manage.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:couchbase-lite-javascript::scopes-collections-manage.adoc[]
---

[View original HTML](/couchbase-lite-javascript/current/scopes-collections-manage.html)

# Manage Scopes and Collections

> Scopes and collections allow you to organize your documents within a database. 

At a glance

**Use collections to organize your content in a database**

For example, if your database contains travel information, airport documents can be assigned to an airports collection, hotel documents can be assigned to a hotels collection, and so on.

* Document names must be unique within their collection.

**Use scopes to group multiple collections**

Collections can be assigned to different scopes according to content-type or deployment-phase (for example, test versus production).

* Collection names must be unique within their scope.

## [](#browser-specific-behavior)Browser-Specific Behavior

> [!IMPORTANT]
> Due to IndexedDB requirements, collections and their indexes must be declared when opening the database. Collections cannot be created or deleted while the database is open. This is different from native Couchbase Lite SDKs.

To modify collections, you must:

1. Close the database
2. Reopen it with the new collection configuration

## [](#default-scopes-and-collections)Default Scopes and Collections

Every database you create contains a default scope and a default collection named \_default.

If you create a document in the database and don’t specify a specific scope or collection, it is saved in the default collection, in the default scope.

The default scope and collection cannot be dropped.

## [](#scope-collection-naming)Scope and Collection Naming

In Couchbase Lite JavaScript, scopes and collections are specified using a combined notation:

| Format   | "scope.collection" or "collection" (implies \_default scope)                  |
| -------- | ----------------------------------------------------------------------------- |
| Examples | "inventory.airlines", "inventory.hotels", "tasks" (same as "\_default.tasks") |

**Naming conventions:**

* Must be between 1 and 251 characters in length
* Can only contain the characters `A-Z`, `a-z`, `0-9`, and the symbols `_`, `-`, and `%`
* Cannot start with `_` or `%` (except for the reserved `_default` scope and collection)
* Scope and collection names are case sensitive

## [](#declare-collections)Declare Collections

Collections must be declared in the `DatabaseConfig` when opening the database.

Example 1\. Declare collections at database open

```javascript
interface TravelAppSchema {
    'inventory.airline': Ariline;
    'inventory.hotel': Hotel;
}

const travelConfig: DatabaseConfig<TravelAppSchema> = {
    name: 'travel',
    version: 1,
    collections: {
        'inventory.airline': {
            indexes: ['name', 'icao']
        },
        'inventory.hotel': {
            indexes: ['country', 'city']
        }
    }
};

const travelDatabase = await Database.open(travelConfig);
```

| **1** | Database configuration                           |
| ----- | ------------------------------------------------ |
| **2** | Collections with custom scope using dot notation |
| **3** | Indexes for each collection                      |
| **4** | Open database with configuration                 |

## [](#access-collections)Access Collections

Once declared, you access collections through the `database.collection` object:

Example 2\. Access collections

```javascript
const tasks = database.collections.tasks;
const users = database.collections.users;
```

```javascript
const inventoryAirlines = travelDatabase.collections['inventory.airline'];
```

| **1** | Access collections in default scope using dot notation   |
| ----- | -------------------------------------------------------- |
| **2** | Access collection in custom scope using bracket notation |

> [!NOTE]
> When accessing collections with custom scopes, use bracket notation with the full `"scope.collection"` string: `database.collection['scope.collection']`

## [](#collection-configuration)Collection Configuration

Each collection can have its own configuration when declared:

Example 3\. Configure collections

```javascript
const database = await Database.open('secure-app', {
  password: 'encryption-password',
  collections: {
    // Collection with default configuration
    tasks: {},

    // Collection with indexes (indexed properties are not encrypted)
    users: {
      indexes: ['username', 'email', 'role']
    },

    // Collection in custom scope with configuration
    'private.documents': {
      indexes: ['type', 'category', 'createdAt']
    }
  }
});

// Access configured collections
const users = database.collection.users;
const privateDocuments = database.collection['private.documents'];
```

| **1** | Default configuration (all properties encrypted if database has password) |
| ----- | ------------------------------------------------------------------------- |
| **2** | Specify properties to leave unencrypted (can be indexed)                  |
| **3** | Custom scope collection with configuration                                |

## [](#add-collections)Add Collections

To add new collections, you must close and reopen the database with the updated configuration:

Example 4\. Add a collection

```javascript
database.close();

const updatedConfig: DatabaseConfig<MySchema> = {
    name: 'myapp',
    version: 2, // Increment version
    collections: {
        tasks: {},
        users: {},
        projects: {} // New collection
    }
};

const updatedDb = await Database.open(updatedConfig);
```

| **1** | Close the database                  |
| ----- | ----------------------------------- |
| **2** | Increment version number            |
| **3** | Add new collection to configuration |
| **4** | Reopen database with new collection |

> [!CAUTION]
> All existing collections must be included when reopening. Omitting a collection from the configuration will make it inaccessible (though its data remains in IndexedDB).

## [](#remove-collections)Remove Collections

To remove a collection, close the database and reopen without that collection in the configuration:

Example 5\. Remove a collection

```javascript
// Database with three collections
const database = await Database.open('myapp', {
  collections: {
    tasks: {},
    users: {},
    archived: {}
  }
});

// Close the database
database.close();

// Reopen without the 'archived' collection
const updatedDatabase = await Database.open('myapp', {
  collections: {
    tasks: {},
    users: {}
    // 'archived' collection omitted
  }
});

// The 'archived' collection is no longer accessible
console.log('Collection removed from configuration');
```

| **1** | Original collections including 'archived' |
| ----- | ----------------------------------------- |
| **2** | Reopen without 'archived'                 |
| **3** | Collection no longer accessible           |

> [!WARNING]
> Removing a collection from the configuration does not delete its data from IndexedDB. The data remains but is inaccessible. To permanently delete the collection’s data, you must delete the documents before removing the collection from the configuration.

## [](#purge-collection-data)Purge Collection Data

To permanently delete a collection’s data:

> [!IMPORTANT]
> Purging deletes all traces of a document, without leaving a "tombstone" revision behind. However, this means _purges are not visible to the replicator_, which has two side effects:

* A push replication will not push the deletion to a server.
* If the document is later updated on the server side, the next pull replication will download the new revision.

Example 6\. Purge collection data before removing

```javascript
const database = await Database.open('myapp', {
  collections: {
    tasks: {},
    archived: {}
  }
});

// Get all documents in the collection
const archived = database.collection.archived;
const query = database.createQuery('SELECT META().id FROM archived');
const results = await query.execute();

// Purge all documents
for (const row of results) {
  const docId = row.id;
  await archived.purge(docId);
}

console.log('All documents purged from archived collection');

// Now close and reopen without the collection
database.close();
const updatedDatabase = await Database.open('myapp', {
  collections: {
    tasks: {}
    // 'archived' removed after purging its data
  }
});
```

| **1** | Query all document IDs in the collection |
| ----- | ---------------------------------------- |
| **2** | Purge each document                      |
| **3** | Reopen without the collection            |

## [](#index-a-collection)Index a Collection

Indexes must be declared in the `DatabaseConfig` when opening the database, similar to collections:

Example 7\. Index a collection

```javascript
const config: DatabaseConfig = {
    name: 'myapp',
    version: 1,
    collections: {
        tasks: {
            indexes: ['title', 'completed', 'createdAt']
        }
    }
};

const db = await Database.open(config);
```

| **1** | Define indexes in collection configuration |
| ----- | ------------------------------------------ |
| **2** | Properties to index                        |

See [Indexing](indexing.md) for comprehensive information on creating and using indexes.

## [](#list-scopes-and-collections)List Scopes and Collections

You can retrieve a list of all scopes and their collections:

Example 8\. List scopes and collections

```javascript
const collectionNames = database.collectionNames;
for (const name of collectionNames) {
    console.log('Collection:', name);
}
```

| **1** | Get all collection names from database |
| ----- | -------------------------------------- |

## [](#get-collection)Get a Specific Collection

To get a collection by its full name:

Example 9\. Get a collection

```javascript
// Get collection from default scope
const tasks = database.collection.tasks;

// Get collection from custom scope
const inventoryAirlines = database.collection['inventory.airlines'];

// Check if collection exists
if (database.collection['archive.old']) {
  console.log('Collection exists');
} else {
  console.log('Collection not found');
}
```

## [](#collection-metadata)Collection Metadata

You can access metadata about a collection:

Example 10\. Collection metadata

```javascript
const tasks = database.collections.tasks;
const users = database.collections.users;
```

```javascript
const docCount = await tasks.count();
console.log('Document count:', docCount);
```

## [](#using-typescript-schemas)Using TypeScript Schemas

TypeScript users can define type-safe schemas for scopes and collections:

Example 11\. TypeScript schema for collections

```typescript
interface Task {
    type: 'task';
    title: string;
    completed: boolean;
    priority: number;
    createdAt: string;
}

// Note: Import as { Blob as CBLBlob } from @couchbase/lite-js
// to avoid conflict with the standard Blob type.
interface User {
    type: 'user';
    username: string;
    email: string;
    role: string;
    avatar: CBLBlob | null;
}

// Define database schema
interface AppSchema {
    tasks: Task;
    users: User;
}
```

## [](#troubleshooting)Troubleshooting

### [](#collection-not-accessible)Collection Not Accessible

**Problem:** Collection exists but cannot be accessed

**Solutions:**

* Verify collection was declared in `DatabaseConfig`
* Check for typos in collection name
* Use correct notation for custom scopes (`'scope.collection'`)
* Use bracket notation for custom scope collections

### [](#cannot-modify-collections)Cannot Modify Collections While Open

**Problem:** Need to add or remove collections

**Solutions:**

* Close the database first: `database.close()`
* Reopen with updated configuration
* Ensure all existing collections are included in the new configuration

### [](#data-not-syncing)Collection Data Not Syncing

**Problem:** Documents in collection not syncing with Sync Gateway

**Solutions:**

* Verify replication configuration includes the collection
* Check Sync Gateway channel access
* Ensure collection name matches Sync Gateway configuration
* Review replication filters

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Databases](database.md)
* [Documents](document.md)
* [Indexing](indexing.md)

.

###### [](#-2)

Learn more . . .

* [Queries](query-n1ql-mobile.md)

.

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.