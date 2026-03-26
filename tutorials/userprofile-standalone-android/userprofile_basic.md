---
title: "User Profile Sample: Couchbase Lite Fundamentals"
editUrl: https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/edit/standalone/content/modules/userprofile-standalone-android/pages/userprofile_basic.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:tutorials:userprofile-standalone-android:userprofile_basic.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/userprofile-standalone-android/userprofile_basic.html)

# User Profile Sample: Couchbase Lite Fundamentals

## [](#introduction)Introduction

Couchbase Mobile brings the power of NoSQL to the edge. It is comprised of three components:

* **Couchbase Lite**, an embedded, NoSQL JSON Document Style database for your mobile apps.
* **Sync Gateway**, an internet-facing synchronization mechanism that securely syncs data between mobile clients and server.
* **Couchbase Server**, a highly scalable, distributed NoSQL database platform.

Couchbase Mobile supports flexible deployment models. You can deploy:

* Couchbase Lite as a standalone embedded database within your mobile apps or
* Couchbase Lite enabled mobile clients with a Sync Gateway to synchronize data between your mobile clients or,
* Couchbase Lite enabled clients with a Sync Gateway to sync data between mobile clients and the Couchbase Server, which can persist data in the cloud (public or private)

What You Will Learn

This tutorial will walk you through a very basic example of how you can use **Couchbase Lite in standalone mode** within your [**Android**](https://www.android.com)app.

You will learn the fundamentals of

* Database Operations
* Document CRUD Operations

You can learn more about Couchbase Mobile [here](https://developer.couchbase.com/mobile)

## [](#prerequisites)Prerequisites

This tutorial assumes familiarity with building Android apps using [Java](https://www.java.com).

* [Android Studio](https://developer.android.com/studio)
* Android device or emulator running API level 22 or above
* Android SDK 29
* Android Build Tools 29
* [JDK 8](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
* git (Optional)  
This is required if you would prefer to pull the source code from GitHub repo.

  * Create a [free github account](https://github.com)if you don't already have one.  
  git can be downloaded from [git-scm.org](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## [](#app-overview)App Overview

In this tutorial you will be working with an app that allows users to log in and make changes to their user profile information.

User profile information is persisted as a `Document` in the local Couchbase Lite `Database`. When the user logs out and logs back in again, the profile information is loaded from the `Database`.

![User Profile App Demo](_images/user_profile.gif) 

## [](#app-installation)App Installation

Clone the **_standalone_** branch of the `User Profile Demo` repository from GitHub. Assuming that you have [Git](https://git-scm.com/downloads)installed you can use the following command to clone the solution:

```console
git clone -b standalone https://github.com/couchbaselabs/userprofile-couchbase-mobile-android.git
```

### [](#installing-couchbase-lite-framework)Installing Couchbase Lite Framework

This [sample project](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/standalone/content/modules/userprofile-standalone-android/examples/src) already contains the appropriate additions for downloading, and utilizing the Android Couchbase Lite dependency module. However, in the future, to include Couchbase Lite support within an Android app add the the following within [app/build.gradle](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/standalone/content/modules/userprofile-standalone-android/examples/src/app/build.gradle).

```console
dependencies {
    implementation 'com.couchbase.lite:couchbase-lite-android-ee:3.0.0'
}
```

Try it out

1. Open [build.gradle](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/standalone/content/modules/userprofile-standalone-android/examples/src/build.gradle) using Android Studio.
2. Build and run the project.
3. Verify that you see the login screen.  
![User Profile Login Screen Image](_images/user_profile_login.png)

## [](#sample-app-architecture)Sample App Architecture

The sample app follows the [MVP pattern](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter), separating the internal data model, from a passive view through a presenter that handles the logic of our application and acts as the conduit between the model and the view.

![MVP Architecture](_images/mvp_architecture.png) 

In the Android Studio project, the code is structured by feature. You can select the Android option in the left navigator to view the files by package.

![MVP Android Studio](_images/mvp_as.png) 

Each package contains 3 different files:

* **Activity**: This is where all the view logic resides.
* **Presenter**: This is where all the business logic resides to fetch and persist data to a web service or the embedded Couchbase Lite database.
* **Contract**: An interface that the `Presenter` and `Activity` implement.

![MVP Package](_images/mvp_package.png) 

## [](#data-model)Data Model

Couchbase Lite is a JSON Document Store. A `Document` is a logical collection of named fields and values. The values are any valid JSON types. In addition to the standard JSON types, Couchbase Lite supports `Date` and `Blob` data types. While it is not required or enforced, it is a recommended practice to include a _"type"_ property that can serve as a namespace for related documents.

### [](#the-user-profile-document)The "User Profile" Document

The sample app deals with a single `Document` with a _"type"_ property of _"user"_. The document ID is of the form _"user::<email>"_.

An example of a document would be

```json
{
    "type":"user",
    "name":"Jane Doe",
    "email":"jane.doe@earth.org",
    "address":"101 Main Street",
    "image":CBLBlob (image/jpg) (1)
}
```

| **1** | Special [Blob](https://docs.couchbase.com/couchbase-lite/current/java.html#blobs) data type that is associated with the profile image. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------- |

### [](#userprofile)UserProfile

For the purpose of this tutorial the _"user"_ `Document` is first stored within an `Object` of type `Map<String, Object>`.

```java
Map<String, Object> profile = new HashMap<>();
profile.put("name", nameInput.getText().toString());
profile.put("email", emailInput.getText().toString());
profile.put("address", addressInput.getText().toString());

byte[] imageViewBytes = getImageViewBytes();

if (imageViewBytes != null) {
    profile.put("imageData", new com.couchbase.lite.Blob("image/jpeg", imageViewBytes));
}
```

The `Map<String, Object>` object functions are used as a data storage mechanism between the app's UI and the backing functionality of the Couchbase Lite `Document` object.

## [](#basic-database-operations)Basic Database Operations

In this section, we will do a code walk-through of the basic Database operations.

### [](#initialize-couchbase-lite)initialize Couchbase Lite

Before you can start using Couchbase Lite on Android, you would have to initialize it, with an appropriate Android Application Context.

* Open the [**DatabaseManager.java**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/standalone/content/modules/userprofile-standalone-android/examples/src/app/src/main/java/com/couchbase/userprofile/util/DatabaseManager.java) file and locate the `initCouchbaseLite` method.  
```java  
public void initCouchbaseLite(Context context) {  
    CouchbaseLite.init(context);  
}  
```

### [](#create-and-open-a-database)Create and Open a Database

When a user logs in, we create an empty Couchbase Lite database for the user if one does not exist.

* Open the [**DatabaseManager.java**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/standalone/content/modules/userprofile-standalone-android/examples/src/app/src/main/java/com/couchbase/userprofile/util/DatabaseManager.java) file and locate the `openOrCreateDatabaseForUser` method.  
```java  
public void openOrCreateDatabaseForUser(Context context, String username)  
```
* We create an instance of the `DatabaseConfiguration` within [**DatabaseManager.java**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/standalone/content/modules/userprofile-standalone-android/examples/src/app/src/main/java/com/couchbase/userprofile/util/DatabaseManager.java) via an `abstract` requirement from the parent class, `BaseRepository`. This is an optional step. In our case, we would like to override the default path of the database. Every user has their own instance of the `Database` that is located in a folder corresponding to the user. Please note that the default path is platform specific.  
```java  
DatabaseConfiguration config = new DatabaseConfiguration();  
config.setDirectory(String.format("%s/%s", context.getFilesDir(), username));  
```
* Then we create a local Couchbase Lite database named **_"userprofiles"_** for the user. If a database already exists for the user, the existing version is returned.

```java
database = new Database(dbName, config);
```

### [](#listening-to-database-changes)Listening to Database Changes

You can be asynchronously notified of any change (add, delete, update) to the Database by registering a change listener with the Database. In our app, we are not doing anything special with the Database change notification other than logging the change. In a real world app, you would use this notification for instance, to update the UI.

* Open the [**DatabaseManager.java**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/standalone/content/modules/userprofile-standalone-android/examples/src/app/src/main/java/com/couchbase/userprofile/util/DatabaseManager.java) file and locate the `registerForDatabaseChanges()` function.

```java
+
----
[data-source-url=https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/blob/07a91be0cffbcee9e7afd069117b61f48bfa1ca8/content/modules/userprofile-standalone-android/examples/src/app/src/main/java/com/couchbase/userprofile/util/DatabaseManager.java]
private void registerForDatabaseChanges()
----
```

* We register a change listener with the database. This is an optional step. We track the `ListenerToken` as it is needed for removing the listener.  
```java  
// Add database change listener  
listenerToken = database.addChangeListener(new DatabaseChangeListener() {  
    @Override  
    public void changed(final DatabaseChange change) {  
        if (change != null) {  
            for(String docId : change.getDocumentIDs()) {  
                Document doc = database.getDocument(docId);  
                if (doc != null) {  
                    Log.i("DatabaseChangeEvent", "Document was added/updated");  
                }  
                else {  
                    Log.i("DatabaseChangeEvent","Document was deleted");  
                }  
            }  
        }  
    }  
});  
```

### [](#close-a-database)Close a Database

When a user logs out, we close the Couchbase Lite Database associated with the user and deregister any database change listeners

* Open the [**DatabaseManager.java**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/standalone/content/modules/userprofile-standalone-android/examples/src/app/src/main/java/com/couchbase/userprofile/util/DatabaseManager.java) file and locate the `closeDatabaseForCurrentUser()` function.  
```java  
public void closeDatabaseForUser()  
```
* Closing the database is pretty straightforward  
```java  
database.close();  
```

### [](#de-registering-from-database-changes)De-registering from Database Changes

* Open the [**DatabaseManager.java**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/standalone/content/modules/userprofile-standalone-android/examples/src/app/src/main/java/com/couchbase/userprofile/util/DatabaseManager.java) file and locate the `deregisterForDatabaseChanges()` function.  
```java  
private void deregisterForDatabaseChanges()  
```
* We stop listening to database changes by passing in the `ListenerToken` associated with the listener.  
```java  
database.removeChangeListener(listenerToken);  
```

Try it out

1. The app can be tested using a simulator/emulator or device.
2. Log into the app with any username and password.  
Let's use the values _"demo@example.com"_ and _"password"_ for username and password fields respectively.  
If this is the first time that the user is signing in, a new Couchbase Lite database will be created. If not, the user's existing database will be opened.

## [](#document-operations)Document Operations

Once an instance of the Couchbase Lite database is created/opened for the specific user, we can perform basic `Document` functions on the database. In this section, we will walk-through the code that describes basic `Document` operations

### [](#reading-a-document)Reading a Document

Once the user logs in, the user is taken to the "Your Profile" screen. A request is made to load [The "User Profile" Document](#the-user-profile-document) for the user. When the user logs in the very first time, there would be no _user profile_ document for the user.

* Open the [**DatabaseManager.java**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/standalone/content/modules/userprofile-standalone-android/examples/src/app/src/main/java/com/couchbase/userprofile/util/DatabaseManager.java) file and locate the `getCurrentUserDocId` method. This document Id is constructed by prefixing the term "user::" to the email Id of the user.  
```java  
public String getCurrentUserDocId() {  
    return "user::" + currentUser;  
}  
```
* Next, in the [**UserProfilePresenter.java**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/standalone/content/modules/userprofile-standalone-android/examples/src/app/src/main/java/com/couchbase/userprofile/profile/UserProfilePresenter.java) file, locate the `fetchProfile` method.  
```java  
public void fetchProfile()  
```

**Note**: The `fetchProfile` method is required by [**UserProfileContract.java**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/standalone/content/modules/userprofile-standalone-android/examples/src/app/src/main/java/com/couchbase/userprofile/profile/UserProfileContract.java), playing a key role in the MVP architecture previously mentioned.
* We try to fetch the `Document` with specified `userProfileDocId` from the database.  
```java  
String docId = DatabaseManager.getSharedInstance().getCurrentUserDocId();  
if (database != null) {  
    Map<String, Object> profile = new HashMap<>(); (1)  
    profile.put("email", DatabaseManager.getSharedInstance().currentUser); (2)  
    Document document = database.getDocument(docId); (3)  
    if (document != null) {  
        profile.put("name", document.getString("name")); (4)  
        profile.put("address", document.getString("address")); (4)  
        profile.put("imageData", document.getBlob("imageData")); (4)  
    }  
    mUserProfileView.showProfile(profile); (5)  
}  
```

| **1** | Create an instance of the [UserProfile](#userprofile) via Map<String,Object>.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Set the email property of the UserProfile with the email Id of the logged in user. This value is not editable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **3** | Fetch an **immutable** copy of the Document from the Database                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **4** | If the document exists and is fetched succesfully, we use appropriate type-getters to fetch the various members of the Document based on the property name. Specifically, note the support of the getBlob type to fetch the value of a property of type Blob                                                                                                                                                                                                                                                                                                                                                                                                              |
| **5** | Using the newly constructed [UserProfile](#userprofile) update the UI via the showProfile method (required by the interface [**UserProfileContract**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/standalone/content/modules/userprofile-standalone-android/examples/src/app/src/main/java/com/couchbase/userprofile/profile/UserProfileContract.java) which is implemented by [**UserProfileActivity**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/standalone/content/modules/userprofile-standalone-android/examples/src/app/src/main/java/com/couchbase/userprofile/profile/UserProfileActivity.java)). |

### [](#creating-updating-a-document)Creating / Updating a Document

A <<"User Profile" Document>> is created for the user when they tap the "Save" button on the "Profile Screen". The method below applies whether you are creating a document or updating an existing version.

* Open the [**UserProfilePresenter.java**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-android/tree/standalone/content/modules/userprofile-standalone-android/examples/src/app/src/main/java/com/couchbase/userprofile/profile/UserProfilePresenter.java) file and locate the `saveProfile` method.  
```java  
public void saveProfile(Map<String,Object> profile)  
```
* We create a **mutable** instance of the Document. By default, all APIs in Couchbase Lite deal with immutable objects, thereby making them **thread-safe** by design. In order to mutate an object, you must explicitly get a mutable copy of the object. Use appropriate type-setters to set the various properties of the Document.  
```java  
MutableDocument mutableDocument = new MutableDocument(docId, profile);  
```
* Save the document.  
```java  
database.save(mutableDocument);  
```

### [](#deleting-a-document)Deleting a Document

We don't delete a `Document` in this sample app. However, deletion of a document is pretty straightforward and this is how you would do it.

```java
var document = database.getDocument(id);

if (document != null) {
    database.delete(document);
}
```

### [](#try-it-out)Try It Out

* You should have followed the steps discussed in the "Try It Out" section under [Create and Open a Database](#create-and-open-a-database).
* Enter a "name" for the user in the Text Entry box and Tap "Save".
* Confirm that you see a "Successfully Updated Profile" toast message. The first time you update the profile screen, the `Document` will be created.  
![User Profile Document Creation](_images/doc_create.png)
* Now tap on the "Upload Photo" button and select an image from the Photo Album.  
![100](_images/image_selection.gif)
* Tap "Save"
* Confirm that you see the _toast_ message "Successfully Updated Profile". The `Document` will be updated this time.
* Tap "Log Out" and log out of the app
* Log back into the app with the same user credentials you used earlier. In my example, I used _"demo@example.com"_ and _"password"_.
* Confirm that you see the profile screen with the _name_ and _image_ values that you set earlier.  
![200](_images/log_off_on.gif)

## [](#learn-more)Learn More

Congratulations on completing this tutorial!

This tutorial walked you through a very basic example of how to get up and running with Couchbase Lite as a local-only, standalone embedded data store in your Android app. If you want to learn more about Couchbase Mobile, check out the following links.

Further Reading

* [Introduction to Couchbase Mobile](https://www.couchbase.com/products/mobile)
* [Couchbase Mobile Overview](https://blog.couchbase.com/couchbase-mobile-2-0/)
* [Couchbase Lite Reference Guide](https://docs.couchbase.com/couchbase-lite/current/introduction.html)
* [Couchbase Mobile Blogs](https://blog.couchbase.com/category/couchbase-mobile/)