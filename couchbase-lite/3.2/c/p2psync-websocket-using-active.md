---
title: Active Peer
description: Couchbase Lite's Peer-to-Peer Synchronization enables edge devices
  to synchronize securely without consuming centralized cloud-server resources
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.2/modules/c/pages/p2psync-websocket-using-active.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:3.2@couchbase-lite:c:p2psync-websocket-using-active.adoc[]
---

[View original HTML](/couchbase-lite/3.2/c/p2psync-websocket-using-active.html)

# Active Peer

> Description — _Couchbase Lite’s Peer-to-Peer Synchronization enables edge devices to synchronize securely without consuming centralized cloud-server resources_  
> _Abstract — How to set up a Replicator to connect with a Listener and replicate changes using peer-to-peer sync_  
> Related Content — [API Reference](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html) | [Passive Peer](p2psync-websocket-using-passive.md) | [Active Peer](p2psync-websocket-using-active.md)

> [!NOTE]
> Code Snippets
> 
> All code examples are indicative only. They demonstrate the basic concepts and approaches to using a feature. Use them as inspiration and adapt these examples to best practice when developing applications for your platform.

## [](#introduction)Introduction

This content provides sample code and configuration examples covering the implementation of [Peer-to-Peer Sync](refer-glossary.md#peer-to-peer-sync) over WebSockets. Specifically it covers the implementation of an [Active Peer](refer-glossary.md#active-peer).

This _active peer_ (also referred to as a client and-or a replicator) will initiate the connection with a [Passive Peer](refer-glossary.md#passive-peer) (also referred to as a server and-or listener) and participate in the replication of database changes to bring both databases into sync.

Subsequent sections provide additional details and examples for the main configuration options.

> [!NOTE]
> Secure Storage
> 
> The use of TLS, its associated keys and certificates requires using secure storage to minimize the chances of a security breach. The implementation of this storage differs from platform to platform — see [Using secure storage](p2psync-websocket.md#using-secure-storage).

## [](#configuration-summary)Configuration Summary

You should configure and initialize a replicator for each Couchbase Lite database instance you want to sync. [Example 1](#simple-replication-to-listener) shows the initialization and configuration process.

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
    FLString url = FLSTR("wss://localhost:4984/db");
    CBLEndpoint* target = CBLEndpoint_CreateWithURL(url, &err); (1)

    CBLReplicationCollection collectionConfig;
    memset(&collectionConfig, 0, sizeof(CBLReplicationCollection));
    collectionConfig.collection = collection;

    CBLReplicatorConfiguration replConfig;
    memset(&replConfig, 0, sizeof(CBLReplicatorConfiguration));
    replConfig.collectionCount = 1;
    replConfig.collections = &collectionConfig;
    replConfig.endpoint = target;

    // Set replication direction and mode
    replConfig.replicatorType = kCBLReplicatorTypePull;
    replConfig.continuous = true;


    // Optionally, configure Client Authentication
    // Here we are using to Basic Authentication,
    // Providing username and password credentials
    CBLAuthenticator* basicAuth =
        CBLAuth_CreatePassword(FLSTR("username"),
                               FLSTR("passwd")); (2)
    replConfig.authenticator = basicAuth;

    // Optionally, configure how we handle conflicts (note that this is set
    // per collection, and not on the overall replicator)
    collectionConfig.conflictResolver = simpleConflictResolver_localWins; (3)

    // Initialize replicator with created config
    CBLReplicator* replicator =
        CBLReplicator_Create(&replConfig, &err); (4)

    CBLEndpoint_Free(target);

    // Optionally, add change listener
    CBLListenerToken* token =
            CBLReplicator_AddChangeListener(replicator,
                                            simpleChangeListener,
                                            NULL); (5)

    // Start replication
    CBLReplicator_Start(replicator, false); (6)
```

| **1** | Configure the URL endpoint of the server. Here we connect only to servers presenting a self-signed certificate. By default, clients accept only servers presenting certificates that can be verified using the OS bundled Root CA Certificates — see: [Authenticating the Listener](#authenticate-listener). |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | Configure the credentials the client will present to the server. Here we say to provide _Basic Authentication_ credentials. Other options are available — see: [Client Authentication](#lbl-authclnt).                                                                                                       |
| **3** | Configure how the replication should perform [Conflict Resolution](#conflict-resolution).                                                                                                                                                                                                                    |
| **4** | Initialize the replicator using your configuration object.                                                                                                                                                                                                                                                   |
| **5** | Register an observer, which will notify you of changes to the replication status.                                                                                                                                                                                                                            |
| **6** | Start the replicator.                                                                                                                                                                                                                                                                                        |

## [](#api-references)API References

You can find [C API References](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html) here.

## [](#device-discovery)Device Discovery

**This phase is optional:** If the listener is initialized on a well known URL endpoint (for example, a static IP Address or well known DNS address) then you can configure Active Peers to connect to those.

Prior to connecting with a listener you may execute a Peer discovery phase to dynamically discover Peers.

## [](#configure-replicator)Configure Replicator

### [](#lbl-cfg-tgt)Configure Target

Initialize and define the replication configuration with local and remote database locations using the [CBLReplicatorConfiguration](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html) object.

The constructor provides:

* the name of the local database to be sync’d
* the server’s URL (including the port number and the name of the remote database to sync with)  
It is expected that the app will identify the IP address and URL and append the remote database name to the URL endpoint, producing for example: `wss://10.0.2.2:4984/travel-sample`  
The URL scheme for web socket URLs uses `ws:` (non-TLS) or `wss:` (SSL/TLS) prefixes.

Example 2\. Add Target to Configuration

```c
// Initialize the configuration object and set db target
CBLError err{};
FLString url = FLSTR("ws://localhost:4984/db");
CBLEndpoint* target =
    CBLEndpoint_CreateWithURL(url, &err); (1)

CBLReplicationCollection collectionConfig;
memset(&collectionConfig, 0, sizeof(CBLReplicationCollection));
collectionConfig.collection = collection;

CBLReplicatorConfiguration replConfig;
memset(&replConfig, 0, sizeof(CBLReplicatorConfiguration));
replConfig.collectionCount = 1;
replConfig.collections = &collectionConfig;
replConfig.endpoint = target; (2)
```

Note use of the scheme prefix: `ws://`, or `wss://`to ensure TLS encryption — strongly recommended in production.

### [](#lbl-cfg-sync)Sync Mode

Here we define the direction and type of replication we want to initiate.

We use `[CBLReplicatorConfiguration](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html)` class’s [replicatorType](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#a40f3195389ab0578aa17e63dd832a390) and [continuous](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#a3d17159fc65a7491c2cde2f56a5016df) parameters, to tell the replicator:

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

### [](#lbl-cfg-retry)Retry Configuration

Couchbase Lite for C’s replication retry logic assures a resilient connection.

The replicator minimizes the chance and impact of dropped connections by maintaining a heartbeat; essentially pinging the listener at a configurable interval to ensure the connection remains alive.

In the event it detects a transient error, the replicator will attempt to reconnect, stopping only when the connection is re-established, or the number of retries exceeds the retry limit (9 times for a single-shot replication and unlimited for a continuous replication).

On each retry the interval between attempts is increased exponentially (exponential backoff) up to the maximum wait time limit (5 minutes).

The REST API provides configurable control over this replication retry logic using a set of configurable properties — see: [Table 1](#tbl-repl-retry).

__Table 1\. Replication Retry Configuration Properties__
| Property                                                                                                                                                                     | Use cases                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [heartbeat](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#a524408f9430d13c783762dce32f1126e)          | Reduce to detect connection errors sooner Align to load-balancer or proxy keep-alive interval — see Sync Gateway’s topic [Load Balancer - Keep Alive](../../../sync-gateway/current/deploy/load-balancer.md#websocket-connection) | The interval (in seconds) between the heartbeat pulses. Default: The replicator pings the listener every 300 seconds.                                                                                                                                                                                                                                                                                                                                                                             |
| [maxAttempts](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#a5b6435c711d93f71566d8814506e0dff)        | Change this to limit or extend the number of retry attempts.                                                                                                                                                                      | The maximum number of retry attempts Set to zero (0) to use default values Set to zero (1) to prevent any retry attempt The retry attempt count is reset when the replicator is able to connect and replicate Default values are: Single-shot replication = 9; Continuous replication = maximum integer value Negative values generate a Couchbase exception InvalidArgumentException                                                                                                             |
| [maxAttemptWaitTime](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#a21d4fffd270c721d1600d7a835f17fd1) | Change this to adjust the interval between retries.                                                                                                                                                                               | The maximum interval between retry attempts While you can configure the **maximum permitted** wait time, the replicator’s exponential backoff algorithm calculates each individual interval which is not configurable. Default value: 300 seconds (5 minutes) Zero sets the maximum interval between retries to the default of 300 seconds 300 sets the maximum interval between retries to the default of 300 seconds A negative value generates a Couchbase exception, InvalidArgumentException |

When necessary you can adjust any or all of those configurable values — see: [Example 4](#ex-repl-retry) for how to do this.

Example 4\. Configuring Replication Retries

```c
// Configure replication retries
replConfig.heartbeat = 120; //  (1)

replConfig.maxAttempts = 20; //  (2)

replConfig.maxAttemptWaitTime = 600; //  (3)
```

| **1** | Here we use [heartbeat](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#a524408f9430d13c783762dce32f1126e) to set the required interval (in seconds) between the heartbeat pulses. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Here we use [maxAttempts](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#a5b6435c711d93f71566d8814506e0dff) to set the required number of retry attempts.                         |
| **3** | Here we use [maxAttemptWaitTime](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#a21d4fffd270c721d1600d7a835f17fd1) to set the required interval between retry attempts.           |

### [](#authenticate-listener)Authenticating the Listener

Define the credentials that your app (the client) is expecting to receive from the server (listener) in order to ensure that the server is one it is prepared to interact with.

Note that the client cannot authenticate the server if TLS is turned off. When TLS is enabled (Sync Gateway’s default) the client _must_ authenticate the server. If the server cannot provide acceptable credentials then the connection will fail.

Use the `[CBLReplicatorConfiguration](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html)` properties [acceptOnlySelfSignedServerCertificate](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#ad1a35fd126871670d2677cabff87f2c3) and [pinnedServerCertificate()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#a4a96fb9fba93dc93f8373b76c3816af6), to tell the replicator how to verify server-supplied TLS server certificates.

* If there is a pinned certificate, nothing else matters, the server cert must **exactly** match the pinned certificate.
* If there are no pinned certs and [acceptOnlySelfSignedServerCertificate](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#ad1a35fd126871670d2677cabff87f2c3) is `true` then any self-signed certificate is accepted. Certificates that are not self signed are rejected, no matter who signed them.
* If there are no pinned certificates and [acceptOnlySelfSignedServerCertificate](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#ad1a35fd126871670d2677cabff87f2c3) is `false` (default), the client validates the server’s certificates against the system CA certificates. The server must supply a chain of certificates whose root is signed by one of the certificates in the system CA bundle.

Example 5\. Set Server TLS security

* CA Cert
* Self Signed Cert
* Pinned Certificate

Set the client to expect and accept only CA attested certificates.

```c
// Configure Server Security -- only accept CA Certs
config.acceptOnlySelfSignedServerCertificate = false;
```

This is the default. Only certificate chains with roots signed by a trusted CA are allowed. Self signed certificates are not allowed.

Set the client to expect and accept only self-signed certificates

```c
// Accept self-signed certificates, for testing purposes only:
replConfig.acceptOnlySelfSignedServerCertificate = true;
```

Set this to `true` to accept any self signed cert. Any certificates that are not self-signed are rejected.

Set the client to expect and accept only a pinned certificate.

```c
// Return the remote pinned cert (the listener's cert)
config.pinnedServerCertificate = certSlice; // Get listener cert if pinned
```

### [](#lbl-authclnt)Client Authentication

Here we define the credentials that the client can present to the server if prompted to do so in order that the server can authenticate it.

We use [CBLReplicatorConfiguration](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html)'s [authenticator](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#aa2cd20835cc4e6b516510d441d419d60) method to define the authentication method to the replicator.

For P2P using URLEndpointListener, the replicator supports two types of authentication:

* Basic Authentication — doesn’t require TLS
* Client Certificate Authentication — requires TLS

## [](#initialize-replicator)Initialize Replicator

Use the `[Replication](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/group%5F%5Freplication.html)` class’s [CBLReplicator\_Create()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga5f5ffc039ce0ac834d1f1f4cd940d65d) constructor, to initialize the replicator with the configuration you have defined. You can, optionally, add a change listener (see [Monitor Sync](#lbl-repl-mon)) before starting the replicator running using [CBLReplicator\_Start()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga224926daa794a424c470bf86dd57aaf9).

Example 6\. Initialize and run replicator

```c
CBLReplicator* replicator =
CBLReplicator_Create(&argConfig, &err); (1)
  CBLReplicator_Start(replicator, false); (2)
```

| **1** | Initialize the replicator with the configuration |
| ----- | ------------------------------------------------ |
| **2** | Start the replicator                             |

## [](#lbl-repl-mon)Monitor Sync

You can monitor a replication’s status by using a combination of [Change Listeners](#lbl-repl-chng) and the `replication.status.activity` property — see; [CBLReplicatorActivityLevel enum](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga9421513c63f1d16bf4740c4d2515dd22). This enables you to know, for example, when the replication is actively transferring data and when it has stopped.

### [](#lbl-repl-chng)Change Listeners

Use this to monitor changes and to inform on sync progress; this is an optional step. You can add and a replicator change listener at any point; it will report changes from the point it is registered.

> [!TIP]
> Best Practice
> 
> Don’t forget to save the token so you can remove the listener later

Use the [Replication](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/group%5F%5Freplication.html) class to add a change listener as a callback to the Replicator ([CBLReplicator\_AddChangeListener()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/group%5F%5Freplication.html#gaa49518d403aaa95f9b342759e0e30769)) — see: [Example 7](#ex-repl-mon). You will then be asynchronously notified of state changes.

### [](#lbl-repl-status)Replicator Status

You can use the [CBLReplicatorStatus](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fstatus.html) struct to check the replicator status. That is, whether it is actively transferring data or if it has stopped — see: [Example 7](#ex-repl-mon).

The returned _ReplicationStatus_ structure comprises:

* [CBLReplicatorActivityLevel enum](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga9421513c63f1d16bf4740c4d2515dd22) — stopped, offline, connecting, idle or busy — see states described in: [Table 2](#tbl-states)
* [CBLReplicatorProgress struct](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fprogress.html)

  * completed — the total number of changes completed
  * total — the total number of changes to be processed
* [CBLError struct](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Ferror.html) — the current error, if any

Example 7\. Monitor replication

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
                                            NULL);
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

### [](#lbl-repl-states)Replication States

[Table 2](#tbl-states) shows the different states, or activity levels, reported in the API; and the meaning of each.

__Table 2\. Replicator activity levels__
| State      | Meaning                                                                                                                           |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------- |
| STOPPED    | The replication is finished or hit a fatal error.                                                                                 |
| OFFLINE    | The replicator is offline as the remote host is unreachable.                                                                      |
| CONNECTING | The replicator is connecting to the remote host.                                                                                  |
| IDLE       | The replication caught up with all the changes available from the server. The IDLE state is only used in continuous replications. |
| BUSY       | The replication is actively transferring data.                                                                                    |

> [!NOTE]
> The replication change object also has properties to track the progress (`change.status.completed` and `change.status.total`). Since the replication occurs in batches the total count can vary through the course of a replication.

### [](#lbl-repl-pend)Documents Pending Push

> [!TIP]
> [CBLReplicator\_IsDocumentPending()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga493eeac915dd54a274b907a010664a2e) is quicker and more efficient. Use it in preference to returning a list of pending document IDs, where possible.

You can check whether documents are waiting to be pushed in any forthcoming sync by using either of the following API methods:

* Use the [CBLReplicator\_PendingDocumentIDs()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga6e9902ae56d5fec0fc19b29c28f1828f) method, which returns a list of document IDs that have local changes, but which have not yet been pushed to the server.  
This can be very useful in tracking the progress of a push sync, enabling the app to provide a visual indicator to the end user on its status, or decide when it is safe to exit.
* Use the [CBLReplicator\_IsDocumentPending()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga493eeac915dd54a274b907a010664a2e) method to quickly check whether an individual document is pending a push.

Example 8\. Use Pending Document ID API

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
                                           &err)) {
            // ... process the still pending docid as required (2)
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

| **1** | [CBLReplicator\_PendingDocumentIDs()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga6e9902ae56d5fec0fc19b29c28f1828f) returns a list of the document IDs for all documents waiting to be pushed. This is a snapshot and may have changed by the time the response is received and processed. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [CBLReplicator\_IsDocumentPending()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga493eeac915dd54a274b907a010664a2e) returns true if the document is waiting to be pushed, and false otherwise.                                                                                              |

## [](#lbl-repl-stop)Stop Sync

Stopping a replication is straightforward. It is done using [CBLReplicator\_Stop()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga548ce284032009546d4092745e89fa8e). This initiates an asynchronous operation and so is not necessarily immediate. Your app should account for this potential delay before attempting any subsequent operations.

You can find further information on database operations in [Databases](database.md).

Example 9\. Stop replicator

```c
// Purpose -- show how to stop a replication
if(CBLReplicator_Status(argRepl).activity!=kCBLReplicatorStopped) {
    CBLReplicator_Stop(argRepl);
}
```

Here we initiate the stopping of the replication using the [CBLReplicator\_Stop()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/group%5F%5Freplication.html#ga548ce284032009546d4092745e89fa8e) method. It will stop any active [change listener](#lbl-repl-chng) once the replication is stopped.

## [](#conflict-resolution)Conflict Resolution

Unless you specify otherwise, Couchbase Lite’s default conflict resolution policy is applied — see [Handling Data Conflicts](conflict.md).

To use a different policy, specify a _conflict resolver_ using [conflictResolver](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Freplicator%5Fconfiguration.html#aa664454f386c8300dd458ece30a3a8c6) as shown in [Example 10](#using-conflict-resolvers).

For more complex solutions you can provide a custom conflict resolver - see: [Handling Data Conflicts](conflict.md).

Example 10\. Using conflict resolvers

* Local Wins
* Remote Wins
* Merge

```c
static const CBLDocument* local_win_conflict_resolver(void* context,
                                                      FLString documentID,
                                                      const CBLDocument* localDocument,
                                                      const CBLDocument* remoteDocument)
{
    return localDocument;
}
```

```c
static const CBLDocument* remote_win_conflict_resolver(void* context,
                                                       FLString documentID,
                                                       const CBLDocument* localDocument,
                                                       const CBLDocument* remoteDocument)
{
    return remoteDocument;
}
```

```c
static const CBLDocument* merge_conflict_resolver(void* context,
                                                  FLString documentID,
                                                  const CBLDocument* localDocument,
                                                  const CBLDocument* remoteDocument)
{
    FLDict localProps = CBLDocument_Properties(localDocument);
    FLDict remoteProps = CBLDocument_Properties(remoteDocument);
    FLMutableDict mergeProps = FLDict_MutableCopy(localProps, kFLDefaultCopy);

    FLDictIterator d;
    FLDictIterator_Begin(localProps, &d);
    FLValue value;
    while((value = FLDictIterator_GetValue(&d))) {
        FLString key = FLDictIterator_GetKeyString(&d);
        if(FLDict_Get(mergeProps, key)) {
            continue;
        }

        FLMutableDict_SetValue(mergeProps, key, value);
        FLDictIterator_Next(&d);
    }

    CBLDocument* mergeDocument = CBLDocument_CreateWithID(documentID);
    CBLDocument_SetProperties(mergeDocument, mergeProps);
    FLMutableDict_Release(mergeProps);

    return mergeDocument;
}
```

Just as a replicator may observe a conflict — when updating a document that has changed both in the local database and in a remote database — any attempt to save a document may also observe a conflict, if a replication has taken place since the local app retrieved the document from the database. To address that possibility, a version of the `Database.save()` method also takes a conflict resolver as shown in [Example 11](#ex-merge-props).

The following code snippet shows an example of merging properties from the existing document (`current`) into the one being saved (`new`). In the event of conflicting keys, it will pick the key value from `new`.

Example 11\. Merging document properties

```c
CBLDatabase* database = kDatabase;
CBLCollection* collection = CBLDatabase_DefaultCollection(database, NULL);
CBLError err{};

CBLDocument* mutableDoc = CBLCollection_GetMutableDocument(collection, FLSTR("xyz"), &err);
FLMutableDict properties = CBLDocument_MutableProperties(mutableDoc);
FLMutableDict_SetString(properties, FLSTR("name"), FLSTR("apples"));

/*
static bool custom_conflict_handler(void* context, CBLDocument* documentBeingSaved,
    const CBLDocument* conflictingDocument) {
    FLDict currentProps = CBLDocument_Properties(conflictingDocument);
    FLDict updatedProps = CBLDocument_Properties(documentBeingSaved);
    FLMutableDict newProps = FLDict_MutableCopy(updatedProps, kFLDefaultCopy);

    FLDictIterator d;
    FLDictIterator_Begin(currentProps, &d);
    FLSlice currentKey = FLDictIterator_GetKeyString(&d);
    for(; currentKey.buf; currentKey = FLDictIterator_GetKeyString(&d)) {
        if(FLDict_Get(newProps, currentKey)) {
            continue;
        }

        FLValue currentValue = FLDictIterator_GetValue(&d);
        FLMutableDict_SetValue(newProps, currentKey, currentValue);
    }

    return true;
}
*/
CBLCollection_SaveDocumentWithConflictHandler(collection, mutableDoc, custom_conflict_handler, NULL, &err);
```

For more on replicator conflict resolution see: [Handling Data Conflicts](conflict.md).

## [](#delta-sync)Delta Sync

If delta sync is enabled on the listener, then replication will use delta sync.

## [](#related-content)Related Content

### [](#)

How to

* [Passive Peer](p2psync-websocket-using-passive.md)
* [Active Peer](p2psync-websocket-using-active.md)

### [](#-2)

Concepts

* [Peer-to-Peer Sync](p2psync-websocket.md)
* [API References](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html)

### [](#-3)

Community Resources …​

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

[Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)