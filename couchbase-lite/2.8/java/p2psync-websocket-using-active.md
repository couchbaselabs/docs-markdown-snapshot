---
title: Active Peer
description: Couchbase Lite's Peer-to-Peer Synchronization enables edge devices
  to synchronize securely without consuming centralized cloud-server resources
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/java/pages/p2psync-websocket-using-active.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@couchbase-lite:java:p2psync-websocket-using-active.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/java/p2psync-websocket-using-active.html)

# Active Peer

> Description — _Couchbase Lite's Peer-to-Peer Synchronization enables edge devices to synchronize securely without consuming centralized cloud-server resources_  
> _Abstract — How to set up a Replicator to connect with a Listener and replicate changes using peer-to-peer sync_  
> Related Content — [API Reference](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?) | [Passive Peer](../../current/java/p2psync-websocket-using-passive.md) | [Active Peer](../../current/java/p2psync-websocket-using-active.md)

> [!IMPORTANT]
> Enterprise Edition only
> 
> This an [Enterprise Edition](https://www.couchbase.com/products/editions) feature. Purchase the _Enterprise License_, which includes official [Couchbase Support](https://www.couchbase.com/support-policy), to use it in production (see the license and support <https://www.couchbase.com/licensing-and-support-faq>).

> [!NOTE]
> Code Snippets
> 
> The code examples are indicative only. They demonstrate basic concepts and approaches to using a feature. Use them as inspiration and adapt these examples to best practice when developing applications for your platform.

## [](#introduction)Introduction

This content provides sample code and configuration examples covering the implementation of [Peer-to-Peer Sync](../../current/java/refer-glossary.md#peer-to-peer-sync) over websockets. Specifically it covers the implementation of an [Active Peer](../../current/java/refer-glossary.md#active-peer).

This _active peer_ (also referred to as a client and-or a replicator) will initiate connection with a [Passive Peer](../../current/java/refer-glossary.md#passive-peer) (also referred to as a server and-or listener) and participate in the replication of database changes to bring both databases into sync.

Subsequent sections provide additional details and examples for the main configuration options.

> [!NOTE]
> Secure Storage
> 
> The use of TLS, its associated keys and certificates requires using secure storage to minimize the chances of a security breach. The implementation of this storage differs from platform to platform — see [Using secure storage](../../current/java/p2psync-websocket.md#using-secure-storage).

## [](#configuration-summary)Configuration Summary

You should configure and initialize a replicator for each Couchbase Lite database instance you want to sync. [Example 1](#simple-replication-to-listener) shows the initialization and configuration process.

Example 1\. Replication configuration and initialization

```Java
// initialize the replicator configuration
final ReplicatorConfiguration thisConfig
   = new ReplicatorConfiguration(
      thisDB,
      URLEndpoint(URI("wss://listener.com:8954"))); (1)

// Set replicator type
thisConfig.setReplicatorType(
  ReplicatorConfiguration.ReplicatorType.PUSH_AND_PULL);

// Configure Sync Mode
thisConfig.setContinuous(false); // default value

// Configure Server Security --
// only accept self-signed certs
thisConfig.setAcceptOnlySelfSignedServerCertificate(true); (2)

// Configure Client Security (3)
// Configure basic auth using user credentials
final BasicAuthenticator thisAuth
  = new BasicAuthenticator(
      "Our Username",
      "Our PasswordValue"));

thisConfig.setAuthenticator(thisAuth)

/* Optionally set custom conflict resolver call back */
thisConfig.setConflictResolver( /* user supplied code */ ); (4)

// Create replicator
final Replicator thisReplicator = new Replicator(thisConfig); (5)

// Optionally add a change listener (6)
ListenerToken thisListener
  = new thisReplicator.addChangeListener(change -> {
    if (change.getStatus().getError() != null) {
      Log.i(TAG, "Error code ::  " +
        change.getStatus().getError().getCode());
    }
  });

// Start replicator
thisReplicator.start(false); (7)
```

**Notes on Example**

| **1** | Use the [ReplicatorConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/ReplicatorConfiguration.html) class's constructor — [ReplicatorConfiguration(database, endpoint)](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/ReplicatorConfiguration.html#ReplicatorConfiguration-com.couchbase.lite.Database-com.couchbase.lite.Endpoint-) — to initialize the replicator configuration with the local database — see also: [\[configure-target\]](#configure-target) |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Configure how the client will authenticate the server. Here we say connect only to servers presenting a self-signed certificate. By default, clients accept only servers presenting certificates that can be verified using the OS bundled Root CA Certificates — see: [\[authenticating-the-listener\]](#authenticating-the-listener).                                                                                                                                                                                                                         |
| **3** | Configure the credentials the client will present to the server. Here we say to provide _Basic Authentication_ credentials. Other options are available — see: [\[client-authentication\]](#client-authentication).                                                                                                                                                                                                                                                                                                                                             |
| **4** | Configure how the replication should perform [Conflict Resolution](#conflict-resolution).                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **5** | Initialize the replicator using your configuration object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **6** | Register an observer, which will notify you of changes to the replication status.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **7** | Start the replicator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## [](#api-references)API References

You can find [Java API References](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?) here.

## [](#device-discovery)Device Discovery

**This phase is optional:** If the listener is initialized on a well known URL endpoint (for example, a static IP Address or well known DNS address) then you can configure active peers to connect to those.

Prior to connecting with a listener you may execute a peer discovery phase to dynamically discover peers.

## [](#configure-replicator)Configure Replicator

In this section

[Configure Target](#lbl-cfg-tgt) | [Sync Mode](#lbl-cfg-sync) | [Heartbeat](#lbl-cfg-htbt) | [Authenticating the Listener](#lbl-auth-lstnr) | [Client Authentication](#lbl-authclnt)

### [](#lbl-cfg-tgt)Configure Target

Use the [ReplicatorConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/ReplicatorConfiguration.html) class and [ReplicatorConfiguration(database, endpoint)](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/ReplicatorConfiguration.html#ReplicatorConfiguration-com.couchbase.lite.Database-com.couchbase.lite.Endpoint-) constructor to initialize the replication configuration with local and remote database locations.

The constructor provides:

* the name of the local database to be sync'd
* the server's URL (including the port number and the name of the remote database to sync with)  
It is expected that the app will identify the IP address and URL and append the remote database name to the URL endpoint, producing for example: `wss://10.0.2.2:4984/travel-sample`  
The URL scheme for web socket URLs uses `ws:` (non-TLS) or `wss:` (SSL/TLS) prefixes.

Example 2\. Add Target to Configuration

```Java
// initialize the replicator configuration
final ReplicatorConfiguration thisConfig
    = new ReplicatorConfiguration(
      thisDB,
      URLEndpoint(URI("wss://listener.com:8954/travel-sample"))); (1)
```

**Notes on Example**

| **1** | Note use of the wss:// prefix to ensure TLS encryption (strongly recommended in production) |
| ----- | ------------------------------------------------------------------------------------------- |

### [](#lbl-cfg-sync)Sync Mode

Here we define the direction and type of replication we want to initiate.

We use `[ReplicatorConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/ReplicatorConfiguration.html)` class's [replicatorType](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/ReplicatorConfiguration.html#setReplicatorType-com.couchbase.lite.AbstractReplicatorConfiguration.ReplicatorType-) and `[continuous](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/ReplicatorConfiguration.html#setContinuous-boolean-)` parameters, to tell the replicator:

* The direction of the replication: `**pushAndPull**`; `pull`; `push`
* The type of replication, that is:

  * Continuous — remaining active indefinitely to replicate changed documents (`continuous=true`).
  * Ad-hoc — a one-shot replication of changed documents (`continuous=false`).

Example 3\. Configure replicator type and mode

```Java
// Set replicator type
thisConfig.setReplicatorType(
  ReplicatorConfiguration.ReplicatorType.PUSH_AND_PULL);

// Configure Sync Mode
thisConfig.setContinuous(false); // default value
```

### [](#lbl-cfg-htbt)Heartbeat

A point to consider when initiating a replication, particularly a continuous replication, is keeping the connection alive. Couchbase Lite minimizes the chance of dropped connections by having the replicator maintain a heartbeat; essentially pinging the listener at a configurable interval.

When necessary you can adjust this interval using [setHeartbeat()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/ReplicatorConfiguration.html#setHeartbeat-long-) as shown in — [Example 4](#ex-htbt).

The default heartbeat value is 300 (5 minutes).

Example 4\. Setting heartbeat interval

```Java
URLEndpoint target =
    new URLEndpoint(new URI("ws://localhost:4984/mydatabase"));

ReplicatorConfiguration config =
    new ReplicatorConfiguration(database, target);

//  other config as required . . .

config.setHeartbeat(60L); (1)

//  other config as required . . .

Replicator repl = new Replicator(config);
```

| **1** | The heartbeat value sets the interval (in seconds) between the heartbeat pulses. |
| ----- | -------------------------------------------------------------------------------- |

### [](#lbl-auth-lstnr)Authenticating the Listener

Define the credentials the your app (the client) is expecting to receive from the server (listener) in order to ensure that the server is one it is prepared to interact with.

Note that the client cannot authenticate the server if TLS is turned off. When TLS is enabled (Sync Gateway's default) the client _must_ authenticate the server. If the server cannot provide acceptable credentials then the connection will fail.

Use `[ReplicatorConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/ReplicatorConfiguration.html)` properties [setAcceptOnlySelfSignedServerCertificate](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/ReplicatorConfiguration.html#setAcceptOnlySelfSignedServerCertificate-boolean-) and [setPinnedServerCertificate()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/ReplicatorConfiguration.html#setPinnedServerCertificate-byte:A-), to tell the replicator how to verify server-supplied TLS server certificates.

* If there is a pinned certificate, nothing else matters, the server cert must **exactly** match the pinned certificate.
* If there are no pinned certs and [setAcceptOnlySelfSignedServerCertificate](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/ReplicatorConfiguration.html#setAcceptOnlySelfSignedServerCertificate-boolean-) is `true` then any self-signed certificate is accepted. Certificates that are not self signed are rejected, no matter who signed them.
* If there are no pinned certificates and [setAcceptOnlySelfSignedServerCertificate](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/ReplicatorConfiguration.html#setAcceptOnlySelfSignedServerCertificate-boolean-) is `false` (default), the client validates the server's certificates against the system CA certificates. The server must supply a chain of certificates whose root is signed by one of the certificates in the system CA bundle.

Example 5\. Set Server TLS security

* CA Cert
* Self Signed Cert
* Pinned Certificate

Set the client to expect and accept only CA attested certificates.

```Java
// Configure Server Security
// -- only accept CA Certs
thisConfig.setAcceptOnlySelfSignedServerCertificate(false); (1)
```

**Notes on Example**

| **1** | This is the default. Only certificate chains with roots signed by a trusted CA are allowed. Self signed certificates are not allowed. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------- |

Set the client to expect and accept only self-signed certificates

```Java
// Configure Server Security --
// only accept self-signed certs
thisConfig.setAcceptOnlySelfSignedServerCertificate(true); (1)
```

**Notes on Example**

| **1** | Set this to true to accept any self signed cert. Any certificates that are not self-signed are rejected. |
| ----- | -------------------------------------------------------------------------------------------------------- |

Set the client to expect and accept only a pinned certificate.

```Java
// Use the pinned certificate from the byte array (cert)
thisConfig.setPinnedServerCertificate(cert.getEncoded()); (1)
```

| **1** | Configure to accept only CA certs                                    |
| ----- | -------------------------------------------------------------------- |
| **2** | Configure the pinned certificate using data from the byte array cert |

### [](#lbl-authclnt)Client Authentication

Here we define the credentials that the client can present to the server if prompted to do so in order that the server can authenticate it.

We use [ReplicatorConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/ReplicatorConfiguration.html)'s [setAuthenticator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/ReplicatorConfiguration.html#setAuthenticator-com.couchbase.lite.Authenticator-) method to define the authentication method to the replicator - see [Example 7](#configuring-client-authentication).

#### [](#basic-authentication)Basic Authentication

Use the `[BasicAuthenticator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/BasicAuthenticator.html)` to supply basic authentication credentials (username and password).

Example 6\. Basic Authentication

This example shows basic authentication using user name and password:

```Java
// Configure basic auth using user credentials
final BasicAuthenticator thisAuth
  = new BasicAuthenticator(
      "Our Username",
      "Our PasswordValue"));

thisConfig.setAuthenticator(thisAuth)
```

#### [](#certificate-authentication)Certificate Authentication

Use the `[ClientCertificateAuthenticator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/ClientCertificateAuthenticator.html)` to configure the client TLS certificates to be presented to the server, on connection. This applies only to the [URLEndpointListener](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/URLEndpointListener.html).

> [!NOTE]
> The **server** (listener) must have `disableTLS` set `false` and have a [ClientCertificateAuthenticator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/ClientCertificateAuthenticator.html) configured, or it will never ask for this client's certificate.

The certificate to be presented to the server will need to be signed by the root certificates or be valid based on the authentication callback set to the listener via ListenerCertificateAuthenticator.

Example 7\. Client Cert Authentication

This example shows client certificate authentication using an identity from secure storage.

```Java
// ... other replicator configuration
// Provide a client certificate to the server for authentication
final TLSIdentity thisClientId =
  TLSIdentity.getIdentity(
    store,     // keystore holding private key and cert chain
    "clientId", // key label/alias
    null        // key password as required
  ); (1)
if (thisClientId == null) { throw new IllegalStateException("Client id not found"); } // Error path

thisConfig.setAuthenticator(
  new ClientCertificateAuthenticator(thisClientId)); (2)

// ... other replicator configuration
// final thisReplicator(thisConfig);
```

**Notes on Example**

| **1** | Get an identity from secure storage and create a TLS Identity object                                                                                                                                                                   |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Set the authenticator to [ClientCertificateAuthenticator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/ClientCertificateAuthenticator.html) and configure it to use the retrieved identity |

## [](#initialize-replicator)Initialize Replicator

Use the `[Replicator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/Replicator.html)` class's [ReplicatorConfiguration(config)](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/Replicator.html#Replicator-com.couchbase.lite.ReplicatorConfiguration-) constructor, to initialize the replicator with the configuration you have defined. You can, optionally, add a change listener (see [Monitor Sync](#lbl-repl-mon)) before starting the replicator running using [start()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/AbstractReplicator.html#start-boolean-).

Example 8\. Initialize and run replicator

```Java
// Create replicator
final Replicator thisReplicator = new Replicator(thisConfig); (1)

// Start replicator
thisReplicator.start(false); (2)
```

**Notes on Example**

| **1** | Initialize the replicator with the configuration |
| ----- | ------------------------------------------------ |
| **2** | Start the replicator                             |

## [](#lbl-repl-mon)Monitor Sync

In this section

[Change Listeners](#lbl-repl-chng) | [Replicator Status](#lbl-repl-status) | [Documents Pending Push](#lbl-repl-pend)

In this section

[Change Listeners](#lbl-repl-chng) | [Replicator Status](#lbl-repl-status) | [\[lbl-repl-evnts\]](#lbl-repl-evnts) | [Documents Pending Push](#lbl-repl-pend)

You can monitor a replication's status by using a combination of [Change Listeners](#lbl-repl-chng) and the `replication.status.activity` property — see; [getActivityLevel()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/AbstractReplicator.Status.html#getActivityLevel--). This enables you to know, for example, when the replication is actively transferring data and when it has stopped.

You can also choose to monitor document changes — see: [\[lbl-repl-evnts\]](#lbl-repl-evnts).

### [](#lbl-repl-chng)Change Listeners

Use this to monitor changes and to inform on sync progress; this is an optional step.

> [!TIP]
> Best Practice
> 
> You should register the listener before starting your replication, to avoid having to do a restart to activate it …​ and don't forget to save the token so you can remove the listener later

Use the [Replicator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/Replicator.html) class to add a change listener as a callback to the Replicator ([addChangeListener()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/AbstractReplicator.html#addChangeListener-java.util.concurrent.Executor-com.couchbase.lite.ReplicatorChangeListener-)) — see: [Example 9](#ex-repl-mon). You will then be asynchronously notified of state changes.

Remove your change listener before stopping the replicator — use the [removeChangeListener(ListenerToken token)](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/AbstractReplicator.html#removeChangeListener-com.couchbase.lite.ListenerToken-) method to do this.

### [](#lbl-repl-status)Replicator Status

You can use the [Replicator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/Replicator.html) class's [replicator.getStatus](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/AbstractReplicator.html#getStatus--) property to check the replicator status. That is, whether it is actively transferring data or if it has stopped — see: [Example 9](#ex-repl-mon).

The returned _ReplicationStatus_ structure comprises:

* [getActivityLevel()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/AbstractReplicator.Status.html#getActivityLevel--) — stopped, offline, connecting, idle or busy — see states described in: [Table 1](#tbl-states)
* [getProgress()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/AbstractReplicator.Status.html#getProgress--)

  * completed — the total number of changes completed
  * total — the total number of changes to be processed
* [getError()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/AbstractReplicator.Status.html#getError--) — the current error, if any

Example 9\. Monitor replication

* Adding a Change Listener
* Using replicator.status

```Java
ListenerToken thisListener
  = new thisReplicator.addChangeListener(change -> {
    if (change.getStatus().getError() != null) {
      Log.i(TAG, "Error code ::  " +
        change.getStatus().getError().getCode());
    }
  });
```

```Java
Log.i(TAG, "The Replicator is currently " +
  thisReplicator.getStatus().getActivityLevel());

Log.i(TAG, "The Replicator has processed " + t);

if (thisReplicator.getStatus().getActivityLevel() ==
  Replicator.ActivityLevel.BUSY) {
    Log.i(TAG, "Replication Processing");
    Log.i(TAG, "It has completed " +
      thisReplicator.getStatus().getProgess().getTotal() +
      " changes");
  }
```

#### [](#lbl-repl-states)Replication States

[Table 1](#tbl-states) shows the different states, or activity levels, reported in the API; and the meaning of each.

__Table 1\. Replicator activity levels__
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
> [Replicator.isDocumentPending](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/AbstractReplicator.html#isDocumentPending-java.lang.String-) is quicker and more efficient. Use it in preference to returning a list of pending document IDs, where possible.

You can check whether documents are waiting to be pushed in any forthcoming sync by using either of the following API methods:

* Use the [Replicator.getPendingDocumentIds()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/AbstractReplicator.html#getPendingDocumentIds--) method, which returns a list of document IDs that have local changes, but which have not yet been pushed to the server.  
This can be very useful in tracking the progress of a push sync, enabling the app to provide a visual indicator to the end user on its status, or decide when it is safe to exit.
* Use the [Replicator.isDocumentPending](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/AbstractReplicator.html#isDocumentPending-java.lang.String-) method to quickly check whether an individual document is pending a push.

Example 10\. Use Pending Document ID API

```Java
    // ... include other code as required
    //
    final Endpoint endpoint =
      new URLEndpoint(new URI("ws://localhost:4984/db"));

    final ReplicatorConfiguration config =
      new ReplicatorConfiguration(database, endpoint)
    .setReplicatorType(ReplicatorConfiguration.ReplicatorType.PUSH);

    replicator = new Replicator(config);
    final Set<String> pendingDocs =
      replicator.getPendingDocumentIds(); (1)


    replicator.addChangeListener(change -> {
      onStatusChanged(pendingDocs, change.getStatus()); });

    replicator.start();

    // ... include other code as required
//
private void onStatusChanged(
  @NonNull final Set<String> pendingDocs,
  @NonNull final Replicator.Status status) {
  // ... sample onStatusChanged function
  //
  Log.i(TAG,
    "Replicator activity level is " + status.getActivityLevel().toString());

  // iterate and report-on previously
  // retrieved pending docids 'list'
  for (Iterator<String> itr = pendingDocs.iterator(); itr.hasNext(); ) {
    final String docId = itr.next();
    try {
      if (!replicator.isDocumentPending(docId)) { continue; } (2)

      itr.remove();
      Log.i(TAG, "Doc ID " + docId + " has been pushed");
    }
    catch (CouchbaseLiteException e) {
      Log.w(TAG, "isDocumentPending failed", e); }
  }
}
```

| **1** | [Replicator.getPendingDocumentIds()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/AbstractReplicator.html#getPendingDocumentIds--) returns a list of the document IDs for all documents waiting to be pushed. This is a snapshot and may have changed by the time the response is received and processed. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [Replicator.isDocumentPending](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/AbstractReplicator.html#isDocumentPending-java.lang.String-) returns true if the document is waiting to be pushed, and false otherwise.                                                                                       |

## [](#lbl-repl-stop)Stop Sync

Stopping a replication is straightforward. It is done using [stop()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/AbstractReplicator.html#stop--). This initiates an asynchronous operation and so is not necessarily immediate. Your app should account for this potential delay before attempting any subsequent operations, for example closing the database.

You can find further information on database operations in [Databases](../../current/java/database.md).

> [!TIP]
> Best Practice
> 
> 1. When you start a change listener, save the returned token, you will need it when you remove the listener
> 2. You can ensure the replication has completely stopped by checking for a replication status = STOPPED

Example 11\. Stop replicator

```Java
// Stop replication.
thisReplicator.stop(); (1)
```

| **1** | Here we initiate the stopping of the replication using the [stop()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/AbstractReplicator.html#stop--) method. We can then remove any active [change listener](#lbl-repl-chng). |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#conflict-resolution)Conflict Resolution

Unless you specify otherwise, Couchbase Lite's default conflict resolution policy is applied — see [Automatic Conflict Resolution](#couchbase-lite:java:{cbl-pg-conflict-auto}).

To use a different policy, specify a _conflict resolver_ using [conflictResolver](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?com/couchbase/lite/ReplicatorConfiguration.html#setConflictResolver-com.couchbase.lite.ConflictResolver-) as shown in [Example 12](#using-conflict-resolvers).

For more complex solutions you can provide a custom conflict resolver - see: [Custom Conflict Resolution](#couchbase-lite:java:{cbl-pg-conflict-custom}).

Example 12\. Using conflict resolvers

* Local Wins
* Remote Wins
* Merge

```Java
class LocalWinConflictResolver implements ConflictResolver {
    public Document resolve(Conflict conflict) {
        return conflict.getLocalDocument();
    }
}
```

```Java
class RemoteWinConflictResolver implements ConflictResolver {
    public Document resolve(Conflict conflict) {
        return conflict.getRemoteDocument();
    }
}
```

```Java
class MergeConflictResolver implements ConflictResolver {
    public Document resolve(Conflict conflict) {
        Map<String, Object> merge = conflict.getLocalDocument().toMap();
        merge.putAll(conflict.getRemoteDocument().toMap());
        return new MutableDocument(conflict.getDocumentId(), merge);
    }
}
```

Just as a replicator may observe a conflict — when updating a document that has changed both in the local database and in a remote database — any attempt to save a document may also observe a conflict, if a replication has taken place since the local app retrieved the document from the database. To address that possibility, a version of the `Database.save()` method also takes a conflict resolver as shown in [\[merging-document-properties\]](#merging-document-properties).

The following code snippet shows an example of merging properties from the existing document (`current`) into the one being saved (`new`). In the event of conflicting keys, it will pick the key value from `new`.

Example 13\. Merging document properties

```Java
Document doc = database.getDocument("xyz");
if (doc == null) { return; }
MutableDocument mutableDocument = doc.toMutable();
mutableDocument.setString("name", "apples");

database.save(
    mutableDocument,
    (newDoc, curDoc) -> {
        if (curDoc == null) { return false; }
        Map<String, Object> dataMap = curDoc.toMap();
        dataMap.putAll(newDoc.toMap());
        newDoc.setData(dataMap);
        return true;
    });
```

## [](#related-content)Related Content

###### [](#)

How to

* [Passive Peer](../../current/java/p2psync-websocket-using-passive.md)
* [Active Peer](../../current/java/p2psync-websocket-using-active.md)

###### [](#-2)

Concepts

* [Landing P2Psync](#couchbase-lite:java:landing-p2psync.adoc)
* [API References](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?).

###### [](#-3)

Community Resources …​

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

* [Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)

For more on replicator conflict resolution see: [Handling Data Conflicts](../../current/java/conflict.md).

## [](#delta-sync)Delta Sync

If delta sync is enabled on the listener, then replication will use delta sync.

## [](#related-content-2)Related Content

###### [](#-4)

How to

* [Passive Peer](../../current/java/p2psync-websocket-using-passive.md)
* [Active Peer](../../current/java/p2psync-websocket-using-active.md)

###### [](#-5)

Concepts

* [Landing P2Psync](#couchbase-lite:java:landing-p2psync.adoc)
* [API References](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-java/index.html?).

###### [](#-6)

Community Resources …​

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

* [Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)