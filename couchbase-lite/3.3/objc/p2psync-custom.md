---
title: Integrate a Custom Built Listener
description: Couchbase Lite database peer-to-peer sync- integrate a custom built listener
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.3/modules/objc/pages/p2psync-custom.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:3.3@couchbase-lite:objc:p2psync-custom.adoc[]
---

[View original HTML](/couchbase-lite/3.3/objc/p2psync-custom.html)

# Integrate a Custom Built Listener

> Description — _Couchbase Lite database peer-to-peer sync- integrate a custom built listener_  
> Related Content — [Peer-to-Peer](p2psync-websocket.md)

## [](#overview)Overview

> [!IMPORTANT]
> Enterprise Edition only
> 
> Peer-to-Peer Synchronization is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature. You must purchase the Enterprise License, which includes official [Couchbase Support](https://www.couchbase.com/support-policy). To use it in production (also see the [FAQ](https://www.couchbase.com/licensing-and-support-faq)).

This content covers how to integrate a custom _MessageEndpointListener_ solution with Couchbase Lite to handle the data transfer, which is the sending and receiving of data. Where applicable, we discuss how to integrate Couchbase Lite into the workflow.

The following sections describe a typical Peer-to-Peer workflow.

## [](#peer-discovery)Peer Discovery

Peer discovery is the first step. The communication framework will generally include a Peer discovery API for devices to advertise themselves on the network and to browse for other Peers.

![discovery](../_images/discovery.png) 

### [](#active-peer)Active Peer

The first step is to initialize the Couchbase Lite database.

### [](#passive-peer)Passive Peer

In addition to initializing the database, the Passive Peer must initialize the `MessageEndpointListener`. The `MessageEndpointListener` acts as a Listener for incoming connections.

```objc
CBLDatabase *database = [[CBLDatabase alloc] initWithName:@"mydb" error:&error];

CBLMessageEndpointListenerConfiguration *config =
[[CBLMessageEndpointListenerConfiguration alloc] initWithCollections:[NSArray arrayWithObject:[database defaultCollection:&error]]
                                                     protocolType:kCBLProtocolTypeMessageStream];
_messageEndpointListener = [[CBLMessageEndpointListener alloc] initWithConfig:config];
```

## [](#peer-selection-and-connection-setup)Peer Selection and Connection Setup

Once a Peer device is found, the application code must decide whether it should establish a connection with that Peer. This step includes inviting a Peer to a session and Peer authentication.

This is handled by the Communication Framework.

![selection](../_images/selection.png) 

Once the remote Peer has been authenticated, the next step is to connect with that Peer and initialize the Message Endpoint API.

## [](#replication-setup)Replication Setup

![connection](../_images/connection.png) 

### [](#active-peer-2)Active Peer

When the connection is established, the active Peer must instantiate a `MessageEndpoint` object corresponding to the remote Peer.

```objc
CBLDatabase *database = [[CBLDatabase alloc] initWithName:@"dbname" error:&error];
CBLCollection *collection = [database defaultCollection:&error];

// The delegate must implement the `CBLMessageEndpointDelegate` protocol.
NSString *id = @"";
CBLMessageEndpoint *endpoint = [[CBLMessageEndpoint alloc] initWithUID:@"UID:123"
                                                                target:id
                                                          protocolType:kCBLProtocolTypeMessageStream
                                                              delegate:self];
```

The `MessageEndpoint` initializer takes the following arguments.

1. `uid`: a unique ID that represents the remote active Peer.
2. `target`: This represents the remote passive Peer and could be any suitable representation of the remote Peer. It could be an Id, URL etc. If using the MultiPeerConnectivity Framework, this could be the MCPeerID.
3. `protocolType`: specifies the kind of transport you intend to implement. There are two options.

  * The default (`MessageStream`) means that you want to "send a series of messages", or in other words the Communication Framework will control the formatting of messages so that there are clear boundaries between messages.
  * The alternative (`ByteStream`) means that you just want to send raw bytes over the stream and Couchbase should format for you to ensure that messages get delivered in full.  
  Typically, the Communication Framework will handle message assembly and disassembly so you would use the `MessageType` option in most cases.
4. `delegate`: the delegate that will implement the `MessageEndpointDelegate` protocol, which is a factory for `MessageEndpointConnection`.

Then, a `Replicator` is instantiated with the initialized `MessageEndpoint` as the target.

```objc
CBLReplicatorConfiguration *replConfig = [[CBLReplicatorConfiguration alloc]
                                      initWithTarget:endpoint];
[replConfig addCollection:collection config:nil];


// Create the replicator object.
CBLReplicator *replicator = [[CBLReplicator alloc] initWithConfig:replConfig];
[replicator start];
```

Next, Couchbase Lite will call back the application code through the `MessageEndpointDelegate.createConnection` interface method. When the application receives the callback, it must create an instance of `MessageEndpointConnection` and return it.

```objc
- (id<CBLMessageEndpointConnection>)createConnectionForEndpoint:(CBLMessageEndpoint *)endpoint {
    return [[ActivePeerConnection alloc] init];
}
```

Next, Couchbase Lite will call back the application code through the `MessageEndpointConnection.open` method.

```objc
/* implementation of CBLMessageEndpointConnection */
- (void)open:(nonnull id<CBLReplicatorConnection>)connection completion:(nonnull void (^)(BOOL, CBLMessagingError  *_Nullable))completion {
    _replicatorConnection = connection;
    completion(YES, nil);
}
```

The connection argument is then set on an instance variable. The application code must keep track of every `ReplicatorConnection` associated with every `MessageEndpointConnection`.

The `MessageError` argument in the completion block specifies whether the error is recoverable or not. If it is a recoverable error, the replicator will begin a retry process, creating a new `MessageEndpointConnection` instance.

### [](#passive-peer-2)Passive Peer

After connection establishment on the Passive Peer, the first step is to initialize a new `MessageEndpointConnection` and pass it to the listener. This message tells the listener to accept incoming data from that Peer.

```objc
PassivePeerConnection *connection = [[PassivePeerConnection alloc] init]; /* implements CBLMessageEndpointConnection */
[_messageEndpointListener accept:connection];
```

`messageEndpointListener` is the instance of the `MessageEndpointListener` that was created in the first step ([Peer Discovery](#peer-discovery))

Couchbase Lite will call the application code back through the `MessageEndpointConnection.open` method.

```objc
/* implementation of CBLMessageEndpointConnection */
- (void)open:(nonnull id<CBLReplicatorConnection>)connection completion:(nonnull void (^)(BOOL, CBLMessagingError *_Nullable))completion {
    _replicatorConnection = connection;
    completion(YES, nil);
}
```

The `connection` argument is then set on an instance variable. The application code must keep track of every `ReplicatorConnection` associated with every `MessageEndpointConnection`.

At this point, the connection is established, and both Peers are ready to exchange data.

## [](#pushpull-replication)Push/Pull Replication

Typically, an application needs to send data and receive data. The directionality of the replication could be any of the following.

* **Push only:** The data is pushed from the local database to the remote database.
* **Pull only:** The data is pulled from the remote database to the local database.
* **Push and Pull:** The data is exchanged both ways.

Usually, the remote is a Sync Gateway database identified through a URL. In Peer-to-Peer syncing, the remote is another Couchbase Lite database.

![replication](../_images/replication.png) 

The replication lifecycle is handled through the `MessageEndpointConnection`.

### [](#active-peer-3)Active Peer

When Couchbase Lite calls back the application code through the `MessageEndpointConnection.send` method, you should send that data to the other Peer using the communication framework.

```objc
/* implementation of CBLMessageEndpointConnection */
- (void)send:(nonnull CBLMessage *)message completion:(nonnull void (^)(BOOL, CBLMessagingError  *_Nullable))completion {
    NSData *data = [message toData];
    NSLog(@"%@", data);
    /* send the data to the other peer */
    /* ... */
    /* call the completion handler once the message is sent */
    completion(YES, nil);
}
```

Once the data is sent, call the completion block to acknowledge the completion. You can use the `MessageError` in the completion block to specify whether the error is recoverable. If it is a recoverable error, the replicator will begin a retry process, creating a new `MessageEndpointConnection`.

When data is received from the passive Peer via the Communication Framework, you call the `ReplicatorConnection.receive` method.

```objc
CBLMessage *message = [CBLMessage fromData:data];
[_replicatorConnection receive:message];
```

The replication connection’s `receive` method is called. Which then processes the data to persist to the local database.

### [](#passive-peer-3)Passive Peer

As in the case of the active Peer, the passive Peer must implement the `MessageEndpointConnection.send` method to send data to the other Peer.

```objc
/* implementation of CBLMessageEndpointConnection */
- (void)send:(nonnull CBLMessage *)message completion:(nonnull void (^)(BOOL, CBLMessagingError *_Nullable))completion {
    NSData *data = [message toData];
    NSLog(@"%@", data);
    /* send the data to the other peer */
    /* ... */
    /* call the completion handler once the message is sent */
    completion(YES, nil);
}
```

Once the data is sent, call the completion block to acknowledge the completion. You can use the `MessageError` in the completion block to specify whether the error is recoverable. If it is a recoverable error, the replicator will begin a retry process, creating a new `MessageEndpointConnection`.

When data is received from the active Peer via the Communication Framework, you call the `ReplicatorConnection.receive` method.

```objc
CBLMessage *message = [CBLMessage fromData:data];
[_replicatorConnection receive:message];
```

## [](#connection-teardown)Connection Teardown

When a Peer disconnects from a Peer-to-Peer network, all connected Peers are notified. The disconnect notification is a good opportunity to close and remove a replication connection. The steps to Teardown the connection are slightly different depending on whether the active or passive Peer disconnects first. We will cover each case below.

### [](#initiated-by-active-peer)Initiated by Active Peer

![dis active](../_images/dis-active.png) 

### [](#active-peer-4)Active Peer

When an active Peer disconnects, it must call the `ReplicatorConnection.close` method.

```objc
[_replicatorConnection close:nil];
```

Then, Couchbase Lite will call back your code through the `MessageEndpointConnection.close` to allow the application to disconnect with the Communication Framework.

```objc
/* implementation of CBLMessageEndpointConnection */
- (void)close:(nullable NSError *)error completion:(nonnull void (^)(void))completion {
    /* disconnect with communications framework */
    /* ... */
    /* call completion handler */
    completion();
}
```

### [](#passive-peer-4)Passive Peer

When the passive Peer receives the corresponding disconnect notification from the Communication Framework, it must call the `ReplicatorConnection.close` method.

```objc
[_replicatorConnection close:nil];
```

Then, Couchbase Lite will call back your code through the `MessageEndpointConnection.close` to allow the application to disconnect with the Communication Framework.

```objc
/* implementation of CBLMessageEndpointConnection */
- (void)close:(nullable NSError *)error completion:(nonnull void (^)(void))completion {
    /* disconnect with communications framework */
    /* ... */
    /* call completion handler */
    completion();
}
```

### [](#initiated-by-passive-peer)Initiated by Passive Peer

![dis passive](../_images/dis-passive.png) 

### [](#passive-peer-5)Passive Peer

When the passive disconnects, it must class the `MessageEndpointListener.closeAll` method.

```objc
[_messageEndpointListener closeAll];
```

Then, Couchbase Lite will call back your code through the `MessageEndpointConnection.close` to allow the application to disconnect with the Communication Framework.

```objc
/* implementation of CBLMessageEndpointConnection */
- (void)close:(nullable NSError *)error completion:(nonnull void (^)(void))completion {
    /* disconnect with communications framework */
    /* ... */
    /* call completion handler */
    completion();
}
```

### [](#active-peer-5)Active Peer

When the active Peer receives the corresponding disconnect notification from the Communication Framework, it must call the `ReplicatorConnection.close` method.

```objc
[_replicatorConnection close:nil];
```

Then, Couchbase Lite will call back your code through the `MessageEndpointConnection.close` to allow the application to disconnect with the Communication Framework.

```objc
/* implementation of CBLMessageEndpointConnection */
- (void)close:(nullable NSError *)error completion:(nonnull void (^)(void))completion {
    /* disconnect with communications framework */
    /* ... */
    /* call completion handler */
    completion();
}
```

## [](#related-content)Related Content

### [](#)

How to

* [Passive Peer](p2psync-websocket-using-passive.md)
* [Active Peer](p2psync-websocket-using-active.md)

.

### [](#-2)

Concepts

* [Peer-to-Peer Sync](#objc:landing-p2psync.adoc)
* [API References](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-objc)

.

### [](#-3)

Community Resources …​

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

. [Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)