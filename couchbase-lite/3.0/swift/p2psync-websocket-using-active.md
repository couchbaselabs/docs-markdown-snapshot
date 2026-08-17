---
title: Active Peer
description: Couchbase Lite's Peer-to-Peer Synchronization enables edge devices
  to synchronize securely without consuming centralized cloud-server resources
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/swift/pages/p2psync-websocket-using-active.adoc
  xref: xref:3.0@couchbase-lite:swift:p2psync-websocket-using-active.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/swift/p2psync-websocket-using-active.html)

# Active Peer

> Description — _Couchbase Lite's Peer-to-Peer Synchronization enables edge devices to synchronize securely without consuming centralized cloud-server resources_  
> _Abstract — How to set up a Replicator to connect with a Listener and replicate changes using peer-to-peer sync_  
> Related Content — [API Reference](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift) | [Passive Peer](p2psync-websocket-using-passive.md) | [Active Peer](p2psync-websocket-using-active.md)

> [!NOTE]
> Code Snippets
> 
> All code examples are indicative only. They demonstrate the basic concepts and approaches to using a feature. Use them as inspiration and adapt these examples to best practice when developing applications for your platform.

## [](#introduction)Introduction

This content provides sample code and configuration examples covering the implementation of [Peer-to-Peer Sync](refer-glossary.md#peer-to-peer-sync) over websockets. Specifically it covers the implementation of an [Active Peer](refer-glossary.md#active-peer).

This _active peer_ (also referred to as a client and-or a replicator) will initiate connection with a [Passive Peer](refer-glossary.md#passive-peer) (also referred to as a server and-or listener) and participate in the replication of database changes to bring both databases into sync.

Subsequent sections provide additional details and examples for the main configuration options.

> [!NOTE]
> Secure Storage
> 
> The use of TLS, its associated keys and certificates requires using secure storage to minimize the chances of a security breach. The implementation of this storage differs from platform to platform — see [Using secure storage](p2psync-websocket.md#using-secure-storage).

## [](#configuration-summary)Configuration Summary

You should configure and initialize a replicator for each Couchbase Lite database instance you want to sync. [Example 1](#simple-replication-to-listener) shows the initialization and configuration process.

Example 1\. Replication configuration and initialization

```swift

guard let targetURL = URL(string: "wss://10.1.1.12:8092/otherDB") else {
    fatalError("Invalid URL")
}
let targetEndpoint = URLEndpoint(url: targetURL)
var config = ReplicatorConfiguration(database: database, target: targetEndpoint) (1)

config.replicatorType = .pushAndPull

// Configure Sync Mode
config.continuous = true

// Configure Server Security -- only accept self-signed certs
config.acceptOnlySelfSignedServerCertificate = true; (2)

// Configure Client Security (3)
//  Set Authentication Mode
config.authenticator = BasicAuthenticator(username: "cbl-user-01",
                                          password: "secret")

/* Optionally set custom conflict resolver call back
 config.conflictResolver = LocalWinConflictResolver()  (4)
 */

// Apply configuration settings to the replicator
self.replicator = Replicator.init( config: config) (5)

// Optionally add a change listener
// Retain token for use in deletion
let token = self.replicator.addChangeListener { change in (6)
    if change.status.activity == .stopped {
        print("Replication stopped")
    } else {
        print("Replicator is currently : \(self.replicator.status.activity)")
    }
}

// Run the replicator using the config settings
self.replicator.start()  (7)
```

| **1** | Configure how the client will authenticate the server. Here we say connect only to servers presenting a self-signed certificate. By default, clients accept only servers presenting certificates that can be verified using the OS bundled Root CA Certificates — see: [Authenticating the Listener](#authenticate-listener). |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Configure the credentials the client will present to the server. Here we say to provide _Basic Authentication_ credentials. Other options are available — see: [Example 7](#configuring-client-authentication).                                                                                                               |
| **3** | Configure how the replication should perform [Conflict Resolution](#conflict-resolution).                                                                                                                                                                                                                                     |
| **4** | Initialize the replicator using your configuration object.                                                                                                                                                                                                                                                                    |
| **5** | Register an observer, which will notify you of changes to the replication status.                                                                                                                                                                                                                                             |
| **6** | Start the replicator.                                                                                                                                                                                                                                                                                                         |

## [](#api-references)API References

You can find [Swift API References](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift) here.

## [](#device-discovery)Device Discovery

**This phase is optional:** If the listener is initialized on a well known URL endpoint (for example, a static IP Address or well known DNS address) then you can configure active peers to connect to those.

Prior to connecting with a listener you may execute a peer discovery phase to dynamically discover peers.

For the active peer this involves browsing-for and selecting the appropriate service using a zero-config protocol such as _Bonjour_\-- see: <https://developer.apple.com/bonjour/>.

## [](#configure-replicator)Configure Replicator

In this section

[Configure Target](#lbl-cfg-tgt)| [Sync Mode](#lbl-cfg-sync)| [Retry Configuration](#lbl-cfg-retry)| [Authenticating the Listener](#authenticate-listener)| [Client Authentication](#lbl-authclnt)

### [](#lbl-cfg-tgt)Configure Target

Use the Initialize and define the replication configuration with local and remote database locations using the [ReplicatorConfiguration](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/ReplicatorConfiguration.html) object.

The constructor provides:

* the name of the local database to be sync'd
* the server's URL (including the port number and the name of the remote database to sync with)  
It is expected that the app will identify the IP address and URL and append the remote database name to the URL endpoint, producing for example: `wss://10.0.2.2:4984/travel-sample`  
The URL scheme for web socket URLs uses `ws:` (non-TLS) or `wss:` (SSL/TLS) prefixes.

Example 2\. Add Target to Configuration

```swift
let tgtUrl = URL(string: "wss://10.1.1.12:8092/travel-sample")!
let targetEndpoint = URLEndpoint(url: tgtUrl)
var config = ReplicatorConfiguration(database: database!, target: targetEndpoint) (1)
```

| **1** | Note use of the scheme prefix (wss://to ensure TLS encryption — strongly recommended in production — or ws://) |
| ----- | -------------------------------------------------------------------------------------------------------------- |

### [](#lbl-cfg-sync)Sync Mode

Here we define the direction and type of replication we want to initiate.

We use `[ReplicatorConfiguration](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/ReplicatorConfiguration.html)` class's [replicatorType](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/ReplicatorConfiguration.html#/s:18CouchbaseLiteSwift23ReplicatorConfigurationC14replicatorTypeAA0dG0Ovp) and `[continuous](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/ReplicatorConfiguration.html#/s:18CouchbaseLiteSwift23ReplicatorConfigurationC10continuousSbvp)` parameters, to tell the replicator:

* The type (or direction) of the replication: `**pushAndPull**`; `pull`; `push`
* The replication mode, that is either of:

  * Continuous — remaining active indefinitely to replicate changed documents (`continuous=true`).
  * Ad-hoc — a one-shot replication of changed documents (`continuous=false`).

Example 3\. Configure replicator type and mode

```swift
config.replicatorType = .pushAndPull

// Configure Sync Mode
config.continuous = true
```

> [!TIP]
> Unless there is a solid use-case not to, always initiate a single `PUSH_AND_PULL` replication rather than identical separate `PUSH` and `PULL` replications.
> 
> This prevents the replications generating the same checkpoint `docID` resulting in multiple conflicts.

### [](#lbl-cfg-retry)Retry Configuration

Couchbase Lite for Swift's replication retry logic assures a resilient connection.

The replicator minimizes the chance and impact of dropped connections by maintaining a heartbeat; essentially pinging the listener at a configurable interval to ensure the connection remains alive.

In the event it detects a transient error, the replicator will attempt to reconnect, stopping only when the connection is re-established, or the number of retries exceeds the retry limit (9 times for a single-shot replication and unlimited for a continuous replication).

On each retry the interval between attempts is increased exponentially (exponential backoff) up to the maximum wait time limit (5 minutes).

The REST API provides configurable control over this replication retry logic using a set of configiurable properties — see: [Table 1](#tbl-repl-retry).

__Table 1\. Replication Retry Configuration Properties__
| Property                                                                                                                                                                                            | Use cases                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [heartbeat()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/ReplicatorConfiguration.html#/s:18CouchbaseLiteSwift23ReplicatorConfigurationC9heartbeatSdvp)                    | Reduce to detect connection errors sooner Align to load-balancer or proxy keep-alive interval — see Sync Gateway's topic [Load Balancer - Keep Alive](../../../sync-gateway/current/deploy/load-balancer.md#websocket-connection) | The interval (in seconds) between the heartbeat pulses. Default: The replicator pings the listener every 300 seconds.                                                                                                                                                                                                                                |
| [maxAttempts()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/ReplicatorConfiguration.html#/s:18CouchbaseLiteSwift23ReplicatorConfigurationC10maxAttemptsSivp)               | Change this to limit or extend the number of retry attempts.                                                                                                                                                                      | The maximum number of retry attempts Set this to zero (0) to prevent any retry attempt The retry attempt count is reset when the replicator is able to connect and replicate Default values are: Single-shot replication = 9; Continuous replication = maximum integer value Negative values generate a Couchbase exception InvalidArgumentException |
| [maxAttemptWaitTime()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/ReplicatorConfiguration.html#/s:18CouchbaseLiteSwift23ReplicatorConfigurationC16maxAttemptWaitTimeSdvp) | Change this to adjust the interval between retries.                                                                                                                                                                               | The maximum interval between retry attempts Whilst you can configure the **maximum permitted** wait time, each individual interval is calculated by the replicator's exponential backoff algorithm and is not configurable. Default value: 300 seconds (5 minutes) Zero or negative values generate a Couchbase exception, InvalidArgumentException. |

When necessary you can adjust any or all of those configurable values — see: [Example 4](#ex-repl-retry) for how to do this.

Example 4\. Configuring Replication Retries

```swift
let target = URLEndpoint(url: URL(string: "ws://foo.couchbase.com/db")!)

var config =  ReplicatorConfiguration(database: database, target: target)
config.replicatorType = .pushAndPull
config.continuous = true
config.heartbeat = 150 (1)

config.maxAttempts = 20 (2)

config.maxAttemptWaitTime = 600 (3)
self.replicator = Replicator(config: config)
```

| **1** | Here we use [heartbeat()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/ReplicatorConfiguration.html#/s:18CouchbaseLiteSwift23ReplicatorConfigurationC9heartbeatSdvp) to set the required interval (in seconds) between the heartbeat pulses  |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Here we use [maxAttempts()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/ReplicatorConfiguration.html#/s:18CouchbaseLiteSwift23ReplicatorConfigurationC10maxAttemptsSivp) to set the required number of retry attempts                       |
| **3** | Here we use [maxAttemptWaitTime()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/ReplicatorConfiguration.html#/s:18CouchbaseLiteSwift23ReplicatorConfigurationC16maxAttemptWaitTimeSdvp) to set the required interval between retry attempts. |

### [](#authenticate-listener)Authenticating the Listener

Define the credentials the your app (the client) is expecting to receive from the server (listener) in order to ensure that the server is one it is prepared to interact with.

Note that the client cannot authenticate the server if TLS is turned off. When TLS is enabled (Sync Gateway's default) the client _must_ authenticate the server. If the server cannot provide acceptable credentials then the connection will fail.

Use `[ReplicatorConfiguration](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/ReplicatorConfiguration.html)` properties [acceptOnlySelfSignedServerCertificate](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/ReplicatorConfiguration.html#/s:18CouchbaseLiteSwift23ReplicatorConfigurationC37acceptOnlySelfSignedServerCertificateSbvp) and [setPinnedServerCertificate()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/ReplicatorConfiguration.html#/s:18CouchbaseLiteSwift23ReplicatorConfigurationC23pinnedServerCertificateSo03SecH3RefaSgvp), to tell the replicator how to verify server-supplied TLS server certificates.

* If there is a pinned certificate, nothing else matters, the server cert must **exactly** match the pinned certificate.
* If there are no pinned certs and [acceptOnlySelfSignedServerCertificate](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/ReplicatorConfiguration.html#/s:18CouchbaseLiteSwift23ReplicatorConfigurationC37acceptOnlySelfSignedServerCertificateSbvp) is `true` then any self-signed certificate is accepted. Certificates that are not self signed are rejected, no matter who signed them.
* If there are no pinned certificates and [acceptOnlySelfSignedServerCertificate](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/ReplicatorConfiguration.html#/s:18CouchbaseLiteSwift23ReplicatorConfigurationC37acceptOnlySelfSignedServerCertificateSbvp) is `false` (default), the client validates the server's certificates against the system CA certificates. The server must supply a chain of certificates whose root is signed by one of the certificates in the system CA bundle.

Example 5\. Set Server TLS security

* CA Cert
* Self Signed Cert
* Pinned Certificate

Set the client to expect and accept only CA attested certificates.

```swift
// Configure Server Security -- only accept CA Certs
config.acceptOnlySelfSignedServerCertificate = false (1)
```

| **1** | This is the default. Only certificate chains with roots signed by a trusted CA are allowed. Self signed certificates are not allowed. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------- |

Set the client to expect and accept only self-signed certificates

```swift
// Configure Server Security -- only accept self-signed certs
config.acceptOnlySelfSignedServerCertificate = true; (1)

// Configure Server Security -- only accept self-signed certs
config.acceptOnlySelfSignedServerCertificate = true (2)
```

| **1** | Set this to true to accept any self signed cert. Any certificates that are not self-signed are rejected. |
| ----- | -------------------------------------------------------------------------------------------------------- |

Set the client to expect and accept only a pinned certificate.

```swift

// Get bundled resource and read into localcert
guard
    let pathToCert = Bundle.main.path(forResource: "listener-pinned-cert", ofType: "cer"),
    let localCertificate:NSData = NSData(contentsOfFile: pathToCert)
else { /* process error */ return }

// Create certificate
// using its DER representation as a CFData
guard
    let pinnedCert = SecCertificateCreateWithData(nil, localCertificate)
else { /* process error */  return }

// Add `pinnedCert` and `acceptOnlySelfSignedServerCertificate=false`(by default)
// to `ReplicatorConfiguration`
config.pinnedServerCertificate = pinnedCert
```

### [](#lbl-authclnt)Client Authentication

Here we define the credentials that the client can present to the server if prompted to do so in order that the server can authenticate it.

We use [ReplicatorConfiguration](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/ReplicatorConfiguration.html)'s [authenticator](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/ReplicatorConfiguration.html#/s:18CouchbaseLiteSwift23ReplicatorConfigurationC13authenticatorAA13Authenticator%5FpSgvp) method to define the authentication method to the replicator.

#### [](#basic-authentication)Basic Authentication

Use the `[BasicAuthenticator](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/BasicAuthenticator.html)` to supply basic authentication credentials (username and password).

Example 6\. Basic Authentication

This example shows basic authentication using user name and password:

```swift
//  Set Authentication Mode
config.authenticator = BasicAuthenticator(username: "cbl-user-01",
                                          password: "secret")

//  Set Authentication Mode
config.authenticator = BasicAuthenticator(username: validUsername, password: validPassword)
```

#### [](#certificate-authentication)Certificate Authentication

Use the `[ClientCertificateAuthenticator](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/ClientCertificateAuthenticator.html)` to configure the client TLS certificates to be presented to the server, on connection. This applies only to the [URLEndpointListener](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Classes/URLEndpointListener.html).

> [!NOTE]
> The **server** (listener) must have `disableTLS` set `false` and have a [ClientCertificateAuthenticator](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/ClientCertificateAuthenticator.html) configured, or it will never ask for this client's certificate.

The certificate to be presented to the server will need to be signed by the root certificates or be valid based on the authentication callback set to the listener via ListenerCertificateAuthenticator.

Example 7\. Client Cert Authentication

This example shows client certificate authentication using an identity from secure storage.

```swift
// Check if Id exists in keychain and if so, use that Id
if let tlsIdentity = try TLSIdentity.identity(withLabel: "doco-sync-server") { (1)
    print("An identity with label : doco-sync-server already exists in keychain")
    config.authenticator = ClientCertificateAuthenticator(identity: tlsIdentity) (2)
}
```

| **1** | Get an identity from secure storage and create a TLS Identity object                                                                                                                                               |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | Set the authenticator to [ClientCertificateAuthenticator](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/ClientCertificateAuthenticator.html) and configure it to use the retrieved identity |

## [](#initialize-replicator)Initialize Replicator

Use the `[Replicator](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Classes/Replicator.html)` class's [init(config:)](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Classes/Replicator.html#/s:18CouchbaseLiteSwift10ReplicatorC6configAcA0D13ConfigurationC%5Ftcfc) constructor, to initialize the replicator with the configuration you have defined. You can, optionally, add a change listener (see [Monitor Sync](#lbl-repl-mon)) before starting the replicator running using [start()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Classes/Replicator.html#/s:18CouchbaseLiteSwift10ReplicatorC5startyyF).

Example 8\. Initialize and run replicator

```swift
// Apply configuration settings to the replicator
self.replicator = Replicator.init( config: config) (1)


// Run the replicator using the config settings
self.replicator.start()  (2)
```

| **1** | Initialize the replicator with the configuration |
| ----- | ------------------------------------------------ |
| **2** | Start the replicator                             |

## [](#lbl-repl-mon)Monitor Sync

In this section

[Change Listeners](#lbl-repl-chng) | [Replicator Status](#lbl-repl-status) | [Documents Pending Push](#lbl-repl-pend)

You can monitor a replication's status by using a combination of [Change Listeners](#lbl-repl-chng) and the `replication.status.activity` property — see; [Activity](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Classes/Replicator/Status.html#/s:18CouchbaseLiteSwift10ReplicatorC6StatusV8activityAC13ActivityLevelOvp). This enables you to know, for example, when the replication is actively transferring data and when it has stopped.

### [](#lbl-repl-chng)Change Listeners

Use this to monitor changes and to inform on sync progress; this is an optional step. You can add and a replicator change listener at any point; it will report changes from the point it is registered.

> [!TIP]
> Best Practice
> 
> Don't forget to save the token so you can remove the listener later

Use the [Replicator](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Classes/Replicator.html) class to add a change listener as a callback to the Replicator ([addChangeListener(\_:)](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Classes/Replicator.html#/s:18CouchbaseLiteSwift10ReplicatorC17addChangeListeneryAA0G5TokenCyAA0dF0VcF)) — see: [Example 9](#ex-repl-mon). You will then be asynchronously notified of state changes.

You can remove a change listener with [removeChangeListener(withToken:)](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Classes/Replicator.html#//s:18CouchbaseLiteSwift10ReplicatorC20removeChangeListener9withTokenyAA0gI0C%5FtF).

### [](#lbl-repl-status)Replicator Status

You can use the [Replicator](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Classes/Replicator.html) class's [Status](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Classes/Replicator/Status.html#/s:18CouchbaseLiteSwift10ReplicatorC6Status) property to check the replicator status. That is, whether it is actively transferring data or if it has stopped — see: [Example 9](#ex-repl-mon).

The returned _ReplicationStatus_ structure comprises:

* [Activity](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Classes/Replicator/Status.html#/s:18CouchbaseLiteSwift10ReplicatorC6StatusV8activityAC13ActivityLevelOvp) — stopped, offline, connecting, idle or busy — see states described in: [Table 2](#tbl-states)
* [Progress](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Classes/Replicator/Status.html#/s:18CouchbaseLiteSwift10ReplicatorC6StatusV8progressAC8ProgressVvp)

  * completed — the total number of changes completed
  * total — the total number of changes to be processed
* [Error](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Classes/Replicator/Status.html#/s:18CouchbaseLiteSwift10ReplicatorC6StatusV5errors5Error%5FpSgvp) — the current error, if any

Example 9\. Monitor replication

* Adding a Change Listener
* Using replicator.status

```swift
// Optionally add a change listener
// Retain token for use in deletion
let token = self.replicator.addChangeListener { change in (1)
    if change.status.activity == .stopped {
        print("Replication stopped")
    } else {
        print("Replicator is currently : \(self.replicator.status.activity)")
    }
}
```

```swift
        print("Replicator is currently : \(self.replicator.status.activity)")
    }
}
```

#### [](#lbl-repl-states)Replication States

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

#### [](#replication-status-and-app-life-cycle)Replication Status and App Life Cycle

The following diagram describes the status changes when the application starts a replication, and when the application is being backgrounded or foregrounded by the OS. It applies to iOS only.

![replicator states](_images/replicator-states.png) 

Additionally, on iOS, an app already in the background may be terminated. In this case, the `Database` and `Replicator` instances will be `null` when the app returns to the foreground. Therefore, as preventive measure, it is recommended to do a `null` check when the app enters the foreground, and to re-initialize the database and replicator if any of those is `null`.

On other platforms, Couchbase Lite doesn't react to OS backgrounding or foregrounding events and replication(s) will continue running as long as the remote system does not terminate the connection and the app does not terminate. It is generally recommended to stop replications before going into the background otherwise socket connections may be closed by the OS and this may interfere with the replication process.

### [](#lbl-repl-pend)Documents Pending Push

> [!TIP]
> [Replicator.isDocumentPending()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Classes/Replicator.html#/s:18CouchbaseLiteSwift10ReplicatorC17isDocumentPendingySbSSKF) is quicker and more efficient. Use it in preference to returning a list of pending document IDs, where possible.

You can check whether documents are waiting to be pushed in any forthcoming sync by using either of the following API methods:

* Use the [Replicator.pendingDocumentIds()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Classes/Replicator.html#/s:18CouchbaseLiteSwift10ReplicatorC18pendingDocumentIdsShySSGyKF) method, which returns a list of document IDs that have local changes, but which have not yet been pushed to the server.  
This can be very useful in tracking the progress of a push sync, enabling the app to provide a visual indicator to the end user on its status, or decide when it is safe to exit.
* Use the [Replicator.isDocumentPending()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Classes/Replicator.html#/s:18CouchbaseLiteSwift10ReplicatorC17isDocumentPendingySbSSKF) method to quickly check whether an individual document is pending a push.

Example 10\. Use Pending Document ID API

```swift

let url = URL(string: "ws://localhost:4984/mydatabase")!
let target = URLEndpoint(url: url)

var config = ReplicatorConfiguration(database: database, target: target)
config.replicatorType = .push

self.replicator = Replicator(config: config)
let myDocIDs = try self.replicator.pendingDocumentIds() (1)

if(!myDocIDs.isEmpty) {
    print("There are \(myDocIDs.count) documents pending")
    let thisID = myDocIDs.first!

    self.replicator.addChangeListener { (change) in
        print("Replicator activity level is \(change.status.activity)")
        do {
            let isPending = try self.replicator.isDocumentPending(thisID)
            if(!isPending) { (2)
                print("Doc ID \(thisID) now pushed")
            }
        } catch {
            print(error)
        }
    }

    self.replicator.start()
```

| **1** | [Replicator.pendingDocumentIds()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Classes/Replicator.html#/s:18CouchbaseLiteSwift10ReplicatorC18pendingDocumentIdsShySSGyKF) returns a list of the document IDs for all documents waiting to be pushed. This is a snapshot and may have changed by the time the response is received and processed. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [Replicator.isDocumentPending()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Classes/Replicator.html#/s:18CouchbaseLiteSwift10ReplicatorC17isDocumentPendingySbSSKF) returns true if the document is waiting to be pushed, and false otherwise.                                                                                                 |

## [](#lbl-repl-stop)Stop Sync

Stopping a replication is straightforward. It is done using [stop()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Classes/Replicator.html#/s:18CouchbaseLiteSwift10ReplicatorC4stopyyF). This initiates an asynchronous operation and so is not necessarily immediate. Your app should account for this potential delay before attempting any subsequent operations.

You can find further information on database operations in [Databases](database.md).

Example 11\. Stop replicator

```swift

// Remove the change listener
self.replicator.removeChangeListener(withToken: token)

// Stop the replicator
self.replicator.stop()
```

| **1** | Here we initiate the stopping of the replication using the [stop()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Classes/Replicator.html#/s:18CouchbaseLiteSwift10ReplicatorC4stopyyF) method. It will stop any active [change listener](#lbl-repl-chng) once the replication is stopped. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#conflict-resolution)Conflict Resolution

Unless you specify otherwise, Couchbase Lite's default conflict resolution policy is applied — see [Handling Data Conflicts](conflict.md).

To use a different policy, specify a _conflict resolver_ using [conflictResolver](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Structs/ReplicatorConfiguration.html#/s:18CouchbaseLiteSwift23ReplicatorConfigurationC16conflictResolverAA08ConflictG8Protocol%5FpSgvp) as shown in [Example 12](#using-conflict-resolvers).

For more complex solutions you can provide a custom conflict resolver - see: [Handling Data Conflicts](conflict.md).

Example 12\. Using conflict resolvers

* Local Wins
* Remote Wins
* Merge

```swift
class LocalWinConflictResolver: ConflictResolverProtocol {
    func resolve(conflict: Conflict) -> Document? {
        return conflict.localDocument
    }
}
```

```swift
class RemoteWinConflictResolver: ConflictResolverProtocol {
    func resolve(conflict: Conflict) -> Document? {
        return conflict.remoteDocument
    }
}
```

```swift
class MergeConflictResolver: ConflictResolverProtocol {
    func resolve(conflict: Conflict) -> Document? {
        let localDict = conflict.localDocument!.toDictionary()
        let remoteDict = conflict.remoteDocument!.toDictionary()
        let result = localDict.merging(remoteDict) { (current, new) -> Any in
            return current // return current value in case of duplicate keys
        }
        return MutableDocument(id: conflict.documentID, data: result)
    }
}
```

Just as a replicator may observe a conflict — when updating a document that has changed both in the local database and in a remote database — any attempt to save a document may also observe a conflict, if a replication has taken place since the local app retrieved the document from the database. To address that possibility, a version of the `Database.save()` method also takes a conflict resolver as shown in [Example 13](#ex-merge-props).

The following code snippet shows an example of merging properties from the existing document (`current`) into the one being saved (`new`). In the event of conflicting keys, it will pick the key value from `new`.

Example 13\. Merging document properties

```swift
guard let document = database.document(withID: "xyz") else { return }
let mutableDocument = document.toMutable()
mutableDocument.setString("apples", forKey: "name")
try database.saveDocument(mutableDocument, conflictHandler: { (new, current) -> Bool in
    let currentDict = current!.toDictionary()
    let newDict = new.toDictionary()
    let result = newDict.merging(currentDict, uniquingKeysWith: { (first, _) in first })
    new.setData(result)
    return true
})
```

For more on replicator conflict resolution see: [Handling Data Conflicts](conflict.md).

## [](#delta-sync)Delta Sync

If delta sync is enabled on the listener, then replication will use delta sync.

## [](#related-content)Related Content

###### [](#)

How to

* [Passive Peer](p2psync-websocket-using-passive.md)
* [Active Peer](p2psync-websocket-using-active.md)

###### [](#-2)

Concepts

* [Peer-to-Peer Sync](#swift:landing-p2psync.adoc)
* [API References](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift)

###### [](#-3)

Community Resources …​

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

[Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)