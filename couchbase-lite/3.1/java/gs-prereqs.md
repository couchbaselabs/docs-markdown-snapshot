---
title: Couchbase Lite on Java&#8201;&#8212;&#8201;Prerequisites
description: Couchbase Lite on Java -- a framework for developing offline-first
  Java applications for mobile and edge
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.1/modules/java/pages/gs-prereqs.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.1@couchbase-lite:java:gs-prereqs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.1/java/gs-prereqs.html)

# Couchbase Lite on Java&#8201;&#8212;&#8201;Prerequisites

> Description — _Couchbase Lite on Java — a framework for developing offline-first Java applications for mobile and edge_  
> _Abstract — This content identities the pre-requisites and preparatory steps to be considered before installing Couchbase Lite for java_  

## [](#introduction)Introduction

_Couchbase Lite_ on Java enables development and deployment of Couchbase Lite applications to a JVM environment. You can deploy to a desktop or web server (for example, Tomcat), including embedded Tomcat deployments.

> [!NOTE]
> We use _Intellij IDEA_, _gradle_, _Maven_ and _Tomcat_ as tools to build and run the examples presented in this content. You are free to use the tools of your choice.

## [](#bmkSetupSyncAndServer)Install Server Software

If you want to use _Couchbase Lite_ on Java with _Couchbase Server_ and-or _Sync Gateway_ you will need to have installed operational instances of these before completing the installation and test build steps.

So, If you have not already done so, see [Prepare Sync Gateway](#sync-gateway::get-started-prepare.adoc)

* Within _Couchbase Server_, create a bucket named getting-started.cblite2
* Create a RBAC user for _Sync Gateway_ with username = `sync-gateway` and password = `password`

## [](#macos-and-windows)MacOS and Windows

You may now proceed directly to [Couchbase Lite on Java — Installing](gs-install.md).

## [](#additional-steps-for-linux)Additional Steps For Linux

Before proceeding to [Couchbase Lite on Java — Installing](gs-install.md), you will need to make the supplied support libraries available to your running application.

### [](#steps)Steps

1. Download the _zip_ file from here — <https://packages.couchbase.com/releases/couchbase-lite-java/3.1.11/couchbase-lite-java-linux-supportlibs-3.1.11.zip>.
2. Unpack the downloaded file to a location accessible to your build and runtime environments, for example `your_dir/couchbase-lite-java-3.1.11`.

1. Set up the Native Libraries for Linux. You will need to add the path of the directory `<lib-directory>` to the value of the Java system property `java.library.path`.

Normally, the simplest way to set this is through the shell variable `LD_LIBRARY_PATH`.

* Web Service/Tomcat
* Desktop

Add the variables to your `$CATALINA_BASE/bin/setenv.sh`. (If the setenv.sh file doesn’t exist, you will need to create a new file.)

```bashrc
LD_LIBRARY_PATH=<lib-directory>/support/libC++:<lib-directory>/support/libicu:$LD_LIBRARY_PATH
```

Export the variable in your .bashrc file:

```bashrc
export LD_LIBRARY_PATH=<lib-directory>/support/libC++:<lib-directory>/support/libicu:$LD_LIBRARY_PATH
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