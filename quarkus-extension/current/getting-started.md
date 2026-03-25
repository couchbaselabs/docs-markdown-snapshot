---
title: Getting Started
description: The Couchbase Quarkus extension integrates the Couchbase Java SDK
  within the Quarkus ecosystem.
editUrl: https://github.com/couchbase/docs-quarkus-extension/edit/release/1.3/modules/ROOT/pages/getting-started.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:quarkus-extension::getting-started.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/quarkus-extension/current/getting-started.html)

# Getting Started

We recommend using SDKMAN to install the JDK, and Mandrel (the Quarkus-recommended version of GraalVM).

```console
sdk install java 25.0.1.r25-mandrel
sdk use java 25.0.1.r25-mandrel
```

## [](#creating-a-quarkus-app)Creating a Quarkus App

It is recommended to generate a starter app using the [Quarkus Code Starter](https://code.quarkus.io/?e=io.quarkiverse.couchbase%3Aquarkus-couchbase). If you already have a Quarkus app on hand, install with Maven or Gradle as follows:

* Maven
* Gradle

Add this to your `pom.xml`:

```xml
<dependency>
  <groupId>io.quarkiverse.couchbase</groupId>
  <artifactId>quarkus-couchbase</artifactId>
  <version>1.3.0</version>
</dependency>
```

```groovy
dependencies {
    implementation 'io.quarkiverse.couchbase:quarkus-couchbase:1.3.0'
}
```

## [](#configuring-couchbase)Configuring Couchbase

Configure the connection in your `application.properties` file, typically located in `src/main/resources`:

```properties
quarkus.couchbase.connection-string=localhost
quarkus.couchbase.username=username
quarkus.couchbase.password=password
```

For additional configuration options, refer to the [Quarkus Configuration Guide](https://docs.quarkiverse.io/quarkus-couchbase/dev/configuration.html) or [API Reference](https://javadoc.io/doc/io.quarkiverse.couchbase/quarkus-couchbase/latest/index.html).

## [](#using-the-extension)Using the Extension

The extension produces an Application-scoped `Cluster` bean that can be injected using the jakarta annotation `@Inject`:

```java
public class QuarkusExample {
    @Inject
    Cluster cluster;
}
```

From there, you can use the Cluster object like you normally would with the Java SDK. Refer to the [Quarkus Guide](https://docs.quarkiverse.io/quarkus-couchbase/dev/index.html) for an example using `quarkus-rest` to create HTTP endpoints.