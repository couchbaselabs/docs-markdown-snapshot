---
title: Getting Started with Peer-to-Peer Sync on Xamarin (UWP, iOS, and Android)
editUrl: https://github.com/couchbaselabs/couchbase-lite-peer-to-peer-sync-examples/edit/master/content/modules/cbl-p2p-sync-websockets/pages/dotnet/cbl-p2p-sync-websockets.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:tutorials:cbl-p2p-sync-websockets:dotnet/cbl-p2p-sync-websockets.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/cbl-p2p-sync-websockets/dotnet/cbl-p2p-sync-websockets.html)

# Getting Started with Peer-to-Peer Sync on Xamarin (UWP, iOS, and Android)

> This tutorial uses a simple inventory tracker app to demonstrate Couchbase Lite's peer-to-peer database sync functionality. 

## [](#introduction)Introduction

Couchbase Lite \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] provides out-of-the-box support for secure [Peer-to-Peer Sync](../../../couchbase-lite/current/csharp/p2psync-websocket.md), over websockets. The sync, between Couchbase Lite enabled clients in IP-based networks, does not require a centralized control point. You do not need a Sync Gateway or Couchbase Server to get peer-to-peer database sync going.

What You Will Learn

We will be using a simple inventory app as an example to demonstrate the peer-to-peer functionality, including:

* How to use a UDP type socket to listen on a specified port for peer discovery. Broadcast its own IP address over UDP type socket.
* How to configure a websockets listener to listen to incoming requests. We will walk through various TLS modes and client authentication modes.
* How to start a bi-directional replication from active peer.
* How to sync data between connected peers

> [!NOTE]
> You need to add the UWP app to the Exception list on the Windows Firewall.

Throughout this tutorial, these terms are used interchangeably:

* "passive peer", "server" and "listener" all refer to the peer on which the websocket listener is started
* "active peer" and "client" both refer to the peer on which the replicator is initialized.

You can learn more about Couchbase Lite [here](../../../couchbase-lite/current/index.md)

## [](#prerequisites)Prerequisites

This tutorial assumes familiarity with building Xamarin apps with Visual Studio and with Couchbase Lite.

* Visual Studio 2019 (Download it from the [Microsoft Website](https://visualstudio.microsoft.com/downloads/)) with:

  * Universal Windows Platform component installed
  * Xamarin component installed (for Android and iOS development).
* If you are unfamiliar with the basics of Couchbase Lite, it is recommended that you follow the [Getting Started](../../../couchbase-lite/current/csharp/gs-install.md)guides
* Wi-Fi network that the peers can communicate over  
You could run your peers in multiple simulators. But if you were running the app on real devices, you will need to ensure that the devices are on the same Wi-Fi network.

## [](#app-overview)App Overview

This is a simple inventory app that can be used as a [passive](../../../couchbase-lite/current/csharp/p2psync-websocket-using-passive.md) or [active](../../../couchbase-lite/current/csharp/p2psync-websocket-using-active.md) peer.

The app uses a local database that is pre-populated with data. There is no Sync Gateway or Couchbase Server installed.

When used as a passive peer:

* Users log in and start websockets listener for the couchbase lite database.  
The Listener IP endpoint is advertised over UDP type socket when users enter the `ListenerPage`.
* View the status of connected clients
* Directly sync data with connected clients.

When used as an active peer, users can:

* Log in and enter the `ListenersBrowserPage` to start browsing for peers
* Connect to a listener
* Directly sync data with connected clients.

## [](#app-installation)App Installation

* Clone the repo  
```bash  
git clone https://github.com/couchbaselabs/couchbase-lite-peer-to-peer-sync-examples  
```

### [](#exercise)Exercise

Try it Out

1. Open the Xamarin .NET project using Visual Studio
2. Build and run the project  
If you are running Android apps on emulators, please see [Connecting to an Android emulator](#connecting-to-an-android-emulator)
3. Verify that you see the login screen
4. If you are having trouble running the Xamarin iOS sample app, please see [Having issue running the Xamarin iOS app?](#having-issue-running-the-xamarin-ios-app)  
![app login screen](../_images/cs-login.png)

![peer to peer sync](../_images/xamarin-demo.gif) 

Figure 1\. The app in action

## [](#exploring-the-app-project)Exploring the App Project

* The Xamarin .NET project comes pre-bundled with some resource files that we will examine here.

![xcode project explorer](../_images/cs-project-explorer.png) 

* `userdb.cblite2.zip` :  
A zip file containing a prebuilt Couchbase Lite database. It includes the data for a single document. See [Data Model](#data-model)
* `userallowlist.json` :  
List of valid client users (and passwords) in the system. This list is looked up when the server tries to authenticate credentials associated with incoming connection request.
* `listener-cert-pkey.p12` :  
This is [PKCS12](https://en.wikipedia.org/wiki/PKCS%5F12)file archive that includes a public key cert corresponding to the listener and associated private key. The cert is a sample cert that was generated using [OpenSSL](https://www.openssl.org)tool.
* `listener-pinned-cert.cer` :  
This is the public key listener cert (the same cert that is embedded in the `listener-cert-pkey.p12` file) in DER encoded format. This cert is pinned on the client replicator and is used for validating server cert during connection setup.

## [](#data-model)Data Model

Couchbase Lite is a JSON Document Store. A Document is a logical collection of named fields and values. The values are any valid JSON types. In addition to the standard JSON types, Couchbase Lite supports some special types like `Date` and `Blob`. While it is not required or enforced, it is a recommended practice to include a _"type"_ property that can serve as a namespace for related.

### [](#the-list-document)The "List" Document

The app deals with a single Document with a _"type"_ property of _"list"_.

An example of a document would be

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

### [](#initializing-local-database)Initializing Local Database

The app extracts a prebuilt database zip file named `userdb.cblite2.zip` into `DBPath` the first time the database is created. This is done regardless of whether the app is launched in passive or active mode.

* Open the **CoreApp.cs** file and locate the `LoadAndInitDB` method.  
This method extracts the Couchbase Lite database into `DBPath` for the user (if one does not already exist).

```C#
if (!Database.Exists(DbName, DBPath)) {
    using (var dbZip = new ZipArchive(ResourceLoader.GetEmbeddedResourceStream(typeof(CoreApp).GetTypeInfo().Assembly, $"{DbName}.cblite2.zip"))) {
        dbZip.ExtractToDirectory(DBPath);
    }
}

DB = new Database(DbName, new DatabaseConfiguration() { Directory = DBPath });
```

* Open the **SeasonalItemsViewModel.cs** file and locate the `SeasonalItemsViewModel` constructor.  
It creates a LiveQuery to pick up document changes in the inventory list array when the ViewModel loads the first time. Each array item contains a dictionary with three key value pairs. Their keys are `key`, `value`, and `image`. Their values are mapped to the properties `Name`, `Quantity`, and `Image` in .NET Object `SeasonalItem`. The `image` property holds a blob entry to an image.

```C#
var q = QueryBuilder.Select(SelectResult.All())
    .From(DataSource.Database(_db))
    .Where(Meta.ID.EqualTo(Expression.String(CoreApp.DocId)))
    .AddChangeListener((sender, args) =>
    {
        var allResult = args.Results.AllResults();
        var result = allResult[0];
        var dict = result[CoreApp.DB.Name].Dictionary;
        var arr = dict.GetArray(CoreApp.ArrKey);

        if (arr.Count < Items.Count)
            Items = new ObservableConcurrentDictionary<int, SeasonalItem>();

        Parallel.For(0, arr.Count, i =>
        {
            var item = arr[i].Dictionary;
            var name = item.GetString("key");
            var cnt = item.GetInt("value");
            var image = item.GetBlob("image");

            if (_items.ContainsKey(i)) {
                _items[i].Name = name;
                _items[i].Quantity = cnt;
                _items[i].ImageByteArray = image?.Content;
            } else {
                var seasonalItem = new SeasonalItem {
                    Index = i,
                    Name = name,
                    Quantity = cnt,
                    ImageByteArray = image?.Content
                };

                _items.Add(i, seasonalItem);
            }

        });
    });
```

## [](#passive-peer-or-server)Passive Peer or Server

First, we will walk through the steps of using the app in passive peer mode.

### [](#initializing-websocket-listener)Initializing Websocket Listener

* Open the **ListenerViewModel.cs** file and locate the `CreateListener` function.  
This is where the websocket listener for peer-to-peer sync is initialized.

```C#
var listenerConfig = new URLEndpointListenerConfiguration(_db); (1)
listenerConfig.NetworkInterface = GetLocalIPv4(NetworkInterfaceType.Wireless80211) ?? GetLocalIPv4(NetworkInterfaceType.Ethernet);
//listenerConfig.Port = 0; // Dynamic port
listenerConfig.Port = 35262; // Fixed port

switch (CoreApp.ListenerTLSMode) { (2)
    case LISTENER_TLS_MODE.DISABLED:
        listenerConfig.DisableTLS = true;
        listenerConfig.TlsIdentity = null;
        break;
    case LISTENER_TLS_MODE.WITH_ANONYMOUS_AUTH:
        listenerConfig.DisableTLS = false; // Use with anonymous self signed cert if TlsIdentity is null
        listenerConfig.TlsIdentity = null;
        break;
    case LISTENER_TLS_MODE.WITH_BUNDLED_CERT:
        listenerConfig.DisableTLS = false;
        listenerConfig.TlsIdentity = ImportTLSIdentityFromPkc12(ListenerCertLabel);
        break;
    case LISTENER_TLS_MODE.WITH_GENERATED_SELF_SIGNED_CERT:
        listenerConfig.DisableTLS = false;
        listenerConfig.TlsIdentity = CreateIdentityWithCertLabel(ListenerCertLabel);
        break;
}

listenerConfig.EnableDeltaSync = true; (3)

if (CoreApp.RequiresUserAuth) { (4)
    listenerConfig.Authenticator = new ListenerPasswordAuthenticator((sender, username, password) =>
    {
        // ** This is only a sample app to use an existing users credential shared cross platforms.
        //    Developers should use SecureString password properly.
        var found = CoreApp.AllowedUsers.Where(u => username == u.Username && new NetworkCredential(string.Empty, password).Password == u.Password).SingleOrDefault();
        return found != null;
    });
}

_urlEndpointListener = new URLEndpointListener(listenerConfig);
```

| **1** | Initialize the URLEndpointListenerConfiguration for the specified database. There is a listener for a given database. You can specify a port to be associated with the listener, or let Couchbase Lite choose the port. We have hard-coded 35262 (in SeasonalItemsViewModel.cs).  |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | This is where we configure the TLS mode. In the app, we have a flag named ListenerTLSMode that allows the app to switch between the various modes. You can change the mode by changing the value of the variable. See [Testing Different TLS Modes](#testing-different-tls-modes) |
| **3** | Enable delta sync. It is disabled by default                                                                                                                                                                                                                                      |
| **4** | Configure the password authenticator callback function. This function authenticates the username/password received from the client during replication setup. The list of valid users are configured in userallowlist.json file bundled with the app                               |

#### [](#testing-different-tls-modes)Testing Different TLS Modes

The app can be configured to test different TLS modes as follows by setting the `ListenerTLSMode` property in the `CoreApp.cs` file

```C#
public static LISTENER_CERT_VALIDATION_MODE ListenerCertValidationMode = LISTENER_CERT_VALIDATION_MODE.SKIP_VALIDATION;
```

__Table 1\. TLS Modes on Listener__
| ListenerTLSMode Value               | Behavior                                                                                                                                                                                                                       |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| DISABLED                            | There is no TLS. All communication is plaintext (insecure mode and not recommended in production)                                                                                                                              |
| WITH\_ANONYMOUS\_AUTH               | The app uses self-signed cert that is auto-generated by Couchbase Lite as TLSIdentity of the server. While server authentication is skipped, all communication is still encrypted. This is the default mode of Couchbase Lite. |
| WITH\_BUNDLED\_CERT                 | The app generates TLSIdentity of the server from public key cert and private key bundled in the listener-cert-pkey.p12 archive. Communication is encrypted                                                                     |
| WITH\_GENERATED\_SELF\_SIGNED\_CERT | The app uses Couchbase Lite CreateIdentity convenience API to generate the TLSIdentity of the server. Communication is encrypted                                                                                               |

### [](#start-websocket-listener)Start Websocket Listener

* Open the **ListenerViewModel.cs** file and locate the `ExecuteStartListenerCommand` method.

```C#
_urlEndpointListener.Start();
```

### [](#advertising-listener-service)Advertising Listener Service

In the app, we broadcast listener's IP endpoint over UDP type socket.

* Open the **ListenerViewModel.cs** file and look for `Broadcast` method.+ Here, we create a Socket with Udp ProtocolType and broadcast listener's IP endpoint to the peers are listening in local network.  
Please note, this App requires peers to start peer discovery before listener start broadcasting. Otherwise, you will have to manually broadcast the listener IP. Please see [Try it out](#tryit10) for detail.

```C#
public void Broadcast()
{
    if (!IsListening)
        return;

    using (var socket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, System.Net.Sockets.ProtocolType.Udp)) {
        socket.EnableBroadcast = true;
        var group = new IPEndPoint(IPAddress.Broadcast, CoreApp.UdpPort);
        var hi = Encoding.ASCII.GetBytes($"{CoreApp.Guid}:{_urlEndpointListener.Urls[0].Host}:{_urlEndpointListener.Port}");
        socket.SendTo(hi, group);

        socket.Close();
    }
}
```

### [](#stop-websocket-listener)Stop Websocket Listener

* Open the **ListenerViewModel.cs** file and locate the `ExecuteStartListenerCommand` method.+ You can stop the listener after the listener is started.

```C#
_urlEndpointListener.Stop();
_urlEndpointListener.Dispose();
```

### [](#exercise-2)Exercise

Try it out

1. Run the app on a simulator or a real device. If it is the latter, make sure you sign your app with the appropriate developer certificate
2. On the login screen, sign in as any one of the users configured in the `userallowlist.json` file, such as "bob" and "password"
3. You can find 4 selections (`What’s in Season?`, `Listener`, `Browser`, and `Logout`) under the "hamburger" menu located on the upper left hand side.
4. From the `ListenerPage`, select `Listener` from the "hamburger" menu, start the listener by clicking on "Start Listener" button
5. You can see 2 toolbar items (`Broadcast` and `Peers`)  
Note: These two items will do nothing if listener is not started.
6. Click on the "Peers" toolbar item to see the number of connected clients. It should be zero if there are no connected clients
7. If you don't see your listener's IP endpoint showing up on a peers' `ListenersBrowserPage`, click on the listener's "Broadcast" toolbar item to broadcast its IP endpoint
8. From the `ListenerPage`, stop the listener by clicking on "Stop Listener" button

![server websocket listener login screen](../_images/xamarin-passive-start-listener.gif) 

Figure 2\. App in action - start passive peer

## [](#active-peer-or-client)Active Peer or Client

We will walk through the steps of using the app in active peer mode

### [](#discovering-listeners)Discovering Listeners

In the app, we use UDP Type Socket to listen on port 15000 for listener.  
Please note, port 15000 is used by UDP Type Socket, not used by the websocket listener.+ Couchbase Lite chooses the port when a websocket listener is created.

* Open the **ListenersBrowserViewModel.cs** file and look for `ListenersBrowserViewModel` constructor.  
Here, we create a `UdpListener` with the port it listens on and pick up any raised Udp packet received event (Listener's broadcasting IP endpoint).

```C#
{
    Title = "Browser";
    Items = new ObservableCollection<ReplicatorItem>();

    _discovery = new UdpListener(CoreApp.UdpPort);
    _discovery.UdpPacketReceived += DiscoveryOnUdpPacketReceived;
    _discovery.Start();
}

#region discover event
private void DiscoveryOnUdpPacketReceived(object sender, UdpPacketReceivedEventArgs args)
{
    var msg = Encoding.ASCII.GetString(args.Data);
    var msgArr = msg.Split(':');
    var remoteId = Guid.Parse(msgArr[0]);
    if (remoteId == CoreApp.Guid) return;
    var remoteIP = IPAddress.Parse(msgArr[1]);
    var remotePort = Int32.Parse(msgArr[2]);
    var remoteEndpoint = new IPEndPoint(remoteIP, remotePort);

    AddReplicator(remoteEndpoint);
}
```

Explore the content in the `UdpListener.cs`. It includes implementation of creating Socket with Udp ProtocolType, start and stop the listener, and `UdpPacketReceived` EventHandler.

### [](#initializing-and-starting-replication)Initializing and Starting Replication

Initializing a replicator for peer-to-peer sync is fundamentally the same as the case if the Couchbase Lite client were to [sync](../../../couchbase-lite/current/csharp/replication.md)with a remote Sync Gateway.

* Open the **ReplicatorItem.cs** file and locate the `ExecuteStartReplicatorCommand` method.  
If you have been using Couchbase Lite to sync data with Sync Gateway, this code should seem very familiar. In this function, we initialize a bi-directional replication to the listener peer in continuous mode. We also register a Replication Listener to be notified of status to the replication status.

```C#
public ReplicatorItem(IPEndPoint listenerEndpoint)
{
    _listenerEndpoint = listenerEndpoint;
    StartReplicatorCommand = new Command(() => ExecuteStartReplicatorCommand());
    CreateReplicator(ListenerEndpointString);
}

~ReplicatorItem()
{
    Dispose(disposing: false);
}
#endregion

public void CreateReplicator(string PeerEndpointString)
{
    if(_repl != null) {
        return;
    }

    Uri host = new Uri(PeerEndpointString);
    var dbUrl = new Uri(host, _db.Name);
    var replicatorConfig = new ReplicatorConfiguration(_db, new URLEndpoint(dbUrl)); (1)
    replicatorConfig.ReplicatorType = ReplicatorType.PushAndPull;
    replicatorConfig.Continuous = true;

    if (CoreApp.ListenerTLSMode > 0) {

        // Explicitly allows self signed certificates. By default, only
        // CA signed cert is allowed
        switch (CoreApp.ListenerCertValidationMode) { (2)
            case LISTENER_CERT_VALIDATION_MODE.SKIP_VALIDATION:
                // Use acceptOnlySelfSignedServerCertificate set to true to only accept self signed certs.
                // There is no cert validation
                replicatorConfig.AcceptOnlySelfSignedServerCertificate = true;
                break;

            case LISTENER_CERT_VALIDATION_MODE.ENABLE_VALIDATION_WITH_CERT_PINNING:
                // Use acceptOnlySelfSignedServerCertificate set to false to only accept CA signed certs
                // Self signed certs will fail validation

                replicatorConfig.AcceptOnlySelfSignedServerCertificate = false;

                // Enable cert pinning to only allow certs that match pinned cert

                try {
                    var pinnedCert = LoadSelfSignedCertForListenerFromBundle();
                    replicatorConfig.PinnedServerCertificate = pinnedCert;
                } catch (Exception ex) {
                    Debug.WriteLine($"Failed to load server cert to pin. Will proceed without pinning. {ex}");
                }

                break;

            case LISTENER_CERT_VALIDATION_MODE.ENABLE_VALIDATION:
                // Use acceptOnlySelfSignedServerCertificate set to false to only accept CA signed certs
                // Self signed certs will fail validation. There is no cert pinning
                replicatorConfig.AcceptOnlySelfSignedServerCertificate = false;
                break;
        }
    }

    if (CoreApp.RequiresUserAuth) {
        var user = CoreApp.CurrentUser;
        replicatorConfig.Authenticator = new BasicAuthenticator(user.Username, user.Password); (3)
    }

    _repl = new Replicator(replicatorConfig); (4)
    _listenerToken = _repl.AddChangeListener(ReplicationStatusUpdate);
}

public void ExecuteStartReplicatorCommand()
{
    if (!IsStarted) {
        _repl.Start(); (5)
```

| **1** | Initialize a Repicator Configuration for the specified local database and remote listener URL endpoint                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | This is where we configure the TLS server cert validation mode - whether we enable cert validation or skip validation. This would only apply if you had enabled TLS support on listener as discussed in [TLS Modes on Listener](#tlsmodes).If you skip server cert validation, you still get encrypted communication, but you are communicating with an un-trusted listener.In the app, we have a flag named ListenerCertValidationMode that allows you to try the various modes. You can change the mode by changing the value of the variable. See [Testing Different Server Authentication Modes](#testing-different-server-authentication-modes) |
| **3** | The app uses basic client authentication to authenticate with the server                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **4** | Initialize the Replicator                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **5** | Start replication. The app uses the events on the Replicator Listener to listen to monitor the replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

#### [](#testing-different-server-authentication-modes)Testing Different Server Authentication Modes

In [Initializing Websocket Listener](#initializing-websocket-listener) section, we discussed the various ways the listener TLSIdentity can be configured. Here, we describe the corresponding changes on the replicator side to authenticate the server identity. The app can be configured to test the different TLS modes ([Table 2](#tlscertauth)) by setting the `ListenerCertValidationMode` property in the `CoreApp.cs` file.

Naturally, if you have initialized the listener with `TLSDisabled` mode, then skip this section as there is no TLS.

```C#
public static LISTENER_CERT_VALIDATION_MODE ListenerCertValidationMode = LISTENER_CERT_VALIDATION_MODE.SKIP_VALIDATION;
```

__Table 2\. TLS Listener Cert Authentication__
| ListenerCertValidationMode Value        | Behavior                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SKIP\_VALIDATION                        | There is no authentication of server cert. The server cert is a self-signed cert. This is typically used in dev or test environments. Skipping server cert authentication is discouraged in production environments. Communication is encrypted.                                                                                                                                      |
| ENABLE\_VALIDATION                      | If the listener cert is from a well known CA then you will use this mode. Of course, in our sample app, the listener cert as specified in listener-cert-pkey is a self signed cert - so you probably will not use this mode to test. But if you have a CA signed cert, you can configure your listener with the CA signed cert and use this mode to test. Communication is encrypted. |
| ENABLE\_VALIDATION\_WITH\_CERT\_PINNING | In this mode, the app uses the pinned cert,listener-pinned-cert.cer that is bundled in the app to validate the listener identity. Only the server cert that exactly matches the pinned cert will be authenticated. Communication is encrypted.                                                                                                                                        |

### [](#stopping-replication)Stopping Replication

* Open the **ReplicatorItem.cs** file and locate the `StopReplicator` method.+ If you have been using Couchbase Lite to sync data with Sync Gateway, this code should seem very familiar. In this function, we remove any listeners attached to the replicator and stop it. You can restart the replicator with `ExecuteStartReplicatorCommand` method

```C#
_repl?.Stop();
```

### [](#exercise-3)Exercise

Try it out

1. Follow instructions in the [Try it out](#tryit10) section of [Passive Peer or Server](#passive-peer-or-server) to start app in passive mode on a simulator instance or real device.
2. Run the app on a separate simulator instance or a real device. If its the latter, make sure you sign your app with the appropriate developer certificate
3. On login screen, sign in as any one of the users configured in the `userallowlist.json` file such as "bob" and "password". As an exercise, try with an invalid user and ensure it fails
4. You can find 4 selections (`What’s in Season?`, `Listener`, `Browser`, and `Logout`) under the "hamburger" menu located on the upper left hand side.
5. Select "Browser" from the "hamburger" menu.  
The app automatically browses for listener and lists it here when any listener is broadcasting.  
> [!NOTE]  
> If the listener is not started before the "Browser" is selected, you will need to click the `Broadcast` toolbar item locates on top of the `ListenerPage` (See `Broadcast` in [Passive Peer or Server](#passive-peer-or-server))  
> You will need to manually enter the listener's IP endpoint (eg: 192.168.0.14:59840) for Xamarin android app.
6. Tap on the row corresponding to listener.  
This will start replication with the listener and it should transition to Connected state  
> [!NOTE]  
> If you [Cannot connect Android app active peer to passive peer when you are using Xamarin.Android SDK 9.x or other older version?](#cannot-connect-android-app-active-peer-to-passive-peer-when-you-are-using-xamarin-android-sdk-9-x-or-other-older-version)
7. Verify the connection count on listener by clicking "Peers" toolbar item locates on top of the `ListenerPage` (See `Broadcast` in [Passive Peer or Server](#passive-peer-or-server))
8. Tap on the row corresponding to listener again.  
This will stop replication with the listener and it should transition to Disconnected state. Try Disconnect and then reconnect again
9. Swipe left (iOS) or long press (Android) or left click (UWP) on the the row. You should see the option to remove listener

![p2p sync](../_images/xamarin-active-start-replicator.gif) 

Figure 3\. App in action — start active peer

## [](#syncing-data)Syncing Data

Once the connection is established between the peers, you can start syncing. Couchbase Lite takes care of it.

### [](#exercise-4)Exercise

Try it out

1. Run the app on two or more simulators or real devices.  
If its the latter, make sure you sign your app with the appropriate developer certificate
2. Start the listener on one of the app instances. You could also have multiple listeners.
3. Connect the other instances of the app to the listener
4. You can find 4 selections (`What’s in Season?`, `Listener`, `Browser`, and `Logout`) under "hamburger" menu locates on the upper left hand side.
5. Enter `SeasonalItemsPage` by selecting "What's in Season?" from the "hamburger" menu.
6. Edit the quantity and/or image on one or multiple instance(s) and press Save when you are done editing
7. Watch it sync automatically to other connected clients

![server websocket listener login screen](../_images/xamarin-sync.gif) 

Figure 4\. App in action — sync

## [](#what-next)What Next

As an exercise, switch between the various TLS modes and server cert validation modes and see how the app behaves. You can also try with different topologies to connect the peers.

## [](#learn-more)Learn More

Congratulations on completing this tutorial!

This tutorial walked you through an example of how to directly synchronize data between Couchbase Lite enabled clients. While the tutorial is for iOS, the concepts apply equally to other Couchbase Lite platforms.

Further Reading

Complete documentation is available [here](../../../couchbase-lite/current/csharp/p2psync-websocket.md)

## [](#troubleshoot)Troubleshoot

### Having issue running the Xamarin iOS app?

* Xamarin iOS p2p sample app should build and run with Visual Studio 2019 with latest updates and XCode 12.0.1
* If you have Xcode 11 and try to run the iOS app on simulator and the simulator is not loading, try to launch the simulator via Xcode and select that simulator when launching it from VS.

### Connecting to an Android emulator

> [!IMPORTANT]
> Sync will not work between two emulators. At least one app must be running on a device.

When starting a listener on Android emulator and trying to connect it from a device or iOS simulator on localhost, the following steps must be followed:

1. Hard-code a port so you know what endpoint to use
2. Start the App on your device or iOS simulator
3. Start an Android emulator from Visual Studio's device manager
4. Use ADB bridge to set port forwarding using hard-coded port number  
For instance, if the listener is listening on port 35262, the command to run on the terminal of the host machine would be:  
```bash  
adb forward tcp:35262 tcp:35262  
```
5. On your device or iOS simulator,

  1. Within the App, select **Browser**
  2. Enter your required endpoint including the hard-coded port number  
  > [!NOTE]  
  > You cannot connect to an emulator directly over localhost.  
  > Regardless of the IP address in the displayed URL, ignore it and use `127.0.0.1` as the host address.  
  > For example, if the listener is listening on `10.2.0.15:35262`,  
  > you must connect to URL `127.0.0.1:35262`.
6. Within the Android emulater app, **Start listener**  
You can make an inventory change and see the change sync to the other app.

### Cannot connect Android app active peer to passive peer when you are using Xamarin.Android SDK 9.x or other older version?

Go to `Advanced Android Options` (Android Project Properties → Android Options → Advanced button) and change `SSL/TLS implementation` configuration to `Managed TLS 1.0` from `Native TLS 1.2+`.

---

[1](#%5Ffootnoteref%5F1). Release 2.8+