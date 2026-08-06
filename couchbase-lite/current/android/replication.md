---
title: Data Sync using Sync Gateway
description: Couchbase Lite for Android -- Synchronizing data changes between
  local and remote databases using Sync Gateway
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.1/modules/android/pages/replication.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:couchbase-lite:android:replication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/android/replication.html)

# Data Sync using Sync Gateway

> Description — _Couchbase Lite for Android — Synchronizing data changes between local and remote databases using Sync Gateway_  
> Related Content — [Handling Data Conflicts](conflict.md) | [Intra-Device](dbreplica.md) | [Peer-to-Peer](#p2psync-websocket.adoc)

> [!CAUTION]
> Android enablers
> 
> Allow Unencrypted Network Traffic
> 
> To use cleartext, un-encrypted, network traffic (`http://` and-or `ws://`), include `android:usesCleartextTraffic="true"` in the `application` element of the manifest as shown on [android.com](https://developer.android.com/training/articles/security-config#CleartextTrafficPermitted).  
> **This not recommended in production**.
> 
> Use Background Threads
> 
> As with any network or file I/O activity, CouchbaseLite activities should not be performed on the UI thread. **Always** use a **background** thread.

> [!NOTE]
> Code Snippets
> 
> All code examples are indicative only. They demonstrate the basic concepts and approaches to using a feature. Use them as inspiration and adapt these examples to best practice when developing applications for your platform.

## [](#introduction)Introduction

Couchbase Lite for Android provides API support for secure, bi-directional, synchronization of data changes between mobile applications and a central server database. It does so by using a _replicator_ to interact with Sync Gateway.

The _replicator_ is designed to manage replication of documents and-or document changes between a source and a target database. For example, between a local Couchbase Lite database and remote Sync Gateway database, which is ultimately mapped to a bucket in a Couchbase Server instance in the cloud or on a server.

This page shows sample code and configuration examples covering the implementation of a replication using Sync Gateway.

Your application runs a replicator (also referred to here as a client), which will initiate connection with a Sync Gateway (also referred to here as a server) and participate in the replication of database changes to bring both local and remote databases into sync.

Subsequent sections provide additional details and examples for the main configuration options.

## [](#replication-concepts)Replication Concepts

Couchbase Lite allows for one database for each application running on the mobile device. This database can contain one or more scopes. Each scope can contain one or more collections.

To learn about Scopes and Collections, see [Databases](database.md)

You can set up a replication scheme across these data levels:

Database

The `_default` collection is synced.

Collection

A specific collection or a set of collections is synced.

As part of the syncing setup, the Gateway has to map the Couchbase Lite database to the database being synced on Capella.

## [](#replication-protocol)Replication Protocol

### [](#scheme)Scheme

Couchbase Mobile uses a replication protocol based on WebSockets for replication. To use this protocol the replication URL should specify WebSockets as the URL scheme (see the [Configure Target](#lbl-cfg-tgt) section below).

Incompatibilities

Couchbase Lite's replication protocol is **incompatible** with CouchDB-based databases. And since Couchbase Lite 2.x+ only supports the new protocol, you will need to run a version of Sync Gateway that supports it — see: [Compatibility](compatibility.md).

Legacy Compatibility

Clients using Couchbase Lite 1.x can continue to use `http` as the URL scheme. Sync Gateway 2.x+ will automatically use:

* The 1.x replication protocol when a Couchbase Lite 1.x client connects through `http://localhost:4984/db`
* The 2.0 replication protocol when a Couchbase Lite 2.0 client connects through `ws://localhost:4984/db`.

You can find further information in our blog: [Introducing the Data Replication Protocol](https://blog.couchbase.com/data-replication-couchbase-mobile/).

### [](#lbl-repl-ord)Ordering

To optimize for speed, the replication protocol doesn't guarantee that documents will be received in a particular order. So we don't recommend to rely on that when using the replication or database change listeners for example.

Couchbase Lite \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] spins up multiple executors. Unless mitigated, for example by using a custom executor, this policy can result in too many threads being spun up.

> [!NOTE]
> If no listeners are registered to listen to a replicator at the time of the most recent `start(. . .)`, then no subsequently registered listeners will receive notifications.

An executor manages a pool of threads and, perhaps, a queue in front of the executor, to handle the asynchronous callbacks. Couchbase Lite API calls processed by an executor include:

* Query.addChangeListener
* MessageEndpointListerner.addChangeListener
* LiveQuery.addChangeListener
* AbstractReplicator.addDocumentReplicationListener
* AbstractReplicator.addChangeListener
* Database.addChangeListener
* Database.addDocumentChangeListener
* Database.addDatabaseChangeListener
* Database.addChangeListener

Couchbase Lite \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] sometimes uses its own internal executor to run asynchronous client code. While this is fine for small tasks, larger tasks — those that take significant compute time, or that perform I/O — can block Couchbase processing. If this happens your application will fail with a `RejectedExecutionException` and it may be necessary to create a separate executor on which to run the large tasks.

The following examples show how to specify a separate executor in the client code. The client code executor can enforce an application policy for delivery ordering and the number of threads.

**Guaranteed Order Delivery**

```java
/**
 * This version guarantees in order delivery and is parsimonious with space
 * The listener does not need to be thread safe (at least as far as this code is concerned).
 * It will run on only thread (the Executor's thread) and must return from a given call
 * before the next call commences.  Events may be delivered arbitrarily late, though,
 * depending on how long it takes the listener to run.
 */
public class InOrderExample {
    private static final ExecutorService IN_ORDER_EXEC = Executors.newSingleThreadExecutor();

    public Replicator runReplicator(Database db1, Database db2, ReplicatorChangeListener listener)
        throws CouchbaseLiteException {
        CollectionConfiguration collectionConfig = new CollectionConfiguration(db1.getDefaultCollection());
        ReplicatorConfiguration config = new ReplicatorConfiguration(
            Set.of(collectionConfig),
            new DatabaseEndpoint(db2)
        );
        config.setType(ReplicatorType.PUSH_AND_PULL);
        config.setContinuous(false);

        Replicator repl = new Replicator(config);
        ListenerToken token = repl.addChangeListener(IN_ORDER_EXEC, listener::changed);

        repl.start();

        return repl;
    }
}
```

**Maximum Throughput**

```java
/**
 * This version maximizes throughput.  It will deliver change notifications as quickly
 * as CPU availability allows. It may deliver change notifications out of order.
 * Listeners must be thread safe because they may be called from multiple threads.
 * In fact, they must be re-entrant because a given listener may be running on mutiple threads
 * simultaneously.  In addition, when notifications swamp the processors, notifications awaiting
 * a processor will be queued as Threads, (instead of as Runnables) with accompanying memory
 * and GC impact.
 */
public class MaxThroughputExample {
    private static final ExecutorService MAX_THROUGHPUT_EXEC = Executors.newCachedThreadPool();

    public Replicator runReplicator(Database db1, Database db2, ReplicatorChangeListener listener)
        throws CouchbaseLiteException {
        CollectionConfiguration collectionConfig = new CollectionConfiguration(db1.getDefaultCollection());
        ReplicatorConfiguration config = new ReplicatorConfiguration(
            Set.of(collectionConfig),
            new DatabaseEndpoint(db2)
        );
        config.setType(ReplicatorType.PUSH_AND_PULL);
        config.setContinuous(false);

        Replicator repl = new Replicator(config);
        ListenerToken token = repl.addChangeListener(MAX_THROUGHPUT_EXEC, listener::changed);

        repl.start();

        return repl;
    }
}
```

**Extreme Configurability**

```java
/**
 * This version demonstrates the extreme configurability of the CouchBase Lite replicator callback system.
 * It may deliver updates out of order and does require thread-safe and re-entrant listeners
 * (though it does correctly synchronizes tasks passed to it using a SynchronousQueue).
 * The thread pool executor shown here is configured for the sweet spot for number of threads per CPU.
 * In a real system, this single executor might be used by the entire application and be passed to
 * this module, thus establishing a reasonable app-wide threading policy.
 * In an emergency (Rejected Execution) it lazily creates a backup executor with an unbounded queue
 * in front of it.  It, thus, may deliver notifications late, as well as out of order.
 */
public class PolicyExample {
    private static final int CPUS = Runtime.getRuntime().availableProcessors();

    private static ThreadPoolExecutor BACKUP_EXEC;

    private static final RejectedExecutionHandler BACKUP_EXECUTION
        = new RejectedExecutionHandler() {
        public void rejectedExecution(Runnable r, ThreadPoolExecutor e) {
            synchronized (this) {
                if (BACKUP_EXEC == null) { BACKUP_EXEC = createBackupExecutor(); }
            }
            BACKUP_EXEC.execute(r);
        }
    };

    private static ThreadPoolExecutor createBackupExecutor() {
        ThreadPoolExecutor exec
            = new ThreadPoolExecutor(CPUS + 1, 2 * CPUS + 1, 30, TimeUnit.SECONDS, new LinkedBlockingQueue<Runnable>());
        exec.allowCoreThreadTimeOut(true);
        return exec;
    }

    private static final ThreadPoolExecutor STANDARD_EXEC
        = new ThreadPoolExecutor(CPUS + 1, 2 * CPUS + 1, 30, TimeUnit.SECONDS, new SynchronousQueue<Runnable>());

    static { STANDARD_EXEC.setRejectedExecutionHandler(BACKUP_EXECUTION); }

    public Replicator runReplicator(Database db1, Database db2, ReplicatorChangeListener listener)
        throws CouchbaseLiteException {
        CollectionConfiguration collectionConfig = new CollectionConfiguration(db1.getDefaultCollection());
        ReplicatorConfiguration config = new ReplicatorConfiguration(
            Set.of(collectionConfig),
            new DatabaseEndpoint(db2)
        );
        config.setType(ReplicatorType.PUSH_AND_PULL);
        config.setContinuous(false);

        Replicator repl = new Replicator(config);
        ListenerToken token = repl.addChangeListener(STANDARD_EXEC, listener::changed);

        repl.start();

        return repl;
    }
}
```

## [](#scopes-and-collections)Scopes and Collections

Scopes and Collections allow you to organize your documents in Couchbase Lite.

When syncing, you can configure the collections to be synced.

The collections specified in the Couchbase Lite replicator setup must exist (both scope and collection name must be identical) on the Sync Gateway side, otherwise starting the Couchbase Lite replicator will result in an error.

During replication:

1. If Sync Gateway config (or server) is updated to remove a collection that is being synced, the client replicator will be offline and will be stopped after the first retry. An error will be reported.
2. If Sync Gateway config is updated to add a collection to a scope that is being synchronized, the replication will ignore the collection. The added collection will not automatically sync until the Couchbase Lite replicator's configuration is updated.

### [](#default-collection)Default Collection

When upgrading Couchbase Lite to 3.1, the existing documents in the database will be automatically migrated to the default collection.

For backward compatibility with the code prior to 3.1, when you set up the replicator with the database, the default collection will be set up to sync with the default collection on Sync Gateway.

Sync Couchbase Lite database with the default collection on Sync Gateway

![Sync Couchbase Lite database with the default collection on Sync Gateway](../_images/cbl-replication-scopes-collections-1.png)

Sync Couchbase Lite default collection with default collection on Sync Gateway

![Sync Couchbase Lite default collection with default collection on Sync Gateway](../_images/cbl-replication-scopes-collections-2.png)

### [](#user-defined-collections)User-Defined Collections

The user-defined collections specified in the Couchbase Lite replicator setup must exist (and be identical) on the Sync Gateway side to sync.

Syncing scope with user-defined collections.

![Syncing scope with user-defined collections.](../_images/cbl-replication-scopes-collections-3.png)

Syncing scope with user-defined collections. Couchbase Lite has more collections than the Sync Gateway configuration (with collection filters)

![Syncing scope with user-defined collections. Couchbase Lite has more collections than the Sync Gateway configuration (with collection filters)](../_images/cbl-replication-scopes-collections-4.png)

## [](#configuration-summary)Configuration Summary

You should configure and initialize a replicator for each Couchbase Lite database instance you want to sync. [Example 1](#ex-simple-repl) shows the configuration and initialization process.

> [!NOTE]
> You need Couchbase Lite 3.1+ and Sync Gateway 3.1+ to use `custom` Scopes and Collections.  
> If you're using Capella App Services or Sync Gateway releases that are older than version 3.1, you won't be able to access `custom` Scopes and Collections. To use Couchbase Lite 3.1+ with these older versions, you can use the `default` Collection as a backup option.

Click the **GitHub** tab in the code examples for further details.

Example 1\. Replication configuration and initialization

* Kotlin
* Java

```Kotlin
val repl = Replicator( (1)

    // initialize the replicator configuration
    ReplicatorConfigurationFactory.newConfig(
        collections = CollectionConfiguration.fromCollections(collections),

        target = URLEndpoint(URI("wss://listener.com:8954")), (2)

        // Set replicator type
        type = ReplicatorType.PUSH_AND_PULL,

        // Configure Sync Mode
        continuous = false, // default value


        // set auto-purge behavior
        // (here we override default)
        enableAutoPurge = false, (3)


        // Configure Server Authentication --
        // only accept self-signed certs
        acceptOnlySelfSignedServerCertificate = true, (4)


        // Configure the credentials the
        // client will provide if prompted
        authenticator = BasicAuthenticator("PRIVUSER", "let me in".toCharArray())  (5)

    )
)

// Optionally add a change listener (6)
val token = repl.addChangeListener { change ->
    val err: CouchbaseLiteException? = change.status.error
    if (err != null) {
        log("Error code ::  ${err.code}", err)
    }
}

// Start replicator
repl.start(false) (7)

thisReplicator = repl
thisToken = token
```

```Java
Replicator repl = new Replicator( (1)

    
    // initialize the replicator configuration
    new ReplicatorConfiguration(
        CollectionConfiguration.fromCollections(collections), 
        new URLEndpoint(new URI("wss://listener.com:8954"))
    ) (2)

        // Set replicator type
        .setType(ReplicatorType.PUSH_AND_PULL)

        // Configure Sync Mode
        .setContinuous(false) // default value


        // set auto-purge behavior
        // (here we override default)
        .setAutoPurgeEnabled(false) (3)


        // Configure Server Authentication --
        // only accept self-signed certs
        .setAcceptOnlySelfSignedServerCertificate(true) (4)

        // Configure the credentials the
        // client will provide if prompted
        .setAuthenticator(new BasicAuthenticator("Our Username", "Our Password".toCharArray())) (5)

);

// Optionally add a change listener (6)
ListenerToken token = repl.addChangeListener(change -> {
    CouchbaseLiteException err = change.getStatus().getError();
    if (err != null) { Logger.log("Error code :: " + err.getCode(), err); }
});

// Start replicator
repl.start(false); (7)

thisReplicator = repl;
thisToken = token;
```

> [!NOTE]
> As with any network or file I/O activity, CouchbaseLite activities should not be performed on the UI thread. **Always** use a **background** thread.

**Notes on Example**

| **1** | get endpoint for target DB                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Use the [ReplicatorConfiguration](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html) class's constructor — [ReplicatorConfiguration( collectionConfigs, endpoint)](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html#ReplicatorConfiguration-com.couchbase.lite.Database-com.couchbase.lite.Endpoint-) — to initialize the replicator configuration with the local database — see also: [Configure Target](#lbl-cfg-tgt) |
| **3** | The default is to auto-purge documents that this user no longer has access to — see: [Auto-purge on Channel Access Revocation](#anchor-auto-purge-on-revoke). Here we over-ride this behavior by setting its flag false.                                                                                                                                                                                                                                                                                                                           |
| **4** | Configure how the client will authenticate the server. Here we say connect only to servers presenting a self-signed certificate. By default, clients accept only servers presenting certificates that can be verified using the OS bundled Root CA Certificates — see: [Server Authentication](#lbl-svr-auth).                                                                                                                                                                                                                                     |
| **5** | Configure the client-authentication credentials (if required). These are the credential the client will present to sync gateway if requested to do so.Here we configure to provide _Basic Authentication_ credentials. Other options are available — see: [Client Authentication](#lbl-client-auth).                                                                                                                                                                                                                                               |
| **6** | Optionally, register an observer, which will notify you of changes to the replication status — see: [Monitor](#lbl-repl-mon)                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **7** | Start the replicator — see: [Start Replicator](#lbl-repl-start).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## [](#lbl-cfg-repl)Configure

In this section

[Configure Target](#lbl-cfg-tgt)| [Sync Mode](#lbl-cfg-sync)| [Retry Configuration](#lbl-cfg-keep-alive)| [User Authorization](#lbl-user-auth)| [Server Authentication](#lbl-svr-auth)| [Client Authentication](#lbl-client-auth)| [Monitor Document Changes](#lbl-repl-evnts)| [Custom Headers](#lbl-repl-hdrs)| [Checkpoint Starts](#lbl-repl-ckpt)| [Replication Filters](#lbl-repl-fltrs)| [Channels](#lbl-repl-chan)| [Auto-purge on Channel Access Revocation](#anchor-auto-purge-on-revoke)| [Delta Sync](#lbl-repl-delta)

### [](#lbl-cfg-tgt)Configure Target

Use the Initialize and define the replication configuration with local and remote database locations using the [ReplicatorConfiguration](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html) object.

The constructor provides:

* the name of the local database to be sync'd
* the server's URL (including the port number and the name of the remote database to sync with)  
It is expected that the app will identify the IP address and URL and append the remote database name to the URL endpoint, producing for example: `wss://10.0.2.2:4984/travel-sample`  
The URL scheme for web socket URLs uses `ws:` (non-TLS) or `wss:` (SSL/TLS) prefixes. To use cleartext, un-encrypted, network traffic (`http://` and-or `ws://`), include `android:usesCleartextTraffic="true"` in the `application` element of the manifest as shown on [android.com](https://developer.android.com/training/articles/security-config#CleartextTrafficPermitted).  
**This not recommended in production**.

Example 2\. Add Target to Configuration

* Kotlin
* Java

```Kotlin
// initialize the replicator configuration
val thisConfig = ReplicatorConfigurationFactory.newConfig(
    collections = CollectionConfiguration.fromCollections(collections),
    target = URLEndpoint(URI("wss://10.0.2.2:8954/travel-sample")) (1)
)
```

```Java
// initialize the replicator configuration
ReplicatorConfiguration thisConfig = new ReplicatorConfiguration(
        CollectionConfiguration.fromCollections(collections),
        new URLEndpoint(new URI("wss://10.0.2.2:8954/travel-sample"))
); (1)
```

| **1** | Note use of the scheme prefix (wss://to ensure TLS encryption — strongly recommended in production — or ws://) |
| ----- | -------------------------------------------------------------------------------------------------------------- |

### [](#lbl-cfg-sync)Sync Mode

Here we define the direction and type of replication we want to initiate.

We use `[ReplicatorConfiguration](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html)` class's [replicatorType](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html#setReplicatorType-com.couchbase.lite.AbstractReplicatorConfiguration.ReplicatorType-) and `[continuous](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html#setContinuous-boolean-)` parameters, to tell the replicator:

* The type (or direction) of the replication: `**PUSH_AND_PULL**`; `PULL`; `PUSH`
* The replication mode, that is either of:

  * Continuous — remaining active indefinitely to replicate changed documents (`continuous=true`).
  * Ad-hoc — a one-shot replication of changed documents (`continuous=false`).

Example 3\. Configure replicator type and mode

* Kotlin
* Java

```Kotlin
// Set replicator type
type = ReplicatorType.PUSH_AND_PULL,

// Configure Sync Mode
continuous = false, // default value
```

```Java
// Set replicator type
.setType(ReplicatorType.PUSH_AND_PULL)

// Configure Sync Mode
.setContinuous(false) // default value
```

> [!TIP]
> Unless there is a solid use-case not to, always initiate a single `PUSH_AND_PULL` replication rather than identical separate `PUSH` and `PULL` replications.
> 
> This prevents the replications generating the same checkpoint `docID` resulting in multiple conflicts.

### [](#lbl-cfg-keep-alive)Retry Configuration

Couchbase Lite for Android's replication retry logic assures a resilient connection.

The replicator minimizes the chance and impact of dropped connections by maintaining a heartbeat; essentially pinging the Sync Gateway at a configurable interval to ensure the connection remains alive.

In the event it detects a transient error, the replicator will attempt to reconnect, stopping only when the connection is re-established, or the number of retries exceeds the retry limit (9 times for a single-shot replication and unlimited for a continuous replication).

On each retry the interval between attempts is increased exponentially (exponential backoff) up to the maximum wait time limit (5 minutes).

The REST API provides configurable control over this replication retry logic using a set of configiurable properties — see: [Table 1](#tbl-repl-retry).

__Table 1\. Replication Retry Configuration Properties__
| Property                                                                                                                                                                      | Use cases                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [setHeartbeat()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicatorConfiguration.html#setHeartbeat-long-)                   | Reduce to detect connection errors sooner Align to load-balancer or proxy keep-alive interval — see Sync Gateway's topic [Load Balancer - Keep Alive](../../../sync-gateway/current/deploy/load-balancer.md#websocket-connection) | The interval (in seconds) between the heartbeat pulses. Default: The replicator pings the Sync Gateway every 300 seconds.                                                                                                                                                                                                                                                                                                                                                                         |
| [setMaxAttempts()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicatorConfiguration.html#setMaxAttempts-int-)                | Change this to limit or extend the number of retry attempts.                                                                                                                                                                      | The maximum number of retry attempts Set to zero (0) to use default values Set to zero (1) to prevent any retry attempt The retry attempt count is reset when the replicator is able to connect and replicate Default values are: Single-shot replication = 9; Continuous replication = maximum integer value Negative values generate a Couchbase exception InvalidArgumentException                                                                                                             |
| [setMaxAttemptWaitTime()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicatorConfiguration.html#setMaxAttemptWaitTime-long-) | Change this to adjust the interval between retries.                                                                                                                                                                               | The maximum interval between retry attempts While you can configure the **maximum permitted** wait time, the replicator's exponential backoff algorithm calculates each individual interval which is not configurable. Default value: 300 seconds (5 minutes) Zero sets the maximum interval between retries to the default of 300 seconds 300 sets the maximum interval between retries to the default of 300 seconds A negative value generates a Couchbase exception, InvalidArgumentException |

When necessary you can adjust any or all of those configurable values — see: [Example 4](#ex-repl-retry) for how to do this.

Example 4\. Configuring Replication Retries

* Kotlin
* Java

```Kotlin
val repl = Replicator(
    ReplicatorConfigurationFactory.newConfig(
        collections = CollectionConfiguration.fromCollections(collections),
        target = URLEndpoint(URI("ws://localhost:4984/mydatabase")),
        //  other config params as required . .
        heartbeat = 150, (1)
        maxAttempts = 20,
        maxAttemptWaitTime = 600
    )
)
repl.start()
thisReplicator = repl
```

```Java
Replicator repl = new Replicator(
        new ReplicatorConfiguration(
                CollectionConfiguration.fromCollections(collections),
                new URLEndpoint(new URI("ws://localhost:4984/mydatabase")))
                //  other config as required . . .
                .setHeartbeat(150) (1)
                .setMaxAttempts(20) (2)
                .setMaxAttemptWaitTime(600)); (3)

repl.start();
thisReplicator = repl;
```

| **1** | Here we use [setHeartbeat()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicatorConfiguration.html#setHeartbeat-long-) to set the required interval (in seconds) between the heartbeat pulses |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Here we use [setMaxAttempts()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicatorConfiguration.html#setMaxAttempts-int-) to set the required number of retry attempts                        |
| **3** | Here we use [setMaxAttemptWaitTime()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicatorConfiguration.html#setMaxAttemptWaitTime-long-) to set the required interval between retry attempts. |

### [](#lbl-user-auth)User Authorization

By default, Sync Gateway does not enable user authorization. This makes it easier to get up and running with synchronization.

You can enable authorization in the sync gateway configuration file, as shown in [Example 5](#example-enable-authorization).

Example 5\. Enable Authorization

```json
{
  "databases": {
    "mydatabase": {
      "users": {
        "GUEST": {"disabled": true}
      }
    }
  }
}
```

To authorize with Sync Gateway, an associated user must first be created. Sync Gateway users can be created through the [POST /{tkn-db}/\_user](../../../sync-gateway/current/rest-api/rest-api-admin.md#/user/post%5F%5Fdb%5F%5F%5Fuser%5F)endpoint on the Admin REST API.

### [](#lbl-svr-auth)Server Authentication

Define the credentials your app (the client) is expecting to receive from the Sync Gateway (the server) in order to ensure it is prepared to continue with the sync.

Note that the client cannot authenticate the server if TLS is turned off. When TLS is enabled (Sync Gateway's default) the client _must_ authenticate the server. If the server cannot provide acceptable credentials then the connection will fail.

Use `[ReplicatorConfiguration](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html)` properties [setAcceptOnlySelfSignedServerCertificate](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html#setAcceptOnlySelfSignedServerCertificate-boolean-) and [setPinnedServerCertificate](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html#setPinnedServerCertificate-byte:A-), to tell the replicator how to verify server-supplied TLS server certificates.

* If there is a pinned certificate, nothing else matters, the server cert must **exactly** match the pinned certificate.
* If there are no pinned certs and [setAcceptOnlySelfSignedServerCertificate](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html#setAcceptOnlySelfSignedServerCertificate-boolean-) is `true` then any self-signed certificate is accepted. Certificates that are not self signed are rejected, no matter who signed them.
* If there are no pinned certificates and [setAcceptOnlySelfSignedServerCertificate](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html#setAcceptOnlySelfSignedServerCertificate-boolean-) is `false` (default), the client validates the server's certificates against the system CA certificates. The server must supply a chain of certificates whose root is signed by one of the certificates in the system CA bundle.

Example 6\. Set Server TLS security

* Kotlin
* Java

* CA Cert
* Self Signed Cert
* Pinned Certificate

Set the client to expect and accept only CA attested certificates.

```Kotlin
// Configure Server Security
// -- only accept CA attested certs
acceptOnlySelfSignedServerCertificate = false, (1)
```

| **1** | This is the default. Only certificate chains with roots signed by a trusted CA are allowed. Self signed certificates are not allowed. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------- |

Set the client to expect and accept only self-signed certificates

```Kotlin
// Configure Server Authentication --
// only accept self-signed certs
acceptOnlySelfSignedServerCertificate = true, (1)
```

| **1** | Set this to true to accept any self signed cert. Any certificates that are not self-signed are rejected. |
| ----- | -------------------------------------------------------------------------------------------------------- |

Set the client to expect and accept only a pinned certificate.

```Kotlin
// Use the pinned certificate from the byte array (cert)
pinnedServerCertificate =
TLSIdentity.getIdentity("Our Corporate Id")?.certs?.get(0) as? X509Certificate (1)
    ?: throw IllegalStateException("Cannot find corporate id"),
```

* CA Cert
* Self Signed Cert
* Pinned Certificate

Set the client to expect and accept only CA attested certificates.

```Java
// Configure Server Security
// -- only accept CA attested certs
.setAcceptOnlySelfSignedServerCertificate(false); (1)
```

| **1** | This is the default. Only certificate chains with roots signed by a trusted CA are allowed. Self signed certificates are not allowed. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------- |

Set the client to expect and accept only self-signed certificates

```Java
// Configure Server Authentication --
// only accept self-signed certs
.setAcceptOnlySelfSignedServerCertificate(true) (1)
```

| **1** | Set this to true to accept any self signed cert. Any certificates that are not self-signed are rejected. |
| ----- | -------------------------------------------------------------------------------------------------------- |

Set the client to expect and accept only a pinned certificate.

```Java
// Use the pinned certificate from the byte array (cert)

TLSIdentity identity = TLSIdentity.getIdentity("OurCorp");
if (identity == null) { throw new IllegalStateException("Cannot find corporate id"); }
config.setPinnedServerX509Certificate((X509Certificate) identity.getCerts().get(0)); (1)
```

This all assumes that you have configured the Sync Gateway to provide the appropriate SSL certificates, and have included the appropriate certificate in your app bundle — for more on this see: [Certificate Pinning](#lbl-cert-pinning).

### [](#lbl-client-auth)Client Authentication

There are two ways to authenticate from a Couchbase Lite client: [Basic Authentication](#basic-authentication) or [Session Authentication](#session-authentication).

#### [](#basic-authentication)Basic Authentication

You can provide a user name and password to the basic authenticator class method. Under the hood, the replicator will send the credentials in the first request to retrieve a `SyncGatewaySession` cookie and use it for all subsequent requests during the replication. This is the recommended way of using basic authentication. [Example 7](#ex-base-auth) shows how to initiate a one-shot replication as the user **username** with the password **password**.

Example 7\. Basic Authentication

* Kotlin
* Java

```Kotlin

// Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
val repl = Replicator(
    ReplicatorConfigurationFactory.newConfig(
        collections = CollectionConfiguration.fromCollections(collections),
        target = URLEndpoint(URI("ws://localhost:4984/mydatabase")),
        authenticator = BasicAuthenticator("username", "password".toCharArray())
    )
)
repl.start()
thisReplicator = repl
```

```Java

// Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
Replicator repl = new Replicator(
    new ReplicatorConfiguration(Set.of(collectionConfig), new URLEndpoint(new URI("ws://localhost:4984/mydatabase")))
        .setAuthenticator(new BasicAuthenticator("username", "password".toCharArray())));

repl.start();
thisReplicator = repl;
```

#### [](#session-authentication)Session Authentication

Session authentication is another way to authenticate with Sync Gateway.

A user session must first be created through the [POST /{tkn-db}/\_session](../../../sync-gateway/current/rest-api/rest-api.md#/session/post%5F%5Fdb%5F%5F%5Fsession)endpoint on the Public REST API.

The HTTP response contains a session ID which can then be used to authenticate as the user it was created for.

See [Example 8](#ex-session-auth), which shows how to initiate a one-shot replication with the session ID returned from the `POST /{tkn-db}/_session` endpoint.

Example 8\. Session Authentication

* Kotlin
* Java

```Kotlin
// Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
val repl = Replicator(
    ReplicatorConfigurationFactory.newConfig(
        collections = CollectionConfiguration.fromCollections(collections),
        target = URLEndpoint(URI("ws://localhost:4984/mydatabase")),
        authenticator = SessionAuthenticator("904ac010862f37c8dd99015a33ab5a3565fd8447")
    )
)
repl.start()
thisReplicator = repl
```

```Java

// Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
Replicator repl = new Replicator(
    new ReplicatorConfiguration(Set.of(collectionConfig), new URLEndpoint(new URI("ws://localhost:4984/mydatabase")))
        .setAuthenticator(new SessionAuthenticator("904ac010862f37c8dd99015a33ab5a3565fd8447")));

repl.start();
thisReplicator = repl;
```

### [](#lbl-repl-hdrs)Custom Headers

Custom headers can be set on the configuration object. The replicator will then include those headers in every request.

This feature is useful in passing additional credentials, perhaps when an authentication or authorization step is being done by a proxy server (between Couchbase Lite and Sync Gateway) — see [Example 9](#ex-cust-hdr).

Example 9\. Setting custom headers

* Kotlin
* Java

```Kotlin
// Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
val repl = Replicator(
    ReplicatorConfigurationFactory.newConfig(
        collections = CollectionConfiguration.fromCollections(collections),
        target = URLEndpoint(URI("ws://localhost:4984/mydatabase")),
        headers = mapOf("CustomHeaderName" to "Value")
    )
)
repl.start()
thisReplicator = repl
```

```Java
Map<String, String> headers = new HashMap<>();
headers.put("CustomHeaderName", "Value");

// Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
Replicator repl = new Replicator(
    new ReplicatorConfiguration(Set.of(collectionConfig), new URLEndpoint(new URI("ws://localhost:4984/mydatabase")))
        .setHeaders(headers));

repl.start();
thisReplicator = repl;
```

### [](#lbl-repl-fltrs)Replication Filters

Replication Filters allow you to have quick control over the documents stored as the result of a push and/or pull replication.

#### [](#push-filter)Push Filter

The push filter allows an app to push a subset of a database to the server. This can be very useful. For instance, high-priority documents could be pushed first, or documents in a "draft" state could be skipped.

* Kotlin
* Java

```Kotlin
val collectionConfig = collections.map { collection ->
    CollectionConfigurationFactory.newConfig(
        collection = collection,
        pushFilter = { _, flags -> flags.contains(DocumentFlag.DELETED) }
    )
}.toSet()

// Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
val repl = Replicator(
    ReplicatorConfigurationFactory.newConfig(
        collections = collectionConfig,
        target = URLEndpoint(URI("ws://localhost:4984/mydatabase"))
    )
)
repl.start()
thisReplicator = repl
```

```Java
Set<CollectionConfiguration> collectionConfigs = CollectionConfiguration.fromCollections(collections);
collectionConfigs.forEach(it->it.setPushFilter((document, flags) -> flags.contains(DocumentFlag.DELETED))); (1)

// Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
Replicator repl = new Replicator(
    new ReplicatorConfiguration(collectionConfigs, new URLEndpoint(new URI("ws://localhost:4984/mydatabase"))));

repl.start();
thisReplicator = repl;
```

| **1** | The callback should follow the semantics of a [pure function](https://en.wikipedia.org/wiki/Pure%5Ffunction). Otherwise, long running functions would slow down the replicator considerably. Furthermore, your callback should not make assumptions about what thread it is being called on. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#### [](#pull-filter)Pull Filter

The pull filter gives an app the ability to validate documents being pulled, and skip ones that fail. This is an important security mechanism in a peer-to-peer topology with peers that are not fully trusted.

> [!NOTE]
> Pull replication filters are not a substitute for channels. Sync Gateway [channels](../../../sync-gateway/current/access-control/channels.md)are designed to be scalable (documents are filtered on the server) whereas a pull replication filter is applied to a document once it has been downloaded.

* Kotlin
* Java

```Kotlin
val collectionConfig = collections.map { collection ->
    CollectionConfigurationFactory.newConfig(
        collection = collection,
        pullFilter = { document, _ -> "draft" == document.getString("type") } (1)
    )
}.toSet()

// Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
val repl = Replicator(
    ReplicatorConfigurationFactory.newConfig(
        collections = collectionConfig,
        target = URLEndpoint(URI("ws://localhost:4984/mydatabase"))
    )
)
repl.start()
thisReplicator = repl
```

```Java
Set<CollectionConfiguration> collectionConfigs = CollectionConfiguration.fromCollections(collections);
collectionConfigs.forEach(it->it.setPullFilter((document, flags) -> "draft".equals(document.getString("type")))); (1)

// Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
Replicator repl = new Replicator(
    new ReplicatorConfiguration(collectionConfigs, new URLEndpoint(new URI("ws://localhost:4984/mydatabase"))));

repl.start();
thisReplicator = repl;
```

| **1** | The callback should follow the semantics of a [pure function](https://en.wikipedia.org/wiki/Pure%5Ffunction). Otherwise, long running functions would slow down the replicator considerably. Furthermore, your callback should not make assumptions about what thread it is being called on. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Losing access to a document via the Sync Function.

Losing access to a document (via the Sync Function) also triggers the pull replication filter.

Filtering out such an event would retain the document locally.

As a result, there would be a local copy of the document disjointed from the one that resides on Couchbase Server.

Further updates to the document stored on Couchbase Server would not be received in pull replications and further local edits could be pushed but the updated versions will not be visible.

For more information, see [Auto Purge on Revoke](#auto-purge-on-revoke).

### [](#lbl-repl-chan)Channels

By default, Couchbase Lite gets all the channels to which the configured user account has access.

This behavior is suitable for most apps that rely on [user authentication](../../../sync-gateway/current/security/authentication-users.md)and the [sync function](../../../sync-gateway/current/access-control/sync-function/sync-function-api.md)to specify which data to pull for each user.

Optionally, it's also possible to specify a string array of channel names on Couchbase Lite's collection configuration object. In this case, the replication from Sync Gateway will only pull documents tagged with those channels.

### [](#anchor-auto-purge-on-revoke)Auto-purge on Channel Access Revocation

> [!CAUTION]
> This is a Breaking Change at 3.0

#### [](#new-outcome)New outcome

By default, when a user loses access to a channel all documents in the channel (that do not also belong to any of the user's other channels) are auto-purged from the local database (in devices belonging to the user).

#### [](#prior-outcome)Prior outcome

_Previously these documents remained in the local database_

Prior to this release, CBL auto-purged only in the case when the user loses access to a document by removing the doc from all of the channels belong to the user. Now, in addition to 2.x auto purge, Couchbase Lite will also auto-purges the docs when the user loses access to the doc via channel access revocation. This feature is enabled by default, but an opt-out is available.

#### [](#behavior)Behavior

Users may lose access to channels in a number of ways:

* User loses direct access to channel
* User is removed from a role
* A channel is removed from a role the user is assigned to

By default, when a user loses access to a channel, the next Couchbase Lite Pull replication auto-purges all documents in the channel from local Couchbase Lite databases (on devices belonging to the user) **unless** they belong to any of the user's other channels — see: [Table 2](#tbl-revoke-behavior).

Documents that exist in multiple channels belonging to the user (even if they are not actively replicating that channel) are not auto-purged unless the user loses access to all channels.

When the auto-purge setting is set to `true`, users will receive an `AccessRemoved` notification from the DocumentListener if they lose document access due to channel access revocation.

__Table 2\. Behavior following access revocation__
| System State     | Impact on Sync                                                                       |                                                                                                                                               |
| ---------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Replication Type | Access Control on Sync Gateway                                                       | Expected behavior when _enable\_auto\_purge=true_                                                                                             |
| Pull only        | User revoked access to channel. Sync Function includes requireAccess(revokedChannel) | Previously synced documents are auto purged on local                                                                                          |
| Push only        | User revoked access to channel. Sync Function includes requireAccess(revokedChannel) | No impact of auto-purge Documents get pushed but are rejected by Sync Gateway                                                                 |
| Push-pull        | User revoked access to channelSync Function includes requireAccess(revokedChannel)   | Previously synced documents are auto purged on Couchbase Lite. Local changes continue to be pushed to remote but are rejected by Sync Gateway |

If a user subsequently regains access to a lost channel, then any previously auto-purged documents still assigned to any of their channels are automatically pulled down by the active Sync Gateway when they are next updated — see behavior summary in [Table 3](#tbl-regain-behavior)

__Table 3\. Behavior if access is regained__
| System State     | Impact on Sync                                                                                                     |                                                                                                                                                                                                                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Replication Type | Access Control on Sync Gateway                                                                                     | Expected behavior when _enable\_auto\_purge=true_                                                                                                                                                                                                                                          |
| Pull only        | User REASSIGNED access to channel                                                                                  | Previously purged documents that are still in the channel are automatically pulled by Couchbase Lite when they are next updated                                                                                                                                                            |
| Push only        | User REASSIGNED access to channel Sync Function includes requireAccess (reassignedChannel) No impact of auto-purge | Local changes previously rejected by Sync Gateway will not be automatically pushed to remote unless resetCheckpoint is involved on CBL. Document changes subsequent to the channel reassignment will be pushed up as usual.                                                                |
| Push-pull        | User REASSIGNED access to channel Sync Function includes requireAccess (reassignedChannel)                         | Previously purged documents are automatically pulled by couchbase lite Local changes previously rejected by Sync Gateway will not be automatically pushed to remote unless resetCheckpoint is involved. Document changes subsequent to the channel reassignment will be pushed up as usual |

#### [](#config)Config

Auto-purge behavior is controlled primarily by the ReplicationConfiguration option [setAutoPurgeEnabled()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicatorConfiguration.html#setAutoPurgeEnabled-boolean-). Changing the state of this will impact **only** future replications; the replicator will not attempt to sync revisions that were auto purged on channel access removal. Clients wishing to sync previously removed documents must use the resetCheckpoint API to resync from the start.

Example 10\. Setting auto-purge

* Kotlin
* Java

```Kotlin
// set auto-purge behavior
// (here we override default)
enableAutoPurge = false, (1)
```

```Java
// set auto-purge behavior
// (here we override default)
.setAutoPurgeEnabled(false) (1)
```

| **1** | Here we have opted to turn off the auto purge behavior. By default auto purge is enabled. |
| ----- | ----------------------------------------------------------------------------------------- |

#### [](#overrides)Overrides

Where necessary, clients can override the default auto-purge behavior. This can be done either by setting [setAutoPurgeEnabled()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicatorConfiguration.html#setAutoPurgeEnabled-boolean-) to false, or for finer control by applying pull-filters — see: [Table 4](#tbl-pull-filters) and [Replication Filters](#lbl-repl-fltrs)This ensures backwards compatible with 2.8 clients that use pull filters to prevent auto purge of removed docs.

__Table 4\. Impact of Pull-Filters__
| purge\_on\_removal setting | Pull Filter                                                                                         |                               |
| -------------------------- | --------------------------------------------------------------------------------------------------- | ----------------------------- |
| Not Defined                | Defined to filter removals/revoked docs                                                             |                               |
| disabled                   | Doc remains in local database App notified of "accessRemoved" if a _Documentlistener_ is registered |                               |
| enabled (DEFAULT)          | Doc is auto purged App notified of "accessRemoved" if _Documentlistener_ registered                 | Doc remains in local database |

### [](#lbl-repl-delta)Delta Sync

> [!IMPORTANT]
> This is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature.

With Delta Sync \[[2](#%5Ffootnotedef%5F2 "View footnote.")\], only the changed parts of a Couchbase document are replicated. This can result in significant savings in bandwidth consumption as well as throughput improvements, especially when network bandwidth is typically constrained.

Replications to a Server (for example, a Sync Gateway, or passive listener) automatically use delta sync if the property is enabled at database level by the server — see: [databases.$db.delta\_sync.enabled](../../../sync-gateway/current/configuration/configuration-properties-legacy.md#databases-foo%5Fdb-delta%5Fsync).

[Intra-Device](dbreplica.md)replications automatically **disable** delta sync, whilst [Peer-to-Peer](#p2psync-websocket.adoc)replications automatically **enable** delta sync.

## [](#lbl-init-repl)Initialize

In this section

[Start Replicator](#lbl-repl-start) | [Checkpoint Starts](#lbl-repl-ckpt)

### [](#lbl-repl-start)Start Replicator

Use the `[Replicator](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/Replicator.html)` class's [ReplicatorConfiguration(config)](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/Replicator.html#Replicator-com.couchbase.lite.ReplicatorConfiguration-) constructor, to initialize the replicator with the configuration you have defined. You can, optionally, add a change listener (see [Monitor](#lbl-repl-mon)) before starting the replicator running using [start()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#start-boolean-).

Example 11\. Initialize and run replicator

* Kotlin
* Java

```Kotlin
val replConfig: ReplicatorConfiguration =
    ReplicatorConfiguration(replicatorConfiguration) (1)
repl.start() (2)
```

```Java
ReplicatorConfiguration replConfig = new ReplicatorConfiguration(replicatorConfiguration); (1)
repl.start(); (2)
```

| **1** | Initialize the replicator with the configuration |
| ----- | ------------------------------------------------ |
| **2** | Start the replicator                             |

### [](#lbl-repl-ckpt)Checkpoint Starts

Replicators use [checkpoints](refer-glossary.md#checkpoint) to keep track of documents sent to the target database.

Without [checkpoints](refer-glossary.md#checkpoint), Couchbase Lite would replicate the entire database content to the target database on each connection, even though previous replications may already have replicated some or all of that content.

This functionality is generally not a concern to application developers. However, if you do want to force the replication to start again from zero, use the [checkpoint](refer-glossary.md#checkpoint) reset argument when starting the replicator — as shown in [Example 12](#ex-repl-ckpt).

Example 12\. Resetting checkpoints

* Kotlin
* Java

```Kotlin
repl.start(true)
```

```Java
repl.start(true);
```

| **1** | Set start's reset option to true.The default false is shown here for completeness only; it is unlikely you would explicitly use it in practice. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#lbl-repl-mon)Monitor

In this section

[Change Listeners](#lbl-repl-chng) | [Replicator Status](#lbl-repl-status) | [Monitor Document Changes](#lbl-repl-evnts) | [Documents Pending Push](#lbl-repl-pend) | [Correlation ID](#lbl-repl-correlation-id)

You can monitor a replication's status by using a combination of [Change Listeners](#lbl-repl-chng) and the `replication.status.activity` property — see; [getActivityLevel()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/ReplicatorStatus.html#getActivityLevel%28%29). This enables you to know, for example, when the replication is actively transferring data and when it has stopped.

You can also choose to monitor document changes — see: [Monitor Document Changes](#lbl-repl-evnts).

### [](#lbl-repl-chng)Change Listeners

Use this to monitor changes and to inform on sync progress; this is an optional step. You can add and a replicator change listener at any point; it will report changes from the point it is registered.

> [!TIP]
> Best Practice
> 
> Don't forget to save the token so you can remove the listener later

Use the [Replicator](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/Replicator.html) class to add a change listener as a callback to the Replicator ([addChangeListener()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#addChangeListener-java.util.concurrent.Executor-com.couchbase.lite.ReplicatorChangeListener-)) — see: [Example 13](#ex-repl-mon). You will then be asynchronously notified of state changes.

You can remove a change listener with [removeChangeListener(ListenerToken token)](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#removeChangeListener-com.couchbase.lite.ListenerToken-).

#### [](#using-kotlin-flows-and-livedata)Using Kotlin Flows and LiveData

Android Kotlin developers can take advantage of Flows and LiveData to monitor replicators.

```Kotlin
        return replicator.replicatorChangesFlow()
            .map { change -> change.status }
            .asLiveData()
```

### [](#lbl-repl-status)Replicator Status

You can use the [ReplicatorStatus()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/ReplicatorStatus.html) class to check the replicator status. That is, whether it is actively transferring data or if it has stopped — see: [Example 13](#ex-repl-mon).

The returned _ReplicationStatus_ structure comprises:

* [getActivityLevel()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/ReplicatorStatus.html#getActivityLevel%28%29) — stopped, offline, connecting, idle or busy — see states described in: [Table 5](#tbl-states)
* [getProgress()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/ReplicatorStatus.html#getProgress%28%29)

  * completed — the total number of changes completed
  * total — the total number of changes to be processed
* [getError()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/ReplicatorStatus.html#getError) — the current error, if any

Example 13\. Monitor replication

* Kotlin
* Java

* Adding a Change Listener
* Using replicator.status

```Kotlin
val token = repl.addChangeListener { change ->
    val err: CouchbaseLiteException? = change.status.error
    if (err != null) {
        log("Error code ::  ${err.code}", err)
    }
}
```

```Kotlin
repl.status.let {
    val progress = it.progress
    log(
        "The Replicator is ${
            it.activityLevel
        } and has processed ${
            progress.completed
        } of ${progress.total} changes"
    )
}
```

* Adding a Change Listener
* Using replicator.status

```Java
ListenerToken token = repl.addChangeListener(change -> {
    CouchbaseLiteException err = change.getStatus().getError();
    if (err != null) { Logger.log("Error code :: " + err.getCode(), err); }
});
```

```Java
    ReplicatorStatus status = repl.getStatus();
    ReplicatorProgress progress = status.getProgress();
    Logger.log(
        "The Replicator is " + status.getActivityLevel()
            + "and has processed " + progress.getCompleted()
            + " of " + progress.getTotal() + " changes");
}
```

#### [](#lbl-repl-states)Replication States

[Table 5](#tbl-states) shows the different states, or activity levels, reported in the API; and the meaning of each.

__Table 5\. Replicator activity levels__
| State      | Meaning                                                                                                                           |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------- |
| STOPPED    | The replication is finished or hit a fatal error.                                                                                 |
| OFFLINE    | The replicator is offline as the remote host is unreachable.                                                                      |
| CONNECTING | The replicator is connecting to the remote host.                                                                                  |
| IDLE       | The replication caught up with all the changes available from the server. The IDLE state is only used in continuous replications. |
| BUSY       | The replication is actively transferring data.                                                                                    |

> [!NOTE]
> The replication change object also has properties to track the progress (`change.status.completed` and `change.status.total`). Since the replication occurs in batches the total count can vary through the course of a replication.

#### [](#replication-status-and-app-life-cycle)Replication Status and App Life Cycle

Couchbase Lite replications will continue running until the app terminates, unless the remote system, or the application, terminates the connection.

> [!NOTE]
> Recall that the Android OS may kill an application without warning. You should explicitly stop replication processes when they are no longer useful (for example, when they are `suspended` or `idle`) to avoid socket connections being closed by the OS, which may interfere with the replication process.

### [](#lbl-repl-evnts)Monitor Document Changes

You can choose to register for document updates during a replication.

For example, the code snippet in [Example 14](#ex-reg-doc-listener) registers a listener to monitor document replication performed by the replicator referenced by the variable `replicator`. It prints the document ID of each document received and sent. Stop the listener as shown in [Example 15](#ex-stop-doc-listener).

Example 14\. Register a document listener

* Kotlin
* Java

```Kotlin
val token = repl.addDocumentReplicationListener { replication ->
    log("Replication type: ${if (replication.isPush) "push" else "pull"}")

    for (document in replication.documents) {
        document.let { doc ->
            log("Doc ID: ${document.id}")

            doc.error?.let {
                // There was an error
                log("Error replicating document: ", it)
                return@addDocumentReplicationListener
            }

            if (doc.flags.contains(DocumentFlag.DELETED)) {
                log("Successfully replicated a deleted document")
            }
        }
    }
}

repl.start()
thisReplicator = repl
```

```Java
ListenerToken token = repl.addDocumentReplicationListener(replication -> {
    Logger.log("Replication type: " + ((replication.isPush()) ? "push" : "pull"));
    for (ReplicatedDocument document: replication.getDocuments()) {
        Logger.log("Doc ID: " + document.getID());

        CouchbaseLiteException err = document.getError();
        if (err != null) {
            // There was an error
            Logger.log("Error replicating document: ", err);
            return;
        }

        if (document.getFlags().contains(DocumentFlag.DELETED)) {
            Logger.log("Successfully replicated a deleted document");
        }
    }
});


repl.start();
thisReplicator = repl;
```

Example 15\. Stop document listener

This code snippet shows how to stop the document listener using the token from the previous example.

* Kotlin
* Java

```Kotlin
token.remove()
```

```Java
token.remove();
```

#### [](#document-access-removal-behavior)Document Access Removal Behavior

When access to a document is removed on Sync Gateway (see: Sync Gateway's [Sync Function](../../../sync-gateway/current/access-control/sync-function/sync-function-api.md)), the document replication listener sends a notification with the `AccessRemoved` flag set to `true` and subsequently purges the document from the database.

### [](#lbl-repl-pend)Documents Pending Push

> [!TIP]
> [Replicator.isDocumentPending()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#isDocumentPending-java.lang.String-) is quicker and more efficient. Use it in preference to returning a list of pending document IDs, where possible.

You can check whether documents are waiting to be pushed in any forthcoming sync by using either of the following API methods:

* Use the [Replicator.getPendingDocumentIds()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#getPendingDocumentIds--) method, which returns a list of document IDs that have local changes, but which have not yet been pushed to the server.  
This can be very useful in tracking the progress of a push sync, enabling the app to provide a visual indicator to the end user on its status, or decide when it is safe to exit.
* Use the [Replicator.isDocumentPending()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#isDocumentPending-java.lang.String-) method to quickly check whether an individual document is pending a push.

Example 16\. Use Pending Document ID API

* Kotlin
* Java

```Kotlin
val repl = Replicator(
    ReplicatorConfigurationFactory.newConfig(
        collections = CollectionConfiguration.fromCollections(setOf(collection)),
        target = URLEndpoint(URI("ws://localhost:4984/mydatabase")),
        type = ReplicatorType.PUSH
    )
)

val pendingDocs = repl.getPendingDocumentIds(collection)

// iterate and report on previously
// retrieved pending docids 'list'
if (pendingDocs.isNotEmpty()) {
    log("There are ${pendingDocs.size} documents pending")

    val firstDoc = pendingDocs.first()
    repl.addChangeListener { change ->
        log("Replicator activity level is ${change.status.activityLevel}")
        try {
            if (!repl.isDocumentPending(firstDoc, collection)) {
                log("Doc ID $firstDoc has been pushed")
            }
        } catch (err: CouchbaseLiteException) {
            log("Failed getting pending docs", err)
        }
    }

    repl.start()
    thisReplicator = repl
}
```

```Java
CollectionConfiguration collConfig = new CollectionConfiguration(collection);
Replicator repl = new Replicator(
        new ReplicatorConfiguration(
                Set.of(collConfig),
                new URLEndpoint(new URI("ws://localhost:4984/mydatabase")))
                .setType(ReplicatorType.PUSH));

Set<String> pendingDocs = repl.getPendingDocumentIds(collection);

if (!pendingDocs.isEmpty()) {
    Logger.log("There are " + pendingDocs.size() + " documents pending");

    final String firstDoc = pendingDocs.iterator().next();

    repl.addChangeListener(change -> {
        Logger.log("Replicator activity level is " + change.getStatus().getActivityLevel());
        try {
            if (!repl.isDocumentPending(firstDoc, collection)) {
                Logger.log("Doc ID " + firstDoc + " has been pushed");
            }
        }
        catch (CouchbaseLiteException err) {
            Logger.log("Failed getting pending docs", err);
        }
    });

    repl.start();
    this.thisReplicator = repl;
}
```

| **1** | [Replicator.getPendingDocumentIds()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#getPendingDocumentIds--) returns a list of the document IDs for all documents waiting to be pushed. This is a snapshot and may have changed by the time the response is received and processed. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [Replicator.isDocumentPending()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#isDocumentPending-java.lang.String-) returns true if the document is waiting to be pushed, and false otherwise.                                                                                     |

### [](#lbl-repl-correlation-id)Correlation ID

The correlation ID is a read-only property that identifies the Sync Gateway session associated with a Couchbase Lite replicator. Use it to correlate log entries on the client and server when diagnosing replication issues.

Example 17\. Get the replicator correlation ID

* Kotlin
* Java

```Kotlin
val correlationID = replicator.correlationId
```

```Java
String correlationID = replicator.getCorrelationId();
```

## [](#lbl-repl-stop)Stop

Stopping a replication is straightforward. It is done using [stop()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#stop--). This initiates an asynchronous operation and so is not necessarily immediate. Your app should account for this potential delay before attempting any subsequent operations.

You can find further information on database operations in [Databases](database.md).

Example 18\. Stop replicator

* Kotlin
* Java

```Kotlin
// Stop replication.
repl.stop() (1)
```

```Java
// Stop replication.
repl.stop(); (1)
```

| **1** | Here we initiate the stopping of the replication using the [stop()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#stop--) method. It will stop any active [change listener](#lbl-repl-chng) once the replication is stopped. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#lbl-nwk-errs)Error Handling

When _replicator_ detects a network error it updates its status depending on the error type (permanent or temporary) and returns an appropriate HTTP error code.

The following code snippet adds a `Change Listener`, which monitors a replication for errors and logs the the returned error code.

Example 19\. Monitoring for network errors

* Kotlin
* Java

```Kotlin
repl.addChangeListener { change ->
    change.status.error?.let {
        log("Error code: ${it.code}")
    }
}
repl.start()
thisReplicator = repl
```

```Java
repl.addChangeListener(change -> {
    CouchbaseLiteException error = change.getStatus().getError();
    if (error != null) { Logger.log("Error code:: " + error); }
});
repl.start();
thisReplicator = repl;
```

**For permanent network errors** (for example, `404` not found, or `401` unauthorized): _Replicator_ will stop permanently, whether `setContinuous` is _true_ or _false_. Of course, it sets its status to `STOPPED`

**For recoverable or temporary errors:** _Replicator_ sets its status to `OFFLINE`, then:

* If `setContinuous=_true_` it retries the connection indefinitely
* If `setContinuous=_false_` (one-shot) it retries the connection a limited number of times.

The following error codes are considered temporary by the Couchbase Lite replicator and thus will trigger a connection retry.

* `408`: Request Timeout
* `429`: Too Many Requests
* `500`: Internal Server Error
* `502`: Bad Gateway
* `503`: Service Unavailable
* `504`: Gateway Timeout
* `1001`: DNS resolution error

### [](#using-kotlin-flows-and-livedata-2)Using Kotlin Flows and LiveData

Android Kotlin developers can also take advantage of Flows and LiveData to monitor replicators.

```Kotlin
        return replicator.replicatorChangesFlow()
            .map { change -> change.status }
            .asLiveData()
```

## [](#load-balancers)Load Balancers

Couchbase Lite \[[3](#%5Ffootnotedef%5F3 "View footnote.")\] uses WebSockets as the communication protocol to transmit data. Some load balancers are not configured for WebSocket connections by default (NGINX for example); so it might be necessary to explicitly enable them in the load balancer's configuration (see [Load Balancers](../../../sync-gateway/current/deploy/load-balancer.md)).

By default, the WebSocket protocol uses compression to optimize for speed and bandwidth utilization. The level of compression is set on Sync Gateway and can be tuned in the configuration file ([replicator\_compression](../../../sync-gateway/current/configuration/configuration-properties-legacy.md#replicator%5Fcompression)).

## [](#lbl-cert-pinning)Certificate Pinning

Couchbase Lite for Android supports certificate pinning.

Certificate pinning is a technique that can be used by applications to "pin" a host to its certificate. The certificate is typically delivered to the client by an out-of-band channel and bundled with the client. In this case, Couchbase Lite uses this embedded certificate to verify the trustworthiness of the server (for example, a Sync Gateway) and no longer needs to rely on a trusted third party for that (commonly referred to as the Certificate Authority).

The following steps describe how to configure certificate pinning between Couchbase Lite and Sync Gateway.

1. [Create your own self-signed certificate](../../../sync-gateway/current/security/authentication-certs.md#creating-your-own-self-signed-certificate)with the `openssl` command. After completing this step, you should have 3 files: `cert.pem`, `cert.cer` and `privkey.pem`.
2. [Configure Sync Gateway](../../../sync-gateway/current/security/authentication-certs.md#installing-the-certificate)with the `cert.pem` and `privkey.pem` files. After completing this step, Sync Gateway is reachable over `https`/`wss`.
3. On the Couchbase Lite side, the replication must point to a URL with the `wss` scheme and configured with the `cert.cer` file created in step 1.  
This example loads the certificate from the application sandbox, then converts it to the appropriate type to configure the replication object.

Example 20\. Cert Pinnings

* Kotlin
* Java

```Kotlin
val repl = Replicator(
    ReplicatorConfigurationFactory.newConfig(
        collections = CollectionConfiguration.fromCollections(collections),
        target = URLEndpoint(URI("ws://localhost:4984/mydatabase")),
        pinnedServerCertificate = KeyStore.getInstance(keyStoreName)
            .getCertificate(certAlias) as X509Certificate
    )
)
repl.start()
thisReplicator = repl
```

```Java
// Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
Replicator repl = new Replicator(
        new ReplicatorConfiguration(
                CollectionConfiguration.fromCollections(collections),
                new URLEndpoint(new URI("ws://localhost:4984/mydatabase")))
                .setPinnedServerX509Certificate(
                        (X509Certificate) KeyStore.getInstance(keyStoreName).getCertificate(certAlias)));

repl.start();
thisReplicator = repl;
```

1. Build and run your app. The replication should now run successfully over https/wss with certificate pinning.

For more on pinning certificates see the blog entry: [Certificate Pinning with Couchbase Mobile](https://blog.couchbase.com/certificate-pinning-android-with-couchbase-mobile/)

## [](#lbl-trouble)Troubleshooting

### [](#logs)Logs

As always, when there is a problem with replication, logging is your friend. You can increase the log output for activity related to replication with Sync Gateway — see [Example 21](#ex-logs).

Example 21\. Set logging verbosity

* Kotlin
* Java

```Kotlin
CouchbaseLite.init(this, true)

LogSinks.get().console = ConsoleLogSink(LogLevel.DEBUG, LogDomain.REPLICATOR)
```

```Java
CouchbaseLite.init(this, true);

LogSinks.get().setConsole(new ConsoleLogSink(LogLevel.DEBUG));
```

For more on troubleshooting with logs, see: [Using Logs](new-logging-api.md).

### [](#authentication-errors)Authentication Errors

If Sync Gateway is configured with a self signed certificate but your app points to a `ws` scheme instead of `wss` you will encounter an error with status code `11006` — see: [Example 22](#ex-11006)

Example 22\. Protocol Mismatch

```console
CouchbaseLite Replicator ERROR: {Repl#2} Got LiteCore error: WebSocket error 1006 "connection closed abnormally"
```

If Sync Gateway is configured with a self signed certificate, and your app points to a `wss` scheme but the replicator configuration isn't' using the certificate you will encounter an error with status code `5011` — see: [Example 23](#ex-5011)

Example 23\. Certificate Mismatch or Not Found

```text
CouchbaseLite Replicator ERROR: {Repl#2} Got LiteCore error: Network error 11 "server TLS certificate is self-signed or has unknown root cert"
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

.

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.

---

[1](#%5Ffootnoteref%5F1). Prior to version 2.6 

[2](#%5Ffootnoteref%5F2). Couchbase Mobile 2.5+ 

[3](#%5Ffootnoteref%5F3). From 2.0