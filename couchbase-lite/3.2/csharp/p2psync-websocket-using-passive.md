---
title: Passive Peer
description: Couchbase Lite's Peer-to-Peer Synchronization enables edge devices
  to synchronize securely without consuming centralized cloud-server resources
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.2/modules/csharp/pages/p2psync-websocket-using-passive.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/couchbase-lite/3.2/csharp/p2psync-websocket-using-passive.html)

# Passive Peer

> Description — _Couchbase Lite’s Peer-to-Peer Synchronization enables edge devices to synchronize securely without consuming centralized cloud-server resources_  
> _Abstract — How to set up a Listener to accept a Replicator connection and sync using peer-to-peer_  
> Related Content — [API Reference](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net) | [Passive Peer](p2psync-websocket-using-passive.md) | [Active Peer](p2psync-websocket-using-active.md)

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

Example 1\. Listener configuration and initialization

```C#
            // Initialize the listener config
            var endpointConfig = new URLEndpointListenerConfiguration(new[] { collection }); (1)

            endpointConfig.Port = 55990; (2)

            endpointConfig.NetworkInterface = "10.1.1.10"; (3)

            endpointConfig.EnableDeltaSync = true; (4)

#warning listener-config-tls-full unused?
            endpointConfig.DisableTLS = false; (5)

            // Use an Anonymous Self-Signed Cert
            endpointConfig.TlsIdentity = null; (6)

            // Configure the client authenticator
            // Here we are using Basic Authentication) (7)
            SecureString validPassword = new SecureString(); /* example only */
            // Get SecureString input for validPassword
            var validUser = "valid.username";
            endpointConfig.Authenticator = new ListenerPasswordAuthenticator(
            (sender, username, password) =>
            {
                // Implement your own ValidatePassword function
                return username == validUser && ValidatePassword(password);
            }
            );

            // Initialize the listener
            var listener = new URLEndpointListener(endpointConfig); (8)

            // Start the listener
            listener.Start(); (9)
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

You can find [C#.Net API References](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net) here.

## [](#device-discovery)Device Discovery

**This phase is optional:** If the Listener is initialized on a well-known URL endpoint (for example, a static IP Address or well-known DNS address) then you can configure Active Peers to connect to those.

Before initiating the Listener, you may execute a peer discovery phase. For the Passive Peer, this involves advertising the service using, for example, and waiting for an invite from the Active Peer. The connection is established once the Passive Peer has authenticated and accepted an Active Peer’s invitation.

## [](#initialize-the-listener-configuration)Initialize the Listener Configuration

Initialize the Listener configuration with a list of collections from the local database — see [Example 2](#ex-locdb). All other configuration values take their default setting.

Example 2\. Specify Local Collections

```C#
// Initialize the listener config
var endpointConfig = new URLEndpointListenerConfiguration(new[] { collection }); (1)
```

| **1** | Set the list of local collections using the [URLEndpointListenerConfiguration](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.URLEndpointListenerConfiguration.html). |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#lbl-set-network-and-port)Set Port and Network Interface

### [](#port-number)Port number

The Listener will automatically select an available port if you do not specify one — see [Example 3](#ex-port) for how to specify a port.

Example 3\. Specify a port

```C#
endpointConfig.Port = 55990; (1)
```

| **1** | To use a canonical port — one known to other applications — specify it explicitly using the [Port](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.URLEndpointListenerConfiguration.html#Couchbase%5FLite%5FP2P%5FURLEndpointListenerConfiguration%5FPort) method shown here.Ensure that firewall rules do not block any port you do specify. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#network-interface)Network Interface

The Listener will listen on all network interfaces by default.

Example 4\. Specify a Network Interface to Use

```C#
endpointConfig.NetworkInterface = "10.1.1.10"; (1)
```

| **1** | To specify an interface — one known to other applications — identify it explicitly, using the [NetworkInterface](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.URLEndpointListenerConfiguration.html#Couchbase%5FLite%5FP2P%5FURLEndpointListenerConfiguration%5FNetworkInterface) method shown here. This must be either an IP Address or network interface name such as en0. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

> [!TIP]
> Where necessary, you can identify the available interfaces at runtime, using appropriate platform tools — see [Example 5](#get-network-interfaces).

Example 5\. Identify available network interfaces

```C#
foreach (NetworkInterface ni in NetworkInterface.GetAllNetworkInterfaces()) {
    if (ni.NetworkInterfaceType == NetworkInterfaceType.Wireless80211 ||
        ni.NetworkInterfaceType == NetworkInterfaceType.Ethernet) {
        // do something with the interface(s)
    }
}
```

## [](#delta-sync)Delta Sync

Delta Sync allows clients to sync only those parts of a document that have changed. This can result in significant bandwidth consumption savings and throughput improvements. Both are valuable benefits, especially when network bandwidth is constrained.

Example 6\. Enable delta sync

```C#
endpointConfig.EnableDeltaSync = true; (1)
```

| **1** | Delta sync replication is not enabled by default. Use [URLEndpointListenerConfiguration](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.URLEndpointListenerConfiguration.html)'s [EnableDeltaSync](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.URLEndpointListenerConfiguration.html#Couchbase%5FLite%5FP2P%5FURLEndpointListenerConfiguration%5FEnableDeltaSync) method to activate or deactivate it. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#lbl-tls-security)TLS Security

### [](#enable-or-disable-tls)Enable or Disable TLS

Define whether the connection is to use TLS or clear text.

TLS-based encryption is enabled by default, and this setting ought to be used in any production environment. However, it _can_ be disabled. For example, for development or test environments.

When TLS is enabled, Couchbase Lite provides several options on how the Listener may be configured with an appropriate TLS Identity — see [Configure TLS Identity for Listener](#configure-tls-identity-for-listener).

You can use [URLEndpointListenerConfiguration](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.URLEndpointListenerConfiguration.html)'s [DisableTLS](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.URLEndpointListenerConfiguration.html#Couchbase%5FLite%5FP2P%5FURLEndpointListenerConfiguration%5FDisableTLS) method to disable TLS communication if necessary

The `disableTLS` setting must be 'false' when _Client Cert Authentication_ is required.

Basic Authentication can be used with, or without, TLS.

[DisableTLS](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.URLEndpointListenerConfiguration.html#Couchbase%5FLite%5FP2P%5FURLEndpointListenerConfiguration%5FDisableTLS) works in conjunction with `TLSIdentity`, to enable developers to define the key and certificate to be used.

* If `disableTLS` is true — TLS communication is disabled and TLS identity is ignored. Active peers will use the `ws://` URL scheme used to connect to the listener.
* If `disableTLS` is false or not specified — TLS communication is enabled.  
Active peers will use the `wss://` URL scheme to connect to the listener.

### [](#configure-tls-identity-for-listener)Configure TLS Identity for Listener

Define the credentials the server will present to the client for authentication. Note that the server must always authenticate itself with the client — see: [Authenticate Listener on Active Peer](p2psync-websocket-using-active.md#authenticate-listener) for how the client deals with this.

Use [URLEndpointListenerConfiguration](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.URLEndpointListenerConfiguration.html)'s [TlsIdentity](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.URLEndpointListenerConfiguration.html#Couchbase%5FLite%5FP2P%5FURLEndpointListenerConfiguration%5FTlsIdentity) method to configure the TLS Identity used in TLS communication.

If `TLSIdentity` is not set, then the listener uses an auto-generated anonymous self-signed identity (unless `disableTLS = true`). Whilst the client cannot use this to authenticate the server, it will use it to encrypt communication, giving a more secure option than non-TLS communication.

The auto-generated anonymous self-signed identity is saved in secure storage for future use to obviate the need to re-generate it.

> [!NOTE]
> Typically, you will configure the Listener’s TLS Identity once during the initial launch and re-use it (from secure storage) on any subsequent starts.

Here are some example code snippets showing:

* Importing a TLS identity — see: [Example 7](#ex-import-tls-id)
* Setting TLS identity to expect self-signed certificate — — see: [Example 8](#ex-create-tls-id)
* Setting TLS identity to expect anonymous certificate — see: [Example 9](#ex-anon-tls-id)

Example 7\. Import Listener’s TLS identity

Import an identity from a secure key and certificate data source.

```C#
            endpointConfig.DisableTLS = false; (1)
                // Use CA Cert
                // Create a TLSIdentity from an imported key-pair
                // . . . previously declared variables include ...
                X509Store store =
                  new X509Store(StoreName.My); // create and label x509 store

                // Get keys and certificates from PKCS12 data
                byte[] certData =
                  File.ReadAllBytes("c:client.p12"); (2)
                                                     // . . . other user code . . .

#warning import-tls-identity unused?
                TLSIdentity identity = TLSIdentity.ImportIdentity(
                  store,
                  certData, (3)
                  "123", // Password to access certificate data
                  "couchbase-demo-cert",
                  null); // Label to get cert in certificate map
                         // NOTE: If a null label is supplied then the same
                         // default directory for a Couchbase Lite database
                         // is used for map.


#warning listener-config-tls-id-set unused?
                // Set the TLS Identity
                endpointConfig.TlsIdentity = identity; (4)
```

| **1** | Ensure TLS is used                                                        |
| ----- | ------------------------------------------------------------------------- |
| **2** | Get key and certificate data                                              |
| **3** | Use the retrieved data to create and store the TLS identity               |
| **4** | Set this identity as the one presented in response to the client’s prompt |

Example 8\. Create Self-Signed Cert

Create a TLSIdentity for the server using convenience API. The system generates a self-signed certificate.

```C#
            endpointConfig.DisableTLS = false; (1)


#warning listener-config-tls-id-set unused?
                // Set the TLS Identity
                endpointConfig.TlsIdentity = identity; (2)
```

| **1** | Ensure TLS is used.                                                                                    |
| ----- | ------------------------------------------------------------------------------------------------------ |
| **2** | Map the required certificate attributes, in this case the common name.                                 |
| **3** | Create the required TLS identity using the attributes. Add to secure storage as 'couchbase-docs-cert'. |
| **4** | Configure the server to present the defined identity credentials when prompted.                        |

Example 9\. Use Anonymous Self-Signed Certificate

This example uses an _anonymous_ self signed certificate. Generated certificates are held in secure storage.

```C#
endpointConfig.DisableTLS = false; (1)
// Use an Anonymous Self-Signed Cert
endpointConfig.TlsIdentity = null; (2)
    // Use an Anonymous Self-Signed Cert
    endpointConfig.TlsIdentity = null; (3)
```

| **1** | Ensure TLS is used.This is the default setting.                                      |
| ----- | ------------------------------------------------------------------------------------ |
| **2** | Authenticate using an anonymous self-signed certificate.This is the default setting. |

## [](#lbl-authenticating-the-client)Authenticating the Client

In this section: [Use Basic Authentication](#use-basic-authentication) | [Using Client Certificate Authentication](#using-client-certificate-authentication) | [Delete Entry](#delete-tls-identity) | [The Impact of TLS Settings](#the-impact-of-tls-settings)

Define how the server (Listener) will authenticate the client as one it is prepared to interact with.

Whilst client authentication is optional, Couchbase lite provides the necessary tools to implement it. Use the [URLEndpointListenerConfiguration](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.URLEndpointListenerConfiguration.html) class’s [Authenticator](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.URLEndpointListenerConfiguration.html#Couchbase%5FLite%5FP2P%5FURLEndpointListenerConfiguration%5FAuthenticator) method to specify how the client-supplied credentials are to be authenticated.

Valid options are:

* No authentication — If you do not define an Authenticator then all clients are accepted.
* Basic Authentication — uses the [ListenerPasswordAuthenticator](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.ListenerPasswordAuthenticator.html) to authenticate the client using the client-supplied username and password (from the http authentication header).
* [ListenerCertificateAuthenticator](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.ListenerCertificateAuthenticator.html) — which authenticates the client using a client supplied chain of one or more certificates. You should initialize the authenticator using one of the following constructors:

  * A root certificate, or a list of intermediate certificates and a root certificate — the client supplied certificate must end at a certificate in this list if it is to be authenticated.
  * A block of code that assumes total responsibility for authentication — it must return a boolean response (true for an authenticated client, or false for a failed authentication).

### [](#use-basic-authentication)Use Basic Authentication

Define how to authenticate client-supplied username and password credentials. To use client-supplied certificates instead — see: [Using Client Certificate Authentication](#using-client-certificate-authentication)

Example 10\. Password authentication

```C#
// Configure the client authenticator
// Here we are using Basic Authentication) (1)
SecureString validPassword = new SecureString(); /* example only */
// Get SecureString input for validPassword
var validUser = "valid.username";
endpointConfig.Authenticator = new ListenerPasswordAuthenticator(
(sender, username, password) =>
{
    // Implement your own ValidatePassword function
    return username == validUser && ValidatePassword(password);
}
);
```

| **1** | Where 'username'/'password' are the client-supplied values (from the http-authentication header) and validUser/validPassword are the values acceptable to the server. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#using-client-certificate-authentication)Using Client Certificate Authentication

Define how the server will authenticate client-supplied certificates.

There are two ways to authenticate a client:

* A chain of one or more certificates that ends at a certificate in the list of certificates supplied to the constructor for [ListenerCertificateAuthenticator](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.ListenerCertificateAuthenticator.html) — see: [Example 11](#ex-set-cert-auth)
* Application logic: This method assumes complete responsibility for verifying and authenticating the client — see: [Example 12](#ex-use-app-logic)  
If the parameter supplied to the constructor for `ListenerCertificateAuthenticator` is of type `ListenerCertificateAuthenticatorDelegate`, all other forms of authentication are bypassed.  
The client response to the certificate request is passed to the method supplied as the constructor parameter. The logic should take the form of function or block (such as, a closure expression) where the platform allows.

Example 11\. Set Certificate Authorization

Configure the server (listener) to authenticate the client against a list of one or more certificates provided by the server to the the [ListenerCertificateAuthenticator](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.ListenerCertificateAuthenticator.html).

```C#
// Configure the client authenticator
// to validate using ROOT CA

// Get the valid cert chain, in this instance from
// PKCS12 data containing private key, public key
// and certificates (1)
var clientData = File.ReadAllBytes("c:client.p12");
var ourCaData = File.ReadAllBytes("c:client-ca.der");

// Get the root certs from the data
var rootCert = new X509Certificate2(ourCaData); (2)

// Configure the authenticator to use the root certs
var certAuth = new ListenerCertificateAuthenticator(new X509Certificate2Collection(rootCert));

endpointConfig.Authenticator = certAuth; (3)

// Initialize the listener using the config
var listener = new URLEndpointListener(endpointConfig);
```

| **1** | Get the identity data to authenticate against. This can be, for example, from a resource file provided with the app, or an identity previously saved in secure storage.                            |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Configure the authenticator to authenticate the client supplied certificate(s) using these root certs. A valid client will provide one or more certificates that match a certificate in this list. |
| **3** | Add the authenticator to the Listener configuration.                                                                                                                                               |

Example 12\. Application Logic

Configure the server (listener) to authenticate the client using user-supplied logic.

```C#
// Configure the client authenticator
// to validate using application logic

// Get the valid cert chain, in this instance from
// PKCS12 data containing private key, public key
// and certificates (1)
clientData = File.ReadAllBytes("c:client.p12");
ourCaData = File.ReadAllBytes("c:client-ca.der");

// Configure the authenticator to pass the root certs
// To a user supplied code block for authentication
var callbackAuth =
  new ListenerCertificateAuthenticator(
    (object sender, X509Certificate2Collection chain) =>
    {
        // . . . user supplied code block
        // . . . returns boolean value (true=authenticated)
        return true;
    }); (2)

endpointConfig.Authenticator = callbackAuth; (3)
```

| **1** | Get the identity data to authenticate against. This can be, for example, from a resource file provided with the app, or an identity previously saved in secure storage.                                                                                                                 |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Configure the Authenticator to pass the root certificates to a user supplied code block. This code assumes complete responsibility for authenticating the client supplied certificate(s). It must return a boolean value; with true denoting the client supplied certificate authentic. |
| **3** | Add the authenticator to the Listener configuration.                                                                                                                                                                                                                                    |

### [](#delete-tls-identity)Delete Entry

You can remove unwanted TLS identities from secure storage using the convenience API.

Example 13\. Deleting TLS Identities

```C#

```

### [](#the-impact-of-tls-settings)The Impact of TLS Settings

The table in this section shows the expected system behavior (in regards to security) depending on the TLS configuration settings deployed.

__Table 1\. Expected system behavior__
| disableTLS | tlsIdentity (corresponding to server)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Expected system behavior                                                                                                                                                                                                     |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| true       | Ignored                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | TLS is disabled; all communication is plain text.                                                                                                                                                                            |
| false      | set to null                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | The system will auto generate an _anonymous_ self signed cert. Active Peers (clients) should be configured to accept self-signed certificates. Communication is encrypted                                                    |
| false      | Set to server identity generated from a self- or CA-signed certificate On first use — Bring your own certificate and private key; for example, using the [TLSIdentity](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.TLSIdentity.html) class’s <https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.TLSIdentity.html#Couchbase%5FLite%5FP2P%5FTLSIdentity%5FCreateIdentity%5FSystem%5FBoolean%5FSystem%5FCollections%5FGeneric%5FDictionary%5FSystem%5FString%5FSystem%5FString>_System\_Nullable\_System\_DateTimeOffset_System\_Security\_Cryptography\_X509Certificates\_X509Store\_System\_String\_System\_String\_\[CreateIdentity()\] method to add it to the secure storage. Each time — Use the server identity from the certificate stored in the secure storage; for example, using the [TLSIdentity](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.TLSIdentity.html) class’s [GetIdentity(X509Store, String, String)](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.TLSIdentity.html#Couchbase%5FLite%5FP2P%5FTLSIdentity%5FGetIdentity%5FSystem%5FSecurity%5FCryptography%5FX509Certificates%5FX509Store%5FSystem%5FString%5FSystem%5FString%5F) method with the alias you want to retrieve.. | System will use the configured identity. Active Peers will validate the server certificate corresponding to the TLSIdentity (as long as they are configured to not skip validation — see [TLS Security](#lbl-tls-security)). |

## [](#lbl-start-listener)Start Listener

Once you have completed the Listener’s configuration settings you can initialize the Listener instance and start it running — see: [Example 14](#initialize-and-start-listener)

Example 14\. Initialize and start listener

```C#
// Initialize the listener
var listener = new URLEndpointListener(endpointConfig); (1)

// Start the listener
listener.Start(); (2)
```

## [](#monitor-listener)Monitor Listener

Use the Listener’s `[Status](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.URLEndpointListener.html#Couchbase%5FLite%5FP2P%5FURLEndpointListener%5FStatus)` property/method to get counts of total and active connections — see: [Example 15](#get-connection-counts).

You should note that these counts can be extremely volatile. So, the actual number of active connections may have changed, by the time the `[ConnectionStatus](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.P2P.ConnectionStatus.html)` class returns a result.

Example 15\. Get connection counts

```C#
ulong connectionCount = listener.Status.ConnectionCount; (1)
ulong activeConnectionCount = listener.Status.ActiveConnectionCount;  (2)
```

## [](#stop-listener)Stop Listener

It is best practice to check the status of the Listener’s connections and stop only when you have confirmed that there are no active connections — see [Example 15](#get-connection-counts).

Example 16\. Stop listener using `stop` method

```C#
listener.Stop();
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

* [Peer-to-Peer Sync](#csharp:landing-p2psync.adoc)
* [API References](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net)

.

### [](#-3)

Community Resources …​

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

. [Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)