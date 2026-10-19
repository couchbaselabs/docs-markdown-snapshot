---
title: Start and Stop Operational Insights
description: You can start and stop the Operational Insights service and application.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/install/pages/start-stop-cb-operational-insights.adoc
  xref: xref:enterprise-analytics:install:start-stop-cb-operational-insights.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/install/start-stop-cb-operational-insights.html)

# Start and Stop Operational Insights

> You can start and stop the Operational Insights service and application. 

This page provides instructions for starting and stopping a standard, package-based installation of Operational Insights.

## [](#start-stop-linux)Linux

On Linux, you can install Operational Insights as a standalone application with support for running as a background (daemon) process during startup. The startup script is automatically installed when you use any of the packaged releases of Operational Insights for Linux. By default, Operational Insights is configured to start automatically at run levels 2, 3, 4, and 5, and explicitly shutdown at run levels 0, 1, and 6.

Start and Stop Operational Insights

```console
sudo systemctl start operational-insights
```

```console
sudo systemctl stop operational-insights
```