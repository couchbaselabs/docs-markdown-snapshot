---
title: CLI Reference
description: The command-line interface (CLI) tools let you manage and monitor
  your Operational Insights installation.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/cli/pages/cli-intro.adoc
  xref: xref:enterprise-analytics:cli:cli-intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/cli/cli-intro.html)

# CLI Reference

> The command-line interface (CLI) tools let you manage and monitor your Operational Insights installation. 

The Operational Insights installation process installs the command-line tools. After installation, the location of these tools depends on your platform:

| Operating System | Directory Locations                                                    |
| ---------------- | ---------------------------------------------------------------------- |
| Linux            | /opt/couchbase/bin /opt/couchbase/bin/install /opt/couchbase/bin/tools |

## [](#managing-diagnostics)Managing Diagnostics

The command-line interface provides commands to start, stop, and report status for log collection. You can collect diagnostics through the command-line interface by using the [couchbase-cli](couchbase-cli.md) or the [cbcollect\_info](cbcollect-info-tool.md) tool.