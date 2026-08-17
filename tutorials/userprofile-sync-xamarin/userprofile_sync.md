---
title: "User Profile Sample: Data Sync Fundamentals"
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin/edit/sync/content/modules/userprofile-sync-xamarin/pages/userprofile_sync.adoc
  xref: xref:tutorials:userprofile-sync-xamarin:userprofile_sync.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/userprofile-sync-xamarin/userprofile_sync.html)

# User Profile Sample: Data Sync Fundamentals

## [](#introduction)Introduction

Couchbase Sync Gateway is a key component of the Couchbase Mobile stack. It is an internet-facing synchronization mechanism that securely syncs data across devices as well as between devices and the cloud. Couchbase Mobile uses a websocket based [replication protocol](https://blog.couchbase.com/data-replication-couchbase-mobile/).

The core functions of the Sync Gateway include

* Data Synchronization across devices and the cloud
* Authorization
* Access Control
* Data Validation

What You Will Learn

In this tutorial you will learn how to:

* Setup a basic Couchbase Sync Gateway configuration to sync content between multiple Couchbase Lite enabled clients — see: [Sync Gateway](#lbl-sync-gateway).  
We will will cover the basics of the [Sync Gateway Configuration](../../sync-gateway/3.0/configuration-overview.md)
* Configure your Sync Gateway to enforce data routing, access control and authorization — see: [Sync Function](#lbl-sync-function).  
We will cover the basics of the [Sync Function API](../../sync-gateway/3.0/sync-function.md).
* Configure your Couchbase Lite clients for replication with the Sync Gateway
* Use "Live Queries" or Query events within your Couchbase Lite clients to be asynchronously notified of changes — see: [Query Events and Live Queries](#lbl-query-events)

We will be using Xamarin (iOS/Android/UWP) apps as examples of Couchbase Lite enabled clients.

You can learn more about the Sync Gateway here in the [Sync Gateway Documentation](../../sync-gateway/3.0/index.md).

## [](#prerequisites)Prerequisites

This tutorial assumes familiarity with building Xamarin apps using C#, XAML, and Couchbase Lite.

* If you are unfamiliar with the basics of Couchbase Lite, it is recommended that you walk through the following tutorials

  * Fundamentals of using Couchbase Lite as a standalone database — see: [Standalone tutorial](../userprofile-standalone-xamarin/userprofile%5Fbasic.md).
  * Using queries with a prebuilt version of Couchbase Lite database — see: [Query tutorial](../userprofile-query-xamarin/userprofile%5Fquery.md).
* Visual Studio 2019
* .Net 3.0
* Android (SDK 29+) API Level 10
* UWP (Windows 10)
* git (Optional)  
This is required to pull the source code from GitHub repo.

  * Create a [free github account](https://github.com) if you don't already have one
  * git can be downloaded from [git-scm.org](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* curl HTTP client  
You can use any HTTP client of your choice. But we will use **curl** in our tutorial. Download latest version from the [curl website](https://curl.haxx.se/download.html)
* Docker  
We will be using Docker to run images of both Couchbase Server and the Sync Gateway — to download Docker, or for more information, see: [Get Docker](https://docs.docker.com/get-docker/)

## [](#system-overview)System Overview

We will be working with the simple "User Profile" app which we introduced in the [Standalone tutorial](../userprofile-standalone-xamarin/userprofile%5Fbasic.md) and extended in the [Query tutorial](../userprofile-query-xamarin/userprofile%5Fquery.md); see: [Solution Overview](#solution-overview)

In this tutorial, we will be further extending that app to support data sync. It will do the following:

* Allows users to log in and create or update their user profile information. The user profile view is _automatically updated_ every time the profile information changes in the underlying database
* The user profile information is synced with a remote Sync Gateway which then syncs it to other devices (subject to access control and routing configurations specified in the `sync function`)

![App with Sync](_images/userprofile_app_overview.gif) 

Figure 1\. The sample user profile application running in a simulator

### [](#solution-overview)Solution Overview

The User Profile demo app is a Xamarin.Forms based solution that supports iOS, Android, and UWP mobile platforms. The solution utilizes various design patterns and principles such as [MVVM](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel), [IoC](https://en.wikipedia.org/wiki/Inversion%5Fof%5Fcontrol), and the Repository Pattern.

The solution comprises seven projects.

* **UserProfileDemo**: A .NET Standard project responsible for maintaining view-level functionality.
* **UserProfileDemo.Core**: A .NET Standard project responsible for maintaining viewmodel-level functionality.
* **UserProfileDemo.Models**: A .NET Standard project consisting of simple data models.
* **UserProfileDemo.Repositories**: A .NET Standard project consisting of repository classes responsible for Couchbase Lite database initilization, interaction, etc.
* **UserProfileDemo.iOS**: A Xamarin.iOS platform project responsible for building the `.ipa` file.
* **UserProfileDemo.Android**: A Xamarin.Android platform project responsible for building the `.apk` file.
* **UserProfileDemo.UWP**: A UWP platform project responsible for building the `.exe` file.

### [](#couchbase-lite-nuget)Couchbase Lite Nuget

Before diving into the code for the apps, it is important to point out the Couchbase Lite dependencies within the solution. The [Couchbase.Lite Nuget package](https://www.nuget.org/packages/Couchbase.Lite/) is included as a reference within four projects of this solution:

* UserProfileDemo.Repositories
* UserProfileDemo.iOS
* UserProfileDemo.Android
* UserProfileDemo.UWP

The `Couchbase.Lite` Nuget package contains the core functionality for Couchbase Lite. In subsequent sections you will dive into the capabilities the package provides.

## [](#app-installation)App Installation

Clone the **_sync_** branch of the `User Profile Demo` project from GitHub. Type the following command in your terminal

```bash
git clone -b sync https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin.git
```

Try it Out

1. Open the `UserProfileDemo.sln` file. This is locate within `/path/to/UserProfileDemo/modules/userprofile/examples/src`.  
```bash  
open UserProfileDemo.sln  
```
2. Build and run the project using **two simulators/emulators**.
3. Verify that you see the login screen on both the simulators/emulators.  
![User Profile Login Screen Image](_images/user_profile_login.png)

## [](#data-model)Data Model

If you followed along with the [Query tutorial](../userprofile-query-xamarin/userprofile%5Fquery.md), you can skip this section and proceed to the [Backend Installation](#backend-installation) section. We have not changed the Data model for this tutorial.

Couchbase Lite is a JSON Document Store. A Document is a logical collection of named fields and values. The values are any valid JSON types. In addition to the standard JSON types, Couchbase Lite supports some special types like `Date` and `Blob`. While it is neither required nor enforced, it is recommended practice to include a _"type"_ property that can serve as a namespace for related documents.

### [](#the-user-profile-document)The User Profile Document

The app deals with a single Document with a _"type"_ property of _"user"_ as shown in [Example 1](#ex-user-profile-doc). The document ID is of the form _"user::demo@example.com"_.

Example 1\. A user profile document

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

### [](#userprofile-encoding)UserProfile Encoding

The _"user"_ Document is encoded to a `class` named _UserProfile_.

```c#
public class UserProfile
{
    public string type => "user";
    public string Id { get; set; }
    public string Name { get; set; }
    public string Email { get; set; }
    public string Address { get; set; }
    public byte[] ImageData { get; set; }
    public string Description { get; set; }
    public string University { get; set; }
}
```

{example$}

### [](#the-university-document)The University Document

The app comes bundled with a collection of Documents of type _"university"_. Each Document represents a university — see [Example 2](#ex-university-doc)

Example 2\. A university document

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

### [](#universityrecord-encoding)UniversityRecord Encoding

The _"university"_ `Document` is encoded to a `class` named _University_.

```c#
public class University
{
    public string Name { get; set; }
    public string Country { get; set; }
}
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
When the setup is completed, you should see output similar to that shown in [Figure 2](#ex-server-setup-output).  
![log output](_images/log-output.png)  
Figure 2\. Server set-up output
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
| 3.x     | [sync-gateway-config-userprofile-demo-3-x-legacy.json](https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin/tree/sync/content/modules/userprofile-sync-xamarin/examples/sync-gateway-config-userprofile-demo-3-x-legacy.json) |
| 2.x     | [sync-gateway-config-userprofile-demo-2-x.json](https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin/tree/sync/content/modules/userprofile-sync-xamarin/examples/sync-gateway-config-userprofile-demo-2-x.json)               |

#### [](#lbl-deploy)Deploy

Let us configure and launch Sync Gateway in a Docker container.

1. Switch to the the folder containing the cloned configuration files, using:  
```bash  
cd /path/to/cloned/repo/userprofile-couchbase-mobile/content/modules/userprofile-sync/examples  
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
Configuring and running Sync Gateway 3.0 in Docker using the configuration in `sync-gateway-config-userprofile-demo-3-x-legacy.json`.  
Note the use of `disable_persistent_config` in the configuration file to force legacy configuration mode.  
```bash  
 docker run -p 4984-4986:4984-4986 \
 --network workshop \
 --name sync-gateway \
 -d \
 -v `pwd`/sync-gateway-config-userprofile-demo-3-x-legacy.json:/etc/sync_gateway/sync_gateway.json \  
 couchbase/sync-gateway:3.0.0-enterprise \  
 /etc/sync_gateway/sync_gateway.json  
```  
Configuring and running Sync Gateway 2.8 in Docker  
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
Configuring and running Sync Gateway 3.0 in legacy mode  
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
2. Then open up <http://localhost:4984> in browser.  
You should see equivalent of the following message  
```bash  
{"couchdb":"Welcome","vendor":{"name":"Couchbase Sync Gateway","version":"3.0"},"version":"Couchbase Sync Gateway/3.0.0(145;e3f46be) EE"}  
```

Now that we have the server and the sync gateway installed, we can verify data sync between Couchbase Lite enabled apps.

## [](#lbl-sync-function)Sync Function

A key component of the sync process is the Sync Function and we will first look at how that can be set-up to control how data sync works.

The Sync Function is a Javascript-function that is specified as part of the Sync Gateway Configuration It handles [Authorization](#lbl-auth) , [Data Validation](#lbl-valid), [Data Routing](#lbl-route) and [Access Control](#lbl-access).

To get started learning about this function:

1. Open the your configuration file using a text editor of your choice. It will be located in the app bundle at  
`/path/to/cloned/repo/UserProfileDemo/content/modules/userprofile/examples`.
2. Locate the `sync` setting in the file

Now you can follow along with the rest of the sections below.

### [](#lbl-auth)Authorization

We use _Basic Authentication_ in our application. The Id of the user making the request is specified in the `Authorization` header.

Locate the `// Authorization` section of the Sync Function. You will see that we are using the Sync function's [requireUser()](../../sync-gateway/3.0/sync-function-api-require-user-cmd.md) API to verify that the `email` property specified in the Document matches the Id of the user making the request — see [Example 3](#ex-auth).

Example 3\. Sync function — Authorization

```JavaScript
function sync(doc, oldDoc) {

/* Authorization */

// Verify the user making the request is the same as the one in doc's email
requireUser(doc.email);


}
```

### [](#lbl-valid)Data Validation

In the sync function we also do some basic validation of the contents of the Document — as shown in [Example 4](#ex-validation).

Example 4\. Sync function — Data Validation

```javascript
/* Data Validation */

// Validate the presence of email field.
// This is the "username" (1)
validateNotEmpty("email", doc.email);

// Validate that the document Id _id is prefixed by owner (2)
var expectedDocId = "user" + "::" + doc.email;

(3)
if (expectedDocId != doc._id) {
  // reject document
  throw({forbidden: "user doc Id must be of form user::email"});
}
```

| **1** | Verify that the email property is not null. If it's null, we throw a JS exception (see validateNotEmpty() function)                                                        |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | If this a new document, then verify that the Id of the Document is of the required format (i.e. _"user::demo@example.com"_). We throw an exception if that's not the case. |
| **3** | If this is a document update, then verify that the email property value has not changed. Again, we throw an exception if that's not the case.                              |

> [!NOTE]
> You can learn more about the Sync Function in the documentation here: [Sync Function API](../../sync-gateway/3.0/sync-function.md)

### [](#lbl-route)Data Routing

[Channels](../../sync-gateway/3.0/channels.md) provide a mechanism to "tag" documents. They are typically used to route/segregate documents based on the contents of those documents — as shown in: [Example 5](#ex-routing).

When combined with the [access()](../../sync-gateway/3.0/sync-function-api-access-cmd.md) and [requireAccess()](../../sync-gateway/3.0/sync-function-api-require-access-cmd.md) API, the [channel()](../../sync-gateway/3.0/sync-function-api-channel-cmd.md) API can also be used to enforce [Access Control](#lbl-access).

As we shall see in a later section, clients can use channels to pull just a subset of documents.

Example 5\. Using channel() to tag/route documents

```javascript
/* Routing */

// Add doc to the user's channel.
var username = getEmail(); (1)

var channelId = "channel."+ username; (2)

channel(channelId); (3)
```

| **1** | Retrieve the the email property specified in the document. We will uses this as our user and channel name             |
| ----- | --------------------------------------------------------------------------------------------------------------------- |
| **2** | Here we generate the channel name from the email property.                                                            |
| **3** | Here we route the document to the channel. The channel comes into existence the first time a document is added to it. |

### [](#lbl-access)Access Control

We can enforce access control to channels using the [access()](../../sync-gateway/3.0/sync-function-api-access-cmd.md) API. The approach shown in [Example 6](#ex-access) ensures that only users with access to a specific channel are able to retrieve documents in the channel.

Example 6\. Controlling access to documents using channel() and access() API

```javascript
// Give user access to document (1)
access(username, channelId);
```

| **1** | Here we use the email property retrieved in [Example 5](#ex-routing) as the username and specify the channel the user is allowed to access |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#starting-replication)Starting Replication

Two-way Replication between the app and the Sync Gateway is enabled when user logs into the app.

* To see the code behind this, open the [**DatabaseManager.cs**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin/tree/sync/content/modules/userprofile-sync-xamarin/examples/src/UserProfileDemo.Repositories/DatabaseManager.cs) file and locate the `Start` method.  
```c#  
public async Task StartReplicationAsync(string username,  
                                        string password,  
                                        string[] channels,  
                                        ReplicatorType replicationType = ReplicatorType.PushAndPull,  
                                        bool continuous = true)  
```
* Next, we create an instance of the `ReplicatorConfig` instance that specifies the source and target database and you can optionally, override the default configuration settings.  
```c#  
var configuration = new ReplicatorConfiguration(database, targetUrlEndpoint) (1)  
{  
    ReplicatorType = replicationType, (2)  
    Continuous = continuous, (3)  
    Authenticator = new BasicAuthenticator(username, password), (4)  
    Channels = channels?.Select(x => $"channel.{x}").ToArray() (5)  
};  
```

| **1** | Initialize with Source as the local Couchbase Lite database and the remote target as the Sync Gateway                                                                                                                                                                                                                                                                                           |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Replication type of PushAndPull indicates that we require two-way sync. A value of .Pull specifies that we only pull data from the Sync Gateway. A value of .Push specifies that we only push data.                                                                                                                                                                                             |
| **3** | The Continuous mode is specified to be _true_ which means that changes are synced in real-time. A value of _false_ implies that data is only pulled from the Sync Gateway.                                                                                                                                                                                                                      |
| **4** | This is where you specify the authentication credentials of the user. In the [Authorization](#lbl-auth) section, we discussed that the Sync Gateway can enforce authorization check using the RequireUser API.                                                                                                                                                                                  |
| **5** | The Channels are used to specify the channels to pull from. Only documents belonging to the specified channels are synced. This is subject to [Access Control](#lbl-access) rights enforced at the Sync Gateway. This means that if a client does not have access to documents in a channel, the documents will not be synched even if the client specifies it in the replicator configuration. |
* Initialize the `Replicator` with the `ReplicatorConfiguration`  
```c#  
_replicator = new Replicator(configuration);  
```
* We attach a callback listener to the `Replicator` to be asynchronously notified of state changes. This could be useful for instance, to inform the user of the progress of the replication.  
This is an optional step.  
```c#  
_replicatorListenerToken = _replicator.AddChangeListener(OnReplicatorUpdate);  
```
* Which is handled by a method called `OnReplicatorUpdate`  
```c#  
void OnReplicatorUpdate(object sender, ReplicatorStatusChangedEventArgs e)  
{  
    var status = e.Status;  
    switch (status.Activity)  
    {  
        case ReplicatorActivityLevel.Busy:  
            Console.WriteLine("Busy transferring data.");  
            break;  
        case ReplicatorActivityLevel.Connecting:  
            Console.WriteLine("Connecting to Sync Gateway.");  
            break;  
        case ReplicatorActivityLevel.Idle:  
            Console.WriteLine("Replicator in idle state.");  
            break;  
        case ReplicatorActivityLevel.Offline:  
            Console.WriteLine("Replicator in offline state.");  
            break;  
        case ReplicatorActivityLevel.Stopped:  
            Console.WriteLine("Completed syncing documents.");  
            break;  
    }  
    if (status.Progress.Completed == status.Progress.Total)  
    {  
        Console.WriteLine("All documents synced.");  
    }  
    else  
    {  
        Console.WriteLine($"Documents {status.Progress.Total - status.Progress.Completed} still pending sync");  
    }  
}  
```
* Start the replicator  
```c#  
_replicator.Start();  
```

## [](#stopping-replication)Stopping Replication

When user logs out of the app, the replication is stopped before the database is closed.

* Open the [**DatabaseManager.cs**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin/tree/sync/content/modules/userprofile-sync-xamarin/examples/src/UserProfileDemo.Repositories/DatabaseManager.cs) file and locate the `Stop` function.  
```c#  
public void StopReplication()  
```
* Stop the replicator and remove any associated change listeners  
```c#  
_replicator.RemoveChangeListener(_replicatorListenerToken);  
_replicator.Stop();  
```

> [!TIP]
> When you close a database, any active replicators, listeners and-or live queries are also be closed.

## [](#lbl-query-events)Query Events and Live Queries

Couchbase Lite applications can set up _live queries_ in order to be asynchronously notified of changes to the database that affect the results of the query. This can be very useful, for instance, in keeping a UI View up-to-date with the results of a query.

In our app, the user profile view is kept up-to-date using a live query that fetches the user profile data used to populate the view. This means that, if the replicator pulls down changes to the user profile, they are automatically reflected in the view.

To see this:

1. Open the [**UserProfileRepository.cs**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin/tree/sync/content/modules/userprofile-sync-xamarin/examples/src/UserProfileDemo.Repositories/UserProfileRepository.cs) file
2. Locate the `GetAsync` function.  
Calling this method and passing in a value for the `Func<UserProfile,Task>` named `onProfileUpdated` implies that the caller wishes to be notified of any changes to query results via delegation.  
```c#  
public async Task<UserProfile> GetAsync(string userProfileId, Action<UserProfile> userProfileUpdated)  
```
3. Build the Query using `QueryBuilder` API.  
If you are unfamiliar with this API, please check out this [tutorial](https://developer.couchbase.com/documentation/mobile/2.0/userprofile%5Fquery.html).  
```c#  
_userQuery = QueryBuilder  
                .Select(SelectResult.All())  
                .From(DataSource.Database(database))  
                .Where(Meta.ID.EqualTo(Expression.String(userProfileId))); (1)  
```

| **1** | We query for documents based on document Id. In our app, there should be exactly one user profile document corresponding to this Id. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------ |
4. Attach listener callback to the query to make it _live_  
```c#  
_userQueryToken = _userQuery.AddChangeListener((object sender, QueryChangedEventArgs e) => (1)  
{  
    if (e?.Results != null && e.Error == null)  
    {  
        foreach (var result in e.Results.AllResults())  
        {  
            var dictionary = result.GetDictionary("userprofile"); (2)  
            if (dictionary != null)  
            {  
                userProfile = new UserProfile (3)  
                {  
                    Name = dictionary.GetString("name"), (4)  
                    Email = dictionary.GetString("email"),  
                    Address = dictionary.GetString("address"),  
                    University = dictionary.GetString("university"),  
                    ImageData = dictionary.GetBlob("imageData")?.Content  
                };  
            }  
        }  
        if (userProfile != null)  
        {  
            userProfileUpdated.Invoke(userProfile);  
        }  
    }  
});  
```

| **1** | Attach a listener callback to the query. Attaching a listener automatically makes it _live_. So any time there is a change in the user profile data in the underlying database, the callback will be invoked.                                                                                                                                                                 |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The SelectResult.all() method is used to query all the properties of a document. In this case, the document in the result is embedded in a dictionary where the key is the database name, which is _"userprofiles"_. So, we retrieve the [DictionaryObject](http://docs.couchbase.com/mobile/2.0/couchbase-lite-swift/Classes/DictionaryObject.html) at key _"userprofiles"_. |
| **3** | Create an instance of [\[UserProfile\]](#UserProfile). This will be populated with the query results.                                                                                                                                                                                                                                                                         |
| **4** | We use appropriate _type getters_ to retrieve values and populate the _UserProfile_ instance                                                                                                                                                                                                                                                                                  |

## [](#exercises)Exercises

> [!TIP]
> If you are running the application in Android emulator(s) then you will need to change the URL of the remote Sync Gateway in `DatabaseManager.cs`.
> 
> 1. Find and uncomment the following line:  
> `readonly Uri _remoteSyncUrl = new Uri("ws://10.0.2.2:4984");`
> 2. Comment out the standard line:  
> `readonly Uri _remoteSyncUrl = new Uri("ws://localhost:4984");`

### [](#exercise-1)Exercise 1

In this exercise, we will observe how changes made on one app are synced across to the other app

* The app should be running in two simulators/emulators side by side
* Log into both the simulators/emulators using the same user credentials:

  * Username — _"[demo@example.com](mailto:demo@example.com)"_
  * Password — _"password"_
* On one simulator/emulator, enter values in the profile's user and address fields.
* Confirm that changes show up in the app on the other simulator/emulator.
* Similarly, make changes to the app in the other simulator/emulator and confirm that the changes are synced over to the first simulator/emulator.

### [](#exercise-2)Exercise 2

In this exercise, we will observe how changes made using the Sync Gateway API are synced with the Couchbase Lite apps.

1. Make sure you complete [Exercise 1](#exercise-1).  
This is to ensure that you have the appropriate user profile document (with document Id of "user::<emailId>") created through the app and synced over to the Sync Gateway.
2. Open the command terminal and issue the following command to get the user profile document via \[GET Document REST API\]. We will be using `curl` to issue the request. If you haven't done so, please install curl as indicated in the [Prerequisites](#prerequisites) section  
```bash  
curl -X GET \  
  http://localhost:4985/userprofile/user::demo@example.com \
  -H 'Accept: application/json' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json'  
```
3. Your response should look something like the response below. The exact contents depends on the user profile information that you provided via your mobile app.  
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

| **1** | If you updated an image via the mobile app, you should see an **"\_attachments"** property. This entry holds an array of attachments corresponding to each image blob entry added by the mobile app. This property is added by the Sync Gateway when it processes the document.You can learn more about how image Blob types are mapped to attachments here in the Couchbase Lite documentation: [Working with Blobs](../../couchbase-lite/3.0/swift/blob.md). |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Record the revision Id of the document. You will need this when you update the document                                                                                                                                                                                                                                                                                                                                                                        |
4. In the command terminal, issue the following command to update the user profile document via  
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
5. Confirm that you get a HTTP _"201 Created"_ status code
6. As soon as you update the document via the Sync Gateway REST API, confirm that the changes show up in the mobile app on the simulator/emulator.  
![App Sync](_images/sync_from_sgw.gif)

## [](#handling-conflicts-during-data-synchronization)Handling Conflicts during Data Synchronization

Data conflicts are inevitable in an environment where you can potentially have multiple writes updating the same data concurrently. Couchbase Mobile supports _Automated Conflict Resolution_.

You can learn more about automated conflict resolution in this blog [Document Conflicts & Resolution ](https://blog.couchbase.com/document-conflicts-couchbase-mobile/).

## [](#learn-more)Learn More

Congratulations on completing this tutorial!

This tutorial walked you through an example of how to use a Sync Gateway to synchronize data between Couchbase Lite enabled clients. We discussed how to configure your Sync Gateway to enforce relevant access control, authorization and data routing between Couchbase Lite enabled clients.

Check out the following links for further details

Further Reading

* [Sync Gateway Configuration](../../sync-gateway/3.0/configuration-overview.md)
* [Couchbase Mobile Blog](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu)
* [Sync function blogs](https://blog.couchbase.com/?s=sync+function)
* [Overview of Replication Protocol](https://blog.couchbase.com/data-replication-couchbase-mobile/)
* [Document Conflicts & Resolution ](https://blog.couchbase.com/document-conflicts-couchbase-mobile/)