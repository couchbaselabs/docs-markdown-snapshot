---
title: Data Sync using Sync Gateway
description: Couchbase Lite for C -- Synchronizing data changes between local
  and remote databases using Sync Gateway
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/c/pages/replication.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:4.0@couchbase-lite:c:replication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/4.0/c/replication.html)

# Data Sync using Sync Gateway

> Description — _Couchbase Lite for C — Synchronizing data changes between local and remote databases using Sync Gateway_  
> Related Content — [Handling Data Conflicts](conflict.md) | [Intra-Device](dbreplica.md) | [Peer-to-Peer](#p2psync-websocket.adoc)

> [!NOTE]
> Code Snippets
> 
> All code examples are indicative only. They demonstrate the basic concepts and approaches to using a feature. Use them as inspiration and adapt these examples to best practice when developing applications for your platform.

## [](#introduction)Introduction

Couchbase Lite for C provides API support for secure, bi-directional, synchronization of data changes between mobile applications and a central server database. It does so by using a _replicator_ to interact with Sync Gateway.

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

```c
// Purpose -- illustrate a simple change listener
static void simpleChangeListener(void* context,
                                 CBLReplicator* repl,
                                 const CBLReplicatorStatus* status)
{
     if(status->error.code != 0) {
         printf("Error %d / %d\n",
                status->error.domain,
                status->error.code);
     }
}
    // Purpose -- Show configuration , initialization and running of a replicator

    // NOTE: No error handling, for brevity (see getting started)
    // Note: Android emulator needs to use 10.0.2.2 for localhost (10.0.3.2 for GenyMotion)

    CBLError err{};
    FLString url = FLSTR("ws://localhost:4984/db");
    CBLEndpoint* target = CBLEndpoint_CreateWithURL(url, &err); (1)

    CBLCollectionConfiguration collectionConfig = {0};
    collectionConfig.collection = collection;

    CBLReplicatorConfiguration replConfig = {0};
    replConfig.collections = &collectionConfig;
    replConfig.collectionCount = 1;
    replConfig.endpoint = target; (2)

    // Set replication direction and mode
    replConfig.replicatorType = kCBLReplicatorTypePull; (3)
    replConfig.continuous = true;

    // Optionally, set auto-purge behavior (here we override default)
    replConfig.disableAutoPurge = true; (4)

    // Optionally, configure Client Authentication
    // Here we are using to Basic Authentication,
    // Providing username and password credentials
    CBLAuthenticator* basicAuth =
        CBLAuth_CreatePassword(FLSTR("username"),
                               FLSTR("passwd")); (5)
    replConfig.authenticator = basicAuth;

    // Optionally, configure how we handle conflicts (note that this is set
    // per collection, and not on the overall replicator)
    collectionConfig.conflictResolver = simpleConflictResolver_localWins; (6)

    // Initialize replicator with created config
    CBLReplicator* replicator =
        CBLReplicator_Create(&replConfig, &err); (7)

    CBLEndpoint_Free(target);

    // Optionally, add change listener
    CBLListenerToken* token =
            CBLReplicator_AddChangeListener(replicator,
                                            simpleChangeListener,
                                            NULL); (8)

    // Start replication
    CBLReplicator_Start(replicator, false); (9)
```

**Notes on Example**

| **1** | get endpoint for target DB                                                                                                                                                                                                                                                                                |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Set local database and target endpoint                                                                                                                                                                                                                                                                    |
| **3** | The default is to auto-purge documents that this user no longer has access to — see: [Auto-purge on Channel Access Revocation](#anchor-auto-purge-on-revoke). Here we over-ride this behavior by setting its flag false.                                                                                  |
| **4** | Configure how the client will authenticate the server. Here we say connect only to servers presenting a self-signed certificate. By default, clients accept only servers presenting certificates that can be verified using the OS bundled Root CA Certificates — see: [\[lbl-svr-auth\]](#lbl-svr-auth). |
| **5** | Configure the client-authentication credentials (if required). These are the credential the client will present to sync gateway if requested to do so.Here we configure to provide _Basic Authentication_ credentials. Other options are available — see: [Client Authentication](#lbl-client-auth).      |
| **6** | Configure how the replication should handle conflict resolution — see: [Handling Data Conflicts](conflict.md) topic for mor on conflict resolution.                                                                                                                                                       |
| **7** | Initialize the replicator using your configuration — see: [Initialize](#lbl-init-repl).                                                                                                                                                                                                                   |
| **8** | Optionally, register an observer, which will notify you of changes to the replication status — see: [Monitor](#lbl-repl-mon)                                                                                                                                                                              |
| **9** | Start the replicator — see: [Start Replicator](#lbl-repl-start).                                                                                                                                                                                                                                          |

## [](#lbl-cfg-repl)Configure

In this section

[Configure Target](#lbl-cfg-tgt)| [Sync Mode](#lbl-cfg-sync)| [Retry Configuration](#lbl-cfg-keep-alive)| [User Authorization](#lbl-user-auth)| [Client Authentication](#lbl-client-auth)| [Monitor Document Changes](#lbl-repl-evnts)| [Custom Headers](#lbl-repl-hdrs)| [Checkpoint Starts](#lbl-repl-ckpt)| [Replication Filters](#lbl-repl-fltrs)| [Channels](#lbl-repl-chan)| [Auto-purge on Channel Access Revocation](#anchor-auto-purge-on-revoke)| [Delta Sync](#lbl-repl-delta)

### [](#lbl-cfg-tgt)Configure Target

Use the Initialize and define the replication configuration with local and remote database locations using the [CBLReplicatorConfiguration](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html) object.

The constructor provides:

* the name of the local database to be sync'd
* the server's URL (including the port number and the name of the remote database to sync with)  
It is expected that the app will identify the IP address and URL and append the remote database name to the URL endpoint, producing for example: `wss://10.0.2.2:4984/travel-sample`  
The URL scheme for web socket URLs uses `ws:` (non-TLS) or `wss:` (SSL/TLS) prefixes.

Example 2\. Add Target to Configuration

```c
// Initialize the configuration object and set db target
CBLError err{};
FLString url = FLSTR("ws://localhost:4984/db");
CBLEndpoint* target =
    CBLEndpoint_CreateWithURL(url, &err); (1)

CBLCollectionConfiguration collectionConfig = {0};
collectionConfig.collection = collection;

CBLReplicatorConfiguration replConfig = {0};
replConfig.collections = &collectionConfig;
replConfig.collectionCount = 1;
replConfig.endpoint = target; (2)
```

| **1** | Note use of the scheme prefix (wss://to ensure TLS encryption — strongly recommended in production — or ws://) |
| ----- | -------------------------------------------------------------------------------------------------------------- |

### [](#lbl-cfg-sync)Sync Mode

Here we define the direction and type of replication we want to initiate.

We use `[CBLReplicatorConfiguration](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html)` class's [replicatorType](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#a40f3195389ab0578aa17e63dd832a390) and `[continuous](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#a3d17159fc65a7491c2cde2f56a5016df)` parameters, to tell the replicator:

* The type (or direction) of the replication: `**pushAndPull**`; `pull`; `push`
* The replication mode, that is either of:

  * Continuous — remaining active indefinitely to replicate changed documents (`continuous=true`).
  * Ad-hoc — a one-shot replication of changed documents (`continuous=false`).

Example 3\. Configure replicator type and mode

```c
// Set replication direction and mode
replConfig.replicatorType = kCBLReplicatorTypePull; (1)
replConfig.continuous = true;
replConfig.replicatorType = kCBLReplicatorTypePull;
replConfig.continuous = true;
```

> [!TIP]
> Unless there is a solid use-case not to, always initiate a single `PUSH_AND_PULL` replication rather than identical separate `PUSH` and `PULL` replications.
> 
> This prevents the replications generating the same checkpoint `docID` resulting in multiple conflicts.

### [](#lbl-cfg-keep-alive)Retry Configuration

Couchbase Lite for C's replication retry logic assures a resilient connection.

The replicator minimizes the chance and impact of dropped connections by maintaining a heartbeat; essentially pinging the Sync Gateway at a configurable interval to ensure the connection remains alive.

In the event it detects a transient error, the replicator will attempt to reconnect, stopping only when the connection is re-established, or the number of retries exceeds the retry limit (9 times for a single-shot replication and unlimited for a continuous replication).

On each retry the interval between attempts is increased exponentially (exponential backoff) up to the maximum wait time limit (5 minutes).

The REST API provides configurable control over this replication retry logic using a set of configiurable properties — see: [Table 1](#tbl-repl-retry).

__Table 1\. Replication Retry Configuration Properties__
| Property                                                                                                                                                              | Use cases                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| {url-api-prop-replicator-config-setHeartbeat}                                                                                                                         | Reduce to detect connection errors sooner Align to load-balancer or proxy keep-alive interval — see Sync Gateway's topic [Load Balancer - Keep Alive](../../../sync-gateway/current/deploy/load-balancer.md#websocket-connection) | The interval (in seconds) between the heartbeat pulses. Default: The replicator pings the Sync Gateway every 300 seconds.                                                                                                                                                                                                                                                                                                                                                                         |
| [maxAttempts](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#a5b6435c711d93f71566d8814506e0dff) | Change this to limit or extend the number of retry attempts.                                                                                                                                                                      | The maximum number of retry attempts Set to zero (0) to use default values Set to zero (1) to prevent any retry attempt The retry attempt count is reset when the replicator is able to connect and replicate Default values are: Single-shot replication = 9; Continuous replication = maximum integer value Negative values generate a Couchbase exception InvalidArgumentException                                                                                                             |
| {url-api-prop-replicator-config-setMaxAttemptWaitTime}                                                                                                                | Change this to adjust the interval between retries.                                                                                                                                                                               | The maximum interval between retry attempts While you can configure the **maximum permitted** wait time, the replicator's exponential backoff algorithm calculates each individual interval which is not configurable. Default value: 300 seconds (5 minutes) Zero sets the maximum interval between retries to the default of 300 seconds 300 sets the maximum interval between retries to the default of 300 seconds A negative value generates a Couchbase exception, InvalidArgumentException |

When necessary you can adjust any or all of those configurable values — see: [Example 4](#ex-repl-retry) for how to do this.

Example 4\. Configuring Replication Retries

```c
// Configure replication retries
replConfig.heartbeat = 120; //  (1)

replConfig.maxAttempts = 20; //  (2)

replConfig.maxAttemptWaitTime = 600; //  (3)
```

| **1** | Here we use {url-api-prop-replicator-config-setHeartbeat} to set the required interval (in seconds) between the heartbeat pulses                                                                                               |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | Here we use [maxAttempts](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#a5b6435c711d93f71566d8814506e0dff) to set the required number of retry attempts |
| **3** | Here we use {url-api-prop-replicator-config-setMaxAttemptWaitTime} to set the required interval between retry attempts.                                                                                                        |

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

### [](#lbl-client-auth)Client Authentication

There are two ways to authenticate from a Couchbase Lite client: [Basic Authentication](#basic-authentication) or [Session Authentication](#session-authentication).

#### [](#basic-authentication)Basic Authentication

You can provide a user name and password to the basic authenticator class method. Under the hood, the replicator will send the credentials in the first request to retrieve a `SyncGatewaySession` cookie and use it for all subsequent requests during the replication. This is the recommended way of using basic authentication. [Example 6](#ex-base-auth) shows how to initiate a one-shot replication as the user **username** with the password **password**.

Example 6\. Basic Authentication

```c
// Configure Client Authentication to Basic Authentication
// Providing username and password credentials
if(docs_example_ShowBasicAuth) {
    CBLAuthenticator* basicAuth =
        CBLAuth_CreatePassword(FLSTR("username"),
        FLSTR("passwd"));
    replConfig.authenticator = basicAuth; (1)
}
```

#### [](#session-authentication)Session Authentication

Session authentication is another way to authenticate with Sync Gateway.

A user session must first be created through the [POST /{tkn-db}/\_session](../../../sync-gateway/current/rest-api/rest-api.md#/session/post%5F%5Fdb%5F%5F%5Fsession)endpoint on the Public REST API.

The HTTP response contains a session ID which can then be used to authenticate as the user it was created for.

See [Example 7](#ex-session-auth), which shows how to initiate a one-shot replication with the session ID returned from the `POST /{tkn-db}/_session` endpoint.

Example 7\. Session Authentication

```c
if(docs_example_ShowSessionAuth) {
    CBLAuthenticator* sessionAuth =
        CBLAuth_CreateSession(FLSTR("904ac010862f37c8dd99015a33ab5a3565fd8447"),
        FLSTR("optionalCookieName"));
    replConfig.authenticator = sessionAuth; (1)
}
```

### [](#lbl-repl-hdrs)Custom Headers

Custom headers can be set on the configuration object. The replicator will then include those headers in every request.

This feature is useful in passing additional credentials, perhaps when an authentication or authorization step is being done by a proxy server (between Couchbase Lite and Sync Gateway) — see [Example 8](#ex-cust-hdr).

Example 8\. Setting custom headers

```c
// Optionally, add custom headers
FLMutableDict customHdrs = FLMutableDict_New();
FLMutableDict_SetString(customHdrs,
    FLSTR("customHeaderName"),
    FLSTR("customHeaderValue"));

replConfig.headers = customHdrs;

char cert_buf[10000];
FILE* cert_file = fopen("cert.pem", "r");
size_t read = fread(cert_buf, 1, sizeof(cert_buf), cert_file);
replConfig.pinnedServerCertificate = (FLSlice){cert_buf, read};
```

### [](#lbl-repl-fltrs)Replication Filters

Replication Filters allow you to have quick control over the documents stored as the result of a push and/or pull replication.

#### [](#push-filter)Push Filter

The push filter allows an app to push a subset of a database to the server. This can be very useful. For instance, high-priority documents could be pushed first, or documents in a "draft" state could be skipped.

Push Filter

```c
// Purpose -- illustrate a simple replication filter function
static bool simpleReplicationFilter(void* context,
                                    CBLDocument* argDoc,
                                    CBLDocumentFlags argFlags)
{
    bool result = (argFlags == kCBLDocumentFlagsDeleted);
    return result;
}

    // Purpose - Illustrate use of push and-or pull filter functions

    // NOTE: Push and pull filters are set per collection
    collectionConfig.pushFilter = simpleReplicationFilter;
    collectionConfig.pullFilter = simpleReplicationFilter;
```

| **1** | Do not provide long running functions, which could slow down the replicator. Nor make assumptions about the thread the function is being called on. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------- |

#### [](#pull-filter)Pull Filter

The pull filter gives an app the ability to validate documents being pulled, and skip ones that fail. This is an important security mechanism in a peer-to-peer topology with peers that are not fully trusted.

> [!NOTE]
> Pull replication filters are not a substitute for channels. Sync Gateway [channels](../../../sync-gateway/current/access-control/channels.md)are designed to be scalable (documents are filtered on the server) whereas a pull replication filter is applied to a document once it has been downloaded.

```c
// Purpose -- illustrate a simple replication filter function
static bool simpleReplicationFilter(void* context,
                                    CBLDocument* argDoc,
                                    CBLDocumentFlags argFlags)
{
    bool result = (argFlags == kCBLDocumentFlagsDeleted);
    return result;
}

    // Purpose - Illustrate use of push and-or pull filter functions

    // NOTE: Push and pull filters are set per collection
    collectionConfig.pushFilter = simpleReplicationFilter;
    collectionConfig.pullFilter = simpleReplicationFilter;
```

| **1** | Do not provide long running functions, which could slow down the replicator. Nor make assumptions about the thread the function is being called on. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------- |

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

Auto-purge behavior is controlled primarily by the ReplicationConfiguration option [disableAutoPurge](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#a3795c0097264ccd1ed612d9a0746d58d). Changing the state of this will impact **only** future replications; the replicator will not attempt to sync revisions that were auto purged on channel access removal. Clients wishing to sync previously removed documents must use the resetCheckpoint API to resync from the start.

Example 9\. Setting auto-purge

```c

```

| **1** | Here we have opted to turn off the auto purge behavior. By default auto purge is enabled. |
| ----- | ----------------------------------------------------------------------------------------- |

#### [](#overrides)Overrides

Where necessary, clients can override the default auto-purge behavior. This can be done either by setting [disableAutoPurge](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#a3795c0097264ccd1ed612d9a0746d58d) to false, or for finer control by applying pull-filters — see: [Table 4](#tbl-pull-filters) and [Replication Filters](#lbl-repl-fltrs)This ensures backwards compatible with 2.8 clients that use pull filters to prevent auto purge of removed docs.

__Table 4\. Impact of Pull-Filters__
| purge\_on\_removal setting | Pull Filter                                                                                         |                               |
| -------------------------- | --------------------------------------------------------------------------------------------------- | ----------------------------- |
| Not Defined                | Defined to filter removals/revoked docs                                                             |                               |
| disabled                   | Doc remains in local database App notified of "accessRemoved" if a _Documentlistener_ is registered |                               |
| enabled (DEFAULT)          | Doc is auto purged App notified of "accessRemoved" if _Documentlistener_ registered                 | Doc remains in local database |

### [](#lbl-repl-delta)Delta Sync

> [!IMPORTANT]
> This is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature.

With Delta Sync \[[1](#%5Ffootnotedef%5F1 "View footnote.")\], only the changed parts of a Couchbase document are replicated. This can result in significant savings in bandwidth consumption as well as throughput improvements, especially when network bandwidth is typically constrained.

Replications to a Server (for example, a Sync Gateway, or passive listener) automatically use delta sync if the property is enabled at database level by the server — see: [databases.$db.delta\_sync.enabled](../../../sync-gateway/current/configuration/configuration-properties-legacy.md#databases-foo%5Fdb-delta%5Fsync).

[Intra-Device](dbreplica.md)replications automatically **disable** delta sync, whilst [Peer-to-Peer](#p2psync-websocket.adoc)replications automatically **enable** delta sync.

## [](#lbl-init-repl)Initialize

In this section

[Start Replicator](#lbl-repl-start) | [Checkpoint Starts](#lbl-repl-ckpt)

### [](#lbl-repl-start)Start Replicator

Use the `[Replication](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5Freplication.html)` class's [initWith(config:)](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5Freplication.html#%28im%29initWithConfig:) constructor, to initialize the replicator with the configuration you have defined. You can, optionally, add a change listener (see [Monitor](#lbl-repl-mon)) before starting the replicator running using [CBLReplicator\_Start()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga224926daa794a424c470bf86dd57aaf9).

Example 10\. Initialize and run replicator

```c
CBLReplicator* replicator =
CBLReplicator_Create(&argConfig, &err); (1)
  CBLReplicator_Start(replicator, false); (2)
```

| **1** | Initialize the replicator with the configuration |
| ----- | ------------------------------------------------ |
| **2** | Start the replicator                             |

### [](#lbl-repl-ckpt)Checkpoint Starts

Replicators use [checkpoints](refer-glossary.md#checkpoint) to keep track of documents sent to the target database.

Without [checkpoints](refer-glossary.md#checkpoint), Couchbase Lite would replicate the entire database content to the target database on each connection, even though previous replications may already have replicated some or all of that content.

This functionality is generally not a concern to application developers. However, if you do want to force the replication to start again from zero, use the [checkpoint](refer-glossary.md#checkpoint) reset argument when starting the replicator — as shown in [Example 11](#ex-repl-ckpt).

Example 11\. Resetting checkpoints

```c
CBLReplicator_Start(replicator, true); (1)
```

| **1** | Set start's reset option to true. |
| ----- | --------------------------------- |

## [](#lbl-repl-mon)Monitor

In this section

[Change Listeners](#lbl-repl-chng) | [Replicator Status](#lbl-repl-status) | [Monitor Document Changes](#lbl-repl-evnts) | [Documents Pending Push](#lbl-repl-pend)

You can monitor a replication's status by using a combination of [Change Listeners](#lbl-repl-chng) and the `replication.status.activity` property — see; [CBLReplicatorActivityLevel enum](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga9421513c63f1d16bf4740c4d2515dd22). This enables you to know, for example, when the replication is actively transferring data and when it has stopped.

You can also choose to monitor document changes — see: [Monitor Document Changes](#lbl-repl-evnts).

### [](#lbl-repl-chng)Change Listeners

Use this to monitor changes and to inform on sync progress; this is an optional step. You can add and a replicator change listener at any point; it will report changes from the point it is registered.

> [!TIP]
> Best Practice
> 
> Don't forget to save the token so you can remove the listener later

Use the [Replication](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5Freplication.html) class to add a change listener as a callback to the Replicator ([addChangeListener(\_:)](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5Freplication.html#%28im%29addChangeListener:)) — see: [Example 12](#ex-repl-mon). You will then be asynchronously notified of state changes.

You can remove a change listener with [removeChangeListenerWithToken(ListenerToken:)](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5Freplication.html#%28im%29removeChangeListenerWithToken).

### [](#lbl-repl-status)Replicator Status

You can use the [CBLReplicatorStatus](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fstatus.html) struct to check the replicator status. That is, whether it is actively transferring data or if it has stopped — see: [Example 12](#ex-repl-mon).

The returned _ReplicationStatus_ structure comprises:

* [CBLReplicatorActivityLevel enum](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga9421513c63f1d16bf4740c4d2515dd22) — stopped, offline, connecting, idle or busy — see states described in: [Table 5](#tbl-states)
* [CBLReplicatorProgress struct](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fprogress.html%29)

  * completed — the total number of changes completed
  * total — the total number of changes to be processed
* [CBLError struct](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Ferror.html) — the current error, if any

Example 12\. Monitor replication

* Adding a Change Listener
* Using replicator.status

```c
// Purpose -- illustrate a simple change listener
static void simpleChangeListener(void* context,
                                 CBLReplicator* repl,
                                 const CBLReplicatorStatus* status)
{
     if(status->error.code != 0) {
         printf("Error %d / %d\n",
                status->error.domain,
                status->error.code);
     }
}
    // Purpose -- illustrate addition of a Replicator change listener
    CBLListenerToken* token_ReplChangeListener =
        CBLReplicator_AddChangeListener(replicator,
        simpleChangeListener,
        NULL); (1)
```

```c
// Purpose -- illustrate use of CBLReplicator_Status()
CBLReplicatorStatus thisState = CBLReplicator_Status(replicator);
if(thisState.activity==kCBLReplicatorStopped) {
    if(thisState.error.code==0) {
        CBLReplicator_Start(replicator,false);
    } else {
        printf("Replicator stopped -- code %d", thisState.error.code);
        // ... handle error ...
        CBLReplicator_Release(replicator);
    }
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

### [](#lbl-repl-evnts)Monitor Document Changes

You can choose to register for document updates during a replication.

For example, the code snippet in [Example 13](#ex-reg-doc-listener) registers a listener to monitor document replication performed by the replicator referenced by the variable `replicator`. It prints the document ID of each document received and sent. Stop the listener as shown in [Example 14](#ex-stop-doc-listener).

Example 13\. Register a document listener

```c
// Purpose -- illustrate addition of a Document Replicator  listener
CBLListenerToken* token_ReplDocListener =
    CBLReplicator_AddDocumentReplicationListener(
        replicator,
        SimpleReplicationDocumentListener,
        context); (1)
```

Example 14\. Stop document listener

This code snippet shows how to stop the document listener using the token from the previous example.

```c
// Purpose -- illustrate removal of a listener
CBLListener_Remove(token_ReplDocListener);
CBLListener_Remove(token_ReplChangeListener);
```

#### [](#document-access-removal-behavior)Document Access Removal Behavior

When access to a document is removed on Sync Gateway (see: Sync Gateway's [Sync Function](../../../sync-gateway/current/access-control/sync-function/sync-function-api.md)), the document replication listener sends a notification with the `AccessRemoved` flag set to `true` and subsequently purges the document from the database.

### [](#lbl-repl-pend)Documents Pending Push

> [!TIP]
> [CBLReplicator.isDocumentPending()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga493eeac915dd54a274b907a010664a2e) is quicker and more efficient. Use it in preference to returning a list of pending document IDs, where possible.

You can check whether documents are waiting to be pushed in any forthcoming sync by using either of the following API methods:

* Use the [CBLReplicator\_PendingDocumentIDs()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga6e9902ae56d5fec0fc19b29c28f1828f) method, which returns a list of document IDs that have local changes, but which have not yet been pushed to the server.  
This can be very useful in tracking the progress of a push sync, enabling the app to provide a visual indicator to the end user on its status, or decide when it is safe to exit.
* Use the [CBLReplicator.isDocumentPending()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga493eeac915dd54a274b907a010664a2e) method to quickly check whether an individual document is pending a push.

Example 15\. Use Pending Document ID API

```c
FLDict thisPendingIdList =
    CBLReplicator_PendingDocumentIDs2(replicator, collection, &err); (1)
if(!FLDict_IsEmpty(thisPendingIdList)) {
    FLDictIterator item;
    FLDictIterator_Begin(thisPendingIdList, &item);
    FLValue itemValue;
    FLString pendingId;
    while(NULL != (itemValue = FLDictIterator_GetValue(&item))) {
        pendingId = FLValue_AsString(itemValue);
        if(CBLReplicator_IsDocumentPending2(replicator,
            pendingId,
            collection,
            &err)) { (2)
            // ... process the still pending docid as required (3)
        } else {
            // Doc Id no longer pending
            if(err.code==0) {
                // No fail so must have already been pushed
                printf("Document already pushed");
            } else {
                // Error detected so handle it
                printf("Error code %d checking for pendingId", err.code);
                break;
            }
        }
        FLDictIterator_Next(&item);
    }
    FLDictIterator_End(&item);
    FLValue_Release(itemValue);
} else {
    printf("No Pending Id Docs to process");
}
FLDict_Release(thisPendingIdList);
```

| **1** | [CBLReplicator\_PendingDocumentIDs()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga6e9902ae56d5fec0fc19b29c28f1828f) returns a list of the document IDs for all documents waiting to be pushed. This is a snapshot and may have changed by the time the response is received and processed. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [CBLReplicator.isDocumentPending()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga493eeac915dd54a274b907a010664a2e) returns true if the document is waiting to be pushed, and false otherwise.                                                                                               |

## [](#lbl-repl-stop)Stop

Stopping a replication is straightforward. It is done using [CBLReplicator\_Stop()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga548ce284032009546d4092745e89fa8e). This initiates an asynchronous operation and so is not necessarily immediate. Your app should account for this potential delay before attempting any subsequent operations.

You can find further information on database operations in [Databases](database.md).

Example 16\. Stop replicator

```c
// Purpose -- show how to stop a replication
if(CBLReplicator_Status(argRepl).activity!=kCBLReplicatorStopped) {
    CBLReplicator_Stop(argRepl);
}
```

| **1** | Here we initiate the stopping of the replication using the [CBLReplicator\_Stop()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga548ce284032009546d4092745e89fa8e) method. It will stop any active [change listener](#lbl-repl-chng) once the replication is stopped. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#lbl-nwk-errs)Error Handling

When _replicator_ detects a network error it updates its status depending on the error type (permanent or temporary) and returns an appropriate HTTP error code.

The following code snippet adds a `Change Listener`, which monitors a replication for errors and logs the the returned error code.

Example 17\. Monitoring for network errors

```c
// Purpose -- illustrate a simple change listener
static void simpleChangeListener(void* context,
                                 CBLReplicator* repl,
                                 const CBLReplicatorStatus* status)
{
     if(status->error.code != 0) {
         printf("Error %d / %d\n",
                status->error.domain,
                status->error.code);
     }
}
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

## [](#load-balancers)Load Balancers

Couchbase Lite \[[2](#%5Ffootnotedef%5F2 "View footnote.")\] uses WebSockets as the communication protocol to transmit data. Some load balancers are not configured for WebSocket connections by default (NGINX for example); so it might be necessary to explicitly enable them in the load balancer's configuration (see [Load Balancers](../../../sync-gateway/current/deploy/load-balancer.md)).

By default, the WebSocket protocol uses compression to optimize for speed and bandwidth utilization. The level of compression is set on Sync Gateway and can be tuned in the configuration file ([replicator\_compression](../../../sync-gateway/current/configuration/configuration-properties-legacy.md#replicator%5Fcompression)).

## [](#lbl-cert-pinning)Certificate Pinning

Couchbase Lite for C supports certificate pinning.

Certificate pinning is a technique that can be used by applications to "pin" a host to its certificate. The certificate is typically delivered to the client by an out-of-band channel and bundled with the client. In this case, Couchbase Lite uses this embedded certificate to verify the trustworthiness of the server (for example, a Sync Gateway) and no longer needs to rely on a trusted third party for that (commonly referred to as the Certificate Authority).

Couchbase Lite 3.0.2

For the 3.02\. release, changes have been made to the way certificates on the host are matched:

| Prior to CBL3.0.2 | The pinned certificate was only compared with the leaf certificate of the host. This is not always suitable as leaf certificates are usually valid for shorter periods of time. |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CBL-3.0.2+        | The pinned certificate will be compared against any certificate in the server's certificate chain.                                                                              |

The following steps describe how to configure certificate pinning between Couchbase Lite and Sync Gateway.

1. [Create your own self-signed certificate](../../../sync-gateway/current/security/authentication-certs.md#creating-your-own-self-signed-certificate)with the `openssl` command. After completing this step, you should have 3 files: `cert.pem`, `cert.cer` and `privkey.pem`.
2. [Configure Sync Gateway](../../../sync-gateway/current/security/authentication-certs.md#installing-the-certificate)with the `cert.pem` and `privkey.pem` files. After completing this step, Sync Gateway is reachable over `https`/`wss`.
3. On the Couchbase Lite side, the replication must point to a URL with the `wss` scheme and configured with the `cert.cer` file created in step 1.  
This example loads the certificate from the application sandbox, then converts it to the appropriate type to configure the replication object.

Example 18\. Cert Pinnings

```c
char cert_buf[10000];
FILE* cert_file = fopen("cert.pem", "r");
size_t read = fread(cert_buf, 1, sizeof(cert_buf), cert_file);
replConfig.pinnedServerCertificate = (FLSlice){cert_buf, read};
```

1. Build and run your app. The replication should now run successfully over https/wss with certificate pinning.

For more on pinning certificates see the blog entry: [Certificate Pinning with Couchbase Mobile](https://blog.couchbase.com/certificate-pinning-android-with-couchbase-mobile/)

### [](#authentication-errors)Authentication Errors

If Sync Gateway is configured with a self signed certificate but your app points to a `ws` scheme instead of `wss` you will encounter an error with status code `11006` — see: [Example 19](#ex-11006)

Example 19\. Protocol Mismatch

```console
CouchbaseLite Replicator ERROR: {Repl#2} Got LiteCore error: WebSocket error 1006 "connection closed abnormally"
```

If Sync Gateway is configured with a self signed certificate, and your app points to a `wss` scheme but the replicator configuration isn't using the certificate you'll encounter an error with status code `5011` — see: [Example 20](#ex-5011)

Example 20\. Certificate Mismatch or Not Found

```text
CouchbaseLite Replicator ERROR: {Repl#2} Got LiteCore error: Network error 11 "server TLS certificate is self-signed or has unknown root cert"
```

## [](#related-content)Related Content

###### [](#)

How to . . .

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

[1](#%5Ffootnoteref%5F1). Couchbase Mobile 2.5+ 

[2](#%5Ffootnoteref%5F2). From 2.0