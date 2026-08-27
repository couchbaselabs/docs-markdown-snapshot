---
title: Passive Peer
description: Couchbase Lite's Peer-to-Peer Synchronization enables edge devices
  to synchronize securely without consuming centralized cloud-server resources
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.1/modules/android/pages/p2psync-websocket-using-passive.adoc
  xref: xref:3.1@couchbase-lite:android:p2psync-websocket-using-passive.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.1/android/p2psync-websocket-using-passive.html)

# Passive Peer

> Description — _Couchbase Lite's Peer-to-Peer Synchronization enables edge devices to synchronize securely without consuming centralized cloud-server resources_  
> _Abstract — How to set up a Listener to accept a Replicator connection and sync using peer-to-peer_  
> Related Content — [API Reference](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/) | [Passive Peer](p2psync-websocket-using-passive.md) | [Active Peer](p2psync-websocket-using-active.md)

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

This content provides code and configuration examples covering the implementation of [Peer-to-Peer Sync](refer-glossary.md#peer-to-peer-sync) over WebSockets. Specifically, it covers the implementation of a [Passive Peer](refer-glossary.md#passive-peer).

Couchbase's Passive Peer (also referred to as the server, or Listener) will accept a connection from an [Active Peer](refer-glossary.md#active-peer) (also referred to as the client or replicator) and replicate database changes to synchronize both databases.

Subsequent sections provide additional details and examples for the main configuration options.

> [!NOTE]
> Secure Storage
> 
> The use of TLS, its associated keys and certificates requires using secure storage to minimize the chances of a security breach. The implementation of this storage differs from platform to platform — see [Using secure storage](p2psync-websocket.md#using-secure-storage).

## [](#configuration-summary)Configuration Summary

You should configure and initialize a Listener for each Couchbase Lite database instance you want to sync. There is no limit on the number of Listeners you may configure — [Example 1](#simple-listener-initialization) shows a simple initialization and configuration process.

> [!TIP]
> You must include the initializer `CouchbaseLite.init(context)` such that it is executed (once only) before initializing the replicator; for example, in your app's `onCreate()` method.

Example 1\. Listener configuration and initialization

* Kotlin
* Java

```Kotlin
val listener = URLEndpointListener(
    URLEndpointListenerConfigurationFactory.newConfig(
        collections = collections, (1)
        port = 55990, (2)
        networkInterface = "wlan0", (3)

        enableDeltaSync = false, (4)

        // Configure server security
        disableTls = false, (5)

        // Use an Anonymous Self-Signed Cert
        identity = null, (6)

        // Configure Client Security using an Authenticator
        // For example, Basic Authentication (7)
        authenticator = ListenerPasswordAuthenticator { usr, pwd ->
            (usr === validUser) && (validPass.contentEquals(pwd))
        }
    ))

// Start the listener
listener.start() (8)
```

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

| **1** | Identify the local database to be used — see: [Initialize the Listener Configuration](#initialize-the-listener-configuration)                                                                                                                                                                                                                                                                               |
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

You can find [Android API References](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/) here.

## [](#device-discovery)Device Discovery

**This phase is optional:** If the Listener is initialized on a well-known URL endpoint (for example, a static IP Address or well-known DNS address) then you can configure Active Peers to connect to those.

Before initiating the Listener, you may execute a peer discovery phase. For the Passive Peer, this involves advertising the service using, for example, _Network Service Discovery_ (see: <https://developer.android.com/training/connect-devices-wirelessly/nsd>) and waiting for an invite from the Active Peer. The connection is established once the Passive Peer has authenticated and accepted an Active Peer's invitation.

## [](#initialize-the-listener-configuration)Initialize the Listener Configuration

Initialize the Listener configuration with the local database — see [Example 2](#ex-locdb)All other configuration values take their default setting.

Each Listener instance serves one Couchbase Lite database. Couchbase sets no hard limit on the number of Listeners you can initialize.

Example 2\. Specify Local Database

* Kotlin
* Java

```Kotlin
collections = collections, (1)
```

```Java
// Initialize the listener config
final URLEndpointListenerConfiguration thisConfig
    = new URLEndpointListenerConfiguration(collections); (1)
```

| **1** | Set the local database using the [URLEndpointListenerConfiguration](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html)'s constructor [(Database database)](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html#URLEndpointListenerConfiguration-com.couchbase.lite.Database-).The database must be opened before the Listener is started. thisDB has previously been declared as an object of type Database. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#lbl-set-network-and-port)Set Port and Network Interface

### [](#port-number)Port number

The Listener will automatically select an available port if you do not specify one — see [Example 3](#ex-port) for how to specify a port.

Example 3\. Specify a port

* Kotlin
* Java

```Kotlin
port = 55990, (1)
```

```Java
thisConfig.setPort(55990); (1)
```

| **1** | To use a canonical port — one known to other applications — specify it explicitly using the [setPort](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html#setPort-int-) method shown here.Ensure that firewall rules do not block any port you do specify.You can query the port using [getPort](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html#getPort-int-). |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#network-interface)Network Interface

The Listener will listen on all network interfaces by default.

Example 4\. Specify a Network Interface to Use

* Kotlin
* Java

```Kotlin
networkInterface = "wlan0", (1)
```

```Java
thisConfig.setNetworkInterface("wlan0"); (1)
```

| **1** | To specify an interface — one known to other applications — identify it explicitly, using the [setNetworkInterface](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html#setNetworkInterface-java.lang.String-) method shown here. This must be either an IP Address or network interface name such as en0. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#delta-sync)Delta Sync

Delta Sync allows clients to sync only those parts of a document that have changed. This can result in significant bandwidth consumption savings and throughput improvements. Both are valuable benefits, especially when network bandwidth is constrained.

Example 5\. Enable delta sync

* Kotlin
* Java

```Kotlin
enableDeltaSync = false, (1)
```

```Java
thisConfig.setEnableDeltaSync(false); (1)
```

| **1** | Delta sync replication is not enabled by default. Use [URLEndpointListenerConfiguration](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html)'s [setEnableDeltaSync](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html#setEnableDeltaSync-boolean-) method to activate or deactivate it. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#lbl-tls-security)TLS Security

### [](#enable-or-disable-tls)Enable or Disable TLS

Define whether the connection is to use TLS or clear text.

TLS-based encryption is enabled by default, and this setting ought to be used in any production environment. However, it _can_ be disabled. For example, for development or test environments.

When TLS is enabled, Couchbase Lite provides several options on how the Listener may be configured with an appropriate TLS Identity — see [Configure TLS Identity for Listener](#configure-tls-identity-for-listener).

> [!NOTE]
> To use cleartext, un-encrypted, network traffic (`http://` and-or `ws://`), include `android:usesCleartextTraffic="true"` in the `application` element of the manifest as shown on [android.com](https://developer.android.com/training/articles/security-config#CleartextTrafficPermitted).  
> **This not recommended in production**.

You can use [URLEndpointListenerConfiguration](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html)'s [setDisableTLS](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html#setDisableTls-boolean-) method to disable TLS communication if necessary

The `disableTLS` setting must be 'false' when _Client Cert Authentication_ is required.

Basic Authentication can be used with, or without, TLS.

[setDisableTLS](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html#setDisableTls-boolean-) works in conjunction with `TLSIdentity`, to enable developers to define the key and certificate to be used.

* If `disableTLS` is true — TLS communication is disabled and TLS identity is ignored. Active peers will use the `ws://` URL scheme used to connect to the listener.
* If `disableTLS` is false or not specified — TLS communication is enabled.  
Active peers will use the `wss://` URL scheme to connect to the listener.

### [](#configure-tls-identity-for-listener)Configure TLS Identity for Listener

Define the credentials the server will present to the client for authentication. Note that the server must always authenticate itself with the client — see: [Authenticate Listener on Active Peer](p2psync-websocket-using-active.md#authenticate-listener) for how the client deals with this.

Use [URLEndpointListenerConfiguration](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html)'s [setTlsIdentity](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html#setTlsIdentity-com.couchbase.lite.TLSIdentity-) method to configure the TLS Identity used in TLS communication.

If `TLSIdentity` is not set, then the listener uses an auto-generated anonymous self-signed identity (unless `disableTLS = true`). Whilst the client cannot use this to authenticate the server, it will use it to encrypt communication, giving a more secure option than non-TLS communication.

The auto-generated anonymous self-signed identity is saved in secure storage for future use to obviate the need to re-generate it.

> [!NOTE]
> Typically, you will configure the Listener's TLS Identity once during the initial launch and re-use it (from secure storage on any subsequent starts.

Here are some example code snippets showing:

* Setting TLS identity to expect self-signed certificate — — see: [Example 6](#ex-create-tls-id)
* Setting TLS identity to expect anonymous certificate — see: [Example 7](#ex-anon-tls-id)

Example 6\. Create Self-Signed Cert

Create a TLSIdentity for the server using convenience API. The system generates a self-signed certificate.

* Kotlin
* Java

```Kotlin

disableTls = false, (1)
```

```Java

thisConfig.setDisableTls(false); (1)
```

| **1** | Ensure TLS is used.                                                                                    |
| ----- | ------------------------------------------------------------------------------------------------------ |
| **2** | Map the required certificate attributes, in this case the common name.                                 |
| **3** | Create the required TLS identity using the attributes. Add to secure storage as 'couchbase-docs-cert'. |
| **4** | Configure the server to present the defined identity credentials when prompted.                        |

Example 7\. Use Anonymous Self-Signed Certificate

This example uses an _anonymous_ self signed certificate. Generated certificates are held in secure storage.

* Kotlin
* Java

```Kotlin
disableTls = false, (1)

// Use an Anonymous Self-Signed Cert
identity = null, (2)
```

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

Whilst client authentication is optional, Couchbase lite provides the necessary tools to implement it. Use the [URLEndpointListenerConfiguration](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html) class's [setAuthenticator](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/URLEndpointListenerConfiguration.html#setAuthenticator-com.couchbase.lite.ListenerAuthenticator-) method to specify how the client-supplied credentials are to be authenticated.

Valid options are:

* No authentication — If you do not define an Authenticator then all clients are accepted.
* Basic Authentication — uses the [ListenerPasswordAuthenticator](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/ListenerPasswordAuthenticator.html) to authenticate the client using the client-supplied username and password (from the http authentication header).
* [ListenerCertificateAuthenticator](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/ListenerCertificateAuthenticator.html) — which authenticates the client using a client supplied chain of one or more certificates. You should initialize the authenticator using one of the following constructors:

  * A list of one or more root certificates — the client supplied certificate must end at a certificate in this list if it is to be authenticated
  * A block of code that assumes total responsibility for authentication — it must return a boolean response (true for an authenticated client, or false for a failed authentication).

### [](#use-basic-authentication)Use Basic Authentication

Define how to authenticate client-supplied username and password credentials. To use client-supplied certificates instead — see: [Using Client Certificate Authentication](#using-client-certificate-authentication)

Example 8\. Password authentication

* Kotlin
* Java

```Kotlin
                // Configure Client Security using an Authenticator
                // For example, Basic Authentication (1)
                authenticator = ListenerPasswordAuthenticator { usr, pwd ->
                    (usr === validUser) && (validPass.contentEquals(pwd))
                }
            ))

        // Start the listener
        listener.start() (2)
    }

    fun simpleListenerExample(db: Database) {
        val listener = URLEndpointListener(
            URLEndpointListenerConfigurationFactory.newConfig(
                collections = db.collections,
                authenticator = ListenerPasswordAuthenticator { user, pwd ->
                    (user == "daniel") && (String(pwd) == "123")  (3)
                })
        )
        listener.start() (4)
        thisListener = listener

    }

    fun overrideConfigExample() {
        val listener8080 = URLEndpointListenerConfigurationFactory.newConfig(
            networkInterface = "en0",
            port = 8080
        )
        val listener8081 = listener8080.newConfig(port = 8081)
    }

    fun listenerStatusCheckExample(db: Database) {
        val listener = URLEndpointListener(
            URLEndpointListenerConfigurationFactory
                .newConfig(collections = db.collections)
        )
        listener.start()
        thisListener = listener
        val connectionCount = listener.status?.connectionCount (5)
        val activeConnectionCount = listener.status?.activeConnectionCount (6)
    }

    fun listenerStopExample() {
        val listener = thisListener
        thisListener = null
        listener?.stop()

    }

}


//
// Copyright (c) 2021 Couchbase, Inc All rights reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
@file:Suppress("UNUSED_VARIABLE", "unused")

package com.couchbase.codesnippets

import com.couchbase.lite.Collection
import com.couchbase.lite.Conflict
import com.couchbase.lite.ConflictResolver
import com.couchbase.lite.Document
import com.couchbase.lite.MutableDocument
import java.io.ByteArrayOutputStream
import java.io.IOException
import java.io.InputStream


private const val TAG = "REPLICATION"

@Throws(IOException::class)
fun InputStream.toByteArray(): ByteArray {
    val buffer = ByteArray(1024)
    val output = ByteArrayOutputStream()

    var n: Int
    while (-1 < this.read(buffer).also { n = it }) {
        output.write(buffer, 0, n)
    }

    return output.toByteArray()
}

//
//        <.> The conflict handler code is provided as a lambda.
//
//        <.> If the handler cannot resolve a conflict, it can return false.
//        In this case, the save method will cancel the save operation and return false the same way as using the save() method with the failOnConflict concurrency control.
//
//        <.> Within the conflict handler, you can modify the document parameter which is the same instance of Document that is passed to the save() method. So in effect, you will be directly modifying the document that is being saved.
//
//        <.> When handling is done, the method must return true (for  successful resolution) or false (if it was unable to resolve the conflict).
//
//        <.> If there is an exception thrown in the handle() method, the exception will be caught and re-thrown in the save() method

// Using replConfig.setConflictResolver(new LocalWinConflictResolver());
@Suppress("unused")
object LocalWinsResolver : ConflictResolver {
    override fun resolve(conflict: Conflict) = conflict.localDocument
}

// Using replConfig.setConflictResolver(new RemoteWinConflictResolver());
@Suppress("unused")
object RemoteWinsResolver : ConflictResolver {
    override fun resolve(conflict: Conflict) = conflict.remoteDocument
}

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

    fun testSaveWithCustomConflictResolver(collection: Collection) {
        val mutableDocument = collection.getDocument("xyz")?.toMutable() ?: return
        mutableDocument.setString("name", "apples")
        collection.save(mutableDocument) { newDoc, curDoc ->  (7)
            if (curDoc == null) {
                return@save false
            } (8)
            val dataMap: MutableMap<String, Any> = curDoc.toMap()
            dataMap.putAll(newDoc.toMap()) (9)
            newDoc.setData(dataMap)
            true (10)
        } (11)
    }
}

//
// Copyright (c) 2021 Couchbase, Inc All rights reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
@file:Suppress("UNUSED_VARIABLE", "unused")

package com.couchbase.codesnippets

import com.couchbase.lite.Collection
import com.couchbase.lite.CouchbaseLiteException
import com.couchbase.lite.Message
import com.couchbase.lite.MessageEndpoint
import com.couchbase.lite.MessageEndpointConnection
import com.couchbase.lite.MessageEndpointDelegate
import com.couchbase.lite.MessageEndpointListener
import com.couchbase.lite.MessageEndpointListenerConfigurationFactory
import com.couchbase.lite.MessagingCloseCompletion
import com.couchbase.lite.MessagingCompletion
import com.couchbase.lite.ProtocolType
import com.couchbase.lite.Replicator
import com.couchbase.lite.ReplicatorConfigurationFactory
import com.couchbase.lite.ReplicatorConnection
import com.couchbase.lite.newConfig


@Suppress("unused")
class BrowserSessionManager : MessageEndpointDelegate {
    private var replicator: Replicator? = null

    fun initCouchbase(collections: Set<Collection>) {

        // The delegate must implement the `MessageEndpointDelegate` protocol.
        val messageEndpoint = MessageEndpoint("UID:123", "active", ProtocolType.MESSAGE_STREAM, this)

        // Create the replicator object.
        val repl = Replicator(
            ReplicatorConfigurationFactory.newConfig(
                collections = mapOf(collections to null),
                target = messageEndpoint
            )
        )

        // Start the replication.
        repl.start()
        replicator = repl
    }

    /* implementation of MessageEndpointDelegate */
    override fun createConnection(endpoint: MessageEndpoint) = ActivePeerConnection()
}

/* ----------------------------------------------------------- */
/* ---------------------  ACTIVE SIDE  ----------------------- */
/* ----------------------------------------------------------- */

@Suppress("unused")
class ActivePeerConnection : MessageEndpointConnection {
    private var replicatorConnection: ReplicatorConnection? = null

    fun disconnect() {
        replicatorConnection?.close(null)
        replicatorConnection = null
    }

    /* implementation of MessageEndpointConnection */
    override fun open(connection: ReplicatorConnection, completion: MessagingCompletion) {
        replicatorConnection = connection
        completion.complete(true, null)
    }

    override fun close(error: Exception?, completion: MessagingCloseCompletion) {
        /* disconnect with communications framework */
        /* ... */
        /* call completion handler */
        completion.complete()
    }

    /* implementation of MessageEndpointConnection */
    override fun send(message: Message, completion: MessagingCompletion) {
        /* send the data to the other peer */
        /* ... */
        /* call the completion handler once the message is sent */
        completion.complete(true, null)
    }

    fun receive(message: Message) {
        replicatorConnection?.receive(message)
    }
}

/* ----------------------------------------------------------- */
/* ---------------------  PASSIVE SIDE  ---------------------- */
/* ----------------------------------------------------------- */

@Suppress("unused")
class PassivePeerConnection : MessageEndpointConnection {
    private var listener: MessageEndpointListener? = null
    private var replicatorConnection: ReplicatorConnection? = null

    @Throws(CouchbaseLiteException::class)
    fun startListener(collections: Set<Collection>) {
        listener = MessageEndpointListener(
            MessageEndpointListenerConfigurationFactory.newConfig(collections, ProtocolType.MESSAGE_STREAM)
        )
    }

    fun stopListener() {
        listener?.closeAll()
    }

    fun accept() {
        val connection = PassivePeerConnection() /* implements MessageEndpointConnection */
        listener?.accept(connection)
    }

    fun disconnect() {
        replicatorConnection?.close(null)
    }

    /* implementation of MessageEndpointConnection */
    override fun open(connection: ReplicatorConnection, completion: MessagingCompletion) {
        replicatorConnection = connection
        completion.complete(true, null)
    }

    /* implementation of MessageEndpointConnection */
    override fun close(error: Exception?, completion: MessagingCloseCompletion) {
        /* disconnect with communications framework */
        /* ... */
        /* call completion handler */
        completion.complete()
    }

    /* implementation of MessageEndpointConnection */
    override fun send(message: Message, completion: MessagingCompletion) {
        /* send the data to the other peer */
        /* ... */
        /* call the completion handler once the message is sent */
        completion.complete(true, null)
    }

    fun receive(message: Message) {
        replicatorConnection?.receive(message)
    }

}
//
// Copyright (c) 2021 Couchbase, Inc All rights reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
@file:Suppress("UNUSED_VARIABLE", "unused")

package com.couchbase.codesnippets

import com.couchbase.codesnippets.util.log
import com.couchbase.lite.Collection
import com.couchbase.lite.DataSource
import com.couchbase.lite.Database
import com.couchbase.lite.Dictionary
import com.couchbase.lite.Expression
import com.couchbase.lite.Function
import com.couchbase.lite.IndexBuilder
import com.couchbase.lite.MutableDictionary
import com.couchbase.lite.PredictionFunction
import com.couchbase.lite.PredictiveModel
import com.couchbase.lite.QueryBuilder
import com.couchbase.lite.SelectResult
import com.couchbase.lite.ValueIndexItem


private const val TAG = "PREDICT"

// tensorFlowModel is a fake implementation
object TensorFlowModel {
    fun predictImage(data: ByteArray?): Map<String, Any?> = TODO()
}

object ImageClassifierModel : PredictiveModel {
    const val name = "ImageClassifier"

    // this would be the implementation of the ml model you have chosen
    override fun predict(input: Dictionary) = input.getBlob("photo")?.let {
        MutableDictionary(TensorFlowModel.predictImage(it.content)) (1)
    }
}


fun predictiveModelExamples(collection: Collection) {

    Database.prediction.registerModel("ImageClassifier", ImageClassifierModel)

    collection.createIndex(
        "value-index-image-classifier",
        IndexBuilder.valueIndex(ValueIndexItem.expression(Expression.property("label")))
    )

    Database.prediction.unregisterModel("ImageClassifier")
}


fun predictiveIndexExamples(collection: Collection) {

    val inputMap: Map<String, Any?> = mutableMapOf("numbers" to Expression.property("photo"))
    collection.createIndex(
        "predictive-index-image-classifier",
        IndexBuilder.predictiveIndex("ImageClassifier", Expression.map(inputMap), null)
    )
}


fun predictiveQueryExamples(collection: Collection) {

    val inputMap: Map<String, Any?> = mutableMapOf("photo" to Expression.property("photo"))
    val prediction: PredictionFunction = Function.prediction(
        ImageClassifierModel.name,
        Expression.map(inputMap) (1)
    )

    val query = QueryBuilder
        .select(SelectResult.all())
        .from(DataSource.collection(collection))
        .where(
            prediction.propertyPath("label").equalTo(Expression.string("car"))
                .and(
                    prediction.propertyPath("probability")
                        .greaterThanOrEqualTo(Expression.doubleValue(0.8))
                )
        )

    query.execute().use {
        log("Number of rows: ${it.allResults().size}")
    }
}
//
// Copyright (c) 2021 Couchbase, Inc All rights reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
@file:Suppress("UNUSED_VARIABLE", "unused", "UNUSED_PARAMETER")

package com.couchbase.codesnippets

import com.couchbase.codesnippets.util.log
import com.couchbase.lite.ArrayFunction
import com.couchbase.lite.Collection
import com.couchbase.lite.DataSource
import com.couchbase.lite.Database
import com.couchbase.lite.Expression
import com.couchbase.lite.FullTextFunction
import com.couchbase.lite.FullTextIndexConfigurationFactory
import com.couchbase.lite.FullTextIndexItem
import com.couchbase.lite.Function
import com.couchbase.lite.IndexBuilder
import com.couchbase.lite.Join
import com.couchbase.lite.Meta
import com.couchbase.lite.Ordering
import com.couchbase.lite.Parameters
import com.couchbase.lite.QueryBuilder
import com.couchbase.lite.Result
import com.couchbase.lite.SelectResult
import com.couchbase.lite.ValueIndexConfigurationFactory
import com.couchbase.lite.ValueIndexItem
import com.couchbase.lite.newConfig
import com.fasterxml.jackson.databind.ObjectMapper


private const val TAG = "QUERY"

// ### Indexing
fun indexingExample(collection: Collection) {

    collection.createIndex(
        "TypeNameIndex",
        ValueIndexConfigurationFactory.newConfig("type", "name")
    )
}

// ### SELECT statement
fun selectStatementExample(collection: Collection) {

    val query = QueryBuilder
        .select(
            SelectResult.expression(Meta.id),
            SelectResult.property("name"),
            SelectResult.property("type")
        )
        .from(DataSource.collection(collection))
        .where(Expression.property("type").equalTo(Expression.string("hotel")))
        .orderBy(Ordering.expression(Meta.id))

    query.execute().use { rs ->
        rs.forEach {
            log("hotel id ->${it.getString("id")}")
            log("hotel name -> ${it.getString("name")}")
        }
    }
}

fun whereStatementExample(collection: Collection) {

    val query = QueryBuilder
        .select(SelectResult.all())
        .from(DataSource.collection(collection))
        .where(Expression.property("type").equalTo(Expression.string("hotel")))
        .limit(Expression.intValue(10))

    query.execute().use { rs ->
        rs.forEach { result ->
            result.getDictionary("myDatabase")?.let {
                log("name -> ${it.getString("name")}")
                log("type -> ${it.getString("type")}")
            }
        }
    }
}

// ####　Collection Operators
fun collectionStatementExample(collection: Collection) {
    val query = QueryBuilder
        .select(
            SelectResult.expression(Meta.id),
            SelectResult.property("name"),
            SelectResult.property("public_likes")
        )
        .from(DataSource.collection(collection))
        .where(
            Expression.property("type").equalTo(Expression.string("hotel"))
                .and(
                    ArrayFunction.contains(
                        Expression.property("public_likes"),
                        Expression.string("Armani Langworth")
                    )
                )
        )
    query.execute().use { rs ->
        rs.forEach {
            log("public_likes -> ${it.getArray("public_likes")?.toList()}")
        }
    }
}

// Pattern Matching
fun patternMatchingExample(collection: Collection) {
    val query = QueryBuilder
        .select(
            SelectResult.expression(Meta.id),
            SelectResult.property("country"),
            SelectResult.property("name")
        )
        .from(DataSource.collection(collection))
        .where(
            Expression.property("type").equalTo(Expression.string("landmark"))
                .and(
                    Function.lower(Expression.property("name"))
                        .like(Expression.string("royal engineers museum"))
                )
        )
    query.execute().use { rs ->
        rs.forEach {
            log("name -> ${it.getString("name")}")
        }
    }
}

// ### Wildcard Match
fun wildcardMatchExample(collection: Collection) {
    val query = QueryBuilder
        .select(
            SelectResult.expression(Meta.id),
            SelectResult.property("country"),
            SelectResult.property("name")
        )
        .from(DataSource.collection(collection))
        .where(
            Expression.property("type").equalTo(Expression.string("landmark"))
                .and(
                    Function.lower(Expression.property("name"))
                        .like(Expression.string("eng%e%"))
                )
        )
    query.execute().use { rs ->
        rs.forEach {
            log("name -> ${it.getString("name")}")
        }
    }
}

// Wildcard Character Match
fun wildCharacterMatchExample(collection: Collection) {
    val query = QueryBuilder
        .select(
            SelectResult.expression(Meta.id),
            SelectResult.property("country"),
            SelectResult.property("name")
        )
        .from(DataSource.collection(collection))
        .where(
            Expression.property("type").equalTo(Expression.string("landmark"))
                .and(
                    Function.lower(Expression.property("name"))
                        .like(Expression.string("eng____r"))
                )
        )
    query.execute().use { rs ->
        rs.forEach {
            log("name -> ${it.getString("name")}")
        }
    }
}

// ### Regex Match
fun regexMatchExample(collection: Collection) {
    val query = QueryBuilder
        .select(
            SelectResult.expression(Meta.id),
            SelectResult.property("country"),
            SelectResult.property("name")
        )
        .from(DataSource.collection(collection))
        .where(
            Expression.property("type").equalTo(Expression.string("landmark"))
                .and(
                    Function.lower(Expression.property("name"))
                        .regex(Expression.string("\\beng.*r\\b"))
                )
        )
    query.execute().use { rs ->
        rs.forEach {
            log("name -> ${it.getString("name")}")
        }
    }
}

// ###　WHERE statement
fun queryDeletedDocumentsExample(collection: Collection) {
    // Query documents that have been deleted
    val query = QueryBuilder
        .select(SelectResult.expression(Meta.id))
        .from(DataSource.collection(collection))
        .where(Meta.deleted)
}

// JOIN statement
fun joinStatementExample(collection: Collection) {
    val query = QueryBuilder
        .select(
            SelectResult.expression(Expression.property("name").from("airline")),
            SelectResult.expression(Expression.property("callsign").from("airline")),
            SelectResult.expression(Expression.property("destinationairport").from("route")),
            SelectResult.expression(Expression.property("stops").from("route")),
            SelectResult.expression(Expression.property("airline").from("route"))
        )
        .from(DataSource.collection(collection).`as`("airline"))
        .join(
            Join.join(DataSource.collection(collection).`as`("route"))
                .on(
                    Meta.id.from("airline")
                        .equalTo(Expression.property("airlineid").from("route"))
                )
        )
        .where(
            Expression.property("type").from("route").equalTo(Expression.string("route"))
                .and(
                    Expression.property("type").from("airline")
                        .equalTo(Expression.string("airline"))
                )
                .and(
                    Expression.property("sourceairport").from("route")
                        .equalTo(Expression.string("RIX"))
                )
        )
    query.execute().use { rs ->
        rs.forEach {
            log("name -> ${it.toMap()}")
        }
    }
}

// ### GROUPBY statement
fun groupByStatementExample(collection: Collection) {
    val query = QueryBuilder
        .select(
            SelectResult.expression(Function.count(Expression.string("*"))),
            SelectResult.property("country"),
            SelectResult.property("tz")
        )
        .from(DataSource.collection(collection))
        .where(
            Expression.property("type").equalTo(Expression.string("airport"))
                .and(Expression.property("geo.alt").greaterThanOrEqualTo(Expression.intValue(300)))
        )
        .groupBy(
            Expression.property("country"), Expression.property("tz")
        )
        .orderBy(Ordering.expression(Function.count(Expression.string("*"))).descending())
    query.execute().use { rs ->
        rs.forEach {
            log(
                "There are ${it.getInt("$1")} airports on the ${
                    it.getString("tz")
                } timezone located in ${
                    it.getString("country")
                } and above 300ft"
            )
        }
    }
}

// ### ORDER BY statement
fun orderByStatementExample(collection: Collection) {
    val query = QueryBuilder
        .select(
            SelectResult.expression(Meta.id),
            SelectResult.property("name")
        )
        .from(DataSource.collection(collection))
        .where(Expression.property("type").equalTo(Expression.string("hotel")))
        .orderBy(Ordering.property("name").ascending())
        .limit(Expression.intValue(10))

    query.execute().use { rs ->
        rs.forEach {
            log("${it.toMap()}")
        }
    }
}

fun querySyntaxAllExample(collection: Collection) {
    val listQuery = QueryBuilder.select(SelectResult.all())
        .from(DataSource.collection(collection))

    val hotels = mutableMapOf<String, Hotel>()
    listQuery.execute().use { rs ->
        rs.allResults().forEach {
            // get the k-v pairs from the 'hotel' key's value into a dictionary
            val thisDocsProps = it.getDictionary(0) (12)
            val thisDocsId = thisDocsProps!!.getString("id")
            val thisDocsName = thisDocsProps.getString("name")
            val thisDocsType = thisDocsProps.getString("type")
            val thisDocsCity = thisDocsProps.getString("city")

            // Alternatively, access results value dictionary directly
            val id = it.getDictionary(0)?.getString("id").toString() (13)
            hotels[id] = Hotel(
                id,
                it.getDictionary(0)?.getString("type"),
                it.getDictionary(0)?.getString("name"),
                it.getDictionary(0)?.getString("city"),
                it.getDictionary(0)?.getString("country"),
                it.getDictionary(0)?.getString("description")
            )
        }
    }
}

fun querySyntaxIdExample(collection: Collection) {
    // tag::query-select-meta
    val query = QueryBuilder
        .select(
            SelectResult.expression(Meta.id).`as`("hotelId")
        )
        .from(DataSource.collection(collection))


    query.execute().use { rs ->
        rs.allResults().forEach {
            log("hotel id ->${it.getString("hotelId")}")
        }
    }
    // end::query-select-meta
}

fun querySyntaxCountExample(collection: Collection) {

    val query = QueryBuilder
        .select(
            SelectResult.expression(Function.count(Expression.string("*"))).`as`("mycount")
        ) (14)
        .from(DataSource.collection(collection))


    query.execute().use { rs ->
        rs.allResults().forEach {
            log("name -> ${it.getInt("mycount")}")
        }
    }
}

fun querySyntaxPropsExample(collection: Collection) {

    val query = QueryBuilder
        .select(
            SelectResult.expression(Meta.id),
            SelectResult.property("country"),
            SelectResult.property("name")
        )
        .from(DataSource.collection(collection))


    query.execute().use { rs ->
        rs.allResults().forEach {
            log("Hotel name -> ${it.getString("name")}, in ${it.getString("country")}")
        }
    }
}

// IN operator
fun inOperatorExample(collection: Collection) {
    val query = QueryBuilder.select(SelectResult.all())
        .from(DataSource.collection(collection))
        .where(
            Expression.string("Armani").`in`(
                Expression.property("first"),
                Expression.property("last"),
                Expression.property("username")
            )
        )

    query.execute().use { rs ->
        rs.forEach {
            log("public_likes -> ${it.toMap()}")
        }
    }
}


fun queryPaginationExample(collection: Collection) {
    val thisOffset = 0
    val thisLimit = 20
    val listQuery = QueryBuilder
        .select(SelectResult.all())
        .from(DataSource.collection(collection))
        .limit(
            Expression.intValue(thisLimit),
            Expression.intValue(thisOffset)
        ) (15)

}

// ### all(*)
fun selectAllExample(collection: Collection) {
    val queryAll = QueryBuilder
        .select(SelectResult.all())
        .from(DataSource.collection(collection))
        .where(Expression.property("type").equalTo(Expression.string("hotel")))

}

fun liveQueryExample(collection: Collection) {
    val query = QueryBuilder
        .select(SelectResult.all())
        .from(DataSource.collection(collection)) (16)

    // Adds a query change listener.
    // Changes will be posted on the main queue.
    val token = query.addChangeListener { change ->
        change.results?.let { rs ->
            rs.forEach {
                log("results: ${it.keys}")
                /* Update UI */
            }
        } (17)
    }


    token.remove()
}

// META function
fun metaFunctionExample(collection: Collection) {
    val query = QueryBuilder
        .select(SelectResult.expression(Meta.id))
        .from(DataSource.collection(collection))
        .where(Expression.property("type").equalTo(Expression.string("airport")))
        .orderBy(Ordering.expression(Meta.id))

    query.execute().use { rs ->
        rs.forEach {
            log("airport id ->${it.getString("id")}")
            log("airport id -> ${it.getString(0)}")
        }
    }
}

// ### EXPLAIN statement
fun explainAllExample(collection: Collection) {
    val query = QueryBuilder
        .select(SelectResult.all())
        .from(DataSource.collection(collection))
        .where(Expression.property("type").equalTo(Expression.string("university")))
        .groupBy(Expression.property("country"))
        .orderBy(Ordering.property("name").descending()) (18)

    log(query.explain()) (19)
}

fun explainLikeExample(collection: Collection) {
    val query = QueryBuilder
        .select(SelectResult.all())
        .from(DataSource.collection(collection))
        .where(Expression.property("type").like(Expression.string("%hotel%"))) (20)
        .groupBy(Expression.property("country"))
        .orderBy(Ordering.property("name").descending()) (21)
    log(query.explain())
}

fun explainNoPFXExample(collection: Collection) {
    val query = QueryBuilder
        .select(SelectResult.all())
        .from(DataSource.collection(collection))
        .where(
            Expression.property("type").like(Expression.string("hotel%")) (22)
                .and(Expression.property("name").like(Expression.string("%royal%")))
        )
    log(query.explain())
}

fun explainFnExample(collection: Collection) {
    val query = QueryBuilder
        .select(SelectResult.all())
        .from(DataSource.collection(collection))
        .where(Function.lower(Expression.property("type").equalTo(Expression.string("hotel")))) (23)
    log(query.explain())

}

fun explainNoFnExample(collection: Collection) {
    val query = QueryBuilder
        .select(SelectResult.all())
        .from(DataSource.collection(collection))
        .where(Expression.property("type").equalTo(Expression.string("hotel"))) (24)
    log(query.explain())
}

fun prepareIndex(collection: Collection) {
    collection.createIndex(
        "overviewFTSIndex",
        FullTextIndexConfigurationFactory.newConfig("overview"))
}

fun prepareIndexBuilderExample(collection: Collection) {
    collection.createIndex(
        "overviewFTSIndex",
        IndexBuilder.fullTextIndex(FullTextIndexItem.property("overview")).ignoreAccents(false)
    )
}

fun indexingQueryBuilderExample(collection: Collection) {
    collection.createIndex(
        "TypeNameIndex",
        IndexBuilder.valueIndex(
            ValueIndexItem.property("type"),
            ValueIndexItem.property("name")
        )
    )
}

fun ftsExample(database: Database) {
    val ftsQuery = database.createQuery(
        "SELECT _id, overview FROM _ WHERE MATCH(overviewFTSIndex, 'michigan') ORDER BY RANK(overviewFTSIndex)"
    )
    ftsQuery.execute().use { rs ->
        rs.allResults().forEach {
            log("${it.getString("id")}: ${it.getString("overview")}")
        }
    }
}

fun ftsQueryBuilderExample(collection: Collection) {
    val ftsQuery =
        QueryBuilder.select(
            SelectResult.expression(Meta.id),
            SelectResult.property("overview")
        )
            .from(DataSource.collection(collection))
            .where(FullTextFunction.match(Expression.fullTextIndex("overviewFTSIndex"), "michigan"))

    ftsQuery.execute().use { rs ->
        rs.allResults().forEach {
            log("${it.getString("Meta.id")}: ${it.getString("overview")}")
        }
    }
}

fun querySyntaxJsonExample(collection: Collection) {
    // Example assumes Hotel class object defined elsewhere
    // Build the query
    val listQuery = QueryBuilder.select(SelectResult.all())
        .from(DataSource.collection(collection))
    // Uses Jackson JSON processor
    val mapper = ObjectMapper()
    val hotels = mutableListOf<Hotel>()

    listQuery.execute().use { rs ->
        rs.forEach {

            // Get result as JSON string
            val json = it.toJSON() (25)

            // Get Hashmap from JSON string
            val dictFromJSONstring = mapper.readValue(json, HashMap::class.java) (26)

            // Use created hashmap
            val hotelId = dictFromJSONstring["id"].toString() //
            val hotelType = dictFromJSONstring["type"].toString()
            val hotelname = dictFromJSONstring["name"].toString()

            // Get custom object from JSON string
            val thisHotel = mapper.readValue(json, Hotel::class.java) (27)
            hotels.add(thisHotel)
        }
    }
}

fun docsOnlyQuerySyntaxN1QL(thisDb: Database): List<Result> {
    // For Documentation -- N1QL Query using parameters
    val thisQuery = thisDb.createQuery(
        "SELECT META().id AS id FROM _ WHERE type = \"hotel\""
    ) (28)

    return thisQuery.execute().use { rs -> rs.allResults() }
}

fun docsOnlyQuerySyntaxN1QLParams(database: Database): List<Result> {
    // For Documentation -- N1QL Query using parameters
    val thisQuery = database.createQuery(
        "SELECT META().id AS id FROM _ WHERE type = \$type"
    ) (29)

    thisQuery.parameters = Parameters().setString("type", "hotel") (30)

    return thisQuery.execute().allResults()

}

//
// Copyright (c) 2023 Couchbase, Inc All rights reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
@file:Suppress("UNUSED_VARIABLE", "unused", "UNUSED_PARAMETER")

package com.couchbase.codesnippets

import com.couchbase.codesnippets.util.log
import com.couchbase.lite.BasicAuthenticator
import com.couchbase.lite.ClientCertificateAuthenticator
import com.couchbase.lite.Collection
import com.couchbase.lite.CollectionConfigurationFactory
import com.couchbase.lite.CouchbaseLiteException
import com.couchbase.lite.Database
import com.couchbase.lite.DatabaseEndpoint
import com.couchbase.lite.DocumentFlag
import com.couchbase.lite.Endpoint
import com.couchbase.lite.ListenerToken
import com.couchbase.lite.Replicator
import com.couchbase.lite.ReplicatorConfigurationFactory
import com.couchbase.lite.ReplicatorType
import com.couchbase.lite.SessionAuthenticator
import com.couchbase.lite.TLSIdentity
import com.couchbase.lite.URLEndpoint
import com.couchbase.lite.newConfig
import java.net.URI
import java.security.KeyStore
import java.security.cert.X509Certificate


class ReplicationExamples {
    private var thisReplicator: Replicator? = null
    private var thisToken: ListenerToken? = null

    fun activeReplicatorExample(collections: Set<Collection>) {
        // Create replicator
        // Consider holding a reference somewhere
        // to prevent the Replicator from being GCed
        val repl = Replicator( (31)

            // initialize the replicator configuration
            ReplicatorConfigurationFactory.newConfig(
                target = URLEndpoint(URI("wss://listener.com:8954")), (32)

                collections = mapOf(collections to null),

                // Set replicator type
                type = ReplicatorType.PUSH_AND_PULL,

                // Configure Sync Mode
                continuous = false, // default value


                // set auto-purge behavior
                // (here we override default)
                enableAutoPurge = false, (33)


                // Configure Server Authentication --
                // only accept self-signed certs
                acceptOnlySelfSignedServerCertificate = true, (34)


                // Configure the credentials the
                // client will provide if prompted
                authenticator = BasicAuthenticator("PRIVUSER", "let me in".toCharArray())  (35)

            )
        )

        // Optionally add a change listener (36)
        val token = repl.addChangeListener { change ->
            val err: CouchbaseLiteException? = change.status.error
            if (err != null) {
                log("Error code ::  ${err.code}", err)
            }
        }

        // Start replicator
        repl.start(false) (37)


        thisReplicator = repl
        thisToken = token

    }

    fun replicationBasicAuthenticationExample(collections: Set<Collection>) {

        // Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
        val repl = Replicator(
            ReplicatorConfigurationFactory.newConfig(
                target = URLEndpoint(URI("ws://localhost:4984/mydatabase")),
                collections = mapOf(collections to null),
                authenticator = BasicAuthenticator("username", "password".toCharArray())
            )
        )
        repl.start()
        thisReplicator = repl
    }

    fun replicationSessionAuthenticationExample(collections: Set<Collection>) {
        // Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
        val repl = Replicator(
            ReplicatorConfigurationFactory.newConfig(
                target = URLEndpoint(URI("ws://localhost:4984/mydatabase")),
                collections = mapOf(collections to null),
                authenticator = SessionAuthenticator("904ac010862f37c8dd99015a33ab5a3565fd8447")
            )
        )
        repl.start()
        thisReplicator = repl
    }

    fun replicationCustomHeaderExample(collections: Set<Collection>) {
        // Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
        val repl = Replicator(
            ReplicatorConfigurationFactory.newConfig(
                target = URLEndpoint(URI("ws://localhost:4984/mydatabase")),
                collections = mapOf(collections to null),
                headers = mapOf("CustomHeaderName" to "Value")
            )
        )
        repl.start()
        thisReplicator = repl
    }

    fun testReplicationPushFilter(collections: Set<Collection>) {
        val collectionConfig = CollectionConfigurationFactory.newConfig(
            pushFilter = { _, flags -> flags.contains(DocumentFlag.DELETED) } (1)
        )

        // Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
        val repl = Replicator(
            ReplicatorConfigurationFactory.newConfig(
                target = URLEndpoint(URI("ws://localhost:4984/mydatabase")),
                collections = mapOf(collections to collectionConfig)
            )
        )
        repl.start()
        thisReplicator = repl
    }

    fun replicationPullFilterExample(collections: Set<Collection>) {
        val collectionConfig = CollectionConfigurationFactory.newConfig(
            pullFilter = { document, _ -> "draft" == document.getString("type") } (1)
        )

        // Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
        val repl = Replicator(
            ReplicatorConfigurationFactory.newConfig(
                target = URLEndpoint(URI("ws://localhost:4984/mydatabase")),
                collections = mapOf(collections to collectionConfig)
            )
        )
        repl.start()
        thisReplicator = repl
    }

    // ### Reset replicator checkpoint
    fun replicationResetCheckpointExample(collections: Set<Collection>) {
        // Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
        val repl = Replicator(
            ReplicatorConfigurationFactory.newConfig(
                target = URLEndpoint(URI("ws://localhost:4984/mydatabase")),
                collections = mapOf(collections to null)
            )
        )

        repl.start(true)

        // ... at some later time

        repl.stop()
    }

    fun handlingNetworkErrorExample(collections: Set<Collection>) {
        val repl = Replicator(
            ReplicatorConfigurationFactory.newConfig(
                target = URLEndpoint(URI("ws://localhost:4984/mydatabase")),
                collections = mapOf(collections to null)
            )
        )

        repl.addChangeListener { change ->
            change.status.error?.let {
                log("Error code: ${it.code}")
            }
        }
        repl.start()
        thisReplicator = repl
    }

    // ### Certificate Pinning
    fun certificatePinningExample(collections: Set<Collection>, keyStoreName: String, certAlias: String) {
        val repl = Replicator(
            ReplicatorConfigurationFactory.newConfig(
                target = URLEndpoint(URI("ws://localhost:4984/mydatabase")),
                collections = mapOf(collections to null),
                pinnedServerCertificate = KeyStore.getInstance(keyStoreName)
                    .getCertificate(certAlias) as X509Certificate
            )
        )
        repl.start()
        thisReplicator = repl
    }

    fun replicatorConfigExample(collections: Set<Collection>) {
        // initialize the replicator configuration
        val thisConfig = ReplicatorConfigurationFactory.newConfig(
            target = URLEndpoint(URI("wss://10.0.2.2:8954/travel-sample")), (38)
            collections = mapOf(collections to null)
        )
    }

    fun p2pReplicatorStatusExample(repl: Replicator) {
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
    }

    fun p2pReplicatorStopExample(repl: Replicator) {
        // Stop replication.
        repl.stop() (39)
    }

    fun testCustomRetryConfig(collections: Set<Collection>) {
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
    }

    fun replicatorDocumentEventExample(collections: Set<Collection>) {
        val repl = Replicator(
            ReplicatorConfigurationFactory.newConfig(
                target = URLEndpoint(URI("ws://localhost:4984/mydatabase")),
                collections = mapOf(collections to null),
            )
        )

        val token = repl.addDocumentReplicationListener { replication ->
            log("Replication type: ${if (replication.isPush) "push" else "pull"}")

            for (document in replication.documents) {
                document.let { doc ->
                    log("Doc ID: ${document.id}")

                    doc.error?.let {
                        // There was an error
                        log("Error replicating document: ", it)
                        return@addDocumentReplicationListener
                    }

                    if (doc.flags.contains(DocumentFlag.DELETED)) {
                        log("Successfully replicated a deleted document")
                    }
                }
            }
        }

        repl.start()
        thisReplicator = repl

        token.remove()
    }

    private fun replicationPendingDocumentsExample(collection: Collection) {
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
                        log("Doc ID ${firstDoc} has been pushed")
                    }
                } catch (err: CouchbaseLiteException) {
                    log("Failed getting pending docs", err)
                }
            }

            repl.start()
            thisReplicator = repl
        }
    }

    fun collectionReplicationExample(srcCollections: Set<Collection>, targetDb: Database) {
        // This is an Enterprise feature:
        // the code below will generate a compilation error
        // if it's compiled against CBL Android Community Edition.
        // Note: the target database must already contain the
        //       source collections or the replication will fail.
        val repl = Replicator(
            ReplicatorConfigurationFactory.newConfig(
                target = DatabaseEndpoint(targetDb),
                collections = mapOf(srcCollections to null),
                type = ReplicatorType.PUSH
            )
        )

        // Start the replicator
        // (be sure to hold a reference somewhere that will prevent it from being GCed)
        repl.start()
        thisReplicator = repl
    }

    fun replicatorConfigurationExample(srcCollections: Set<Collection>, targetUrl: URI) {
        val repl = Replicator(
            ReplicatorConfigurationFactory.newConfig(
                target = URLEndpoint(targetUrl),

                collections = mapOf(srcCollections to null),

                // Configure Server Security
                // -- only accept CA attested certs
                acceptOnlySelfSignedServerCertificate = false, (40)


                // Use the pinned certificate from the byte array (cert)
                pinnedServerCertificate =
                TLSIdentity.getIdentity("Our Corporate Id")?.certs?.get(0) as? X509Certificate (41)
                    ?: throw IllegalStateException("Cannot find corporate id"),


                // Provide a client certificate to the server for authentication
                authenticator = ClientCertificateAuthenticator(
                    TLSIdentity.getIdentity("clientId")
                        ?: throw IllegalStateException("Cannot find client id")
                ) (42)

                // ... other replicator configuration
            )
        )

        thisReplicator = repl
    }

    fun ibReplicatorSimple(collections: Set<Collection>) {
        val theListenerEndpoint: Endpoint = URLEndpoint(URI("wss://10.0.2.2:4984/db")) (43)
        val repl = Replicator(
            ReplicatorConfigurationFactory.newConfig(
                collections = mapOf(collections to null),
                target = theListenerEndpoint,
                authenticator = BasicAuthenticator("valid.user", "valid.password.string".toCharArray()), (44)
                acceptOnlySelfSignedServerCertificate = true
            )
        )
        repl.start() (45)
        thisReplicator = repl
    }

    fun testReplicationWithCustomConflictResolver(srcCollections: Set<Collection>) {

        val collectionConfig = CollectionConfigurationFactory.newConfig(conflictResolver = LocalWinsResolver)
        val repl = Replicator(
            ReplicatorConfigurationFactory.newConfig(
                target = URLEndpoint(URI("ws://localhost:4984/mydatabase")),
                collections = mapOf(srcCollections to collectionConfig)
            )
        )

        // Start the replicator
        // (be sure to hold a reference somewhere that will prevent it from being GCed)
        repl.start()
        thisReplicator = repl
    }
}

/* C A L L O U T S

// Listener Callouts


<.> Initialize the listener instance using the configuration settings.
<.> Start the listener, ready to accept connections and incoming data from active peers.


<.> `connectionCount` -- the total number of connections served by the listener
<.> `activeConnectionCount` -- the number of active (BUSY) connections currently being served by the listener
//


<.> Configure the pinned certificate using data from the byte array `cert`

<.> Attempt to get the identity from secure storage
<.> Set the authenticator to ClientCertificateAuthenticator and configure it to use the retrieved identity


<.> A replication is an asynchronous operation.
To keep a reference to the `replicator` object, you can set it as an instance property.
<.> The URL scheme for remote database URLs uses `ws:`, or `wss:` for SSL/TLS connections over wb sockets.
In this example the hostname is `10.0.2.2` because the Android emulator runs in a VM that is generally accessible on `10.0.2.2` from the host machine (see https://developer.android.com/studio/run/emulator-networking[Android Emulator networking] documentation).
+
NOTE: As of Android Pie, version 9, API 28, cleartext support is disabled, by default.
Although `wss:` protocol URLs are not affected, in order to use the `ws:` protocol, applications must target API 27 or lower, or must configure application network security as described https://developer.android.com/training/articles/security-config#CleartextTrafficPermitted[here].

*/

//
// Copyright (c) 2023 Couchbase, Inc All rights reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
package com.couchbase.codesnippets

import android.app.Application
import com.couchbase.lite.CouchbaseLite
import com.couchbase.lite.Database
import com.couchbase.lite.LogDomain
import com.couchbase.lite.LogLevel


class SnippetApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        // Initialize the Couchbase Lite system
        CouchbaseLite.init(this)
    }

    fun troubleshootingExample() {
        CouchbaseLite.init(this, true)

        Database.log.console.setDomains(LogDomain.REPLICATOR)
        Database.log.console.level = LogLevel.DEBUG
    }
}
```

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

* A chain of one or more certificates that ends at a certificate in the list of certificates supplied to the constructor for [ListenerCertificateAuthenticator](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/ListenerCertificateAuthenticator.html) — see: [Example 9](#ex-set-cert-auth)
* Application logic: This method assumes complete responsibility for verifying and authenticating the client — see: [Example 10](#ex-use-app-logic)  
If the parameter supplied to the constructor for `ListenerCertificateAuthenticator` is of type `ListenerCertificateAuthenticatorDelegate`, all other forms of authentication are bypassed.  
The client response to the certificate request is passed to the method supplied as the constructor parameter. The logic should take the form of function or block (such as, a closure expression) where the platform allows.

Example 9\. Set Certificate Authorization

Configure the server (listener) to authenticate the client against a list of one or more certificates provided by the server to the the [ListenerCertificateAuthenticator](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/ListenerCertificateAuthenticator.html).

* Kotlin
* Java

```Kotlin
// Configure the client authenticator
// to validate using ROOT CA
// thisClientID.certs is a list containing a client cert to accept
// and any other certs needed to complete a chain between the client cert
// and a CA
val validId = TLSIdentity.getIdentity("Our Corporate Id")
    ?: throw IllegalStateException("Cannot find corporate id")

// accept only clients signed by the corp cert
val listener = URLEndpointListener(
    URLEndpointListenerConfigurationFactory.newConfig(
        // get the identity (1)
        collections = collections,
        identity = validId,
        authenticator = ListenerCertificateAuthenticator(validId.certs)
    )
) (2)
```

```Java
// Configure the client authenticator
// to validate using ROOT CA
// thisClientID.certs is a list containing a client cert to accept
// and any other certs needed to complete a chain between the client cert
// and a CA
final TLSIdentity validId =
    TLSIdentity.getIdentity("Our Corporate Id");  // get the identity (1)
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

Example 10\. Application Logic

Configure the server (listener) to authenticate the client using user-supplied logic.

* Kotlin
* Java

```Kotlin
// Configure authentication using application logic
val thisCorpId = TLSIdentity.getIdentity("OurCorp") (1)
    ?: throw IllegalStateException("Cannot find corporate id")

thisConfig.tlsIdentity = thisCorpId

thisConfig.authenticator = ListenerCertificateAuthenticator { certs ->
    // supply logic that returns boolean
    // true for authenticate, false if not
    // For instance:
    certs[0] == thisCorpId.certs[0]
} (2) (3)


val thisListener = URLEndpointListener(thisConfig)
```

```Java
// Configure authentication using application logic
final TLSIdentity thisCorpId = TLSIdentity.getIdentity("OurCorp"); (1)
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
URLEndpointListener listener = new URLEndpointListener(thisConfig);
listener.start();
thisListener = listener;
```

| **1** | Get the identity data to authenticate against. This can be, for example, from a resource file provided with the app, or an identity previously saved in secure storage.                                                                                                                 |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Configure the Authenticator to pass the root certificates to a user supplied code block. This code assumes complete responsibility for authenticating the client supplied certificate(s). It must return a boolean value; with true denoting the client supplied certificate authentic. |
| **3** | Add the authenticator to the Listener configuration.                                                                                                                                                                                                                                    |

### [](#delete-tls-identity)Delete Entry

You can remove unwanted entries from secure storage using the secure storage API (see — <https://developer.android.com/reference/java/security/KeyStore#deleteEntry%28java.lang.String%29>).

Example 11\. Deleting TLS Identities

* Kotlin
* Java

```Kotlin
val thisKeyStore = KeyStore.getInstance("AndroidKeyStore")
thisKeyStore.load(null)
thisKeyStore.deleteEntry(alias)
```

```Java
KeyStore thisKeyStore = KeyStore.getInstance("AndroidKeyStore");
thisKeyStore.load(null);
thisKeyStore.deleteEntry(alias);
```

### [](#the-impact-of-tls-settings)The Impact of TLS Settings

The table in this section shows the expected system behavior (in regards to security) depending on the TLS configuration settings deployed.

__Table 1\. Expected system behavior__
| disableTLS | tlsIdentity (corresponding to server)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Expected system behavior                                                                                                                                                                                                     |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| true       | Ignored                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | TLS is disabled; all communication is plain text.                                                                                                                                                                            |
| false      | set to nil                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | The system will auto generate an _anonymous_ self signed cert. Active Peers (clients) should be configured to accept self-signed certificates. Communication is encrypted                                                    |
| false      | Set to server identity generated from a self- or CA-signed certificate On first use — Bring your own certificate and private key; for example, using the [TLSIdentity](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/TLSIdentity.html) class's [createIdentity()](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/TLSIdentity.html#createIdentity-boolean-java.util.Map-java.util.Date-java.lang.String-) method to add it to the secure storage. Each time — Use the server identity from the certificate stored in the secure storage; for example, using the [TLSIdentity](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/TLSIdentity.html) class's [getIdentity()](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/TLSIdentity.html#getIdentity-java.lang.String-) method with the alias you want to retrieve.. | System will use the configured identity. Active Peers will validate the server certificate corresponding to the TLSIdentity (as long as they are configured to not skip validation — see [TLS Security](#lbl-tls-security)). |

## [](#lbl-start-listener)Start Listener

Once you have completed the Listener's configuration settings you can initialize the Listener instance and start it running — see: [Example 12](#initialize-and-start-listener)

Example 12\. Initialize and start listener

* Kotlin
* Java

```Kotlin
// Initialize the listener
val listener = URLEndpointListener(
    URLEndpointListenerConfigurationFactory.newConfig(
        collections = collections, (1)
        port = 55990, (2)
        networkInterface = "wlan0", (3)

        enableDeltaSync = false, (4)

        // Configure server security
        disableTls = false, (5)

        // Use an Anonymous Self-Signed Cert
        identity = null, (6)

        // Configure Client Security using an Authenticator
        // For example, Basic Authentication (7)
        authenticator = ListenerPasswordAuthenticator { usr, pwd ->
            (usr === validUser) && (validPass.contentEquals(pwd))
        }
    ))

// Start the listener
listener.start() (8)
```

```Java
// Initialize the listener
final URLEndpointListener thisListener
    = new URLEndpointListener(thisConfig); (1)

// Start the listener
thisListener.start(); (2)
```

## [](#monitor-listener)Monitor Listener

Use the Listener's `[getStatus](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/URLEndpointListener.html#getStatus--)` property/method to get counts of total and active connections — see: [Example 13](#get-connection-counts).

You should note that these counts can be extremely volatile. So, the actual number of active connections may have changed, by the time the `[ConnectionStatus](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/com/couchbase/lite/ConnectionStatus.html)` class returns a result.

Example 13\. Get connection counts

* Kotlin
* Java

```Kotlin
val connectionCount = listener.status?.connectionCount (1)
val activeConnectionCount = listener.status?.activeConnectionCount (2)
```

```Java
int connectionCount =
    thisListener.getStatus().getConnectionCount(); (1)

int activeConnectionCount =
    thisListener.getStatus().getActiveConnectionCount();  (2)
```

## [](#stop-listener)Stop Listener

It is best practice to check the status of the Listener's connections and stop only when you have confirmed that there are no active connections — see [Example 13](#get-connection-counts).

Example 14\. Stop listener using `stop` method

* Kotlin
* Java

```Kotlin
val listener = thisListener
thisListener = null
listener?.stop()
```

```Java
thisListener.stop();
```

> [!NOTE]
> Closing the database will also close the Listener.

## [](#related-content)Related Content

###### [](#)

How to

* [Passive Peer](p2psync-websocket-using-passive.md)
* [Active Peer](p2psync-websocket-using-active.md)

###### [](#-2)

Concepts

* [Peer-to-Peer Sync](#android:landing-p2psync.adoc)
* [API References](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-android/)

###### [](#-3)

Community Resources …​

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

[Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)