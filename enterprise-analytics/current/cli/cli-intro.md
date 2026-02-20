---
title: CLI Reference
description: The command-line interface (CLI) tools let you manage and monitor
  your Enterprise Analytics installation.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/cli/pages/cli-intro.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:enterprise-analytics:cli:cli-intro.adoc[]
---

[View original HTML](/enterprise-analytics/current/cli/cli-intro.html)

# CLI Reference

> The command-line interface (CLI) tools let you manage and monitor your Enterprise Analytics installation. 

The Enterprise Analytics installation process installs the command-line tools. After installation, the location of these tools depends on your platform:

| Operating System | Directory Locations                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------- |
| Linux            | /opt/enterprise-analytics/bin /opt/enterprise-analytics/bin/install /opt/enterprise-analytics/bin/tools |

## [](#managing-diagnostics)Managing Diagnostics

The command-line interface provides commands to start, stop, and report status for log collection. You can collect diagnostics through the command-line interface by using the [couchbase-cli](#cli:cbcli/couchbase-cli.adoc) or the [cbcollect\_info](cbcollect-info-tool.md) tool.