---
title: Passive Peer
description: Couchbase Lite's Peer-to-Peer Synchronization enables edge devices
  to synchronize securely without consuming centralized cloud-server resources
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/swift/pages/p2psync-websocket-using-passive.adoc
  xref: xref:2.8@couchbase-lite:swift:p2psync-websocket-using-passive.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/swift/p2psync-websocket-using-passive.html)

# Passive Peer

> Description — _Couchbase Lite's Peer-to-Peer Synchronization enables edge devices to synchronize securely without consuming centralized cloud-server resources_  
> _Abstract — How to set up a Listener to accept a Replicator connection and sync using peer-to-peer_  
> Related Content — [API Reference](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift) | [Passive Peer](../../current/swift/p2psync-websocket-using-passive.md) | [Active Peer](../../current/swift/p2psync-websocket-using-active.md)

> [!IMPORTANT]
> Enterprise Edition only
> 
> This an [Enterprise Edition](https://www.couchbase.com/products/editions) feature. Purchase the _Enterprise License_, which includes official [Couchbase Support](https://www.couchbase.com/support-policy), to use it in production (see the license and support <https://www.couchbase.com/licensing-and-support-faq>).

> [!CAUTION]
> iOS Restrictions
> 
> iOS 14 Applications
> 
> When your application attempts to access the user's local network, iOS will prompt them to allow (or deny) access. You can customize the message presented to the user by editing the description for the `NSLocalNetworkUsageDescription` key in the `Info.plist`.

> [!NOTE]
> Code Snippets
> 
> The code examples are indicative only. They demonstrate basic concepts and approaches to using a feature. Use them as inspiration and adapt these examples to best practice when developing applications for your platform.

## [](#introduction)Introduction

This content provides code and configuration examples covering the implementation of [Peer-to-Peer Sync](../../current/swift/refer-glossary.md#peer-to-peer-sync) over websockets. Specifically it covers the implementation of a [Passive Peer](../../current/swift/refer-glossary.md#passive-peer).

This _passive peer_ (also referred to as the server, or listener) will accept a connection from an [Active Peer](../../current/swift/refer-glossary.md#active-peer) (also referred to as the client or replicator) and participate in the replication of database changes to synchronize both databases.

Subsequent sections provide additional details, and examples for the main configuration options.

> [!NOTE]
> Secure Storage
> 
> The use of TLS, its associated keys and certificates requires using secure storage to minimize the chances of a security breach. The implementation of this storage differs from platform to platform — see [Using secure storage](../../current/swift/p2psync-websocket.md#using-secure-storage).

## [](#configuration-summary)Configuration Summary

You should configure and initialize a listener for each Couchbase Lite database instance you want to sync. There is no limit on the number of listeners you may configure — [Example 1](#simple-listener-initialization) shows a simple initialization and configuration process.

Example 1\. Listener configuration and initialization

```swift
fileprivate var _thisListener:URLEndpointListener?
fileprivate var thisDB:Database?

  let listenerConfig =
    URLEndpointListenerConfiguration(database: thisDB!) (1)

  /* optionally */ let wsPort: UInt16 = 55991
  /* optionally */ let wssPort: UInt16 = 55990
  listenerConfig.port =  wssPort (2)

  listenerConfig.networkInterface = "10.1.1.10"  (3)

  listenerConfig.enableDeltaSync = true (4)

  listenerConfig.disableTLS  = false (5)

  // Set the credentials the server presents the client
  // Use an anonymous self-signed cert
  listenerConfig.tlsIdentity = nil (6)

  // Configure how the client is to be authenticated
  // Here, use Basic Authentication
  listenerConfig.authenticator =
    ListenerPasswordAuthenticator(authenticator: {
      (validUser, validPassword) -> Bool in
        if (self._allowlistedUsers.contains {
              $0 == validPassword && $1 == validUser
            }) {
            return true
            }
          return false
        }) (7)


  // Initialize the listener
  _thisListener = URLEndpointListener(config: listenerConfig) (8)
  guard let thisListener = _thisListener else {
    throw ListenerError.NotInitialized
    // ... take appropriate actions
  }
  // Start the listener
  try thisListener.start() (9)
```

**Notes on example:**

| **1** | Identify the local database to be used — see: [Initialize the Listener Configuration](#initialize-the-listener-configuration)                                                                                                                                                                                                                                                                            |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Optionally, choose a port to use. By default the system will automatically assign a port — to over-ride this, see: [\[set-network-and-port\]](#set-network-and-port)                                                                                                                                                                                                                                     |
| **3** | Optionally, choose a network-interface to use. By default the system will listen on all network interfaces — to over-ride this see: [\[set-network-and-port\]](#set-network-and-port)                                                                                                                                                                                                                    |
| **4** | Optionally, choose to sync only changes, the default is not to enable delta-sync — see: [Delta Sync](#delta-sync).                                                                                                                                                                                                                                                                                       |
| **5** | Set server security. TLS is always enabled out-of-the-box, so you can usually omit this line. But you _can_, optionally, disable TLS (**not** advisable in production) — see: [TLS Security](#tls-security)                                                                                                                                                                                              |
| **6** | Set the credentials this server will present to the client for authentication. Here we show the default TLS authentication, which is by anonymous self-signed certificate. The server must always authenticate itself to the client.                                                                                                                                                                     |
| **7** | Set client security — define the credentials the server expects the client to present for authentication. Here we show how basic authentication is configured to authenticate the client-supplied credentials from the http authentication header against valid credentials — see [Authenticating the Client](#authenticating-the-client) for more options. Note that client authentication is optional. |
| **8** | Initialize the listener using the configuration settings.                                                                                                                                                                                                                                                                                                                                                |
| **9** | [Start Listener](#start-listener)Unresolved directive in common-p2psync-websocket-using-passive.adoc - include::{example-callouts}\[tags=listener-initialize\]                                                                                                                                                                                                                                           |

## [](#api-references)API References

You can find [Swift API References](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift) here.

## [](#device-discovery)Device Discovery

**This phase is optional:** If the listener is initialized on a well known URL endpoint (for example, a static IP Address or well known DNS address) then you can configure active peers to connect to those.

Prior to initiating the listener you may execute a peer discovery phase.

For the passive peer, this involves advertising the service using, for example _Bonjour_ (see: <https://developer.apple.com/bonjour/>) and waiting for an invite from the active peer.

The connection is established once the passive peer has authenticated and accepted an active peer's invitation.

## [](#initialize-the-listener-configuration)Initialize the Listener Configuration

Initialize the listener configuration with the local database. All other configuration values take their default setting.

Each Listener instance serves one Couchbase Lite database. Couchbase sets no hard limit on the number of listeners you can initialize.

Example 2\. Specify Local Database

In this example `thisDB` has previously been declared as an object of type Database.

```swift
let listenerConfig =
  URLEndpointListenerConfiguration(database: thisDB!) (1)
```

**Notes on example:**

| **1** | Set the local database using the [URLEndpointListenerConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/URLEndpointListenerConfiguration.html)'s constructor [init(database:)](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/URLEndpointListenerConfiguration.html#/s:18CouchbaseLiteSwift32URLEndpointListenerConfigurationC8databaseAcA8DatabaseC%5Ftcfc). The database must be opened before the listener is started. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#set-port-and-network-interface)Set Port and Network Interface

### [](#port-number)Port number

The Listener will automatically select an available port if you do not specify one.

Example 3\. Specify a Port to Use

```swift
/* optionally */ let wsPort: UInt16 = 55991
/* optionally */ let wssPort: UInt16 = 55990
listenerConfig.port =  wssPort (1)
```

**Notes on example:**

| **1** | To use a canonical port — one known to other applications — specify it explicitly using the [port](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/URLEndpointListenerConfiguration.html#/s:18CouchbaseLiteSwift32URLEndpointListenerConfigurationC4ports6UInt16VSgvp) method shown here. Ensure that any port you do specify is not blocked by firewall rules. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#network-interface)Network Interface

The Listener will listen on all network interfaces by default.

Example 4\. Specify a Network Interface to Use

```swift
listenerConfig.networkInterface = "10.1.1.10"  (1)
```

Notes on [Example 4](#specify-a-network-interface-to-use)

| **1** | To specify an interface — one known to other applications — identify it explicitly, using the [networkInterface](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/URLEndpointListenerConfiguration.html#/s:18CouchbaseLiteSwift32URLEndpointListenerConfigurationC16networkInterfaceSSSgvp) method shown here. This must be either an IP Address or network interface name such as en0. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

> [!TIP]
> Where necessary, you can identify the available interfaces at runtime, using appropriate platform tools — see [Example 5](#get-network-interfaces).

Example 5\. Identify available network interfaces

```swift
import SystemConfiguration
// . . .

  #if os(macOS)
  for interface in SCNetworkInterfaceCopyAll() as! [SCNetworkInterface] {
      // do something with this `interface`
  }
  #endif
// . . .
```

## [](#delta-sync)Delta Sync

Delta Sync allows clients to sync only those parts of a document that have changed. This can result in significant savings in bandwidth consumption as well as throughput improvements. Both valuable benefits, especially when network bandwidth is constrained.

Example 6\. Enable delta sync

```swift
listenerConfig.enableDeltaSync = true (1)
```

**Notes on example:**

| **1** | Delta sync replication is not enabled by default. Use [URLEndpointListenerConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/URLEndpointListenerConfiguration.html)'s [enableDeltaSync](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/URLEndpointListenerConfiguration.html#/s:18CouchbaseLiteSwift32URLEndpointListenerConfigurationC15enableDeltaSyncSbvp) method to activate or deactivate it. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#tls-security)TLS Security

### [](#enable-or-disable-tls)Enable or Disable TLS

Define whether the connection is to use TLS or clear text.

TLS based encryption is enabled by default and this setting ought to be used in any production environment. However, it _can_ be disabled, for example for development and-or test environments.

When TLS is enabled, Couchbase Lite provides several options on how the Listener may be configured with an appropriate TLS Identity — see [Configure TLS Identity for Listener](#configure-tls-identity-for-listener).

You can use [URLEndpointListenerConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/URLEndpointListenerConfiguration.html)'s [disableTLS](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/URLEndpointListenerConfiguration.html#/s:18CouchbaseLiteSwift32URLEndpointListenerConfigurationC10disableTLSSbvp) method to disable TLS communication if necessary

The `disableTLS` setting must be 'false' when _Client Cert Authentication_ is required.

Basic Authentication can be used with, or without, TLS.

[disableTLS](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/URLEndpointListenerConfiguration.html#/s:18CouchbaseLiteSwift32URLEndpointListenerConfigurationC10disableTLSSbvp) works in conjunction with `TLSIdentity`, to enable developers to define the key and certificate to be used.

* If `disableTLS` is true — TLS communication is disabled and TLS identity is ignored. Active peers will use the `ws://` URL scheme used to connect to the listener.
* If `disableTLS` is false or not specified — TLS communication is enabled.  
Active peers will use the `wss://` URL scheme to connect to the listener.

### [](#configure-tls-identity-for-listener)Configure TLS Identity for Listener

Define the credentials the server will present to the client for authentication. Note that the server must always authenticate itself with the client — see [Active Peer - authenticating the listener](../../current/swift/p2psync-websocket-using-active.md#authenticating-the-listener) for how the client deals with this.

Use [URLEndpointListenerConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/URLEndpointListenerConfiguration.html)'s [tlsIdentity](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/URLEndpointListenerConfiguration.html#/s:18CouchbaseLiteSwift32URLEndpointListenerConfigurationC11tlsIdentityAA11TLSIdentityCSgvp) method to configure the TLS Identity used in TLS communication.

If `TLSIdentity` is not set, then the listener uses an auto-generated anonymous self-signed identity (unless `disableTLS = true`). Whilst the client cannot use this to authenticate the server, it will use it to encrypt communication, giving a more secure option than non-TLS communication.

The auto-generated anonymous self-signed identity is saved in Keychain for future use to obviate the need to re-generate it.

> [!NOTE]
> Typically, you will configure the listener's TLS Identity once during initial launch and re-use it (from Keychain on any subsequent starts.

Example 7\. Set Listener's TLS identity

* Import
* Create Self-Signed Cert
* Use Anonymous Self-Signed Certificate

Import an identity from a secure key and certificate data source.

```swift
listenerConfig.disableTLS  = false (1)

guard let pathToCert =
  Bundle.main.path(forResource: "cert", ofType: "p12")
else { /* process error */ return }

guard let localCertificate =
  try? NSData(contentsOfFile: pathToCert) as Data
else { /* process error */ return } (2)

let thisIdentity =
  try TLSIdentity.importIdentity(withData: localCertificate,
                                password: "123",
                                label: thisSecId) (3)

// Set the credentials the server presents the client
listenerConfig.tlsIdentity = thisIdentity    (4)
```

**Notes on example:**

| **1** | Ensure TLS is used                                                        |
| ----- | ------------------------------------------------------------------------- |
| **2** | Get key and certificate data                                              |
| **3** | Use the retrieved data to create and store the TLS identity               |
| **4** | Set this identity as the one presented in response to the client's prompt |

Create a TLSIdentity for the server using convenience API. The system generates a self-signed certificate.

```swift
listenerConfig.disableTLS  = false (1)

let attrs = [certAttrCommonName: "Couchbase Inc"] (2)

let thisIdentity =
  try TLSIdentity.createIdentity(forServer: true, /* isServer */
        attributes: attrs,
        expiration: Date().addingTimeInterval(86400),
        label: "Server-Cert-Label") (3)

// Set the credentials the server presents the client
listenerConfig.tlsIdentity = thisIdentity    (4)
```

**Notes on example:**

| **1** | Ensure TLS is used.                                                                              |
| ----- | ------------------------------------------------------------------------------------------------ |
| **2** | Map the required certificate attributes, in this case the common name.                           |
| **3** | Create the required TLS identity using the attributes. Add to Keychain as 'couchbase-docs-cert'. |
| **4** | Configure the server to present the defined identity credentials when prompted.                  |

This examples uses an "anonymous" self signed certificate. Generated certificates are held in Keychain.

```swift
listenerConfig.disableTLS  = false (1)

// Set the credentials the server presents the client
// Use an anonymous self-signed cert
listenerConfig.tlsIdentity = nil (2)
```

**Notes on example:**

| **1** | These are are the default settings. Authentication using an anonymous self-signed certificate is assumed. |
| ----- | --------------------------------------------------------------------------------------------------------- |

## [](#authenticating-the-client)Authenticating the Client

In this section: [Use Basic Authentication](#use-basic-authentication) | [Using Client Certificate Authentication](#using-client-certificate-authentication) | [Delete Entry](#delete-tls-identity) | [The Impact of TLS Settings](#the-impact-of-tls-settings)

Define how the server (listener) will authenticate the client as one it is prepared to interact with.

Whilst client authentication is optional, Couchbase lite provides the necessary tools to implement it. Use the [URLEndpointListenerConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/URLEndpointListenerConfiguration.html) class's [authenticator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/URLEndpointListenerConfiguration.html#/s:18CouchbaseLiteSwift32URLEndpointListenerConfigurationC13authenticatorAA0E13Authenticator%5FpSgvp) method to specify how the client-supplied credentials are to be authenticated.

Valid options are:

* No authentication — If you do not define an Authenticator then all clients are accepted.
* Basic Authentication — uses the [ListenerPasswordAuthenticator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes//ListenerPasswordAuthenticator.html) to authenticate the client using the client-supplied username and password (from the http authentication header).
* [ListenerCertificateAuthenticator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes//ListenerCertificateAuthenticator.html) — which authenticates the client using a client supplied chain of one or more certificates. You should initialize the authenticator using one of the following constructors:

  * A list of one or more root certificates — the client supplied certificate must end at a certificate in this list if it is to be authenticated
  * A block of code that assumes total responsibility for authentication — it must return a boolean response (true for an authenticated client, or false for a failed authentication).

### [](#use-basic-authentication)Use Basic Authentication

Define how to authenticate client-supplied username and password credentials. To use client-supplied certificates instead — see: [Using Client Certificate Authentication](#using-client-certificate-authentication)

Example 8\. Password authentication

```swift
// Configure how the client is to be authenticated
// Here, use Basic Authentication
listenerConfig.authenticator =
  ListenerPasswordAuthenticator(authenticator: {
    (validUser, validPassword) -> Bool in
      if (self._allowlistedUsers.contains {
            $0 == validPassword && $1 == validUser
          }) {
          return true
          }
        return false
      }) (1)
```

**Notes on example:**

| **1** | Where 'username'/'password' are the client-supplied values (from the http-authentication header) and validUser/validPassword are the values acceptable to the server. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#using-client-certificate-authentication)Using Client Certificate Authentication

Define how the server will authenticate client-supplied certificates.

There are two ways to authenticate a client:

* A chain of one or more certificates that ends at a certificate in the list of certificates supplied to the constructor for [ListenerCertificateAuthenticator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes//ListenerCertificateAuthenticator.html).
* Application logic: This method assumes complete responsibility for verifying and authenticating the client.  
If the parameter supplied to the constructor for `ListenerCertificateAuthenticator` is of type `ListenerCertificateAuthenticatorDelegate`, all other forms of authentication are bypassed.  
The client response to the certificate request is passed to the method supplied as the constructor parameter. The logic should take the form of function or block (such as, a closure expression) where the platform allows.

Example 9\. Set Certificate Authorization

* Root CA
* Application Logic

Configure the server (listener) to authenticate the client against a list of one or more certificates provided by the server to the the [ListenerCertificateAuthenticator](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes//ListenerCertificateAuthenticator.html).

```swift
// Authenticate using Cert Authority

// cert is a pre-populated object of type:SecCertificate representing a certificate
let rootCertData = SecCertificateCopyData(cert) as Data (1)
let rootCert = SecCertificateCreateWithData(kCFAllocatorDefault, rootCertData as CFData)! //

listenerConfig.authenticator = ListenerCertificateAuthenticator.init (rootCerts: [rootCert]) (2) (3)
```

**Notes on example:**

| **1** | Get the identity data to authenticate against. This can be, for example, from a resource file provided with the app, or an identity previously saved in Keychain.                                  |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Configure the authenticator to authenticate the client supplied certificate(s) using these root certs. A valid client will provide one or more certificates that match a certificate in this list. |
| **3** | Add the authenticator to the listener configuration.                                                                                                                                               |

Configure the server (listener) to authenticate the client using user-supplied logic.

```swift
// Authenticate self-signed cert using application logic

// cert is a user-supplied object of type:SecCertificate representing a certificate
let rootCertData = SecCertificateCopyData(cert) as Data (1)
let rootCert = SecCertificateCreateWithData(kCFAllocatorDefault, rootCertData as CFData)!

listenerConfig.authenticator = ListenerCertificateAuthenticator.init { (2)
  (certs) -> Bool in
    var certs:SecCertificate
    var certCommonName:CFString?
    let status=SecCertificateCopyCommonName(certs[0], &certCommonName)
    if (self._allowedCommonNames.contains(["name": certCommonName! as String])) {
        return true
    }
    return false
} (3)
```

**Notes on example:**

| **1** | Get the identity data to authenticate against. This can be, for example, from a resource file provided with the app, or an identity previously saved in Keychain.                                                                                                                       |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Configure the Authenticator to pass the root certificates to a user supplied code block. This code assumes complete responsibility for authenticating the client supplied certificate(s). It must return a boolean value; with true denoting the client supplied certificate authentic. |
| **3** | Add the authenticator to the listener configuration.                                                                                                                                                                                                                                    |

### [](#delete-tls-identity)Delete Entry

You can remove unwanted TLS identities from Keychain using the convenience API.

Example 10\. Deleting TLS Identities

```swift
try TLSIdentity.deleteIdentity(withLabel: serverCertLabel);
```

### [](#the-impact-of-tls-settings)The Impact of TLS Settings

The table in this section shows the expected system behavior (in regards to security) depending on the TLS configuration settings deployed.

__Table 1\. Expected system behavior__
| disableTLS | tlsIdentity (corresponding to server)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Expected system behavior                                                                                                                                                                                                 |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| true       | Ignored                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | TLS is disabled; all communication is plain text.                                                                                                                                                                        |
| false      | set to nil                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | The system will auto generate an _anonymous_ self signed cert. Active peers (clients) should be configured to accept self-signed certificates. Communication is encrypted                                                |
| false      | Set to server identity generated from a self- or CA-signed certificate On first use — Bring your own certificate and private key; for example, using the [TLSIdentity](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/TLSIdentity.html) class's [CreateIdentity()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/TLSIdentity.html#/s:18CouchbaseLiteSwift11TLSIdentityC14createIdentity9forServer10attributes10expiration5labelACSb%5FSDyS2SG10Foundation4DateVSgSStKFZ) method to add it to the Keychain. Each time — Use the server identity from the certificate stored in the Keychain; for example, using the [TLSIdentity](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/TLSIdentity.html) class's [identity(withLabel:)](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/TLSIdentity.html#//s:18CouchbaseLiteSwift11TLSIdentityC8identity9withLabelACSgSS%5FtKFZ) method with the alias you want to retrieve.. | System will use the configured identity. Active peers will validate the server certificate corresponding to the TLSIdentity (as long as they are configured to not skip validation — see [TLS Security](#tls-security)). |

## [](#start-listener)Start Listener

Once you have completed the Listener's configuration settings you can initialize the Listener instance and start it running — see: [Example 11](#initialize-and-start-listener)

Example 11\. Initialize and start listener

```swift
// Initialize the listener
_thisListener = URLEndpointListener(config: listenerConfig) (1)
guard let thisListener = _thisListener else {
  throw ListenerError.NotInitialized
  // ... take appropriate actions
}
// Start the listener
try thisListener.start() (2)
```

Unresolved directive in common-p2psync-websocket-using-passive.adoc - include::{module-callouts}\[tags=listener-start, indent=0\]

## [](#monitor-listener)Monitor Listener

Use the Listener's `[status](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/URLEndpointListener.html#/s:18CouchbaseLiteSwift19URLEndpointListenerC6statusAC16ConnectionStatusVvp)` property/method to get counts of total and active connections — see: [Example 12](#get-connection-counts).

You should note that these counts can be extremely volatile. So, the actual number of active connections may have changed, by the time the `[ConnectionStatus](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/URLEndpointListener/ConnectionStatus.html)` class returns a result.

Example 12\. Get connection counts

```swift
let totalConnections = thisListener.status.connectionCount
let activeConnections = thisListener.status.activeConnectionCount
```

**Notes on example:**

Unresolved directive in common-p2psync-websocket-using-passive.adoc - include::{example\_callouts}\[tags=listener-status-check, indent=0\]

## [](#stop-listener)Stop Listener

It is best practice to check tha status of the listener's connections and stop only when you have confirmed that there are no active connections — see [Example 12](#get-connection-counts).

Example 13\. Stop listener using `stop` method

```swift
thisListener.stop()
```

> [!NOTE]
> Closing the database will also close the listener.

## [](#related-content)Related Content

###### [](#)

How to

* [Passive Peer](../../current/swift/p2psync-websocket-using-passive.md)
* [Active Peer](../../current/swift/p2psync-websocket-using-active.md)

###### [](#-2)

Concepts

* [Landing P2Psync](#couchbase-lite:swift:landing-p2psync.adoc)
* [API References](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift).

###### [](#-3)

Community Resources …​

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

* [Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)