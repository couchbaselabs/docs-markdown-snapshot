---
title: Passive Peer
description: Couchbase Lite's Peer-to-Peer Synchronization enables edge devices
  to synchronize securely without consuming centralized cloud-server resources
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/c/pages/p2psync-websocket-using-passive.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:4.0@couchbase-lite:c:p2psync-websocket-using-passive.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/4.0/c/p2psync-websocket-using-passive.html)

# Passive Peer

> Description — _Couchbase Lite's Peer-to-Peer Synchronization enables edge devices to synchronize securely without consuming centralized cloud-server resources_  
> _Abstract — How to set up a Listener to accept a Replicator connection and sync using peer-to-peer_  
> Related Content — [API Reference](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html) | [Passive Peer](p2psync-websocket-using-passive.md) | [Active Peer](p2psync-websocket-using-active.md)

> [!NOTE]
> Code Snippets
> 
> All code examples are indicative only. They demonstrate the basic concepts and approaches to using a feature. Use them as inspiration and adapt these examples to best practice when developing applications for your platform.

## [](#introduction)Introduction

This content provides code and configuration examples covering the implementation of [Peer-to-Peer Sync](refer-glossary.md#peer-to-peer-sync) over WebSockets. Specifically, it covers the implementation of a [Passive Peer](refer-glossary.md#passive-peer).

Couchbase's Passive Peer (also referred to as the server, or Listener) will accept a connection from an [Active Peer](refer-glossary.md#active-peer) (also referred to as the client or replicator) and replicate database changes to synchronize both databases.

Subsequent sections provide additional details and examples for the main configuration options.

> [!NOTE]
> Secure Storage
> 
> The use of TLS, its associated keys and certificates requires using secure storage to minimize the chances of a security breach. The implementation of this storage differs from platform to platform — see [Using secure storage](p2psync-websocket.md#using-secure-storage).

## [](#configuration-summary)Configuration Summary

You must configure and initialize the Listener with a list of collections to sync. There is no limit on the number of Listeners you may configure — [Example 1](#simple-listener-initialization) shows a simple initialization and configuration process.

1. Identify the local database and the collections to be used — see: [Initialize the Listener Configuration](#initialize-the-listener-configuration).
2. Optionally, choose a port to use. By default the system will automatically assign a port — to over-ride this, see: [Set Port and Network Interface](#lbl-set-network-and-port).
3. Optionally, choose a network interface to use. By default the system will listen on all network interfaces — to over-ride this see: [Set Port and Network Interface](#lbl-set-network-and-port).
4. Optionally, choose to sync only changes. The default is not to enable delta-sync — see: [Delta Sync](#delta-sync).
5. Set server security. TLS is always enabled instantly, so you can usually omit this line. But you _can_, optionally, disable TLS (**not** advisable in production) — see: [TLS Security](#lbl-tls-security).
6. Set the credentials this server will present to the client for authentication. Here we show the default TLS authentication, which is an anonymous self-signed certificate. The server must always authenticate itself to the client.
7. Set client security — define the credentials the server expects the client to present for authentication. Here we show how basic authentication is configured to authenticate the client-supplied credentials from the http authentication header against valid credentials — see [Authenticating the Client](#lbl-authenticating-the-client) for more options.  
Note that client authentication is optional.
8. Initialize the listener using the configuration settings.
9. [Start Listener](#lbl-start-listener).

Example 1\. Listener configuration and initialization

```c
CBLURLEndpointListenerConfiguration config;
memset(&config, 0, sizeof(CBLURLEndpointListenerConfiguration));

// Setup collections available for replication:
CBLCollection* collections[1];
collections[0] = collection;

config.collections = collections;
config.collectionCount = 1;

// Use default anonymous TLSIdentity by setting NULL to tlsIdentity property:
config.disableTLS = false;
config.tlsIdentity = NULL; (1)

// Setup authenticator:
// Note: You can safely free `auth` after the listener is created:
CBLListenerAuthenticator* auth = CBLListenerAuth_CreatePassword(
    [](void* ctx, FLString user, FLString password) {
    return authenticate(user, password);
}, nullptr);
config.authenticator = auth; (2)

CBLError error;
memset(&error, 0, sizeof(CBLError));

// Create the listener with the config:
CBLURLEndpointListener* listener = CBLURLEndpointListener_Create(&config, &error);

// Start the listener:
CBLURLEndpointListener_Start(listener, &error);
```

| **1** | Here we show the default TLS authentication, which is an anonymous self-signed certificate. The server must always authenticate itself to the client.                                                                                                                                              |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Here we show how basic authentication is configured to authenticate the client-supplied credentials from the http authentication header against valid credentials — see [Authenticating the Client](#lbl-authenticating-the-client) for more options. Note that client authentication is optional. |

## [](#api-references)API References

You can find [C API References](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html) here.

## [](#device-discovery)Device Discovery

**This phase is optional:** If the Listener is initialized on a well-known URL endpoint (for example, a static IP Address or well-known DNS address) then you can configure Active Peers to connect to those.

Before initiating the Listener, you may execute a peer discovery phase. For the Passive Peer, this involves advertising the service using platform libraries, and waiting for an invite from the Active Peer. The connection is established once the Passive Peer has authenticated and accepted an Active Peer's invitation.

## [](#initialize-the-listener-configuration)Initialize the Listener Configuration

Initialize the Listener configuration with a list of collections from the local database — see [Example 2](#ex-locdb). All other configuration values take their default setting.

Example 2\. Specify Local Collections

```c
CBLURLEndpointListenerConfiguration config;
memset(&config, 0, sizeof(CBLURLEndpointListenerConfiguration));

// Setup collections available for replication:
CBLCollection* collections[1];
collections[0] = collection;

config.collections = collections;
config.collectionCount = 1;
```

Set the list of local collections using the [URLEndpointListenerConfiguration](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Fu%5Fr%5Fl%5Fendpoint%5Flistener%5Fconfiguration.html).

## [](#lbl-set-network-and-port)Set Port and Network Interface

### [](#port-number)Port number

The Listener will automatically select an available port if you do not specify one — see [Example 3](#ex-port) for how to specify a port.

Example 3\. Specify a port

```c
config.port = 55990;
```

To use a canonical port — one known to other applications — specify it explicitly using the [port](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Fu%5Fr%5Fl%5Fendpoint%5Flistener%5Fconfiguration.html#ae164b791eeeb816b9e3c3b25722a13a6) method shown here. Ensure that firewall rules do not block any port you do specify.

### [](#network-interface)Network Interface

The Listener will listen on all network interfaces by default.

Example 4\. Specify a Network Interface to Use

```c
config.networkInterface = FLSTR("10.1.1.10");
```

To specify an interface — one known to other applications — identify it explicitly, using the [networkInterface](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Fu%5Fr%5Fl%5Fendpoint%5Flistener%5Fconfiguration.html#a5a10543158ed28e4489d1256cb50309f) method shown here. This must be either an IP Address or network interface name such as `en0`.

## [](#delta-sync)Delta Sync

Delta Sync allows clients to sync only those parts of a document that have changed. This can result in significant bandwidth consumption savings and throughput improvements. Both are valuable benefits, especially when network bandwidth is constrained.

Example 5\. Enable delta sync

```c
config.enableDeltaSync = true;
```

Delta sync replication is not enabled by default. Use [URLEndpointListenerConfiguration](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Fu%5Fr%5Fl%5Fendpoint%5Flistener%5Fconfiguration.html)'s [enableDeltaSync](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Fu%5Fr%5Fl%5Fendpoint%5Flistener%5Fconfiguration.html#a09df56683ec60fadd06b9e7b2c457b36) method to activate or deactivate it.

## [](#lbl-tls-security)TLS Security

### [](#enable-or-disable-tls)Enable or Disable TLS

Define whether the connection is to use TLS or clear text.

TLS-based encryption is enabled by default, and this setting ought to be used in any production environment. However, it _can_ be disabled. For example, for development or test environments.

When TLS is enabled, Couchbase Lite provides several options on how the Listener may be configured with an appropriate TLS Identity — see [Configure TLS Identity for Listener](#configure-tls-identity-for-listener).

You can use [URLEndpointListenerConfiguration](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Fu%5Fr%5Fl%5Fendpoint%5Flistener%5Fconfiguration.html)'s [disableTLS](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Fu%5Fr%5Fl%5Fendpoint%5Flistener%5Fconfiguration.html#a6e12a73664e15fbd503be94e82ca8177) method to disable TLS communication if necessary.

The `disableTLS` setting must be 'false' when _Client Cert Authentication_ is required.

Basic Authentication can be used with, or without, TLS.

[disableTLS](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Fu%5Fr%5Fl%5Fendpoint%5Flistener%5Fconfiguration.html#a6e12a73664e15fbd503be94e82ca8177) works in conjunction with `TLSIdentity`, to enable developers to define the key and certificate to be used.

* If `disableTLS` is true — TLS communication is disabled and TLS identity is ignored. Active peers will use the `ws://` URL scheme used to connect to the listener.
* If `disableTLS` is false or not specified — TLS communication is enabled.  
Active peers will use the `wss://` URL scheme to connect to the listener.

### [](#configure-tls-identity-for-listener)Configure TLS Identity for Listener

Define the credentials the server will present to the client for authentication. Note that the server must always authenticate itself with the client — see: [Authenticate Listener on Active Peer](p2psync-websocket-using-active.md#authenticate-listener) for how the client deals with this.

Use [URLEndpointListenerConfiguration](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Fu%5Fr%5Fl%5Fendpoint%5Flistener%5Fconfiguration.html)'s [tlsIdentity](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Fu%5Fr%5Fl%5Fendpoint%5Flistener%5Fconfiguration.html#a872c060c215290313ab95bb920ad33ae) method to configure the TLS Identity used in TLS communication.

If `TLSIdentity` is not set, then the listener uses an auto-generated anonymous self-signed identity (unless `disableTLS = true`). Whilst the client cannot use this to authenticate the server, it will use it to encrypt communication, giving a more secure option than non-TLS communication.

On macOS, iOS, and Windows, the auto-generated anonymous self-signed identity is saved in secure storage for future use to obviate the need to re-generate it. Typically, you will configure the Listener's TLS Identity once during the initial launch and re-use it (from secure storage) on any subsequent starts.

On Linux and Android, the auto-generated anonymous self-signed identity is kept in memory and will be regenerated each time the listener is started.

Alternatively, you can use the [CBLTLSIdentity\_CreateIdentityWithKeyPair()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5F%5Ft%5Fl%5Fs%5Fidentity.html#ga28cacc360238506e7ea36f058a4bcd23) API with a [CBLKeyPair](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5F%5Ft%5Fl%5Fs%5Fidentity.html#ga50d0a2acc3f0d3794164edeed66074c0) object created using [CBLKeyPair\_CreateWithExternalKey()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5F%5Ft%5Fl%5Fs%5Fidentity.html#ga78d47a8c2157dad4347709d1adec6b39). This approach enables the use of a developer-provided private key stored in secure key storage of your choice, allowing cryptographic operations to be performed through CBLExternalKeyCallbacks functions without exposing the private key.

Couchbase Lite for C does not provide a convenience function to import a TLS identity from a secure key and certificate data source. You can generate a TLS identity from existing private key and certificate data in either PEM or DER format.

Here are some example code snippets showing:

* Setting TLS identity to expect self-signed certificate — see: [Example 6](#ex-create-tls-id)
* Setting TLS identity to expect anonymous certificate — see: [Example 7](#ex-anon-tls-id)
* Perform cryptographic operations through external key callback functions — see: [Example 8](#ex-external-key-callbacks)

Example 6\. Create Self-Signed Cert

Create a TLSIdentity for the server using convenience API. The system generates a self-signed certificate.

* macOS / iOS / Windows
* Linux / Android

```c
// Certificate Attributes:
FLMutableDict attributes = FLMutableDict_New();
FLMutableDict_SetString(attributes, kCBLCertAttrKeyCommonName, "Dev1"); (1)

// Creates and persists the self-signed identity with label named "myidentity":
CBLError error {};
CBLTLSIdentity* identity = CBLTLSIdentity_CreateIdentity( (2)
  kCBLKeyUsagesServerAuth,
  keypair,
  attributes,
  0 /* Default, 1 year */,
  FLSTR("myidentity") /* Persistent label */, (3)
  &error
);

// Release the attributes after creating the identity
FLMutableDict_Release(attributes);

// Release identity when you finish using it.
CBLTLSIdentity_Release(identity);
```

| **1** | The Common Name (CN) is the only required attribute for generating the certificate.                                                                                                                                                      |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Generate the self-signed TLS identity using the [CBLTLSIdentity\_CreateIdentity()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5F%5Ft%5Fl%5Fs%5Fidentity.html#ga7b9afa6f5f3167f7a2af08abc7778883) function. |
| **3** | If a persistent label is specified, the identity (including an RSA key pair and certificate) is also stored in secure key storage.                                                                                                       |

```c
// Certificate Attributes:
FLMutableDict attributes = FLMutableDict_New();
FLMutableDict_SetString(attributes, kCBLCertAttrKeyCommonName, "Dev1"); (1)

// Creates the self-signed identity:
CBLError error {};
CBLTLSIdentity* identity = CBLTLSIdentity_CreateIdentity( (2)
  kCBLKeyUsagesServerAuth,
  keypair,
  attributes,
  0 /* Default, 1 year */,
  kFLSliceNull /* NULL label */, (3)
  &error
);

// Release the attributes after creating the identity
FLMutableDict_Release(attributes);

// Release identity when you finish using it.
CBLTLSIdentity_Release(identity);
```

| **1** | The Common Name (CN) is the only required attribute for generating the certificate.                                                                                                                                                      |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Generate the self-signed TLS identity using the [CBLTLSIdentity\_CreateIdentity()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5F%5Ft%5Fl%5Fs%5Fidentity.html#ga7b9afa6f5f3167f7a2af08abc7778883) function. |
| **3** | The persistent label must be NULL, as identity persistence with a label is not supported. The created identity is stored in memory only.                                                                                                 |

Example 7\. Use Anonymous Self-Signed Certificate

This example uses an _anonymous_ self signed certificate. Generated certificates are held in secure storage.

```c
config.disableTLS  = false; (1)
// Use an anonymous self-signed cert
config.tlsIdentity = NULL; (2)
```

| **1** | Ensure TLS is used. This is the default setting.                                      |
| ----- | ------------------------------------------------------------------------------------- |
| **2** | Authenticate using an anonymous self-signed certificate. This is the default setting. |

Example 8\. Use External Key Callbacks

```c
typedef struct CBLExternalKeyCallbacks
{
  /** Provides the public key's raw data as an ASN.1 DER sequence of [modulus, exponent]. */
  bool (*publicKeyData)(void* externalKey, (1) (2)
                        void* output,
                        size_t outputMaxLen, (3)
                        size_t* outputLen);

  /** Decrypts data using the private key. */
  bool (*decrypt)(void* externalKey, (4)
                  FLSlice input,
                  void* output,
                  size_t outputMaxLen,
                  size_t* outputLen);

  /** Uses the private key to generate a signature of input data. */
  bool (*sign)(void* externalKey,
               CBLSignatureDigestAlgorithm digestAlgorithm, (5)
               FLSlice inputData, (6)
               void* outSignature);

  /** ( Optional ) For freeing any resource when the callbacks are no longer needed.*/
  void (*_cbl_nullable free)(void* externalKey);
} CBLKeyPairCallbacks;
```

| **1** | The public key is part of an RSA key pair generated by a secure key storage or cryptographic API.                                                                                                                                                                                                                                                   |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | externalKey is an opaque pointer passed to [CBLKeyPair\_CreateWithExternalKey()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5F%5Ft%5Fl%5Fs%5Fidentity.html#ga78d47a8c2157dad4347709d1adec6b39), typically representing a reference or token used to access the public / private key within the secure storage system. |
| **3** | Use outputMaxLen as a guardrail to ensure the public key data size is within the expected range.                                                                                                                                                                                                                                                    |
| **4** | Use RSA with PKCS#1 v1.5 padding. Algorithm names may vary — for example, RSA/ECB/PKCS1Padding on Java or Android. Note that depending on the selected key exchange method, the decrypt() function may not be invoked during the TLS handshake.                                                                                                     |
| **5** | You must use PKCS#1 v1.5 padding algorithm when generating the signature.                                                                                                                                                                                                                                                                           |
| **6** | Ensure that the input data, which is already hashed based on the specified digest algorithm, is encoded as an ASN.1 DigestInfo structure in DER format before performing the signing operation. Some cryptographic libraries may handle the DigestInfo formatting internally.                                                                       |

## [](#lbl-authenticating-the-client)Authenticating the Client

Define how the server (Listener) will authenticate the client as one it is prepared to interact with.

Whilst client authentication is optional, Couchbase lite provides the necessary tools to implement it. Use the [URLEndpointListenerConfiguration](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Fu%5Fr%5Fl%5Fendpoint%5Flistener%5Fconfiguration.html) class's [authenticator](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Fu%5Fr%5Fl%5Fendpoint%5Flistener%5Fconfiguration.html#a68159e04ec97a47fcbe785709ca54b35) method to specify how the client-supplied credentials are to be authenticated.

Valid options are:

* No authentication — If you do not define an Authenticator then all clients are accepted.
* Basic Authentication — uses the Listener [passwordAuthenticator](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Flistener%5Fauthenticator.html#ab289395196d0bbd4b7bd27bfbf1b9157) to authenticate the client using the client-supplied username and password (from the http authentication header).
* Listener [certificate](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Flistener%5Fauthenticator.html#ab772751f6c964814f9c49c934eb9facf) authenticator — which authenticates the client using a client supplied chain of one or more certificates. You should initialize the authenticator using one of the following constructors:

  * A root certificate, or a list of intermediate certificates and a root certificate — the client supplied certificate must end at a certificate in this list if it is to be authenticated.
  * A block of code that assumes total responsibility for authentication — it must return a boolean response (true for an authenticated client, or false for a failed authentication).

### [](#use-basic-authentication)Use Basic Authentication

Define how to authenticate client-supplied username and password credentials. To use client-supplied certificates instead — see: [Using Client Certificate Authentication](#using-client-certificate-authentication)

Example 9\. Password authentication

```c
// Configure Client Security using an Authenticator, for example, Basic Authentication.
// Note: You can safely free `auth` using CBLListenerAuth_Free() after the listener is created.
CBLListenerAuthenticator* auth = CBLListenerAuth_CreatePassword(
    [](void* ctx, FLString user, FLString password) {
        return authenticate(user, password);
    }, nullptr);
config.authenticator = auth;
```

Where `user` and `password` are the client-supplied values from the http-authentication header.

### [](#using-client-certificate-authentication)Using Client Certificate Authentication

Define how the server will authenticate client-supplied certificates.

There are two ways to authenticate a client:

* A chain of one or more certificates that ends at a certificate in the list of certificates supplied to the constructor for the Listener [certificate](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Flistener%5Fauthenticator.html#ab772751f6c964814f9c49c934eb9facf) authenticator — see: [Example 10](#ex-set-cert-auth).
* Application logic: This method assumes complete responsibility for verifying and authenticating the client — see: [Example 11](#ex-use-app-logic).  
If the parameter supplied to the constructor for the Listener `certificate` authenticator is of type `ListenerCertificateAuthenticatorDelegate`, all other forms of authentication are bypassed.  
The client response to the certificate request is passed to the method supplied as the constructor parameter. The logic should take the form of function or block (such as, a closure expression) where the platform allows.

Example 10\. Set Certificate Authorization

Configure the server (listener) to authenticate the client against a list of one or more certificates provided by the server to the Listener [certificate](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Flistener%5Fauthenticator.html#ab772751f6c964814f9c49c934eb9facf) authenticator.

```c
// Read intermediate and root cert from a PEM file:
char certPEMData[10000];
size_t certPEMSize = 10000;
read_pem_file("/drive/root_certs.pem", certPEMData, &certPEMSize);
FLSlice certSlice = {certPEMData, certPEMSize};

CBLError error;
memset(&error, 0, sizeof(CBLError));

// Create a cert object from certificates loaded from the PEM file:
// Note: You can safely release `rootCerts` using CBLCert_Release() after the listener is created.
CBLCert* rootCerts = CBLCert_CreateWithData(certSlice, &error); (1)

// Create a client certificate authenticator with the root certificate:
// Note: You can safely free `auth` using CBLListenerAuth_Free() after the listener is created.
CBLListenerAuthenticator* auth = CBLListenerAuth_CreateCertificateWithRootCerts(rootCerts); (2)

// Set the authenticator to the CBLURLEndpointListenerConfiguration:
config.authenticator = auth; (3)
```

| **1** | Get the identity data to authenticate against. This can be, for example, from a resource file provided with the app, or an identity previously saved in secure storage.                            |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Configure the authenticator to authenticate the client supplied certificate(s) using these root certs. A valid client will provide one or more certificates that match a certificate in this list. |
| **3** | Add the authenticator to the Listener configuration.                                                                                                                                               |

Example 11\. Application Logic

Configure the server (listener) to authenticate the client using user-supplied logic.

```c
// Create a client certificate authenticator with callback:
// Note: You can safely free `auth` using CBLListenerAuth_Free() after the listener is created.
CBLListenerAuthenticator* auth = CBLListenerAuth_CreateCertificate([](void* ctx, CBLCert* cert) {
    return authenticateClientCert(cert); (1)
}, nullptr);

// Set the authenticator to the config:
config.authenticator = auth; (2)
```

| **1** | Configure the Authenticator to pass the root certificates to a user supplied code block. This code assumes complete responsibility for authenticating the client supplied certificate(s). It must return a boolean value; with true denoting the client supplied certificate authentic. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Add the authenticator to the Listener configuration.                                                                                                                                                                                                                                    |

### [](#delete-tls-identity)Delete Entry

You can remove unwanted TLS identities from secure storage using the convenience API.

Example 12\. Deleting TLS Identities

```c
CBLError error;
memset(&error, 0, sizeof(CBLError));
CBLTLSIdentity_DeleteIdentityWithLabel(FLSTR("couchbaselite-server-cert-label"), &error);
```

### [](#the-impact-of-tls-settings)The Impact of TLS Settings

The table in this section shows the expected system behavior (in regards to security) depending on the TLS configuration settings deployed.

__Table 1\. Expected system behavior__
| disableTLS | tlsIdentity (corresponding to server)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Expected system behavior                                                                                                                                                                                                     |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| true       | Ignored                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | TLS is disabled; all communication is plain text.                                                                                                                                                                            |
| false      | set to nil                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | The system will auto generate an _anonymous_ self signed cert. Active Peers (clients) should be configured to accept self-signed certificates. Communication is encrypted                                                    |
| false      | Set to server identity generated from a self- or CA-signed certificate On first use — Bring your own certificate and private key; for example, using the [CBLTLSIdentity\_CreateIdentity()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5F%5Ft%5Fl%5Fs%5Fidentity.html#ga7b9afa6f5f3167f7a2af08abc7778883) method to add it to the secure storage. Each time — Use the server identity from the certificate stored in the secure storage, if supported. Alternatively, use external key callbacks to access private key stored in secure key storage of your choice. | System will use the configured identity. Active Peers will validate the server certificate corresponding to the TLSIdentity (as long as they are configured to not skip validation — see [TLS Security](#lbl-tls-security)). |

## [](#lbl-start-listener)Start Listener

Once you have completed the Listener's configuration settings you can initialize the Listener instance and start it running — see: [Example 13](#initialize-and-start-listener)

Example 13\. Initialize and start listener

```c
CBLError error;
memset(&error, 0, sizeof(CBLError));
CBLURLEndpointListener* listener = CBLURLEndpointListener_Create(&config, &error);

// Start the listener:
CBLURLEndpointListener_Start(listener, &error);
```

## [](#monitor-listener)Monitor Listener

Use the Listener's [CBLURLEndpointListener\_Status()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/%5Fc%5Fb%5Fl%5Fu%5Fr%5Fl%5Fendpoint%5Flistener%5F8h.html#ac5cc57610ce3d6a2fb1e891a8f24a448) property/method to get counts of total and active connections — see: [Example 14](#get-connection-counts).

You should note that these counts can be extremely volatile. So, the actual number of active connections may have changed, by the time the [ConnectionStatus](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Fconnection%5Fstatus.html) class returns a result.

Example 14\. Get connection counts

```c
CBLConnectionStatus status = CBLURLEndpointListener_Status(listener);
uint64_t totalConnections = status.connectionCount;
uint64_t activeConnections = status.activeConnectionCount;
```

## [](#stop-listener)Stop Listener

It is best practice to check the status of the Listener's connections and stop only when you have confirmed that there are no active connections — see [Example 14](#get-connection-counts).

Example 15\. Stop listener using `stop` method

```c
CBLURLEndpointListener_Stop(listener);
```

> [!NOTE]
> Closing the database will also close the Listener.

## [](#related-content)Related Content

### [](#)

How to

* [Passive Peer](p2psync-websocket-using-passive.md)
* [Active Peer](p2psync-websocket-using-active.md)

### [](#-2)

Concepts

* [Peer-to-Peer Sync](p2psync-websocket.md)
* [API References](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html)

### [](#-3)

Community Resources …​

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

[Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)