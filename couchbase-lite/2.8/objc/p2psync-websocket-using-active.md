---
title: Active Peer
description: Couchbase Lite's Peer-to-Peer Synchronization enables edge devices
  to synchronize securely without consuming centralized cloud-server resources
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/objc/pages/p2psync-websocket-using-active.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@couchbase-lite:objc:p2psync-websocket-using-active.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/objc/p2psync-websocket-using-active.html)

# Active Peer

> Description — _Couchbase Lite's Peer-to-Peer Synchronization enables edge devices to synchronize securely without consuming centralized cloud-server resources_  
> _Abstract — How to set up a Replicator to connect with a Listener and replicate changes using peer-to-peer sync_  
> Related Content — [API Reference](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc) | [Passive Peer](../../current/objc/p2psync-websocket-using-passive.md) | [Active Peer](../../current/objc/p2psync-websocket-using-active.md)

> [!IMPORTANT]
> Enterprise Edition only
> 
> This an [Enterprise Edition](https://www.couchbase.com/products/editions) feature. Purchase the _Enterprise License_, which includes official [Couchbase Support](https://www.couchbase.com/support-policy), to use it in production (see the license and support <https://www.couchbase.com/licensing-and-support-faq>).

> [!NOTE]
> Code Snippets
> 
> The code examples are indicative only. They demonstrate basic concepts and approaches to using a feature. Use them as inspiration and adapt these examples to best practice when developing applications for your platform.

## [](#introduction)Introduction

This content provides sample code and configuration examples covering the implementation of [Peer-to-Peer Sync](../../current/objc/refer-glossary.md#peer-to-peer-sync) over websockets. Specifically it covers the implementation of an [Active Peer](../../current/objc/refer-glossary.md#active-peer).

This _active peer_ (also referred to as a client and-or a replicator) will initiate connection with a [Passive Peer](../../current/objc/refer-glossary.md#passive-peer) (also referred to as a server and-or listener) and participate in the replication of database changes to bring both databases into sync.

Subsequent sections provide additional details and examples for the main configuration options.

> [!NOTE]
> Secure Storage
> 
> The use of TLS, its associated keys and certificates requires using secure storage to minimize the chances of a security breach. The implementation of this storage differs from platform to platform — see [Using secure storage](../../current/objc/p2psync-websocket.md#using-secure-storage).

## [](#configuration-summary)Configuration Summary

You should configure and initialize a replicator for each Couchbase Lite database instance you want to sync. [Example 1](#simple-replication-to-listener) shows the initialization and configuration process.

Example 1\. Replication configuration and initialization

```objc
// Set listener DB endpoint
NSURL *url = [NSURL URLWithString:@"ws://listener.com:55990/otherDB"];
CBLURLEndpoint *thisListener = [[CBLURLEndpoint alloc] initWithURL:url];

CBLReplicatorConfiguration *thisConfig
  = [[CBLReplicatorConfiguration alloc]
      initWithDatabase:thisDB target:thisListener]; (1)

thisConfig.replicatorType = kCBLReplicatorTypePush;

thisConfig.continuous = YES;

// Configure Server Authentication
// Here - expect and accept self-signed certs
thisConfig.acceptOnlySelfSignedServerCertificate = YES; (2)

// Configure Client Authentication
// Here set client to use basic authentication
// Providing username and password credentials
// If prompted for them by server
thisConfig.authenticator = [[CBLBasicAuthenticator alloc] initWithUsername:@"Our Username" password:@"Our Password"]; (3)

/* Optionally set custom conflict resolver call back */
thisConfig.conflictResolver = [[LocalWinConflictResolver alloc] (4)

// Apply configuration settings to the replicator
_thisReplicator = [[CBLReplicator alloc] initWithConfig:thisConfig]; (5)

// Optionally add a change listener (6)
// Retain token for use in deletion
id<CBLListenerToken> thisListenerToken
  = [thisReplicator addChangeListener:^(CBLReplicatorChange *thisChange) {
      if (thisChange.status.activity == kCBLReplicatorStopped) {
        NSLog(@"Replication stopped");
        } else {
        NSLog(@"Status: %d", thisChange.status.activity);
        };
    }];
// Run the replicator using the config settings
[thisReplicator start]; (7)
```

**Notes on Example**

| **1** | Use the [ReplicatorConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorConfiguration.html) class's constructor — [\-initWithDatabase:target:](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorConfiguration.html#/c:objc%28cs%29CBLReplicatorConfiguration%28im%29initWithDatabase:target:) — to initialize the replicator configuration with the local database — see also: [\[configure-target\]](#configure-target) |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Configure how the client will authenticate the server. Here we say connect only to servers presenting a self-signed certificate. By default, clients accept only servers presenting certificates that can be verified using the OS bundled Root CA Certificates — see: [\[authenticating-the-listener\]](#authenticating-the-listener).                                                                                                                                                           |
| **3** | Configure the credentials the client will present to the server. Here we say to provide _Basic Authentication_ credentials. Other options are available — see: [\[client-authentication\]](#client-authentication).                                                                                                                                                                                                                                                                               |
| **4** | Configure how the replication should perform [Conflict Resolution](#conflict-resolution).                                                                                                                                                                                                                                                                                                                                                                                                         |
| **5** | Initialize the replicator using your configuration object.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **6** | Register an observer, which will notify you of changes to the replication status.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **7** | Start the replicator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## [](#api-references)API References

You can find [Objective-C API References](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc) here.

## [](#device-discovery)Device Discovery

**This phase is optional:** If the listener is initialized on a well known URL endpoint (for example, a static IP Address or well known DNS address) then you can configure active peers to connect to those.

Prior to connecting with a listener you may execute a peer discovery phase to dynamically discover peers.

For the active peer this involves browsing-for and selecting the appropriate service using a zero-config protocol such as _Bonjour_\-- see: <https://developer.apple.com/bonjour/>.

## [](#configure-replicator)Configure Replicator

In this section

[Configure Target](#lbl-cfg-tgt) | [Sync Mode](#lbl-cfg-sync) | [Heartbeat](#lbl-cfg-htbt) | [Authenticating the Listener](#lbl-auth-lstnr) | [Client Authentication](#lbl-authclnt)

### [](#lbl-cfg-tgt)Configure Target

Use the [ReplicatorConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorConfiguration.html) class and [\-initWithDatabase:target:](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorConfiguration.html#/c:objc%28cs%29CBLReplicatorConfiguration%28im%29initWithDatabase:target:) constructor to initialize the replication configuration with local and remote database locations.

The constructor provides:

* the name of the local database to be sync'd
* the server's URL (including the port number and the name of the remote database to sync with)  
It is expected that the app will identify the IP address and URL and append the remote database name to the URL endpoint, producing for example: `wss://10.0.2.2:4984/travel-sample`  
The URL scheme for web socket URLs uses `ws:` (non-TLS) or `wss:` (SSL/TLS) prefixes.

Example 2\. Add Target to Configuration

```objc
// Set listener DB endpoint
NSURL *url = [NSURL URLWithString:@"ws://10.0.2.2.com:55990/travel-sample"];
CBLURLEndpoint *thisListener = [[CBLURLEndpoint alloc] initWithURL:url];

CBLReplicatorConfiguration *thisConfig
  = [[CBLReplicatorConfiguration alloc]
      initWithDatabase:thisDB target:thisListener]; (1)
```

**Notes on Example**

| **1** | Note use of the wss:// prefix to ensure TLS encryption (strongly recommended in production) |
| ----- | ------------------------------------------------------------------------------------------- |

### [](#lbl-cfg-sync)Sync Mode

Here we define the direction and type of replication we want to initiate.

We use `[ReplicatorConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorConfiguration.html)` class's [replicatorType](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorConfiguration.html#/c:objc%28cs%29CBLReplicatorConfiguration%28py%29replicatorType) and `[continuous](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorConfiguration.html#/c:objc%28cs%29CBLReplicatorConfiguration%28py%29continuous)` parameters, to tell the replicator:

* The direction of the replication: `**pushAndPull**`; `pull`; `push`
* The type of replication, that is:

  * Continuous — remaining active indefinitely to replicate changed documents (`continuous=true`).
  * Ad-hoc — a one-shot replication of changed documents (`continuous=false`).

Example 3\. Configure replicator type and mode

```objc
thisConfig.replicatorType = kCBLReplicatorTypePush;

thisConfig.continuous = YES;
```

### [](#lbl-cfg-htbt)Heartbeat

A point to consider when initiating a replication, particularly a continuous replication, is keeping the connection alive. Couchbase Lite minimizes the chance of dropped connections by having the replicator maintain a heartbeat; essentially pinging the listener at a configurable interval.

When necessary you can adjust this interval using [heartbeat](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorConfiguration.html#/c:objc%28cs%29CBLReplicatorConfiguration%28py%29heartbeat) as shown in — [Example 4](#ex-htbt).

The default heartbeat value is 300 (5 minutes).

Example 4\. Setting heartbeat interval

```objc
id target =
  [[CBLURLEndpoint alloc] initWithURL: [NSURL URLWithString: @"ws://foo.cbl.com/db"]];

CBLReplicatorConfiguration* config =
    [[CBLReplicatorConfiguration alloc] initWithDatabase: db target: target];
config.type = kCBLReplicatorTypePush;
config.continuous: YES;
//  other config as required . . .
config.heartbeat = 60; (1)
//  other config as required . . .
repl = [[CBLReplicator alloc] initWithConfig: config];

// Cleanup:
repl = nil;
```

| **1** | The heartbeat value sets the interval (in seconds) between the heartbeat pulses. |
| ----- | -------------------------------------------------------------------------------- |

### [](#lbl-auth-lstnr)Authenticating the Listener

Define the credentials the your app (the client) is expecting to receive from the server (listener) in order to ensure that the server is one it is prepared to interact with.

Note that the client cannot authenticate the server if TLS is turned off. When TLS is enabled (Sync Gateway's default) the client _must_ authenticate the server. If the server cannot provide acceptable credentials then the connection will fail.

Use `[ReplicatorConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorConfiguration.html)` properties [acceptOnlySelfSignedServerCertificate](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorConfiguration.html#/c:objc%28cs%29CBLReplicatorConfiguration%28py%29acceptOnlySelfSignedServerCertificate) and [setPinnedServerCertificate()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorConfiguration.html#/c:objc%28cs%29CBLReplicatorConfiguration%28py%29pinnedServerCertificate), to tell the replicator how to verify server-supplied TLS server certificates.

* If there is a pinned certificate, nothing else matters, the server cert must **exactly** match the pinned certificate.
* If there are no pinned certs and [acceptOnlySelfSignedServerCertificate](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorConfiguration.html#/c:objc%28cs%29CBLReplicatorConfiguration%28py%29acceptOnlySelfSignedServerCertificate) is `true` then any self-signed certificate is accepted. Certificates that are not self signed are rejected, no matter who signed them.
* If there are no pinned certificates and [acceptOnlySelfSignedServerCertificate](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorConfiguration.html#/c:objc%28cs%29CBLReplicatorConfiguration%28py%29acceptOnlySelfSignedServerCertificate) is `false` (default), the client validates the server's certificates against the system CA certificates. The server must supply a chain of certificates whose root is signed by one of the certificates in the system CA bundle.

Example 5\. Set Server TLS security

* CA Cert
* Self Signed Cert
* Pinned Certificate

Set the client to expect and accept only CA attested certificates.

```objc
// Configure Server Security -- only accept CA Certs
thisConfig.acceptOnlySelfSignedServerCertificate = NO; (1)
```

**Notes on Example**

| **1** | This is the default. Only certificate chains with roots signed by a trusted CA are allowed. Self signed certificates are not allowed. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------- |

Set the client to expect and accept only self-signed certificates

```objc
// Configure Server Authentication
// Here - expect and accept self-signed certs
thisConfig.acceptOnlySelfSignedServerCertificate = YES; (1)
```

**Notes on Example**

| **1** | Set this to true to accept any self signed cert. Any certificates that are not self-signed are rejected. |
| ----- | -------------------------------------------------------------------------------------------------------- |

Set the client to expect and accept only a pinned certificate.

```objc
NSURL *certURL =
  [[NSBundle mainBundle] URLForResource: @"cert" withExtension: @"cer"];
NSData *data =
  [[NSData alloc] initWithContentsOfURL: certURL];
SecCertificateRef certificate =
  SecCertificateCreateWithData(NULL, (__bridge CFDataRef)data);

NSURL *url =
  [NSURL URLWithString:@"ws://localhost:4984/db"];

CBLURLEndpoint *target = [[CBLURLEndpoint alloc] initWithURL: url];

CBLReplicatorConfiguration *thisConfig =
  [[CBLReplicatorConfiguration alloc] initWithDatabase:database
                                      target:target];
thisConfig.pinnedServerCertificate =
  (SecCertificateRef)CFAutorelease(certificate);

thisConfig.acceptOnlySelfSignedServerCertificate=false;
```

### [](#lbl-authclnt)Client Authentication

Here we define the credentials that the client can present to the server if prompted to do so in order that the server can authenticate it.

We use [ReplicatorConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorConfiguration.html)'s [authenticator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorConfiguration.html#/c:objc%28cs%29CBLReplicatorConfiguration%28py%29authenticator) method to define the authentication method to the replicator - see [Example 7](#configuring-client-authentication).

#### [](#basic-authentication)Basic Authentication

Use the `[BasicAuthenticator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLBasicAuthenticator.html)` to supply basic authentication credentials (username and password).

Example 6\. Basic Authentication

This example shows basic authentication using user name and password:

```objc
// Here set client to use basic authentication
// Providing username and password credentials
// If prompted for them by server
thisConfig.authenticator = [[CBLBasicAuthenticator alloc] initWithUsername:@"Our Username" password:@"Our Password"]; (1)
```

#### [](#certificate-authentication)Certificate Authentication

Use the `[ClientCertificateAuthenticator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLClientCertificateAuthenticator.html)` to configure the client TLS certificates to be presented to the server, on connection. This applies only to the [URLEndpointListener](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLURLEndpointListener.html).

> [!NOTE]
> The **server** (listener) must have `disableTLS` set `false` and have a [ClientCertificateAuthenticator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLClientCertificateAuthenticator.html) configured, or it will never ask for this client's certificate.

The certificate to be presented to the server will need to be signed by the root certificates or be valid based on the authentication callback set to the listener via ListenerCertificateAuthenticator.

Example 7\. Client Cert Authentication

This example shows client certificate authentication using an identity from secure storage.

```objc
// Check if Id exists in keychain and if so, use it
CBLTLSIdentity* identity =
  [CBLTLSIdentity identityWithLabel: @"doco-sync-server" error: &error]; (1)

thisConfig.authenticator =
  [[CBLClientCertificateAuthenticator alloc] initWithIdentity: identity]; (2)
```

**Notes on Example**

| **1** | Get an identity from secure storage and create a TLS Identity object                                                                                                                                                |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Set the authenticator to [ClientCertificateAuthenticator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLClientCertificateAuthenticator.html) and configure it to use the retrieved identity |

## [](#initialize-replicator)Initialize Replicator

Use the `[Replicator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html)` class's [initWith(config:)](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html#/c:objc%28cs%29CBLReplicator%28im%29initWithConfig:) constructor, to initialize the replicator with the configuration you have defined. You can, optionally, add a change listener (see [Monitor Sync](#lbl-repl-mon)) before starting the replicator running using [start()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html#/c:objc%28cs%29CBLReplicator%28im%29start).

Example 8\. Initialize and run replicator

```objc
// Apply configuration settings to the replicator
_thisReplicator = [[CBLReplicator alloc] initWithConfig:thisConfig]; (1)

// Run the replicator using the config settings
[thisReplicator start]; (2)
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

You can monitor a replication's status by using a combination of [Change Listeners](#lbl-repl-chng) and the `replication.status.activity` property — see; [activity enum](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorStatus.html#/c:objc%28cs%29CBLReplicatorStatus%28py%29activity). This enables you to know, for example, when the replication is actively transferring data and when it has stopped.

You can also choose to monitor document changes — see: [\[lbl-repl-evnts\]](#lbl-repl-evnts).

### [](#lbl-repl-chng)Change Listeners

Use this to monitor changes and to inform on sync progress; this is an optional step.

> [!TIP]
> Best Practice
> 
> You should register the listener before starting your replication, to avoid having to do a restart to activate it …​ and don't forget to save the token so you can remove the listener later

Use the [Replicator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html) class to add a change listener as a callback to the Replicator ([addChangeListener(\_:)](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html#/c:objc%28cs%29CBLReplicator%28im%29addChangeListener:)) — see: [Example 9](#ex-repl-mon). You will then be asynchronously notified of state changes.

Remove your change listener before stopping the replicator — use the [removeChangeListenerWithToken(CBLListenerToken:)](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html#/c:objc%28cs%29CBLReplicator%28im%29removeChangeListenerWithToken) method to do this.

### [](#lbl-repl-status)Replicator Status

You can use the [Replicator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html) class's [status](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html#/c:objc%28cs%29CBLReplicator%28py%29status) property to check the replicator status. That is, whether it is actively transferring data or if it has stopped — see: [Example 9](#ex-repl-mon).

The returned _ReplicationStatus_ structure comprises:

* [activity enum](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorStatus.html#/c:objc%28cs%29CBLReplicatorStatus%28py%29activity) — stopped, offline, connecting, idle or busy — see states described in: [Table 1](#tbl-states)
* [progress enum](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorStatus.html#/c:objc%28cs%29CBLReplicatorStatus%28py%29progress%29)

  * completed — the total number of changes completed
  * total — the total number of changes to be processed
* [error enum](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorStatus.html#/c:objc%28cs%29CBLReplicatorStatus%28py%29error) — the current error, if any

Example 9\. Monitor replication

* Adding a Change Listener
* Using replicator.status

```objc
// Retain token for use in deletion
id<CBLListenerToken> thisListenerToken
  = [thisReplicator addChangeListener:^(CBLReplicatorChange *thisChange) {
      if (thisChange.status.activity == kCBLReplicatorStopped) {
        NSLog(@"Replication stopped");
        } else {
        NSLog(@"Status: %d", thisChange.status.activity);
        };
    }];
```

```objc
if (thisChange.status.activity == kCBLReplicatorStopped) {
  NSLog(@"Replication stopped");
  } else {
  NSLog(@"Status: %d", thisChange.status.activity);
  };
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

The following diagram describes the status changes when the application starts a replication, and when the application is being backgrounded or foregrounded by the OS. It applies to iOS only.

![replicator states](_images/replicator-states.png) 

Additionally, on iOS, an app already in the background may be terminated. In this case, the `Database` and `Replicator` instances will be `null` when the app returns to the foreground. Therefore, as preventive measure, it is recommended to do a `null` check when the app enters the foreground, and to re-initialize the database and replicator if any of those is `null`.

On other platforms, Couchbase Lite doesn't react to OS backgrounding or foregrounding events and replication(s) will continue running as long as the remote system does not terminate the connection and the app does not terminate. It is generally recommended to stop replications before going into the background otherwise socket connections may be closed by the OS and this may interfere with the replication process.

### [](#lbl-repl-pend)Documents Pending Push

> [!TIP]
> [CBLReplicator.isDocumentPending()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html#/c:objc%28cs%29CBLReplicator%28im%29isDocumentPending:error:) is quicker and more efficient. Use it in preference to returning a list of pending document IDs, where possible.

You can check whether documents are waiting to be pushed in any forthcoming sync by using either of the following API methods:

* Use the [CBLReplicator.pendingDocumentIDs()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html#/c:objc%28cs%29CBLReplicator%28im%29pendingDocumentIDs:) method, which returns a list of document IDs that have local changes, but which have not yet been pushed to the server.  
This can be very useful in tracking the progress of a push sync, enabling the app to provide a visual indicator to the end user on its status, or decide when it is safe to exit.
* Use the [CBLReplicator.isDocumentPending()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html#/c:objc%28cs%29CBLReplicator%28im%29isDocumentPending:error:) method to quickly check whether an individual document is pending a push.

Example 10\. Use Pending Document ID API

```objc
CBLDatabase *database = self.db;
NSURL *url = [NSURL URLWithString:@"ws://localhost:4984/db"];
CBLURLEndpoint *target =
  [[CBLURLEndpoint alloc] initWithURL: url];
CBLReplicatorConfiguration *config =
  [[CBLReplicatorConfiguration alloc]
    initWithDatabase:database
    target:target];

config.replicatorType = kCBLReplicatorTypePush;

CBLReplicator *replicator =
  [[CBLReplicator alloc] initWithConfig:config];

// Get list of pending doc IDs
NSError* err = nil;
NSSet *mydocids =
  [NSSet setWithSet:[replicator pendingDocumentIDs:&err]]; (1)


if ([mydocids count] > 0) {

  NSLog(@"There are %lu documents pending", (unsigned long)[mydocids count]);

  [replicator addChangeListener:^(CBLReplicatorChange *change) {

    NSLog(@"Replicator activity level is %u", change.status.activity);
    // iterate and report-on the pending doc IDs  in 'mydocids'
    for (thisid in mydocids) {

      NSError* err = nil;
      if (![replicator isDocumentPending: thisid error: &err]) { (2)
        NSLog(@"Doc ID %@ now pushed", thisid);
      }
    }

  }];
  [replicator start];

};
```

| **1** | [CBLReplicator.pendingDocumentIDs()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html#/c:objc%28cs%29CBLReplicator%28im%29pendingDocumentIDs:) returns a list of the document IDs for all documents waiting to be pushed. This is a snapshot and may have changed by the time the response is received and processed. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [CBLReplicator.isDocumentPending()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html#/c:objc%28cs%29CBLReplicator%28im%29isDocumentPending:error:) returns true if the document is waiting to be pushed, and false otherwise.                                                                                         |

## [](#lbl-repl-stop)Stop Sync

Stopping a replication is straightforward. It is done using [stop()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html#/c:objc%28cs%29CBLReplicator%28im%29stop). This initiates an asynchronous operation and so is not necessarily immediate. Your app should account for this potential delay before attempting any subsequent operations, for example closing the database.

You can find further information on database operations in [Databases](../../current/objc/database.md).

> [!TIP]
> Best Practice
> 
> 1. When you start a change listener, save the returned token, you will need it when you remove the listener
> 2. You can ensure the replication has completely stopped by checking for a replication status = STOPPED

Example 11\. Stop replicator

```objc
// Remove the change listener
[thisReplicator removeChangeListenerWithToken: thisListenerToken];

// Stop the replicator
[thisReplicator stop];
```

| **1** | Here we initiate the stopping of the replication using the [stop()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html#/c:objc%28cs%29CBLReplicator%28im%29stop) method. We can then remove any active [change listener](#lbl-repl-chng). |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#conflict-resolution)Conflict Resolution

Unless you specify otherwise, Couchbase Lite's default conflict resolution policy is applied — see [Automatic Conflict Resolution](#couchbase-lite:objc:{cbl-pg-conflict-auto}).

To use a different policy, specify a _conflict resolver_ using [conflictResolver](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorConfiguration.html#/c:objc%28cs%29CBLReplicatorConfiguration%28py%29conflictResolver) as shown in [Example 12](#using-conflict-resolvers).

For more complex solutions you can provide a custom conflict resolver - see: [Custom Conflict Resolution](#couchbase-lite:objc:{cbl-pg-conflict-custom}).

Example 12\. Using conflict resolvers

* Local Wins
* Remote Wins
* Merge

```objc
@interface LocalWinConflictResolver: NSObject<CBLConflictResolver>
@end

@implementation LocalWinConflictResolver
- (CBLDocument*) resolve: (CBLConflict*)conflict {
    return conflict.localDocument;
}

@end
```

```objc
@interface RemoteWinConflictResolver: NSObject<CBLConflictResolver>
@end

@implementation RemoteWinConflictResolver
- (CBLDocument*) resolve: (CBLConflict*)conflict {
    return conflict.remoteDocument;
}

@end
```

```objc
@interface MergeConflictResolver: NSObject<CBLConflictResolver>
@end

@implementation MergeConflictResolver
- (CBLDocument*) resolve: (CBLConflict*)conflict {
    NSDictionary *localDict = conflict.localDocument.toDictionary;
    NSDictionary *remoteDict = conflict.remoteDocument.toDictionary;

    NSMutableDictionary *result = [NSMutableDictionary dictionaryWithDictionary:localDict];
    [result addEntriesFromDictionary:remoteDict];

    return [[CBLMutableDocument alloc] initWithID:conflict.documentID
                                             data:result];
}

@end
```

Just as a replicator may observe a conflict — when updating a document that has changed both in the local database and in a remote database — any attempt to save a document may also observe a conflict, if a replication has taken place since the local app retrieved the document from the database. To address that possibility, a version of the `Database.save()` method also takes a conflict resolver as shown in [\[merging-document-properties\]](#merging-document-properties).

The following code snippet shows an example of merging properties from the existing document (`current`) into the one being saved (`new`). In the event of conflicting keys, it will pick the key value from `new`.

Example 13\. Merging document properties

```objc
CBLDocument *document = [database documentWithID:@"xyz"];
CBLMutableDocument *mutableDocument = [document toMutable];
[mutableDocument setString:@"apples" forKey:@"name"];

[database saveDocument:mutableDocument
       conflictHandler:^BOOL(CBLMutableDocument *new, CBLDocument *current) {
           NSDictionary *currentDict = current.toDictionary;
           NSDictionary *newDict = new.toDictionary;

           NSMutableDictionary *result = [NSMutableDictionary dictionaryWithDictionary:currentDict];
           [result addEntriesFromDictionary:newDict];
           [new setData: result];
           return YES;
       }
                 error: &error];
```

## [](#related-content)Related Content

###### [](#)

How to

* [Passive Peer](../../current/objc/p2psync-websocket-using-passive.md)
* [Active Peer](../../current/objc/p2psync-websocket-using-active.md)

###### [](#-2)

Concepts

* [Landing P2Psync](#couchbase-lite:objc:landing-p2psync.adoc)
* [API References](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc).

###### [](#-3)

Community Resources …​

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

* [Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)

For more on replicator conflict resolution see: [Handling Data Conflicts](../../current/objc/conflict.md).

## [](#delta-sync)Delta Sync

If delta sync is enabled on the listener, then replication will use delta sync.

## [](#related-content-2)Related Content

###### [](#-4)

How to

* [Passive Peer](../../current/objc/p2psync-websocket-using-passive.md)
* [Active Peer](../../current/objc/p2psync-websocket-using-active.md)

###### [](#-5)

Concepts

* [Landing P2Psync](#couchbase-lite:objc:landing-p2psync.adoc)
* [API References](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc).

###### [](#-6)

Community Resources …​

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

* [Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)