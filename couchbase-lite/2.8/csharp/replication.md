---
title: Data Sync using Sync Gateway
description: Couchbase Lite for C# -- Synchronizing data changes between local
  and remote databases using Sync Gateway
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/csharp/pages/replication.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@couchbase-lite:csharp:replication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/csharp/replication.html)

# Data Sync using Sync Gateway

> Description — _Couchbase Lite for C# — Synchronizing data changes between local and remote databases using Sync Gateway_  
> Related Content — [Handling Data Conflicts](../../current/csharp/conflict.md) | [Intra-device Data Sync](../../current/csharp/dbreplica.md) | [Peer-to-Peer](p2psync-websocket.md)

> [!NOTE]
> Code Snippets
> 
> The code examples are indicative only. They demonstrate basic concepts and approaches to using a feature. Use them as inspiration and adapt these examples to best practice when developing applications for your platform.

## [](#introduction)Introduction

Couchbase Lite for C#.Net provides API support for secure, bi-directional, synchronization of data changes between mobile applications and a central server database. It does so by using a replicator to interact with Sync Gateway. Simply put, the replicator is designed to send documents from a source to a target database. In this case, between a local Couchbase Lite database and remote Sync Gateway database (server or cloud).

This content provides sample code and configuration examples covering the implementation of a replication using Sync Gateway.

Your application runs a replicator (also referred to here as a client), which will initiate connection with a Sync Gateway (also referred to here as a server) and participate in the replication of database changes to bring both local and remote databases into sync.

Subsequent sections provide additional details and examples for the main configuration options.

## [](#replication-protocol)Replication Protocol

### [](#scheme)Scheme

Couchbase Mobile uses a replication protocol based on WebSockets fof replication. To use this protocol the replication URL should specify WebSockets as the URL scheme (see the [Configure Target](#lbl-cfg-tgt) section below).

Incompatibilities

Couchbase Lite’s replication protocol is **incompatible** with CouchDB-based databases. And since Couchbase Lite 2.x+ only supports the new protocol, you will need to run a version of Sync Gateway that supports it — see: [Compatibility](../../current/csharp/compatibility.md).

Legacy Compatibility

Clients using Couchbase Lite 1.x can continue to use `http` as the URL scheme. Sync Gateway 2.x+ will automatically use:

* The 1.x replication protocol when a Couchbase Lite 1.x client connects through `http://localhost:4984/db`
* The 2.0 replication protocol when a Couchbase Lite 2.0 client connects through `ws://localhost:4984/db`.

You can find further information in our blog: [Introducing the Data Replication Protocol](https://blog.couchbase.com/data-replication-couchbase-mobile/).

### [](#lbl-repl-ord)Ordering

To optimize for speed, the replication protocol doesn’t guarantee that documents will be received in a particular order. So we don’t recommend to rely on that when using the replication or database change listeners for example.

## [](#configuration-summary)Configuration Summary

You should configure and initialize a replicator for each Couchbase Lite database instance you want to sync. [Example 1](#ex-simple-repl) shows the configuration and initialization process.

Example 1\. Replication configuration and initialization

```C#
// . . . preceding code. for example . . .
private static ListenerToken _thisListenerToken;
var Database thisDB;
// . . . other code . . .
// initialize the replicator configuration

var thisUrl = new URLEndpoint("wss://listener.com:4984/otherDB"); (1)
var config = new ReplicatorConfiguration(thisDB, thisUrl);


// Set replicator type
thisConfig.ReplicatorType = ReplicatorType.PushAndPull;

// Configure Sync Mode
thisConfig.Continuous = true; // default value

// Configure Server Security -- only accept self-signed certs
thisConfig.AcceptOnlySelfSignedServerCertificate = true; (2)

// Configure Client Security (3)
// Configure basic auth using user credentials
thisConfig.Authenticator = new BasicAuthenticator("Our Username", "Our Password");

/* Optionally set a conflict resolver call back */ (4)
// Use built-in resolver
thisConfig.ConflictResolver = new LocalWinConflictResolver();  //

// optionally use custom resolver
thisConfig.ConflictResolver = new ConflictResolver(
  (conflict) => {
    /* define resolver function */
  }
); //

// Initialize and start a replicator
// Initialize replicator with configuration data
var thisReplicator = new Replicator(thisConfig); (5)

//Optionally add a change listener (6)
_thisListenerToken =
  thisReplicator.AddChangeListener((sender, args) =>
    {
      if (args.Status.Activity == ReplicatorActivityLevel.Stopped) {
          Console.WriteLine("Replication stopped");
      }
    });

// Start replicator
thisReplicator.Start(); (7)
```

**Notes on Example**

| **1** | Use the [ReplicatorConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorConfiguration.html) class’s constructor — [ReplicatorConfiguration(Database database, IEndpoint target)](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorConfiguration.html#Couchbase%5FLite%5FSync%5FReplicatorConfiguration%5F%5Fctor%5FCouchbase%5FLite%5FDatabase%5FCouchbase%5FLite%5FSync%5FIEndpoint) — to initialize the replicator configuration with the local database — see also: [Configure Target](#lbl-cfg-tgt) |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Configure how the client will authenticate the server. Here we say connect only to servers presenting a self-signed certificate. By default, clients accept only servers presenting certificates that can be verified using the OS bundled Root CA Certificates — see: [Server Authentication](#lbl-svr-auth).                                                                                                                                                                                                                                                                                           |
| **3** | Configure the credentials the client will present to the server. Here we say to provide _Basic Authentication_ credentials. Other options are available — see: [Client Authentication](#lbl-client-auth).                                                                                                                                                                                                                                                                                                                                                                                                |
| **4** | Configure how the replication should handle conflict resolution — see: [Handling Data Conflicts](../../current/csharp/conflict.md) topic for mor on conflict resolution.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **5** | Initialize the replicator using your configuration object — see: [Initialize](#lbl-init-repl).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **6** | Optionally, register an observer, which will notify you of changes to the replication status — see: [Monitor](#lbl-repl-mon)                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **7** | Start the replicator — see: [Start Replicator](#lbl-repl-start).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## [](#lbl-cfg-repl)Configure

In this section

[Configure Target](#lbl-cfg-tgt) | [Sync Mode](#lbl-cfg-sync) | [Heartbeat](#lbl-cfg-keep-alive) | [Server Authentication](#lbl-svr-auth) | [Client Authentication](#lbl-client-auth) | [Monitor Document Changes](#lbl-repl-evnts) | [Custom Headers](#lbl-repl-hdrs) | [Checkpoint Starts](#lbl-repl-ckpt) | [Replication Filters](#lbl-repl-fltrs) | [Channels](#lbl-repl-chan) | [Delta Sync](#lbl-repl-delta)

### [](#lbl-cfg-tgt)Configure Target

Use the [ReplicatorConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorConfiguration.html) class and [ReplicatorConfiguration(Database database, IEndpoint target)](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorConfiguration.html#Couchbase%5FLite%5FSync%5FReplicatorConfiguration%5F%5Fctor%5FCouchbase%5FLite%5FDatabase%5FCouchbase%5FLite%5FSync%5FIEndpoint) constructor to initialize the replication configuration with local and remote database locations.

The constructor provides:

* the name of the local database to be sync’d
* the server’s URL (including the port number and the name of the remote database to sync with)  
It is expected that the app will identify the IP address and URL and append the remote database name to the URL endpoint, producing for example: `wss://10.0.2.2:4984/travel-sample`  
The URL scheme for web socket URLs uses `ws:` (non-TLS) or `wss:` (SSL/TLS) prefixes.

Example 2\. Add Target to Configuration

```C#
// initialize the replicator configuration

var thisUrl = new URLEndpoint("wss://l10.0.2.2:4984/anotherDB"); (1)
var config = new ReplicatorConfiguration(thisDB, thisUrl);
```

**Notes on Example**

| **1** | Note use of the wss:// prefix to ensure TLS encryption (strongly recommended in production) |
| ----- | ------------------------------------------------------------------------------------------- |

### [](#lbl-cfg-sync)Sync Mode

Here we define the direction and type of replication we want to initiate.

We use `[ReplicatorConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorConfiguration.html)` class’s [ReplicatorType](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorConfiguration.html#Couchbase%5FLite%5FSync%5FReplicatorConfiguration%5FReplicatorType) and `[Continuous](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorConfiguration.html#Couchbase%5FLite%5FSync%5FReplicatorConfiguration%5FContinuous)` parameters, to tell the replicator:

* The direction of the replication: `**pushAndPull**`; `pull`; `push`
* The type of replication, that is:

  * Continuous — remaining active indefinitely to replicate changed documents (`continuous=true`).
  * Ad-hoc — a one-shot replication of changed documents (`continuous=false`).

Example 3\. Configure replicator type and mode

```C#
// Set replicator type
thisConfig.ReplicatorType = ReplicatorType.PushAndPull;

// Configure Sync Mode
thisConfig.Continuous = true; // default value
```

### [](#lbl-cfg-keep-alive)Heartbeat

A point to consider when initiating a replication, particularly a continuous replication, is keeping the connection alive. Couchbase Lite minimizes the chance of dropped connections by having the replicator maintain a heartbeat; essentially pinging the Sync Gateway at a configurable interval.

When necessary you can adjust this interval using [Heartbeat()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorConfiguration.html#Couchbase%5FLite%5FSync%5FReplicatorConfiguration%5FHeartbeat) as shown in — [Example 4](#ex-htbt). You may need to do this when, for example, when the Sync Gateway is behind a load balancer, which may have its own keep-alive parameters — see Sync Gateway’s topic [Load Balancer - Keep Alive](../../../sync-gateway/current/deploy/load-balancer.md#lbl-keepalive).

The default heartbeat value is 300 (5 minutes).

Example 4\. Setting heartbeat interval

```C#
    var url = new Uri("ws://localhost:4984/mydatabase");
    var target = new URLEndpoint(url);

    var config = new ReplicatorConfiguration(database, target);

//  other config as required . . .

    config.Heartbeat = TimeSpan.FromSeconds(60); //  (1)

//  other config as required . . .

    var repl = new Replicator(config);
```

| **1** | The heartbeat value sets the interval (in seconds) between the heartbeat pulses. |
| ----- | -------------------------------------------------------------------------------- |

### [](#lbl-svr-auth)Server Authentication

Define the credentials your app (the client) is expecting to receive from the Sync Gateway (the server) in order to ensure it is prepared to continue with the sync.

Note that the client cannot authenticate the server if TLS is turned off. When TLS is enabled (Sync Gateway’s default) the client _must_ authenticate the server. If the server cannot provide acceptable credentials then the connection will fail.

Use `[ReplicatorConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorConfiguration.html)` properties [AcceptOnlySelfSignedServerCertificate](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorConfiguration.html#Couchbase%5FLite%5FSync%5FReplicatorConfiguration%5FAcceptOnlySelfSignedServerCertificate) and [PinnedServerCertificate](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorConfiguration.html#Couchbase%5FLite%5FSync%5FReplicatorConfiguration%5FPinnedServerCertificate), to tell the replicator how to verify server-supplied TLS server certificates.

* If there is a pinned certificate, nothing else matters, the server cert must **exactly** match the pinned certificate.
* If there are no pinned certs and [AcceptOnlySelfSignedServerCertificate](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorConfiguration.html#Couchbase%5FLite%5FSync%5FReplicatorConfiguration%5FAcceptOnlySelfSignedServerCertificate) is `true` then any self-signed certificate is accepted. Certificates that are not self signed are rejected, no matter who signed them.
* If there are no pinned certificates and [AcceptOnlySelfSignedServerCertificate](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorConfiguration.html#Couchbase%5FLite%5FSync%5FReplicatorConfiguration%5FAcceptOnlySelfSignedServerCertificate) is `false` (default), the client validates the server’s certificates against the system CA certificates. The server must supply a chain of certificates whose root is signed by one of the certificates in the system CA bundle.

Example 5\. Set Server TLS security

* CA Cert
* Self Signed Cert
* Pinned Certificate

Set the client to expect and accept only CA attested certificates.

```C#
// Configure Server Security -- only accept CA certs
thisConfig.AcceptOnlySelfSignedServerCertificate = false; (1)
```

**Notes on Example**

| **1** | This is the default. Only certificate chains with roots signed by a trusted CA are allowed. Self signed certificates are not allowed. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------- |

Set the client to expect and accept only self-signed certificates

```C#
// Configure Server Security -- only accept self-signed certs
thisConfig.AcceptOnlySelfSignedServerCertificate = true; (1)
```

**Notes on Example**

| **1** | Set this to true to accept any self signed cert. Any certificates that are not self-signed are rejected. |
| ----- | -------------------------------------------------------------------------------------------------------- |

Set the client to expect and accept only a pinned certificate.

```C#
// Only CA Certs accepted
thisConfig.AcceptOnlySelfSignedServerCertificate =
  false; (1)

var thisCert =
  new X509Certificate2(caData); (2)

thisConfig.PinnedServerCertificate =
  thisCert; (3)
```

| **1** | Configure to accept only CA certs                                    |
| ----- | -------------------------------------------------------------------- |
| **2** | Configure the pinned certificate using data from the byte array cert |
| **3** | Set the certificate to be compared with that provided by the server  |

This all assumes that you have configured the Sync Gateway to provide the appropriate SSL certificates, and have included the appropriate certificate in your app bundle — for more on this see: [Certificate Pinning](#lbl-cert-pinning).

### [](#lbl-client-auth)Client Authentication

By default, Sync Gateway does not enable authentication. This is to make it easier to get up and running with synchronization. You can enable authentication with the following properties in the configuration file:

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

To authenticate with Sync Gateway, an associated user must first be created. Sync Gateway users can be created through the [POST /{db}/\_user](../../../sync-gateway/current/rest-api/rest-api-admin.md#/user/post%5F%5Fdb%5F%5F%5Fuser%5F) endpoint on the Admin REST API. Provided that the user exists on Sync Gateway, there are two ways to authenticate from a Couchbase Lite client: Basic Authentication or Session Authentication.

#### [](#basic-authentication)Basic Authentication

You can provide a user name and password to the basic authenticator class method. Under the hood, the replicator will send the credentials in the first request to retrieve a `SyncGatewaySession` cookie and use it for all subsequent requests during the replication. This is the recommended way of using basic authentication. The following example initiates a one-shot replication as the user **username** with the password **password**.

```C#
var url = new Uri("ws://localhost:4984/mydatabase");
var target = new URLEndpoint(url);
var config = new ReplicatorConfiguration(database, target);
config.Authenticator = new BasicAuthenticator("john", "pass");

var replicator = new Replicator(config);
replicator.Start();
```

#### [](#session-authentication)Session Authentication

Session authentication is another way to authenticate with Sync Gateway. A user session must first be created through the [POST /{db}/\_session](../../../sync-gateway/current/rest-api/rest-api.md#/session/post%5F%5Fdb%5F%5F%5Fsession) endpoint on the Public REST API. The HTTP response contains a session ID which can then be used to authenticate as the user it was created for. The following example initiates a one-shot replication with the session ID that is returned from the `POST /{db}/_session` endpoint.

```C#
var url = new Uri("ws://localhost:4984/mydatabase");
var target = new URLEndpoint(url);
var config = new ReplicatorConfiguration(database, target);
config.Authenticator = new SessionAuthenticator("904ac010862f37c8dd99015a33ab5a3565fd8447");

var replicator = new Replicator(config);
replicator.Start();
```

### [](#lbl-repl-hdrs)Custom Headers

Custom headers can be set on the configuration object. And the replicator will send those header(s) in every request. As an example, this feature can be useful to pass additional credentials when there is an authentication or authorization step being done by a proxy server (between Couchbase Lite and Sync Gateway).

Example 6\. Setting custom headers

```C#
var config = new ReplicatorConfiguration(database, target)
{
    Headers = new Dictionary<string, string>
    {
        ["CustomHeaderName"] = "Value"
    }
};
```

### [](#lbl-repl-fltrs)Replication Filters

Replication Filters allow you to have quick control over which documents are stored as the result of a push and/or pull replication.

#### [](#push-filter)Push Filter

A push filter allows an app to push a subset of a database to the server, which can be very useful in some circumstances. For instance, high-priority documents could be pushed first, or documents in a "draft" state could be skipped.

The following example filters out documents whose `type` property is equal to `draft`.

```C#
var url = new Uri("ws://localhost:4984/mydatabase");
var target = new URLEndpoint(url);

var config = new ReplicatorConfiguration(database, target);
config.PushFilter = (document, flags) => (1)
{
    if (flags.HasFlag(DocumentFlags.Deleted)) {
        return false;
    }

    return true;
};

// Dispose() later
var replicator = new Replicator(config);
replicator.Start();
```

| **1** | The callback should follow the semantics of a [pure function](https://en.wikipedia.org/wiki/Pure%5Ffunction). Otherwise, long running functions would slow down the replicator considerably. Furthermore, your callback should not make assumptions about what thread it is being called on. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#### [](#pull-filter)Pull Filter

A pull filter gives an app the ability to validate documents being pulled, and skip ones that fail. This is an important security mechanism in a peer-to-peer topology with peers that are not fully trusted.

> [!NOTE]
> Pull replication filters are not a substitute for channels. Sync Gateway [channels](../../../sync-gateway/current/access-control/channels.md) are designed to be scalable (documents are filtered on the server) whereas a pull replication filter is applied to a document once it has been downloaded.

```C#
var url = new Uri("ws://localhost:4984/mydatabase");
var target = new URLEndpoint(url);

var config = new ReplicatorConfiguration(database, target);
config.PullFilter = (document, flags) => (1)
{
    if (document.GetString("type") == "draft") {
        return false;
    }

    return true;
};

// Dispose() later
var replicator = new Replicator(config);
replicator.Start();
```

| **1** | The callback should follow the semantics of a [pure function](https://en.wikipedia.org/wiki/Pure%5Ffunction). Otherwise, long running functions would slow down the replicator considerably. Furthermore, your callback should not make assumptions about what thread it is being called on. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

> [!NOTE]
> Losing access to a document (via the Sync Function) also triggers the pull replication filter. Filtering out such an event would retain the document locally. As a result, there would be a local copy of the document disjointed from the one that resides on Couchbase Server. Further updates to the document stored on Couchbase Server would not be received in pull replications and further local edits could be potentially pushed, which would result in 409 errors since access has been revoked.

### [](#lbl-repl-chan)Channels

By default, Couchbase Lite gets all the channels to which the configured user account has access. This behavior is suitable for most apps that rely on [user authentication](../../../sync-gateway/current/security/authentication-users.md) and the [sync function](../../../sync-gateway/current/access-control/sync-function/sync-function-api.md) to specify which data to pull for each user.

Optionally, it’s also possible to specify a comma-separated list of channel names on Couchbase Lite’s replicator configuration object. In this case, the replication from Sync Gateway will only pull documents tagged with those channels.

### [](#lbl-repl-delta)Delta Sync

> [!IMPORTANT]
> This is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature.

With Delta Sync \[[1](#%5Ffootnotedef%5F1 "View footnote.")\], only the changed parts of a Couchbase document are replicated. This can result in significant savings in bandwidth consumption as well as throughput improvements, especially when network bandwidth is typically constrained.

Replications to a Server (for example, a Sync Gateway, or passive listener) automatically use delta sync if the property is enabled at database level by the server — see: [databases.$db.delta\_sync.enabled](../../../sync-gateway/current/configuration/configuration-properties-legacy.md#databases-foo%5Fdb-delta%5Fsync).

[Intra-device Data Sync](../../current/csharp/dbreplica.md) replications automatically **disable** delta sync, whilst [Peer-to-Peer](p2psync-websocket.md) replications automatically **enable** delta sync.

## [](#lbl-init-repl)Initialize

In this section

[Start Replicator](#lbl-repl-start) | [Checkpoint Starts](#lbl-repl-ckpt)

### [](#lbl-repl-start)Start Replicator

Use the `[Replicator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html)` class’s [(ReplicatorConfiguration config)](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5F%5Fctor%5FCouchbase%5FLite%5FSync%5FReplicatorConfiguration%5F) constructor, to initialize the replicator with the configuration you have defined. You can, optionally, add a change listener (see [Monitor](#lbl-repl-mon)) before starting the replicator running using [Start()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5FStart).

Example 7\. Initialize and run replicator

```C#
// Initialize and start a replicator
// Initialize replicator with configuration data
var thisReplicator = new Replicator(thisConfig); (1)

// Start replicator
thisReplicator.Start(); (2)
```

**Notes on Example**

| **1** | Initialize the replicator with the configuration |
| ----- | ------------------------------------------------ |
| **2** | Start the replicator                             |

### [](#lbl-repl-ckpt)Checkpoint Starts

Replicators use [checkpoints](../../current/csharp/refer-glossary.md#checkpoint) to keep track of documents sent to the target database. Without [checkpoints](../../current/csharp/refer-glossary.md#checkpoint) , Couchbase Lite would replicate the entire database content to the target database on each connection, even though previous replications may already have replicated some or all of that content.

This functionality is generally not a concern to application developers. However, if you do want to force the replication to start again from zero, use the [checkpoint](../../current/csharp/refer-glossary.md#checkpoint) reset method `replicator.resetCheckpoint()` **before** starting the replicator.

Example 8\. Resetting checkpoints

```C#
// replicator is a Replicator instance
replicator.ResetCheckpoint();
replicator.Start();
```

## [](#lbl-repl-mon)Monitor

In this section

[Change Listeners](#lbl-repl-chng) | [Replicator Status](#lbl-repl-status) | [Monitor Document Changes](#lbl-repl-evnts) | [Documents Pending Push](#lbl-repl-pend)

You can monitor a replication’s status by using a combination of [Change Listeners](#lbl-repl-chng) and the `replication.status.activity` property — see; [Activity](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorStatus.html#Couchbase%5FLite%5FSync%5FReplicatorStatus%5FActivity). This enables you to know, for example, when the replication is actively transferring data and when it has stopped.

You can also choose to monitor document changes — see: [Monitor Document Changes](#lbl-repl-evnts).

### [](#lbl-repl-chng)Change Listeners

Use this to monitor changes and to inform on sync progress; this is an optional step.

> [!TIP]
> Best Practice
> 
> You should register the listener before starting your replication, to avoid having to do a restart to activate it …​ and don’t forget to save the token so you can remove the listener later

Use the [Replicator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html) class to add a change listener as a callback to the Replicator ([addChangeListener()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5FAddChangeListener%5FSystem%5FEventHandler%5FCouchbase%5FLite%5FSync%5FReplicatorStatusChangedEventArgs%5F%5F)) — see: [Example 9](#ex-repl-mon). You will then be asynchronously notified of state changes.

Remove your change listener before stopping the replicator — use the [RemoveChangeListener(ListenerToken)](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5FRemoveChangeListener%5FCouchbase%5FLite%5FListenerToken%5F) method to do this.

### [](#lbl-repl-status)Replicator Status

You can use the [Replicator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html) class’s [Replicator.Status](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5FStatus) property to check the replicator status. That is, whether it is actively transferring data or if it has stopped — see: [Example 9](#ex-repl-mon).

The returned _ReplicationStatus_ structure comprises:

* [Activity](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorStatus.html#Couchbase%5FLite%5FSync%5FReplicatorStatus%5FActivity) — stopped, offline, connecting, idle or busy — see states described in: [Table 1](#tbl-states)
* [Progress](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorStatus.html#Couchbase%5FLite%5FSync%5FReplicatorStatus%5FProgress)

  * completed — the total number of changes completed
  * total — the total number of changes to be processed
* [Error](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorStatus.html#Couchbase%5FLite%5FSync%5FReplicatorStatus%5FError) — the current error, if any

Example 9\. Monitor replication

* Adding a Change Listener
* Using replicator.status

```C#
_thisListenerToken =
  thisReplicator.AddChangeListener((sender, args) =>
    {
      if (args.Status.Activity == ReplicatorActivityLevel.Stopped) {
          Console.WriteLine("Replication stopped");
      }
    });
```

```C#
_thisReplicator.Stop();
while (_thisReplicator.Status.Activity != ReplicatorActivityLevel.Stopped) {
    // Database cannot close until replicators are stopped
    Console.WriteLine($"Waiting for replicator to stop (currently {_thisReplicator.Status.Activity})...");
    Thread.Sleep(200);
}
_thisDatabase.Close();
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

#### [](#replication-status-and-app-life-cycle)Replication Status and App Life Cycle

Couchbase Lite doesn’t react to OS backgrounding or foregrounding events and replication(s) will continue running as long as the remote system does not terminate the connection and the app does not terminate. It is generally recommended to stop replications before going into the background otherwise socket connections may be closed by the OS and this may interfere with the replication process.

### [](#lbl-repl-evnts)Monitor Document Changes

You can choose to register for document updates during a replication.

> [!TIP]
> You should register the listener before starting your replication, to avoid having to do a restart to activate it.

For example, the code snippet in [Example 10](#ex-reg-doc-listener) registers a listener to monitor document replication performed by the replicator referenced by the variable `replicator`. It prints the document ID of each document received and sent. Stop the listener as shown in [Example 11](#ex-stop-doc-listener).

Example 10\. Register a document listener

```C#
var token = replicator.AddDocumentReplicationListener((sender, args) =>
{
    var direction = args.IsPush ? "Push" : "Pull";
    Console.WriteLine($"Replication type :: {direction}");
    foreach (var document in args.Documents) {
        if (document.Error == null) {
            Console.WriteLine($"Doc ID :: {document.Id}");
            if (document.Flags.HasFlag(DocumentFlags.Deleted)) {
                Console.WriteLine("Successfully replicated a deleted document");
            }
        } else {
            // There was an error
        }
    }
});

replicator.Start();
```

Example 11\. Stop document listener

This code snippet shows how to stop the document listener using the token from the previous example.

```C#
replicator.RemoveChangeListener(token);
```

#### [](#document-access-removal-behavior)Document Access Removal Behavior

When access to a document is removed on Sync Gateway (see: Sync Gateway’s [Sync Function](../../../sync-gateway/current/access-control/sync-function/sync-function-api.md)), the document replication listener sends a notification with the `AccessRemoved` flag set to `true` and subsequently purges the document from the database.

### [](#lbl-repl-pend)Documents Pending Push

> [!TIP]
> [Replicator.IsDocumentPending()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5FIsDocumentPending%5FSystem%5FString%5F) is quicker and more efficient. Use it in preference to returning a list of pending document IDs, where possible.

You can check whether documents are waiting to be pushed in any forthcoming sync by using either of the following API methods:

* Use the [Replicator.GetPendingDocumentIDs()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5FGetPendingDocumentIDs) method, which returns a list of document IDs that have local changes, but which have not yet been pushed to the server.  
This can be very useful in tracking the progress of a push sync, enabling the app to provide a visual indicator to the end user on its status, or decide when it is safe to exit.
* Use the [Replicator.IsDocumentPending()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5FIsDocumentPending%5FSystem%5FString%5F) method to quickly check whether an individual document is pending a push.

Example 12\. Use Pending Document ID API

```C#
var url = new Uri("ws://localhost:4984/mydatabase");
var target = new URLEndpoint(url);
var database = new Database("myDB");
var config = new ReplicatorConfiguration(database, target);
config.ReplicatorType  = ReplicatorType.Push;

var replicator = new Replicator(config);

var mydocids =
  new HashSet <string> (replicator.GetPendingDocumentIDs()); (1)


if (mydocids.Count > 0)
{
    Console.WriteLine($"There are {mydocids.Count} documents pending");
    replicator.AddChangeListener((sender, change) =>
    {
        Console.WriteLine($"Replicator activity level is " +
                          change.Status.Activity.ToString());
        // iterate and report-on previously
        // retrieved pending docids 'list'
        foreach (var thisId in mydocids)
            if (!replicator.IsDocumentPending(thisId)) (2)
            {
                Console.WriteLine($"Doc ID {thisId} now pushed");
            };
    });

    replicator.Start();
}
```

| **1** | [Replicator.GetPendingDocumentIDs()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5FGetPendingDocumentIDs) returns a list of the document IDs for all documents waiting to be pushed. This is a snapshot and may have changed by the time the response is received and processed. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [Replicator.IsDocumentPending()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5FIsDocumentPending%5FSystem%5FString%5F) returns true if the document is waiting to be pushed, and false otherwise.                                                                                |

## [](#lbl-repl-stop)Stop

Stopping a replication is straightforward. It is done using [Stop()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5FStop). This initiates an asynchronous operation and so is not necessarily immediate. Your app should account for this potential delay before attempting any subsequent operations, for example closing the database.

You can find further information on database operations in [Databases](../../current/csharp/database.md).

> [!TIP]
> Best Practice
> 
> 1. When you start a change listener, save the returned token, you will need it when you remove the listener
> 2. You can ensure the replication has completely stopped by checking for a replication status = STOPPED

Example 13\. Stop replicator

```C#
// Stop replication.
thisReplicator.Stop(); (1)
```

| **1** | Here we initiate the stopping of the replication using the [Stop()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5FStop) method. We can then remove any active [change listener](#lbl-repl-chng). |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#lbl-nwk-errs)Error Handling

When _replicator_ detects a network error it updates its status depending on the error type (permanent or temporary) and returns an appropriate HTTP error code.

The following code snippet adds a `Change Listener`, which monitors a replication for errors and logs the the returned error code.

Example 14\. Monitoring for network errors

```C#
replicator.AddChangeListener((sender, args) =>
{
    if (args.Status.Error != null) {
        Console.WriteLine($"Error :: {args.Status.Error}");
    }
});
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

Couchbase Lite \[[2](#%5Ffootnotedef%5F2 "View footnote.")\] uses WebSockets as the communication protocol to transmit data. Some load balancers are not configured for WebSocket connections by default (NGINX for example); so it might be necessary to explicitly enable them in the load balancer’s configuration (see [Load Balancers](../../../sync-gateway/current/deploy/load-balancer.md)).

By default, the WebSocket protocol uses compression to optimize for speed and bandwidth utilization. The level of compression is set on Sync Gateway and can be tuned in the configuration file ([replicator\_compression](../../../sync-gateway/current/configuration/configuration-properties-legacy.md#replicator%5Fcompression)).

## [](#lbl-cert-pinning)Certificate Pinning

Couchbase Lite for C#.Net supports certificate pinning.

Certificate pinning is a technique that can be used by applications to "pin" a host to its certificate. The certificate is typically delivered to the client by an out-of-band channel and bundled with the client. In this case, Couchbase Lite uses this embedded certificate to verify the trustworthiness of the server (for example, a Sync Gateway) and no longer needs to rely on a trusted third party for that (commonly referred to as the Certificate Authority).

The following steps describe how to configure certificate pinning between Couchbase Lite and Sync Gateway.

1. [Create your own self-signed certificate](../../../sync-gateway/current/security/authentication-certs.md#creating-your-own-self-signed-certificate) with the `openssl` command. After completing this step, you should have 3 files: `cert.pem`, `cert.cer` and `privkey.pem`.
2. [Configure Sync Gateway](../../../sync-gateway/current/security/authentication-certs.md#installing-the-certificate) with the `cert.pem` and `privkey.pem` files. After completing this step, Sync Gateway is reachable over `https`/`wss`.
3. On the Couchbase Lite side, the replication must point to a URL with the `wss` scheme and configured with the `cert.cer` file created in step 1.  
This example loads the certificate from the application sandbox, then converts it to the appropriate type to configure the replication object.  
```C#  
// Note: `GetCertificate` is a fake method. This would be the platform-specific method  
// to find and load the certificate as an instance of `X509Certificate2`.  
// For .NET Core / .NET Framework this can be loaded from the filesystem path.  
// For UWP, from the assets directory.  
// For iOS, from the main bundle.  
// For Android, from the assets directory.  
var certificate = GetCertificate("cert.cer");  
var config = new ReplicatorConfiguration(db, target)  
{  
    PinnedServerCertificate = certificate  
};  
```
4. Build and run your app. The replication should now run successfully over https/wss with certificate pinning.

For more on pinning certificates see the blog entry: [Certificate Pinning with Couchbase Mobile](https://blog.couchbase.com/certificate-pinning-android-with-couchbase-mobile/)

## [](#lbl-trouble)Troubleshooting

### [](#logs)Logs

As always, when there is a problem with replication, logging is your friend. You can increase the log output for activity related to replication with Sync Gateway — see [Example 15](#ex-logs).

Example 15\. Set logging verbosity

```C#
// deprecated
Database.SetLogLevel(LogDomain.Replicator, LogLevel.Verbose);
Database.SetLogLevel(LogDomain.Network, LogLevel.Verbose);
```

For more on troubleshooting with logs, see: [Using Logs](../../current/csharp/troubleshooting-logs.md).

### [](#authentication-errors)Authentication Errors

If Sync Gateway is configured with a self signed certificate but your app points to a `ws` scheme instead of `wss` you will encounter an error with status code `11006` — see: [Example 16](#ex-11006)

Example 16\. Protocol Mismatch

```console
CouchbaseLite Replicator ERROR: {Repl#2} Got LiteCore error: WebSocket error 1006 "connection closed abnormally"
```

If Sync Gateway is configured with a self signed certificate, and your app points to a `wss` scheme but the replicator configuration isn’t using the certificate you will encounter an error with status code `5011` — see: [Example 17](#ex-5011)

Example 17\. Certificate Mismatch or Not Found

```text
CouchbaseLite Replicator ERROR: {Repl#2} Got LiteCore error: Network error 11 "server TLS certificate is self-signed or has unknown root cert"
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](#couchbase-lite:csharp:gs-prereqs.adoc)
* [Install](../../current/csharp/gs-install.md)
* [Build and Run](../../current/csharp/gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](../../current/csharp/database.md)
* [Documents](../../current/csharp/document.md)
* [Blobs](../../current/csharp/blob.md)
* [Remote Sync using Sync Gateway](../../current/csharp/replication.md)
* [Handling Data Conflicts](../../current/csharp/conflict.md)

###### [](#-3)

Dive Deeper . . .

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

---

[1](#%5Ffootnoteref%5F1). Couchbase Mobile 2.5+ 

[2](#%5Ffootnoteref%5F2). From 2.0