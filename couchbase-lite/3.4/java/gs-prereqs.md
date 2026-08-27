---
title: Couchbase Lite on Java&#8201;&#8212;&#8201;Prerequisites
description: Couchbase Lite on Java -- a framework for developing offline-first
  Java applications for mobile and edge
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.4/modules/java/pages/gs-prereqs.adoc
  xref: xref:3.4@couchbase-lite:java:gs-prereqs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.4/java/gs-prereqs.html)

# Couchbase Lite on Java&#8201;&#8212;&#8201;Prerequisites

> Description — _Couchbase Lite on Java — a framework for developing offline-first Java applications for mobile and edge_  
> _Abstract — This content identities the pre-requisites and preparatory steps to be considered before installing Couchbase Lite for java_  

> [!IMPORTANT]
> Vector Search Prerequisites
> 
> To use Vector Search, you must have Couchbase Lite installed and add the Vector Search extension to your Couchbase Lite application. Vector Search is available only for 64-bit architectures and Intel processors that support the Advanced Vector Extensions 2 (AVX2) instruction set. To verify whether your device supports the AVX2 instructions set, [follow these instructions.](https://www.intel.com/content/www/us/en/support/articles/000090473/processors/intel-core-processors.html)

## [](#introduction)Introduction

Couchbase Lite enables development and deployment of Couchbase Lite applications to a JVM environment. You can deploy to a desktop or web server (for example, Tomcat), including embedded Tomcat deployments.

> [!NOTE]
> We use _Intellij IDEA_, _gradle_, _Maven_ and _Tomcat_ as tools to build and run the examples presented in this content. You are free to use the tools of your choice.

## [](#bmkSetupSyncAndServer)Install Server Software

If you want to use Couchbase Lite with _Couchbase Server_ and-or \_Sync Gateway you will need to have installed operational instances of these before completing the installation and test build steps.

So, If you have not already done so, see [Prepare Sync Gateway](#sync-gateway::get-started-prepare.adoc)

* Within _Couchbase Server_, create a bucket named getting-started.cblite2
* Create a RBAC user for \_Sync Gateway with username = `sync-gateway` and password = `password`

## [](#macos-and-windows)MacOS and Windows

You may now proceed directly to [Couchbase Lite on Java — Installing](gs-install.md).

## [](#additional-steps-for-linux)Additional Steps For Linux

Before proceeding to [Couchbase Lite on Java — Installing](gs-install.md), you will need to make the supplied support libraries available to your running application.

### [](#steps)Steps

1. Download the _zip_ file from here — <https://packages.couchbase.com/releases/couchbase-lite-java/3.4.0/couchbase-lite-java-linux-supportlibs-3.4.0.zip>.
2. Unpack the downloaded file to a location accessible to your build and runtime environments, for example `your_dir/couchbase-lite-java-3.4.0`.

1. Set up the Native Libraries for Linux. You will need to add the path of the directory containing the unpacked support libraries to the value of the Java system property `java.library.path`.  
The simplest way to set this is through the shell variable `LD_LIBRARY_PATH`:  
```bash  
export LD_LIBRARY_PATH=<your_dir>/couchbase-lite-java-3.4.0/:$LD_LIBRARY_PATH  
```  
Where `<your_dir>` is the path where you unpacked the support libraries in step 2.  
> [!NOTE]  
> This environment variable must be set before running your Java application that uses Couchbase Lite.

* Web Service/Tomcat
* Desktop

Add the variables to your `$CATALINA_BASE/bin/setenv.sh`. (If the setenv.sh file doesn't exist, you will need to create a new file.)

LD\_LIBRARY\_PATH="$LD\_LIBRARY\_PATH:" 

Export the variable in your .bashrc file:

export LD\_LIBRARY\_PATH="$LD\_LIBRARY\_PATH:" 

Please refer to the Linux Platform Support section for the minimum version requirements of those libraries.

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