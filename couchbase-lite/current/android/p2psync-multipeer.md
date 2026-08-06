---
title: Multipeer P2P Replicator
description: The Multipeer Replicator enables lightweight, self-organizing mesh
  networks over Wi-Fi and Bluetooth Low Energy.
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.1/modules/android/pages/p2psync-multipeer.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:couchbase-lite:android:p2psync-multipeer.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/android/p2psync-multipeer.html)

# Multipeer P2P Replicator

> The Multipeer Replicator enables lightweight, self-organizing mesh networks over Wi-Fi and Bluetooth Low Energy. This approach requires minimal setup and automates peer discovery and connectivity management, making it simpler than [active-passive P2P configurations](p2psync-websocket.md). 

## [](#introduction)Introduction

Couchbase Lite's Peer-to-Peer synchronization solution offers secure storage and bidirectional data synchronization between mobile and IoT devices without needing a centralized cloud-based control point.

For small mesh topologies, Multipeer Replicator offers autodiscovery over Wi-Fi and Bluetooth Low Energy, with secure communication via TLS and certificate-based authentication.

The dynamic mesh topology gives optimal peer connectivity and the lightweight and low-maintenance configuration requires less management and less code than using active-passive peer-to-peer sync.

## [](#overview)Overview

To maintain optimal connectivity, efficient data transport, and balanced workloads, the Multipeer Replicator forms a dynamic mesh network among peers in the same group. The mesh network provides resilience through multiple communication pathways. If one connection fails, data can flow through alternative routes.

It avoids redundant direct connections, evenly distributes connections across peers, and optimizes communication paths through intelligent routing.

The mesh network continuously adapts as peers join or leave, automatically healing itself by establishing new connections and rerouting data flow to maintain network integrity.

This self-organizing approach ensures reliable data synchronization even in challenging network conditions, where individual peer connections may be intermittent or unreliable.

> [!NOTE]
> The Multipeer Replicator supports cross-platform replication between Android and iOS peers running Couchbase Lite 4.1 or higher. An Android powered device and an iOS device using the same group ID, identity certificates from the same CA, and matching transport configuration can discover and replicate with each other over both Wi-Fi and Bluetooth.

## [](#prerequisites)Prerequisites

The Multipeer Replicator supports two transports for peer discovery and replication: Wi-Fi and Bluetooth Low Energy (BLE). Wi-Fi is enabled by default. Bluetooth is optional and you enable it through the replicator configuration. See [Transports](#transports).

### [](#transport-support)Transport Support

__Table 1\. Transport support__
| Transport            | Available from | Discovery                    | Minimum Android API | Notes                                                                                                                            |
| -------------------- | -------------- | ---------------------------- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Wi-Fi                | CBL 3.3        | DNS-SD (Bonjour)             | API 24              | Peers must connect to the same Wi-Fi network.                                                                                    |
| Bluetooth Low Energy | CBL 4.1        | BLE advertising and scanning | API 29              | Requires additional manifest permissions and runtime permission requests. See [Platform Configuration](#platform-configuration). |

### [](#supported-platforms)Supported Platforms

For Wi-Fi transport, CBL supports Android API 24 and higher.

For Bluetooth transport, CBL supports Android API 29 and higher. On API 29 and 30, Bluetooth uses the legacy `BLUETOOTH`, `BLUETOOTH_ADMIN`, and `ACCESS_FINE_LOCATION` permissions. On API 31 and higher, Bluetooth uses the runtime permissions `BLUETOOTH_SCAN`, `BLUETOOTH_ADVERTISE`, and `BLUETOOTH_CONNECT`.

See [Supported Platforms](#kotlin:supported-os.adoc) for the full platform support matrix.

### [](#platform-configuration)Platform Configuration

This section applies only if your application enables Bluetooth transport. Applications that use Wi-Fi only do not require these permissions.

#### [](#manifest-permissions)Manifest Permissions

Declare the required Bluetooth permissions in your `AndroidManifest.xml`. The permissions differ between Android 11 (API 30) and lower, and Android 12 (API 31) and higher.

```xml
<manifest ...>

    <!-- Android 11 (API 30) and lower -->
    <uses-permission
        android:name="android.permission.BLUETOOTH"
        android:maxSdkVersion="30" />
    <uses-permission
        android:name="android.permission.BLUETOOTH_ADMIN"
        android:maxSdkVersion="30" />
    <uses-permission
        android:name="android.permission.ACCESS_FINE_LOCATION"
        android:maxSdkVersion="30" />

    <!-- Android 12 (API 31) and higher -->
    <uses-permission
        android:name="android.permission.BLUETOOTH_SCAN"
        android:usesPermissionFlags="neverForLocation" />
    <uses-permission
        android:name="android.permission.BLUETOOTH_ADVERTISE" />
    <uses-permission
        android:name="android.permission.BLUETOOTH_CONNECT" />

    <!-- Android 13 (API 33) and higher: required for Wi-Fi peer discovery -->
    <uses-permission
        android:name="android.permission.NEARBY_WIFI_DEVICES"
        android:usesPermissionFlags="neverForLocation"
        tools:targetApi="33" />

</manifest>
```

#### [](#runtime-permission-request)Runtime Permission Request

On Android 12 (API 31) and higher, your application must request `BLUETOOTH_SCAN`, `BLUETOOTH_ADVERTISE`, and `BLUETOOTH_CONNECT` at runtime before starting the Multipeer Replicator. On Android 11 (API 30) and lower, your application must request `ACCESS_FINE_LOCATION` at runtime.

On Android 13 (API 33) and higher, your application must also request `NEARBY_WIFI_DEVICES` at runtime for Wi-Fi peer discovery.

> [!CAUTION]
> On Android 13 (API 33) and higher, the runtime permission prompt is labelled **Nearby devices**, not Bluetooth. You must still explicitly request `BLUETOOTH_SCAN`, `BLUETOOTH_ADVERTISE`, and `BLUETOOTH_CONNECT` at runtime on these devices. Declaring permissions in the manifest alone is not sufficient: Android 13+ devices will not show a prompt and BLE sync will not work.

Requesting Bluetooth permissions at runtime

```kotlin
private val requestPermissions =
    registerForActivityResult(ActivityResultContracts.RequestMultiplePermissions()) {}

private fun requestMissingPermissions() {
    val needed = buildList {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
            add(Manifest.permission.BLUETOOTH_SCAN)
            add(Manifest.permission.BLUETOOTH_ADVERTISE)
            add(Manifest.permission.BLUETOOTH_CONNECT)
        } else {
            add(Manifest.permission.ACCESS_FINE_LOCATION)
        }
        // On Android 13 (API 33) and higher, also request Wi-Fi peer discovery.
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
            add(Manifest.permission.NEARBY_WIFI_DEVICES)
        }
    }.filter {
        ContextCompat.checkSelfPermission(this, it) != PackageManager.PERMISSION_GRANTED
    }

    if (needed.isNotEmpty()) {
        requestPermissions.launch(needed.toTypedArray())
    }
}
```

> [!TIP]
> If you have already created a `MultipeerReplicator`, you can call `getNecessaryPermissions()` on it to get the exact set of runtime permissions required for its configured transports, rather than listing them manually.

## [](#configuration)Configuration

The `MultipeerReplicator` requires several configuration components to establish secure peer-to-peer replication between devices. This section covers the key configurations you need to set up:

### [](#collection-configurations)Collection Configurations

You can specify one or more collections available for replication when creating a `MultipeerReplicatorConfiguration`.

For each collection, you'll create `MultipeerCollectionConfiguration` with the collection object and optionally configure a custom conflict resolver or any replication filters you want to use for the collection.

Specify collections without any configurations

```kotlin
val collections = mutableSetOf<MultipeerCollectionConfiguration>()
for(col in listOf(collection1, collection2, collection3)) {
    val builder = MultipeerCollectionConfiguration.Builder(col)
    collections.add(builder.build())
}
```

Specify collections with some configuration

```kotlin

// Config with custom conflict resolver
val config1 = MultipeerCollectionConfiguration.Builder(collection1)
    .setConflictResolver { peerId, conflict -> conflict.remoteDocument }
    .build()

// Config with document IDs filter
val config2 = MultipeerCollectionConfiguration.Builder(collection2)
    .setDocumentIDs(setOf("doc1", "doc2"))
    .build()

// Config with push replication filter
val config3 = MultipeerCollectionConfiguration.Builder(collection3)
    .setPushFilter { peerId, document, flags -> document.getInt("access-level") == 2 }
    .build()

val collections = setOf(config1, config2, config3)
```

### [](#peer-identity)Peer Identity

Each peer in the Multipeer replication is uniquely identified and authenticated by using a peer's certificate.

Multipeer Replicator which uses TLS communication by default requires to specify a `TLSIdentity` object for specifying the identity.

You can use either a self-signed certificate for the identity or have an authority or issuer sign the identity's certificate. The choice depends on your specific security requirements and deployment environment.

As each peer could be either a client or a server to the other peer in the Multipeer replication environment, you must create the identity's certificate with the extension key usages for both client and server authentication to allow either direction to authenticate the certificate.

#### [](#ca-signed-identity)CA-Signed Identity

When using a certificate authority (CA) signed identity, the issuer's certificate authenticates the connecting peer.

Get and Create an identity signed by an issuer

```kotlin
// NOTE: Error handling omitted

val persistentLabel = "com.myapp.identity"

// Retrieve the TLS identity from the key store using the persistent label.
var identity = TLSIdentity.getIdentity(persistentLabel)

// If the identity exists but is expired, delete it.
if(identity != null && identity.expiration.before(Date())) {
    // NOTE: Important to delete identity this way for CA signed identities
    // since they extend beyond the Android key store
    TLSIdentity.deleteIdentity(persistentLabel)
}

if(identity == null) {
    // Define certificate attributes and expiration date.
    val certAttributes = mapOf(
        TLSIdentity.CERT_ATTRIBUTE_COMMON_NAME to "Couchbase Demo",
        TLSIdentity.CERT_ATTRIBUTE_ORGANIZATION to "Couchbase",
        TLSIdentity.CERT_ATTRIBUTE_ORGANIZATION_UNIT to "Mobile",
        TLSIdentity.CERT_ATTRIBUTE_EMAIL_ADDRESS to "noreply@couchbase.com"
    )

    val calendar = Calendar.getInstance()
    calendar.add(Calendar.YEAR, 2)
    val expiration = calendar.time

    val caKey = getCAPrivateKeyData()
    val caCert = getCACertificateData()

    // As the function name indicates, this is not a secure way of doing things
    // and should either be done for testing only, or in an environment that you
    // assure to be secure against unknown actors, because otherwise anyone who
    // can install the app can probably easily extract the CA key.
    identity = TLSIdentity.createdSignedIdentityInsecure(
        setOf(KeyUsage.SERVER_AUTH, KeyUsage.CLIENT_AUTH),
        certAttributes,
        caKey,
        caCert,
        expiration,
        persistentLabel
    )
}
```

#### [](#self-signed-identity)Self-Signed Identity

For environments where certificate authority management is not feasible, you can implement peer identity using self-signed certificates. This approach is commonly used in closed network environments where devices need to authenticate with each other without external certificate authorities.

Creating a self-signed identity for peer authentication

```kotlin
// NOTE: Error handling omitted

val persistentLabel = "com.myapp.identity"

// Retrieve the TLS identity from the key store using the persistent label.
var identity = TLSIdentity.getIdentity(persistentLabel)

// If the identity exists but is expired, delete it.
if(identity != null && identity.expiration.before(Date())) {
    TLSIdentity.deleteIdentity(persistentLabel)
}

if(identity == null) {
    // Define certificate attributes and expiration date.
    val certAttributes = mapOf(
        TLSIdentity.CERT_ATTRIBUTE_COMMON_NAME to "Couchbase Demo",
        TLSIdentity.CERT_ATTRIBUTE_ORGANIZATION to "Couchbase",
        TLSIdentity.CERT_ATTRIBUTE_ORGANIZATION_UNIT to "Mobile",
        TLSIdentity.CERT_ATTRIBUTE_EMAIL_ADDRESS to "noreply@couchbase.com"
    )

    val calendar = Calendar.getInstance()
    calendar.add(Calendar.YEAR, 2)
    val expiration = calendar.time

    identity = TLSIdentity.createIdentity(
        setOf(KeyUsage.CLIENT_AUTH, KeyUsage.SERVER_AUTH),
        certAttributes,
        expiration,
        persistentLabel
    )
}
```

When using self-signed certificates, implement your own certificate validation logic in the authenticator callback to make sure only trusted peers can join your mesh network.

### [](#peer-authenticator)Peer Authenticator

`MultipeerReplicator` only supports certificate based authentication. You can specify the authenticator in two ways:

* certificate authentication callback
* root certificates.

When specifying the certificate authentication callback, the callback calls the remote peer's identity certificate.

When specifying the root certificates, the Multipeer replicator automatically authenticates the remote peer's identity certificate by verifying whether one of the specified root certificates signed the certificate.

Authenticator with authentication callback

```kotlin
// Use peer and certs to decide whether or not to allow (true) this peer
// or reject (false)
val authenticator = MultipeerCertificateAuthenticator { peer, certs -> true }
```

Authenticator with root certificates

```kotlin
val caCert = getCACertificateData()
val certificateFactory = CertificateFactory.getInstance("X.509")
val inputStream = ByteArrayInputStream(caCert)
val certObject = certificateFactory.generateCertificate(inputStream) as X509Certificate
val authenticator = MultipeerCertificateAuthenticator(listOf(certObject))
```

### [](#transports)Transports

The `transports` property on `MultipeerReplicatorConfiguration` controls which transports the replicator uses for peer discovery and replication. The default is Wi-Fi only.

To enable Bluetooth Low Energy alongside Wi-Fi, add `MultipeerTransport.BLUETOOTH` to the transports set.

Default (Wi-Fi only)

```kotlin
// Wi-Fi is the default transport. No additional configuration is required.
val config = MultipeerReplicatorConfiguration.Builder()
    .setPeerGroupID("com.myapp")
    .setIdentity(identity)
    .setAuthenticator(authenticator)
    .setCollections(collections)
    .build()
// transports defaults to EnumSet.of(MultipeerTransport.WIFI)
```

Wi-Fi and Bluetooth

```kotlin
val config = MultipeerReplicatorConfiguration.Builder()
    .setPeerGroupID("com.myapp")
    .setIdentity(identity)
    .setAuthenticator(authenticator)
    .setCollections(collections)
    .setTransports(EnumSet.of(MultipeerTransport.WIFI, MultipeerTransport.BLUETOOTH))
    .build()
```

> [!NOTE]
> Bluetooth has lower throughput and higher latency than Wi-Fi, and its reliability can decrease as more peers join the Bluetooth network. We recommend using Wi-Fi as the primary transport for multipeer sync, with Bluetooth as a fallback, rather than relying on Bluetooth alone.

Bluetooth only

```kotlin
val config = MultipeerReplicatorConfiguration.Builder()
    .setPeerGroupID("com.myapp")
    .setIdentity(identity)
    .setAuthenticator(authenticator)
    .setCollections(collections)
    .setTransports(EnumSet.of(MultipeerTransport.BLUETOOTH))
    .build()
```

When you enable both transports, the replicator automatically selects the best available transport for each peer and switches between them as reachability changes. See [Automatic Transport Switching](#automatic-transport-switching).

### [](#create-multipeerreplicatorconfiguration)Create MultipeerReplicatorConfiguration

The `MultipeerReplicatorConfiguration` can be created with a `peerGroupID` which is an identifier that identifies the peer-to-peer network used by the app, collection configurations, peer identity, and authenticator.

Creating MultipeerReplicatorConfiguration

```kotlin
val config = MultipeerReplicatorConfiguration.Builder()
    .setPeerGroupID("com.myapp")
    .setIdentity(identity)
    .setAuthenticator(authenticator)
    .setCollections(collections)
    .build()
```

> [!TIP]
> Performance may vary in mesh networks depending on your specific environment and number of peers. We recommend running tests with your network configuration to assess any effects on packet loss or latency.

## [](#automatic-transport-switching)Automatic Transport Switching

When `MultipeerReplicator` is configured with both Wi-Fi and Bluetooth transports, it automatically selects the best available transport for each peer and switches transports as reachability changes.

### [](#transport-preference)Transport Preference

The replicator prefers Wi-Fi over Bluetooth when both transports can reach a peer. Bluetooth acts as a fallback when Wi-Fi cannot reach a peer.

### [](#fallback-to-bluetooth)Fallback to Bluetooth

For an individual peer, `MultipeerReplicator` falls back to Bluetooth when the peer is no longer reachable over Wi-Fi. This can occur if the peer disables Wi-Fi, becomes unreachable on the local network, or if replication over Wi-Fi fails because of a network-related error.

In cases of connection or replication failure over Wi-Fi, `MultipeerReplicator` performs a small number of retries before falling back to Bluetooth.

### [](#return-to-wi-fi)Return to Wi-Fi

If a peer becomes reachable over Wi-Fi while replication is active over Bluetooth, `MultipeerReplicator` establishes a Wi-Fi connection in parallel with the existing Bluetooth connection. The Bluetooth connection remains active until the Wi-Fi connection is fully established and replication has resumed over Wi-Fi. This prevents any interruption in synchronization during the transition.

## [](#life-cycle)Life Cycle

### [](#create-multipeerreplicator-with-configuration)Create MultipeerReplicator with Configuration

Creating MultipeerReplicator

```kotlin
val replicator = MultipeerReplicator(config)
```

### [](#start)Start

Starting MultipeerReplicator

```kotlin
replicator.start()
```

### [](#stop)Stop

Stopping MultipeerReplicator

```kotlin
replicator.stop()
```

### [](#background-behavior)Background Behavior

The `MultipeerReplicator` supports continuous mode, which allows it to operate in the background.

When the application is put into the background, the `MultipeerReplicator` will continue to operate in the background.

You should make sure that the application has the necessary permissions to run in the background and configure the `MultipeerReplicator` to support background operations.

### [](#events)Events

In general, the connection should just work, and most of these optional listen events give status you may only want to use during development and testing.

Status events include a `transport` property that identifies which transport the event applies to. `MultipeerReplicatorStatus` events are delivered per enabled transport and also as an aggregated status (where `transport` is `null`) representing the overall replicator state.

Event types include the following:

#### [](#multipeer-replicator-status)Multipeer Replicator Status

Multipeer Replicator Status Listener

```kotlin
val token = replicator.addStatusListener { status ->
    val state = if(status.isActive) "active" else "inactive"
    val error = status.error?.message ?: "none"
    Log.i(TAG, "Multipeer replicator: $state, Error: $error")
}
```

#### [](#peer-discovery-status)Peer Discovery Status

Peer Discovery Status Listener

```kotlin
val token = replicator.addPeerDiscoveryStatusListener { status ->
    val online = if(status.isOnline) "online" else "offline"
    Log.i(TAG, "Peer Discovery Status - Peer ID: ${status.peer}, Status: $online")
}
```

#### [](#peers-replicator-status)Peer's Replicator Status

Peer's Replicator Status Listener

```kotlin
//val activities = ["stopped", "offline", "connecting", "idle", "busy"]
val token = replicator.addPeerReplicatorStatusListener { status ->
    val direction = if(status.isOutgoing) "outgoing" else "incoming"
    val activity = status.status.activityLevel.name.lowercase()
    val error = status.status.error?.message ?: "none"
    Log.i(TAG, "Peer Replicator Status - Peer ID: $status, " +
            "Direction: $direction, " +
            "Activity: $activity" +
            "Error: $error")
}
```

#### [](#peers-document-replication)Peer's Document Replication

Peer's Document Replication Listener

```kotlin
val token = replicator.addPeerDocumentReplicationListener { status ->
    val direction = if(status.isPush) "push" else "pull"
    Log.i(TAG, "Peer Document Replication - Peer ID: ${status.peer}, Direction: $direction")
    for(doc in status.documents) {
        val error = doc.error?.message ?: "none"
        val collection = "${doc.scope}.${doc.collection}"
        Log.i(TAG, " Collection: $collection, Document ID: ${doc.id}, " +
                "Flags: ${doc.flags}, Error: $error")
    }
}
```

## [](#peer-info)Peer Info

### [](#peer-identifier)Peer Identifier

A unique `peerID`, which is a digest of the peer's identity certificate, identifies each peer. You can get your `peerID` from the `peerID` property of the `MultipeerReplicator`.

Getting peer ID

```kotlin
val peerID = replicator.peerId
Log.i(TAG, "Peer ID: $peerID")
```

### [](#neighbor-peers)Neighbor Peers

You can get a list of current online peers' Identifiers from the `MultipeerReplicator` from the `neighborPeers` property.

Getting neighbor peers

```kotlin
Log.i(TAG, "Neighbor Peers:")
replicator.neighborPeers.forEach { peer -> Log.i(TAG, " $peer") }
```

### [](#peer-info-2)Peer Info

The `PeerInfo` object provides information about a peer, including its identifier, certificate, online status, replicator status, neighbor peers, the transports on which the peer was discovered, and the transport currently used for replication.

Getting peer info

```kotlin
fun printPeerInfo(info: PeerInfo) {
    Log.i(TAG, "Peer ID: ${info.peerId}")
    Log.i(TAG, " Status: ${if(info.isOnline) "online" else "offline"}")
    Log.i(TAG, " Neighbor Peers:")
    info.neighbors.forEach { peer -> Log.i(TAG, " $peer") }

    val replStatus = info.replicatorStatus
    val activity = replStatus.activityLevel.name.lowercase()
    val error = replStatus.error?.message ?: "none"
    Log.i(TAG, " Replicator Status: $activity, Error: $error")
}

for(peer in replicator.neighborPeers) {
    replicator.getPeerInfo(peer)?.let { printPeerInfo(it) }
}
```

## [](#lbl-testing)Testing

### [](#testing-device-requirements)Device Requirements

The Multipeer Replicator requires physical devices for end-to-end testing. Android emulators and iOS simulators do not support Bluetooth Low Energy. Test on real devices connected to the same Wi-Fi network for Wi-Fi transport, or in close physical proximity for Bluetooth.

### [](#testing-isolating-ble)Isolating the Bluetooth Path

To verify that BLE transport is working independently of Wi-Fi:

1. Enable airplane mode on both test devices to disable Wi-Fi.
2. Re-enable Bluetooth on both devices (airplane mode allows this on both Android and iOS).
3. Start the Multipeer Replicator on both devices.
4. Confirm replication completes using the BLE transport only.

This approach removes any ambiguity about which transport is carrying the data.

### [](#testing-android-doze)Android Doze Mode

Android Doze mode can silently suspend background network activity, including Multipeer Replication, when a device is idle. During testing, keep the screen on or disable battery optimization for your test application to prevent Doze from interfering with replication. In production, see [Background Behavior](#background-behavior) for configuration guidance.

## [](#logging)Logging

`LogDomain` sets up the logging of:

1. Peer discovery log messages
2. Multipeer replication and mesh network management log messages

```kotlin
// Enable verbose console logging for multipeer replicator-related domains only.
LogSinks.get().console = ConsoleLogSink(LogLevel.VERBOSE, LogDomain.PEER_DISCOVERY,
    LogDomain.MULTIPEER)
```

## [](#api-reference)API Reference

You can find [Kotlin API References](https://docs.couchbase.com/mobile/4.1.{maintenance-kotlin}/couchbase-lite-kotlin) here.