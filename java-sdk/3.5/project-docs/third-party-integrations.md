---
title: 3rd Party Integrations
description: The Couchbase Java SDK is often used with unofficial and third
  party tools and applications to integrate into broader language and platform
  ecosystems, and across data lakes in heterogeneous environments.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.5/modules/project-docs/pages/third-party-integrations.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.5@java-sdk:project-docs:third-party-integrations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.5/project-docs/third-party-integrations.html)

# 3rd Party Integrations

> The Couchbase Java SDK is often used with unofficial and third party tools and applications to integrate into broader language and platform ecosystems, and across data lakes in heterogeneous environments. 

Couchbase SDKs are often used with unofficial and third party tools and applications to integrate into broader language and platform ecosystems, and across data lakes in heterogeneous environments. These are some of the applications that you need to be aware of.

## [](#couchbase-integrations)Couchbase Integrations

Couchbase engineers are involved to a greater or lesser degree with projects that help get the SDK working with various common challenges.

The Couchbase Java SDK is a first class citizen in the [Spring Data](https://spring.io/projects/spring-data-couchbase) world, and there are many examples of using the SDK with [Spring Boot](https://blog.couchbase.com/couchbase-spring-boot-spring-data/) and Spring Data (and Spring Data JPA).

Couchbase also supports integrating with [Spark](#3.2@spark-connector:ROOT:java-api.adoc).

## [](#across-the-ecosystem)Across the Ecosystem

Although unsupported, and not maintained by Couchbase, several projects are worth a look at. We offer brief notes on what you should consider if integrating with them:

Many dataflow tools integrate with Couchbase, including [Apache NiFi](https://github.com/apache/nifi/tree/main/nifi-nar-bundles/nifi-couchbase-bundle), [Apache Camel](https://wildfly-extras.github.io/wildfly-camel/#%5Fcamel%5Fcouchbase), and [Apache Flink](https://github.com/couchbaselabs/flink-connector-couchbase). Why not make development easier, and use [Apache Zeppelin](https://blog.couchbase.com/create-a-zeppelin-interpreter-for-couchbase/)?

## [](#community)Community

There are too many third party integrations to evaluate and list (and absence of a mention in these pages is no judgement on importance or quality), but the following are well worth investigating:

[Couchmove](https://github.com/differentway/couchmove) is an open-source Java migration tool for Couchbase, inspired by Flyway. It can help you "track, manage and apply changes, in your Couchbase buckets." The philosophy of the project claims to "strongly favor simplicity and convention over configuration".

In CouchMove you write your migrations in [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql), while in [CouchVersion](https://github.com/couchbaselabs/CouchVersion) you can write them using the Java SDK, which essentially allow you to create more complex migrations. CouchVersion provides a new approach for adding changes (change sets) based on Java classes and methods with appropriate annotations.