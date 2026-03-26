---
title: Integrate a Custom Built Listener
description: Couchbase Lite database peer-to-peer sync- integrate a custom built listener
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.1/modules/csharp/pages/p2psync-custom.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.1@couchbase-lite:csharp:p2psync-custom.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.1/csharp/p2psync-custom.html)

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

#### [](#active-peer)Active Peer

The first step is to initialize the Couchbase Lite database.

#### [](#passive-peer)Passive Peer

In addition to initializing the database, the Passive Peer must initialize the `MessageEndpointListener`. The `MessageEndpointListener` acts as a Listener for incoming connections.

```C#
var database = new Database("mydb");
var endpointConfig = new MessageEndpointListenerConfiguration(new[] { database.GetDefaultCollection() }, ProtocolType.MessageStream);
_messageEndpointListener = new MessageEndpointListener(endpointConfig);
```

## [](#peer-selection-and-connection-setup)Peer Selection and Connection Setup

Once a Peer device is found, the application code must decide whether it should establish a connection with that Peer. This step includes inviting a Peer to a session and Peer authentication.

This is handled by the Communication Framework.

![selection](../_images/selection.png) 

Once the remote Peer has been authenticated, the next step is to connect with that Peer and initialize the Message Endpoint API.

## [](#replication-setup)Replication Setup

![connection](../_images/connection.png) 

#### [](#active-peer-2)Active Peer

When the connection is established, the active Peer must instantiate a `MessageEndpoint` object corresponding to the remote Peer.

```C#
var database = new Database("dbname");

// The delegate must implement the `IMessageEndpointDelegate` protocol.
var messageEndpointTarget = new MessageEndpoint(uid: "UID:123", target: "",
    protocolType: ProtocolType.MessageStream, delegateObject: this);
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

```C#
var replConfig = new ReplicatorConfiguration(messageEndpointTarget);
replConfig.AddCollection(database.GetDefaultCollection());

// Create the replicator object
var replicator = new Replicator(replConfig);
// Start the replicator
replicator.Start();
```

Next, Couchbase Lite will call back the application code through the `MessageEndpointDelegate.createConnection` interface method. When the application receives the callback, it must create an instance of `MessageEndpointConnection` and return it.

```C#
/* implementation of MessageEndpointDelegate */
public IMessageEndpointConnection CreateConnection(MessageEndpoint endpoint)
{
    var connection = new ActivePeerConnection(); /* implements MessageEndpointConnection */
    return connection;
}
```

Next, Couchbase Lite will call back the application code through the `MessageEndpointConnection.open` method.

```C#
/* implementation of MessageEndpointConnection */
public async Task Open(IReplicatorConnection connection)
{
    _replicatorConnection = connection;
    // await socket.Open(), etc
    // throw MessagingException if something goes wrong
}
```

The connection argument is then set on an instance variable. The application code must keep track of every `ReplicatorConnection` associated with every `MessageEndpointConnection`.

The `MessageError` argument in the completion block specifies whether the error is recoverable or not. If it is a recoverable error, the replicator will begin a retry process, creating a new `MessageEndpointConnection` instance.

#### [](#passive-peer-2)Passive Peer

After connection establishment on the Passive Peer, the first step is to initialize a new `MessageEndpointConnection` and pass it to the listener. This message tells the listener to accept incoming data from that Peer.

```C#
var connection = new PassivePeerConnection(); /* implements MessageEndpointConnection */
_messageEndpointListener?.Accept(connection);
```

`messageEndpointListener` is the instance of the `MessageEndpointListener` that was created in the first step ([Peer Discovery](#peer-discovery))

Couchbase Lite will call the application code back through the `MessageEndpointConnection.open` method.

```C#
/* implementation of MessageEndpointConnection */
public Task Open(IReplicatorConnection connection)
{
    _replicatorConnection = connection;
    // socket should already be open on the passive side
    return Task.FromResult(true);
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

#### [](#active-peer-3)Active Peer

When Couchbase Lite calls back the application code through the `MessageEndpointConnection.send` method, you should send that data to the other Peer using the communication framework.

```C#
/* implementation of MessageEndpointConnection */
public async Task Send(Message message)
{
    var data = message.ToByteArray();
    // await Socket.Send(), etc
    // throw MessagingException if something goes wrong
}
```

Once the data is sent, call the completion block to acknowledge the completion. You can use the `MessageError` in the completion block to specify whether the error is recoverable. If it is a recoverable error, the replicator will begin a retry process, creating a new `MessageEndpointConnection`.

When data is received from the passive Peer via the Communication Framework, you call the `ReplicatorConnection.receive` method.

```C#
var message = Message.FromBytes(data);
_replicatorConnection?.Receive(message);
```

The replication connection's `receive` method is called. Which then processes the data to persist to the local database.

#### [](#passive-peer-3)Passive Peer

As in the case of the active Peer, the passive Peer must implement the `MessageEndpointConnection.send` method to send data to the other Peer.

```C#
/* implementation of MessageEndpointConnection */
public async Task Send(Message message)
{
    var data = message.ToByteArray();
    // await Socket.Send(), etc
    // throw MessagingException if something goes wrong
}
```

Once the data is sent, call the completion block to acknowledge the completion. You can use the `MessageError` in the completion block to specify whether the error is recoverable. If it is a recoverable error, the replicator will begin a retry process, creating a new `MessageEndpointConnection`.

When data is received from the active Peer via the Communication Framework, you call the `ReplicatorConnection.receive` method.

```C#
var message = Message.FromBytes(data);
_replicatorConnection?.Receive(message);
```

## [](#connection-teardown)Connection Teardown

When a Peer disconnects from a Peer-to-Peer network, all connected Peers are notified. The disconnect notification is a good opportunity to close and remove a replication connection. The steps to Teardown the connection are slightly different depending on whether the active or passive Peer disconnects first. We will cover each case below.

#### [](#initiated-by-active-peer)Initiated by Active Peer

![dis active](../_images/dis-active.png) 

##### [](#active-peer-4)Active Peer

When an active Peer disconnects, it must call the `ReplicatorConnection.close` method.

```C#
_replicatorConnection?.Close(null);
```

Then, Couchbase Lite will call back your code through the `MessageEndpointConnection.close` to allow the application to disconnect with the Communication Framework.

```C#
/* implementation of MessageEndpointConnection */
public async Task Close(Exception error)
{
    // await socket.Close, etc (or do nothing if already closed)
    // throw MessagingException if something goes wrong (though
    // since it is "close" nothing special will happen)
}
```

##### [](#passive-peer-4)Passive Peer

When the passive Peer receives the corresponding disconnect notification from the Communication Framework, it must call the `ReplicatorConnection.close` method.

```C#
_replicatorConnection?.Close(null);
```

Then, Couchbase Lite will call back your code through the `MessageEndpointConnection.close` to allow the application to disconnect with the Communication Framework.

```C#
/* implementation of MessageEndpointConnection */
public async Task Close(Exception error)
{
    // await socket.Close, etc (or do nothing if already closed)
    // throw MessagingException if something goes wrong (though
    // since it is "close" nothing special will happen)
}
```

#### [](#initiated-by-passive-peer)Initiated by Passive Peer

![dis passive](../_images/dis-passive.png) 

##### [](#passive-peer-5)Passive Peer

When the passive disconnects, it must class the `MessageEndpointListener.closeAll` method.

```C#
_messageEndpointListener?.CloseAll();
```

Then, Couchbase Lite will call back your code through the `MessageEndpointConnection.close` to allow the application to disconnect with the Communication Framework.

```C#
/* implementation of MessageEndpointConnection */
public async Task Close(Exception error)
{
    // await socket.Close, etc (or do nothing if already closed)
    // throw MessagingException if something goes wrong (though
    // since it is "close" nothing special will happen)
}
```

##### [](#active-peer-5)Active Peer

When the active Peer receives the corresponding disconnect notification from the Communication Framework, it must call the `ReplicatorConnection.close` method.

```C#
_replicatorConnection?.Close(null);
```

Then, Couchbase Lite will call back your code through the `MessageEndpointConnection.close` to allow the application to disconnect with the Communication Framework.

```C#
/* implementation of MessageEndpointConnection */
public async Task Close(Exception error)
{
    // await socket.Close, etc (or do nothing if already closed)
    // throw MessagingException if something goes wrong (though
    // since it is "close" nothing special will happen)
}
```

## [](#related-content)Related Content

###### [](#)

How to

* [Passive Peer](p2psync-websocket-using-passive.md)
* [Active Peer](p2psync-websocket-using-active.md)

###### [](#-2)

Concepts

* [Peer-to-Peer Sync](#csharp:landing-p2psync.adoc)
* [API References](http://docs.couchbase.com/mobile/3.1.10/couchbase-lite-net)

###### [](#-3)

Community Resources …​

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

[Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)