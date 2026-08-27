---
title: Multipeer P2P Replicator
description: The Multipeer Replicator enables lightweight, self-organizing mesh
  networks over Wi-Fi and Bluetooth Low Energy.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.1/modules/objc/pages/p2psync-multipeer.adoc
  xref: xref:couchbase-lite:objc:p2psync-multipeer.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/objc/p2psync-multipeer.html)

# Multipeer P2P Replicator

> The Multipeer Replicator enables lightweight, self-organizing mesh networks over Wi-Fi and Bluetooth Low Energy. This approach requires minimal setup and automates peer discovery and connectivity management, making it simpler than [active-passive P2P configurations](p2psync-websocket.md). 

## [](#introduction)Introduction

Couchbase Lite's Peer-to-Peer synchronization solution offers secure storage and bidirectional data synchronization between mobile and IoT devices without needing a centralized cloud-based control point.

For small mesh topologies, Multipeer Replicator offers autodiscovery over Wi-Fi and Bluetooth Low Energy, with secure communication via TLS and certificate-based authentication. The dynamic mesh topology gives optimal peer connectivity and the lightweight and low-maintenance configuration requires less management and less code than using active-passive peer-to-peer sync.

## [](#overview)Overview

To maintain optimal connectivity, efficient data transport, and balanced workloads, the Multipeer Replicator forms a dynamic mesh network among peers in the same group. The mesh network provides resilience through multiple communication pathways. If one connection fails, data can flow through alternative routes. It avoids redundant direct connections, evenly distributes connections across peers, and optimizes communication paths through intelligent routing.

The mesh network continuously adapts as peers join or leave, automatically healing itself by establishing new connections and rerouting data flow to maintain network integrity.

This self-organizing approach ensures reliable data synchronization even in challenging network conditions, where individual peer connections may be intermittent or unreliable.

## [](#prerequisites)Prerequisites

The Multipeer Replicator supports two transports for peer discovery and replication: Wi-Fi and Bluetooth Low Energy (BLE). Wi-Fi is enabled by default. The enabled transports are configured through the replicator configuration. See [Transports](#transports).

### [](#transport-support)Transport Support

__Table 1\. Transport support__
| Transport            | Available from | Discovery                    | Notes                                                                                                                                                                                       |
| -------------------- | -------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Wi-Fi                | CBL 3.3        | DNS-SD (Bonjour)             | Peers must connect to the same Wi-Fi network. Requires NSBonjourServices and NSLocalNetworkUsageDescription in Info.plist. See [Bluetooth Platform Configuration](#platform-configuration). |
| Bluetooth Low Energy | CBL 4.1        | BLE advertising and scanning | Requires NSBluetoothAlwaysUsageDescription in Info.plist. See [Bluetooth Platform Configuration](#platform-configuration).                                                                  |

> [!NOTE]
> When you configure both transports, the Multipeer Replicator automatically selects the best available transport for each peer and switches between them as reachability changes, preferring Wi-Fi over Bluetooth. See [Automatic Transport Switching](#automatic-transport-switching).

### [](#supported-platforms)Supported Platforms

__Table 2\. iOS version requirements__
| Feature                                   | Minimum iOS |
| ----------------------------------------- | ----------- |
| Couchbase Lite general support            | iOS 15      |
| Multipeer Replicator: Wi-Fi transport     | iOS 15      |
| Multipeer Replicator: Bluetooth transport | iOS 15      |

See [Bluetooth Platform Configuration](#platform-configuration) for the required `Info.plist` keys.

See [Supported Platforms](supported-os.md) for the full platform support matrix.

### [](#platform-configuration)Bluetooth Platform Configuration

This section applies only if your application enables Bluetooth transport. Applications that use Wi-Fi only do not require these keys.

iOS applications must declare the required keys in `Info.plist` for each transport they enable. You can also configure these settings through Xcode's Info configuration UI.

#### [](#wi-fi-transport)Wi-Fi Transport

To use Wi-Fi transport, declare the Bonjour service type and a local network usage description.

NSBonjourServices

```xml
<key>NSBonjourServices</key>
<array>
  <string>_couchbaseP2P._tcp</string>
</array>
```

NSLocalNetworkUsageDescription

```xml
<key>NSLocalNetworkUsageDescription</key>
<string>Used for discovering and connecting to peers for peer-to-peer sync.</string>
```

#### [](#bluetooth-transport)Bluetooth Transport

To use Bluetooth transport, declare a Bluetooth usage description.

NSBluetoothAlwaysUsageDescription

```xml
<key>NSBluetoothAlwaysUsageDescription</key>
<string>Used for discovering and connecting to peers for peer-to-peer sync.</string>
```

## [](#configuration)Configuration

### [](#collection-configurations)Collection Configurations

You can specify one or more collections available for replication when creating a `CBLMultipeerReplicatorConfiguration`. For each collection, you create `CBLMultipeerCollectionConfiguration` with the collection object and optionally configure a custom conflict resolver or any replication filters you want to use for the collection.

Specify collections without any configurations

```objc

```

Specify collections with some configuration

```objc

```

### [](#peer-identity)Peer Identity

Each peer in the Multipeer replication is uniquely identified and authenticated by using a peer's certificate.

Multipeer Replicator uses TLS communication by default and requires a `CBLTLSIdentity` object for specifying the identity.

You can use either a self-signed certificate for the identity or have an authority or issuer sign the identity's certificate. The choice depends on your specific security requirements and deployment environment.

As each peer could be either a client or a server to the other peer in the Multipeer replication environment, you must create the identity's certificate with the extension key usages for both client and server authentication to allow either direction to authenticate the certificate.

#### [](#ca-signed-identity)CA-Signed Identity

When using a certificate authority (CA) signed identity, the issuer's certificate authenticates the connecting peer.

Get and Create an identity signed by an issuer

```objc

```

#### [](#self-signed-identity)Self-Signed Identity

For environments where certificate authority management is not feasible, you can implement peer identity using self-signed certificates. This approach is commonly used in closed network environments where devices need to authenticate with each other without external certificate authorities.

Creating a self-signed identity for peer authentication

```objc

```

When using self-signed certificates, implement your own certificate validation logic in the authenticator callback to make sure only trusted peers can join your mesh network.

### [](#peer-authenticator)Peer Authenticator

`CBLMultipeerReplicator` only supports certificate based authentication. You can specify the authenticator in two ways:

* certificate authentication callback
* root certificates.

When specifying the certificate authentication callback, the callback receives the remote peer's identity certificate.

When specifying the root certificates, the Multipeer replicator automatically authenticates the remote peer's identity certificate by verifying whether one of the specified root certificates signed the certificate.

Authenticator with authentication callback

```objc

```

Authenticator with root certificates

```objc

```

### [](#transports)Transports

The `transports` property on `CBLMultipeerReplicatorConfiguration` controls which transports the replicator uses for peer discovery and replication.

The property type is `CBLMultipeerTransportSet`, an `NS_OPTIONS` bitmask. To enable Bluetooth Low Energy alongside Wi-Fi, combine the transport options with the bitwise OR operator.

#### [](#wi-fi-only)Wi-Fi Only

Wi-Fi is the default transport. Existing applications continue to operate on Wi-Fi only after upgrading to CBL 4.1 with no code changes required.

Default (Wi-Fi only)

```objc
// Wi-Fi is the default transport. No additional configuration is required.
CBLMultipeerReplicatorConfiguration *config =
[[CBLMultipeerReplicatorConfiguration alloc] initWithPeerGroupID:@"com.myapp"
    identity:identity
    authenticator:authenticator
    collections:collections];
// config.transports defaults to kCBLMultipeerTransportWifi
```

#### [](#bluetooth-only)Bluetooth Only

To use Bluetooth as the sole transport, set `transports` to `kCBLMultipeerTransportBluetooth`. Peers discover each other using BLE advertising and scanning rather than DNS-SD.

Bluetooth only

```objc
CBLMultipeerReplicatorConfiguration *config =
[[CBLMultipeerReplicatorConfiguration alloc] initWithPeerGroupID:@"com.myapp"
    identity:identity
    authenticator:authenticator
    collections:collections];
config.transports = kCBLMultipeerTransportBluetooth;
```

#### [](#wi-fi-and-bluetooth-with-automatic-switching)Wi-Fi and Bluetooth with Automatic Switching

To enable both transports, set `transports` to `kCBLMultipeerTransportWifi | kCBLMultipeerTransportBluetooth`. The replicator prefers Wi-Fi and falls back to Bluetooth automatically when Wi-Fi is unavailable. See [Automatic Transport Switching](#automatic-transport-switching).

Wi-Fi and Bluetooth

```objc
CBLMultipeerReplicatorConfiguration *config =
[[CBLMultipeerReplicatorConfiguration alloc] initWithPeerGroupID:@"com.myapp"
    identity:identity
    authenticator:authenticator
    collections:collections];
config.transports = kCBLMultipeerTransportWifi | kCBLMultipeerTransportBluetooth;
```

> [!NOTE]
> Bluetooth has lower throughput and higher latency than Wi-Fi, and its reliability can decrease as more peers join the Bluetooth network. We recommend using Wi-Fi as the primary transport for multipeer sync, with Bluetooth as a fallback, rather than relying on Bluetooth alone.

### [](#create-multipeerreplicatorconfiguration)Create MultipeerReplicatorConfiguration

The `CBLMultipeerReplicatorConfiguration` is created with a `peerGroupID` that identifies the peer-to-peer network used by the app, collection configurations, peer identity, and authenticator.

Creating MultipeerReplicatorConfiguration

```objc

```

> [!TIP]
> Performance may vary in mesh networks depending on your specific environment and number of peers. We recommend running tests with your network configuration to assess any effects on packet loss or latency.

## [](#automatic-transport-switching)Automatic Transport Switching

When `CBLMultipeerReplicator` is configured with both Wi-Fi and Bluetooth transports, it automatically selects the best available transport for each peer and switches transports as reachability changes.

### [](#transport-preference)Transport Preference

The replicator prefers Wi-Fi over Bluetooth when both transports can reach a peer. Bluetooth acts as a fallback when Wi-Fi cannot reach a peer.

### [](#fallback-to-bluetooth)Fallback to Bluetooth

For an individual peer, `CBLMultipeerReplicator` falls back to Bluetooth when the peer is no longer reachable over Wi-Fi. This can occur if the peer disables Wi-Fi, becomes unreachable on the local network, or if replication over Wi-Fi fails because of a network-related error.

In cases of connection or replication failure over Wi-Fi, `CBLMultipeerReplicator` performs a small number of retries before falling back to Bluetooth.

### [](#return-to-wi-fi)Return to Wi-Fi

If a peer becomes reachable over Wi-Fi while replication is active over Bluetooth, `CBLMultipeerReplicator` establishes a Wi-Fi connection in parallel with the existing Bluetooth connection. The Bluetooth connection remains active until the Wi-Fi connection is fully established and replication has resumed over Wi-Fi. This prevents any interruption in synchronization during the transition.

## [](#life-cycle)Life Cycle

### [](#create-multipeerreplicator-with-configuration)Create MultipeerReplicator with Configuration

Creating MultipeerReplicator

```objc

```

### [](#start)Start

Starting MultipeerReplicator

```objc

```

### [](#stop)Stop

Stopping MultipeerReplicator

```objc

```

### [](#events)Events

In general, the connection should just work, and most of these optional listen events give status you may only want to use during development and testing.

Status events include a `transport` property that identifies which transport the event applies to. `CBLMultipeerReplicatorStatus` events are delivered per enabled transport and also as an aggregated status (where `transport` is `nil`) representing the overall replicator state.

Event types include the following:

#### [](#multipeer-replicator-status)Multipeer Replicator Status

Multipeer Replicator Status Listener

```objc
[replicator addStatusListenerWithQueue:nil listener:^(CBLMultipeerReplicatorStatus *status) {
    // transport is nil for the aggregated overall status;
    // non-nil for a per-transport status update.
    NSString *transport = status.transport == nil ? @"all"
        : (status.transport.unsignedIntegerValue == kCBLMultipeerTransportWifi ? @"wifi" : @"bluetooth");
    NSString *state = status.active ? @"active" : @"inactive";
    NSString *err = status.error ? status.error.localizedDescription : @"none";
    NSLog(@"Multipeer Replicator [%@]: %@, Error: %@", transport, state, err);
}];
```

#### [](#peer-discovery-status)Peer Discovery Status

Peer Discovery Status Listener

```objc
[replicator addPeerDiscoveryStatusListenerWithQueue:nil listener:^(CBLPeerDiscoveryStatus *status) {
    NSString *online = status.online ? @"online" : @"offline";
    NSString *transport = (status.transport == kCBLMultipeerTransportWifi) ? @"wifi" : @"bluetooth";
    NSLog(@"Peer Discovery Status - Peer ID: %@, Transport: %@, Status: %@",
          status.peerID, transport, online);
}];
```

#### [](#peers-replicator-status)Peer's Replicator Status

Peer's Replicator Status Listener

```objc
NSArray<NSString *> *activities = @[ @"stopped", @"offline", @"connecting", @"idle", @"busy" ];
[replicator addPeerReplicatorStatusListenerWithQueue:nil listener:^(CBLPeerReplicatorStatus *replStatus) {
    NSString *direction = replStatus.outgoing ? @"outgoing" : @"incoming";
    NSString *activity = activities[replStatus.status.activity];
    NSString *transport = (replStatus.transport == kCBLMultipeerTransportWifi) ? @"wifi" : @"bluetooth";
    NSString *error = replStatus.status.error ? replStatus.status.error.localizedDescription : @"none";
    NSLog(@"Peer Replicator Status - "
          "Peer ID: %@, Transport: %@, Direction: %@, Activity: %@, Error: %@",
          replStatus.peerID, transport, direction, activity, error);
}];
```

#### [](#peers-document-replication)Peer's Document Replication

Peer's Document Replication Listener

```objc
[replicator addPeerDocumentReplicationListenerWithQueue:nil listener:^(CBLPeerDocumentReplication *docRepl) {
    NSString *direction = docRepl.isPush ? @"Push" : @"Pull";
    NSString *transport = (docRepl.transport == kCBLMultipeerTransportWifi) ? @"wifi" : @"bluetooth";
    NSLog(@"Peer Document Replication - Peer ID: %@, Transport: %@, Direction: %@",
          docRepl.peerID, transport, direction);
    for (CBLReplicatedDocument *doc in docRepl.documents) {
        NSString *error = doc.error ? doc.error.localizedDescription : @"none";
        NSString *collection = [NSString stringWithFormat:@"%@.%@", doc.scope, doc.collection];
        NSLog(@" Collection: %@ Document ID: %@, Flags: %lu, Error: %@",
            collection, doc.id, (unsigned long)doc.flags, error);
    }
}];
```

## [](#peer-info)Peer Info

### [](#peer-identifier)Peer Identifier

A unique `peerID`, which is a digest of the peer's identity certificate, identifies each peer. You can get your `peerID` from the `peerID` property of the `CBLMultipeerReplicator`.

Getting peer ID

```objc

```

### [](#neighbor-peers)Neighbor Peers

You can get a list of current online peers' identifiers from the `CBLMultipeerReplicator` using the `neighborPeers` property.

Getting neighbor peers

```objc

```

### [](#peer-info-2)Peer Info

The `CBLPeerInfo` object provides information about a peer, including its identifier, certificate, online status, replicator status, neighbor peers, the transports on which the peer was discovered, and the transport currently used for replication.

Getting peer info

```objc
NSArray<NSString *> *activities = @[ @"stopped", @"offline", @"connecting", @"idle", @"busy" ];

void (^printPeerInfo)(CBLPeerInfo *) = ^(CBLPeerInfo *info) {
    NSLog(@"Peer ID: %@", info.peerID);
    NSLog(@" Status: %@", info.online ? @"online" : @"offline");

    // transports: the set of transports on which this peer was discovered.
    NSMutableArray<NSString *> *transportNames = [NSMutableArray array];
    if ((info.transports & kCBLMultipeerTransportWifi) != 0) {
        [transportNames addObject:@"wifi"];
    }

    if ((info.transports & kCBLMultipeerTransportBluetooth) != 0) {
        [transportNames addObject:@"bluetooth"];
    }

    // replicatorTransport: the transport currently used for replication.
    // The value is kCBLMultipeerTransportWifi or kCBLMultipeerTransportBluetooth,
    // or 0 if replication is not active.
    NSString *replicatorTransport = (info.replicatorTransport == kCBLMultipeerTransportWifi) ? @"wifi"
        : (info.replicatorTransport == kCBLMultipeerTransportBluetooth) ? @"bluetooth"
        : @"none";
    NSLog(@" Replicating on: %@", replicatorTransport);

    NSLog(@" Neighbor Peers:");
    for (CBLPeerID *peerID in info.neighborPeers) {
        NSLog(@"  %@", peerID);
    }

    CBLReplicatorStatus *replStatus = info.replicatorStatus;
    NSString *activity = activities[(NSInteger)replStatus.activity];
    NSString *error = replStatus.error ? replStatus.error.localizedDescription : @"none";
    NSLog(@" Replicator Status: %@, Error: %@", activity, error);
};

for (CBLPeerID *peerID in replicator.neighborPeers) {
    CBLPeerInfo *peerInfo = [replicator peerInfoForPeerID: peerID];
    if (peerInfo) {
        printPeerInfo(peerInfo);
    }
}
```

## [](#logging)Logging

`CBLLogDomain` sets up the logging of:

1. Peer discovery log messages
2. Multipeer replication and mesh network management log messages

```objc

```

## [](#api-reference)API Reference

You can find [Objective-C API References](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-objc) here.