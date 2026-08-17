---
title: Couchbase Lite on Java&#8201;&#8212;&#8201;Prerequisites
description: Couchbase Lite on Java -- a framework for developing offline-first
  Java applications for mobile and edge
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/java/pages/gs-prereqs.adoc
  xref: xref:3.0@couchbase-lite:java:gs-prereqs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/java/gs-prereqs.html)

# Couchbase Lite on Java&#8201;&#8212;&#8201;Prerequisites

> Description — _Couchbase Lite on Java — a framework for developing offline-first Java applications for mobile and edge_  
> _Abstract — This content identities the pre-requisites and preparatory steps to be considered before installing Couchbase Lite for java_  

## [](#introduction)Introduction

_Couchbase Lite_ on Java enables development and deployment of Couchbase Lite applications to a JVM environment. You can deploy to a desktop or web server (for example, Tomcat), including embedded Tomcat deployments.

> [!NOTE]
> We use _Intellij IDEA_, _gradle_, _Maven_ and _Tomcat_ as tools to build and run the examples presented in this content. You are free to use the tools of your choice.

## [](#bmkSetupSyncAndServer)Install Companion Software

If you want to use _Couchbase Lite_ on Java with _Couchbase Server_ and-or _Sync Gateway_ you will need to have installed operational instances of these before completing the installation and test build steps.

So, If you have not already done so, see [Prepare Sync Gateway](#sync-gateway::get-started-prepare.adoc)

* Within _Couchbase Server_, create a bucket named getting-started.cblite2
* Create a RBAC user for _Sync Gateway_ with username = `sync-gateway` and password = `password`

## [](#downloaded-binaries)Downloaded Binaries

### [](#package-contents)Package Contents

The download package contains a license file, jar libraries for the appropriate edition of the Couchbase Lite and a set of Linux _shared libraries_.

Get the download package from here — [Extend with Mobile](https://www.couchbase.com/downloads#extend-with-mobile).

* Community Edition — couchbase-lite-java-3.0.15
* Enterprise Edition — couchbase-lite-java-ee-3.0.15

When unpacked the package contains the following:

* A `lib` folder containing all necessary JAR files:

  * couchbase-lite-java-3.0.15 or for EE couchbase-lite-java-ee-3.0.15
  * okhttp-3.14.7.jar
  * okio-1.17.2.jar
* A `support` folder containing the Linux native libraries:  
> [!NOTE]  
> This means you do not need to download and-or build compatible versions of system libraries for the Linux platform of choice.

  * `libz` (requires zlib v.1.2.11+)
  * `libC++` requires libc++ v.3.6.0+)
  * `libicu` (requires ICU4C v.5.4.1+)

### [](#steps)Steps

1. Download the _zip_ file from here — [Extend with Mobile](https://www.couchbase.com/downloads#extend-with-mobile).
2. Unpack the downloaded file to a location accessible to — and usable by — your chosen **build** environment.  
We'll refer to that location — `<your dir>/couchbase-lite-java-3.0.15` — as the `<pathToCbl>`.
3. Include the following dependency in your `build.gradle` file, you can remove any Couchbase Lite Maven references:  
```Java  
Dependencies {  
  implementation fileTree(include: ['*.jar'], dir: <pathToCbl>/lib>  
}  
```

Where <pathToCbl> is the location of the downloaded Couchbase Lite library.

Sample build gradle

```Java

```

## [](#using-native-libraries-for-linux)Using Native Libraries for Linux

Additional Steps for Linux

In addition to setting-up your build environment, you also need to make the supplied support libraries available:

> [!NOTE]
> These libraries are provided only in the `.zip` distributable.

* Web Service/Tomcat
* Desktop

1. Copy the directory `<exploded-distribution-zip>/support` to a location accessible and executable by your build and runtime environments.  
Unresolved include directive in modules/java/pages/\_partials/gs-additional-steps-for-linux.adoc - include::partial$directory-diagrams.adoc\[\]
2. Add the paths of the directories `libc++` and `libicu` to `LD_LIBRARY_PATH` in \`$CATALINA\_BASE/bin/setenv.sh. (If the setenv.sh file doesn't exist, you will need to create a new file.)  
```bashrc  
LD_LIBRARY_PATH=<lib-directory>/support/libc++:<lib-directory>/support/libicu:$LD_LIBRARY_PATH  
```

1. Copy the directory `<exploded-distribution-zip>/support` to a location accessible and executable by your build and runtime environments.  
Unresolved include directive in modules/java/pages/\_partials/gs-additional-steps-for-linux.adoc - include::partial$directory-diagrams.adoc\[\]
2. Add the paths of the directories `<lib-directory>/support/libc++` and `<lib-directory>/support/libicu` to `LD_LIBRARY_PATH` in the .bashrc file:  
```bashrc  
export LD_LIBRARY_PATH=<lib-directory>/support/libc++:<lib-directory>/support/libicu:$LD_LIBRARY_PATH  
```

Please refer to the Linux Platform Support section for the minimum version requirements of those libraries.

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