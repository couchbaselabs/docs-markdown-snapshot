---
title: Sync
editUrl: https://github.com/couchbaselabs/mobile-travel-sample/edit/master/content/modules/mobile-travel-tutorial/pages/csharp/develop/sync.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:tutorials:mobile-travel-tutorial:csharp/develop/sync.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/mobile-travel-tutorial/csharp/develop/sync.html)

# Sync

\[[1](#%5Ffootnotedef%5F1 "View footnote.")\] \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

## [](#%5Fchannelsdata%5Frouting)Channels/Data Routing

In the lesson on [Access Control](security.md#access-control)we discussed how Sync Gateway supports Authorization and Access Control functions. In this lesson we discuss how it can be used for Data Synchronization and Routing.

A Sync Gateway configuration file determines the runtime behavior of Sync Gateway, including server configuration and the database or set of databases with which a Sync Gateway instance can interact.

* Sync Gateway uses channels to make it easy to share a database between a large number of users and control access to the database. Conceptually, a channel could be viewed as a tag. Every document in the database belongs to a set of channels, and a user is granted appropriate access a set of channels. A channel is used to
* Partition the data set
* Authorize users to access documents.
* Minimize the amount of data synced down to devices.

In the "Installation" guide, we walked you through the steps to launch Sync Gateway with a specific config file. Open the sync-gateway-config-travelsample.json file located at <https://github.com/couchbaselabs/mobile-travel-sample/blob/master/sync-gateway-config-travelsample.json>. It includes the `sync function` which is a JavaScript function whose source code is stored in the Sync Gateway's database configuration file.

```javascript
/* Routing */
// Add doc to the user's channel.
channel("channel." + username);
```

## [](#shared-bucket-access)Shared Bucket Access

Before you begin this lesson, confirm that you have Sync Gateway up and running by following the instructions in the [Sync Gateway installation](../installation/index.md)section.

Sync Gateway and Couchbase Server \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] mobile and server/web applications can read and write to the same bucket. It is an opt-in feature that can be enabled in the Sync Gateway configuration file.

![convergence](../../_images/convergence.png) 

The sync metadata used by the Sync Gateway for replication with mobile clients is located in the Extended Attributes or XAttrs associated with the document.

The capability can be enabled through a configuration setting in the sync gateway config file. It is to be noted that if you are using Enterprise Edition of Sync Gateway \[[2](#%5Ffootnotedef%5F2 "View footnote.")\], then the "import\_docs" flag is optional. Every node with "enable\_shared\_bucket\_access" set to "true" will automatically import document mutations from the server bucket.

Open the sync-gateway-config-travelsample.json file located at <https://github.com/couchbaselabs/mobile-travel-sample/blob/master/sync-gateway-config-travelsample.json>

```javascript
"import_docs": "continuous",
"enable_shared_bucket_access": true
```

You can specify the Couchbase Server documents that need to be imported and processed by the Sync Gateway by defining an import filter function.

In our demo, we will only be synchornizing the "user" document. So every other document type is ignored.

```javascript
"import_filter": `
function(doc) {
  /* Just ignore all the static travel-sample files */
  if (doc._deleted == true ) {
    return true;
   }
  if (doc.type == "landmark" || doc.type == "hotel" || doc.type == "airport" || doc.type =="airline" || doc.type == "route") {
    return false;
  }

  return true;
} `
```

## [](#replication)Replication

Replication is the process by which clients running Couchbase Lite synchronize database changes with the remote (server) database.

* Pull Replication is the process by which clients running Couchbase Lite download database changes from the remote (server) source database to the local target database
* Push Replication is the process by which clients running Couchbase Lite upload database changes from the local source database to the remote (server) target database

Couchbase Mobile's replication protocol is implemented as a messaging protocol layered over WebSocket.

![replication 2 0](../../_images/replication-2-0.png) 

The replication process can be "continuous" or "\`one shot"\`.

* In "Continuous" replication mode, the changes are continually synchronized between the client and Sync Gateway in real time.
* In "One shot" mode, the changes are synchronized once and the connection between the client and server disconnects. When any future changes need to be pushed up or pulled down, the client must start a new replication.

**Open the file**`LoginModel.cs`. We will review the method `StartReplication(string username, string password, Database db)`

[LoginModel.cs](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/dotnet/TravelSample/TravelSample.Core/Models/LoginModel.cs#L103)

```csharp
private Replicator StartReplication(string username, string password, Database db)
  ...
}
```

First, Do some checks to confirm the validity of the user credentials

```csharp
if (String.IsNullOrWhiteSpace(username) || String.IsNullOrWhiteSpace(password)){
  throw new InvalidOperationException("User credentials not provided");
}
```

Create the URL of the Sync Gateway

```csharp
private static readonly Uri SyncUrl = new Uri("ws://localhost:4984");
var dbUrl = new Uri(SyncUrl, DbName);
```

The `ReplicatorConfiguration` is initialized with the local database and URL of the target DB on Sync Gateway. The `ReplicatorType` in the Replicator Config specifies the type of replication. In the code snippet in the Travel app, it is `PushAndPull` indicating that both push and pull replication is enabled. The `Continuous` mode is set to `true` in the Travel app.

```csharp
var config = new ReplicatorConfiguration(db, new URLEndpoint(dbUrl)) {
  ReplicatorType = ReplicatorType.PushAndPull,
  Continuous = true,
  ...
};
```

The Replicator is configured with relevant authentication credentials. In the Travel app, the list of users that are permitted access is configured in the Sync Gateway configuration file as discussed in the [Access Control](/develop/csharp#/2/2/1) section

```csharp
var config = new ReplicatorConfiguration(db, dbUrl) {
    ...
    Authenticator = new BasicAuthenticator(username, password),
    ...
};
```

The Replicator is configured to only pull from current user's channels. The list of channels that the user has access to is defined in the Sync Gateway configuration file as discussed in the [Channels/ Data Routing](/develop/csharp#/2/3/0) section

```csharp
var config = new ReplicatorConfiguration(db, dbUrl) {
    ...
    Channels = new[] {$"channel.{username}"}
};
```

The Replicator is initialized with the specified configuration

```csharp
var repl = new Replicator(config);
```

A change listener callback block is registered to listen for replication changes. Every time, there is a push or pull change, the callback is invoked.

```csharp
repl.AddChangeListener((sender, args) =>
{
  var s = args.Status;
  Debug.WriteLine(
      $"PushPull Replicator: {s.Progress.Completed}/{s.Progress.Total}, error {s.Error?.Message ?? "<none>"}, activity = {s.Activity}");

});
```

Start the Replication

```csharp
repl.Start();
```

### [](#try-push-replication)Try Push Replication

Try it out (Mobile App)

1. Log into the Travel Sample Mobile app as "demo" user and password as "password"
2. Tap on "+" button to make a flight reservation
3. Leave the default airport in the "From" field
4. Leave the default airport in the "To" field
5. Enter From and/or Return Dates
6. Tap "lookup" button
7. From list of flights, select the first flight listing
8. Select "Confirm Booking" — see: [Book a Flight \[1\]](#fig-net-pushrepl)

Book a Flight \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

![uwp push replication](../../_images/uwp_push_replication.gif)

* Access the Travel Sample Python Web app. The URL would be <http://localhost:8080>. If you did cloud based install, please replace `localhost` in the URL with the IP Address of the cloud instance of the web app.
* Log into the web app as "demo" user with password as "password"
* Use the "Booked" tab to navigate to the list of booked flights
* Confirm that you see the flight that you reserved via the mobile app in your list of flights in the web app

![travel app push](../../_images/travel-app-push.gif) 

### [](#try-it-out-pull-replication)Try it out (Pull Replication)

Try it out (Web App)

1. Access the Travel Sample Python Web app. The URL would be <http://localhost:8080>. If you did cloud based install, please replace `localhost` in the URL with the IP Address of the cloud instance of the web app.
2. Log into the web app as "demo" user with password as "password"
3. Make a flight reservation by clicking the "Flights" tab
4. Enter "From" airport as "Seattle" and select the airport from drop down menu.
5. Enter "To" airport as "San Francisco" and select the airport from drop down menu.
6. Enter From and Return Travel Dates
7. Click on "Search" button
8. From list of flights, select the first flight listing by clicking on the corresponding "Add to Basket" button
9. Confirm the booking by clicking on the "Basket" tab to view the flight selections and then click on the "Buy" button
10. The "Booked" tab should show the confirmed flight reservations
11. If you are not already logged into the mobile app, Log into the Travel Sample Mobile app as "demo" user and password as "password"
12. Confirm that you see the flight that you reserved via the web app in your list of flights in the mobile app

![travel app pull](../../_images/travel-app-pull.gif) 

Figure 1\. Book a Flight \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

---

[1](#%5Ffootnoteref%5F1). The screen capture is for UWP version of the app. 

[1](#%5Ffootnoteref%5F1). 1.5+/5.0+ 

[2](#%5Ffootnoteref%5F2). 2.7+