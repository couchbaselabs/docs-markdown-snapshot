---
title: Migrating from SDK2 to SDK3 API
description: This is the first release of the Couchbase Scala SDK -- you will
  not have any code based upon older API versions.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/temp/1.6/modules/project-docs/pages/migrating-sdk-code-to-3.n.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:1.6@scala-sdk:project-docs:migrating-sdk-code-to-3.n.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/1.6/project-docs/migrating-sdk-code-to-3.n.html)

# Migrating from SDK2 to SDK3 API

> This is the first release of the Couchbase Scala SDK — you will not have any code based upon older API versions. 

Couchbase Scala SDK 1.0 implements the Couchbase SDK 3.0 API. It it the first release of the Couchbase Scala SDK, there are no releases implementing older APIs. Migration will only be a concern if you are mixing code from different JVM SDKs in your application — specifically the Java SDK — in which case you will need to be using Java SDK 3.0 and above. If you have programmed Couchbase client software against the Java 2.x SDK previously, then you may want to read the [Java migration guide](#3.0@java-sdk:project-docs:migrating-sdk-code-to-3.n.adoc).