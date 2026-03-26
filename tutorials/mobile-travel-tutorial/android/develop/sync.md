---
title: Sync
editUrl: https://github.com/couchbaselabs/mobile-travel-sample/edit/master/content/modules/mobile-travel-tutorial/pages/android/develop/sync.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:tutorials:mobile-travel-tutorial:android/develop/sync.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/mobile-travel-tutorial/android/develop/sync.html)

# Sync

## [](#channelsdata-routing)Channels/Data Routing

In the [Access Control](security.md#access-control)lesson we discussed how the Couchbase Sync Gateway supports _Authorization and Access Control_ functions. In this lesson we discuss how it can be used for _Data Synchronization and Routing_.

A Sync Gateway configuration file determines the runtime behavior of Sync Gateway, including server configuration and the database or set of databases with which a Sync Gateway instance can interact.

Sync Gateway uses channels to make it easy to share a database between a large number of users and control access to the database. Conceptually, a channel could be viewed as a tag. Every document in the database belongs to a set of channels, and a user is granted appropriate access a set of channels. A channel is used to:

* Partition the data set.
* Authorize users to access documents.
* Minimize the amount of data synced down to devices.

In the [Sync Gateway installation](../installation/index.md)section, we walked you through the steps to launch Sync Gateway with a specific config file.

Open the sync-gateway-config-travelsample.json file located at <https://github.com/couchbaselabs/mobile-travel-sample/blob/master/sync-gateway-config-travelsample.json>. It includes the `sync function` which is a JavaScript function whose source code is stored in the Sync Gateway's database configuration file.

```javascript
/* Routing */
// Add doc to the user's channel.
channel("channel." + username);
```

## [](#shared-bucket-access)Shared Bucket Access

Before you begin this lesson, confirm that you have Sync Gateway up and running by following the instructions in the [Sync Gateway installation](../installation/index.md)section.

Sync Gateway and Couchbase Server mobile and server/web applications can read and write to the same bucket \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]. It is an opt-in feature that can be enabled in the Sync Gateway configuration file.

![convergence](https://raw.githubusercontent.com/couchbaselabs/mobile-travel-sample/master/content/assets/convergence.png) 

The sync metadata used by the Sync Gateway for replication with mobile clients is stored in the Extended Attributes or XAttrs associated with the document.

The capability can be enabled through a configuration setting in the sync gateway config file.

Note that if you are using Enterprise Edition of Sync Gateway \[[2](#%5Ffootnotedef%5F2 "View footnote.")\], then the "import\_docs" flag is optional. Every node with "enable\_shared\_bucket\_access" set to "true" will automatically import document mutations from the server bucket.

Open the sync-gateway-config-travelsample.json file located at <https://github.com/couchbaselabs/mobile-travel-sample/blob/master/sync-gateway-config-travelsample.json>

```javascript
"import_docs": "true",
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

* Pull Replication is the process by which clients running Couchbase Lite download database changes from the remote (server) source database to the local target database.
* Push Replication is the process by which clients running Couchbase Lite upload database changes from the local source database to the remote (server) target database.

Couchbase Mobile \[[3](#%5Ffootnotedef%5F3 "View footnote.")\] replication protocol is implemented as a messaging protocol layered over WebSocket.

![replication 2 0](../../_images/replication-2-0.png) 

The replication process can be `continuous` or `one shot`.

* In "Continuous" replication mode, the changes are continually synchronized between the client and Sync Gateway in real time.
* In "One shot" mode, the changes are synchronized once and the connection between the client and server disconnects. When any future changes need to be pushed up or pulled down, the client must start a new replication.

Open the file `app/src/android/java/…​/util/DatabaseManager.java`. We will review the method `startPushAndPullReplicationForCurrentUser(String username, String password)`.

[DatabaseManager.java](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/android/app/src/main/java/com/couchbase/travelsample/util/DatabaseManager.java#L131)

```java
public static void startPushAndPullReplicationForCurrentUser(String username, String password) {
  ...
}
```

First, you initialize the `URL` object which points to the Sync Gateway instance to synchronize with.

```java
public static String mSyncGatewayEndpoint = "ws://10.0.2.2:4984/travel-sample";
URI url = null;
try {
    url = new URI(mSyncGatewayEndpoint);
} catch (URISyntaxException e) {
    e.printStackTrace();
}
```

Next, you will configure the replication. The `ReplicatorConfiguration` is initialized with the local database and URL of the target DB on Sync Gateway. The `replicatorType` in the Replicator Config specifies the type of replication. In the code snippet in the Travel App, it is `pushAndPull` indicating that both push and pull replication is enabled. The `continuous` mode is set to `true` in the Travel app.

```java
ReplicatorConfiguration config = new ReplicatorConfiguration(database, new URLEndpoint(url));
config.setReplicatorType(ReplicatorConfiguration.ReplicatorType.PUSH_AND_PULL);
config.setContinuous(true);
```

The Replicator is configured with relevant authentication credentials. The list of users that are granted access sync with the Sync Gateway are created as discussed in the [Access Control](security.md) section

```java
config.setAuthenticator(new BasicAuthenticator(username, password));
```

The Replicator is initialized with the specified configuration

```java
Replicator replicator = new Replicator(config);
```

A change listener callback block is registered to listen for replication changes. Every time, there is a push or pull change, the callback is invoked.

```java
replicator.addChangeListener(new ReplicatorChangeListener() {
@Override
public void changed(ReplicatorChange change) {

    if (change.getReplicator().getStatus().getActivityLevel().equals(Replicator.ActivityLevel.IDLE)) {

        Log.e("Replication Comp Log", "Schedular Completed");

    }
    if (change.getReplicator().getStatus().getActivityLevel().equals(Replicator.ActivityLevel.STOPPED) || change.getReplicator().getStatus().getActivityLevel().equals(Replicator.ActivityLevel.OFFLINE)) {
        // stopReplication();
        Log.e("Rep schedular  Log", "ReplicationTag Stopped");
    }
}
});
```

Replication is started

```java
replicator.start();
```

### [](#try-push-replication)Try Push Replication

Try it out (Mobile App)

1. Log into the Travel Sample Mobile app as "demo" user and password as "password". This user must be created via the travel sample web backend.
2. Tap the "airline" button to make a flight reservation. Both the "From" and "To" airports and flight dates are already set.
3. Tap the "lookup" button
4. From list of flights, select the first flight listing — see [Figure 1](#fig-android-push). This automatically confirms the booking.

![android push](../../_images/android-push.gif) 

Figure 1\. Lookup Flights

Try it out (Web App)

1. Access the Travel Sample Python Web app. The URL would be <http://localhost:8080>. If you did cloud based install, please replace `localhost` in the URL with the IP Address of the cloud instance of the web app.
2. Log into the web app as "demo" user with password as "password"
3. Use the "Booked" tab to navigate to the list of booked flights
4. Confirm that you see the flight that you reserved via the mobile app in your list of flights in the web app

![travel app push](https://raw.githubusercontent.com/couchbaselabs/mobile-travel-sample/master/content/assets/travel-app-push.gif) 

Figure 2\. View Booked Flights

### [](#try-pull-replication)Try Pull Replication

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
10. The "Booked" tab should show the confirmed flight reservations — see: [Figure 3](#fig-android-pull-repl)

![travel app pull](../../_images/travel-app-pull.gif) 

Figure 3\. Pull Replication

Try it out (Mobile App)

1. Log into the Travel Sample Mobile app as "demo" user and password as "password"
2. Confirm that you see the flight that you reserved via the web app in your list of flights in the mobile app

---

[1](#%5Ffootnoteref%5F1). From 1.5 and 5.0 respectively 

[2](#%5Ffootnoteref%5F2). 2.7 

[3](#%5Ffootnoteref%5F3). From 2.0