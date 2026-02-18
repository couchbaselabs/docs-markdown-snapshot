---
title: Multipeer P2P Replicator
description: The Multipeer Replicator enables lightweight, self-organizing mesh
  networks for apps running on the same local Wi-Fi.
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/swift/pages/p2psync-multipeer.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/couchbase-lite/current/swift/p2psync-multipeer.html)

# Multipeer P2P Replicator

> The Multipeer Replicator enables lightweight, self-organizing mesh networks for apps running on the same local Wi-Fi. This approach requires minimal setup and automates peer discovery and connectivity management, making it simpler than [active-passive P2P configurations](p2psync-websocket.md). 

Couchbase Lite’s Peer-to-Peer synchronization solution offers secure storage and bidirectional data synchronization between mobile and IoT devices without needing a centralized cloud-based control point.

For small mesh topologies, Multipeer Replicator offers `autodiscovery` for Wi-Fi-based networks and secure communication via TLS and certificate-based authentication. The dynamic mesh topology gives optimal peer connectivity and the lightweight and low-maintenance configuration requires less management and less code than using active-passive peer-to-peer sync.

## [](#overview)Overview

To maintain optimal connectivity, efficient data transport, and balanced workloads, the Multipeer Replicator forms a dynamic mesh network among peers in the same group. The mesh network provides resilience through multiple communication pathways - if one connection fails, data can flow through alternative routes. It avoids redundant direct connections, evenly distributes connections across peers, and optimizes communication paths through intelligent routing.

The mesh network continuously adapts as peers join or leave, automatically healing itself by establishing new connections and rerouting data flow to maintain network integrity.

This self-organizing approach ensures reliable data synchronization even in challenging network conditions, where individual peer connections may be intermittent or unreliable.

Multipeer Replicator supports Wi-Fi (IP-based transport) as of CBL 3.3.

## [](#prerequisites)Prerequisites

### [](#transport-and-peer-discovery-protocol)Transport and Peer Discovery Protocol

Multipeer Replicator supports Wi-Fi transport, using `DNS-SD` (also known as **Bonjour**) for peer discovery. You must connect Peers to the same Wi-Fi network to discover and establish connections with one another.

### [](#configuration-requirements)Configuration Requirements

To use `DNS-SD` for peer discovery, iOS apps must declare the **Bonjour** service type and request local network access permissions. Add the following keys to your app’s `Info.plist`:

#### [](#nsbonjourservices)NSBonjourServices

Declare the service type used by MultipeerReplicator:

```xml
<key>NSBonjourServices</key>
<array>
  <string>_couchbaseP2P._tcp</string>
</array>
```

#### [](#nslocalnetworkusagedescription)NSLocalNetworkUsageDescription

Add a usage description for local network access:

```xml
<key>NSLocalNetworkUsageDescription</key>
<string>Used for discovering and connecting to peers for peer-to-peer sync.</string>
```

> [!TIP]
> You can also configure these settings through Xcode’s Info configuration UI under "**Bonjour Services**" and "**Privacy – Local Network Usage Description**."

### [](#supported-platforms)Supported Platforms

We recommend using a recent release of iOS, see [Supported Platforms](supported-os.md) for details.

## [](#configuration)Configuration

### [](#collection-configurations)Collection Configurations

You can specify one or more collections available for replication when creating a `MultipeerReplicatorConfiguration`. For each collection, you’ll create `MultipeerCollectionConfiguration` with the collection object and optionally configure a custom conflict resolver or any replication filters you want to use for the collection.

Specify collections without any configurations

```swift
let collections = [collection1, collection2, collection3].map {
    MultipeerCollectionConfiguration(collection: $0)
}
```

Specify collections with some configuration

```swift
class CustomConflictResolver: MultipeerConflictResolver {
    func resolve(peerID: PeerID, conflict: Conflict) -> Document? {
        return conflict.remoteDocument
    }
}

// Create a collection config with a conflict resolver
var config1 = MultipeerCollectionConfiguration(collection: collection1)
config1.conflictResolver = CustomConflictResolver()

// Create a collection config with a document ID filter
var config2 = MultipeerCollectionConfiguration(collection: collection2)
config2.documentIDs = ["doc1", "doc2"]

// Create a collection config with a push replication filter
var config3 = MultipeerCollectionConfiguration(collection: collection3)
config3.pushFilter = { peerID, document, flags in
    return document.int(forKey: "access-level") == 2
}

let collections = [config1, config2, config3]
```

### [](#peer-identity)Peer Identity

Each peer in the Multipeer replication is uniquely identified and authenticated by using a peer’s certificate.

Multipeer Replicator which uses TLS communication by default requires to specify a `TLSIdentity` object for specifying the identity.

You can use either a self-signed certificate for the identity or have an authority or issuer sign the identity’s certificate. The choice depends on your specific security requirements and deployment environment.

As each peer could be either a client or a server to the other peer in the Multipeer replication environment, you must create the identity’s certificate with the extension key usages for both client and server authentication to allow either direction to authenticate the certificate.

#### [](#ca-signed-identity)CA-Signed Identity

When using a certificate authority (CA) signed identity, the issuer’s certificate authenticates the connecting peer.

Get and Create an identity signed by an issuer

```swift
let persistentLabel = "com.myapp.identity"

// Retrieve the TLS identity from the keychain using the persistent label.
var identity = try TLSIdentity.identity(withLabel: persistentLabel)

// If the identity exists but is expired, delete it.
if let existing = identity, existing.expiration < Date() {
    try TLSIdentity.deleteIdentity(withLabel: persistentLabel)
    identity = nil
}

// If the identity doesn't exist or expired, create a new one.
if identity == nil {
    // Define certificate attributes and expiration date.
    let attrs: [String: String] = [certAttrCommonName: "MyApp"]
    let expiration = Calendar.current.date(byAdding: .year, value: 2, to: Date())!

    // Get issuer's private key and certificate data (DER format) for signing the identity's certificate.
    let caKey = try getIssuerPrivateKeyData()
    let caCert = try getIssuerCertificateData()
    
    // Create and store a new identity signed with the issuer in the keychain with a persistent label.
    identity = try TLSIdentity.createSignedIdentityInsecure(
        for: [.clientAuth, .serverAuth],
        attributes: attrs,
        expiration: expiration,
        caKey: caKey,
        caCertificate: caCert,
        label: persistentLabel)
}
```

#### [](#self-signed-identity)Self-Signed Identity

For environments where certificate authority management is not feasible, you can implement peer identity using self-signed certificates. This approach is commonly used in closed network environments where devices need to authenticate with each other without external certificate authorities.

Creating a self-signed identity for peer authentication

```swift
let persistentLabel = "com.myapp.identity"

// Retrieve the TLS identity from the keychain using the persistent label.
var identity = try TLSIdentity.identity(withLabel: persistentLabel)

// If the identity exists but is expired, delete it.
if let existing = identity, existing.expiration < Date() {
    try TLSIdentity.deleteIdentity(withLabel: persistentLabel)
    identity = nil
}

// If the identity doesn't exist or expired, create a new one.
if identity == nil {
    // Define certificate attributes and expiration date.
    let attrs: [String: String] = [certAttrCommonName: "MyApp"]
    let expiration = Calendar.current.date(byAdding: .year, value: 2, to: Date())!
    
    // Create and store a new self-signed identity in the keychain with a persistent label.
    identity = try TLSIdentity.createIdentity(
        for: [.clientAuth, .serverAuth],
        attributes: attrs,
        expiration: expiration,
        label: persistentLabel)
}
```

When using self-signed certificates, implement your own certificate validation logic in the authenticator callback to make sure only trusted peers can join your mesh network.

### [](#peer-authenticator)Peer Authenticator

MultpeerReplicator only supports certificate based authentication. You can specify the authenticator in two ways:

* certificate authentication callback
* root certificates.

When specifying the certificate authentication callback, the callback calls the remote peer’s identity certificate.

When specifying the root certificates, the Multipeer replicator automatically authenticates the remote peer’s identity certificate by verifying whether one of the specified root certificates signed the certificate.

Authenticator with authentication callback

```swift
let authenticator = MultipeerCertificateAuthenticator { peerID, certs in
    return true
}
```

Authenticator with root certificates

```swift
// Get issuer's certificate data (DER format), which was used to sign the peer's certificate.
let caCert = try getIssuerCertificateData()
let caCertRef = SecCertificateCreateWithData(nil, caCert as CFData)!
let authenticator = MultipeerCertificateAuthenticator(rootCerts: [caCertRef])
```

### [](#create-multipeerreplicatorconfiguration)Create MultipeerReplicatorConfiguration

The `MultipeerReplicatorConfiguration` can be created with a `peerGroupID` which is an identity identifies the Peer-to-peer network used by the app, collection configurations, peer identity, and authenticator.

Creating MultipeerReplicatorConfiguration

```swift
let config = MultipeerReplicatorConfiguration(
    peerGroupID: "com.myapp",
    identity: identity,
    authenticator: authenticator,
    collections: collections)
```

> [!TIP]
> Performance may vary in mesh networks depending on your specific environment and number of peers. We recommend running tests with your network configuration to assess any effects on packet loss or latency.

## [](#life-cycle)Life Cycle

### [](#create-multipeerreplicator-with-configuration)Create MultipeerReplicator with Configuration

Creating MultipeerReplicator

```swift
let replicator = try MultipeerReplicator(config: config)
```

### [](#start)Start

Starting MultipeerReplicator

```swift
replicator.start()
```

### [](#stop)Stop

Stopping MultipeerReplicator

```swift
replicator.stop()
```

### [](#events)Events

In general, the connection should just work, and most of these optional listen events give status you may only want to use during development and testing. Event types include the following:

#### [](#multipeer-replicator-status)Multipeer Replicator Status

Multipeer Replicator Status Listener

```swift
let token = replicator.addStatusListener { status in
    let state = status.active ? "active" : "inactive"
    let error = status.error?.localizedDescription ?? "none"
    print("Multipeer Replicator: \(state), Error: \(error)")
}
```

#### [](#peer-discovery-status)Peer Discovery Status

Peer Discovery Status Listener

```swift
let token = replicator.addPeerDiscoveryStatusListener { status in
    let online = status.online ? "online" : "offline"
    print("Peer Discovery Status - Peer ID: \(status.peerID), Status: \(online)")
}
```

#### [](#peers-replicator-status)Peer’s Replicator Status

Peer’s Replicator Status Listener

```swift
let activities = ["stopped", "offline", "connecting", "idle", "busy"]
let token = replicator.addPeerReplicatorStatusListener { replStatus in
    let direction = replStatus.outgoing ? "outgoing" : "incoming"
    let activity = activities[Int(replStatus.status.activity.rawValue)]
    let error = replStatus.status.error?.localizedDescription ?? "none"
    print("Peer Replicator Status - Peer ID: \(replStatus.peerID), " +
          "Direction: \(direction), " +
          "Activity: \(activity), " +
          "Error: \(error)")
}
```

#### [](#peers-document-replication)Peer’s Document Replication

Peer’s Document Replication Listener

```swift
let token = replicator.addPeerDocumentReplicationListener { docRepl in
    let direction = docRepl.isPush ? "Push" : "Pull"
    print("Peer Document Replication - Peer ID: \(docRepl.peerID), Direction: \(direction)")
    docRepl.documents.forEach { doc in
        let error = doc.error?.localizedDescription ?? "none"
        let collection = "\(doc.scope).\(doc.collection)"
        print(" Collection: \(collection)" +
              " Document ID: \(doc.id)," +
              " Flags: \(doc.flags)," +
              " Error: \(error)")
    }
}
```

## [](#peer-info)Peer Info

### [](#peer-identifier)Peer Identifier

A unique `peerID`, which is a digest of the peer’s identity certificate, identifies each peer. You can get your `peerID` from the `peerID` property of the `MultipeerReplicator`.

Getting peer ID

```swift
let peerID = replicator.peerID
print("Peer ID: \(peerID)")
```

### [](#neighbor-peers)Neighbor Peers

You can get a list of current online peers' Identifiers from the `MultipeerReplicator` from the `neighborPeers` property.

Getting neighbor peers

```swift
print("Neighbor Peers:")
replicator.neighborPeers.forEach { peerID in
    print(" \(peerID)")
}
```

### [](#peer-info-2)Peer Info

Getting peer info

```swift
let activities = ["stopped", "offline", "connecting", "idle", "busy"]

let printPeerInfo: (PeerInfo) -> Void = { info in
    print("Peer ID: \(info.peerID)")
    print(" Status: \(info.online ? "online" : "offline")")
    print(" Neighbor Peers:")
    info.neighborPeers.forEach { peerID in
        print("  \(peerID)")
    }

    let replStatus = info.replicatorStatus
    let activity = activities[Int(replStatus.activity.rawValue)]
    let error = replStatus.error?.localizedDescription ?? "none"
    print(" Replicator Status: \(activity), Error: \(error)")
}

replicator.neighborPeers.forEach { peerID in
    if let peerInfo = replicator.peerInfo(for: peerID) {
        printPeerInfo(peerInfo)
    }
}
```

## [](#logging)Logging

`LogDomain` sets up the logging of:

1. Peer discovery log messages
2. Multipeer replication and mesh network management log messages

```swift
// Enable verbose console logging for multipeer replicator-related domains only.
LogSinks.console = ConsoleLogSink(level: .verbose, domains: [.peerDiscovery, .multipeer])
```

## [](#api-reference)API Reference

You can find [Swift API References](https://docs.couchbase.com/mobile/4.0.1/couchbase-lite-swift) here.