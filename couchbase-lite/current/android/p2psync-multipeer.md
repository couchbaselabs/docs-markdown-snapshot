---
title: Multipeer P2P Replicator
description: The Multipeer Replicator enables lightweight, self-organizing mesh
  networks for apps running on the same local Wi-Fi.
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/android/pages/p2psync-multipeer.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:couchbase-lite:android:p2psync-multipeer.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/android/p2psync-multipeer.html)

# Multipeer P2P Replicator

> The Multipeer Replicator enables lightweight, self-organizing mesh networks for apps running on the same local Wi-Fi. This approach requires minimal setup and automates peer discovery and connectivity management, making it simpler than [active-passive P2P configurations](p2psync-websocket.md). 

## [](#introduction)Introduction

Couchbase Lite's Peer-to-Peer synchronization solution offers secure storage and bidirectional data synchronization between mobile and IoT devices without needing a centralized cloud-based control point.

For small mesh topologies, Multipeer Replicator offers `autodiscovery` for Wi-Fi-based networks and secure communication via TLS and certificate-based authentication.

The dynamic mesh topology gives optimal peer connectivity and the lightweight and low-maintenance configuration requires less management and less code than using active-passive peer-to-peer sync.

## [](#overview)Overview

To maintain optimal connectivity, efficient data transport, and balanced workloads, the Multipeer Replicator forms a dynamic mesh network among peers in the same group. The mesh network provides resilience through multiple communication pathways - if one connection fails, data can flow through alternative routes.

It avoids redundant direct connections, evenly distributes connections across peers, and optimizes communication paths through intelligent routing.

The mesh network continuously adapts as peers join or leave, automatically healing itself by establishing new connections and rerouting data flow to maintain network integrity.

This self-organizing approach ensures reliable data synchronization even in challenging network conditions, where individual peer connections may be intermittent or unreliable.

Multipeer Replicator supports Wi-Fi (IP-based transport) as of CBL 3.3.

## [](#prerequisites)Prerequisites

### [](#transport-and-peer-discovery-protocol)Transport and Peer Discovery Protocol

Multipeer Replicator supports Wi-Fi transport, using `DNS-SD` (also known as Bonjour) for peer discovery. Peers connect to the same Wi-Fi network to discover and establish connections with one another.

### [](#supported-platforms)Supported Platforms

For Android, we recommend using a recent release, preferably supporting minimum API level 24, or more recent but earlier versions should work with the multipeer sync feature. See [Supported Platforms](#kotlin:supported-os.adoc) for more details.

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

In general, the connection should just work, and most of these optional listen events give status you may only want to use during development and testing. Event types include the following:

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
    printPeerInfo(replicator.getPeerInfo(peer))
}
```

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

You can find [Kotlin API References](https://docs.couchbase.com/mobile/4.0.{maintenance-kotlin}/couchbase-lite-kotlin) here.