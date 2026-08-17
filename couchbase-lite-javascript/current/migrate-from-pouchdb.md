---
title: Migrating from PouchDB
description: Couchbase Lite JavaScript -- Migrating from PouchDB to Couchbase Lite
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-js/edit/release/1.0/modules/ROOT/pages/migrate-from-pouchdb.adoc
  xref: xref:couchbase-lite-javascript::migrate-from-pouchdb.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite-javascript/current/migrate-from-pouchdb.html)

# Migrating from PouchDB

> Description — _Couchbase Lite JavaScript — Migrating from PouchDB to Couchbase Lite_  
> Related Content — [Databases](database.md) | [Replication](replication.md)

## [](#overview)Overview

Couchbase Lite JavaScript provides an officially supported alternative to PouchDB for building offline-first web applications with Sync Gateway.

This guide helps developers migrate from PouchDB to Couchbase Lite JavaScript.

## [](#why-migrate)Why Migrate?

**Official Couchbase Support:**\* Full support from Couchbase \* Regular updates and security patches \* Enterprise-grade reliability

**Performance Improvements:**\* Optimized for modern browser APIs \* Better sync reliability with WebSocket protocol \* Improved IndexedDB performance

**Enhanced Features:**\* TypeScript support with full type definitions \* Advanced conflict resolution strategies \* Field-level encryption \* Better storage quota management \* Production-ready error handling

**Better Integration:**\* Seamless integration with Sync Gateway 3.0+ \* Compatible with Couchbase Server 7.0+ \* Modern authentication methods \* Improved monitoring and logging

## [](#api-comparison)API Comparison

### [](#core-operations)Core Operations

__Table 1\. Database and Document Operations__
| PouchDB API         | Couchbase Lite JS API                           | Notes                    |
| ------------------- | ----------------------------------------------- | ------------------------ |
| new PouchDB('mydb') | await Database.open(config)                     | Async operation          |
| db.info()           | database.name, database.path                    | Properties, not method   |
| db.put(doc)         | await collection.save(doc)                      | Collection-based         |
| db.get(id)          | await collection.document(id)                   | Returns document or null |
| db.remove(doc)      | await collection.deleteDocument(doc)            | Requires document object |
| db.bulkDocs(\[…​\]) | await collection.updateMultiple({save: \[…​\]}) | Batch operations         |
| db.allDocs()        | collection.documents()                          | Iterator pattern         |
| db.destroy()        | await Database.delete(name)                     | Static method            |

### [](#query-operations)Query Operations

__Table 2\. Querying Data__
| PouchDB API          | Couchbase Lite JS API     | Notes                   |
| -------------------- | ------------------------- | ----------------------- |
| db.find({selector})  | database.createQuery(sql) | SQL++ instead of Mango  |
| db.createIndex({…​}) | Declare in DatabaseConfig | At database open time   |
| db.query(mapFn)      | database.createQuery(sql) | No map/reduce functions |

### [](#replication)Replication

__Table 3\. Sync Operations__
| PouchDB API            | Couchbase Lite JS API     | Notes               |
| ---------------------- | ------------------------- | ------------------- |
| db.sync(url, opts)     | new Replicator(config)    | WebSocket-based     |
| db.replicate.to(url)   | replicatorType: 'push'    | In ReplicatorConfig |
| db.replicate.from(url) | replicatorType: 'pull'    | In ReplicatorConfig |
| sync.on('change', fn)  | replicator.onStatusChange | Property, not event |
| sync.cancel()          | await replicator.stop()   | Async operation     |

### [](#change-events)Change Events

__Table 4\. Listening to Changes__
| PouchDB API              | Couchbase Lite JS API                  | Notes              |
| ------------------------ | -------------------------------------- | ------------------ |
| db.changes({live: true}) | collection.addChangeListener(fn)       | Returns token      |
| changes.cancel()         | collection.removeChangeListener(token) | Use token from add |

## [](#migration-steps)Migration Steps

### [](#step-1-install)Step 1: Install Couchbase Lite

Install Package

```bash
# Remove PouchDB
npm uninstall pouchdb

# Install Couchbase Lite
npm install @couchbase/lite-js

# Install LogTape for logging (optional)
npm install @logtape/logtape
```

### [](#step-2-database-initialization)Step 2: Update Database Initialization

Example 1\. Before (PouchDB)

```javascript
import PouchDB from 'pouchdb';

const db = new PouchDB('myapp');
```

Example 2\. After (Couchbase Lite)

```javascript
import { Database } from '@couchbase/lite-js';

const config = {
  name: 'myapp',
  version: 1,
  collections: {
    _default: {} // Default collection
  }
};

const database = await Database.open(config);
const collection = database.collections._default;
```

### [](#step-3-document-operations)Step 3: Update Document Operations

Example 3\. Before (PouchDB)

```javascript
// Create document
await db.put({
  _id: 'doc1',
  type: 'task',
  title: 'Learn Couchbase',
  completed: false
});

// Read document
const doc = await db.get('doc1');

// Update document
doc.completed = true;
await db.put(doc);

// Delete document
await db.remove(doc);
```

Example 4\. After (Couchbase Lite)

```javascript
const collection = database.collections._default;

// Create document
await collection.save({
  _id: 'doc1',
  type: 'task',
  title: 'Learn Couchbase',
  completed: false
});

// Read document
const doc = await collection.document('doc1');

// Update document
doc.completed = true;
await collection.save(doc);

// Delete document
await collection.deleteDocument(doc);
```

### [](#step-4-queries)Step 4: Update Queries

Example 5\. Before (PouchDB - Mango Query)

```javascript
// Create index
await db.createIndex({
  index: {
    fields: ['type', 'completed']
  }
});

// Query documents
const result = await db.find({
  selector: {
    type: 'task',
    completed: false
  },
  sort: ['title']
});

result.docs.forEach(doc => {
  console.log(doc.title);
});
```

Example 6\. After (Couchbase Lite - SQL++)

```javascript
// Declare indexes in config (at database open)
const config = {
  name: 'myapp',
  version: 1,
  collections: {
    _default: {
      indexes: ['type', 'completed', 'title']
    }
  }
};

const database = await Database.open(config);

// Query documents with SQL++
const query = database.createQuery(`
  SELECT *
  FROM _default
  WHERE type = 'task' AND completed = false
  ORDER BY title
`);

await query.execute(row => {
  console.log(row._default.title);
});
```

### [](#step-5-replication)Step 5: Update Replication

Example 7\. Before (PouchDB)

```javascript
const sync = PouchDB.sync('myapp', 'http://localhost:4984/myapp', {
  live: true,
  retry: true
});

sync.on('change', info => {
  console.log('Change:', info);
});

sync.on('error', err => {
  console.error('Error:', err);
});
```

Example 8\. After (Couchbase Lite)

```javascript
import { Replicator } from '@couchbase/lite-js';

const replicator = new Replicator({
  database: database,
  url: 'wss://localhost:4984/myapp',
  collections: {
    _default: { pull: {}, push: {} }
  },
  credentials: {
    username: 'user',
    password: 'pass'
  },
  continuous: true
});

replicator.onStatusChange = (status) => {
  console.log('Status:', status.activity);
  if (status.error) {
    console.error('Error:', status.error);
  }
};

await replicator.start();
```

### [](#step-6-change-listeners)Step 6: Update Change Listeners

Example 9\. Before (PouchDB)

```javascript
const changes = db.changes({
  since: 'now',
  live: true,
  include_docs: true
});

changes.on('change', change => {
  console.log('Document changed:', change.id);
});

// Cancel later
changes.cancel();
```

Example 10\. After (Couchbase Lite)

```javascript
const collection = database.collections._default;

const token = collection.addChangeListener((changes) => {
  changes.documentIDs.forEach(id => {
    console.log('Document changed:', id);
  });
});

// Remove listener later
collection.removeChangeListener(token);
```

## [](#data-migration)Data Migration

### [](#export-from-pouchdb)Export from PouchDB

Example 11\. Export All Documents

```javascript
// Export all documents from PouchDB
const result = await pouchDB.allDocs({
  include_docs: true,
  attachments: true
});

const docs = result.rows.map(row => row.doc);

// Save to file or prepare for import
const dataExport = {
  docs: docs,
  timestamp: new Date().toISOString()
};

// Download as JSON
const blob = new Blob(
  [JSON.stringify(dataExport, null, 2)],
  { type: 'application/json' }
);
const url = URL.createObjectURL(blob);
const a = document.createElement('a');
a.href = url;
a.download = 'pouchdb-export.json';
a.click();
```

### [](#import-to-couchbase)Import to Couchbase Lite

Example 12\. Import Documents

```javascript
import { Database } from '@couchbase/lite-js';

// Open Couchbase Lite database
const database = await Database.open(config);
const collection = database.collections._default;

// Load exported data
const response = await fetch('pouchdb-export.json');
const dataExport = await response.json();

// Import documents in batches
const batchSize = 100;
for (let i = 0; i < dataExport.docs.length; i += batchSize) {
  const batch = dataExport.docs.slice(i, i + batchSize);

  const docsToSave = batch.map(doc => {
    // Remove PouchDB metadata if desired
    const { _rev, ...cleanDoc } = doc;
    return cleanDoc;
  });

  await collection.updateMultiple({
    save: docsToSave
  });

  console.log(`Imported ${Math.min(i + batchSize, dataExport.docs.length)} of ${dataExport.docs.length}`);
}

console.log('Migration complete!');
```

## [](#key-differences)Key Differences

### [](#architecture)Architecture

**PouchDB:**\* HTTP-based replication (\_changes feed, \_bulk\_docs) \* CouchDB replication protocol \* Map/reduce for queries

**Couchbase Lite:**\* WebSocket-based replication \* Couchbase Mobile protocol \* SQL++ for queries \* Collection-based data organization

### [](#configuration)Configuration

**PouchDB:**\* Runtime configuration \* Dynamic index creation \* Flexible schema

**Couchbase Lite:**\* Indexes declared at database open \* Structured configuration \* TypeScript schema support

### [](#authentication)Authentication

**PouchDB:**\* Basic auth in URL or headers \* Cookie-based sessions

**Couchbase Lite:**\* Two-step authentication (session + WebSocket) \* CORS configuration required \* See [CORS Configuration](cors-configuration.md)

### [](#conflict-resolution)Conflict Resolution

**PouchDB:**\* Automatic conflict resolution \* Winner by revision tree depth \* Limited custom resolution

**Couchbase Lite:**\* Automatic and custom strategies \* Flexible conflict resolvers \* See [Handling Data Conflicts](conflict.md)

## [](#common-pitfalls)Common Pitfalls

### [](#pitfall-1-sync-url)1\. Sync URL Protocol

**Issue:** Using HTTP URL instead of WebSocket

Incorrect

```javascript
url: 'http://localhost:4984/myapp' // Wrong protocol
```

Correct

```javascript
url: 'ws://localhost:4984/myapp'   // For development
url: 'wss://sync.example.com/myapp' // For production (TLS)
```

### [](#pitfall-2-index-timing)2\. Index Creation Timing

**Issue:** Trying to create indexes after database is open

Incorrect

```javascript
const database = await Database.open(config);
// Cannot create indexes here
```

Correct

```javascript
const config = {
  name: 'myapp',
  version: 1,
  collections: {
    _default: {
      indexes: ['field1', 'field2'] // Declare indexes here
    }
  }
};
const database = await Database.open(config);
```

### [](#pitfall-3-query-syntax)3\. Query Syntax

**Issue:** Using Mango query syntax

Incorrect

```javascript
// Mango queries don't work
db.find({ selector: { type: 'task' } })
```

Correct

```javascript
// Use SQL++
database.createQuery('SELECT * FROM _default WHERE type = "task"')
```

### [](#pitfall-4-change-listeners)4\. Change Listener Cleanup

**Issue:** Not removing change listeners

Incorrect

```javascript
// Listener never removed - memory leak
collection.addChangeListener(fn);
```

Correct

```javascript
// Store token and remove when done
const token = collection.addChangeListener(fn);
// Later...
collection.removeChangeListener(token);
```

## [](#related-content)Related Content

### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)

.

### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Queries](query-n1ql-mobile.md)
* [Replication](replication.md)

.

### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.