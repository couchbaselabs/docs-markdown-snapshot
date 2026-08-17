---
title: Sync
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/mobile-travel-sample/edit/master/content/modules/mobile-travel-tutorial/pages/swift/develop/sync.adoc
  xref: xref:tutorials:mobile-travel-tutorial:swift/develop/sync.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/mobile-travel-tutorial/swift/develop/sync.html)

# Sync

## [](#data-routing)Data Routing

In the [Access Control](security.md#access-control)lesson we discussed how Sync Gateway supports Authorization and Access Control functions. In this lesson we discuss how it can be used for Data Synchronization and Routing.

A Sync Gateway configuration file determines the runtime behavior of Sync Gateway, including server configuration and the database or set of databases with which a Sync Gateway instance can interact.

Sync Gateway uses channels to make it easy to share a database between a large number of users and control access to the database. Conceptually, a channel could be viewed as a tag. Every document in the database belongs to a set of channels, and a user is granted appropriate access a set of channels. A channel is used to:

* Partition the data set.
* Authorize users to access documents.
* Minimize the amount of data synced down to devices.

In the [backend installation](#{param-module}/installation/index.adoc)section, we walked you through the steps to launch Sync Gateway with a specific config file.

Open the sync-gateway-config-travelsample.json file located at <https://github.com/couchbaselabs/mobile-travel-sample/blob/master/sync-gateway-config-travelsample.json>. It includes the `sync function` which is a JavaScript function whose source code is stored in the Sync Gateway's database configuration file.

```javascript
/* Routing */
// Add doc to the user's channel.
channel("channel." + username);
```

## [](#shared-bucket-access)Shared Bucket Access

Before you begin this lesson, confirm that you have Sync Gateway up and running by following the instructions in the [Sync Gateway installation](../installation/index.md)section.

Sync Gateway and Couchbase Server \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] mobile and server/web applications now have the ability to read and write to the same bucket. It is an opt-in feature that can be enabled in the Sync Gateway configuration file.

![convergence](../../_images/convergence.png) 

The sync metadata used by the Sync Gateway for replication with mobile clients is included in the Extended Attributes or XAttrs associated with the document.

The capability can be enabled through a configuration setting in the sync gateway config file. It is to be noted that if you are using Enterprise Edition of Sync Gateway \[[2](#%5Ffootnotedef%5F2 "View footnote.")\], then the "import\_docs" flag is optional. Every node with "enable\_shared\_bucket\_access" set to "true" will automatically import document mutations from the server bucket.

Open the sync-gateway-config-travelsample.json file located at <https://github.com/couchbaselabs/mobile-travel-sample/blob/master/sync-gateway-config-travelsample.json>

```javascript
"import_docs": "continuous",
"enable_shared_bucket_access": true
```

You can specify the Couchbase Server documents that need to be imported and processed by the Sync Gateway by defining an import filter function. In our demo, we will only be synchronizing the "user" document. So every other document type is ignored.

```javascript
function(doc) {
  /* Just ignore all the static travel-sample files */
  if (doc._deleted == true ) {
    return true;
   }
  if (doc.type == "landmark" || doc.type == "hotel" || doc.type == "airport" || doc.type =="airline" || doc.type == "route") {
    return false;
  }

  return true;
}
```

## [](#replication)Replication

Replication is the process by which clients running Couchbase Lite synchronize database changes with the remote (server) database.

* Pull Replication is the process by which clients running Couchbase Lite download database changes from the remote (server) source database to the local target database
* Push Replication is the process by which clients running Couchbase Lite upload database changes from the local source database to the remote (server) target database

Couchbase Mobile's replication protocol is implemented as a messaging protocol layered over WebSocket.

![replication 2 0](../../_images/replication-2-0.png)

The replication process can be "continuous" or "\`one shot"\`.

* In "Continuous" replication mode, the changes are continually synchronized between the client and Sync Gateway.
* In "One shot" mode, the changes are synchronized once and the connection between the client and server disconnects. When any future changes need to be pushed up or pulled down, the client must start a new replication.

**Open the file**`DatabaseManager.swift`. We will review the method `func startPushAndPullReplicationForCurrentUser()`

[DatabaseManager.swift](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/ios/TravelSample/TravelSample/Model/DatabaseManager.swift#L202)

```swift
func startPushAndPullReplicationForCurrentUser() {
  ...
}
```

First, you fetch the URL of the Sync Gateway

```swift
guard let remoteUrl = URL.init(string: kRemoteSyncUrl) else {
  lastError = TravelSampleError.RemoteDatabaseNotReachable

  return
}
```

Do some checks to confirm the validity of the database and user credentials

```swift
guard let user = self.currentUserCredentials?.user,let password =   self.currentUserCredentials?.password  else {
  lastError = TravelSampleError.UserCredentialsNotProvided
  return
}

guard let db = db else {
  lastError = TravelSampleError.RemoteDatabaseNotReachable
  return
}
```

Verify that the replicator is not already in progress

```swift
if _pushPullRepl != nil {
  // Replication is already started
  return
}
```

The `ReplicatorConfiguration` is initialized with the local database and URL of the target DB on Sync Gateway. The `replicatorType` in the Replicator Config specifies the type of replication. In the code snippet in the Travel app, it is `pushAndPull` indicating that both push and pull replication is enabled. The `continuous` mode is set to `true` in the Travel app.

```swift
fileprivate let kRemoteSyncUrl = "ws://localhost:4984"
let dbUrl = remoteUrl.appendingPathComponent(kDBName)

let config = ReplicatorConfiguration.init(database: db, target: URLEndpoint.init(url:dbUrl))

config.replicatorType = .pushAndPull
config.continuous =  true
```

The Replicator is configured with relevant authentication credentials. In the Travel app, the list of users that are permitted access is configured in the Sync Gateway configuration file as discussed in the [Access Control](security.md#acccess-control) section.

```swift
config.authenticator = BasicAuthenticator(username: user, password: password)
```

The Replicator is configured to **only** pull from current user's channels. The list of channels that the user has access to is defined in the Sync Gateway configuration file as discussed in the [Data Routing](#data-routing) section.

```swift
// This should match what is specified in the sync gateway config
// Only pull documents from this user's channel
let userChannel = "channel.\(user)"
config.channels = [userChannel]
```

The Replicator is initialized with the specified configuration

```swift
_pushPullRepl = Replicator.init(config: config)
```

A change listener callback block is registered to listen for replication changes. Every time, there is a push or pull change, the callback is invoked.

```swift
_pushPullReplListener = _pushPullRepl?.addChangeListener({ [weak self] (change) in
    let s = change.status
    print("PushPull Replicator: \(s.progress.completed)/\(s.progress.total), error: \(String(describing: s.error)), activity = \(s.activity)")

    if s.progress.completed == s.progress.total {
        self?.postNotificationOnReplicationState(.idle)
    }
    else {
        self?.postNotificationOnReplicationState(s.activity)
    }
})
```

Start the Replication

```swift
_pushPullRepl?.start()
```

### [](#try-push-replication)Try Push Replication

Try it out — Book a Flight

1. Log into the Travel Sample Mobile app as "demo" user and password as "password"
2. Tap on "+" button to make a flight reservation
3. Enter "From" airport as SFO and select the airport from drop down menu
4. Enter "To" airport as DTW and select the airport from drop down menu
5. Enter From (01/20/2020) and Return (02/20/2020) Dates
6. Tap "lookup" button
7. From list of flights, select the first flight listing
8. Select "Confirm Booking" — see: [Figure 1](#fig-swift-bookflight)

![ios push sync](../../_images/ios_push_sync.gif) 

Figure 1\. Book a Flight in Mobile App

Try it out — Check the Flight Details Sync'd

1. Access the Travel Sample Python Web app. The URL would be <http://localhost:8080>. If you did cloud based install, please replace `localhost` in the URL with the IP Address of the cloud instance of the web app.
2. Log into the web app as "demo" user with password as "password"
3. Use the "Booked" tab to navigate to the list of booked flights
4. Confirm that you see the flight that you reserved via the mobile app in your list of flights in the web app

![travel app push](../../_images/travel-app-push.gif) 

Figure 2\. View Booking in WebApp

### [](#try-out-pull-replication)Try out Pull Replication

Try it out — Book Flight in WebApp

1. Access the Travel Sample Python Web app. The URL would be <http://localhost:8080>. If you did cloud based install, please replace `localhost` in the URL with the IP Address of the cloud instance of the web app.
2. Log into the web app as "demo" user with password as "password"
3. Make a flight reservation by clicking the "Flights" tab
4. Enter "From" airport as "Seattle Tacoma Intl" and select the airport from drop down menu.
5. Enter "To" airport as "San Francisco Intl" and select the airport from drop down menu.
6. Enter From (20/01/2020) and Return (20/02/2020) Travel Dates
7. Click on "Search" button
8. From list of flights, select the first flight listing by clicking on the corresponding "Add to Basket" button
9. Confirm the booking by clicking on the "Basket" tab to view the flight selections and then click on the "Buy" button
10. The "Booked" tab should show the confirmed flight reservations — see: [Figure 3](#fig-swift-bookflightweb)

![travel app pull](../../_images/travel-app-pull.gif) 

Figure 3\. Book Flight in WebApp

Try it out — Check Booking in Mobile App

1. Log into the Travel Sample Mobile app as "demo" user and password as "password"
2. Confirm that you see the flight that you reserved via the web app in your list of flights in the mobile app

---

[1](#%5Ffootnoteref%5F1). 1.5/5.0 

[2](#%5Ffootnoteref%5F2). 2.7+