---
title: Travel Mobile App
editUrl: https://github.com/couchbaselabs/mobile-travel-sample/edit/master/content/modules/mobile-travel-tutorial/pages/android/installation/travel-mobile-app.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:tutorials:mobile-travel-tutorial:android/installation/travel-mobile-app.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/mobile-travel-tutorial/android/installation/travel-mobile-app.html)

# Travel Mobile App

## [](#pre-requisites)Pre-requisites

* Latest version of Android Studio downloadable from [Google Developer site](https://developer.android.com)
* Android device or emulator running API level 22 or above
* Android SDK 29
* Android Build Tools 29+
* JDK 8

**Windows Users**: If you are developing on Windows, you must use a Windows 10 machine. Also, note that if you choose the Manual or Docker installation mode, you must also have **administrative privileges on the Windows box** so you can authorize the installation and running of the required executables.

## [](#travel-sample-mobile-app)Travel Sample Mobile App

* Clone the "master" branch of the Travel Sample app from GitHub. We are doing a shallow pull with `depth` as 1 to speed the cloning process.  
```bash  
git clone -b master --depth 1 https://github.com/couchbaselabs/mobile-travel-sample.git  
```
* Open the project using Android Studio. The **build.gradle** is located in /path/to/mobile-travel-sample/android/TravelSample/ folder/directory.

## [](#configure-app-to-connect-to-backend)Configure App to connect to Backend

You will have to update the URLs specified in the app to connect to the backend If you haven’t done so already, complete the steps outlined in the "Backend Installation" to install your Couchbase Server, Sync Gateway and Python web backend app.

### [](#updating-the-web-backend-url)Updating the web backend URL

**Open the file** `DatabaseManager.java` in util folder. You must update the `APPLICATION_ENDPOINT` constant which points to the Python Web Server.

Now, the URLs that you specify will vary depending on the installation option that you chose for deploying your backend

* Manual
* Docker

```java
public static String APPLICATION_ENDPOINT = "http://10.0.2.2:8080/api/";
```

```java
public static String APPLICATION_ENDPOINT = "http://10.0.2.2:8080/api/";
```

### [](#updating-the-sync-gateway-url)Updating the Sync Gateway URL

Next, you will update the Sync Gateway endpoint.

**Open the file** `DatabaseManager.java` in util folder You must update the `SGW_ENDPOINT` constant.

Now, the URLs that you specify will vary depending on the installation option that you chose for deploying your backend

* Manual
* Docker

```java
    public static String SGW_ENDPOINT = "ws://10.0.2.2:4984/travel-sample";
```

```java
    public static String SGW_ENDPOINT = "ws://10.0.2.2:4984/travel-sample";
```

Try it Out

1. Build and run the project using Android emulator.  
![android as build](../../_images/android-as-build.png)
2. Verify that the login screen appears in the emulator.  
![android login](../../_images/android-login.png)