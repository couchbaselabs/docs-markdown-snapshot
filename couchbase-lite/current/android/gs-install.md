---
title: Installing Couchbase Lite on Android
description: How to install Couchbase Lite on Android
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/android/pages/gs-install.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:couchbase-lite:android:gs-install.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/android/gs-install.html)

# Installing Couchbase Lite on Android

> Description — _How to install Couchbase Lite on Android_  
> _Abstract — Getting you up and running quickly with Couchbase Lite on android_  

## [](#introduction)Introduction

Couchbase Lite on Android supports the development of applications in Java or [Kotlin](kotlin.md).

You can install Couchbase Lite Community and-or Enterprise editions from the Maven repository. There are separate downloads for Kotlin and Java.

Enterprise users can also download the Couchbase Lite Vector Search extension library. Installation instructions are included in the step-by-step install guides for both Java and Kotlin.

Couchbase Lite Quick Steps

For experienced developers, this is all you need to add \_Couchbase Lite for Android 4.0.0 to your application projects.

Kotlin - Enterprise

1. Create a Kotlin Android app project in Android Studio
2. Add Couchbase Lite as a dependency in your app-level `build.gradle`  
`implementation 'com.couchbase.lite:couchbase-lite-android-ee-ktx:4.0.0'`
3. Add the following _maven_ repo to your repositories (in `build.gradle` or `settings.gradle` as required  
`<https://mobile.maven.couchbase.com/maven2/dev/>`

  1. If you want to use Vector Search, add the Couchbase Lite Vector Search dependency for architectures other than `x86_64`: `com.couchbase.lite:couchbase-lite-java-vector-search-arm64-2.0.0`

    1. For `x86_64` architectures: `com.couchbase.lite:couchbase-lite-android-vector-search-x86_64-2.0.0`
  2. You must then use `CouchbaseLite.enableVectorSearch();` to enable the vector search extension.
4. Build the project and it will pull Couchbase Lite down.

Kotlin - Community

1. Create a Kotlin Android app project in Android Studio
2. Add Couchbase Lite as a dependency in your app-level `build.gradle`  
`implementation 'com.couchbase.lite:couchbase-lite-android-ktx:4.0.0'`
3. Check you have `mavenCentral()` in `repositories` (or in `settings.gradle`)
4. Build the project and it will pull Couchbase Lite down.

Java - Enterprise

1. Create a Java Android app project in Android Studio
2. Add Couchbase Lite as a dependency in your app-level `build.gradle`  
`implementation 'com.couchbase.lite:couchbase-lite-android-ee:4.0.0'`
3. Add the following _maven_ repo to your repositories (in `build.gradle` or `settings.gradle` as required  
`<https://mobile.maven.couchbase.com/maven2/dev/>`

  1. If you want to use Vector Search, add the Couchbase Lite Vector Search dependency for architectures other than `x86_64`: `com.couchbase.lite:couchbase-lite-java-vector-search-arm64-2.0.0`

    1. For `x86_64` architectures: `com.couchbase.lite:couchbase-lite-android-vector-search-x86_64-2.0.0`
  2. You must then use `CouchbaseLite.enableVectorSearch();` to enable the vector search extension.
4. Build the project and it will pull Couchbase Lite down.

Java - Community

1. Create a Java Android app project in Android Studio
2. Add Couchbase Lite as a dependency in your app-level `build.gradle`  
`implementation 'com.couchbase.lite:couchbase-lite-android:4.0.0'`
3. Check you have `mavenCentral()` in `repositories` (or in `settings.gradle`)
4. Build the project and it will pull Couchbase Lite down.

That’s it! You''re all set to begin developing powerful Couchbase Lite applications.

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
  implementation 'com.couchbase.lite:couchbase-lite-android-ee-ktx:4.0.0'  
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
  implementation "com.couchbase.lite:couchbase-lite-android-ktx:4.0.0"  
//   ... other section content as required by user  
}  
```

## [](#kotlin-vector-search-extension-detailed-installation-instructions)Kotlin Vector Search Extension: Detailed Installation Instructions

You can get set up with the Vector Search Extension for Android (Kotlin) by following these instructions.

> [!NOTE]
> The Kotlin download also includes the Java version of Couchbase Lite for Android, along with the other dependencies.

Create or open an existing Android Studio project and include the following entries in the app-level `build.gradle` file (typically in the **app** folder).

> [!IMPORTANT]
> You must have Couchbase Lite installed before you can use the Vector Search Extension. Vector Search is available only for 64-bit architectures. The Vector Search extension is an **Enterprise-only** feature.

### [](#installing-the-vector-search-extension)Installing the Vector Search Extension

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
  google()  
  mavenCentral()  
//   ... other section content as required by user  
}  
```
3. For architectures other than x86\_64:  
```kotlin  
dependencies {  
  implementation 'com.couchbase.lite:couchbase-lite-android-ee-ktx:4.0.0'  
  // All standard 64-bit ARM architectures  
  implementation 'com.couchbase.lite:couchbase-lite-android-vector-search-arm64-2.0.0'  
//   ... other section content as required by user  
}  
```

  1. For x86\_64 architectures:  
  ```kotlin  
  dependencies {  
    implementation 'com.couchbase.lite:couchbase-lite-android-ee-ktx:4.0.0'  
    implementation 'com.couchbase.lite:couchbase-lite-android-vector-search-x86_64-2.0.0'  
  //   ... other section content as required by user  
  }  
  ```
4. To activate the extension, the snippet below is required:

```Kotlin
        try { CouchbaseLite.enableVectorSearch(); }
        catch (CouchbaseLiteException e) {
            throw new IllegalStateException("Could not enable vector search", e);
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
  implementation 'com.couchbase.lite:couchbase-lite-android-ee:4.0.0'  
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
  implementation 'com.couchbase.lite:couchbase-lite-android:4.0.0'  
//   ... other section content as required by user  
}  
```

## [](#java-vector-search-extension-detailed-installation-instructions)Java Vector Search Extension: Detailed Installation Instructions

> [!NOTE]
> The Vector Search extension is an **Enterprise-only** feature.

You can get set up with the Vector Search Extension for Android (Java) by following these instructions.

Create or open an existing _Android Studio_ project and install Couchbase Lite using the following method.

Include the following entries to the app-level `build.gradle` file (typically in the **app** folder).

### [](#installing-the-vector-search-extension-2)Installing the Vector Search Extension

> [!IMPORTANT]
> To use Vector Search, you must have Couchbase Lite installed and add the Vector Search extension to your Couchbase Lite application. Vector Search is available only for 64-bit architectures and Intel processors that support the Advanced Vector Extensions 2 (AVX2) instruction set. To verify whether your device supports the AVX2 instructions set, [follow these instructions.](https://www.intel.com/content/www/us/en/support/articles/000090473/processors/intel-core-processors.html)

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
  google()  
  mavenCentral()  
//   ... other section content as required by user  
}  
```
3. Include the following in the `dependencies{}` section:  
```kotlin  
dependencies {  
  implementation 'com.couchbase.lite:couchbase-lite-android-ee-ktx:4.0.0'  
  // All standard 64-bit ARM architectures  
  implementation 'com.couchbase.lite:couchbase-lite-android-vector-search-arm64-2.0.0'  
//   ... other section content as required by user  
}  
```

  1. For running on x86\_64 architectures, include the following in the `dependencies{}` section instead:  
  ```kotlin  
  dependencies {  
    implementation 'com.couchbase.lite:couchbase-lite-android-ee-ktx:4.0.0'  
    implementation 'com.couchbase.lite:couchbase-lite-android-vector-search-x86_64-1.0.0-2.0.0'  
  //   ... other section content as required by user  
  }  
  ```
4. To activate the extension, the snippet below is required:  
```java  
        try { CouchbaseLite.enableVectorSearch(); }  
        catch (CouchbaseLiteException e) {  
            throw new IllegalStateException("Could not enable vector search", e);  
        }  
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

.

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.