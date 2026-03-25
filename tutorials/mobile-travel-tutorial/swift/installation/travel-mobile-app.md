---
title: Travel Sample Mobile App
editUrl: https://github.com/couchbaselabs/mobile-travel-sample/edit/master/content/modules/mobile-travel-tutorial/pages/swift/installation/travel-mobile-app.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:tutorials:mobile-travel-tutorial:swift/installation/travel-mobile-app.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/mobile-travel-tutorial/swift/installation/travel-mobile-app.html)

# Travel Sample Mobile App

## [](#pre-requisites)Pre-requisites

* Xcode 12.5+: download the latest version from the [Mac App Store](https://itunes.apple.com/us/app/xcode/id497799835?mt=12).
* swift 5.5

## [](#getting-started)Getting Started

* Clone the "master" branch of the Travel Sample app from GitHub. We are doing a shallow pull with `depth` as 1 to speed the cloning process.  
```bash  
git clone -b master --depth 1 https://github.com/couchbaselabs/mobile-travel-sample.git  
```  
You will have to download the compatible version of Couchbase Lite xcframework
* In Terminal, navigate to the **TravelSample** directory.  
```bash  
cd /path/to/mobile-travel-sample/ios/TravelSample  
```
* Run the following script to download and install Couchbase Lite. Scripts are provided to install Couchbase Lite compatible with different versions of Xcode and Swift, here we use the version for Xcode 13.  
```bash  
sh install_13.sh  
```  
> [!NOTE]  
> If you choose to use Xcode12.3+, you may be impacted by an issue in Xcode while using linked frameworks. Please follow the instructions outlined [here](../../../../couchbase-lite/2.8/swift/gs-install.md) to workaround the issue.
* Open the `TravelSample.xcodeproj` using Xcode

## [](#configure-app-to-connect-to-backend)Configure App to connect to Backend

You will have to update the URLs specified in the app to connect to the backend If you haven’t done so already, complete the steps outlined in the "Backend Installation" to install your Couchbase Server, Sync Gateway and Python web backend app.

### [](#updating-the-web-backend-url)Updating the web backend URL

**Open the file** `QueryConsts.swift`. You must update the `webUrl` constant which points to the Python Web Server.

[QueryConsts.swift](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/ios/TravelSample/TravelSample/Utilities/QueryConsts.swift)

Now, the URLs that you specify will vary depending on the installation option that you chose for deploying your backend

* Manual
* Docker

```swift
static var webUrl:String = "http://localhost:8080"
```

```swift
static var webUrl:String = "http://127.0.0.1:8080/"
```

### [](#updating-the-sync-gateway-url)Updating the Sync Gateway URL

Next, you will update the Sync Gateway endpoint.

**Open the file** `DatabaseManager.swift`. You must update the `kRemoteSyncUrl` constant. Now, the URLs that you specify will vary depending on the installation option that you chose for deploying your backend

* Manual
* Docker

```swift
let kRemoteSyncUrl = "ws://localhost:4984"
```

```swift
let kRemoteSyncUrl = "ws://127.0.0.1:4984"
```

Try it Out

1. Build and run the project using simulator
2. Verify that the login screen appears in the simulator