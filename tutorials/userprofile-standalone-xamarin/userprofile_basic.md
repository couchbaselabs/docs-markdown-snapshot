---
title: "User Profile Sample: Couchbase Lite Fundamentals"
editUrl: https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin/edit/standalone/content/modules/userprofile-standalone-xamarin/pages/userprofile_basic.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/tutorials/userprofile-standalone-xamarin/userprofile_basic.html)

# User Profile Sample: Couchbase Lite Fundamentals

## [](#introduction)Introduction

Couchbase Mobile brings the power of NoSQL to the edge. It is comprised of three components:

* _Couchbase Lite_, an embedded, NoSQL JSON Document Style database for your mobile apps
* _Sync Gateway_, an internet-facing synchronization mechanism that securely syncs data between mobile clients and server, and
* _Couchbase Server_, a highly scalable, distributed NoSQL database platform

Couchbase Mobile supports flexible deployment models. You can deploy:

* Couchbase Lite as a standalone embedded database within your mobile apps or,
* Couchbase Lite enabled mobile clients with a Sync Gateway to synchronize data between your mobile clients or,
* Couchbase Lite enabled clients with a Sync Gateway to sync data between mobile clients and the Couchbase Server, which can persist data in the cloud (public or private)

What You Will Learn

This tutorial will walk you through a very basic example of how you can use **Couchbase Lite in standalone mode** within your Swift app. In this mode, Couchbase Lite will serve as a local, embedded data store within your iOS App and can be a replacement for SQLite or Core Data.

You will learn the fundamentals of:

* Database Operations
* Document CRUD Operations

You can learn more about Couchbase Mobile [here](https://developer.couchbase.com/mobile)

## [](#prerequisites)Prerequisites

This tutorial assumes familiarity with building [Xamarin](https://www.xamarin.com), more specifically Xamarin.Forms, apps using C# and XAML.

* iOS (Xcode 12.5+)
* Android (SDK 22+)
* UWP (Windows 10)
* git (Optional) This is required if you would prefer to pull the source code from GitHub repo.

  * Create a [free github account](https://github.com)if you don’t already have one
  * git can be downloaded from [git-scm.org](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## [](#app-overview)App Overview

We will be working with a very simple _User Profile_ app. It does one thing — Allow a user to log in and create or update their user profile data\*

The user profile data is persisted as a Document in the local Couchbase Lite Database. So, when the user logs out and logs back in again, the profile information is loaded from the Database.

![The sample user profile application running in a simulator](_images/user_profile.gif) 

Figure 1\. The sample user profile application running in a simulator

## [](#installation)Installation

Clone the **_standalone_** branch of the `User Profile Demo` solution from GitHub. Assuming that you have [Git](https://git-scm.com/downloads)installed you can do this using the following command:

```bash
git clone -b standalone https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin.git
```

Next, let’s verify the installation.

Try it Out

1. Open the `UserProfileDemo.sln`. The project would be located at `/path/to/UserProfileDemo/modules/userprofile/examples/src`.  
```bash  
open UserProfileDemo.sln  
```
2. Build the solution using your preferred IDE (e.g. [Visual Studio for Windows or Mac](https://visualstudio.microsoft.com/)) or [directly through command line](https://docs.microsoft.com/en-us/dotnet/core/tools/dotnet-build?tabs=netcore2x).
3. [Run the app](https://docs.microsoft.com/en-us/xamarin/get-started/first-app/index?pivots=windows)on a device or simulator/emulator.
4. Verify that you see the login screen.  
![User Profile Login Screen Image](_images/user_profile_login.png)

## [](#solution-overview)Solution Overview

The User Profile demo app is a Xamarin.Forms based solution that supports iOS and Android mobile platforms.

The solution utilizes various design patterns and principles such as [MVVM](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel), [IoC](https://en.wikipedia.org/wiki/Inversion%5Fof%5Fcontrol), and the Repository Pattern.

The solution consists of seven projects.

* **UserProfileDemo**: A .NET Standard project responsible for maintaining view-level functionality.
* **UserProfileDemo.Core**: A .NET Standard project responsible for maintaining viewmodel-level functionality.
* **UserProfileDemo.Models**: A .NET Standard project consisting of simple data models.
* **UserProfileDemo.Repositories**: A .NET Standard project consisting of repository classes responsible for Couchbase Lite database initialization, interaction, etc.
* **UserProfileDemo.iOS**: A Xamarin.iOS platform project responsible for building the `.ipa` file.
* **UserProfileDemo.Android**: A Xamarin.Android platform project responsible for building the `.apk` file.
* **UserProfileDemo.UWP**: A UWP platform project responsible for building the `.exe` file.

Now that you have an understanding of the solution architecture let’s dive into the app!

## [](#couchbase-lite-nuget)Couchbase Lite Nuget

Before diving into the code for the apps, it is important to point out the Couchbase Lite dependencies within the solution. The [Couchbase.Lite Nuget package](https://www.nuget.org/packages/Couchbase.Lite/)is included as a reference within four projects of this solution:

* UserProfileDemo.Repositories
* UserProfileDemo.iOS
* UserProfileDemo.Android
* UserProfileDemo.UWP

The `Couchbase.Lite` Nuget package contains the core functionality for Couchbase Lite.

In the following sections you will dive into the capabilities the package provides.

## [](#getting-started-on-android)Getting started on Android

In order to use Couchbase Lite within a Xamarin app for Android you will need to activate it.

Open [MainActivity.cs](https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin/tree/standalone/content/modules/userprofile-standalone-xamarin/examples/src/UserProfileDemo.Android/MainActivity.cs) in the `UserProfileDemo.Android` project.

```c#
Couchbase.Lite.Support.Droid.Activate(this);
```

## [](#data-model)Data Model

Let’s take a look at the foundations of Couchbase; data models and documents.

Couchbase Lite is a JSON Document Store. A Document is a logical collection of named fields and values. The values are any valid JSON types. In addition to the standard JSON types, Couchbase Lite supports `Date` and `Blob` data types. While it is not required or enforced, it is a recommended practice to include a _"type"_ property that can serve as a namespace for related documents.

### [](#lbl-user-profile-document)The User Profile Document

The app deals with a single Document with a _"type"_ property of _"user"_ as shown in [Example 1](#ex-user-profile-doc). The document ID is of the form _"user::demo@example.com"_.

Example 1\. A user profile document

```json
{
    "type":"user",
    "name":"Jane Doe",
    "email":"jame.doe@earth.org",
    "address":"101 Main Street",
    "image":CBLBlob (image/jpg) (1)
}
```

| **1** | The special 'blob' data type associated with the profile image — see: [Working with Blobs](#3.0@couchbase-lite:swift:blob.adoc) |
| ----- | ------------------------------------------------------------------------------------------------------------------------------- |

### [](#lbl-user-record)The User Record

The _"user"_ Document is encoded to a native struct named _UserRecord_ as shown in [Example 2](#ex-user-rec)

Example 2\. The encoding of a UserRecord to a native structure

Unresolved include directive in modules/userprofile-standalone-xamarin/pages/userprofile_basic.adoc - include::example$UserProfileDemo/model/UserRecord.swift[]

## [](#basic-database-operations)Basic Database Operations

In this section, we will do a code walk-through of the basic Database operations

### [](#lbl-create-open-database)Create / Open a Database

When a user logs in, we create an empty Couchbase Lite database for the user if one does not exist.

* Open the [**BaseRepository.cs**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin/tree/standalone/content/modules/userprofile-standalone-xamarin/examples/src/UserProfileDemo.Repositories/BaseRepository.cs) file and locate the `Database` property. When the `Database` property is used for the first time a Couchbase Lite database is opened, or created if it does not already exist via the instantiation of a new object.  
```c#  
Database _database;  
protected Database Database  
{  
    get  
    {  
        if (_database == null)  
        {  
            _database = new Database(DatabaseName, DatabaseConfig);  
        }  
        return _database;  
    }  
    private set => _database = value;  
}  
```
* We create an instance of the `DatabaseConfiguration` within [**UserProfileRepository.cs**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin/tree/standalone/content/modules/userprofile-standalone-xamarin/examples/src/UserProfileDemo.Repositories/UserProfileRepository.cs)via an `abstract` requirement from the parent class, `BaseRepository`.  
This is an optional step. In our case, we would like to override the default path of the database. Every user has their own instance of the `Database` that is located in a folder corresponding to the user. Please note that the default path is platform specific.  
```c#  
DatabaseConfiguration _databaseConfig;  
protected override DatabaseConfiguration DatabaseConfig  
{  
    get  
    {  
        if (_databaseConfig == null)  
        {  
            if (AppInstance.User?.Username == null)  
            {  
                throw new Exception($"Repository Exception: A valid user is required!");  
            }  
            _databaseConfig = new DatabaseConfiguration  
            {  
                Directory = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData),  
                                AppInstance.User.Username)  
            };  
        }  
        return _databaseConfig;  
    }  
    set => _databaseConfig = value;  
}  
```
* Then we create a local Couchbase Lite database named **_"userprofile"_** for the user. If a database already exists for the user, the existing version is returned.  
```c#  
_database = new Database(DatabaseName, DatabaseConfig);  
```

### [](#listening-to-database-changes)Listening to Database Changes

You can be asynchronously notified of any change (add, delete, update) to the `Database` by registering a change listener with the `Database`.  
In our app, we are not doing anything special with the `Database` change notification other than logging the change. In a real world app, you would use this notification for instance, to update the UI.

* Open the [**BaseRepository.cs**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin/tree/standalone/content/modules/userprofile-standalone-xamarin/examples/src/UserProfileDemo.Repositories/BaseRepository.cs)file and locate the `Database.AddChangeListener` function usage within the constructor.  
```c#  
DatabaseListenerToken = Database.AddChangeListener(OnDatabaseChangeEvent);  
```
* To register a change listener with the database we add the delegate method `OnDatabaseChangeEvent`. This is an optional step. The `AddChangeListener` method returns a `ListenerToken`. The `ListenerToken` is required to remove the listener from the database.  
The listener is a delegate method that takes two parameters of type `object` and `DatabaseChangedEventArgs` respectively.  
```c#  
void OnDatabaseChangeEvent(object sender, DatabaseChangedEventArgs e)  
{  
    foreach (var documentId in e.DocumentIDs)  
    {  
        var document = Database?.GetDocument(documentId);  
        string message = $"Document (id={documentId}) was ";  
        if (document == null)  
        {  
            message += "deleted";  
        }  
        else  
        {  
            message += "added/updaAted";  
        }  
        Console.WriteLine(message);  
    }  
}  
```

### [](#close-database)Close Database

When a user logs out, we close the Couchbase Lite database associated with the user, deregister any database change listeners, and free up memory allocations.

Open the [**BaseRepository.cs**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin/tree/standalone/content/modules/userprofile-standalone-xamarin/examples/src/UserProfileDemo.Repositories/BaseRepository.cs)file and locate the `Dispose` method. In our sample `Dispose` handles the removal of database listeners, removing various objects from memory, and closing the database. `Dispose` will be called when a user logs out.

```c#
public void Dispose()
{
    DatabaseConfig = null;

    Database.RemoveChangeListener(DatabaseListenerToken);
    Database.Close();
    Database = null;
}
```

Try it out

1. Run the app to be tested using a simulator/emulator or device.
2. Log into the app with any username and password.  
Use the values _"[demo@example.com](mailto:demo@example.com)"_ and _"password"_ for username and password fields respectively.  
If this is the first time that the user is signing in, a new Couchbase Lite database will be created. If not, the user’s existing database will be opened.
3. Confirm that the console log output has a message similar to the one below.  
In my example, I am logging in with a username of _"[demo@example.com](mailto:demo@example.com)"_.  
This will open (or create) a database at path `/Users/[user_name]/Library/Developer/CoreSimulator/Devices/[unique_device_id]/data/Containers/Data/Application/[unique_app_id]/Library/Application Support/demo@example.com`
4. Note the folder location of the database, which is indicated in the above log message
5. Open the folder in your Finder app and verify that a database with name _"userprofile"_ is exists for the user  
![User Profile Database Location](_images/db_location.png)

## [](#document-operations)Document Operations

Once an instance of the Couchbase Lite database is created/opened for the specific user, we can perform basic `Document` functions on the database.

In this section, we will walk-through the code that describes basic `Document` operations

### [](#reading-a-document)Reading a Document

Once the user logs in, the user is taken to the "Your Profile" screen. A request is made to load [The User Profile Document](#lbl-user-profile-document) for the user. When the user logs in the very first time, there would be no _user profile_ document for the user.

* Open the [**UserProfileViewModel.cs**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin/tree/standalone/content/modules/userprofile-standalone-xamarin/examples/src/UserProfileDemo.Core/ViewModels/UserProfileViewModel.cs)file and locate the `userProfileDocId` definition. This document Id is constructed by prefixing the term "user::" to the username of the user.  
```c#  
string UserProfileDocId => $"user::{AppInstance.User.Username}";  
```
* The `UserProfileViewModel` is tasked with retrieving the profile for a logged in user. It does this by using a class that implements `IUserProfileRepository`.  
```c#  
var up = UserProfileRepository?.Get(UserProfileDocId);  
```
* In the [**UserProfileRepository.cs**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin/tree/standalone/content/modules/userprofile-standalone-xamarin/examples/src/UserProfileDemo.Repositories/UserProfileRepository.cs)file, locate the `Get` function.  
```c#  
public override UserProfile Get(string userProfileId)  
```
* We try to fetch the document with specified `userProfileDocId` from the database.  
```c#  
var document = Database.GetDocument(userProfileId);  
if (document != null)  
{  
    userProfile = new UserProfile  
    {  
        Id = document.Id,  
        Name = document.GetString("Name"),  
        Email = document.GetString("Email"),  
        Address = document.GetString("Address"),  
        ImageData = document.GetBlob("ImageData")?.Content  
    };  
}  
```

| **1** | Fetch an **immutable** copy of the Document from the database.                                                                                                                                                                      |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Create an instance of [The User Record](#lbl-user-record) object                                                                                                                                                                    |
| **3** | Set the email property of the UserProfile with the username of the logged in user. **Note:** This value is not editable after it’s initially saved.                                                                                 |
| **4** | If the document exists and is fetched successfully, a variety of methods exist that can be used to fetch members of the Document. Specifically, note the support of the GetBlob type to fetch the value of a property of type Blob. |

### [](#creating-updating-a-document)Creating / Updating a Document

A [The User Profile Document](#lbl-user-profile-document) is created for the user when the user taps the "Done" button on the "Profile Screen". The function below applies whether you are creating a document or updating an existing version

* The `UserProfileViewModel` is tasked with setting values of a profile for a logged in user, and saving them to the database. It does this by using a class that implements `IUserProfileRepository`.  
```c#  
bool? success = UserProfileRepository?.Save(userProfile);  
```
* Open the [**UserProfileRepository.cs**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin/tree/standalone/content/modules/userprofile-standalone-xamarin/examples/src/UserProfileDemo.Repositories/UserProfileRepository.cs) file and locate the `Save` function.  
```c#  
public override bool Save(UserProfile userProfile)  
```
* We create a **mutable** instance of the `Document`. By default, all APIs in Couchbase Lite deal with immutable objects, thereby making them **thread-safe** by design. In order to mutate an object, you must explicitly get a mutable copy of the object. Use appropriate type-setters to set the various properties of the `Document`  
```c#  
var mutableDocument = new MutableDocument(userProfile.Id);  
mutableDocument.SetString("Name", userProfile.Name);  
mutableDocument.SetString("Email", userProfile.Email);  
mutableDocument.SetString("Address", userProfile.Address);  
mutableDocument.SetString("type", "user");  
if (userProfile.ImageData != null)  
{  
    mutableDocument.SetBlob("ImageData", new Blob("image/jpeg", userProfile.ImageData));  
}  
```

| **1** | Specifically, note the support of the SetBlob type to fetch the value of a property of type Blob. Save the document Database.Save(mutableDocument); |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#deleting-a-document)Deleting a Document

We don’t delete a `Document` in this sample app. However, deletion of a document is pretty straightforward and this is how you would do it.

```c#
var document = Database.GetDocument(id);

if (document != null)
{
    Database.Delete(document);
}
```

Try It Out

1. You should have followed the steps discussed in the "Try It Out" section under [Create / Open a Database](#lbl-create-open-database)
2. Enter a "name" for the user in the Text Entry box and Tap "Done"
3. Confirm that you see an alert message "Succesfully Updated Profile". The first time, you update the profile screen, the Document will be created.  
![User Profile Document Creation](_images/doc_create.png)
4. Now tap on the "Upload Image" button and select an image from the Photo Album. Tap "Done".  
![100](_images/image_selection.gif)
5. Confirm that you see an alert message "Successfully Updated Profile". The Document will be updated this time.
6. Tap "Log Off" and log out of the app
7. Log back into the app with the same user credentials you used earlier. In my example, I used _"demo@example.com"_ and _"password"_. So I will log in with those credentials again.
8. Confirm that you see the profile screen with the _name_ and _image_ values that you set earlier.  
![200](_images/log_off_on.gif)

## [](#learn-more)Learn More

Congratulations on completing this tutorial!

This tutorial walked you through a very basic example of how to get up and running with Couchbase Lite as a local-only, standalone embedded data store in your iOS, Android, or UWP app. If you want to learn more about Couchbase Mobile, check out the following links.

Further Reading

* [Introduction to Couchbase Mobile](https://www.couchbase.com/products/mobile)
* [Couchbase Mobile Overview](https://blog.couchbase.com/couchbase-mobile-2-0/)
* [Couchbase Lite Reference Guide](https://developer.couchbase.com/documentation/mobile/2.0/couchbase-lite/index.html)
* [Couchbase Mobile Blogs](https://blog.couchbase.com/category/couchbase-mobile/)