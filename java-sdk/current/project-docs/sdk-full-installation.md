---
title: Full Installation
description: Installation instructions for the Couchbase Java Client.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.11/modules/project-docs/pages/sdk-full-installation.adoc
pubDate: 2026-04-17T05:26:26.225Z
link: xref:java-sdk:project-docs:sdk-full-installation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/current/project-docs/sdk-full-installation.html)

# Full Installation

> Installation instructions for the Couchbase Java Client. 

The Couchbase Java SDK allows Java applications to access a Couchbase cluster. It offers synchronous APIs as well as reactive and asynchronous equivalents to maximize flexibility and performance.

The Couchbase Java SDK 3._x_ is a complete rewrite of the 2.x API, providing a simpler surface area and adding support for Couchbase Server features like [Collections and Scopes](../concept-docs/collections.md) (available in Couchbase Server 7.0+). The (reactive) API also migrated from `RxJava` to `Reactor`, along with other improvements to performance, logging, debugging and timeout troubleshooting. If you're upgrading your application from Java SDK 2.x, please read our [Migrating 2.x code to SDK 3.0 Guide](migrating-sdk-code-to-3.n.md).

## [](#prerequisites)Prerequisites

The Java SDK is tested against LTS versions of Oracle JDK and OpenJDK — see our [compatibility docs](compatibility.md#jdk-compat). The underlying OS normally makes no difference, but library incompatibilities in Alpine Linux makes a [workaround](compatibility.md#alpine-linux-compatibility) necessary for this OS.

## [](#installing-the-sdk)Installing the SDK

At least Java 8 is required for current releases; see the [Compatibility](compatibility.md#jdk-compat) section for details. We recommend running the latest Java LTS version (i.e. at the time of writing JDK 25) with the highest patch version available.

Couchbase publishes all stable artifacts to [Maven Central](https://central.sonatype.com/namespace/com.couchbase.client). The latest version of the 3.11 SDK is [3.11.2](https://central.sonatype.com/artifact/com.couchbase.client/java-client/3.11.2/jar).

You can use your favorite dependency management tool to install the SDK.

* Maven
* Gradle

For [Maven](https://maven.apache.org), you can insert the following into the dependencies section of your project's `pom.xml` file:

```xml
    <dependency>
        <groupId>com.couchbase.client</groupId>
        <artifactId>java-client</artifactId>
        <version>3.11.2</version>
    </dependency>
```

Refer to the [Maven Documentation](https://maven.apache.org/guides/introduction/introduction-to-the-pom.html) for more information regarding the structure of the `pom.xml` file.

For [Gradle](https://gradle.org/), you can use:

```groovy
implementation 'com.couchbase.client:java-client:3.11.2'
```

Alternatively, we provide a zip file with all the dependencies bundled if you wish to manually include the `jar` files in your classpath. Refer to the [Release Notes](sdk-release-notes.md) for further details. You can also find links to the hosted javadocs there.

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