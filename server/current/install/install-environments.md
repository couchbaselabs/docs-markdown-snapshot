---
title: Additional Requirements
description: Depending on your local configuration, some components of Couchbase
  Server may have additional system requirements.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/install/pages/install-environments.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/install/install-environments.html)

# Additional Requirements

> Depending on your local configuration, some components of Couchbase Server may have additional system requirements. 

## [](#java-runtime-environment-jre-analytics-service-only)Java Runtime Environment (JRE) — Analytics Service Only

The Analytics Service requires a Java Runtime Environment to be installed. Only [HotSpot-based JVMs](https://openjdk.java.net/groups/hotspot/), which includes the ones provided by OpenJDK and Oracle’s JDK, are supported.

OpenJDK 11 is installed when you install Couchbase Server — you do not need to install any additional prerequisites to use the Analytics service.

However, if necessary, you can specify an alternative JRE for the Analytics Service when you [initialize a node](../manage/manage-nodes/create-cluster.md). If you plan to use an alternative JRE for the Analytics service, note that the following versions are supported.

__Table 1\. Supported Java Runtime Environments__
| **Implementation** | **Version** |
| ------------------ | ----------- |
| Oracle JRE         | Version 11  |
| OpenJDK            | Version 11  |