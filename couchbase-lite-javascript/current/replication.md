---
title: Data Sync using Sync Gateway
description: Couchbase Lite JavaScript -- Synchronizing data changes between
  local and remote databases using Sync Gateway
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-js/edit/release/1.0/modules/ROOT/pages/replication.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:couchbase-lite-javascript::replication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite-javascript/current/replication.html)

# Data Sync using Sync Gateway

> Description — _Couchbase Lite JavaScript — Synchronizing data changes between local and remote databases using Sync Gateway_  
> Related Content — [Handling Data Conflicts](conflict.md)

> [!NOTE]
> Code Snippets
> 
> All code examples are indicative only. They demonstrate the basic concepts and approaches to using a feature. Use them as inspiration and adapt these examples to best practice when developing applications for your platform.

## [](#introduction)Introduction

Couchbase Lite JavaScript provides API support for secure, bi-directional, synchronization of data changes between browser applications and a central server database. It does so by using a _replicator_ to interact with Sync Gateway.

The _replicator_ is designed to manage replication of documents and document changes between a source and a target database. For example, between a local Couchbase Lite database in the browser and a remote Sync Gateway database, which is ultimately mapped to a bucket in a Couchbase Server instance in the cloud or on a server.

This page shows sample code and configuration examples covering the implementation of a replication using Sync Gateway.

Your application runs a replicator (also referred to here as a client), which will initiate connection with a Sync Gateway (also referred to here as a server) and participate in the replication of database changes to bring both local and remote databases into sync.

> [!WARNING]
> Configuring CORS settings for Sync Gateway is a prerequisite for enabling data syncronization with the JavaScript SDK. See [CORS Configuration](cors-configuration.md) for more details.

## [](#replication-concepts)Replication Concepts

Couchbase Lite allows for one database for each application running in the browser. This database can contain one or more scopes. Each scope can contain one or more collections.

To learn about Scopes and Collections, see [Databases](database.md)

You can set up a replication scheme across these data levels:

Database

The `_default` collection is synced.

Collection

A specific collection or a set of collections is synced.

As part of the syncing setup, the Gateway has to map the Couchbase Lite database to the database being synced on Capella.

## [](#replication-protocol)Replication Protocol

### [](#scheme)Scheme

Couchbase Lite JavaScript uses a WebSocket-based replication protocol. The replication URL must specify WebSockets as the URL scheme using `ws://` (non-TLS) or `wss://` (SSL/TLS) prefixes.

> [!IMPORTANT]
> Always use `wss://` (WebSocket Secure) in production for encrypted communication with Sync Gateway.

Incompatibilities

Couchbase Lite’s replication protocol is **incompatible** with CouchDB-based databases and PouchDB’s replication protocol.

### [](#lbl-repl-ord)Ordering

To optimize for speed, the replication protocol doesn’t guarantee that documents will be received in a particular order. We don’t recommend relying on document order when using replication or database change listeners.

## [](#scopes-and-collections)Scopes and Collections

Scopes and Collections allow you to organize your documents in Couchbase Lite.

When syncing, you can configure the collections to be synced.

The collections specified in the Couchbase Lite replicator setup must exist (both scope and collection name must be identical) on the Sync Gateway side, otherwise starting the Couchbase Lite replicator will result in an error.

During replication:

1. If Sync Gateway config (or server) is updated to remove a collection that is being synced, the client replicator will be offline and will be stopped after the first retry. An error will be reported.
2. If Sync Gateway config is updated to add a collection to a scope that is being synchronized, the replication will ignore the collection. The added collection will not automatically sync until the Couchbase Lite replicator’s configuration is updated.

### [](#default-collection)Default Collection

When you set up the replicator with the database, the default collection will be set up to sync with the default collection on Sync Gateway.

### [](#user-defined-collections)User-Defined Collections

The user-defined collections specified in the Couchbase Lite replicator setup must exist (and be identical) on the Sync Gateway side to sync.

## [](#configuration-summary)Configuration Summary

You should configure and initialize a replicator for each Couchbase Lite database instance you want to sync. The following example shows the configuration and initialization process.

Example 1\. Replication configuration and initialization

```javascript
// Open database
    const database = await Database.open({
        name: 'myapp',
        version: 1,
        collections: {
            tasks: {},
            users: {}
        }
    });

    // Configure replicator
    const replicatorConfig: ReplicatorConfig = {
        database: database, (1)
        url: 'wss://sync-gateway.example.com:4984/myapp',
        collections: { (2)
            tasks: { pull: {}, push: {} },
            users: { pull: {}, push: {} }
        },
        credentials: { (3)
            username: 'user@example.com',
            password: 'password'
        }
    };

    // Create replicator
    const replicator = new Replicator(replicatorConfig); (4)

    // Add status change listener
    replicator.onStatusChange = (status) => { (5)
        console.log('Replication status:', status.status);
        if (status.error) {
            console.error('Replication error:', status.error);
        }
    };

    // Start replication
    await replicator.run(); (6)
```

**Notes on Example**

| **1** | Configure the replicator with database and target URL |
| ----- | ----------------------------------------------------- |
| **2** | Configure collections to replicate                    |
| **3** | Set up authentication credentials                     |
| **4** | Create the replicator instance                        |
| **5** | Add status change listener                            |
| **6** | Start the replicator                                  |

## [](#lbl-cfg-repl)Configure

### [](#lbl-cfg-tgt)Configure Target

Initialize and define the replication configuration with local and remote database locations using the `ReplicatorConfig` object.

The configuration provides:

* The local database to be synced
* The server’s URL (including the port number and the name of the remote database to sync with)
* The URL scheme for WebSocket URLs uses `ws:` (non-TLS) or `wss:` (SSL/TLS) prefixes

Example 2\. Add Target to Configuration

```javascript
const replicatorConfig: ReplicatorConfig = {
    database: database,
    url: 'wss://sync-gateway.example.com:4984/myapp', (1)
    collections: {
        tasks: { pull: {}, push: {} }
    }
};
```

| **1** | Use wss:// to ensure TLS encryption (strongly recommended in production) |
| ----- | ------------------------------------------------------------------------ |

### [](#lbl-cfg-sync)Sync Mode

Define the direction and type of replication you want to initiate.

Use the `ReplicatorConfig` object’s `replicatorType` and `continuous` parameters to specify:

* The type (or direction) of the replication:

  * `pushAndPull` \- Bi-directional replication (default)
  * `pull` \- Pull-only replication
  * `push` \- Push-only replication
* The replication mode:

  * **Continuous** \- remaining active indefinitely to replicate changed documents (`continuous: true`)
  * **Ad-hoc** \- a one-shot replication of changed documents (`continuous: false`)

Example 3\. Configure replicator type and mode

```javascript
// Configure bi-directional continuous replication
const bidirectionalConfig = {
    database: database,
    url: 'wss://sync-gateway.example.com:4984/myapp',
    collections: {
        tasks: {
            pull: {}, // Pull changes from server
            push: {}  // Push changes to server
        }
    }
};

// Configure pull-only replication
const pullOnlyConfig = {
    database: database,
    url: 'wss://sync-gateway.example.com:4984/myapp',
    collections: {
        tasks: {
            pull: {} // Only pull, no push
        }
    }
};

// Configure push-only replication
const pushOnlyConfig = {
    database: database,
    url: 'wss://sync-gateway.example.com:4984/myapp',
    collections: {
        tasks: {
            push: {} // Only push, no pull
        }
    }
};
```

> [!TIP]
> Unless there is a solid use-case not to, always initiate a single `pushAndPull` replication rather than separate `push` and `pull` replications.
> 
> This prevents the replications generating the same checkpoint resulting in conflicts.

### [](#lbl-authentication)Authentication

Sync Gateway or App Services users should be placed in the credentials section of the replication configuration.

To create a Basic Auth user in Sync Gateway, you use the Admin REST API. The Admin API allows you to create and manage users, roles, and access settings for a specific database.

To create a new user, send a POST request to `[{db}/_user/{username}](https://docs.couchbase.com/sync-gateway/current/rest-api/rest%5Fapi%5Fadmin.html#tag/Database-Security/operation/post%5Fdb-%5Fuser-)` with a minimal JSON body:

Example 4\. Example: Create User Request

```json
{
  "name": "alice",
  "password": "secret123"
}
```

This creates a user with Basic Authentication enabled, meaning you can authenticate against Sync Gateway using username and password in your Couchbase Lite for JavaScript replicator configuration.

Example 5\. Example: Using Credentials in Replicator

```javascript
const replicator = new Replicator({
  database: database,
  url: 'wss://sync-gateway.example.com:4984/myapp',
  collections: {
    tasks: { pull: {}, push: {} }
  },
  credentials: {
    username: 'alice',
    password: 'secret123'
  },
  continuous: true
});

await replicator.start();
```

### [](#lbl-repl-fltrs)Replication Filters

Replication Filters allow you to have control over the documents stored as the result of a push and/or pull replication.

#### [](#push-filter)Push Filter

The push filter allows an app to push a subset of a database to the server.

Example 6\. Push Filter

```javascript
const replicatorConfig: ReplicatorConfig = {
    database: database,
    url: 'wss://sync-gateway.example.com:4984/myapp',
    collections: {
        tasks: {
            push: {
                filter: (doc, flags) => { (1)
                // Only push documents that are not deleted
                    if (flags === DocumentFlags.deleted) {
                        return false;
                    }

                    // Only push tasks that are completed
                    return doc.completed === true;
                }
            }
        }
    }
};

const replicator = new Replicator(replicatorConfig);
```

| **1** | The callback should follow the semantics of a pure function. Long running functions would slow down the replicator considerably. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------- |

#### [](#pull-filter)Pull Filter

The pull filter gives an app the ability to validate documents being pulled, and skip ones that fail.

> [!NOTE]
> Pull replication filters are not a substitute for channels. Sync Gateway channels are designed to be scalable (documents are filtered on the server) whereas a pull replication filter is applied to a document once it has been downloaded.

Example 7\. Pull Filter

```javascript
const replicatorConfig: ReplicatorConfig = {
    database: database,
    url: 'wss://sync-gateway.example.com:4984/myapp',
    collections: {
        tasks: {
            pull: {
                filter: (doc, flags) => {
                // Skip deleted documents
                    if (flags === DocumentFlags.deleted) {
                        return false;
                    }

                    // Only pull tasks assigned to current user
                    return doc.assignedTo === 'currentUser@example.com';
                }
            }
        }
    }
};

const replicator = new Replicator(replicatorConfig);
```

## [](#lbl-init-repl)Initialize

### [](#lbl-repl-start)Start Replicator

Use the `Replicator` class constructor to initialize the replicator with the configuration you have defined. You can optionally add change listeners before starting the replicator using `start()`.

Example 8\. Initialize and run replicator

```javascript
// Create replicator
const replicator = new Replicator(replicatorConfig); (1)

// Start replication
await replicator.run(); (2)
console.log('Replication started');
```

| **1** | Create the replicator with the configuration |
| ----- | -------------------------------------------- |
| **2** | Start the replicator                         |

## [](#lbl-repl-mon)Monitor

You can monitor a replication’s status by using change listeners and the `replicator.status` property. This enables you to know when the replication is actively transferring data and when it has stopped.

### [](#lbl-repl-chng)Change Listeners

Use change listeners to monitor replication progress. You can add a replicator change listener at any point; it will report changes from the point it is registered.

> [!TIP]
> Best Practice
> 
> Remove listeners when they’re no longer needed to prevent memory leaks

Example 9\. Monitor replication

```javascript
// Monitor replication status
replicator.onStatusChange = (status) => {
    console.log('Replication status:', status.status);

    // Check progress
    if (status.pulledRevisions !== undefined) {
        console.log('Documents pulled:', status.pulledRevisions);
    }

    if (status.pushedRevisions !== undefined) {
        console.log('Documents pushed:', status.pushedRevisions);
    }

    // Handle errors
    if (status.error) {
        console.error('Replication error:', status.error);

        if (status.status === 'stopped') {
        // App logic here to determine if a restart is warranted
            console.log('Replicator stopped due to error');
        }
    }

    // Handle different states
    switch (status.status) {
        case 'connecting':
            console.log('Connecting to server...');
            break;
        case 'busy':
            console.log('Actively transferring data');
            break;
        case 'idle':
            console.log('Caught up with server');
            break;
        case 'stopped':
            console.log('Replication stopped');
            break;
    }
};
```

### [](#lbl-repl-status)Replicator Status

You can check the replicator status using the `status` property. The status indicates whether the replicator is actively transferring data or if it has stopped.

The returned status structure comprises:

* `activity` \- stopped, offline, connecting, idle or busy
* `progress`

  * `completed` \- the total number of changes completed
  * `total` \- the total number of changes to be processed
* `error` \- the current error, if any

#### [](#lbl-repl-states)Replication States

__Table 1\. Replicator activity levels__
| State      | Meaning                                                                                                                           |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------- |
| STOPPED    | The replication is finished or hit a fatal error.                                                                                 |
| OFFLINE    | The replicator is offline as the remote host is unreachable.                                                                      |
| CONNECTING | The replicator is connecting to the remote host.                                                                                  |
| IDLE       | The replication caught up with all the changes available from the server. The IDLE state is only used in continuous replications. |
| BUSY       | The replication is actively transferring data.                                                                                    |

### [](#lbl-repl-evnts)Monitor Document Changes

You can register listeners to monitor document replication.

Example 10\. Register a document listener

```javascript
// Monitor individual document replication
replicator.onDocuments = (collection, direction, documents) => {
    console.log(`${direction} - ${documents.length} documents in ${collection.name}`);

    for (const doc of documents) {
        if (doc.error) {
            console.error(`Error ${direction}ing ${doc.docID}:`, doc.error);
        } else if (doc.deleted) {
            console.log(`Document ${doc.docID} was deleted`);
        } else {
            console.log(`Document ${doc.docID} ${direction}ed successfully`);
        }
    }
};
```

#### [](#document-access-removal-behavior)Document Access Removal Behavior

When access to a document is removed on Sync Gateway, the document replication listener receives a notification and the document is purged from the local database.

### [](#lbl-repl-pend)Documents Pending Push

You can check whether documents are waiting to be pushed in any forthcoming sync.

Example 11\. Check pending documents

```javascript
// Note: The getPendingDocumentIDs and isDocumentPending methods are not yet implemented in this version.
```

## [](#lbl-repl-stop)Stop

Stopping a replication is straightforward using `stop()`. This initiates an asynchronous operation and so is not necessarily immediate.

Example 12\. Stop replicator

```javascript
// Stop the replicator
replicator.stop();
console.log('Replication stopped');
```

## [](#lbl-nwk-errs)Error Handling

When the replicator detects a network error it updates its status depending on the error type (permanent or temporary) and returns an appropriate error code.

Example 13\. Monitoring for network errors

```javascript
// Monitor for network errors
replicator.onStatusChange = (status) => {
    if (status.error) {
        const error = status.error as ReplicatorError;

        console.error('Replication error:', error.message);
        switch (error.code) {
            case 401:
                console.error('Unauthorized - check credentials');
                break;
            case 404:
                console.error('Database not found on server');
                break;
            case 500:
            case 502:
            case 503:
            case 504:
                console.log('Server error');
                break;
            case 1001:
                console.log('Web Socket hung up');
                break;
            default:
                console.error('Unexpected error code:', error.code);
        }
    }
};
```

**For permanent network errors** (for example, `404` not found, or `401` unauthorized): The replicator will stop permanently. It sets its status to `STOPPED`.

**For recoverable or temporary errors:** The replicator sets its status to `OFFLINE`, then:

* If `continuous=true` it retries the connection indefinitely
* If `continuous=false` (one-shot) it retries the connection a limited number of times

## [](#related-content)Related Content

### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)

.

### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](#)
* [Handling Data Conflicts](conflict.md)

.

### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.