---
title: Active Peer
description: Couchbase Lite's Peer-to-Peer Synchronization enables edge devices
  to synchronize securely without consuming centralized cloud-server resources
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/csharp/pages/p2psync-websocket-using-active.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@couchbase-lite:csharp:p2psync-websocket-using-active.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/csharp/p2psync-websocket-using-active.html)

# Active Peer

> Description — _Couchbase Lite’s Peer-to-Peer Synchronization enables edge devices to synchronize securely without consuming centralized cloud-server resources_  
> _Abstract — How to set up a Replicator to connect with a Listener and replicate changes using peer-to-peer sync_  
> Related Content — [API Reference](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net) | [Passive Peer](../../current/csharp/p2psync-websocket-using-passive.md) | [Active Peer](../../current/csharp/p2psync-websocket-using-active.md)

> [!IMPORTANT]
> Enterprise Edition only
> 
> This an [Enterprise Edition](https://www.couchbase.com/products/editions) feature. Purchase the _Enterprise License_, which includes official [Couchbase Support](https://www.couchbase.com/support-policy), to use it in production (see the license and support <https://www.couchbase.com/licensing-and-support-faq>).

> [!NOTE]
> Code Snippets
> 
> The code examples are indicative only. They demonstrate basic concepts and approaches to using a feature. Use them as inspiration and adapt these examples to best practice when developing applications for your platform.

## [](#introduction)Introduction

This content provides sample code and configuration examples covering the implementation of [Peer-to-Peer Sync](../../current/csharp/refer-glossary.md#peer-to-peer-sync) over websockets. Specifically it covers the implementation of an [Active Peer](../../current/csharp/refer-glossary.md#active-peer).

This _active peer_ (also referred to as a client and-or a replicator) will initiate connection with a [Passive Peer](../../current/csharp/refer-glossary.md#passive-peer) (also referred to as a server and-or listener) and participate in the replication of database changes to bring both databases into sync.

Subsequent sections provide additional details and examples for the main configuration options.

> [!NOTE]
> Secure Storage
> 
> The use of TLS, its associated keys and certificates requires using secure storage to minimize the chances of a security breach. The implementation of this storage differs from platform to platform — see [Using secure storage](../../current/csharp/p2psync-websocket.md#using-secure-storage).

## [](#configuration-summary)Configuration Summary

You should configure and initialize a replicator for each Couchbase Lite database instance you want to sync. [Example 1](#simple-replication-to-listener) shows the initialization and configuration process.

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

| **1** | Use the [ReplicatorConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorConfiguration.html) class’s constructor — [ReplicatorConfiguration(Database database, IEndpoint target)](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorConfiguration.html#Couchbase%5FLite%5FSync%5FReplicatorConfiguration%5F%5Fctor%5FCouchbase%5FLite%5FDatabase%5FCouchbase%5FLite%5FSync%5FIEndpoint) — to initialize the replicator configuration with the local database — see also: [\[configure-target\]](#configure-target) |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Configure how the client will authenticate the server. Here we say connect only to servers presenting a self-signed certificate. By default, clients accept only servers presenting certificates that can be verified using the OS bundled Root CA Certificates — see: [\[authenticating-the-listener\]](#authenticating-the-listener).                                                                                                                                                                                                                                                                           |
| **3** | Configure the credentials the client will present to the server. Here we say to provide _Basic Authentication_ credentials. Other options are available — see: [\[client-authentication\]](#client-authentication).                                                                                                                                                                                                                                                                                                                                                                                               |
| **4** | Configure how the replication should perform [Conflict Resolution](#conflict-resolution).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **5** | Initialize the replicator using your configuration object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **6** | Register an observer, which will notify you of changes to the replication status.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **7** | Start the replicator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## [](#api-references)API References

You can find [C#.Net API References](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net) here.

## [](#device-discovery)Device Discovery

**This phase is optional:** If the listener is initialized on a well known URL endpoint (for example, a static IP Address or well known DNS address) then you can configure active peers to connect to those.

Prior to connecting with a listener you may execute a peer discovery phase to dynamically discover peers.

## [](#configure-replicator)Configure Replicator

In this section

[Configure Target](#lbl-cfg-tgt) | [Sync Mode](#lbl-cfg-sync) | [Heartbeat](#lbl-cfg-htbt) | [Authenticating the Listener](#lbl-auth-lstnr) | [Client Authentication](#lbl-authclnt)

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

### [](#lbl-cfg-htbt)Heartbeat

A point to consider when initiating a replication, particularly a continuous replication, is keeping the connection alive. Couchbase Lite minimizes the chance of dropped connections by having the replicator maintain a heartbeat; essentially pinging the listener at a configurable interval.

When necessary you can adjust this interval using [Heartbeat()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorConfiguration.html#Couchbase%5FLite%5FSync%5FReplicatorConfiguration%5FHeartbeat) as shown in — [Example 4](#ex-htbt).

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

### [](#lbl-auth-lstnr)Authenticating the Listener

Define the credentials the your app (the client) is expecting to receive from the server (listener) in order to ensure that the server is one it is prepared to interact with.

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

### [](#lbl-authclnt)Client Authentication

Here we define the credentials that the client can present to the server if prompted to do so in order that the server can authenticate it.

We use [ReplicatorConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorConfiguration.html)'s [Authenticator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorConfiguration.html#Couchbase%5FLite%5FSync%5FReplicatorConfiguration%5FAuthenticator) method to define the authentication method to the replicator - see [Example 7](#configuring-client-authentication).

#### [](#basic-authentication)Basic Authentication

Use the `[BasicAuthenticator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.BasicAuthenticator.html)` to supply basic authentication credentials (username and password).

Example 6\. Basic Authentication

This example shows basic authentication using user name and password:

```C#
// Configure basic auth using user credentials
thisConfig.Authenticator = new BasicAuthenticator("Our Username", "Our Password");

// Configure basic auth using user credentials
thisConfig.Authenticator = new BasicAuthenticator("Our Username", "Our Password");
```

#### [](#certificate-authentication)Certificate Authentication

Use the `[ClientCertificateAuthenticator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.P2P.ClientCertificateAuthenticator.html)` to configure the client TLS certificates to be presented to the server, on connection. This applies only to the [URLEndpointListener](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.P2P.URLEndpointListener.html).

> [!NOTE]
> The **server** (listener) must have `disableTLS` set `false` and have a [ClientCertificateAuthenticator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.P2P.ClientCertificateAuthenticator.html) configured, or it will never ask for this client’s certificate.

The certificate to be presented to the server will need to be signed by the root certificates or be valid based on the authentication callback set to the listener via ListenerCertificateAuthenticator.

Example 7\. Client Cert Authentication

This example shows client certificate authentication using an identity from secure storage.

```C#
// Client identity
thisIdentity =
  TLSIdentity.ImportIdentity(_store,
    clientData,
    "123",
    "CBL-Client-Cert",
    null); (1)

thisConfig.Authenticator =
  new ClientCertificateAuthenticator(thisIdentity); (2)
```

**Notes on Example**

| **1** | Get an identity from secure storage and create a TLS Identity object                                                                                                                                                           |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | Set the authenticator to [ClientCertificateAuthenticator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.P2P.ClientCertificateAuthenticator.html) and configure it to use the retrieved identity |

## [](#initialize-replicator)Initialize Replicator

Use the `[Replicator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html)` class’s [(ReplicatorConfiguration config)](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5F%5Fctor%5FCouchbase%5FLite%5FSync%5FReplicatorConfiguration%5F) constructor, to initialize the replicator with the configuration you have defined. You can, optionally, add a change listener (see [Monitor Sync](#lbl-repl-mon)) before starting the replicator running using [Start()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5FStart).

Example 8\. Initialize and run replicator

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

## [](#lbl-repl-mon)Monitor Sync

In this section

[Change Listeners](#lbl-repl-chng) | [Replicator Status](#lbl-repl-status) | [Documents Pending Push](#lbl-repl-pend)

In this section

[Change Listeners](#lbl-repl-chng) | [Replicator Status](#lbl-repl-status) | [\[lbl-repl-evnts\]](#lbl-repl-evnts) | [Documents Pending Push](#lbl-repl-pend)

You can monitor a replication’s status by using a combination of [Change Listeners](#lbl-repl-chng) and the `replication.status.activity` property — see; [Activity](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorStatus.html#Couchbase%5FLite%5FSync%5FReplicatorStatus%5FActivity). This enables you to know, for example, when the replication is actively transferring data and when it has stopped.

You can also choose to monitor document changes — see: [\[lbl-repl-evnts\]](#lbl-repl-evnts).

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

### [](#lbl-repl-pend)Documents Pending Push

> [!TIP]
> [Replicator.IsDocumentPending()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5FIsDocumentPending%5FSystem%5FString%5F) is quicker and more efficient. Use it in preference to returning a list of pending document IDs, where possible.

You can check whether documents are waiting to be pushed in any forthcoming sync by using either of the following API methods:

* Use the [Replicator.GetPendingDocumentIDs()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5FGetPendingDocumentIDs) method, which returns a list of document IDs that have local changes, but which have not yet been pushed to the server.  
This can be very useful in tracking the progress of a push sync, enabling the app to provide a visual indicator to the end user on its status, or decide when it is safe to exit.
* Use the [Replicator.IsDocumentPending()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5FIsDocumentPending%5FSystem%5FString%5F) method to quickly check whether an individual document is pending a push.

Example 10\. Use Pending Document ID API

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

## [](#lbl-repl-stop)Stop Sync

Stopping a replication is straightforward. It is done using [Stop()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5FStop). This initiates an asynchronous operation and so is not necessarily immediate. Your app should account for this potential delay before attempting any subsequent operations, for example closing the database.

You can find further information on database operations in [Databases](../../current/csharp/database.md).

> [!TIP]
> Best Practice
> 
> 1. When you start a change listener, save the returned token, you will need it when you remove the listener
> 2. You can ensure the replication has completely stopped by checking for a replication status = STOPPED

Example 11\. Stop replicator

```C#
// Stop replication.
thisReplicator.Stop(); (1)
```

| **1** | Here we initiate the stopping of the replication using the [Stop()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5FStop) method. We can then remove any active [change listener](#lbl-repl-chng). |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#conflict-resolution)Conflict Resolution

Unless you specify otherwise, Couchbase Lite’s default conflict resolution policy is applied — see [Automatic Conflict Resolution](#couchbase-lite:csharp:{cbl-pg-conflict-auto}).

To use a different policy, specify a _conflict resolver_ using [ConflictResolver](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.ReplicatorConfiguration.html#Couchbase%5FLite%5FSync%5FReplicatorConfiguration%5FConflictResolver) as shown in [Example 12](#using-conflict-resolvers).

For more complex solutions you can provide a custom conflict resolver - see: [Custom Conflict Resolution](#couchbase-lite:csharp:{cbl-pg-conflict-custom}).

Example 12\. Using conflict resolvers

* Local Wins
* Remote Wins
* Merge

```C#
class LocalWinConflictResolver : IConflictResolver
{
    Document Resolve(Conflict conflict)
    {
        return conflict.LocalDocument;
    }
}
```

```C#
class RemoteWinConflictResolver : IConflictResolver
{
    public Document Resolve(Conflict conflict)
    {
        return conflict.RemoteDocument;
    }
}
```

```C#
class MergeConflictResolver : IConflictResolver
{
    public Document Resolve(Conflict conflict)
    {
        var localDict = conflict.LocalDocument.ToDictionary();
        var remoteDict = conflict.RemoteDocument.ToDictionary();
        var result = localDict.Concat(remoteDict)
           .GroupBy(kv => kv.Key)
           .ToDictionary(g => g.Key, g => g.First().Value);
        return new MutableDocument(conflict.DocumentID, result);
    }
}
```

Just as a replicator may observe a conflict — when updating a document that has changed both in the local database and in a remote database — any attempt to save a document may also observe a conflict, if a replication has taken place since the local app retrieved the document from the database. To address that possibility, a version of the `Database.save()` method also takes a conflict resolver as shown in [\[merging-document-properties\]](#merging-document-properties).

The following code snippet shows an example of merging properties from the existing document (`current`) into the one being saved (`new`). In the event of conflicting keys, it will pick the key value from `new`.

Example 13\. Merging document properties

```C#
using (var document = database.GetDocument("xyz"))
using (var mutableDocument = document.ToMutable()) {
    mutableDocument.SetString("name", "apples");
    database.Save(mutableDocument, (updated, current) =>
    {
        var currentDict = current.ToDictionary();
        var newDict = updated.ToDictionary();
        var result = newDict.Concat(currentDict)
            .GroupBy(kv => kv.Key)
            .ToDictionary(g => g.Key, g => g.First().Value);
        updated.SetData(result);
        return true;
    });
}
```

## [](#related-content)Related Content

###### [](#)

How to

* [Passive Peer](../../current/csharp/p2psync-websocket-using-passive.md)
* [Active Peer](../../current/csharp/p2psync-websocket-using-active.md)

###### [](#-2)

Concepts

* [Landing P2Psync](#couchbase-lite:csharp:landing-p2psync.adoc)
* [API References](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net).

###### [](#-3)

Community Resources …​

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

* [Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)

For more on replicator conflict resolution see: [Handling Data Conflicts](../../current/csharp/conflict.md).

## [](#delta-sync)Delta Sync

If delta sync is enabled on the listener, then replication will use delta sync.

## [](#related-content-2)Related Content

###### [](#-4)

How to

* [Passive Peer](../../current/csharp/p2psync-websocket-using-passive.md)
* [Active Peer](../../current/csharp/p2psync-websocket-using-active.md)

###### [](#-5)

Concepts

* [Landing P2Psync](#couchbase-lite:csharp:landing-p2psync.adoc)
* [API References](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net).

###### [](#-6)

Community Resources …​

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

* [Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)