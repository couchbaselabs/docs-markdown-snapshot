---
title: Active Peer
description: Couchbase Lite's Peer-to-Peer Synchronization enables edge devices
  to synchronize securely without consuming centralized cloud-server resources
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.3/modules/android/pages/p2psync-websocket-using-active.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/couchbase-lite/3.3/android/p2psync-websocket-using-active.html)

# Active Peer

> Description — _Couchbase Lite’s Peer-to-Peer Synchronization enables edge devices to synchronize securely without consuming centralized cloud-server resources_  
> _Abstract — How to set up a Replicator to connect with a Listener and replicate changes using peer-to-peer sync_  
> Related Content — [API Reference](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/) | [Passive Peer](p2psync-websocket-using-passive.md) | [Active Peer](p2psync-websocket-using-active.md)

> [!CAUTION]
> Android enablers
> 
> Allow Unencrypted Network Traffic
> 
> To use cleartext, un-encrypted, network traffic (`http://` and-or `ws://`), include `android:usesCleartextTraffic="true"` in the `application` element of the manifest as shown on [android.com](https://developer.android.com/training/articles/security-config#CleartextTrafficPermitted).  
> **This not recommended in production**.
> 
> Use Background Threads
> 
> As with any network or file I/O activity, CouchbaseLite activities should not be performed on the UI thread. **Always** use a **background** thread.

> [!NOTE]
> Code Snippets
> 
> All code examples are indicative only. They demonstrate the basic concepts and approaches to using a feature. Use them as inspiration and adapt these examples to best practice when developing applications for your platform.

## [](#introduction)Introduction

This content provides sample code and configuration examples covering the implementation of [Peer-to-Peer Sync](refer-glossary.md#peer-to-peer-sync) over WebSockets. Specifically it covers the implementation of an [Active Peer](refer-glossary.md#active-peer).

This _active peer_ (also referred to as a client and-or a replicator) will initiate the connection with a [Passive Peer](refer-glossary.md#passive-peer) (also referred to as a server and-or listener) and participate in the replication of database changes to bring both databases into sync.

Subsequent sections provide additional details and examples for the main configuration options.

> [!NOTE]
> Secure Storage
> 
> The use of TLS, its associated keys and certificates requires using secure storage to minimize the chances of a security breach. The implementation of this storage differs from platform to platform — see [Using secure storage](p2psync-websocket.md#using-secure-storage).

## [](#configuration-summary)Configuration Summary

You should configure and initialize a replicator for each Couchbase Lite database instance you want to sync. [Example 1](#simple-replication-to-listener) shows the initialization and configuration process.

> [!NOTE]
> As with any network or file I/O activity, CouchbaseLite activities should not be performed on the UI thread. **Always** use a **background** thread.

Example 1\. Replication configuration and initialization

* Kotlin
* Java

```Kotlin
    // initialize the replicator configuration
    ReplicatorConfigurationFactory.newConfig(
        target = URLEndpoint(URI("wss://listener.com:8954")), (1)

        collections = mapOf(collections to null),

        // Set replicator type
        type = ReplicatorType.PUSH_AND_PULL,

        // Configure Sync Mode
        continuous = false, // default value


        // Configure Server Authentication --
        // only accept self-signed certs
        acceptOnlySelfSignedServerCertificate = true, (2)


        // Configure the credentials the
        // client will provide if prompted
        authenticator = BasicAuthenticator("PRIVUSER", "let me in".toCharArray())  (3)

    )
)

// Optionally add a change listener (4)
val token = repl.addChangeListener { change ->
    val err: CouchbaseLiteException? = change.status.error
    if (err != null) {
        log("Error code ::  ${err.code}", err)
    }
}

// Start replicator
repl.start(false) (5)

thisReplicator = repl
thisToken = token
```

```Java
    // initialize the replicator configuration
    new ReplicatorConfiguration(new URLEndpoint(new URI("wss://listener.com:8954"))) (1)
        .addCollections(collections, null)

        // Set replicator type
        .setType(ReplicatorType.PUSH_AND_PULL)

        // Configure Sync Mode
        .setContinuous(false) // default value


        // Configure Server Authentication --
        // only accept self-signed certs
        .setAcceptOnlySelfSignedServerCertificate(true) (2)

        // Configure the credentials the
        // client will provide if prompted
        .setAuthenticator(new BasicAuthenticator("Our Username", "Our Password".toCharArray())) (3)

);

// Optionally add a change listener (4)
ListenerToken token = repl.addChangeListener(change -> {
    CouchbaseLiteException err = change.getStatus().getError();
    if (err != null) { Logger.log("Error code :: " + err.getCode(), err); }
});

// Start replicator
repl.start(false); (5)

thisReplicator = repl;
thisToken = token;
```

| **1** | Configure how the client will authenticate the server. Here we say connect only to servers presenting a self-signed certificate. By default, clients accept only servers presenting certificates that can be verified using the OS bundled Root CA Certificates — see: [Authenticating the Listener](#authenticate-listener). |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Configure the credentials the client will present to the server. Here we say to provide _Basic Authentication_ credentials. Other options are available — see: [Example 7](#configuring-client-authentication).                                                                                                               |
| **3** | Configure how the replication should perform [Conflict Resolution](#conflict-resolution).                                                                                                                                                                                                                                     |
| **4** | Initialize the replicator using your configuration object.                                                                                                                                                                                                                                                                    |
| **5** | Register an observer, which will notify you of changes to the replication status.                                                                                                                                                                                                                                             |
| **6** | Start the replicator.                                                                                                                                                                                                                                                                                                         |

## [](#api-references)API References

You can find [Android API References](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/) here.

## [](#device-discovery)Device Discovery

**This phase is optional:** If the listener is initialized on a well known URL endpoint (for example, a static IP Address or well known DNS address) then you can configure Active Peers to connect to those.

Prior to connecting with a listener you may execute a Peer discovery phase to dynamically discover Peers.

For the Active Peer this involves browsing-for and selecting the appropriate service using a zero-config protocol such as _Network Service Discovery_ — see: <https://developer.android.com/training/connect-devices-wirelessly/nsd>.

## [](#configure-replicator)Configure Replicator

In this section

[Configure Target](#lbl-cfg-tgt)| [Sync Mode](#lbl-cfg-sync)| [Retry Configuration](#lbl-cfg-retry)| [Authenticating the Listener](#authenticate-listener)| [Client Authentication](#lbl-authclnt)

### [](#lbl-cfg-tgt)Configure Target

Use the Initialize and define the replication configuration with local and remote database locations using the [ReplicatorConfiguration](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html) object.

The constructor provides:

* the name of the local database to be sync’d
* the server’s URL (including the port number and the name of the remote database to sync with)  
It is expected that the app will identify the IP address and URL and append the remote database name to the URL endpoint, producing for example: `wss://10.0.2.2:4984/travel-sample`  
The URL scheme for web socket URLs uses `ws:` (non-TLS) or `wss:` (SSL/TLS) prefixes. To use cleartext, un-encrypted, network traffic (`http://` and-or `ws://`), include `android:usesCleartextTraffic="true"` in the `application` element of the manifest as shown on [android.com](https://developer.android.com/training/articles/security-config#CleartextTrafficPermitted).  
**This not recommended in production**.

Example 2\. Add Target to Configuration

* Kotlin
* Java

```Kotlin
// initialize the replicator configuration
val thisConfig = ReplicatorConfigurationFactory.newConfig(
    target = URLEndpoint(URI("wss://10.0.2.2:8954/travel-sample")), (1)
    collections = mapOf(collections to null)
)
```

```Java
// initialize the replicator configuration
ReplicatorConfiguration thisConfig = new ReplicatorConfiguration(
    new URLEndpoint(new URI("wss://10.0.2.2:8954/travel-sample"))) (1)
    .addCollections(collections, null);
```

| **1** | Note use of the scheme prefix (wss://to ensure TLS encryption — strongly recommended in production — or ws://) |
| ----- | -------------------------------------------------------------------------------------------------------------- |

### [](#lbl-cfg-sync)Sync Mode

Here we define the direction and type of replication we want to initiate.

We use `[ReplicatorConfiguration](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html)` class’s [replicatorType](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html#setReplicatorType-com.couchbase.lite.AbstractReplicatorConfiguration.ReplicatorType-) and `[continuous](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html#setContinuous-boolean-)` parameters, to tell the replicator:

* The type (or direction) of the replication: `**PUSH_AND_PULL**`; `PULL`; `PUSH`
* The replication mode, that is either of:

  * Continuous — remaining active indefinitely to replicate changed documents (`continuous=true`).
  * Ad-hoc — a one-shot replication of changed documents (`continuous=false`).

Example 3\. Configure replicator type and mode

* Kotlin
* Java

```Kotlin
// Set replicator type
type = ReplicatorType.PUSH_AND_PULL,

// Configure Sync Mode
continuous = false, // default value
```

```Java
// Set replicator type
.setType(ReplicatorType.PUSH_AND_PULL)

// Configure Sync Mode
.setContinuous(false) // default value
```

> [!TIP]
> Unless there is a solid use-case not to, always initiate a single `PUSH_AND_PULL` replication rather than identical separate `PUSH` and `PULL` replications.
> 
> This prevents the replications generating the same checkpoint `docID` resulting in multiple conflicts.

### [](#lbl-cfg-retry)Retry Configuration

Couchbase Lite for Android’s replication retry logic assures a resilient connection.

The replicator minimizes the chance and impact of dropped connections by maintaining a heartbeat; essentially pinging the listener at a configurable interval to ensure the connection remains alive.

In the event it detects a transient error, the replicator will attempt to reconnect, stopping only when the connection is re-established, or the number of retries exceeds the retry limit (9 times for a single-shot replication and unlimited for a continuous replication).

On each retry the interval between attempts is increased exponentially (exponential backoff) up to the maximum wait time limit (5 minutes).

The REST API provides configurable control over this replication retry logic using a set of configiurable properties — see: [Table 1](#tbl-repl-retry).

__Table 1\. Replication Retry Configuration Properties__
| Property                                                                                                                                                                      | Use cases                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [setHeartbeat()](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicatorConfiguration.html#setHeartbeat-long-)                   | Reduce to detect connection errors sooner Align to load-balancer or proxy keep-alive interval — see Sync Gateway’s topic [Load Balancer - Keep Alive](../../../sync-gateway/current/deploy/load-balancer.md#websocket-connection) | The interval (in seconds) between the heartbeat pulses. Default: The replicator pings the listener every 300 seconds.                                                                                                                                                                                                                                                                                                                                                                             |
| [setMaxAttempts()](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicatorConfiguration.html#setMaxAttempts-int-)                | Change this to limit or extend the number of retry attempts.                                                                                                                                                                      | The maximum number of retry attempts Set to zero (0) to use default values Set to zero (1) to prevent any retry attempt The retry attempt count is reset when the replicator is able to connect and replicate Default values are: Single-shot replication = 9; Continuous replication = maximum integer value Negative values generate a Couchbase exception InvalidArgumentException                                                                                                             |
| [setMaxAttemptWaitTime()](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicatorConfiguration.html#setMaxAttemptWaitTime-long-) | Change this to adjust the interval between retries.                                                                                                                                                                               | The maximum interval between retry attempts While you can configure the **maximum permitted** wait time, the replicator’s exponential backoff algorithm calculates each individual interval which is not configurable. Default value: 300 seconds (5 minutes) Zero sets the maximum interval between retries to the default of 300 seconds 300 sets the maximum interval between retries to the default of 300 seconds A negative value generates a Couchbase exception, InvalidArgumentException |

When necessary you can adjust any or all of those configurable values — see: [Example 4](#ex-repl-retry) for how to do this.

Example 4\. Configuring Replication Retries

* Kotlin
* Java

```Kotlin
val repl = Replicator(
    ReplicatorConfigurationFactory.newConfig(
        target = URLEndpoint(URI("ws://localhost:4984/mydatabase")),
        collections = mapOf(collections to null),
        //  other config params as required . .
        heartbeat = 150, (1)
        maxAttempts = 20,
        maxAttemptWaitTime = 600
    )
)
repl.start()
thisReplicator = repl
```

```Java
Replicator repl = new Replicator(
    new ReplicatorConfiguration(new URLEndpoint(new URI("ws://localhost:4984/mydatabase")))
        .addCollections(collections, null)
        //  other config as required . . .
        .setHeartbeat(150) (1)
        .setMaxAttempts(20) (2)
        .setMaxAttemptWaitTime(600)); (3)

repl.start();
thisReplicator = repl;
```

| **1** | Here we use [setHeartbeat()](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicatorConfiguration.html#setHeartbeat-long-) to set the required interval (in seconds) between the heartbeat pulses |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Here we use [setMaxAttempts()](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicatorConfiguration.html#setMaxAttempts-int-) to set the required number of retry attempts                        |
| **3** | Here we use [setMaxAttemptWaitTime()](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicatorConfiguration.html#setMaxAttemptWaitTime-long-) to set the required interval between retry attempts. |

### [](#authenticate-listener)Authenticating the Listener

Define the credentials the your app (the client) is expecting to receive from the server (listener) in order to ensure that the server is one it is prepared to interact with.

Note that the client cannot authenticate the server if TLS is turned off. When TLS is enabled (Sync Gateway’s default) the client _must_ authenticate the server. If the server cannot provide acceptable credentials then the connection will fail.

Use `[ReplicatorConfiguration](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html)` properties [setAcceptOnlySelfSignedServerCertificate](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html#setAcceptOnlySelfSignedServerCertificate-boolean-) and [setPinnedServerCertificate](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html#setPinnedServerCertificate-byte:A-), to tell the replicator how to verify server-supplied TLS server certificates.

* If there is a pinned certificate, nothing else matters, the server cert must **exactly** match the pinned certificate.
* If there are no pinned certs and [setAcceptOnlySelfSignedServerCertificate](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html#setAcceptOnlySelfSignedServerCertificate-boolean-) is `true` then any self-signed certificate is accepted. Certificates that are not self signed are rejected, no matter who signed them.
* If there are no pinned certificates and [setAcceptOnlySelfSignedServerCertificate](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html#setAcceptOnlySelfSignedServerCertificate-boolean-) is `false` (default), the client validates the server’s certificates against the system CA certificates. The server must supply a chain of certificates whose root is signed by one of the certificates in the system CA bundle.

Example 5\. Set Server TLS security

* Kotlin
* Java

* CA Cert
* Self Signed Cert
* Pinned Certificate

Set the client to expect and accept only CA attested certificates.

```Kotlin
// Configure Server Security
// -- only accept CA attested certs
acceptOnlySelfSignedServerCertificate = false, (1)
```

| **1** | This is the default. Only certificate chains with roots signed by a trusted CA are allowed. Self signed certificates are not allowed. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------- |

Set the client to expect and accept only self-signed certificates

```Kotlin
// Configure Server Authentication --
// only accept self-signed certs
acceptOnlySelfSignedServerCertificate = true, (1)
```

| **1** | Set this to true to accept any self signed cert. Any certificates that are not self-signed are rejected. |
| ----- | -------------------------------------------------------------------------------------------------------- |

Set the client to expect and accept only a pinned certificate.

```Kotlin
// Use the pinned certificate from the byte array (cert)
pinnedServerCertificate =
TLSIdentity.getIdentity("Our Corporate Id")?.certs?.get(0) as? X509Certificate (1)
    ?: throw IllegalStateException("Cannot find corporate id"),
```

* CA Cert
* Self Signed Cert
* Pinned Certificate

Set the client to expect and accept only CA attested certificates.

```Java
// Configure Server Security
// -- only accept CA attested certs
.setAcceptOnlySelfSignedServerCertificate(false); (1)
```

| **1** | This is the default. Only certificate chains with roots signed by a trusted CA are allowed. Self signed certificates are not allowed. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------- |

Set the client to expect and accept only self-signed certificates

```Java
// Configure Server Authentication --
// only accept self-signed certs
.setAcceptOnlySelfSignedServerCertificate(true) (1)
```

| **1** | Set this to true to accept any self signed cert. Any certificates that are not self-signed are rejected. |
| ----- | -------------------------------------------------------------------------------------------------------- |

Set the client to expect and accept only a pinned certificate.

```Java
// Use the pinned certificate from the byte array (cert)

TLSIdentity identity = TLSIdentity.getIdentity("OurCorp");
if (identity == null) { throw new IllegalStateException("Cannot find corporate id"); }
config.setPinnedServerX509Certificate((X509Certificate) identity.getCerts().get(0)); (1)
```

### [](#lbl-authclnt)Client Authentication

Here we define the credentials that the client can present to the server if prompted to do so in order that the server can authenticate it.

We use [ReplicatorConfiguration](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html)'s [setAuthenticator](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html#setAuthenticator-com.couchbase.lite.Authenticator-) method to define the authentication method to the replicator.

### [](#basic-authentication)Basic Authentication

Use the `[BasicAuthenticator](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/BasicAuthenticator.html)` to supply basic authentication credentials (username and word).

Example 6\. Basic Authentication

This example shows basic authentication using user name and password:

* Kotlin
* Java

```Kotlin
// Configure the credentials the
// client will provide if prompted
authenticator = BasicAuthenticator("PRIVUSER", "let me in".toCharArray())  (1)
```

```Java
// Configure the credentials the
// client will provide if prompted
.setAuthenticator(new BasicAuthenticator("Our Username", "Our Password".toCharArray())) (1)
```

### [](#certificate-authentication)Certificate Authentication

Use the `[ClientCertificateAuthenticator](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ClientCertificateAuthenticator.html)` to configure the client TLS certificates to be presented to the server, on connection. This applies only to the [URLEndpointListener](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/URLEndpointListener.html).

> [!NOTE]
> The **server** (listener) must have `disableTLS` set `false` and have a [ClientCertificateAuthenticator](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ClientCertificateAuthenticator.html) configured, or it will never ask for this client’s certificate.

The certificate to be presented to the server will need to be signed by the root certificates or be valid based on the authentication callback set to the listener via ListenerCertificateAuthenticator.

TLSIdentity.getIdentity uses the Android keystore. Please see (Android developers documentation (for example <https://developer.android.com/training/articles/keystore>) for more information about how to import a keychain.

Example 7\. Client Cert Authentication

This example shows client certificate authentication using an identity from secure storage.

* Kotlin
* Java

```Kotlin
        // Provide a client certificate to the server for authentication
        authenticator = ClientCertificateAuthenticator(
            TLSIdentity.getIdentity("clientId")
                ?: throw IllegalStateException("Cannot find client id")
        ) (1)

        // ... other replicator configuration
    )
)

thisReplicator = repl
```

```Java
// Provide a client certificate to the server for authentication
TLSIdentity clientId = TLSIdentity.getIdentity("client");
if (clientId == null) { throw new IllegalStateException("Cannot find client id"); }
config.setAuthenticator(new ClientCertificateAuthenticator(clientId)); (1)

// ... other replicator configuration

Replicator repl = new Replicator(config);
repl.start();
thisReplicator = repl;
```

| **1** | Get an identity from secure storage and create a TLS Identity object                                                                                                                                                            |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Set the authenticator to [ClientCertificateAuthenticator](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ClientCertificateAuthenticator.html) and configure it to use the retrieved identity |

## [](#initialize-replicator)Initialize Replicator

Use the `[Replicator](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/Replicator.html)` class’s [ReplicatorConfiguration(config)](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/Replicator.html#Replicator-com.couchbase.lite.ReplicatorConfiguration-) constructor, to initialize the replicator with the configuration you have defined. You can, optionally, add a change listener (see [Monitor Sync](#lbl-repl-mon)) before starting the replicator running using [start()](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#start-boolean-).

Example 8\. Initialize and run replicator

* Kotlin
* Java

```Kotlin
// Create replicator
// Consider holding a reference somewhere
// to prevent the Replicator from being GCed
val repl = Replicator( (1)

    // initialize the replicator configuration
    ReplicatorConfigurationFactory.newConfig(
        target = URLEndpoint(URI("wss://listener.com:8954")), (2)

        collections = mapOf(collections to null),

        // Set replicator type
        type = ReplicatorType.PUSH_AND_PULL,

        // Configure Sync Mode
        continuous = false, // default value


        // set auto-purge behavior
        // (here we override default)
        enableAutoPurge = false, (3)


        // Configure Server Authentication --
        // only accept self-signed certs
        acceptOnlySelfSignedServerCertificate = true, (4)


        // Configure the credentials the
        // client will provide if prompted
        authenticator = BasicAuthenticator("PRIVUSER", "let me in".toCharArray())  (5)

    )
)

// Start replicator
repl.start(false) (6)

thisReplicator = repl
thisToken = token
```

```Java
// Create replicator
// Consider holding a reference somewhere
// to prevent the Replicator from being GCed
Replicator repl = new Replicator( (1)

    // initialize the replicator configuration
    new ReplicatorConfiguration(new URLEndpoint(new URI("wss://listener.com:8954"))) (2)
        .addCollections(collections, null)

        // Set replicator type
        .setType(ReplicatorType.PUSH_AND_PULL)

        // Configure Sync Mode
        .setContinuous(false) // default value


        // set auto-purge behavior
        // (here we override default)
        .setAutoPurgeEnabled(false) (3)


        // Configure Server Authentication --
        // only accept self-signed certs
        .setAcceptOnlySelfSignedServerCertificate(true) (4)

        // Configure the credentials the
        // client will provide if prompted
        .setAuthenticator(new BasicAuthenticator("Our Username", "Our Password".toCharArray())) (5)

);

// Start replicator
repl.start(false); (6)

thisReplicator = repl;
thisToken = token;
```

| **1** | Initialize the replicator with the configuration |
| ----- | ------------------------------------------------ |
| **2** | Start the replicator                             |

## [](#lbl-repl-mon)Monitor Sync

In this section

[Change Listeners](#lbl-repl-chng) | [Replicator Status](#lbl-repl-status) | [Documents Pending Push](#lbl-repl-pend)

You can monitor a replication’s status by using a combination of [Change Listeners](#lbl-repl-chng) and the `replication.status.activity` property — see; [getActivityLevel()](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ReplicatorStatus.html#getActivityLevel%28%29). This enables you to know, for example, when the replication is actively transferring data and when it has stopped.

### [](#lbl-repl-chng)Change Listeners

Use this to monitor changes and to inform on sync progress; this is an optional step. You can add and a replicator change listener at any point; it will report changes from the point it is registered.

> [!TIP]
> Best Practice
> 
> Don’t forget to save the token so you can remove the listener later

Use the [Replicator](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/Replicator.html) class to add a change listener as a callback to the Replicator ([addChangeListener()](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#addChangeListener-java.util.concurrent.Executor-com.couchbase.lite.ReplicatorChangeListener-)) — see: [Example 9](#ex-repl-mon). You will then be asynchronously notified of state changes.

You can remove a change listener with [removeChangeListener(ListenerToken token)](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#removeChangeListener-com.couchbase.lite.ListenerToken-).

### [](#using-kotlin-flows-and-livedata)Using Kotlin Flows and LiveData

Android Kotlin developers can take advantage of Flows and LiveData to monitor replicators.

```Kotlin
Unresolved include directive in modules/android/pages/p2psync-websocket-using-active.adoc - include::android:example$snippets/app/src/main/kotlin/com/couchbase/code_snippets/FlowExamples.kt[]
```

### [](#lbl-repl-status)Replicator Status

You can use the [ReplicatorStatus()](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ReplicatorStatus.html) class to check the replicator status. That is, whether it is actively transferring data or if it has stopped — see: [Example 9](#ex-repl-mon).

The returned _ReplicationStatus_ structure comprises:

* [getActivityLevel()](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ReplicatorStatus.html#getActivityLevel%28%29) — stopped, offline, connecting, idle or busy — see states described in: [Table 2](#tbl-states)
* [getProgress()](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ReplicatorStatus.html#getProgress%28%29)

  * completed — the total number of changes completed
  * total — the total number of changes to be processed
* [getError()](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ReplicatorStatus.html#getError) — the current error, if any

Example 9\. Monitor replication

* Kotlin
* Java

* Adding a Change Listener
* Using replicator.status

```Kotlin
val token = repl.addChangeListener { change ->
    val err: CouchbaseLiteException? = change.status.error
    if (err != null) {
        log("Error code ::  ${err.code}", err)
    }
}
```

```Kotlin
repl.status.let {
    val progress = it.progress
    log(
        "The Replicator is ${
            it.activityLevel
        } and has processed ${
            progress.completed
        } of ${progress.total} changes"
    )
}
```

* Adding a Change Listener
* Using replicator.status

```Java
ListenerToken token = repl.addChangeListener(change -> {
    CouchbaseLiteException err = change.getStatus().getError();
    if (err != null) { Logger.log("Error code :: " + err.getCode(), err); }
});
```

```Java
    ReplicatorStatus status = repl.getStatus();
    ReplicatorProgress progress = status.getProgress();
    Logger.log(
        "The Replicator is " + status.getActivityLevel()
            + "and has processed " + progress.getCompleted()
            + " of " + progress.getTotal() + " changes");
}
```

### [](#lbl-repl-states)Replication States

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

### [](#replication-status-and-app-life-cycle)Replication Status and App Life Cycle

Couchbase Lite replications will continue running until the app terminates, unless the remote system, or the application, terminates the connection.

> [!NOTE]
> Recall that the Android OS may kill an application without warning. You should explicitly stop replication processes when they are no longer useful (for example, when they are `suspended` or `idle`) to avoid socket connections being closed by the OS, which may interfere with the replication process.

### [](#lbl-repl-pend)Documents Pending Push

> [!TIP]
> [Replicator.isDocumentPending()](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#isDocumentPending-java.lang.String-) is quicker and more efficient. Use it in preference to returning a list of pending document IDs, where possible.

You can check whether documents are waiting to be pushed in any forthcoming sync by using either of the following API methods:

* Use the [Replicator.getPendingDocumentIds()](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#getPendingDocumentIds--) method, which returns a list of document IDs that have local changes, but which have not yet been pushed to the server.  
This can be very useful in tracking the progress of a push sync, enabling the app to provide a visual indicator to the end user on its status, or decide when it is safe to exit.
* Use the [Replicator.isDocumentPending()](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#isDocumentPending-java.lang.String-) method to quickly check whether an individual document is pending a push.

Example 10\. Use Pending Document ID API

* Kotlin
* Java

```Kotlin
val repl = Replicator(
    ReplicatorConfigurationFactory.newConfig(
        target = URLEndpoint(URI("ws://localhost:4984/mydatabase")),
        collections = mapOf(setOf(collection) to null),
        type = ReplicatorType.PUSH
    )
)

val pendingDocs = repl.getPendingDocumentIds(collection)

// iterate and report on previously
// retrieved pending docids 'list'
if (pendingDocs.isNotEmpty()) {
    log("There are ${pendingDocs.size} documents pending")

    val firstDoc = pendingDocs.first()
    repl.addChangeListener { change ->
        log("Replicator activity level is ${change.status.activityLevel}")
        try {
            if (!repl.isDocumentPending(firstDoc, collection)) {
                log("Doc ID $firstDoc has been pushed")
            }
        } catch (err: CouchbaseLiteException) {
            log("Failed getting pending docs", err)
        }
    }

    repl.start()
    thisReplicator = repl
}
```

```Java
Replicator repl = new Replicator(
    new ReplicatorConfiguration(new URLEndpoint(new URI("ws://localhost:4984/mydatabase")))
        .addCollection(collection, null)
        .setType(ReplicatorType.PUSH));

Set<String> pendingDocs = repl.getPendingDocumentIds(collection);

if (!pendingDocs.isEmpty()) {
    Logger.log("There are " + pendingDocs.size() + " documents pending");

    final String firstDoc = pendingDocs.iterator().next();

    repl.addChangeListener(change -> {
        Logger.log("Replicator activity level is " + change.getStatus().getActivityLevel());
        try {
            if (!repl.isDocumentPending(firstDoc, collection)) {
                Logger.log("Doc ID " + firstDoc + " has been pushed");
            }
        }
        catch (CouchbaseLiteException err) {
            Logger.log("Failed getting pending docs", err);
        }
    });

    repl.start();
    this.thisReplicator = repl;
}
```

| **1** | [Replicator.getPendingDocumentIds()](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#getPendingDocumentIds--) returns a list of the document IDs for all documents waiting to be pushed. This is a snapshot and may have changed by the time the response is received and processed. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [Replicator.isDocumentPending()](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#isDocumentPending-java.lang.String-) returns true if the document is waiting to be pushed, and false otherwise.                                                                                     |

## [](#lbl-repl-stop)Stop Sync

Stopping a replication is straightforward. It is done using [stop()](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#stop--). This initiates an asynchronous operation and so is not necessarily immediate. Your app should account for this potential delay before attempting any subsequent operations.

You can find further information on database operations in [Databases](database.md).

Example 11\. Stop replicator

* Kotlin
* Java

```Kotlin
// Stop replication.
repl.stop() (1)
```

```Java
// Stop replication.
repl.stop(); (1)
```

| **1** | Here we initiate the stopping of the replication using the [stop()](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#stop--) method. It will stop any active [change listener](#lbl-repl-chng) once the replication is stopped. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#conflict-resolution)Conflict Resolution

Unless you specify otherwise, Couchbase Lite’s default conflict resolution policy is applied — see [Handling Data Conflicts](conflict.md).

To use a different policy, specify a _conflict resolver_ using [conflictResolver](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html#setConflictResolver-com.couchbase.lite.ConflictResolver-) as shown in [Example 12](#using-conflict-resolvers).

For more complex solutions you can provide a custom conflict resolver - see: [Handling Data Conflicts](conflict.md).

Example 12\. Using conflict resolvers

* Kotlin
* Java

* Local Wins
* Remote Wins
* Merge

```Kotlin
// Using replConfig.setConflictResolver(new LocalWinConflictResolver());
@Suppress("unused")
object LocalWinsResolver : ConflictResolver {
    override fun resolve(conflict: Conflict) = conflict.localDocument
}
```

```Kotlin
// Using replConfig.setConflictResolver(new RemoteWinConflictResolver());
@Suppress("unused")
object RemoteWinsResolver : ConflictResolver {
    override fun resolve(conflict: Conflict) = conflict.remoteDocument
}
```

```Kotlin
// Using replConfig.setConflictResolver(new MergeConflictResolver());
@Suppress("unused")
object MergeConflictResolver : ConflictResolver {
    override fun resolve(conflict: Conflict): Document {
        val localDoc = conflict.localDocument?.toMap()
        val remoteDoc = conflict.remoteDocument?.toMap()

        val merge: MutableMap<String, Any>?
        if (localDoc == null) {
            merge = remoteDoc
        } else {
            merge = localDoc
            if (remoteDoc != null) {
                merge.putAll(remoteDoc)
            }
        }

        return if (merge == null) {
            MutableDocument(conflict.documentId)
        } else {
            MutableDocument(conflict.documentId, merge)
        }
    }
```

* Local Wins
* Remote Wins
* Merge

```Java
class LocalWinConflictResolver implements ConflictResolver {
    public Document resolve(Conflict conflict) {
        return conflict.getLocalDocument();
    }
}
```

```Java
// Using replConfig.setConflictResolver(new RemoteWinConflictResolver());
@Suppress("unused")
object RemoteWinsResolver : ConflictResolver {
    override fun resolve(conflict: Conflict) = conflict.remoteDocument
}
```

```Java
class MergeConflictResolver implements ConflictResolver {
    public Document resolve(Conflict conflict) {
        Map<String, Object> merge = conflict.getLocalDocument().toMap();
        merge.putAll(conflict.getRemoteDocument().toMap());
        return new MutableDocument(conflict.getDocumentId(), merge);
    }
}
```

Just as a replicator may observe a conflict — when updating a document that has changed both in the local database and in a remote database — any attempt to save a document may also observe a conflict, if a replication has taken place since the local app retrieved the document from the database. To address that possibility, a version of the `Database.save()` method also takes a conflict resolver as shown in [Example 13](#ex-merge-props).

The following code snippet shows an example of merging properties from the existing document (`current`) into the one being saved (`new`). In the event of conflicting keys, it will pick the key value from `new`.

Example 13\. Merging document properties

* Kotlin
* Java

```Kotlin
val mutableDocument = collection.getDocument("xyz")?.toMutable() ?: return
mutableDocument.setString("name", "apples")
collection.save(mutableDocument) { newDoc, curDoc ->  (1)
    if (curDoc == null) {
        return@save false
    } (2)
    val dataMap: MutableMap<String, Any> = curDoc.toMap()
    dataMap.putAll(newDoc.toMap()) (3)
    newDoc.setData(dataMap)
    true (4)
} (5)
```

```Java
Document doc = collection.getDocument("xyz");
if (doc == null) { return; }
MutableDocument mutableDocument = doc.toMutable();
mutableDocument.setString("name", "apples");

collection.save(
    mutableDocument,
    (newDoc, curDoc) -> {
        if (curDoc == null) { return false; }
        Map<String, Object> dataMap = curDoc.toMap();
        dataMap.putAll(newDoc.toMap());
        newDoc.setData(dataMap);
        return true;
    });
```

For more on replicator conflict resolution see: [Handling Data Conflicts](conflict.md).

## [](#delta-sync)Delta Sync

If delta sync is enabled on the listener, then replication will use delta sync.

## [](#related-content)Related Content

### [](#)

How to

* [Passive Peer](p2psync-websocket-using-passive.md)
* [Active Peer](p2psync-websocket-using-active.md)

.

### [](#-2)

Concepts

* [Peer-to-Peer Sync](#android:landing-p2psync.adoc)
* [API References](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/)

.

### [](#-3)

Community Resources …​

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

. [Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)