---
title: Couchbase Scala SDK Installation
description: Installation instructions for the Couchbase Scala Client.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.11/modules/project-docs/pages/sdk-full-installation.adoc
pubDate: 2026-06-12T16:31:57.907Z
link: xref:scala-sdk:project-docs:sdk-full-installation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/current/project-docs/sdk-full-installation.html)

# Couchbase Scala SDK Installation

> Installation instructions for the Couchbase Scala Client. 

This page gives full installation instructions for the Scala SDK. In most cases, the [Quickstart Guide](../hello-world/start-using-sdk.md) should be enough to get you up and running if you're in a hurry.

## [](#prerequisites)Prerequisites

The Scala SDK is tested against LTS versions of Oracle JDK and OpenJDK — see our [compatibility docs](compatibility.md#jdk-compat). The underlying OS normally makes no difference, but library incompatibilities in Alpine Linux makes a [workaround](compatibility.md#alpine-linux-compatibility) necessary for this OS.

The Couchbase Scala SDK 3.9 Client supports Scala 2.12, 2.13, and 3.3 through 3.7 (inclusive).

## [](#installing-the-sdk)Installing the SDK

The Couchbase Scala SDK is available on the Maven repository, packaged for Scala 2.12, 2.13, and 3.

### [](#with-sbt-projects)With SBT Projects

It can be included in your SBT build like this:

```sbt
libraryDependencies += "com.couchbase.client" %% "scala-client" % "3.11.3"
```

This will automatically use the correct build for your Scala version.

### [](#with-gradle-projects)With Gradle Projects

It can be included in your `build.gradle` like this for 2.12:

```groovy
dependencies {
    compile group: 'com.couchbase.client', name: 'scala-client_2.12', version: '3.11.3'
}
```

or 2.13 or 3.3 through 3.7:

```groovy
dependencies {
    compile group: 'com.couchbase.client', name: 'scala-client_3', version: '3.11.3'
}
```

There is a dedicated 2.13 build too, but from the 3.9.0 release we recommended 2.13 users use the 3.x build instead. If the 2.13 build is explicitly desired, it can be included like this:

```groovy
dependencies {
    compile group: 'com.couchbase.client', name: 'scala-client_2.13', version: '3.11.3'
}
```

### [](#with-maven-projects)With Maven Projects

It can be included in your Maven `pom.xml` like this for 2.12:

```xml
<dependencies>
    <dependency>
        <groupId>com.couchbase.client</groupId>
        <artifactId>scala-client_2.12</artifactId>
        <version>3.11.3</version>
    </dependency>
</dependencies>
```

or 2.13 or 3.3 through 3.7:

```xml
<dependencies>
    <dependency>
        <groupId>com.couchbase.client</groupId>
        <artifactId>scala-client_3</artifactId>
        <version>3.11.3</version>
    </dependency>
</dependencies>
```

There is a dedicated 2.13 build too, but from the 3.9.0 release we recommended 2.13 users use the 3.x build instead. If the 2.13 build is explicitly desired, it can be included like this:

```xml
<dependencies>
    <dependency>
        <groupId>com.couchbase.client</groupId>
        <artifactId>scala-client_2.13</artifactId>
        <version>3.11.3</version>
    </dependency>
</dependencies>
```

## [](#using-a-snapshot-version)Using a Snapshot Version

Couchbase publishes pre-release snapshot artifacts to the Central Portal Snapshots Repository. If you wish to use a snapshot version, you'll need to tell your build tool about this repository.

* Maven
* Gradle (Groovy)

`**pom.xml**`

```xml
<repositories>
    <repository>
        <name>Central Portal Snapshots</name>
        <id>central-portal-snapshots</id>
        <url>https://central.sonatype.com/repository/maven-snapshots/</url>
        <releases>
            <enabled>false</enabled>
        </releases>
        <snapshots>
            <enabled>true</enabled>
        </snapshots>
    </repository>
</repositories>
```

`**build.gradle**`

```groovy
repositories {
    mavenCentral()
    maven {
        url "https://central.sonatype.com/repository/maven-snapshots/"
        mavenContent { snapshotsOnly() }
    }
}
```

## [](#further-reading)Further Reading

For those who spend little or no time using Scala, but have to evaluate the platform, further installation and background help is available on the [Scala Platform Introduction page](../hello-world/platform-help.md).