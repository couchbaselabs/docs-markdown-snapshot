---
title: Active-Passive Peer-to-Peer Sync
description: Where MultiPeer Sync is not available, Couchbase Lite's
  Active-Passive Peer-to-Peer Synchronization enables edge devices to
  synchronize securely without consuming centralized cloud-server resources
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/android/pages/p2psync-websocket.adoc
pubDate: 2026-03-24T03:43:23.693Z
link: xref:couchbase-lite:android:p2psync-websocket.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/android/p2psync-websocket.html)

# Active-Passive Peer-to-Peer Sync

> Description — _Where MultiPeer Sync is not available, Couchbase Lite’s Active-Passive Peer-to-Peer Synchronization enables edge devices to synchronize securely without consuming centralized cloud-server resources_  
> _Abstract — An introduction to Couchbase Lite’s Peer-to-Peer Synchronization and its concepts._  
> Related Content — [API Reference](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/) | [Passive Peer](p2psync-websocket-using-passive.md) | [Active Peer](p2psync-websocket-using-active.md)

> [!TIP]
> [Multipeer P2P Replicator](p2psync-multipeer.md)

Multipeer P2P Replicator is available for Android, offering:

* Auto-discovery over local Wi-Fi (via `DNS-SD`)
* Lightweight and low-maintenance configuration
* Dynamic mesh topology for optimal peer connectivity
* Secure communication via TLS and certificate-based authentication

## [](#introduction)Introduction

Couchbase Lite’s Peer-to-Peer synchronization solution offers secure storage and bidirectional data synchronization between edge devices without needing a centralized cloud-based control point.

Couchbase Lite’s Peer-to-Peer data synchronization provides:

* Instant WebSocket-based listener for use in Peer-to-Peer applications communicating over IP-based networks
* Simple application development, enabling sync with a short amount of code
* Optimized network bandwidth usage and reduced data transfer costs with Delta Sync support
* Securely sync data with built-in support for Transport Layer Security (TLS) encryption and authentication support
* Document management. Reducing conflicts in concurrent writes with built-in conflict management support
* Built-in network resiliency

## [](#overview)Overview

Peer-to-Peer synchronization requires one Peer to act as the Listener to the other Peer’s replicator.

![docs listener diagram](../_images/docs-listener-diagram.png) 

Peer-to-Peer synchronization requires one Peer to act as the Listener to the other Peer’s replicator. Therefore, to use Peer-to-Peer synchronization in your application, you must configure one Peer to act as a Listener using the Couchbase Listener API, the most important of which include _URLEndpointListener_ and _URLEndpointListenerConfiguration_.

Example 1\. Simple workflow

1. Configure the Listener (_passive peer_, or _server_)
2. Initialize the Listener, which listens for incoming WebSocket connections (on a user-defined, or auto-selected, port)
3. Configure a replicator (_active peer_, or _client_)
4. Use some form of discovery phase, perhaps with a zero-config protocol such as Network Service Discovery — see: <https://developer.android.com/training/connect-devices-wirelessly/nsd>, or use known URL endpoints, to identify a Listener
5. Point the replicator at the Listener
6. Initialize the replicator
7. Replicator and Listener engage in the configured security protocol exchanges to confirm connection
8. If connection is confirmed then replication will commence, synchronizing the two data stores.

Here you can see configuration involves a [Passive Peer](p2psync-websocket-using-passive.md) and an [Active Peer](p2psync-websocket-using-active.md) and a user-friendly Listener configuration in [Basic Setup](#simple-configuration).

Couchbase Lite supports different transport modes depending on the peer-to-peer synchronization approach:

### [](#active-passive-peer-to-peer)Active-Passive Peer-to-Peer

* Supports: Wi-Fi (IP-based transport modes only)

You can also learn how to implement Peer-to-Peer synchronization by referring to our tutorial — see: [Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md).

## [](#features)Features

Couchbase Lite for Android’s Peer-to-Peer synchronization solution provides support for cross-platform synchronization, for example, between Android and iOS devices.

Each listener instance serves a single Couchbase Lite database, enabling synchronization for documents within specified collections of that database.

Having a Listener on a database still allows you to open replications to the other clients. For example, a Listener can actively begin replicating to other Listeners while listening for connections. These replications can be for the same or a different database.

The Listener will automatically select a port to use or a user-specified port. It will also listen on all available networks, unless you specify a specific network.

### [](#security)Security

Couchbase Lite’s Peer-to-Peer synchronization supports encryption and authentication over TLS with multiple modes, including:

* No encryption, for example, clear text.
* CA Cert
* Self-signed Cert
* Anonymous Self-signed — an auto-generated anonymous TLS identity is generated if no identity is specified. This TLS identity provides encryption but **not** authentication.  
Any self-signed certificates generated by the convenience API are stored in secure storage.

The replicator (client) can handle certificates pinned by the Listener for authentication purposes.

Support is also provided for basic authentication using username and password credentials. Whilst this can be used in clear text mode, developers are strongly advised to use TLS encryption.

For testing and development purposes, support is provided for the client (active, replicator) to skip verification of self-signed certificates; this mode should not be used in production.

### [](#error-handling)Error Handling

When a Listener is stopped, then all connected replicators are notified by a WebSocket error. Your application should distinguish between transient and permanent connectivity errors.

#### [](#passive-peers)Passive peers

A Passive Peer losing connectivity with an Active Peer will clean up any associated endpoint connections to that Peer. The Active Peer may attempt to reconnect to the Passive Peer.

#### [](#active-peers)Active peers

An Active Peer permanently losing connectivity with a Passive Peer will cease replicating.

An Active Peer temporarily losing connectivity with a passive Peer will use exponential backoff functionality to attempt reconnection.

### [](#delta-sync)Delta Sync

Optional delta-sync support is provided but is inactive by default.

Delta-sync can be enabled on a per-replication basis provided that the databases involved are also configured to permit it.

### [](#conflict-resolution)Conflict Resolution

Conflict resolution for Peer-to-Peer synchronization works in the same way as it does for Sync Gateway replication, with both custom and automatic resolution available.

## [](#simple-configuration)Basic Setup

You can configure a Peer-to-Peer synchronization with just a short amount of code as shown here in [Example 2](#ex-simple-listener) and [Example 3](#ex-simple-replicator).

Example 2\. Simple Listener

This simple listener configuration will give you a listener ready to participate in an encrypted synchronization with a replicator providing a valid user name and password.

* Kotlin
* Java

```Kotlin
val listener = URLEndpointListener(
    URLEndpointListenerConfigurationFactory.newConfig(
        collections = db.collections,
        authenticator = ListenerPasswordAuthenticator { user, pwd ->
            (user == "daniel") && (String(pwd) == "123")  (1)
        })
)
listener.start() (2)
thisListener = listener
```

```Java
final URLEndpointListenerConfiguration thisConfig =
    new URLEndpointListenerConfiguration(collections); (1)

thisConfig.setAuthenticator(
    new ListenerPasswordAuthenticator(
            (username, password) ->
                    validUser.equals(username) && Arrays.equals(validPass, password)
    )
); (2)

final URLEndpointListener thisListener =
    new URLEndpointListener(thisConfig); (3)

thisListener.start(); (4)
```

| **1** | Initialize the Listener configuration                              |
| ----- | ------------------------------------------------------------------ |
| **2** | Configure the client authenticator to require basic authentication |
| **3** | Initialize the Listener                                            |
| **4** | Start the Listener                                                 |

Example 3\. Simple Replicator

This simple replicator configuration will give you an encrypted, bi-directional Peer-to-Peer synchronization with automatic conflict resolution.

* Kotlin
* Java

```Kotlin
val theListenerEndpoint: Endpoint = URLEndpoint(URI("wss://10.0.2.2:4984/db")) (1)
val repl = Replicator(
    ReplicatorConfigurationFactory.newConfig(
        collections = CollectionConfiguration.fromCollections(collections),
        target = theListenerEndpoint,
        authenticator = BasicAuthenticator("valid.user", "valid.password.string".toCharArray()), (2)
        acceptOnlySelfSignedServerCertificate = true
    )
)
repl.start() (3)
thisReplicator = repl
```

```Java
Endpoint theListenerEndpoint
    = new URLEndpoint(new URI("wss://10.0.2.2:4984/db")); (1)

Set<CollectionConfiguration> collConfigs = CollectionConfiguration.fromCollections(collections);

ReplicatorConfiguration thisConfig =
    new ReplicatorConfiguration(collConfig, theListenerEndpoint) (2)

        .setAcceptOnlySelfSignedServerCertificate(true) (3)
        .setAuthenticator(new BasicAuthenticator(
            "valid.user",
            "valid.password".toCharArray())); (4)

Replicator repl = new Replicator(thisConfig); (5)
// Start the replicator
repl.start(); (6)
// (be sure to hold a reference somewhere that will prevent it from being GCed)
thisReplicator = repl;
```

| **1** | Get the Listener’s endpoint. Here we use a known URL, but it could be a URL established dynamically in a discovery phase.                 |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Initialize the replicator configuration with the database to be synchronized and the Listener it is to synchronize with                   |
| **3** | Configure the replicator to expect a self-signed certificate from the Listener                                                            |
| **4** | Configure the replicator to present basic authentication credentials if the Listener prompts for them (client authentication is optional) |
| **5** | Initialize the replicator                                                                                                                 |
| **6** | Start the replicator                                                                                                                      |

## [](#api-highlights)API Highlights

### [](#urlendpointlistener)URLEndpointListener

The `URLEndpointListener` is the listener for peer-to-peer synchronization. It acts like a passive replicator, in the same way that Sync Gateway does in a 'standard' replication. On the client side, the listener’s endpoint is used to point the replicator to the listener.

Core functionalities of the listener are:

* Users can initialize the class using a _URLEndpointListenerConfiguration_ object.
* The listener can be started, or can be stopped.
* Once the listener is started, a total number of connections or active connections can be checked.

API Reference: [URLEndpointListener](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/URLEndpointListener.html)

### [](#urlendpointlistenerconfiguration)URLEndpointListenerConfiguration

Use this to create a configuration object you can then use to initialize the listener.

Port

This is the port that the listener will listen to.

If the port is null or zero, the listener will auto-assign an available port to listen on.

Default value is null or zero depending on platform. When the listener is not started, the port is null (or zero if the platform requires).

Network Interface

Use this to select a specific Network Interface to use, in the form of the IP Address or network interface name.

If the network interface is specified, only that interface wil be used.

If the network interface is not specified, all available network interfaces will be used.

The value is null if the listener is not started.

disableTLS

You can use [URLEndpointListenerConfiguration](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html)'s [setDisableTLS](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html#setDisableTls-boolean-) method to disable TLS communication if necessary

The `disableTLS` setting must be 'false' when _Client Cert Authentication_ is required.

Basic Authentication can be used with, or without, TLS.

[setDisableTLS](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html#setDisableTls-boolean-) works in conjunction with `TLSIdentity`, to enable developers to define the key and certificate to be used.

* If `disableTLS` is true — TLS communication is disabled and TLS identity is ignored. Active peers will use the `ws://` URL scheme used to connect to the listener.
* If `disableTLS` is false or not specified — TLS communication is enabled.  
Active peers will use the `wss://` URL scheme to connect to the listener.

API Reference: [setDisableTLS](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html#setDisableTls-boolean-)

tlsIdentity

Use [URLEndpointListenerConfiguration](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html)'s [setTlsIdentity](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html#setTlsIdentity-com.couchbase.lite.TLSIdentity-) method to configure the TLS Identity used in TLS communication.

If `TLSIdentity` is not set, then the listener uses an auto-generated anonymous self-signed identity (unless `disableTLS = true`). Whilst the client cannot use this to authenticate the server, it will use it to encrypt communication, giving a more secure option than non-TLS communication.

The auto-generated anonymous self-signed identity is saved in secure storage for future use to obviate the need to re-generate it.

When the listener is not started, the identity is null. When TLS is disabled, the identity is always null.

API Reference: [setTlsIdentity](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html#setTlsIdentity-com.couchbase.lite.TLSIdentity-)

authenticator

Use this to specify the authenticator the listener uses to authenticate the client’s connection request. This should be set to one of the following:

* ListenerPasswordAuthenticator
* ListenerCertificateAuthenticator
* Null — there is no authentication.

API Reference: [setAuthenticator](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html#setAuthenticator-com.couchbase.lite.ListenerAuthenticator-)

readOnly

Use this to allow only pull replication. Default value is false.

enableDeltaSync

The option to enable Delta Sync and replicate only changed data also depends on the delta sync settings at database level. The default value is false.

API Reference: [URLEndpointListenerConfiguration](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html)

## [](#security-2)Security

Couchbase Lite’s Peer-to-Peer synchronization ensures secure communication through TLS and supports multiple authentication mechanisms.

### [](#tls-identity)TLS Identity

The URLEndpointListener uses a TLS identity to establish secure connections. (A TLS identity is an RSA public/private key pair and certificate.) The identity can include either a certificate signed by a trusted Certificate Authority (CA), or a self-signed certificate. If no identity is specified, the listener automatically generates an anonymous, self-signed certificate, which is primarily used for encryption, but not for authentication.

When replicating with a listener that uses a self-signed certificate, the replicator (client) can be configured to skip certificate validation. This option is useful for development or testing, but not recommended for production.

> [!NOTE]
> The minimum supported version of TLS is TLS 1.2\.

### [](#authentication)Authentication Mechanisms

The URLEndpointListener supports two authentication mechanisms:

* Basic Authentication, using a username and password.
* Certificate Authentication, which authenticates clients using client certificates, and is only available when TLS is enabled.

### [](#using-secure-storage)Using Secure Storage

TLS and its associated keys and certificates might require using secure storage to minimize the chances of a security breach. The implementation of this storage differs from platform to platform. This table summarizes the secure storage used to store keys and certificates.

* Android
* MacOS / iOS
* Java
* .Net (excluding Xamarin)
* Xamarin

__Secure storage details__
| **Platform**            | Android                                                                                                                                                                                                                                                  |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Key Storage**         | Android System KeyStore                                                                                                                                                                                                                                  |
| **Certificate Storage** | Android System KeyStore                                                                                                                                                                                                                                  |
| **Notes**               | Android KeyStore was introduced from Android API 18. Android KeyStore security has evolved over time to provide more secure support. Please check this document for more info: [Hardware-backed Keystore](https://source.android.com/security/keystore). |
| **Reference**           | [Android Keystore system](https://developer.android.com/training/articles/keystore)                                                                                                                                                                      |

__Secure storage details__
| **Platform**            | MacOS/iOS                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| **Key Storage**         | KeyChain                                                                                    |
| **Certificate Storage** | KeyChain                                                                                    |
| **Notes**               | Use kSecAttrLabel of the SecCertificate to store the TLSIdentity’s label                    |
| **Reference**           | [Keychain services](https://developer.apple.com/documentation/security/keychain%5Fservices) |

__Secure storage details__
| **Platform**            | Java                                                                                                                                                                                                                                                          |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Key Storage**         | User Specified KeyStore                                                                                                                                                                                                                                       |
| **Certificate Storage** | User Specified KeyStore                                                                                                                                                                                                                                       |
| **Notes**               | The KeyStore represents a storage facility for cryptographic keys and certificates. It’s users' choice to decide whether to persist the KeyStore or not. The supported KeyStore types are PKCS12 (Default from Java 9) and JKS (Default on Java 8 and below). |
| **Reference**           | [Class KeyStore](https://docs.oracle.com/javase/7/docs/api/java/security/KeyStore.html)                                                                                                                                                                       |

__Secure storage details__
| **Platform**            | .Net (excluding Xamarin)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Key Storage**         | Opaque; Keys are stored automatically by the runtime when storing the certificate with the PersistKeySet flag set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Certificate Storage** | User specified X509Store                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Notes**               | Use a map file to map the stored certificates and TLSIdentity’s labels. The actual store of X509Store depends on platform implementation: Windows — OS KeyStore macOS — KeyChain Linux — file on filesystem                                                                                                                                                                                                                                                                                                                                                                             |
| **Reference**           | Opaque Keys: [X509Certificate2Collection.Import Method](https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.x509certificates.x509certificate2collection.import?view=netstandard-2.0#System%5FSecurity%5FCryptography%5FX509Certificates%5FX509Certificate2Collection%5FImport%5FSystem%5FByte%5F%5F%5FSystem%5FString%5FSystem%5FSecurity%5FCryptography%5FX509Certificates%5FX509KeyStorageFlags%5F) X509Store Reference: [X509Store Class](https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.x509certificates.x509store?view=netcore-3.1) |

__Secure storage details__
| **Platform**            | Xamarin                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Key Storage**         | RSACryptoServiceProvider provided by Xamarin.                                                                                                                                                                                                                                                                                                                             |
| **Certificate Storage** | User specified X509Store                                                                                                                                                                                                                                                                                                                                                  |
| **Notes**               | Use a map file to map the stored certificates and TLSIdentity’s labels. The same label is used to persist the key The current Xamarin’s RSACryptoServiceProvider implementation stores keys in files. Users can use TLSIdentity.getIdentity(X509Certificate2Collection) to create a TLSIdentity object if they would like to manage the keys and certificates themselves. |
| **Reference**           | RSACryptoServiceProvider: [Store asymmetric keys in a key container](https://docs.microsoft.com/en-us/dotnet/standard/security/how-to-store-asymmetric-keys-in-a-key-container) X509Store Reference — [X509Store Class](https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.x509certificates.x509store?view=netcore-3.1)                             |

## [](#related-content)Related Content

###### [](#)

How to

* [Passive Peer](p2psync-websocket-using-passive.md)
* [Active Peer](p2psync-websocket-using-active.md)

.

###### [](#-2)

Concepts

* [Peer-to-Peer Sync](#android:landing-p2psync.adoc)
* [API References](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/)

.

###### [](#-3)

Community Resources …​

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

. [Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)