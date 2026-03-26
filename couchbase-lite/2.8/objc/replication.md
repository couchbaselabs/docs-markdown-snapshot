---
title: Data Sync using Sync Gateway
description: Couchbase Lite for Objective-C -- Synchronizing data changes
  between local and remote databases using Sync Gateway
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/objc/pages/replication.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@couchbase-lite:objc:replication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/objc/replication.html)

# Data Sync using Sync Gateway

> Description — _Couchbase Lite for Objective-C — Synchronizing data changes between local and remote databases using Sync Gateway_  
> Related Content — [Handling Data Conflicts](../../current/objc/conflict.md) | [Intra-device Data Sync](../../current/objc/dbreplica.md) | [Peer-to-Peer](p2psync-websocket.md)

> [!NOTE]
> Code Snippets
> 
> The code examples are indicative only. They demonstrate basic concepts and approaches to using a feature. Use them as inspiration and adapt these examples to best practice when developing applications for your platform.

## [](#introduction)Introduction

Couchbase Lite for Objective-C provides API support for secure, bi-directional, synchronization of data changes between mobile applications and a central server database. It does so by using a replicator to interact with Sync Gateway. Simply put, the replicator is designed to send documents from a source to a target database. In this case, between a local Couchbase Lite database and remote Sync Gateway database (server or cloud).

This content provides sample code and configuration examples covering the implementation of a replication using Sync Gateway.

Your application runs a replicator (also referred to here as a client), which will initiate connection with a Sync Gateway (also referred to here as a server) and participate in the replication of database changes to bring both local and remote databases into sync.

Subsequent sections provide additional details and examples for the main configuration options.

## [](#replication-protocol)Replication Protocol

### [](#scheme)Scheme

Couchbase Mobile uses a replication protocol based on WebSockets fof replication. To use this protocol the replication URL should specify WebSockets as the URL scheme (see the [Configure Target](#lbl-cfg-tgt) section below).

Incompatibilities

Couchbase Lite's replication protocol is **incompatible** with CouchDB-based databases. And since Couchbase Lite 2.x+ only supports the new protocol, you will need to run a version of Sync Gateway that supports it — see: [Compatibility](../../current/objc/compatibility.md).

Legacy Compatibility

Clients using Couchbase Lite 1.x can continue to use `http` as the URL scheme. Sync Gateway 2.x+ will automatically use:

* The 1.x replication protocol when a Couchbase Lite 1.x client connects through `http://localhost:4984/db`
* The 2.0 replication protocol when a Couchbase Lite 2.0 client connects through `ws://localhost:4984/db`.

You can find further information in our blog: [Introducing the Data Replication Protocol](https://blog.couchbase.com/data-replication-couchbase-mobile/).

### [](#lbl-repl-ord)Ordering

To optimize for speed, the replication protocol doesn't guarantee that documents will be received in a particular order. So we don't recommend to rely on that when using the replication or database change listeners for example.

## [](#configuration-summary)Configuration Summary

You should configure and initialize a replicator for each Couchbase Lite database instance you want to sync. [Example 1](#ex-simple-repl) shows the configuration and initialization process.

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

| **1** | Use the [ReplicatorConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorConfiguration.html) class's constructor — [\-initWithDatabase:target:](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorConfiguration.html#/c:objc%28cs%29CBLReplicatorConfiguration%28im%29initWithDatabase:target:) — to initialize the replicator configuration with the local database — see also: [Configure Target](#lbl-cfg-tgt) |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Configure how the client will authenticate the server. Here we say connect only to servers presenting a self-signed certificate. By default, clients accept only servers presenting certificates that can be verified using the OS bundled Root CA Certificates — see: [Server Authentication](#lbl-svr-auth).                                                                                                                                                                           |
| **3** | Configure the credentials the client will present to the server. Here we say to provide _Basic Authentication_ credentials. Other options are available — see: [Client Authentication](#lbl-client-auth).                                                                                                                                                                                                                                                                                |
| **4** | Configure how the replication should handle conflict resolution — see: [Handling Data Conflicts](../../current/objc/conflict.md) topic for mor on conflict resolution.                                                                                                                                                                                                                                                                                                                   |
| **5** | Initialize the replicator using your configuration object — see: [Initialize](#lbl-init-repl).                                                                                                                                                                                                                                                                                                                                                                                           |
| **6** | Optionally, register an observer, which will notify you of changes to the replication status — see: [Monitor](#lbl-repl-mon)                                                                                                                                                                                                                                                                                                                                                             |
| **7** | Start the replicator — see: [Start Replicator](#lbl-repl-start).                                                                                                                                                                                                                                                                                                                                                                                                                         |

## [](#lbl-cfg-repl)Configure

In this section

[Configure Target](#lbl-cfg-tgt) | [Sync Mode](#lbl-cfg-sync) | [Heartbeat](#lbl-cfg-keep-alive) | [Server Authentication](#lbl-svr-auth) | [Client Authentication](#lbl-client-auth) | [Monitor Document Changes](#lbl-repl-evnts) | [Custom Headers](#lbl-repl-hdrs) | [Checkpoint Starts](#lbl-repl-ckpt) | [Replication Filters](#lbl-repl-fltrs) | [Channels](#lbl-repl-chan) | [Delta Sync](#lbl-repl-delta)

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

### [](#lbl-cfg-keep-alive)Heartbeat

A point to consider when initiating a replication, particularly a continuous replication, is keeping the connection alive. Couchbase Lite minimizes the chance of dropped connections by having the replicator maintain a heartbeat; essentially pinging the Sync Gateway at a configurable interval.

When necessary you can adjust this interval using [heartbeat](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorConfiguration.html#/c:objc%28cs%29CBLReplicatorConfiguration%28py%29heartbeat) as shown in — [Example 4](#ex-htbt). You may need to do this when, for example, when the Sync Gateway is behind a load balancer, which may have its own keep-alive parameters — see Sync Gateway's topic [Load Balancer - Keep Alive](../../../sync-gateway/current/deploy/load-balancer.md#lbl-keepalive).

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

### [](#lbl-svr-auth)Server Authentication

Define the credentials your app (the client) is expecting to receive from the Sync Gateway (the server) in order to ensure it is prepared to continue with the sync.

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

```objc
NSURL *url = [NSURL URLWithString:@"ws://localhost:4984/db"];
CBLURLEndpoint *target = [[CBLURLEndpoint alloc] initWithURL:url];
CBLReplicatorConfiguration *config = [[CBLReplicatorConfiguration alloc] initWithDatabase:database target:target];
config.authenticator = [[CBLBasicAuthenticator alloc] initWithUsername:@"john" password:@"pass"];

CBLReplicator *replicator = [[CBLReplicator alloc] initWithConfig:config];
[replicator start];
```

#### [](#session-authentication)Session Authentication

Session authentication is another way to authenticate with Sync Gateway. A user session must first be created through the [POST /{db}/\_session](../../../sync-gateway/current/rest-api/rest-api.md#/session/post%5F%5Fdb%5F%5F%5Fsession) endpoint on the Public REST API. The HTTP response contains a session ID which can then be used to authenticate as the user it was created for. The following example initiates a one-shot replication with the session ID that is returned from the `POST /{db}/_session` endpoint.

```objc
NSURL *url = [NSURL URLWithString:@"ws://localhost:4984/db"];
CBLURLEndpoint *target = [[CBLURLEndpoint alloc] initWithURL:url];
CBLReplicatorConfiguration *config = [[CBLReplicatorConfiguration alloc] initWithDatabase:database target:target];
config.authenticator = [[CBLSessionAuthenticator alloc] initWithSessionID:@"904ac010862f37c8dd99015a33ab5a3565fd8447"];

CBLReplicator *replicator = [[CBLReplicator alloc] initWithConfig:config];
[replicator start];
```

### [](#lbl-repl-hdrs)Custom Headers

Custom headers can be set on the configuration object. And the replicator will send those header(s) in every request. As an example, this feature can be useful to pass additional credentials when there is an authentication or authorization step being done by a proxy server (between Couchbase Lite and Sync Gateway).

Example 6\. Setting custom headers

```objc
CBLReplicatorConfiguration *config = [[CBLReplicatorConfiguration alloc] initWithDatabase:database target:endpoint];
config.headers = @{@"CustomHeaderName" : @"Value"};
```

### [](#lbl-repl-fltrs)Replication Filters

Replication Filters allow you to have quick control over which documents are stored as the result of a push and/or pull replication.

#### [](#push-filter)Push Filter

A push filter allows an app to push a subset of a database to the server, which can be very useful in some circumstances. For instance, high-priority documents could be pushed first, or documents in a "draft" state could be skipped.

The following example filters out documents whose `type` property is equal to `draft`.

```objc
NSURL *url = [NSURL URLWithString:@"ws://localhost:4984/db"];
CBLURLEndpoint *target = [[CBLURLEndpoint alloc] initWithURL: url];

CBLReplicatorConfiguration *config = [[CBLReplicatorConfiguration alloc] initWithDatabase:database target:target];
config.pushFilter = ^BOOL(CBLDocument * _Nonnull document, CBLDocumentFlags flags) { (1)
    if ([[document stringForKey: @"type"] isEqualToString: @"draft"]) {
        return false;
    }
    return true;
};

CBLReplicator *replicator = [[CBLReplicator alloc] initWithConfig:config];
[replicator start];
```

| **1** | The callback should follow the semantics of a [pure function](https://en.wikipedia.org/wiki/Pure%5Ffunction). Otherwise, long running functions would slow down the replicator considerably. Furthermore, your callback should not make assumptions about what thread it is being called on. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#### [](#pull-filter)Pull Filter

A pull filter gives an app the ability to validate documents being pulled, and skip ones that fail. This is an important security mechanism in a peer-to-peer topology with peers that are not fully trusted.

> [!NOTE]
> Pull replication filters are not a substitute for channels. Sync Gateway [channels](../../../sync-gateway/current/access-control/channels.md) are designed to be scalable (documents are filtered on the server) whereas a pull replication filter is applied to a document once it has been downloaded.

```objc
NSURL *url = [NSURL URLWithString:@"ws://localhost:4984/db"];
CBLURLEndpoint *target = [[CBLURLEndpoint alloc] initWithURL: url];

CBLReplicatorConfiguration *config = [[CBLReplicatorConfiguration alloc] initWithDatabase:database target:target];
config.pullFilter = ^BOOL(CBLDocument * _Nonnull document, CBLDocumentFlags flags) { (1)
    if ((flags & kCBLDocumentFlagsDeleted) == kCBLDocumentFlagsDeleted) {
        return false;
    }
    return true;
};

CBLReplicator *replicator = [[CBLReplicator alloc] initWithConfig:config];
[replicator start];
```

| **1** | The callback should follow the semantics of a [pure function](https://en.wikipedia.org/wiki/Pure%5Ffunction). Otherwise, long running functions would slow down the replicator considerably. Furthermore, your callback should not make assumptions about what thread it is being called on. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

> [!NOTE]
> Losing access to a document (via the Sync Function) also triggers the pull replication filter. Filtering out such an event would retain the document locally. As a result, there would be a local copy of the document disjointed from the one that resides on Couchbase Server. Further updates to the document stored on Couchbase Server would not be received in pull replications and further local edits could be potentially pushed, which would result in 409 errors since access has been revoked.

### [](#lbl-repl-chan)Channels

By default, Couchbase Lite gets all the channels to which the configured user account has access. This behavior is suitable for most apps that rely on [user authentication](../../../sync-gateway/current/security/authentication-users.md) and the [sync function](../../../sync-gateway/current/access-control/sync-function/sync-function-api.md) to specify which data to pull for each user.

Optionally, it's also possible to specify a comma-separated list of channel names on Couchbase Lite's replicator configuration object. In this case, the replication from Sync Gateway will only pull documents tagged with those channels.

### [](#lbl-repl-delta)Delta Sync

> [!IMPORTANT]
> This is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature.

With Delta Sync \[[1](#%5Ffootnotedef%5F1 "View footnote.")\], only the changed parts of a Couchbase document are replicated. This can result in significant savings in bandwidth consumption as well as throughput improvements, especially when network bandwidth is typically constrained.

Replications to a Server (for example, a Sync Gateway, or passive listener) automatically use delta sync if the property is enabled at database level by the server — see: [databases.$db.delta\_sync.enabled](../../../sync-gateway/current/configuration/configuration-properties-legacy.md#databases-foo%5Fdb-delta%5Fsync).

[Intra-device Data Sync](../../current/objc/dbreplica.md) replications automatically **disable** delta sync, whilst [Peer-to-Peer](p2psync-websocket.md) replications automatically **enable** delta sync.

## [](#lbl-init-repl)Initialize

In this section

[Start Replicator](#lbl-repl-start) | [Checkpoint Starts](#lbl-repl-ckpt)

### [](#lbl-repl-start)Start Replicator

Use the `[Replicator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html)` class's [initWith(config:)](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html#/c:objc%28cs%29CBLReplicator%28im%29initWithConfig:) constructor, to initialize the replicator with the configuration you have defined. You can, optionally, add a change listener (see [Monitor](#lbl-repl-mon)) before starting the replicator running using [start()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html#/c:objc%28cs%29CBLReplicator%28im%29start).

Example 7\. Initialize and run replicator

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

### [](#lbl-repl-ckpt)Checkpoint Starts

Replicators use [checkpoints](../../current/objc/refer-glossary.md#checkpoint) to keep track of documents sent to the target database. Without [checkpoints](../../current/objc/refer-glossary.md#checkpoint) , Couchbase Lite would replicate the entire database content to the target database on each connection, even though previous replications may already have replicated some or all of that content.

This functionality is generally not a concern to application developers. However, if you do want to force the replication to start again from zero, use the [checkpoint](../../current/objc/refer-glossary.md#checkpoint) reset method `replicator.resetCheckpoint()` **before** starting the replicator.

Example 8\. Resetting checkpoints

```objc
[replicator resetCheckpoint];
[replicator start];
```

## [](#lbl-repl-mon)Monitor

In this section

[Change Listeners](#lbl-repl-chng) | [Replicator Status](#lbl-repl-status) | [Monitor Document Changes](#lbl-repl-evnts) | [Documents Pending Push](#lbl-repl-pend)

You can monitor a replication's status by using a combination of [Change Listeners](#lbl-repl-chng) and the `replication.status.activity` property — see; [activity enum](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicatorStatus.html#/c:objc%28cs%29CBLReplicatorStatus%28py%29activity). This enables you to know, for example, when the replication is actively transferring data and when it has stopped.

You can also choose to monitor document changes — see: [Monitor Document Changes](#lbl-repl-evnts).

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

### [](#lbl-repl-evnts)Monitor Document Changes

You can choose to register for document updates during a replication.

> [!TIP]
> You should register the listener before starting your replication, to avoid having to do a restart to activate it.

For example, the code snippet in [Example 10](#ex-reg-doc-listener) registers a listener to monitor document replication performed by the replicator referenced by the variable `replicator`. It prints the document ID of each document received and sent. Stop the listener as shown in [Example 11](#ex-stop-doc-listener).

Example 10\. Register a document listener

```objc
id token = [replicator addDocumentReplicationListener:^(CBLDocumentReplication * _Nonnull replication) {
    NSLog(@"Replication type :: %@", replication.isPush ? @"Push" : @"Pull");
    for (CBLReplicatedDocument* document in replication.documents) {
        if (document.error == nil) {
            NSLog(@"Doc ID :: %@", document.id);
            if ((document.flags & kCBLDocumentFlagsDeleted) == kCBLDocumentFlagsDeleted) {
                NSLog(@"Successfully replicated a deleted document");
            }
        } else {
            // There was an error
        }
    }
}];

[replicator start];
```

Example 11\. Stop document listener

This code snippet shows how to stop the document listener using the token from the previous example.

```objc
[replicator removeChangeListenerWithToken: token];
```

#### [](#document-access-removal-behavior)Document Access Removal Behavior

When access to a document is removed on Sync Gateway (see: Sync Gateway's [Sync Function](../../../sync-gateway/current/access-control/sync-function/sync-function-api.md)), the document replication listener sends a notification with the `AccessRemoved` flag set to `true` and subsequently purges the document from the database.

### [](#lbl-repl-pend)Documents Pending Push

> [!TIP]
> [CBLReplicator.isDocumentPending()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html#/c:objc%28cs%29CBLReplicator%28im%29isDocumentPending:error:) is quicker and more efficient. Use it in preference to returning a list of pending document IDs, where possible.

You can check whether documents are waiting to be pushed in any forthcoming sync by using either of the following API methods:

* Use the [CBLReplicator.pendingDocumentIDs()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html#/c:objc%28cs%29CBLReplicator%28im%29pendingDocumentIDs:) method, which returns a list of document IDs that have local changes, but which have not yet been pushed to the server.  
This can be very useful in tracking the progress of a push sync, enabling the app to provide a visual indicator to the end user on its status, or decide when it is safe to exit.
* Use the [CBLReplicator.isDocumentPending()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html#/c:objc%28cs%29CBLReplicator%28im%29isDocumentPending:error:) method to quickly check whether an individual document is pending a push.

Example 12\. Use Pending Document ID API

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

## [](#lbl-repl-stop)Stop

Stopping a replication is straightforward. It is done using [stop()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html#/c:objc%28cs%29CBLReplicator%28im%29stop). This initiates an asynchronous operation and so is not necessarily immediate. Your app should account for this potential delay before attempting any subsequent operations, for example closing the database.

You can find further information on database operations in [Databases](../../current/objc/database.md).

> [!TIP]
> Best Practice
> 
> 1. When you start a change listener, save the returned token, you will need it when you remove the listener
> 2. You can ensure the replication has completely stopped by checking for a replication status = STOPPED

Example 13\. Stop replicator

```objc
// Remove the change listener
[thisReplicator removeChangeListenerWithToken: thisListenerToken];

// Stop the replicator
[thisReplicator stop];
```

| **1** | Here we initiate the stopping of the replication using the [stop()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-objc/Classes/CBLReplicator.html#/c:objc%28cs%29CBLReplicator%28im%29stop) method. We can then remove any active [change listener](#lbl-repl-chng). |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#lbl-nwk-errs)Error Handling

When _replicator_ detects a network error it updates its status depending on the error type (permanent or temporary) and returns an appropriate HTTP error code.

The following code snippet adds a `Change Listener`, which monitors a replication for errors and logs the the returned error code.

Example 14\. Monitoring for network errors

```objc
[replicator addChangeListener:^(CBLReplicatorChange *change) {
    if (change.status.error) {
        NSLog(@"Error code: %ld", change.status.error.code);
    }
}];
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

Couchbase Lite for Objective-C supports certificate pinning.

Certificate pinning is a technique that can be used by applications to "pin" a host to its certificate. The certificate is typically delivered to the client by an out-of-band channel and bundled with the client. In this case, Couchbase Lite uses this embedded certificate to verify the trustworthiness of the server (for example, a Sync Gateway) and no longer needs to rely on a trusted third party for that (commonly referred to as the Certificate Authority).

The following steps describe how to configure certificate pinning between Couchbase Lite and Sync Gateway.

1. [Create your own self-signed certificate](../../../sync-gateway/current/security/authentication-certs.md#creating-your-own-self-signed-certificate) with the `openssl` command. After completing this step, you should have 3 files: `cert.pem`, `cert.cer` and `privkey.pem`.
2. [Configure Sync Gateway](../../../sync-gateway/current/security/authentication-certs.md#installing-the-certificate) with the `cert.pem` and `privkey.pem` files. After completing this step, Sync Gateway is reachable over `https`/`wss`.
3. On the Couchbase Lite side, the replication must point to a URL with the `wss` scheme and configured with the `cert.cer` file created in step 1.  
This example loads the certificate from the application sandbox, then converts it to the appropriate type to configure the replication object.  
```objc  
// tag=p2p-act-rep-config-cacert-pinned[]  
NSURL *certURL = [[NSBundle mainBundle] URLForResource: @"cert" withExtension: @"cer"];  
NSData *data = [[NSData alloc] initWithContentsOfURL: certURL];  
SecCertificateRef certificate = SecCertificateCreateWithData(NULL, (__bridge CFDataRef)data);  
NSURL *url = [NSURL URLWithString:@"ws://localhost:4984/db"];  
CBLURLEndpoint *target = [[CBLURLEndpoint alloc] initWithURL: url];  
CBLReplicatorConfiguration *config = [[CBLReplicatorConfiguration alloc] initWithDatabase:database  
                                                                                   target:target];  
config.pinnedServerCertificate = (SecCertificateRef)CFAutorelease(certificate);  
// end=p2p-act-rep-config-cacert-pinned[]  
```
4. Build and run your app. The replication should now run successfully over https/wss with certificate pinning.

For more on pinning certificates see the blog entry: [Certificate Pinning with Couchbase Mobile](https://blog.couchbase.com/certificate-pinning-android-with-couchbase-mobile/)

## [](#lbl-trouble)Troubleshooting

### [](#logs)Logs

As always, when there is a problem with replication, logging is your friend. You can increase the log output for activity related to replication with Sync Gateway — see [Example 15](#ex-logs).

Example 15\. Set logging verbosity

```objc
// Replicator
[CBLDatabase setLogLevel:kCBLLogLevelVerbose domain:kCBLLogDomainReplicator];
// Network
[CBLDatabase setLogLevel:kCBLLogLevelVerbose domain:kCBLLogDomainNetwork];
```

For more on troubleshooting with logs, see: [Using Logs](#couchbase-lite:objc:troubleshooting-logs.adoc).

### [](#authentication-errors)Authentication Errors

If Sync Gateway is configured with a self signed certificate but your app points to a `ws` scheme instead of `wss` you will encounter an error with status code `11006` — see: [Example 16](#ex-11006)

Example 16\. Protocol Mismatch

```console
CouchbaseLite Replicator ERROR: {Repl#2} Got LiteCore error: WebSocket error 1006 "connection closed abnormally"
```

If Sync Gateway is configured with a self signed certificate, and your app points to a `wss` scheme but the replicator configuration isn't using the certificate you will encounter an error with status code `5011` — see: [Example 17](#ex-5011)

Example 17\. Certificate Mismatch or Not Found

```text
CouchbaseLite Replicator ERROR: {Repl#2} Got LiteCore error: Network error 11 "server TLS certificate is self-signed or has unknown root cert"
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](../../current/objc/gs-prereqs.md)
* [Install](../../current/objc/gs-install.md)
* [Build and Run](../../current/objc/gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](../../current/objc/database.md)
* [Documents](../../current/objc/document.md)
* [Blobs](../../current/objc/blob.md)
* [Remote Sync using Sync Gateway](../../current/objc/replication.md)
* [Handling Data Conflicts](../../current/objc/conflict.md)

###### [](#-3)

Dive Deeper . . .

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

---

[1](#%5Ffootnoteref%5F1). Couchbase Mobile 2.5+ 

[2](#%5Ffootnoteref%5F2). From 2.0