---
title: Getting Started with Peer-to-Peer Sync on iOS
editUrl: https://github.com/couchbaselabs/couchbase-lite-peer-to-peer-sync-examples/edit/master/content/modules/cbl-p2p-sync-websockets/pages/swift/cbl-p2p-sync-websockets.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:tutorials:cbl-p2p-sync-websockets:swift/cbl-p2p-sync-websockets.adoc[]
---

[View original HTML](/tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.html)

# Getting Started with Peer-to-Peer Sync on iOS

> This tutorial uses a simple inventory tracker app to demonstrate Couchbase Lite’s peer-to-peer database sync functionality. 

## [](#introduction)Introduction

Couchbase Lite \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] provides out-of-the-box support for secure [Peer-to-Peer Sync](../../../couchbase-lite/current/swift/p2psync-websocket.md), over websockets. The sync, between Couchbase Lite enabled clients in IP-based networks, does not require a centralized control point. You do not need a Sync Gateway or Couchbase Server to get peer-to-peer database sync going.

What You Will Learn

This tutorial will demonstrate how to -

* Use [NetService](https://developer.apple.com/documentation/foundation/netservice)for peer discovery (i.e.to advertise and discover services/devices )
* Configure a websockets listener to listen to incoming requests. We will walk through various TLS modes and client authentication modes.
* Start a bi-directional replication from active peer.
* Sync data between connected peers

Throughout this tutorial, these terms are used interchangeably:

* "passive peer", "server" and "listener" all refer to the peer on which the websocket listener is started
* "active peer" and "client" both refer to the peer on which the replicator is initialized.

We will be using a simple inventory app in swift as an example to demonstrate the peer-to-peer functionality.

You can learn more about Couchbase Lite [here](../../../couchbase-lite/current/index.md)

## [](#prerequisites)Prerequisites

This tutorial assumes familiarity with building swift apps with Xcode and with Couchbase Lite.

* If you are unfamiliar with the basics of Couchbase Lite, it is recommended that you follow the [Getting Started](../../../couchbase-lite/current/swift/gs-install.md)guides
* iOS (Xcode 12+)

  * Download latest version from the [Mac App Store](https://itunes.apple.com/us/app/xcode/id497799835?mt=12)
* Wi-Fi network that the peers can communicate over  
You could run your peers in multiple simulators. But if you were running the app on real devices, you will need to ensure that the devices are on the same WiFi network

## [](#app-overview)App Overview

This is a simple inventory app that can be used as a [passive](../../../couchbase-lite/current/swift/p2psync-websocket-using-passive.md) or [active](../../../couchbase-lite/current/swift/p2psync-websocket-using-active.md) peer.

The app uses a local database that is pre-populated with data. There is no Sync Gateway or Couchbase Server installed.

When used as a passive peer:

* Users log in and start websockets listener for the couchbase lite database. A service corresponding to the listener is advertised over Bonjour.
* View the status of connected clients
* Directly sync data with connected clients

When used as an active peer, users can:

* Log in and start browsing for peers
* Connect to a listener
* Directly sync data with connected clients.

![peer to peer sync](../_images/ios-demo.gif) 

## [](#app-installation)App Installation

* Clone the repo  
```bash  
git clone https://github.com/couchbaselabs/couchbase-lite-peer-to-peer-sync-examples  
```
* The app project does not come bundled with the Couchbase Lite framework. Run the script to pull down the framework  
```bash  
cd /path/to/cloned/repo/couchbase-lite-peer-to-peer-sync-examples/ios/list-sync  
sh install_12.sh  
```

Try it Out

1. Open the iOS project using Xcode  
```bash  
open list-sync.xcodeproj  
```
2. Build and run the project
3. Verify that you see the login screen

![app login screen](../_images/swift-login.png) 

Figure 1\. App in Action

## [](#exploring-the-app-project)Exploring the App Project

* The xcode project comes pre-bundled with some resource files that we will examine here

![xcode project explorer](../_images/swift-project-explorer.png) 

* `samplelist.json`  
JSON data that is loaded into the local Couchbase Lite database. It includes the data for a single document. See [Data Model](#data-model)
* `userallowlist.json`  
List of valid client users (and passwords) in the system. This list is looked up when the server tries to authenticate credentials associated with incoming connection request.
* `listener-cert-pkey.p12`  
This is [PKCS12](https://en.wikipedia.org/wiki/PKCS%5F12)file archive that includes a public key cert corresponding to the listener and associated private key. The cert is a sample cert that was generated using [OpenSSL](https://www.openssl.org)tool.
* `listener-pinned-cert.cer`  
This is the public key listener cert (the same cert that is embedded in the `listener-cert-pkey.p12` file) in DER encoded format. This cert is pinned on the client replicator and is used for validating server cert during connection setup

## [](#data-model)Data Model

Couchbase Lite is a JSON Document Store. A Document is a logical collection of named fields and values. The values are any valid JSON types. In addition to the standard JSON types, Couchbase Lite supports some special types like `Date` and `Blob`. While it is not required or enforced, it is a recommended practice to include a _"type"_ property that can serve as a namespace for related.

### [](#the-list-document)The "List" Document

The app deals with a single Document with a _"type"_ property of _"list"_. This document is loaded from the `samplelist.json` file bundled with the project

Sample List Document

```json
{
    "type":"list",
    "list":[
      {
         "image":{"length":16608,"digest":"sha1-LEFKeUfywGIjASSBa0l/cg5rlm8=","content_type":"image/jpeg","@type":"blob"},
          "value":10,
          "key":"Apples"
      },
      {
        "image":{"length":16608,"digest":"sha1-LEFKeUsswGIjASssSBa0l/cg5rlm8=","content_type":"image/jpeg","@type":"blob"},
        "value":110,
        "key":"oranges"
       }
    ]

}
```

The document is encoded as a `ListRecord` struct defined in the `ListRecord.swift` file

### [](#initializing-local-database)Initializing Local Database

The app loads the data from the JSON document named `samplelist.json` the first time the database is created. This is done regardless of whether the app is launched in passive or active mode.

* Open the **DatabaseManager.swift** file and locate the `openOrCreateDatabaseForUser()` method. This method creates an instance of Couchbase Lite database for the user if one does not exist and loads the empty database with data ready from bundled sample JSON file

```swift
        var exists = false
        if Database.exists(withName: kUserDBName, inDirectory: userFolderPath) == true {
              _userDb = try? Database(name: kUserDBName, config: options)
            exists = true
 
        }
        else {
              _userDb = try? Database(name: kUserDBName, config: options)
              
        }
```

* Open the **SampleFileLoaderUtils.swift** file and locate the `loadSampleJSONDataForUserFromFile()` method. This function parses the document in JSON and updates it to embed the "image" property into every object in the "list" array. The "image" property holds a blob entry to an image asset. The image for the blob is available in the "Assets.xcassets" folder
* Open the **DatabaseManager.swift** file and locate the `createUserDocumentWithData()` method. This is where the document is saved into the database. Again, this is only done if there is no preexisting database for the user

```swift
        for (key,value) in data {
            let docId = "\(kDocPrefix)\(key)"
            print("DocId is \(docId)")
            let doc = MutableDocument(id:docId, data:value as! Dictionary<String, Any>)
            try db.saveDocument(doc)
        }
```

## [](#passive-peer-or-server)Passive Peer or Server

First, we will walk through the steps of using the app in passive peer mode

### [](#initializing-websockets-listener)Initializing Websockets Listener

* Open the **DatabaseManager.swift** file and locate the `initWebsocketsListenerForUserDb()` function. This is where the websockets listener for peer-to-peer sync is initialized

```swift
        // Include websockets listener initializer code
        var listenerConfig = URLEndpointListenerConfiguration(database: db) (1)
        
        // Configure the appropriate auth test mode
        switch listenerTLSSupportMode { (2)
            case .TLSDisabled:
                listenerConfig.disableTLS  = true
                listenerConfig.tlsIdentity = nil
            case .TLSWithAnonymousAuth:
                listenerConfig.disableTLS  = false // Use with anonymous self signed cert
                listenerConfig.tlsIdentity = nil
             case .TLSWithBundledCert:
                
                if let tlsIdentity = self.importTLSIdentityFromPKCS12DataWithCertLabel(kListenerCertLabel) {
                    listenerConfig.disableTLS  = false
                    listenerConfig.tlsIdentity = tlsIdentity
                }
                else {
                    print("Could not create identity from provided cert")
                    throw ListDocError.WebsocketsListenerNotInitialized
                }
            case .TLSWithGeneratedSelfSignedCert:
                if let tlsIdentity = self.createIdentityWithCertLabel(kListenerCertLabel) {
                    listenerConfig.disableTLS  = false
                    listenerConfig.tlsIdentity = tlsIdentity
                }
                else {
                    print("Could not create identity from generated self signed cert")
                    throw ListDocError.WebsocketsListenerNotInitialized
                }

        
        }
        
        listenerConfig.enableDeltaSync = true (3)
        
        listenerConfig.authenticator = ListenerPasswordAuthenticator.init { (4)
                   (username, password) -> Bool in
            if (self._allowlistedUsers.contains(["password" : password, "name":username])) {
                return true
            }
            return false
               }
        
        _websocketListener = URLEndpointListener(config: listenerConfig)
```

| **1** | Initialize the URLEndpointListenerConfiguration for the specified database. There is a listener for a given database. You can specify a port to be associated with the listener. In our app, we let Couchbase Lite choose the port                                                       |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | This is where we configure the TLS mode. In the app, we have a flag named listenerTLSSupportMode that allows the app to switch between the various modes. You can change the mode by changing the value of the variable. See [Testing Different TLS Modes](#testing-different-tls-modes) |
| **3** | Enable delta sync. It is disabled by default                                                                                                                                                                                                                                             |
| **4** | Configure the password authenticator callback function that authenticates the username/password received from the client during replication setup. The list of valid users are configured in userallowlist.json file bundled with the app                                                |

#### [](#testing-different-tls-modes)Testing Different TLS Modes

The app can be configured to test different TLS modes by changing the `listenerTLSSupportMode` setting property in the `DatabaseManager.swift` file — see values in [Table 1](#tbl%5Ftls%5Fmodes).

This flag operates in conjunction with \`listenerCertValidationMode — see: [Testing Different Server Authentication Modes](#testing-different-server-authentication-modes). Recommended combinations are shown in [Table 2](#tbl%5Fmode%5Fcombos).

```swift
         fileprivate let listenerCertValidationMode:ListenerCertValidationTestMode = .TLSSkipValidation
```

__Table 1\. TLS Modes on Listener__
| listenerTLSSupportMode Value   | Behavior                                                                                                                                                                                                                    |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TLSDisabled                    | There is no TLS. All communication is plaintext (insecure mode and not recommended in production)                                                                                                                           |
| TLSWithAnonymousAuth           | The app uses self-signed cert that is auto-generated by Couchbase Lite as TLSIdentity of the server. While server authentication is skipped, all encryption is still encrypted. This is the default mode of Couchbase Lite. |
| TLSWithBundledCert             | The app generates TLSIdentity of the server from public key cert and private key bundled in the listener-cert-pkey.p12 archive. Communication is encrypted                                                                  |
| TLSWithGeneratedSelfSignedCert | The app uses Couchbase Lite createIdentity convenience API to generate the TLSIdentity of the server. Communication is encrypted                                                                                            |

__Table 2\. Recommended combination of flags__
| TLS Mode                                           | Validation Mode                                                   |
| -------------------------------------------------- | ----------------------------------------------------------------- |
| ListenerTLSTestMode.TLSDisabled                    | ListenerCertValidationTestMode.TLSSkipValidation                  |
| ListenerTLSTestMode.TLSWithAnonymousAuth           | ListenerCertValidationTestMode.TLSSkipValidation                  |
| ListenerTLSTestMode.TLSWithBundledCert             | ListenerCertValidationTestMode.TLSEnableValidationWithCertPinning |
| ListenerTLSTestMode.TLSWithGeneratedSelfSignedCert | ListenerCertValidationTestMode.TLSSkipValidation (edited)         |

### [](#start-websockets-listener)Start Websockets Listener

* Open the **DatabaseManager.swift** file and locate the `startWebsocketsListenerForUserDb()` method.

```swift
        DispatchQueue.global().sync {
            do {
                try websocketListener.start()
                handler(websocketListener.urls,nil)
            }
            catch {
                handler(nil,error)
            }
    
        }
```

### [](#advertising-listener-service)Advertising Listener Service

In the app, we use [NetService](https://developer.apple.com/documentation/foundation/netservice) to advertise the websockets listener service listening at the specified listener port. This aspect of the app has nothing to do with Couchbase Lite. In your production app, you can use any suitable mechanism including using a well known URL to advertise your service that active clients can be pre-configured to connect to.

* Open the **ServiceAdvertiser.swift** file and look for `ServiceAdvertiser` class. Here, we advertise a [Bonjour](https://developer.apple.com/bonjour/) service with service type of _\`\_cblistservicesync.\_tcp\`_

```swift
  /// The Bonjour service name. Setting it to an empty String will be
  /// mapped to the device's name.
  public var serviceName: String = ""
  
  /// The Bonjour service type.
  public var serviceType = "_cblistservicesync._tcp"
  
 /// The Bonjour domain type.
 public var serviceDomain = ""
```

* The service is published as implemented in the `doStart()` method.

```swift
    private func doStart(database:String, _ port:UInt16) {
        let service = NetService(domain: serviceDomain, type: serviceType,
                                 name: serviceName, port:Int32(port))

        service.delegate = self
        service.includesPeerToPeer = true
        service.publish()
        services[database] = service

    }
```

Explore the content in the `ServiceAdvertiser.swift`. It includes implementation of the `NetServiceDelegate` delegate callback methods to accept incoming connections.

### [](#stop-websockets-listener)Stop Websockets Listener

* Open the **DatabaseManager.swift** file and locate the `stopWebsocketsListenerForUserDb()` method. You can stop the listener at any point. If there are connected clients, it will warn you that there are active connections. If you choose to stop listener, all connected clients will be disconnected

```swift
    func stopWebsocketsListenerForUserDb() throws{
        print(#function)
        guard let websocketListener = _websocketListener else {
            throw ListDocError.WebsocketsListenerNotInitialized
        }
        websocketListener.stop()
        _websocketListener = nil
    }
```

Try it out

* Run the app on a simulator or a real device. If its the latter, make sure you sign your app with the appropriate developer certificate
* On login screen, sign in as any one of the users configured in the `userallowlist.json` file such as "bob" and "password"
* From the "listener" tab, start the listener by clicking on "Start Listener" button
* Click on the "action" button to see number of connected clients. It should be 0 if there are no connected clients
* From the "listener" tab, stop the listener by clicking on "Stop Listener" button

![server websockets listener login screen](../_images/ios-passive-start-listener.gif) 

Figure 2\. App in action - start passive peer

## [](#active-peer-or-client)Active Peer or Client

We will walk through the steps of using the app in active peer mode

### [](#discovering-listeners)Discovering Listeners

In the app, we use [NetService](https://developer.apple.com/documentation/foundation/netservice) to browse for devices that are advertising services with name _\`\_cblistservicesync.\_tcp\`_. This aspect of the app has nothing to do with Couchbase Lite. In your production app, you could launch your listener at well known URL well and pre-configure your active peer to connect to the URL.

* Open the **ServiceBrowser.swift** file and look for `ServiceBrowser` class. Here, we browse for a service with service type of _\`\_cblistservicesync.\_tcp\`_ using [Bonjour](https://developer.apple.com/bonjour/)

```swift
    public func startSearch(withDelegate delegate:ServiceBrowserDelegate? ){
         peerBrowserDelegate = delegate
        self.browser = NetServiceBrowser()
        self.browser?.delegate = self
        self.browser?.searchForServices(ofType: serviceType, inDomain: domain)
    }
```

Explore the content in the `ServiceBrowser.swift`. It includes implementation of the `NetServiceDelegate` delegate callback methods to resolve the service to its IP Address and port that will be used by the client to connect to the listener.

### [](#initializing-and-starting-replication)Initializing and Starting Replication

Initializing a replicator for peer-to-peer sync is fundamentally the same as the case if the Couchbase Lite client were to [sync](../../../couchbase-lite/current/swift/replication.md)with a remote Sync Gateway.

* Open the **DatabaseManager.swift** file and locate the `startP2PReplicationWithUserDatabaseToRemotePeer()` method.  
If you have been using Couchbase Lite to sync data with Sync Gateway, this code should seem very familiar. In this function, we initialize a bi-directional replication to the listener peer in continuous mode. We also register a Replication Listener to be notified of status to the replication status.

```swift
        if replicatorForUserDb == nil {
            // Start replicator to connect to the URLListenerEndpoint
            var target = URL(string: "wss://\(peer)/\(kUserDBName)")
            switch listenerTLSSupportMode {
            case .TLSDisabled:
                target = URL(string: "ws://\(peer)/\(kUserDBName)")
            default:
                target = URL(string: "wss://\(peer)/\(kUserDBName)")
            }
            guard let targetUrl = target else {
                throw ListDocError.URLInvalid
            }
            print("\(#function) with \(targetUrl)")
         
            
            var config = ReplicatorConfiguration.init(database: userDb, target: URLEndpoint.init(url:targetUrl)) (1)

            config.replicatorType = .pushAndPull
            config.continuous =  true
            
            // Explicitly allows self signed certificates. By default, only
            // CA signed cert is allowed
            switch listenerCertValidationMode { (2)
                  
                case .TLSSkipValidation :
                    // Use acceptOnlySelfSignedServerCertificate set to true to only accept self signed certs.
                    // There is no cert validation
                    config.acceptOnlySelfSignedServerCertificate = true
                                
                
                case .TLSEnableValidationWithCertPinning:
                    // Set acceptOnlySelfSignedServerCertificate set to false if you are using CA signed certs
                    // Set acceptOnlySelfSignedServerCertificate when listener is setup with self signed certs
                   
                    config.acceptOnlySelfSignedServerCertificate = true // since app is bundled with self signed cert
                    
                    // Enable cert pinning to only allow certs that match pinned cert
                    
                    if let pinnedCert = self.loadSelfSignedCertForListenerFromBundle() {
                        config.pinnedServerCertificate = pinnedCert
                    }
                    else {
                        print("Failed to load server cert to pin. Will proceed without pinning")
                    }
                
                case .TLSEnableValidation:
                     // Use acceptOnlySelfSignedServerCertificate set to false to only accept CA signed certs
                     // Self signed certs will fail validation. There is no cert pinning
                    config.acceptOnlySelfSignedServerCertificate = false
                
                            
            }
             
            
            let authenticator = BasicAuthenticator(username: user, password: password)(3)
            config.authenticator = authenticator

            replicatorForUserDb = Replicator.init(config: config) (4)
            _replicatorsToPeers[peer] = replicatorForUserDb

          }
        if let pushPullReplListenerForUserDb = registerForEventsForReplicator(replicatorForUserDb,handler:handler) {
            _replicatorListenersToPeers[peer] = pushPullReplListenerForUserDb
        
        }

            
        replicatorForUserDb?.start() (5)
        handler(PeerConnectionStatus.Connecting)
```

| **1** | Initialize a Repicator Configuration for the specified local database and remote listener URL endpoint                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | This is where we configure the TLS server cert validation mode - whether we enable cert validation or skip validation. This would only apply if you had enabled TLS support on listener as discussed in [Table 1](#tbl%5Ftls%5Fmodes). If you skip server cert validation, you still get encrypted communication, but you are communicating with a untrusted listener. In the app, we have a flag named listenerCertValidationMode that allows you to try the various modes. You can change the mode by changing the value of the variable. See [Testing Different Server Authentication Modes](#testing-different-server-authentication-modes) |
| **3** | The app uses basic client authentication to authenticate with the server                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **4** | Initialize the Replicator                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **5** | Start replication. The app uses the events on the Replicator Listener to listen to monitor the replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

#### [](#testing-different-server-authentication-modes)Testing Different Server Authentication Modes

In [Initializing Websockets Listener](#initializing-websockets-listener) section, we discussed the various ways the listener TLSIdentity can be configured. Here, we describe the corresponding changes on the replicator side to authenticate the server identity. The app can be configured to test different TLS modes as follows by setting the `listenerCertValidationMode` property in the `DatabaseManager.swift` file — see possible values in [Table 3](#tbl%5Fcert%5Fauth%5Fmodes).

This flag operates in conjunction with `listenerTLSSupportMode`. Recommended combinations are shown in [Table 2](#tbl%5Fmode%5Fcombos).

Naturally, if you initialized the listener with `TLSDisabled` mode, skip this section as there is no TLS.

```swift
         fileprivate let listenerCertValidationMode:ListenerCertValidationTestMode = .TLSSkipValidation
```

__Table 3\. TLS Listener Cert Authentication__
| listenerCertValidationMode Value   | Behavior                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TLSSkipValidation                  | There is no authentication of server cert. The server cert is a self-signed cert. This is typically in used in dev or test environments. Skipping server cert authentication is discouraged in production environments. Communication is encrypted.                                                                                                                                |
| TLSEnableValidation                | If the listener cert is from well known CA then you will use this mode. Of course, in our sample app, the listener cert as specified in listener-cert-pkey is a self signed cert - so you probably will not use this mode to test. But if you have a CA signed cert, you can configure your listener with the CA signed cert and use this mode to test. Communication is encrypted |
| TLSEnableValidationWithCertPinning | In this mode, the app uses the pinned cert,listener-pinned-cert.cer that is bundled in the app to validate the listener identity. Only the server cert that exactly matches the pinned cert will be authenticated. Communication is encrypted                                                                                                                                      |

### [](#stopping-replication)Stopping Replication

* Open the **DatabaseManager.swift** file and locate the `stopP2PReplicationWithUserDatabaseToRemotePeer()` method.  
If you have been using Couchbase Lite to sync data with Sync Gateway, this code should seem very familiar. In this function, we remove any listeners attached to the replicator and stop it. You can restart the replicator again in `startP2PReplicationWithUserDatabaseToRemotePeer()` method

```swift
        if let listener = _replicatorListenersToPeers[peer] {
            replicator.removeChangeListener(withToken: listener)
            _replicatorListenersToPeers.removeValue(forKey: peer)
        }
        
        replicator.stop()
```

Try it out

1. Follow instructions in "Try It Out" section of [Passive Peer or Server](#passive-peer-or-server) to start app in passive mode on a simulator instance or real device.
2. Run the app on a separate simulator instance or a real device. If its the latter, make sure you sign your app with the appropriate developer certificate
3. On login screen, sign in as any one of the users configured in the `userallowlist.json` file such as "bob" and "password". As an exercise, try with an invalid user and ensure it fails
4. Tap on the "browser" tab. The app automatically browses for listener and lists it here.
5. Tap on the row corresponding to listener. This will start replication with the listener and it should transition to Connected state
6. Verify the connection count on listener
7. Swipe left on the the row. You should see option to remove listener and Disconnect. Try Disconnect and then reconnect again

![p2p sync](../_images/ios-active-start-replicator.gif) 

Figure 3\. App in action — start active peer

## [](#syncing-data)Syncing Data

Once the connection is established between the peers, you can start syncing. Couchbase Lite takes care of it.

Try it out

1. Run the app on two or more simulators or real devices. If it’s the latter, make sure you sign your app with the appropriate developer certificate
2. Start the listener on one of the app instances. You could also have multiple listeners.
3. Connect the other instances of the app to the listener
4. Tap on the "List" tab
5. Edit the quantity or image on any one of the instances
6. Watch it sync automatically to other connected clients

![server websockets listener login screen](../_images/ios-sync.gif) 

Figure 4\. App in action — sync

## [](#what-next)What Next

As an exercise, switch between the various TLS modes and server cert validation modes and see how the app behaves. You can also try with different topologies to connect the peers.

## [](#learn-more)Learn More

Congratulations on completing this tutorial!

This tutorial walked you through an example of how to directly synchronize data between Couchbase Lite enabled clients. While the tutorial is for iOS, the concepts apply equally to other Couchbase Lite platforms.

Further Reading

Complete documentation is available [here](../../../couchbase-lite/current/swift/p2psync-websocket.md)

---

[1](#%5Ffootnoteref%5F1). Release 2.8+