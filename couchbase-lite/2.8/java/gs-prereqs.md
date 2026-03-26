---
title: Couchbase Lite on Java&#8201;&#8212;&#8201;Prerequisites
description: Couchbase Lite on Java -- a framework for developing offline-first
  Java applications for mobile and edge
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/java/pages/gs-prereqs.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@couchbase-lite:java:gs-prereqs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/java/gs-prereqs.html)

# Couchbase Lite on Java&#8201;&#8212;&#8201;Prerequisites

> Description — _Couchbase Lite on Java — a framework for developing offline-first Java applications for mobile and edge_  
> _Abstract — This content identities the pre-requisites and preparatory steps to be considered before installing Couchbase Lite for java_  

## [](#introduction)Introduction

Couchbase Lite on Java enables development and deployment of Couchbase Lite applications to a JVM environment. You can deploy to a desktop or web server (for example, Tomcat), including embedded Tomcat deployments.

> [!NOTE]
> We use _Intellij IDEA_, _gradle_, _Maven_ and _Tomcat_ as tools to build and run the examples presented in this content. You are free to use the tools of your choice.

## [](#preparatory-steps-for-installation-and-use)Preparatory Steps for Installation and Use

### [](#install-companion-software)Install Companion Software

If you want to use Couchbase Lite on Java with Couchbase Server and-or Sync Gateway you will need to have installed operational instances of these before completing the installation and test build steps.

So, If you have not already done so:

Install _Couchbase Server_ and _Sync Gateway_ for instructions — see [Install](../../current/java/gs-install.md)

For supported versions — see: [Compatibility](../../current/java/compatibility.md) | [Supported OS](../../current/java/supported-os.md)

### [](#prepare-couchbase-server-and-sync-gateway-for-the-test-build)Prepare Couchbase Server and Sync Gateway for the Test Build

1. Within Couchbase Server, create a bucket named getting-started.cblite2  
For instructions — see: [Create a Bucket](#sync-gateway::get-started-prepare&.adoc#8212;​page.adoc#lbl-create-bucket)
2. Create a RBAC user for Sync Gateway  
For instructions — see: [Create an RBAC User](#sync-gateway::get-started-prepare&.adoc#8212;​page.adoc#lbl-create-rbac-user)

  * Set username to `sync-gateway`
  * Set password to `password`

## [](#how-to-use-downloaded-binaries)How to Use Downloaded Binaries

**Package Contents**

The download package contains a license file, jar libraries for the appropriate edition of the Couchbase Lite and a set of Linux _shared libraries_.

Get the download package from the [Couchbase Downloads](https://www.couchbase.com/downloads?family=mobile) page.

* Community Edition — couchbase-lite-java-2.8.3
* Enterprise Edition — couchbase-lite-java-ee-2.8.3

When unpacked the package contains the following:

* A `lib` folder containing all necessary JAR files:

  * couchbase-lite-java-2.8.3 or for EE couchbase-lite-java-ee-2.8.3
  * okhttp-3.14.7.jar
  * okio-1.17.2.jar
* A `support` folder containing the Linux native libraries:  
> [!NOTE]  
> This means you do not need to download and-or build compatible versions of system libraries for the Linux platform of choice.

  * `libz` (requires zlib v.1.2.11+)
  * `libC++` requires libc++ v.3.6.0+)
  * `libicu` (requires ICU4C v.5.4.1+)

**Steps**

1. Download the _zip_ file from the [Couchbase Downloads](https://www.couchbase.com/downloads?family=mobile) page.
2. Unpack the downloaded file to a location accessible to — and usable by — your chosen **build** environment.  
We'll refer to that location — `<your dir>/couchbase-lite-java-2.8.3` — as the `<pathToCbl>`.
3. Include the following dependency in your `build.gradle` file, you can remove any Couchbase Lite Maven references:  
```Java  
Dependencies {  
  implementation fileTree(include: ['*.jar'], dir: <pathToCbl>/lib>  
}  
```

Where <pathToCbl> is the location of the downloaded Couchbase Lite library.

Sample build gradle

```Java
apply plugin: 'java'
apply plugin: 'jar'
// apply plugin: 'war'
sourceCompatibility = 1.8
repositories {
  jcenter()
}
dependencies {
    implementation fileTree(dir: 'libs', include: '*.jar')
    compileOnly "javax.servlet:javax.servlet-api:4.0.1"
}
```

## [](#using-native-libraries-for-linux)Using Native Libraries for Linux

In addition to setting-up your build environment, you also need to make the supplied native libraries (`<pathToCbl/support`) available:

> [!NOTE]
> These libraries are provided only in the `.zip` distributable.

Web Service/Tomcat

1. Copy the _native libraries_ (`<pathToCbl>/support`) to a location accessible to — and usable by — your build and runtime environments.
2. Add the following libraries to the `LD_LIBRARY_PATH` in \`$CATALINA\_BASE/bin/setenv.sh:  
> [!NOTE]  
> If the setenv.sh file doesn't exist, you will need to create a new file.  
```bashrc  
LD_LIBRARY_PATH=<pathToCbl>/support/linux/x86_64/:$LD_LIBRARY_PATH  
```

Desktop

1. Copy the _native libraries_ (`<pathToCbl>/support`) to a location accessible to — and usable by — your build and runtime environments.
2. Add the following libraries to the `LD_LIBRARY_PATH` in the .bashrc file:  
```bashrc  
export LD_LIBRARY_PATH=<pathToCbl>/support/linux/x86_64/:$LD_LIBRARY_PATH  
```

Please refer to the Linux Platform Support section for the mini mum version requirements of those libraries.

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](../../current/java/gs-prereqs.md)
* [Install](../../current/java/gs-install.md)
* [Build and Run](../../current/java/gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](../../current/java/database.md)
* [Documents](../../current/java/document.md)
* [Blobs](../../current/java/blob.md)
* [Remote Sync using Sync Gateway](../../current/java/replication.md)
* [Handling Data Conflicts](../../current/java/conflict.md)

###### [](#-3)

Dive Deeper . . .

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)