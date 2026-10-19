---
title: Additional Requirements
description: Depending on your local configuration, you might need to install or
  configure some additional system requirements to use Operational Insights.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/install/pages/additional-req.adoc
  xref: xref:enterprise-analytics:install:additional-req.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/install/additional-req.html)

# Additional Requirements

> Depending on your local configuration, you might need to install or configure some additional system requirements to use Operational Insights. 

## [](#java-runtime-environment-jre)Java Runtime Environment (JRE)

OpenJDK 21 is installed when you install Operational Insights. Only [HotSpot-based JVMs](https://openjdk.java.net/groups/hotspot/), which include the ones provided by OpenJDK and Oracle's JDK, are supported. If you plan to use an alternative JRE, the following versions are supported.

__Table 1\. Supported Java Runtime Environments__
| **Implementation** | **Version** |
| ------------------ | ----------- |
| Oracle JRE         | Version 21  |
| OpenJDK            | Version 21  |