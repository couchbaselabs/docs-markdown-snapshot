---
title: Passive Peer
description: Couchbase Lite's Peer-to-Peer Synchronization enables edge devices
  to synchronize securely without consuming centralized cloud-server resources
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/c/pages/p2psync-websocket-using-passive.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.0@couchbase-lite:c:p2psync-websocket-using-passive.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/c/p2psync-websocket-using-passive.html)

# Passive Peer

> Description — _Couchbase Lite’s Peer-to-Peer Synchronization enables edge devices to synchronize securely without consuming centralized cloud-server resources_  
> _Abstract — How to set up a Listener to accept a Replicator connection and sync using peer-to-peer_  
> Related Content — [API Reference](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html) | [Passive Peer](p2psync-websocket-using-passive.md) | [Active Peer](p2psync-websocket-using-active.md)

> [!NOTE]
> Code Snippets
> 
> All code examples are indicative only. They demonstrate the basic concepts and approaches to using a feature. Use them as inspiration and adapt these examples to best practice when developing applications for your platform.

## [](#introduction)Introduction

This content provides code and configuration examples covering the implementation of [Peer-to-Peer Sync](refer-glossary.md#peer-to-peer-sync) over websockets. Specifically it covers the implementation of a [Passive Peer](refer-glossary.md#passive-peer).

This _passive peer_ (also referred to as the server, or listener) will accept a connection from an [Active Peer](refer-glossary.md#active-peer) (also referred to as the client or replicator) and participate in the replication of database changes to synchronize both databases.

Subsequent sections provide additional details, and examples for the main configuration options.

> [!NOTE]
> Secure Storage
> 
> The use of TLS, its associated keys and certificates requires using secure storage to minimize the chances of a security breach. The implementation of this storage differs from platform to platform — see [Using secure storage](p2psync-websocket.md#using-secure-storage).

## [](#configuration-summary)Configuration Summary

You should configure and initialize a listener for each Couchbase Lite database instance you want to sync. There is no limit on the number of listeners you may configure — [Example 1](#simple-listener-initialization) shows a simple initialization and configuration process.

Example 1\. Listener configuration and initialization

```c

```

| **1** | Identify the local database to be used — see: [Initialize the Listener Configuration](#initialize-the-listener-configuration)                                                                                                                                                                                                                                                                               |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Optionally, choose a port to use. By default the system will automatically assign a port — to over-ride this, see: [Set Port and Network Interface](#lbl-set-network-and-port)                                                                                                                                                                                                                              |
| **3** | Optionally, choose a network-interface to use. By default the system will listen on all network interfaces — to over-ride this see: [Set Port and Network Interface](#lbl-set-network-and-port)                                                                                                                                                                                                             |
| **4** | Optionally, choose to sync only changes, the default is not to enable delta-sync — see: [Delta Sync](#delta-sync).                                                                                                                                                                                                                                                                                          |
| **5** | Set server security. TLS is always enabled out-of-the-box, so you can usually omit this line. But you _can_, optionally, disable TLS (**not** advisable in production) — see: [TLS Security](#lbl-tls-security)                                                                                                                                                                                             |
| **6** | Set the credentials this server will present to the client for authentication. Here we show the default TLS authentication, which is by anonymous self-signed certificate. The server must always authenticate itself to the client.                                                                                                                                                                        |
| **7** | Set client security — define the credentials the server expects the client to present for authentication. Here we show how basic authentication is configured to authenticate the client-supplied credentials from the http authentication header against valid credentials — see [Authenticating the Client](#lbl-authenticating-the-client) for more options.Note that client authentication is optional. |
| **8** | Initialize the listener using the configuration settings.                                                                                                                                                                                                                                                                                                                                                   |
| **9** | [Start Listener](#lbl-start-listener)                                                                                                                                                                                                                                                                                                                                                                       |

## [](#api-references)API References

You can find [C API References](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html) here.

## [](#device-discovery)Device Discovery

**This phase is optional:** If the listener is initialized on a well known URL endpoint (for example, a static IP Address or well known DNS address) then you can configure active peers to connect to those.

Prior to initiating the listener you may execute a peer discovery phase. For the passive peer, this involves advertising the service using, for example and waiting for an invite from the active peer. The connection is established once the passive peer has authenticated and accepted an active peer’s invitation.

## [](#initialize-the-listener-configuration)Initialize the Listener Configuration

Initialize the listener configuration with the local database — see [Example 2](#ex-locdb)All other configuration values take their default setting.

Each Listener instance serves one Couchbase Lite database. Couchbase sets no hard limit on the number of listeners you can initialize.

Example 2\. Specify Local Database

```c

```

| **1** | Set the local database using the [URLEndpointListenerConfiguration](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FURLEndpointListenerConfiguration.html)'s constructor [\-initWithDatabase:](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FURLEndpointListenerConfiguration.html#URLEndpointListenerConfiguration%28im%29initWithDatabase:).The database must be opened before the listener is started. thisDB has previously been declared as an object of type Database. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#lbl-set-network-and-port)Set Port and Network Interface

### [](#port-number)Port number

The Listener will automatically select an available port if you do not specify one — see [Example 3](#ex-port) for how to specify a port.

Example 3\. Specify a port

```c

```

| **1** | To use a canonical port — one known to other applications — specify it explicitly using the [port](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FURLEndpointListenerConfiguration.html#URLEndpointListenerConfiguration%28py%29port) method shown here.Ensure that any port you do specify is not blocked by firewall rules. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#network-interface)Network Interface

The Listener will listen on all network interfaces by default.

Example 4\. Specify a Network Interface to Use

```c

```

| **1** | To specify an interface — one known to other applications — identify it explicitly, using the [networkInterface](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FURLEndpointListenerConfiguration.html#URLEndpointListenerConfiguration%28py%29networkInterface) method shown here. This must be either an IP Address or network interface name such as en0. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#delta-sync)Delta Sync

Delta Sync allows clients to sync only those parts of a document that have changed. This can result in significant savings in bandwidth consumption as well as throughput improvements. Both valuable benefits, especially when network bandwidth is constrained.

Example 5\. Enable delta sync

```c

```

| **1** | Delta sync replication is not enabled by default. Use [URLEndpointListenerConfiguration](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FURLEndpointListenerConfiguration.html)'s [enableDeltaSync](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FURLEndpointListenerConfiguration.html#URLEndpointListenerConfiguration%28py%29enableDeltaSync) method to activate or deactivate it. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#lbl-tls-security)TLS Security

### [](#enable-or-disable-tls)Enable or Disable TLS

Define whether the connection is to use TLS or clear text.

TLS based encryption is enabled by default and this setting ought to be used in any production environment. However, it _can_ be disabled, for example for development and-or test environments.

When TLS is enabled, Couchbase Lite provides several options on how the Listener may be configured with an appropriate TLS Identity — see [Configure TLS Identity for Listener](#configure-tls-identity-for-listener).

You can use [URLEndpointListenerConfiguration](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FURLEndpointListenerConfiguration.html)'s [disableTLS](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FURLEndpointListenerConfiguration.html#URLEndpointListenerConfiguration%28py%29disableTLS) method to disable TLS communication if necessary

The `disableTLS` setting must be 'false' when _Client Cert Authentication_ is required.

Basic Authentication can be used with, or without, TLS.

[disableTLS](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FURLEndpointListenerConfiguration.html#URLEndpointListenerConfiguration%28py%29disableTLS) works in conjunction with `TLSIdentity`, to enable developers to define the key and certificate to be used.

* If `disableTLS` is true — TLS communication is disabled and TLS identity is ignored. Active peers will use the `ws://` URL scheme used to connect to the listener.
* If `disableTLS` is false or not specified — TLS communication is enabled.  
Active peers will use the `wss://` URL scheme to connect to the listener.

### [](#configure-tls-identity-for-listener)Configure TLS Identity for Listener

Define the credentials the server will present to the client for authentication. Note that the server must always authenticate itself with the client — see: [Authenticate Listener on Active Peer](p2psync-websocket-using-active.md#authenticate-listener) for how the client deals with this.

Use [URLEndpointListenerConfiguration](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FURLEndpointListenerConfiguration.html)'s [tlsIdentity](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FURLEndpointListenerConfiguration.html#URLEndpointListenerConfiguration%28py%29tlsIdentity) method to configure the TLS Identity used in TLS communication.

If `TLSIdentity` is not set, then the listener uses an auto-generated anonymous self-signed identity (unless `disableTLS = true`). Whilst the client cannot use this to authenticate the server, it will use it to encrypt communication, giving a more secure option than non-TLS communication.

The auto-generated anonymous self-signed identity is saved in secure storage for future use to obviate the need to re-generate it.

> [!NOTE]
> Typically, you will configure the listener’s TLS Identity once during initial launch and re-use it (from secure storage on any subsequent starts.

Here are some example code snippets showing:

* Importing a TLS identity — see: [Example 6](#ex-import-tls-id)
* Setting TLS identity to expect self-signed certificate — — see: [Example 7](#ex-create-tls-id)
* Setting TLS identity to expect anonymous certificate — see: [Example 8](#ex-anon-tls-id)

Example 6\. Import Listener’s TLS identity

Import an identity from a secure key and certificate data source.

```c

```

| **1** | Ensure TLS is used                                                        |
| ----- | ------------------------------------------------------------------------- |
| **2** | Get key and certificate data                                              |
| **3** | Use the retrieved data to create and store the TLS identity               |
| **4** | Set this identity as the one presented in response to the client’s prompt |

Example 7\. Create Self-Signed Cert

Create a TLSIdentity for the server using convenience API. The system generates a self-signed certificate.

```c

```

| **1** | Ensure TLS is used.                                                                                    |
| ----- | ------------------------------------------------------------------------------------------------------ |
| **2** | Map the required certificate attributes, in this case the common name.                                 |
| **3** | Create the required TLS identity using the attributes. Add to secure storage as 'couchbase-docs-cert'. |
| **4** | Configure the server to present the defined identity credentials when prompted.                        |

Example 8\. Use Anonymous Self-Signed Certificate

This example uses an _anonymous_ self signed certificate. Generated certificates are held in secure storage.

```c

```

| **1** | Ensure TLS is used.This is the default setting.                                      |
| ----- | ------------------------------------------------------------------------------------ |
| **2** | Authenticate using an anonymous self-signed certificate.This is the default setting. |

## [](#lbl-authenticating-the-client)Authenticating the Client

In this section: [Use Basic Authentication](#use-basic-authentication) | [Using Client Certificate Authentication](#using-client-certificate-authentication) | [Delete Entry](#delete-tls-identity) | [The Impact of TLS Settings](#the-impact-of-tls-settings)

Define how the server (listener) will authenticate the client as one it is prepared to interact with.

Whilst client authentication is optional, Couchbase lite provides the necessary tools to implement it. Use the [URLEndpointListenerConfiguration](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FURLEndpointListenerConfiguration.html) class’s [authenticator](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FURLEndpointListenerConfiguration.html#URLEndpointListenerConfiguration%28py%29authenticator) method to specify how the client-supplied credentials are to be authenticated.

Valid options are:

* No authentication — If you do not define an Authenticator then all clients are accepted.
* Basic Authentication — uses the [ListenerPasswordAuthenticator](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FListenerPasswordAuthenticator.html) to authenticate the client using the client-supplied username and password (from the http authentication header).
* [ListenerCertificateAuthenticator](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FListenerCertificateAuthenticator.html) — which authenticates the client using a client supplied chain of one or more certificates. You should initialize the authenticator using one of the following constructors:

  * A list of one or more root certificates — the client supplied certificate must end at a certificate in this list if it is to be authenticated
  * A block of code that assumes total responsibility for authentication — it must return a boolean response (true for an authenticated client, or false for a failed authentication).

### [](#use-basic-authentication)Use Basic Authentication

Define how to authenticate client-supplied username and password credentials. To use client-supplied certificates instead — see: [Using Client Certificate Authentication](#using-client-certificate-authentication)

Example 9\. Password authentication

```c

```

| **1** | Where 'username'/'password' are the client-supplied values (from the http-authentication header) and validUser/validPassword are the values acceptable to the server. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#using-client-certificate-authentication)Using Client Certificate Authentication

Define how the server will authenticate client-supplied certificates.

There are two ways to authenticate a client:

* A chain of one or more certificates that ends at a certificate in the list of certificates supplied to the constructor for [ListenerCertificateAuthenticator](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FListenerCertificateAuthenticator.html) — see: [Example 10](#ex-set-cert-auth)
* Application logic: This method assumes complete responsibility for verifying and authenticating the client — see: [Example 11](#ex-use-app-logic)  
If the parameter supplied to the constructor for `ListenerCertificateAuthenticator` is of type `ListenerCertificateAuthenticatorDelegate`, all other forms of authentication are bypassed.  
The client response to the certificate request is passed to the method supplied as the constructor parameter. The logic should take the form of function or block (such as, a closure expression) where the platform allows.

Example 10\. Set Certificate Authorization

Configure the server (listener) to authenticate the client against a list of one or more certificates provided by the server to the the [ListenerCertificateAuthenticator](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FListenerCertificateAuthenticator.html).

```c

```

| **1** | Get the identity data to authenticate against. This can be, for example, from a resource file provided with the app, or an identity previously saved in secure storage.                            |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Configure the authenticator to authenticate the client supplied certificate(s) using these root certs. A valid client will provide one or more certificates that match a certificate in this list. |
| **3** | Add the authenticator to the listener configuration.                                                                                                                                               |

Example 11\. Application Logic

Configure the server (listener) to authenticate the client using user-supplied logic.

```c

```

| **1** | Get the identity data to authenticate against. This can be, for example, from a resource file provided with the app, or an identity previously saved in secure storage.                                                                                                                 |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Configure the Authenticator to pass the root certificates to a user supplied code block. This code assumes complete responsibility for authenticating the client supplied certificate(s). It must return a boolean value; with true denoting the client supplied certificate authentic. |
| **3** | Add the authenticator to the listener configuration.                                                                                                                                                                                                                                    |

### [](#delete-tls-identity)Delete Entry

You can remove unwanted TLS identities from secure storage using the convenience API.

Example 12\. Deleting TLS Identities

```c

```

### [](#the-impact-of-tls-settings)The Impact of TLS Settings

The table in this section shows the expected system behavior (in regards to security) depending on the TLS configuration settings deployed.

__Table 1\. Expected system behavior__
| disableTLS | tlsIdentity (corresponding to server)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Expected system behavior                                                                                                                                                                                                     |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| true       | Ignored                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | TLS is disabled; all communication is plain text.                                                                                                                                                                            |
| false      | set to nil                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | The system will auto generate an _anonymous_ self signed cert. Active peers (clients) should be configured to accept self-signed certificates. Communication is encrypted                                                    |
| false      | Set to server identity generated from a self- or CA-signed certificate On first use — Bring your own certificate and private key; for example, using the [TLSIdentity](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FTLSIdentity.html) class’s [createIdentity()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FTLSIdentity.html#TLSIdentity%28cm%29createIdentityForServer:attributes:expiration:label:error:) method to add it to the secure storage. Each time — Use the server identity from the certificate stored in the secure storage; for example, using the [TLSIdentity](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FTLSIdentity.html) class’s [identityWithLabel:error](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FTLSIdentity.html#TLSIdentity%28cm%29identityWithLabel:error:) method with the alias you want to retrieve.. | System will use the configured identity. Active peers will validate the server certificate corresponding to the TLSIdentity (as long as they are configured to not skip validation — see [TLS Security](#lbl-tls-security)). |

## [](#lbl-start-listener)Start Listener

Once you have completed the Listener’s configuration settings you can initialize the Listener instance and start it running — see: [Example 13](#initialize-and-start-listener)

Example 13\. Initialize and start listener

```c

```

## [](#monitor-listener)Monitor Listener

Use the Listener’s `[status](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FURLEndpointListener.html#CBLURLEndpointListener%28py%29status)` property/method to get counts of total and active connections — see: [Example 14](#get-connection-counts).

You should note that these counts can be extremely volatile. So, the actual number of active connections may have changed, by the time the `[ConnectionStatus](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5FType%20Definitions/ConnectionStatus.html)` class returns a result.

Example 14\. Get connection counts

```c

```

## [](#stop-listener)Stop Listener

It is best practice to check tha status of the listener’s connections and stop only when you have confirmed that there are no active connections — see [Example 14](#get-connection-counts).

Example 15\. Stop listener using `stop` method

```c

```

> [!NOTE]
> Closing the database will also close the listener.

## [](#related-content)Related Content

###### [](#)

How to

* [Passive Peer](p2psync-websocket-using-passive.md)
* [Active Peer](p2psync-websocket-using-active.md)

###### [](#-2)

Concepts

* [Peer-to-Peer Sync](landing-p2psync.md)
* [API References](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html)

###### [](#-3)

Community Resources …​

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

[Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)