---
title: Integrations &amp; Ecosystem
description: The Couchbase Scala SDK is often used with unofficial and third
  party tools and applications to integrate into broader language and platform
  ecosystems, and across data lakes in heterogeneous environments.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.11/modules/project-docs/pages/third-party-integrations.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:scala-sdk:project-docs:third-party-integrations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/current/project-docs/third-party-integrations.html)

# Integrations &amp; Ecosystem

> The Couchbase Scala SDK is often used with unofficial and third party tools and applications to integrate into broader language and platform ecosystems, and across data lakes in heterogeneous environments. 

Couchbase SDKs are often used with unofficial and third party tools and applications to integrate into broader language and platform ecosystems, and across data lakes in heterogeneous environments. These are some of the applications that you need to be aware of.

## [](#couchbase-integrations)Couchbase Integrations

Couchbase engineers are involved to a greater or lesser degree with projects that help get the SDK working with various common challenges.

The Couchbase Scala SDK is a first class citizen in the [Spring Data](https://spring.io/projects/spring-data-couchbase) world, and the Scala SDK can leverage that through the JVM.

Couchbase also supports integrating with [Spark](#spark-connector:ROOT:getting-started.adoc.adoc).

### [](#ide-integrations)IDE Integrations

To make development easier, [Couchbase plugins](../../../server/current/third-party/integrations.md#ide-integrations) are available for [VSCode](https://marketplace.visualstudio.com/items?itemName=Couchbase.vscode-couchbase) and the [IntelliJ](https://plugins.jetbrains.com/plugin/22131-couchbase) family of IDEs and editors.

## [](#across-the-ecosystem)Across the Ecosystem

Although unsupported, and not maintained by Couchbase, several projects are worth a look at. We offer brief notes on what you should consider if integrating with them:

Why not take advantage of compatible Java tools? Many dataflow tools integrate with Couchbase, including [Apache NiFi](https://github.com/apache/nifi/tree/main/nifi-nar-bundles/nifi-couchbase-bundle), [Apache Camel](https://wildfly-extras.github.io/wildfly-camel/#%5Fcamel%5Fcouchbase), and [Apache Flink](https://github.com/couchbaselabs/flink-connector-couchbase).

## [](#community)Community

There are too many third party integrations to evaluate and list (and absence of a mention in these pages is no judgement on importance or quality), but the following are well worth investigating:

[Databricks](https://docs.databricks.com/data/data-sources/couchbase.html) provides integration with the Couchbase Scala SDK and Spark.

## [](#see-also)See Also

Couchbase Server (Capella or self-managed) offers many partner and community integrations — the [Integrations, Connectors, and Tools](../../../cloud/third-party/integrations.md) page contains a full listing.