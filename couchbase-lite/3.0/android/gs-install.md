---
title: Installing Couchbase Lite on Android
description: How to install Couchbase Lite on Android
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/android/pages/gs-install.adoc
  xref: xref:3.0@couchbase-lite:android:gs-install.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/android/gs-install.html)

# Installing Couchbase Lite on Android

> Description — _How to install Couchbase Lite on Android_  
> _Abstract — Getting you up and running quickly with Couchbase Lite on android_  

## [](#introduction)Introduction

Couchbase Lite on Android supports the development of applications in Java or [Kotlin](kotlin.md).

You can install Couchbase Lite Community and-or Enterprise editions from the Maven repository. There are separate downloads for Kotlin and Java.

Quick Steps

For experienced developers, this is all you need to add _Couchbase Lite for Android 3.0.15_ to your application projects.

Kotlin - Enterprise

1. Create a Kotlin Android app project in Android Studio
2. Add Couchbase Lite as a dependency in your app-level `build.gradle`  
`implementation 'com.couchbase.lite:couchbase-lite-android-ee-ktx:3.0.15'`
3. Add the following _maven_ repo to your repositories (in `build.gradle` or `settings.gradle` as required  
`<https://mobile.maven.couchbase.com/maven2/dev/>`
4. Build the project and it will pull Couchbase Lite down.

Kotlin - Community

1. Create a Kotlin Android app project in Android Studio
2. Add Couchbase Lite as a dependency in your app-level `build.gradle`  
`implementation 'com.couchbase.lite:couchbase-lite-android-ktx:3.0.15'`
3. Check you have `mavenCentral()` in `repositories` (or in `settings.gradle`)
4. Build the project and it will pull Couchbase Lite down.

Java - Enterprise

1. Create a Java Android app project in Android Studio
2. Add Couchbase Lite as a dependency in your app-level `build.gradle`  
`implementation 'com.couchbase.lite:couchbase-lite-android-ee:3.0.15'`
3. Add the following _maven_ repo to your repositories (in `build.gradle` or `settings.gradle` as required  
`<https://mobile.maven.couchbase.com/maven2/dev/>`
4. Build the project and it will pull Couchbase Lite down.

Java - Community

1. Create a Java Android app project in Android Studio
2. Add Couchbase Lite as a dependency in your app-level `build.gradle`  
`implementation 'com.couchbase.lite:couchbase-lite-android:3.0.15'`
3. Check you have `mavenCentral()` in `repositories` (or in `settings.gradle`)
4. Build the project and it will pull Couchbase Lite down.

That's it! You''re all set to begin developing powerful Couchbase Lite applications.

Now, try the [Getting Started](gs-build.md) application, which demonstrates use of key CRUD functionality.

## [](#kotlin-step-by-step-install)Kotlin - Step-by-Step Install

More detailed instructions on getting up and running with Couchbase Lite for Android (Kotlin).

> [!NOTE]
> The Kotlin download also includes the Java version of Couchbase Lite for Android, along with the other dependencies.

Create or open an existing Android Studio project and include the following entries in the app-level `build.gradle` file (typically in the **app** folder).

* Enterprise Edition
* Community Edition

1. Include the following in the `android {}` section:  
```groovy  
android {  
// Required only if your project has some Kotlin source code  
  kotlinOptions { jvmTarget = 1.8}  
  compileOptions {  
      targetCompatibility 1.8  
      sourceCompatibility 1.8  
  }  
//   ... other section content as required by user  
}  
```
2. Include the following in the `repositories {}` section:  
```groovy  
repositories {  
  maven { url 'https://mobile.maven.couchbase.com/maven2/dev/' }  
//   ... other section content as required by user  
}  
```
3. Include the following in the `dependencies{}` section:  
```kotlin  
dependencies {  
  implementation 'com.couchbase.lite:couchbase-lite-android-ee-ktx:3.0.15'  
//   ... other section content as required by user  
}  
```

1. Set the Java Version, include the following in the `android {}` section:  
```kotlin  
android {  
  compileOptions {  
      sourceCompatibility JavaVersion.VERSION_1_8  
      targetCompatibility JavaVersion.VERSION_1_8  
  }  
//   ... other section content as required by user  
}  
```
2. Ensure your `repositories` section includes `mavencentral()`  
```kotlin  
repositories {  
  mavenCentral()  
  //   ... other section content as required by user  
}  
```
3. Add _Couchbase Lite_ to the `dependencies{}` section:  
```kotlin  
dependencies {  
  implementation "com.couchbase.lite:couchbase-lite-android-ktx:3.0.15"  
//   ... other section content as required by user  
}  
```

## [](#java-step-by-step-install)Java - Step-by-step Install

More detailed instructions on getting up and running with Couchbase Lite for Android (Java).

Create or open an existing _Android Studio_ project and install Couchbase Lite using the following method.

Include the following entries to the app-level `build.gradle` file (typically in the **app** folder).

* Enterprise
* Community

1. Set the Java Version, include the following in the `android {}` section:  
```groovy  
android {  
// Required only if your project has some Kotlin source code  
  kotlinOptions { jvmTarget = 1.8}  
  compileOptions {  
      targetCompatibility 1.8  
      sourceCompatibility 1.8  
  }  
//   ... other section content as required by user  
}  
```
2. Add the following in the `repositories {}` section:  
```groovy  
repositories {  
  maven { url 'https://mobile.maven.couchbase.com/maven2/dev/' }  
//   ... other section content as required by user  
}  
```
3. Add _Couchbase Lite_ to your `dependencies{}` section:  
```groovy  
dependencies {  
  implementation 'com.couchbase.lite:couchbase-lite-android-ee:3.0.15'  
//   ... other section content as required by user  
}  
```

1. Include the following in the `android {}` section:  
```groovy  
android {  
// Required only if your project has some Kotlin source code  
  kotlinOptions { jvmTarget = 1.8 }  
  compileOptions {  
      targetCompatibility 1.8  
      sourceCompatibility 1.8  
  }  
//   ... other section content as required by user  
}  
```
2. Ensure your `repositories` section includes `mavencentral()`  
```groovy  
repositories {  
  mavenCentral()  
  //   ... other section content as required by user  
}  
```
3. Include the following in the `dependencies{}` section:  
```groovy  
dependencies {  
  implementation 'com.couchbase.lite:couchbase-lite-android:3.0.15'  
//   ... other section content as required by user  
}  
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)