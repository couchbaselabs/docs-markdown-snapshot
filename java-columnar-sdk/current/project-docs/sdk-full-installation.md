---
title: Maven Coordinates
description: How to get the Java Columnar SDK from Maven Central.
editUrl: https://github.com/couchbase/docs-columnar-sdk-java/edit/release/1.0/modules/project-docs/pages/sdk-full-installation.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:java-columnar-sdk:project-docs:sdk-full-installation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-columnar-sdk/current/project-docs/sdk-full-installation.html)

# Maven Coordinates

> How to get the Java Columnar SDK from Maven Central. 

## [](#getting-the-sdk)Getting the SDK

Couchbase publishes all stable artifacts to [Maven Central](https://central.sonatype.com/artifact/com.couchbase.client/couchbase-columnar-java-client).

Use your favorite dependency management tool to include the SDK in your project:

* Maven
* Gradle (Kotlin)
* Gradle (Groovy)

For [Maven](https://maven.apache.org), add this to the `dependencies` section of your project's `pom.xml` file:

```xml
<dependency>
    <groupId>com.couchbase.client</groupId>
    <artifactId>couchbase-columnar-java-client</artifactId>
    <version>1.0.7</version>
</dependency>
```

Refer to the [Maven Documentation](https://maven.apache.org/guides/introduction/introduction-to-the-pom.html/) for more information regarding the structure of the `pom.xml` file.

For a [Gradle](https://gradle.org/) script written in Kotlin, add this line to the `dependencies` section of your project's `build.gradle.kts` file:

```kotlin
implementation("com.couchbase.client:couchbase-columnar-java-client:1.0.7")
```

For a [Gradle](https://gradle.org/) script written in Groovy, add this line to the `dependencies` section of your project's `build.gradle` file:

```groovy
implementation 'com.couchbase.client:couchbase-columnar-java-client:1.0.7'
```

## [](#using-a-snapshot-version)Using a Snapshot Version

Couchbase publishes pre-release snapshot artifacts to the Sonatype OSS Snapshot Repository. If you wish to use a snapshot version, you'll need to tell your build tool about this repository.

* Maven
* Gradle (Kotlin)
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

`**build.gradle.kts**`

```kotlin
repositories {
    mavenCentral()
    maven {
        url = uri("https://oss.sonatype.org/content/repositories/snapshots")
        mavenContent { snapshotsOnly() }
    }
}
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

> [!CAUTION]
> Couchbase does not provide support for snapshot artifacts. We don't recommend using them unless you're working closely with Couchbase Support to verify a particular issue has been resolved prior to release.