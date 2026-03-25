---
title: Installing Couchbase Lite on Android
description: How to install Couchbase Lite on Android
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/android/pages/gs-install.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@couchbase-lite:android:gs-install.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/android/gs-install.html)

# Installing Couchbase Lite on Android

> Description — _How to install Couchbase Lite on Android_  
> _Abstract — Getting you up and running quickly with Couchbase Lite on java-android_  

Create or open an existing Android Studio project and install Couchbase Lite using the following method.

Make the following additions to the module-level `build.gradle` file (typically in the **app** folder). **Note:** In the gradle examples replace the `$2.8` token with the required Couchbase Lite version number.

* Community
* Enterprise

1. Include the following in the `android {}` section:  
```groovy  
android {  
    // Required only if your project has some Kotlin source code  
    kotlinOptions { jvmTarget = '1.8' }  
    // Set minimum JVM level to ensure availability of, for example, lambda expressions  
    compileOptions {  
        targetCompatibility 1.8  
        sourceCompatibility 1.8  
    }  
//   ... other section content as required by user  
}  
```
2. Include the following in the `dependencies{}` section:  
```groovy  
dependencies {  
    implementation "com.couchbase.lite:couchbase-lite-android:${version}"  
//   ... other section content as required by user  
}  
```

1. Include the following in the `android {}` section:  
```groovy  
android {  
    // Required only if your project has some Kotlin source code  
    kotlinOptions { jvmTarget = '1.8' }  
    // Set minimum JVM level to ensure availability of, for example, lambda expressions  
    compileOptions {  
        targetCompatibility 1.8  
        sourceCompatibility 1.8  
    }  
//   ... other section content as required by user  
}  
```
2. Include the following in the `dependencies{}` section:  
```groovy  
dependencies {  
    implementation "com.couchbase.lite:couchbase-lite-android-ee:${version}"  
//   ... other section content as required by user  
}  
```
3. Include the following in the `repositories {}` section:  
```groovy  
repositories {  
    maven { url 'https://mobile.maven.couchbase.com/maven2/dev/' }  
    google()  
    jcenter()  
//   ... other section content as required by user  
}  
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](../../current/android/gs-prereqs.md)
* [Install](../../current/android/gs-install.md)
* [Build and Run](../../current/android/gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](../../current/android/database.md)
* [Documents](../../current/android/document.md)
* [Blobs](../../current/android/blob.md)
* [Remote Sync using Sync Gateway](../../current/android/replication.md)
* [Handling Data Conflicts](../../current/android/conflict.md)

###### [](#-3)

Dive Deeper . . .

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)