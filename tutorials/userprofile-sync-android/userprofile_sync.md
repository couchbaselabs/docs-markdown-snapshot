---
title: "User Profile Sample: Data Sync Fundamentals"
editUrl: https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/edit/sync/content/modules/userprofile-sync-android/pages/userprofile_sync.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:tutorials:userprofile-sync-android:userprofile_sync.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/userprofile-sync-android/userprofile_sync.html)

# User Profile Sample: Data Sync Fundamentals

## [](#introduction)Introduction

Couchbase Sync Gateway is a key component of the Couchbase Mobile stack. It is an internet-facing synchronization mechanism that securely syncs data across devices as well as between devices and the cloud. Couchbase Mobile is built upon a websocket based [replication protocol](https://blog.couchbase.com/data-replication-couchbase-mobile/).

The core functions of the Sync Gateway include

* Data Synchronization across devices and the cloud
* Authorization
* Access Control
* Data Validation

What You Will Learn

This tutorial will demonstrate how to -

* Setup the Couchbase Sync Gateway to sync content between multiple Couchbase Lite enabled clients. We will will cover the basics of the [Sync Gateway Configuration](../../sync-gateway/3.0/configuration-overview.md).
* Configure your Sync Gateway to enforce data routing, access control and authorization. We will cover the basics of the [Sync Function API](../../sync-gateway/3.0/sync-function.md).
* Configure your Couchbase Lite clients for replication with the Sync Gateway.
* Use "Live Queries" or Query events within your Couchbase Lite clients to be asynchronously notified of changes.

We will be using an Android app as an example of a Couchbase Lite enabled client.

You can learn more about Sync Gateway here in the [Sync Gateway Documentation](../../sync-gateway/3.0/index.md)

## [](#prerequisites)Prerequisites

This tutorial assumes familiarity with building [Android](https://www.android.com/)apps using [Java](https://www.java.com)and with the basics of Couchbase Lite.

* If you are unfamiliar with the basics of Couchbase Lite, it is recommended that you walk through the following tutorials:

  * The fundamentals of using Couchbase Lite, in the [Standalone tutorial](../userprofile-standalone-android/userprofile%5Fbasic.md)
  * The [Query tutorial](../userprofile-query-android/userprofile%5Fquery.md), which introduces Query basics, together with use of a prebuilt database

To follow the tutorial it will be useful to have:

* [Android Studio](https://developer.android.com/studio)
* Android device or emulator running API level 29 or above
* Android SDK 29+
* Android Build Tools 29+
* [JDK 8](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
* git (Optional)  
This is required if you want prefer to pull the source code from GitHub repo.

  * Create a [free github account](https://github.com)if you don't already have one
  * git can be downloaded from [git-scm.org](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* curl HTTP client  
We use **curl** in our tutorial. Download latest version from [curl website](https://curl.haxx.se/download.html), or use the HTTP client of your choice.

## [](#system-overview)System Overview

### [](#userprofile-sample-app)Userprofile Sample App

We will be working with a simple "User Profile" app which we introduced in the [Standalone tutorial](../userprofile-standalone-android/userprofile%5Fbasic.md) and extended in the [Query tutorial](../userprofile-query-android/userprofile%5Fquery.md).

In this tutorial, we will be extending that app to support data sync. It will now also:

* Allows users to log in and create or update his/her user profile information.  
The user profile view is _automatically updated_ every time the profile information changes in the underlying database
* The user profile information is synced with a remote Sync Gateway which then syncs it to other devices (subject to access control and routing configurations specified in the `sync function`)

![App with Sync](_images/userprofile_app_overview.gif) 

### [](#sample-app-architecture)Sample App Architecture

The sample app follows the [MVP pattern](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter), separating the internal data model, from a passive view through a presenter that handles the logic of our application and acts as the conduit between the model and the view.

![MVP Architecture](_images/mvp_architecture.png) 

In the Android Studio project, the code is structured by feature. You can select the Android option in the left navigator to view the files by package.

![MVP Android Studio](_images/mvp_as.png) 

Each package contains 3 different files:

* **Activity**: This is where all the view logic resides.
* **Presenter**: This is where all the business logic resides to fetch and persist data to a web service or the embedded Couchbase Lite database.
* **Contract**: An interface that the `Presenter` and `Activity` implement.

![MVP Package](_images/mvp_package.png) 

## [](#app-installation)App Installation

Clone the [**_sync_** branch](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/sync)of the `User Profile Demo` project from GitHub. Type the following command in your terminal

```bash
git clone -b sync https://github.com/couchbaselabs/userprofile-couchbase-mobile-android
```

### [](#installing-couchbase-lite)Installing Couchbase Lite

This [sample project](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/sync/content/modules/userprofile-sync-android/examples/src) already contains the appropriate additions for downloading, and utilizing the Android Couchbase Lite dependency module. However, in the future, to include Couchbase Lite support within an Android app include the following in [app/build.gradle](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/sync/content/modules/userprofile-sync-android/examples/src/app/build.gradle).

```gradle
  dependencies {
    ...

    implementation 'com.couchbase.lite:couchbase-lite-android-ee:3.0.0'
}
```

Try it out

* Open [build.gradle](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/sync/content/modules/userprofile-sync-android/examples/src/app/build.gradle)using Android Studio.
* Build and run the project.
* Verify that you see the login screen.  
![User Profile Login Screen Image](_images/user_profile_login.png)

## [](#data-model)Data Model

If have followed the [Query tutorial](../userprofile-query-android/userprofile%5Fquery.md), you can skip this section and proceed to the [Backend Installation](#backend-installation). section. We have not made any changes to the Data model for this tutorial.

Couchbase Lite is a JSON Document Store. A Document is a logical collection of named fields and values.The values are any valid JSON types. In addition to the standard JSON types, Couchbase Lite supports some special types like `Date` and `Blob`. While it is not required or enforced, it is a recommended practice to include a _"type"_ property that can serve as a namespace for related.

### [](#the-user-profile-document)The "User Profile" Document

The app deals with a single Document with a _"type"_ property of _"user"_. The document ID is of the form _"user::<email>"_. An example of a document would be:

```json
{
    "type":"user",
    "name":"Jane Doe",
    "email":"jame.doe@earth.org",
    "address":"101 Main Street",
    "image":CBLBlob (image/jpg),
    "university":"Missouri State University"
}
```

### [](#userprofile)UserProfile

For the purpose of this tutorial the _"user"_ `Document` is first stored within an `Object` of type `Map<String, Object>`.

```java
Map<String, Object> profile = new HashMap<>();
profile.put("name", nameInput.getText().toString());
profile.put("email", emailInput.getText().toString());
profile.put("address", addressInput.getText().toString());
profile.put("university", universityText.getText().toString());
profile.put("type", "user");
byte[] imageViewBytes = getImageViewBytes();

if (imageViewBytes != null) {
    profile.put("imageData", new com.couchbase.lite.Blob("image/jpeg", imageViewBytes));
}
```

### [](#the-university-document)The "University" Document

The app comes bundled with a collection of Documents of type _"university"_. Each `Document` represents a university.

```json
{
    "type":"university","web_pages": [
      "http://www.missouristate.edu/"
    ],
    "name": "Missouri State University",
    "alpha_two_code": "US",
    "state-province": MO,
    "domains": [
      "missouristate.edu"
    ],
    "country": "United States"
}
```

### [](#the-university-record)The University Record

When _"university"_ `Document` is retrieved from the database it is stored within an `Object` of type `Map<String, Object>`.

```java
Map<String, Object> properties = new HashMap<>();
properties.put("name", row.getDictionary("universities").getString("name"));
properties.put("country", row.getDictionary("universities").getString("country"));
properties.put("web_pages", row.getDictionary("universities").getArray("web_pages"));
```

## [](#backend-installation)Backend Installation

We will install [Couchbase Server](#couchbase-server) and [Sync Gateway](#lbl-sync-gateway) using Docker.

### [](#prerequisites-2)Prerequisites

* You must have Docker installed on your laptop. For more on Docker — see: [Get Docker](https://docs.docker.com/get-docker/)
* On Windows, you may need admin privileges.
* Ensure that you have sufficient memory and cores allocated to docker. At Least 3GB of RAM is recommended.

### [](#docker-network)Docker Network

Create a docker network named "workshop"

```bash
docker network ls

docker network create -d bridge workshop
```

### [](#couchbase-server)Couchbase Server

#### [](#install)Install

We have a custom docker image `priyacouch/couchbase-server-userprofile:7.0.0-dev` of Couchbase Server, which creates an empty bucket named "userprofile" and an RBAC user "admin" with "sync gateway" role.

Alternatively, you can follow the instructions in our documentation — see: [Get Started - Prepare](../../sync-gateway/3.0/get-started-prepare.md), to install Couchbase Server and configure it with the relevant bucket.

1. Optionally, remove any existing Docker container  
```bash  
docker stop cb-server && docker rm cb-server  
```
2. Start Couchbase Server in a Docker container  
```bash  
docker run -d --name cb-server \
--network workshop \
-p 8091-8094:8091-8094 -p 11210:11210 \  
priyacouch/couchbase-server-userprofile:7.0.0-dev  
```

#### [](#test-server-install)Test Server Install

The server could take a few minutes to deploy and fully initialize; so be patient.

1. Check the Docker logs using the command:  
```bash  
docker logs -f cb-server  
```  
When the setup is completed, you should see output similar to that shown in [Figure 1](#ex-server-setup-output).  
![log output](_images/log-output.png)  
Figure 1\. Server set-up output
2. Now check the required data is in place:

  1. Open up <http://localhost:8091> in a browser
  2. Sign in as "Administrator" and "password" in login page
  3. Go to "buckets" menu and confirm "userprofile" bucket is created  
  ![confirm bucket created](_images/confirm-bucket-created.png)
  4. Go to "security" menu and confirm "admin" user is created  
  ![confirm admin user created](_images/confirm-admin-user-created.png)

### [](#lbl-sync-gateway)Sync Gateway

Now we will install, configure and run Sync Gateway.

#### [](#lbl-install)Configuration

When using Sync Gateway 3.0, we can opt to provide a bootstrap configuration — see: [Sync Gateway Configuration](../../sync-gateway/3.0/configuration-overview.md). We would then provision database, sync and other configuration using the Admin REST endpoints Alternatively, we can continue to run in legacy-mode, using the Pre-3.0 configuration.

In this tutorial — for the purposes of backward compatibility — we will run 3.x using its [legacy configuration option](../../sync-gateway/3.0/configuration-properties-legacy.md). That is, we will be running with the `disable_persistent_config` option in the configuration file set to `true`. You can, if you wish, run a 2.8 version of Sync Gateway instead.

The configuration files corresponding to this sample application are shown in [Table 1](#tbl-config-files). They are available in the "sync" branch of the github repo hosting the app, which you cloned — look in:  
`/path/to/cloned/repo/userprofile-couchbase-mobile/content/modules/userprofile-sync/examples/`  

__Table 1\. Available configuration files__
| Release | Filename                                                                                                                                                                                                                                       |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3.x     | [sync-gateway-config-userprofile-demo-3-x-legacy.json](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/sync/content/modules/userprofile-sync-android/examples/sync-gateway-config-userprofile-demo-3-x-legacy.json) |
| 2.x     | [sync-gateway-config-userprofile-demo-2-x.json](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/sync/content/modules/userprofile-sync-android/examples/sync-gateway-config-userprofile-demo-2-x.json)               |

#### [](#lbl-deploy)Deploy

Configure and launch Sync Gateway in a Docker container.

1. Switch to the the folder containing the cloned configuration files, using:  
```bash  
cd /path/to/cloned/repo/userprofile-couchbase-mobile-android/content/modules/userprofile-sync/examples  
```
2. Make sure no Sync Gateway container exists, using:  
```bash  
docker stop sync-gateway && docker rm sync-gateway  
```
3. Launch Sync Gateway in a Docker container  
You should see configuration files for the latest major version and the previous major version in this folder — see: [Table 1](#tbl-config-files). Choose an appropriate version.  
For non-Windows Systems

  * Sync Gateway 3.0
  * Sync Gateway 2.x  
Configure and run Sync Gateway 3.0 in Docker using the configuration file `sync-gateway-config-userprofile-demo-3-x-legacy.json`.  
Note the use of `disable_persistent_config` in the configuration file to force legacy configuration mode.  
```bash  
docker run -p 4984-4986:4984-4986 \
--network workshop \
--name sync-gateway \
-d \
-v `pwd`/sync-gateway-config-userprofile-demo-3-x-legacy.json:\  
/etc/sync_gateway/sync_gateway.json \  
couchbase/sync-gateway:3.0.0-enterprise \  
/etc/sync_gateway/sync_gateway.json  
```  
Configure and run Sync Gateway 2.8 in Docker  
```bash  
docker run -p 4984-4986:4984-4986 \
--network workshop \
--name sync-gateway \
-d \
-v `pwd`/sync-gateway-config-userprofile-demo-2-x.json:\  
/etc/sync_gateway/sync_gateway.json \  
couchbase/sync-gateway:2.8.4-enterprise \  
/etc/sync_gateway/sync_gateway.json  
```  
For Windows Systems

  * Sync Gateway 3.0
  * Sync Gateway 2.x  
Configure and run Sync Gateway 3.0 in legacy mode  
```dos  
docker run -p 4984-4986:4984-4986 ^
--network workshop ^
--name sync-gateway ^
-d -v %cd%sync-gateway-config-userprofile-demo-3-x-legacy.json:^  
/etc/sync_gateway/sync_gateway.json ^  
couchbase/sync-gateway:3.0.0-enterprise ^  
/etc/sync_gateway/sync_gateway.json  
```  
Configuring and running Sync Gateway 2.8  
```dos  
docker run -p 4984-4986:4984-4986 ^
--network workshop ^
--name sync-gateway ^\
-d ^
-v %cd%/sync-gateway-config-userprofile-demo-2-x.json:^  
etc/sync_gateway/sync_gateway.json ^  
couchbase/sync-gateway:2.8.4-enterprise ^  
/etc/sync_gateway/sync_gateway.json  
```

#### [](#test-the-installation)Test the Installation

Now we can confirm that the Sync Gateway is up and running.

1. Check the log messages  
```bash  
docker logs -f sync-gateway  
```  
You will see a series of log messages. Make sure there are no errors.
2. Open up <http://localhost:4984>in a browser.  
You should see equivalent of the following message  
```bash  
{"couchdb":"Welcome","vendor":{"name":"Couchbase Sync Gateway","version":"3.0"},"version":"Couchbase Sync Gateway/3.0.0(145;e3f46be) EE"}  
```

Now that we have the server and the sync gateway installed, we can verify data sync between Couchbase Lite enabled apps.

## [](#sync-function)Sync Function

The Sync Function is a Javascript function that is specified as part of the [Sync Gateway Configuration](#lbl-install). The Sync Function handles data validation, authorization, access control and data routing.

* Open the `sync-gateway-config-userprofile-demo-2-x.json*` file using any text editor of your choice. This configuration file is located in the app bundle at `/path/to/UserProfileDemo/modules/userprofile/examples/src`.
* Locate the `sync` setting and follow along with the rest of the sections below

### [](#authorization)Authorization

We use the [requireUser()](../../sync-gateway/3.0/sync-function-api-require-user-cmd.md)API to verify that the `email` property specified in the Document matches the Id of the user making the request. The Id of the user making the request is specified in the `Authorization` header. We will be using _Basic Authentication_ in our application.

```javascript
function sync(doc, oldDoc) {

   /* Authorization */

  // Verify the user making the request is the same as the one in doc's email
  requireUser(doc.email);

}
```

### [](#data-validation)Data Validation

In this case, we are doing some basic validation of the contents of the Document

```javascript
function sync(doc, oldDoc) {

   /* Data Validation */

   if (!isDelete()) {
      // Validate the presence of email fields
      validateNotEmpty("email", doc.email); (1)

      // Check if document is being created / added for first time
      // We allow any user to create the document
      if (isCreate()) {

        // Validate that the document Id _id is prefixed by owner.
        var expectedDocId = "user" + "::" + doc.email;

        if (expectedDocId != doc._id) { (2)
            throw({forbidden: "user doc Id must be of form user:email"});
        }

      } else {
         // Validate that the email hasn't changed.
        validateReadOnly("email", doc.email, oldDoc.email); (3)
      }

    }
  }


  // Verify that specified property exists
  function validateNotEmpty(key, value) {
    if (!value) {
      throw({forbidden: key + " is not provided."});
    }
  }

  // Verify that specified property value has not changed during update
  function validateReadOnly(name, value, oldValue) {
    if (value != oldValue) {
      throw({forbidden: name + " is read-only."});
    }
  }
```

| **1** | Verify that the email property is not null. If it's null, we throw a JS exception (see validateNotEmpty() function)                                               |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | If this a new document, then verify that the Id of the Document is of the required format (i.e. _"user::<email>"_). We throw an exception if that's not the case. |
| **3** | If this is a document update, then verify that the email property value has not changed. Again, we throw an exception if that's not the case.                     |

You can learn more about the Sync Function in the [Sync Function API](../../sync-gateway/3.0/sync-function.md)

### [](#data-routing)Data Routing

[Channels](../../sync-gateway/3.0/channels.md) are a mechanism to "tag" documents and is typically used to segregate documents based on the contents of the document. Combined with the [access()](../../sync-gateway/3.0/sync-function-api-access-cmd.md)and [requireAccess()](../../sync-gateway/3.0/sync-function-api-require-access-cmd.md)API, it can be used to enforce [Access Control](#access-control). As we shall see in a later section, clients can use channels to pull only a subset of documents.

```javascript
  /* Routing */
  // Subsequent updates to document must be authorized
  var email = getEmail();

  // Add doc to the user's channel.
  channel("channel." + email); (1)

  // get email Id property
  function getEmail() {
    return (isDelete() ? oldDoc.email : doc.email);
  }
```

| **1** | The channel comes into existance the first time a document is added to it. In our case, the channel name is generated from the email property specified in the document |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#access-control)Access Control

You can enforce access control to channels using the [access()](../../sync-gateway/3.0/sync-function-api-access-cmd.md)API. This will ensure that only users with access to a specific channel will be able to retrieve documents in the channel.

```javascript
  /* Access Control */
  // Give user read access to channel
   if(!isDelete()) {
    // Deletion of user document is essentially deletion of user
       access(email,"channel." + email)
   }
```

## [](#starting-replication)Starting Replication

Two-way Replication between the app and the Sync Gateway is enabled when user logs into the app.

* Open the [**DatabaseManager.java**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/sync/content/modules/userprofile-sync-android/examples/src/app/src/main/java/com/couchbase/userprofile/util/DatabaseManager.java) file and locate the `startPushAndPullReplicationForCurrentUser()` function.  
```java  
public static void startPushAndPullReplicationForCurrentUser(String username, String password)  
```
* Next, we create an instance of the `ReplicatorConfiguration` instance that specifies the source and target database and you can optionally, override the default configuration settings.  
```java  
ReplicatorConfiguration config = new ReplicatorConfiguration(userprofileDatabase, new URLEndpoint(url)); (1)  
config.setType(ReplicatorType.PUSH_AND_PULL); (2)  
config.setContinuous(true); (3)  
config.setAuthenticator(new BasicAuthenticator(username, password.toCharArray())); (4)  
config.setChannels(Arrays.asList("channel." + username)); (5)  
```

| **1** | Initialize with source as the local Couchbase Lite database and the remote target as the Sync Gateway                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | Replication type of PUSH\_AND\_PULL indicates that we require two-way sync. A value of .PUSH specifies that we only pull data from the Sync Gateway. A value of .PULL specifies that we only push data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **3** | The continuous mode is specified to be _true_, which means that changes are synced in real-time. A value of _false_ implies that data is only pulled from the Sync Gateway.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **4** | This is where you specify the authentication credentials of the user. In the [Authorization](#authorization) section, we discussed that the Sync Gateway can enforce authorization check using the requireUser API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **5** | The channels are used to specify the channels to pull from. Only documents belonging to the specified channels are synced. This is subject to [Access Control](#access-control) rights enforced at the Sync Gateway. This means that if a client does not have access to documents in a channel, the documents will not be synched even if the client specifies it in the replicator configuration. Initialize the Replicator with the ReplicatorConfiguration replicator = new Replicator(config); We attach a callback listener to the Replicator to be asynchronously notified of state changes. This could be useful for instance, to inform the user of the progress of the replication. This is an optional step replicatorListenerToken = replicator.addChangeListener(new ReplicatorChangeListener() {     @Override     public void changed(ReplicatorChange change) {         if (change.getReplicator().getStatus().getActivityLevel().equals(ReplicatorActivityLevel.IDLE)) {             Log.e("Replication Comp Log", "Scheduler Completed");         }         if (change.getReplicator().getStatus().getActivityLevel().equals(ReplicatorActivityLevel.STOPPED)                 \|| change.getReplicator().getStatus().getActivityLevel().equals(ReplicatorActivityLevel.OFFLINE)) {             Log.e("Rep Scheduler  Log", "ReplicationTag Stopped");         }     } }); Start the replicator replicator.start(); |

## [](#stopping-replication)Stopping Replication

When user logs out of the app, the replication is stopped before the database is closed.

* Open the [**DatabaseManager.java**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/sync/content/modules/userprofile-sync-android/examples/src/app/src/main/java/com/couchbase/userprofile/util/DatabaseManager.java) file and locate the `stopAllReplicationForCurrentUser()` function.  
```java  
public static void stopAllReplicationForCurrentUser()  
```
* Stop the replicator and remove any associated change listeners  
```java  
replicator.removeChangeListener(replicatorListenerToken);  
replicator.stop();  
```  
> [!NOTE]  
> All open replicators must be stopped before database is closed. There will be an exception if you attempt to close the database without closing the active replicators.

## [](#query-events-live-queries)Query Events / Live Queries

Couchbase Lite apps can set up _live queries_ in order to be asynchronously notified of changes to the database that affect the results of the query. This would be very useful for instance, to keep a UI View up-to-date with the results of a query.

In our app, the user profile view is kept up-to-date with a live query that fetches the user profile data that is used to populate the view. This means that, if the replicator pulls down changes to the user profile, it will be automatically reflected in the view.

* Open the [**UserProfilePresenter.java**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/sync/content/modules/userprofile-sync-android/examples/src/app/src/main/java/com/couchbase/userprofile/profile/UserProfilePresenter.java) file and locate the `fetchProfile()` function.  
```java  
 public void fetchProfile()  
```
* Build the Query using `QueryBuilder` API. If you are unfamiliar with this API, please check out this [tutorial](https://developer.couchbase.com/documentation/mobile/2.0/userprofile%5Fquery.html).  
```java  
Query query = QueryBuilder  
                .select(SelectResult.all())  
                .from(DataSource.database(database))  
                .where(Meta.id.equalTo(Expression.string(docId))); (1)  
```

| **1** | We query for documents based on document Id. In our app, there should be exactly one user profile document corresponding to this Id. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------ |
* Attach listener callback to the query to make it _live_  
```java  
query.addChangeListener(new QueryChangeListener() {  
    @Override  
    public void changed(QueryChange change) { (1)  
        ResultSet rows = change.getResults();  
        Result row = null;  
        Map<String, Object> profile = new HashMap<>(); (2)  
        profile.put("email", DatabaseManager.getSharedInstance().currentUser);  
        while ((row = rows.next()) != null) {  
            Dictionary dictionary = row.getDictionary("userprofile"); (3)  
            if (dictionary != null) {  
                profile.put("name", dictionary.getString("name")); (4)  
                profile.put("address", dictionary.getString("address")); (4)  
                profile.put("imageData", dictionary.getBlob("imageData")); (4)  
                profile.put("university", dictionary.getString("university")); (4)  
                profile.put("type", dictionary.getString("type")); (4)  
            }  
        }  
        mUserProfileView.showProfile(profile);  
    }  
});  
```

| **1** | Attach a listener callback to the query. Attaching a listerner automatically makes it _live_ so any time there is a change in the user profile data in the underlying database, the callback would be invoked                                                             |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Create an instance of [\[UserRecord\]](#UserRecord). This will be populated with the query results.                                                                                                                                                                       |
| **3** | The SelectResult.all() method is used to query all the properties of a document. In this case, the document in the result is embedded in a dictionary where the key is the database name, which is _"userprofile"_. So we retrieve the Dictionary at key _"userprofile"_. |
| **4** | We use appropriate _type getters_ to retrieve values and populate the _UserRecord_ instance                                                                                                                                                                               |

## [](#exercises)Exercises

### [](#exercise-1)Exercise 1

In this exercise, we will observe how changes made on one app are synced across to the other app

* The app should be running in two simulators side by side
* Log into both the simulators with same userId and password. Use the values _"[demo@example.com](mailto:demo@example.com)"_ and _"password"_ for user Id and password fields respectively
* On one simulator, enter values in the user and address fields.
* Confirm that changes show up in the app on the other simulator.
* Similarly, make changes to the app in the other simulator and confirm that the changes are synced over to the first simulator.

### [](#exercise-2)Exercise 2

In this exercise, we will observe changes made via Sync Gateway are synced over to the apps.

* Make sure you complete [Exercise 1](#exercise-1).  
This is to ensure that you have the appropriate user profile document (with document Id of "user::<emailId>") created through the app and synced over to the Sync Gateway.
* Open the command terminal and issue the following command to get the user profile document via \[GET Document REST API\].  
We will be using `curl` to issue the request. If you haven't done so, please install curl as indicated in the [Prerequisites](#prerequisites) section  
```bash  
curl -X GET \  
  http://localhost:4985/userprofile/user::demo@example.com \
  -H 'Accept: application/json' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json'  
```
* Your response should look something like the response below.  
The exact contents depends on the user profile information that you provided via your mobile app.  
```bash  
{  
    "_attachments": { (1)  
        "blob_1": {  
            "content_type": "image/jpeg",  
            "digest": "sha1-S8asPSgzA+F+fp8/2DdIy4K+0U8=",  
            "length": 14989,  
            "revpos": 2,  
            "stub": true  
        }  
    },  
    "_id": "user::demo@example.com",  
    "_rev": "2-3a76cfa911e2c54d1e82b29dbffc7f4e5a9bc265", (2)  
    "address": "",  
    "email": "demo@example.com",  
    "image": {  
        "@type": "blob",  
        "content_type": "image/jpeg",  
        "digest": "sha1-S8asPSgzA+F+fp8/2DdIy4K+0U8=",  
        "length": 14989  
    },  
    "name": "",  
    "type": "user",  
    "university": "Missouri State University"  
}  
```

| **1** | If you had updated an image via the mobile app, you should see an \* "\_attachments"\* property. This entry holds an array of attachments corresponding to each image blob entry added by the mobile app. This property is added by the Sync Gateway when it processes the document. You can learn more about how image Blob types are mapped to attachments \[here\]. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Record the revision Id of the document. You will need this when you update the document                                                                                                                                                                                                                                                                                |
* In the command terminal, issue the following command to update the user profile document via \[PUT Document REST API\]  
```bash  
curl -X PUT \  
  'http://localhost:4985/userprofile/user::demo@example.com?rev=3-12d203d6024c8b844c5ed736c726ac63379e05dc' \
  -H 'Accept: application/json' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{  
    "address": "101 Main Street", (1)  
    "email": "demo@example.com",  
    "image": {  
        "@type": "blob",  
        "content_type": "image/jpeg",  
        "digest": "sha1-S8asPSgzA+F+fp8/2DdIy4K+0U8=",  
        "length": 14989  
    },  
    "name": "",  
    "type": "user",  
    "university": "Missouri State University"  
}'  
```

| **1** | I updated the university field via the REST API. You can choose to update any other profile information |
| ----- | ------------------------------------------------------------------------------------------------------- |
* Confirm that you get a HTTP _"201 Created"_ status code
* As soon as you update the document via the Sync Gateway REST API, confirm that the changes show up in the mobile app on the simulator.  
![App Sync](_images/sync_from_sgw.gif)

## [](#handling-conflicts-during-data-synchronization)Handling Conflicts during Data Synchronization

Data conflicts are inevitable in an environment where you can potentially have multiple writes updating the same data concurrently. Couchbase MObile supports _Automated Conflict Resolution_.

You can learn more about automated conflict resolution in this [blog post](https://blog.couchbase.com/document-conflicts-couchbase-mobile/).

## [](#learn-more)Learn More

Congratulations on completing this tutorial!

This tutorial walked you through an example of how to use a Sync Gateway to synchronize data between Couchbase Lite enabled clients. We discussed how to configure your Sync Gateway to enforce relevant access control, authorization and data routing between Couchbase Lite enabled clients.

Check out the following links for further details

Further Reading

* [Sync Gateway Configuration](../../sync-gateway/3.0/configuration-overview.md)
* [Overview of Replication Protocol 2.0](https://blog.couchbase.com/data-replication-couchbase-mobile/)
* [Installing Sync Gateway using Docker](https://blog.couchbase.com/couchbase-mobile-docker/)