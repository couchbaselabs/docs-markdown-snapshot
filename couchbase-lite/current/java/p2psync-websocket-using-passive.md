---
title: Passive Peer
description: Couchbase Lite's Peer-to-Peer Synchronization enables edge devices
  to synchronize securely without consuming centralized cloud-server resources
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/java/pages/p2psync-websocket-using-passive.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:couchbase-lite:java:p2psync-websocket-using-passive.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/java/p2psync-websocket-using-passive.html)

# Passive Peer

> Description — _Couchbase Lite’s Peer-to-Peer Synchronization enables edge devices to synchronize securely without consuming centralized cloud-server resources_  
> _Abstract — How to set up a Listener to accept a Replicator connection and sync using peer-to-peer_  
> Related Content — [API Reference](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/) | [Passive Peer](p2psync-websocket-using-passive.md) | [Active Peer](p2psync-websocket-using-active.md)

> [!NOTE]
> Code Snippets
> 
> All code examples are indicative only. They demonstrate the basic concepts and approaches to using a feature. Use them as inspiration and adapt these examples to best practice when developing applications for your platform.

## [](#introduction)Introduction

This content provides code and configuration examples covering the implementation of [Peer-to-Peer Sync](refer-glossary.md#peer-to-peer-sync) over WebSockets. Specifically, it covers the implementation of a [Passive Peer](refer-glossary.md#passive-peer).

Couchbase’s Passive Peer (also referred to as the server, or Listener) will accept a connection from an [Active Peer](refer-glossary.md#active-peer) (also referred to as the client or replicator) and replicate database changes to synchronize both databases.

Subsequent sections provide additional details and examples for the main configuration options.

> [!NOTE]
> Secure Storage
> 
> The use of TLS, its associated keys and certificates requires using secure storage to minimize the chances of a security breach. The implementation of this storage differs from platform to platform — see [Using secure storage](p2psync-websocket.md#using-secure-storage).

## [](#configuration-summary)Configuration Summary

You should configure and initialize the Listener with a list of collections to sync. There is no limit on the number of Listeners you may configure — [Example 1](#simple-listener-initialization) shows a simple initialization and configuration process.

> [!TIP]
> You must include the initializer `CouchbaseLite.init(context)` such that it is executed (once only) before initializing the replicator; for example, in your app’s `onCreate()` method.

Example 1\. Listener configuration and initialization

```Java
// Initialize the listener config
final URLEndpointListenerConfiguration thisConfig
    = new URLEndpointListenerConfiguration(collections); (1)

thisConfig.setPort(55990); (2)

thisConfig.setNetworkInterface("wlan0"); (3)

thisConfig.setEnableDeltaSync(false); (4)

// Configure server security
thisConfig.setDisableTls(false); (5)

// Use an Anonymous Self-Signed Cert
thisConfig.setTlsIdentity(null); (6)


// Configure Client Security using an Authenticator
// For example, Basic Authentication (7)
thisConfig.setAuthenticator(new ListenerPasswordAuthenticator(
    (username, password) ->
        username.equals(validUser) && Arrays.equals(password, validPass)));

// Initialize the listener
final URLEndpointListener thisListener
    = new URLEndpointListener(thisConfig); (8)

// Start the listener
thisListener.start(); (9)
```

| **1** | Identify the local database and the collections to be used — see: [Initialize the Listener Configuration](#initialize-the-listener-configuration)                                                                                                                                                                                                                                                           |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Optionally, choose a port to use. By default the system will automatically assign a port — to over-ride this, see: [Set Port and Network Interface](#lbl-set-network-and-port)                                                                                                                                                                                                                              |
| **3** | Optionally, choose a network interface to use. By default the system will listen on all network interfaces — to over-ride this see: [Set Port and Network Interface](#lbl-set-network-and-port)                                                                                                                                                                                                             |
| **4** | Optionally, choose to sync only changes. The default is not to enable delta-sync — see: [Delta Sync](#delta-sync).                                                                                                                                                                                                                                                                                          |
| **5** | Set server security. TLS is always enabled instantly, so you can usually omit this line. But you _can_, optionally, disable TLS (**not** advisable in production) — see: [TLS Security](#lbl-tls-security)                                                                                                                                                                                                  |
| **6** | Set the credentials this server will present to the client for authentication. Here we show the default TLS authentication, which is an anonymous self-signed certificate. The server must always authenticate itself to the client.                                                                                                                                                                        |
| **7** | Set client security — define the credentials the server expects the client to present for authentication. Here we show how basic authentication is configured to authenticate the client-supplied credentials from the http authentication header against valid credentials — see [Authenticating the Client](#lbl-authenticating-the-client) for more options.Note that client authentication is optional. |
| **8** | Initialize the listener using the configuration settings.                                                                                                                                                                                                                                                                                                                                                   |
| **9** | [Start Listener](#lbl-start-listener)                                                                                                                                                                                                                                                                                                                                                                       |

## [](#api-references)API References

You can find [Java API References](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/) here.

## [](#device-discovery)Device Discovery

**This phase is optional:** If the Listener is initialized on a well-known URL endpoint (for example, a static IP Address or well-known DNS address) then you can configure Active Peers to connect to those.

Before initiating the Listener, you may execute a peer discovery phase. For the Passive Peer, this involves advertising the service using, for example, and waiting for an invite from the Active Peer. The connection is established once the Passive Peer has authenticated and accepted an Active Peer’s invitation.

## [](#initialize-the-listener-configuration)Initialize the Listener Configuration

Initialize the Listener configuration with a list of collections from the local database — see [Example 2](#ex-locdb). All other configuration values take their default setting.

Example 2\. Specify Local Collections

```Java
// Initialize the listener config
final URLEndpointListenerConfiguration thisConfig
    = new URLEndpointListenerConfiguration(collections); (1)
```

| **1** | Set the list of local collections using the [URLEndpointListenerConfiguration](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/URLEndpointListenerConfiguration.html). |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#lbl-set-network-and-port)Set Port and Network Interface

### [](#port-number)Port number

The Listener will automatically select an available port if you do not specify one — see [Example 3](#ex-port) for how to specify a port.

Example 3\. Specify a port

```Java
thisConfig.setPort(55990); (1)
```

| **1** | To use a canonical port — one known to other applications — specify it explicitly using the [setPort](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/URLEndpointListenerConfiguration.html#setPort-int-) method shown here.Ensure that firewall rules do not block any port you do specify. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#network-interface)Network Interface

The Listener will listen on all network interfaces by default.

Example 4\. Specify a Network Interface to Use

```Java
thisConfig.setNetworkInterface("wlan0"); (1)
```

| **1** | To specify an interface — one known to other applications — identify it explicitly, using the [setNetworkInterface](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/URLEndpointListenerConfiguration.html#setNetworkInterface-java.lang.String-) method shown here. This must be either an IP Address or network interface name such as en0. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#delta-sync)Delta Sync

Delta Sync allows clients to sync only those parts of a document that have changed. This can result in significant bandwidth consumption savings and throughput improvements. Both are valuable benefits, especially when network bandwidth is constrained.

Example 5\. Enable delta sync

```Java
thisConfig.setEnableDeltaSync(false); (1)
```

| **1** | Delta sync replication is not enabled by default. Use [URLEndpointListenerConfiguration](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/URLEndpointListenerConfiguration.html)'s [setEnableDeltaSync](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/URLEndpointListenerConfiguration.html#setEnableDeltaSync-boolean-) method to activate or deactivate it. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#lbl-tls-security)TLS Security

### [](#enable-or-disable-tls)Enable or Disable TLS

Define whether the connection is to use TLS or clear text.

TLS-based encryption is enabled by default, and this setting ought to be used in any production environment. However, it _can_ be disabled. For example, for development or test environments.

When TLS is enabled, Couchbase Lite provides several options on how the Listener may be configured with an appropriate TLS Identity — see [Configure TLS Identity for Listener](#configure-tls-identity-for-listener).

You can use [URLEndpointListenerConfiguration](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/URLEndpointListenerConfiguration.html)'s [setDisableTLS](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/URLEndpointListenerConfiguration.html#setDisableTls-boolean-) method to disable TLS communication if necessary

The `disableTLS` setting must be 'false' when _Client Cert Authentication_ is required.

Basic Authentication can be used with, or without, TLS.

[setDisableTLS](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/URLEndpointListenerConfiguration.html#setDisableTls-boolean-) works in conjunction with `TLSIdentity`, to enable developers to define the key and certificate to be used.

* If `disableTLS` is true — TLS communication is disabled and TLS identity is ignored. Active peers will use the `ws://` URL scheme used to connect to the listener.
* If `disableTLS` is false or not specified — TLS communication is enabled.  
Active peers will use the `wss://` URL scheme to connect to the listener.

### [](#configure-tls-identity-for-listener)Configure TLS Identity for Listener

Define the credentials the server will present to the client for authentication. Note that the server must always authenticate itself with the client — see: [Authenticate Listener on Active Peer](p2psync-websocket-using-active.md#authenticate-listener) for how the client deals with this.

Use [URLEndpointListenerConfiguration](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/URLEndpointListenerConfiguration.html)'s [setTlsIdentity](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/URLEndpointListenerConfiguration.html#setTlsIdentity-com.couchbase.lite.TLSIdentity-) method to configure the TLS Identity used in TLS communication.

If `TLSIdentity` is not set, then the listener uses an auto-generated anonymous self-signed identity (unless `disableTLS = true`). Whilst the client cannot use this to authenticate the server, it will use it to encrypt communication, giving a more secure option than non-TLS communication.

The auto-generated anonymous self-signed identity is saved in secure storage for future use to obviate the need to re-generate it.

> [!NOTE]
> Typically, you will configure the Listener’s TLS Identity once during the initial launch and re-use it (from secure storage) on any subsequent starts.

Here are some example code snippets showing:

* Importing a TLS identity — see: [Example 6](#ex-import-tls-id)
* Setting TLS identity to expect self-signed certificate — — see: [Example 7](#ex-create-tls-id)
* Setting TLS identity to expect anonymous certificate — see: [Example 8](#ex-anon-tls-id)

Example 6\. Import Listener’s TLS identity

Import an identity from a secure key and certificate data source.

```Java

// Import a key pair from a file into a keystore
// Create a TLSIdentity from the imported key-pair
// This only needs to happen once.  Once the key is in the internal store
// it can be referenced using its alias
KeyStore keyStore = KeyStore.getInstance("PKCS12");
try (InputStream keyStream = Files.newInputStream(keyFile.toPath())) { (1)
    keyStore.load(keyStream, "skerit".toCharArray());
}

// Set the TLS Identity
URLEndpointListenerConfiguration config = new URLEndpointListenerConfiguration(collections);
config.setTlsIdentity(TLSIdentity.getIdentity(keyStore, "test-alias", "keyPass".toCharArray())); (2)
thisConfig.setDisableTls(false); (3)
```

| **1** | Ensure TLS is used                                                        |
| ----- | ------------------------------------------------------------------------- |
| **2** | Get key and certificate data                                              |
| **3** | Use the retrieved data to create and store the TLS identity               |
| **4** | Set this identity as the one presented in response to the client’s prompt |

Example 7\. Create Self-Signed Cert

Create a TLSIdentity for the server using convenience API. The system generates a self-signed certificate.

```Java
thisConfig.setDisableTls(false); (1)
```

| **1** | Ensure TLS is used.                                                                                    |
| ----- | ------------------------------------------------------------------------------------------------------ |
| **2** | Map the required certificate attributes, in this case the common name.                                 |
| **3** | Create the required TLS identity using the attributes. Add to secure storage as 'couchbase-docs-cert'. |
| **4** | Configure the server to present the defined identity credentials when prompted.                        |

Example 8\. Use Anonymous Self-Signed Certificate

This example uses an _anonymous_ self signed certificate. Generated certificates are held in secure storage.

```Java
thisConfig.setDisableTls(false); (1)

// Use an Anonymous Self-Signed Cert
thisConfig.setTlsIdentity(null); (2)
```

| **1** | Ensure TLS is used.This is the default setting.                                      |
| ----- | ------------------------------------------------------------------------------------ |
| **2** | Authenticate using an anonymous self-signed certificate.This is the default setting. |

## [](#lbl-authenticating-the-client)Authenticating the Client

In this section: [Use Basic Authentication](#use-basic-authentication) | [Using Client Certificate Authentication](#using-client-certificate-authentication) | [Delete Entry](#delete-tls-identity) | [The Impact of TLS Settings](#the-impact-of-tls-settings)

Define how the server (Listener) will authenticate the client as one it is prepared to interact with.

Whilst client authentication is optional, Couchbase lite provides the necessary tools to implement it. Use the [URLEndpointListenerConfiguration](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/URLEndpointListenerConfiguration.html) class’s [setAuthenticator](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/URLEndpointListenerConfiguration.html#setAuthenticator-com.couchbase.lite.ListenerAuthenticator-) method to specify how the client-supplied credentials are to be authenticated.

Valid options are:

* No authentication — If you do not define an Authenticator then all clients are accepted.
* Basic Authentication — uses the [ListenerPasswordAuthenticator](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/ListenerPasswordAuthenticator.html) to authenticate the client using the client-supplied username and password (from the http authentication header).
* [ListenerCertificateAuthenticator](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/ListenerCertificateAuthenticator.html) — which authenticates the client using a client supplied chain of one or more certificates. You should initialize the authenticator using one of the following constructors:

  * A root certificate, or a list of intermediate certificates and a root certificate — the client supplied certificate must end at a certificate in this list if it is to be authenticated.
  * A block of code that assumes total responsibility for authentication — it must return a boolean response (true for an authenticated client, or false for a failed authentication).

### [](#use-basic-authentication)Use Basic Authentication

Define how to authenticate client-supplied username and password credentials. To use client-supplied certificates instead — see: [Using Client Certificate Authentication](#using-client-certificate-authentication)

Example 9\. Password authentication

```Java
// Configure Client Security using an Authenticator
// For example, Basic Authentication (1)
thisConfig.setAuthenticator(new ListenerPasswordAuthenticator(
    (username, password) ->
        username.equals(validUser) && Arrays.equals(password, validPass)));
```

| **1** | Where 'username'/'password' are the client-supplied values (from the http-authentication header) and validUser/validPassword are the values acceptable to the server. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#using-client-certificate-authentication)Using Client Certificate Authentication

Define how the server will authenticate client-supplied certificates.

There are two ways to authenticate a client:

* A chain of one or more certificates that ends at a certificate in the list of certificates supplied to the constructor for [ListenerCertificateAuthenticator](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/ListenerCertificateAuthenticator.html) — see: [Example 10](#ex-set-cert-auth)
* Application logic: This method assumes complete responsibility for verifying and authenticating the client — see: [Example 11](#ex-use-app-logic)  
If the parameter supplied to the constructor for `ListenerCertificateAuthenticator` is of type `ListenerCertificateAuthenticatorDelegate`, all other forms of authentication are bypassed.  
The client response to the certificate request is passed to the method supplied as the constructor parameter. The logic should take the form of function or block (such as, a closure expression) where the platform allows.

Example 10\. Set Certificate Authorization

Configure the server (listener) to authenticate the client against a list of one or more certificates provided by the server to the the [ListenerCertificateAuthenticator](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/ListenerCertificateAuthenticator.html).

```Java
// Configure the client authenticator
// to validate using ROOT CA
// thisClientID.certs is a list containing a client cert to accept
// and any other certs needed to complete a chain between the client cert
// and a CA
final TLSIdentity validId =
    TLSIdentity.getIdentity(keyStore, "OurCorp", "sekrit".toCharArray());  // get the identity (1)
if (validId == null) { throw new IllegalStateException("Cannot find corporate id"); }

thisConfig.setTlsIdentity(validId);

thisConfig.setAuthenticator(
    new ListenerCertificateAuthenticator(validId.getCerts())); (2) (3)
// accept only clients signed by the corp cert

final URLEndpointListener thisListener =
    new URLEndpointListener(thisConfig);
```

| **1** | Get the identity data to authenticate against. This can be, for example, from a resource file provided with the app, or an identity previously saved in secure storage.                            |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Configure the authenticator to authenticate the client supplied certificate(s) using these root certs. A valid client will provide one or more certificates that match a certificate in this list. |
| **3** | Add the authenticator to the Listener configuration.                                                                                                                                               |

Example 11\. Application Logic

Configure the server (listener) to authenticate the client using user-supplied logic.

```Java
// Configure authentication using application logic
final TLSIdentity thisCorpId = TLSIdentity.getIdentity(keyStore, "OurCorp", "sekrit".toCharArray()); (1)
if (thisCorpId == null) {
    throw new IllegalStateException("Cannot find corporate id");
}
thisConfig.setTlsIdentity(thisCorpId);
thisConfig.setAuthenticator(
    new ListenerCertificateAuthenticator(
        (certs) -> {
            // supply logic that returs boolean
            // true for authenticate, false if not
            // For instance:
            return certs.get(0).equals(thisCorpId.getCerts().get(0));
        }
    )); (2) (3)

thisListener = new URLEndpointListener(thisConfig);
```

| **1** | Get the identity data to authenticate against. This can be, for example, from a resource file provided with the app, or an identity previously saved in secure storage.                                                                                                                 |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Configure the Authenticator to pass the root certificates to a user supplied code block. This code assumes complete responsibility for authenticating the client supplied certificate(s). It must return a boolean value; with true denoting the client supplied certificate authentic. |
| **3** | Add the authenticator to the Listener configuration.                                                                                                                                                                                                                                    |

### [](#delete-tls-identity)Delete Entry

You can remove unwanted TLS identities from secure storage using the convenience API.

Example 12\. Deleting TLS Identities

```Java
KeyStore thisKeyStore = KeyStore.getInstance("AndroidKeyStore");
thisKeyStore.load(null);
thisKeyStore.deleteEntry(alias);
```

### [](#the-impact-of-tls-settings)The Impact of TLS Settings

The table in this section shows the expected system behavior (in regards to security) depending on the TLS configuration settings deployed.

__Table 1\. Expected system behavior__
| disableTLS | tlsIdentity (corresponding to server)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Expected system behavior                                                                                                                                                                                                     |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| true       | Ignored                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | TLS is disabled; all communication is plain text.                                                                                                                                                                            |
| false      | set to nil                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | The system will auto generate an _anonymous_ self signed cert. Active Peers (clients) should be configured to accept self-signed certificates. Communication is encrypted                                                    |
| false      | Set to server identity generated from a self- or CA-signed certificate On first use — Bring your own certificate and private key; for example, using the [TLSIdentity](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/TLSIdentity.html) class’s [createIdentity()](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/TLSIdentity.html#createIdentity-boolean-java.util.Map-java.util.Date-java.lang.String-) method to add it to the secure storage. Each time — Use the server identity from the certificate stored in the secure storage; for example, using the [TLSIdentity](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/TLSIdentity.html) class’s [getIdentity()](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/TLSIdentity.html#getIdentity-java.lang.String-) method with the alias you want to retrieve.. | System will use the configured identity. Active Peers will validate the server certificate corresponding to the TLSIdentity (as long as they are configured to not skip validation — see [TLS Security](#lbl-tls-security)). |

## [](#lbl-start-listener)Start Listener

Once you have completed the Listener’s configuration settings you can initialize the Listener instance and start it running — see: [Example 13](#initialize-and-start-listener)

Example 13\. Initialize and start listener

```Java
// Initialize the listener
final URLEndpointListener thisListener
    = new URLEndpointListener(thisConfig); (1)

// Start the listener
thisListener.start(); (2)
```

## [](#monitor-listener)Monitor Listener

Use the Listener’s `[getStatus](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/URLEndpointListener.html#getStatus--)` property/method to get counts of total and active connections — see: [Example 14](#get-connection-counts).

You should note that these counts can be extremely volatile. So, the actual number of active connections may have changed, by the time the `[ConnectionStatus](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/com/couchbase/lite/ConnectionStatus.html)` class returns a result.

Example 14\. Get connection counts

```Java
int connectionCount =
    thisListener.getStatus().getConnectionCount(); (1)

int activeConnectionCount =
    thisListener.getStatus().getActiveConnectionCount();  (2)
```

## [](#stop-listener)Stop Listener

It is best practice to check the status of the Listener’s connections and stop only when you have confirmed that there are no active connections — see [Example 14](#get-connection-counts).

Example 15\. Stop listener using `stop` method

```Java
thisListener.stop();
```

> [!NOTE]
> Closing the database will also close the Listener.

## [](#related-content)Related Content

### [](#)

How to

* [Passive Peer](p2psync-websocket-using-passive.md)
* [Active Peer](p2psync-websocket-using-active.md)

.

### [](#-2)

Concepts

* [Peer-to-Peer Sync](#java:landing-p2psync.adoc)
* [API References](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-java/)

.

### [](#-3)

Community Resources …​

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

. [Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)