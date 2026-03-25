---
editUrl: https://github.com/couchbaselabs/userprofile-couchbase-mobile/edit/backgroundfetch/content/modules/userprofile/pages/userprofile_sync.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:userprofile-couchbase-mobile:userprofile:userprofile_sync.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/userprofile-couchbase-mobile/current/userprofile/userprofile_sync.html)

# undefined

## [](#introduction)Introduction

Couchbase Sync Gateway is a key component of the Couchbase Mobile stack. It is an Internet-facing synchronization mechanism that securely syncs data across devices as well as between devices and the cloud. Couchbase Mobile 2.0 introduces a brand new websockets based [replication protocol](https://blog.couchbase.com/data-replication-couchbase-mobile/).

The core functions of the Sync Gateway include

* Data Synchronization across devices and the cloud
* Authorization & Access Control
* Data Validation

This tutorial will demonstrate how to -

* Setup the Couchbase Sync Gateway (in walrus mode) to sync content between multiple Couchbase Lite enabled clients. We will will cover the basics of the [Sync Gateway Configuration](https://developer.couchbase.com/documentation/mobile/2.0/guides/sync-gateway/config-properties/index.html).
* Configure your Sync Gateway to enforce data routing, access control and authorization. We will cover the basics of [Sync Function API](https://developer.couchbase.com/documentation/mobile/2.0/guides/sync-gateway/sync-function-api-guide/index.html)
* Configure your Couchbase Lite clients for replication with the Sync Gateway
* Use "Live Queries" or Query events within your Couchbase Lite clients to be asyncronously notified of changes

We will be usiing a Swift App as an example of a Couchbase Lite enabled client.

You can learn more about the Sync Gateway [here](https://developer.couchbase.com/documentation/mobile/2.0/guides/sync-gateway/index.html)

## [](#prerequisites)Prerequisites

This tutorial assumes familiarity with building swift apps with Xcode and with Couchbase Lite.

* If you are unfamiliar with the basics of Couchbase Lite, it is recommended that you walk through the following tutorials

  * [Fundamentals](https://developer.couchbase.com/documentation/mobile/2.0/userprofile%5Fbasic.html) of using Couchbase Lite 2.0 as a standalone database
  * [Query Basics](https://developer.couchbase.com/documentation/mobile/2.0/userprofile%5Fquery.html) with a prebuilt version of Couchbase Lite database
* iOS (Xcode 9.3+)

  * Download latest version from the [Mac App Store](https://itunes.apple.com/us/app/xcode/id497799835?mt=12)
  * NOTE: If you are on an older version of Xcode that you must retain for your other development needs, you can make a copy of your existing version of Xcode and install Xcode 9.3\. So you can have multiple versions of Xcode on your Mac.
* git (Optional) This is required if you would prefer to pull the source code from GitHub repo.

  * Create a [free github account](https://github.com) if you don’t already have one
  * git can be downloaded from [git-scm.org](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* curl HTTP client

  * You could use any HTTP client of your choice. But we will use **curl** in our tutorial. Download latest version from [curl website](https://curl.haxx.se/download.html)

## [](#system-overview)System Overview

We will be working with a simple "User Profile" app which we introduced in the [Fundamentals Tutorial](https://developer.couchbase.com/documentation/mobile/2.0/userprofile%5Fbasic.html) and extended in the [Query Tutorial](https://developer.couchbase.com/documentation/mobile/2.0/userprofile%5Fquery.html).

In this tutorial, we will be extending that app to support data sync.

The app does the following

* Allows users to log in and create or update his/her user profile information. The user profile view is _automatically updated_ everytime the profile information changes in the underlying database
* The user profile information is synced with a remote Sync Gateway which then syncs it to other devices (subject to access control and routing configurations specified in the `sync function`)

![App with Sync](https://raw.githubusercontent.com/couchbaselabs/userprofile-couchbase-mobile/sync/content/modules/userprofile/assets/images/userprofile_app_overview.gif) 

## [](#app-installation)App Installation

### [](#fetching-app-source-code)Fetching App Source Code

You have two options

#### [](#option-1-git-clone)Option 1 : Git Clone

* Clone the **_sync_** branch of the `User Profile Demo` project from GitHub. Type the following command in your terminal  
```bash  
  git clone -b sync https://github.com/couchbaselabs/userprofile-couchbase-mobile.git  
```

#### [](#option-2-download-zip)Option 2 : Download .zip

* Download the `User Profile Demo` project from [here](https://github.com/couchbaselabs/userprofile-couchbase-mobile/archive/sync.zip)

### [](#installing-couchbase-lite-framework)Installing Couchbase Lite Framework

* Next, we will download the Couchbase Lite 2.0 framework. The Couchbase Lite iOS framework is [distributed](https://developer.couchbase.com/documentation/mobile/2.0/couchbase-lite/swift.html) via Cocoapods, Carthage or you can download the pre-built framework. In our example, we will be downloading the pre-built version of the framework. For this, type the following in the command terminal  
```bash  
  cd /path/to/UserProfileDemo/content/modules/userprofile/examples  
  sh install_9.sh  
```

Now, let’s verify the installation

### [](#try-it-out)Try it Out

* Open the `UserProfileDemo.xcodeproj`. The project would be located at `/path/to/UserProfileDemo/content/modules/userprofile/examples`  
```bash  
open UserProfileDemo.xcodeproj  
```
* Build and run the project using **two simulators** using Xcode
* Verify that you see the login screen on both the simulators  
![User Profile Login Screen Image](_images/user_profile_login_2.png)

## [](#sync-gateway-2-0-installation)Sync Gateway 2.0 Installation

There are several [deployment](https://developer.couchbase.com/documentation/mobile/2.0/installation/sync-gateway/index.html) options for the Sync Gateway. In our tutorial, we will be using the Sync Gateway installer to install the Sync Gateway on the same _localhost_ as the mobile app.

### [](#download-the-installer)Download the Installer

* Download the Sync Gateway 2.0.0 installer from [Downloads](https://www.couchbase.com/downloads#couchbase-mobile) page. Be sure to select the **"Mobile"** tab.
* Launch the Sync Gateway from the command line with the **sync-gateway-config-userprofile-walrus.json** config file. This file is bundled with the User Profile mobile App source that you downloaded as per instructions in [Fetching App Source Code](#fetching-app-source-code) section. The `sync-gateway-config-userprofile-walrus.json` will be located in the `/path/to/UserProfileDemo/content/modules/userprofile/examples/` folder  
Type following commands in the command terminal -  
```bash  
cd  /path/to/sync-gateway-installation/couchbase-sync-gateway/bin  
./sync_gateway /path/to/UserProfileDemo/content/modules/userprofile/examples/sync-gateway-config-userprofile-walrus.json  
```
* You should see a bunch of logs output to the console, similar to one below. For brevity, some of the log messages have been trimmed from output below  
```bash  
~/couchbase-sync-gateway/bin | => ./sync_gateway ~/projects/ios/UserProfileDemo/content/modules/userprofile/examples/sync-gateway-config-userprofile-walrus.json  
2018-05-07T15:25:02.924-04:00 Enabling logging: [*]  
2018-05-07T15:25:02.924-04:00 ==== Couchbase Sync Gateway/2.0.0(832;2d8a6c0) ====  
2018-05-07T15:25:03.028-04:00     Created user "demo@example.com"  
2018-05-07T15:25:03.028-04:00 Starting admin server on 127.0.0.1:4985  
2018-05-07T15:25:03.028-04:00 Changes+: Notifying that "userprofile" changed (keys="{_sync:user:demo@example.com}") count=2  
2018-05-07T15:25:03.028-04:00 Cache: Received #1 ("_user/demo@example.com")  
2018-05-07T15:25:03.028-04:00 Cache: Initialized cache for channel "*" with options: &{ChannelCacheMinLength:50 ChannelCacheMaxLength:500 ChannelCacheAge:1m0s}  
2018-05-07T15:25:03.028-04:00 Cache:     #1 ==> channel "*"  
2018-05-07T15:25:03.028-04:00 Changes+: Notifying that "userprofile" changed (keys="{*}") count=3  
2018-05-07T15:25:03.031-04:00 Starting server on :4984 ...  
```

Now, let’s verify the installation

### [](#try-it-out-2)Try it Out

* Open a browser and enter `<http://localhost:4984>` in the address bar
* You should see a message similar one below  
```bash  
{"couchdb":"Welcome","vendor":{"name":"Couchbase Sync Gateway","version":"2.0"},"version":"Couchbase Sync Gateway/2.0.0(832;2d8a6c0)"}  
```

## [](#data-model)Data Model

If have followed along the tutorial on Query Basics, you can skip this section and proceed to the [Sync Gateway Configuration](#sync-gateway-configuration). section We have not made any changes to the Data model for this tutorial. Couchbase Lite is a JSON Document Store. A Document is a logical collection of named fields and values.The values are any valid JSON types. In addition to the standard JSON types, Couchbase Lite supports some special types like `Date` and `Blob`. While it is not required or enforced, it is a recommended practice to include a _"type"_ property that can serve as a namespace for related.

### [](#the-user-profile-document)The "User Profile" Document

The app deals with a single Document with a _"type"_ property of _"user"_. The document ID is of the form _"user::<email>"_. An example of a document would be

```json
{
    "type":"user",
    "name":"Jane Doe",
    "email":"jame.doe@earth.org",
    "address":"101 Main Street",
    "image":CBLBlob (image/jpg),
    "university":"Rensselaer Polytechnic"
}
```

### [](#userrecord)UserRecord

The _"user"_ Document is encoded to a native struct named _UserRecord_.

```swift
let kUserRecordDocumentType = "user"
typealias ExtendedData = [[String:Any]]
struct UserRecord : CustomStringConvertible{
    let type = kUserRecordDocumentType
    var name:String?
    var email:String?
    var address:String?
    var imageData:Data?
    var university:String?
    var extended:ExtendedData? // future
  
    var description: String {
        return "name = \(String(describing: name)), email = \(String(describing: email)), address = \(String(describing: address)), imageData = \(imageData)"
    }
    

}
```

## [](#the-university-document)The "University" Document

The app comes bundled with a collection of Documents of type _"university"_. Each Document represents a university.

```json
{
    "type":"university","web_pages": [
      "http://www.rpi.edu/"
    ],
    "name": "Rensselaer Polytechnic Institute",
    "alpha_two_code": "US",
    "state-province": null,
    "domains": [
      "rpi.edu"
    ],
    "country": "United States"
}
```

### [](#universityrecord)UniversityRecord

The _"university"_ Document is encoded to a native struct named _UniversityRecord_.

```swift
typealias Universities = [UniversityRecord]
// Native object
struct UniversityRecord : CustomStringConvertible{
    
    var alphaTwoCode:String?
    var country:String?
    var domains:[String]?
    var name:String?
    var webPages:[String]?
    
    var description: String {
        return "name = \(String(describing: name)), country = \(String(describing: country)), domains = \(String(describing: domains)), webPages = \(webPages), alphaTwoCode = \(String(describing: alphaTwoCode)) "
    }
    
}
```

## [](#sync-gateway-configuration)Sync Gateway Configuration

The [Sync Gateway Configuration](https://developer.couchbase.com/documentation/mobile/2.0/guides/sync-gateway/config-properties/index.html) determines the run time behavior of the Sync Gateway and is typically specified in a JSON file. You can also use the [Sync Gateway Config REST Endpoint](https://developer.couchbase.com/documentation/mobile/2.0/references/sync-gateway/admin-rest-api/index.html#/database/put<em>db</em>%5Fconfig) to specify the configuration. In our application, we will be defining it in the `**sync-gateway-config-userprofile-walrus.json**` file.

* Open the `**sync-gateway-config-userprofile-walrus.json**` file using any text editor of your choice. The `sync-gateway-config-userprofile-walrus.json` is located in the app bundle at `/path/to/UserProfileDemo/content/modules/userprofile/examples`.  
Locate the following settings in the configuration file -
* The **users** setting.  
The list of users recognized by the Sync Gateway is specified using the `users` config setting. The Sync Gateway will only authorize syncronization requests from valid/recognized users.  
For simplicity, we have hardcoded the `user` to be _"[demo@example.com](mailto:demo@example.com)"_ and the `password` of _"password"_. In a production app, you would likely configure the user dynamically on the Sync Gateway through the [User Admin REST API](https://developer.couchbase.com/documentation/mobile/2.0/references/sync-gateway/admin-rest-api/index.html#/user/post<em>db</em><em>user</em>) instead of hardcoding it this way.  
```json  
"userprofile": {  
      "users": { "demo@example.com": { "password": "password"} },  
      ....  
}  
```  
> [!NOTE]  
> If you want to want to use a different user, then add the credentials of that user to this configuration setting and restart the Sync Gateway.
* The **server** setting  
This is where we specify the URL of the server. We have specified this to be `**walrus**`. This is an _in-memory-only_ mode that is only recommended for development environments. We will be configuring Sync Gateway to operate in this mode. In a production deployment, the Sync Gatway should be backed up by a Couchbase Server.  
This is specified using the `server` config setting  
```json  
"userprofile": {  
      "server": "walrus:",  
      ....  
}  
```

You can learn more about the walrus mode in this [guide](https://developer.couchbase.com/documentation/mobile/current/installation/sync-gateway/index.html#walrus-mode).

## [](#sync-function)Sync Function

The Sync Function is a Javascript function that is specified as part of the [Sync Gateway Configuration](#sync-gateway-configuration). The Sync Function handles data validation, authorization, access control and data routing.

* Open the `**sync-gateway-config-userprofile-walrus.json**` file using any text editor of your choice. The `sync-gateway-config-userprofile-walrus.json` is located in the app bundle at `/path/to/UserProfileDemo/content/modules/userprofile/examples`.
* Locate the `sync` setting and follow along with the rest of the sections below

### [](#authorization)Authorization

We use the [requireUser()](https://developer.couchbase.com/documentation/mobile/2.0/guides/sync-gateway/sync-function-api-guide/index.html#requireuserusername) API to verify that the `email` property specified in the Document matches the Id of the user making the request. The Id of the user making the request is specified in the `Authorization` header. We will be using _Basic Authentication_ in our application.

```javascript
function sync(doc, oldDoc) {
   ....
   /* Authorization */

  // Verify the user making the request is the same as the one in doc's email
  requireUser(doc.email);
  .....
}
```

### [](#data-validation)Data Validation

In this case, we are doing some basic validation of the contents of the Document

```javascript
function sync(doc, oldDoc) {
   ...
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

| **1** | Verify that the email property is not null. If it’s null, we throw a JS exception (see validateNotEmpty() function)                                               |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | If this a new document, then verify that the Id of the Document is of the required format (i.e. _"user::<email>"_). We throw an exception if that’s not the case. |
| **3** | If this is a document update, then verify that the email property value has not changed. Again, we throw an exception if that’s not the case.                     |

You can learn more about the Sync Function in this [guide](https://developer.couchbase.com/documentation/mobile/2.0/guides/sync-gateway/sync-function-api-guide/index.htm)

### [](#data-routing)Data Routing

[channels](https://developer.couchbase.com/documentation/mobile/2.0/guides/sync-gateway/channels/index.html#introduction-to-channels) are a mechanism to "tag" documents and is typically used to seggregate documents based on the contents of the document. Combined with [access API](https://developer.couchbase.com/documentation/mobile/2.0/guides/sync-gateway/sync-function-api-guide/index.html#access-username-channelname) and `requireAccess API`, it can be used to enforce [Access Control](#access-control). As we shall see in a later section, clients can use channels to pull only a subset of documents.

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

You can enforce access control to channels using the [access API](https://developer.couchbase.com/documentation/mobile/2.0/guides/sync-gateway/sync-function-api-guide/index.html#access-username-channelname). This will ensure that only users with access to a specific channel will be able to retrieve documents in the channel.

```javascript
  /* Access Control */
  // Give user read access to channel
   if (!isDelete()) {
    // Deletion of user document is essentially deletion of user
       access(email,"channel." + email)
   }
```

## [](#starting-replication)Starting Replication

Two-way Replication between the app and the Sync Gateway is enabled when user logs into the app.

* Open the **DatabaseManager.swift** file and locate the `startPushAndPullReplicationForCurrentUser()` function.  
```swift  
    func startPushAndPullReplicationForCurrentUser() {  
```
* Next, we create an instance of the `ReplicatorConfig` instance that specifies the source and target database and you can optionally, override the default configuration settings.  
```swift  
        let dbUrl = remoteUrl.appendingPathComponent(kDBName)  
        let config = ReplicatorConfiguration.init(database: db, target: URLEndpoint.init(url:dbUrl)) (1)  
          
        config.replicatorType = .pushAndPull (2)  
        config.continuous =  true (3)  
        config.authenticator =  BasicAuthenticator(username: user, password: password) (4)  
          
          
        // This should match what is specified in the sync gateway config  
        // Only pull documents from this user's channel  
        let userChannel = "channel.\(user)"  
        config.channels = [userChannel] (5)  
```

| **1** | Initialize with source as the local Couchbase Lite database and the remote target as the Sync Gateway                                                                                                                                                                                                                                                                                               |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Replication type of pushAndPull indicates that we require two-way sync. A value of .pull specifies that we only pull data from the Sync Gateway. A value of .push specifies that we only push data.                                                                                                                                                                                                 |
| **3** | The continuous mode is specified to be _true_ which means that changes are synced in real-time. A value of _false_ which implies that data is only pulled from the Sync Gateway.                                                                                                                                                                                                                    |
| **4** | This is where you specify the authentication credentials of the user. In the [Authorization](#authorization) section, we discussed that the Sync Gateway can enforce authorization check using the requireUser API.                                                                                                                                                                                 |
| **5** | The channels are used to specify the channels to pull from. Only documents belonging to the specified channels are synced. This is subject to [Access Control](#access-control) rights enforced at the Sync Gateway. This means that if a client does not have access to documents in a channel, the documents will not be synched even if the client specifies it in the replicator configuration. |
* Initialize the `Replicator` with the `ReplicatorConfiguration`  
```swift  
        _pushPullRepl = Replicator.init(config: config)  
```
* We attach a callback listener to the `Replicator` to be asynchronously notified of state changes. This could be useful for instance, to inform the user of the progress of the replication. This is an optional step  
```swift  
        _pushPullReplListener = _pushPullRepl?.addChangeListener({ (change) in  
            let s = change.status  
            switch s.activity {  
            case .busy:  
                print("Busy transferring data")  
            case .connecting:  
                print("Connecting to Sync Gateway")  
            case .idle:  
                print("Replicator in Idle state")  
            case .offline:  
                print("Replicator in offline state")  
            case .stopped:  
                print("Completed syncing documents")  
            }  
            
            if s.progress.completed == s.progress.total {  
                print("All documents synced")  
            }  
            else {  
                 print("Documents \(s.progress.total - s.progress.completed) still pending sync")  
            }  
        })  
```
* Start the replicator  
```swift  
        _pushPullRepl?.start()  
```

## [](#stopping-replication)Stopping Replication

When user logs out of the app, the replication is stopped before the database is closed.

* Open the **DatabaseManager.swift** file and locate the `stopAllReplicationForCurrentUser()` function.  
```swift  
    func stopAllReplicationForCurrentUser() {  
```
* Stop the replicator and remove any associated change listeners  
```swift  
        if let pushPullReplListener = _pushPullReplListener{  
            print(#function)  
            _pushPullRepl?.removeChangeListener(withToken:  pushPullReplListener)  
            _pushPullRepl = nil  
            _pushPullReplListener = nil  
        }  
        _pushPullRepl?.stop()  
          
        if let oneshotPushPullReplListener = _oneshotPushPullReplListener{  
            print(#function)  
            _oneshotPushPullRepl?.removeChangeListener(withToken:  oneshotPushPullReplListener)  
            _oneshotPushPullRepl = nil  
            _oneshotPushPullRepl = nil  
        }  
        _oneshotPushPullRepl?.stop()  
```  
> [!NOTE]  
> All open replicators must be stopped before database is closed. There will be an exception if you attempt to close the database without closing the active replicators.

## [](#query-events-live-queries)Query Events / Live Queries

In couchbase Lite 2.0, the app can set up _live queries_ in order to be asynchronously notified of changes to the database that affect the results of the query. This would be very useful for instance, to keep a UI View up-to-date with the results of a query.

In our app, the user profile view is kept up-to-date with a live query that fetches the user profile data that is used to populate the view. This means that, if the replicator pulls down changes to the user profile, it will be automatically reflected in the view.

* Open the **UserPresenter.swift** file and locate the `fetchRecordForCurrentUserWithLiveModeEnabled()` function. Calling this function with a value of `true` implies that the caller wishes to be notified of any changes to query results.  
```swift  
    func fetchRecordForCurrentUserWithLiveModeEnabled(__ enabled:Bool = false) {  
```
* Build the Query using `QueryBuilder` API. If you are unfamiliar with this API, please check out this [tutorial](https://developer.couchbase.com/documentation/mobile/2.0/userprofile%5Fquery.html).  
```swift  
            guard let db = dbMgr.db else {  
                fatalError("db is not initialized at this point!")  
            }  
            userQuery = QueryBuilder  
                .select(SelectResult.all())  
                .from(DataSource.database(db))  
                .where(Meta.id.equalTo(Expression.string(self.userProfileDocId))) (1)  
```

| **1** | We query for documents based on document Id. In our app, there should be exactly one user profile document corresponding to this Id. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------ |
* Attach listener callback to the query to make it _live_  
```swift  
                userQueryToken = userQuery?.addChangeListener { [weak self] (change) in (1)  
                    guard let `self` = self else {return}  
                    switch change.error {  
                    case nil:  
                        var userRecord = UserRecord.init() (2)  
                        userRecord.email = self.dbMgr.currentUserCredentials?.user  
                          
                        for (_, row) in (change.results?.enumerated())! {  
                            // There should be only one user profile document for a user  
                            print(row.toDictionary())  
                            if let userVal = row.dictionary(forKey: "userprofile") { (3)  
                                userRecord.email  =  userVal.string(forKey: UserRecordDocumentKeys.email.rawValue)  
                                userRecord.address = userVal.string(forKey:UserRecordDocumentKeys.address.rawValue)  
                                userRecord.name =  userVal.string(forKey: UserRecordDocumentKeys.name.rawValue)  
                                userRecord.university = userVal.string(forKey: UserRecordDocumentKeys.university.rawValue)  
                                userRecord.imageData = userVal.blob(forKey:UserRecordDocumentKeys.image.rawValue)?.content (4)  
                            }  
                        }  
```

| **1** | Attach a listener callback to the query. Attaching a listerner automatically makes it _live_ so any time there is a change in the user profile data in the underlying database, the callback would be invoked                                                                                                                                                              |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Create an instance of [UserRecord](#userrecord). This will be populated with the query results.                                                                                                                                                                                                                                                                            |
| **3** | The SelectResult.all() method is used to query all the properties of a document. In this case, the document in the result is embedded in a dictionary where the key is the database name, which is _"userprofile"_. So we retrieve the [DictionaryObject](http://docs.couchbase.com/mobile/2.0/couchbase-lite-swift/Classes/DictionaryObject.html) at key _"userprofile"_. |
| **4** | We use appropriate _type getters_ to retrieve values and populate the _UserRecord_ instance                                                                                                                                                                                                                                                                                |

## [](#exercises)Exercises

### [](#exercise-1)Exercise 1

In this exercise, we will observe how changes made on one app are synced across to the other app

* The app should be running in two simulators side by side
* Log into both the simulators with same userId and password. Use the values _"[demo@example.com](mailto:demo@example.com)"_ and _"password"_ for user Id and password fields respectively
* On one simulator, enter values in the user and address fields.
* Confirm that changes show up in the app on the other simulator.
* Similarly, make changes to the app in the other simulator and confirm that the changes are synced over to the first simulator.

### [](#exercise-2)Exercise 2

In this exercise, we will observe changes made via Sync Gateway are synced over to the apps

* Make sure you complete [Exercise 1](#exercise-1). This is to ensure that you have the appropriate user profile document (with document Id of "user::<emailId>") created through the app and synced over to the Sync Gateway.
* Open the command terminal and issue the following command to get the user profile document via GET Document REST API . We will be using `curl` to issue the request. If you haven’t done so, please install curl as indicated in the [Prerequisites](#prerequisites) section  
```bash  
curl -X GET \  
  http://localhost:4985/userprofile/user::demo@example.com \
  -H 'Accept: application/json' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json'  
```
* Your response should look something like the response below. The exact contents depends on the user profile information that you provided via your mobile app.  
```bash  
{  
    "_attachments": { (2)  
        "blob_1": {  
            "content_type": "image/jpeg",  
            "digest": "sha1-S8asPSgzA+F+fp8/2DdIy4K+0U8=",  
            "length": 14989,  
            "revpos": 2,  
            "stub": true  
        }  
    },  
    "_id": "user::demo@example.com",  
    "_rev": "2-3a76cfa911e2c54d1e82b29dbffc7f4e5a9bc265", (1)  
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
    "university": "British Institute in Paris, University of London"  
}  
```

| **1** | Record the revision Id of the document. You will need this when you update the document                                                                                                                                                                                                                                                                           |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | If you had updated an image via the mobile app, you should see an **"\_attachments"** property. This entry holds an array of attachments corresponding to each image blob entry added by the mobile app. This property is added by the Sync Gateway when it processes the document. You can learn more about how image Blob types are mapped to attachments here. |
* In the command terminal, issue the following command to update the user profile document via PUT Document REST API  
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
    "university": "British Institute in Paris, University of London"  
}'  
```

| **1** | I updated the university field via the REST API. You can choose to update any other profile information |
| ----- | ------------------------------------------------------------------------------------------------------- |
* Confirm that you get a HTTP _"201 Created"_ status code
* As soon as you update the document via the Sync Gateway REST API, confirm that the changes show up in the mobile app on the simulator.  
![App Sync](https://raw.githubusercontent.com/couchbaselabs/userprofile-couchbase-mobile/sync/content/modules/userprofile/assets/images/sync_from_sgw.gif)

> [!NOTE]
> From [Exercise 2](#exercise-2) above, you observed that changes made on the Sync Gateway are propagated to the Couchbase Lite clients. However, if you tried to update the attachment / image using the Attachments REST API, you would not see the image getting updated on the client side. This is a known issue in 2.0 and should be fixed in the next release.

## [](#handling-conflicts-during-data-syncronization)Handling Conflicts during Data Syncronization

Data conflicts are inevtiable in an environment where you can potentially have multiple writes updating the same data concurrently. Couchbase MObile 2.0 supports _Automated Conflict Resolution_.

You can learn more about automated conflict resolution in this [blog post](https://blog.couchbase.com/document-conflicts-couchbase-mobile/).

## [](#learn-more)Learn More

Congratulations on completing this tutorial!

This tutorial walked you through an example of how to use a Sync Gateway to synchronize data between Couchbase Lite enabled clients. We discussed how to configure your Sync Gateway to enforce relevat access control, authorization and data routing between Couchbase Lite enabled clients.

Check out the following links for further details

### [](#further-reading)Further Reading

* [Sync Gateway Configuration](https://developer.couchbase.com/documentation/mobile/2.0/guides/sync-gateway/config-properties/index.html)
* [Sync Function API](TBD)
* [Overview of Replication Protocol 2.0](https://blog.couchbase.com/data-replication-couchbase-mobile/)
* [Installing Sync Gateway using Docker](https://blog.couchbase.com/couchbase-mobile-docker/)