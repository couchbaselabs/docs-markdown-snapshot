---
title: Start and Stop Enterprise Analytics
description: You can start and stop the Enterprise Analytics service and application.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/install/pages/start-stop-cb-enterprise-analytics.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/enterprise-analytics/2.0/install/start-stop-cb-enterprise-analytics.html)

# Start and Stop Enterprise Analytics

> You can start and stop the Enterprise Analytics service and application. 

This page provides instructions for starting and stopping a standard, package-based installation of Enterprise Analytics.

## [](#start-stop-linux)Linux

On Linux, you can install Enterprise Analytics as a standalone application with support for running as a background (daemon) process during startup. The startup script is automatically installed when you use any of the packaged releases of Enterprise Analytics for Linux. By default, Enterprise Analytics is configured to start automatically at run levels 2, 3, 4, and 5, and explicitly shutdown at run levels 0, 1, and 6.

Start and Stop Enterprise Analytics

```console
sudo systemctl start enterprise-analytics
```

```console
sudo systemctl stop enterprise-analytics
```