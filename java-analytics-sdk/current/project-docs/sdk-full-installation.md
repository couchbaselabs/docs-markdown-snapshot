---
title: Maven Coordinates
description: How to get the Java Analytics SDK from Maven Central.
editUrl: https://github.com/couchbase/docs-analytics-sdk-java/edit/release/1.0/modules/project-docs/pages/sdk-full-installation.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:java-analytics-sdk:project-docs:sdk-full-installation.adoc[]
---

[View original HTML](/java-analytics-sdk/current/project-docs/sdk-full-installation.html)

# Maven Coordinates

> How to get the Java Analytics SDK from Maven Central. 

## [](#getting-the-sdk)Getting the SDK

Couchbase publishes all stable artifacts to [Maven Central](https://central.sonatype.com/artifact/com.couchbase.client/couchbase-analytics-java-client).

Use your favorite dependency management tool to include the SDK in your project:

* Maven
* Gradle (Kotlin)
* Gradle (Groovy)

For [Maven](https://maven.apache.org), add this to the `dependencies` section of your project’s `pom.xml` file:

```xml
<dependency>
    <groupId>com.couchbase.client</groupId>
    <artifactId>couchbase-analytics-java-client</artifactId>
    <version>1.0.0</version>
</dependency>
```

Refer to the [Maven Documentation](https://maven.apache.org/guides/introduction/introduction-to-the-pom.html/) for more information regarding the structure of the `pom.xml` file.

For a [Gradle](https://gradle.org/) script written in Kotlin, add this line to the `dependencies` section of your project’s `build.gradle.kts` file:

```kotlin
implementation("com.couchbase.client:couchbase-analytics-java-client:1.0.0")
```

For a [Gradle](https://gradle.org/) script written in Groovy, add this line to the `dependencies` section of your project’s `build.gradle` file:

```groovy
implementation 'com.couchbase.client:couchbase-analytics-java-client:1.0.0'
```

## [](#using-a-snapshot-version)Using a Snapshot Version

Couchbase publishes pre-release snapshot artifacts to the Sonatype OSS Snapshot Repository. If you wish to use a snapshot version, you’ll need to tell your build tool about this repository.

* Maven
* Gradle (Kotlin)
* Gradle (Groovy)

`**pom.xml**`

```xml
<repositories>
  <repository>
    <name>Central Portal Snapshots</name>
    <id>central-portal-snapshots</id>
    <url>https://central.sonatype.com/repository/maven-snapshots/</url>
    <releases><enabled>false</enabled></releases>
    <snapshots><enabled>true</enabled></snapshots>
  </repository>
</repositories>
```

`**build.gradle.kts**`

```kotlin
repositories {
    mavenCentral()
    maven {
        url = uri("https://central.sonatype.com/repository/maven-snapshots/")
        mavenContent { snapshotsOnly() }
    }
}
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

> [!CAUTION]
> Couchbase does not provide support for snapshot artifacts. We don’t recommend using them unless you’re working closely with Couchbase Support to verify a particular issue has been resolved prior to release.