---
title: Couchbase Scala SDK Installation
description: Installation instructions for the Couchbase Scala Client.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-scala/edit/temp/1.6/modules/project-docs/pages/sdk-full-installation.adoc
  xref: xref:1.6@scala-sdk:project-docs:sdk-full-installation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/1.6/project-docs/sdk-full-installation.html)

# Couchbase Scala SDK Installation

> Installation instructions for the Couchbase Scala Client. 

This page gives full installation instructions for the Scala SDK. In most cases, the [Quickstart Guide](../hello-world/start-using-sdk.md) should be enough to get you up and running if you're in a hurry.

## [](#prerequisites)Prerequisites

The Scala SDK is tested against LTS versions of Oracle JDK and OpenJDK — see our [compatibility docs](compatibility.md#jdk-compat). The underlying OS normally makes no difference, but library incompatibilities in Alpine Linux makes a [workaround](compatibility.md#alpine-linux-compatibility) necessary for this OS.

## [](#installing-the-sdk)Installing the SDK

The Couchbase Scala SDK is available on the Maven repository, packaged for Scala 2.12 and 2.13.

### [](#with-sbt-projects)With SBT Projects

It can be included in your SBT build like this:

```sbt
libraryDependencies += "com.couchbase.client" %% "scala-client" % "1.6.2"
```

This will automatically use the Scala 2.12 or 2.13 builds, as appropriate for your SBT project.

### [](#with-gradle-projects)With Gradle Projects

It can be included in your `build.gradle` like this for 2.12:

```groovy
dependencies {
    compile group: 'com.couchbase.client', name: 'scala-client_2.12', version: '1.6.2'
}
```

or 2.13:

```groovy
dependencies {
    compile group: 'com.couchbase.client', name: 'scala-client_2.13', version: '1.6.2'
}
```

### [](#with-maven-projects)With Maven Projects

It can be included in your Maven `pom.xml` like this for 2.12:

```xml
<dependencies>
    <dependency>
        <groupId>com.couchbase.client</groupId>
        <artifactId>scala-client_2.12</artifactId>
        <version>1.6.2</version>
    </dependency>
</dependencies>
```

or 2.13:

```xml
<dependencies>
    <dependency>
        <groupId>com.couchbase.client</groupId>
        <artifactId>scala-client_2.13</artifactId>
        <version>1.6.2</version>
    </dependency>
</dependencies>
```

## [](#using-a-snapshot-version)Using a Snapshot Version

Couchbase publishes pre-release snapshot artifacts to the Sonatype OSS Snapshot Repository. If you wish to use a snapshot version, you'll need to tell your build tool about this repository.

* Maven
* Gradle (Groovy)

`**pom.xml**`

```xml
<repositories>
  <repository>
    <id>sonatype-snapshots</id>
    <url>https://oss.sonatype.org/content/repositories/snapshots</url>
    <releases><enabled>false</enabled></releases>
    <snapshots><enabled>true</enabled></snapshots>
  </repository>
</repositories>
```

`**build.gradle**`

```groovy
repositories {
    mavenCentral()
    maven {
        url "https://oss.sonatype.org/content/repositories/snapshots"
        mavenContent { snapshotsOnly() }
    }
}
```