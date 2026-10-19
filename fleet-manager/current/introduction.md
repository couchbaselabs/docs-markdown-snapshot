---
title: Couchbase Fleet Manager
description: Asset Management for Couchbase Server.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Fleet Manager
    version: "1.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-fleetmanager/edit/main/modules/ROOT/pages/introduction.adoc
  xref: xref:fleet-manager::introduction.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/fleet-manager/current/introduction.html)

# Couchbase Fleet Manager

> Asset Management for Couchbase Server. 

## [](#overview)Overview

Fleet Manager is a self-service portal and telemetry system that gives self-managed customers visibility into their Couchbase Server deployments, enabling transparent license alignment without operational disruption.

Fleet Manager provides:

* Telemetry collected by all the nodes across your clusters that are sent to Fleet Manager.  
> [!NOTE]  
> Only Couchbase versions `7.6.12` and `8.0.3+` broadcast the telemetry.
* A web-based dashboard that aggregates the telemetry and uses it to generate metrics and usage alerts checked across your licensing subscriptions.

![Couchbase Fleet Manager Architecture](_images/diag-ca9fdcbbd8ea5c2752bd5d761529405270170073.svg) 

Figure 1\. Couchbase Fleet Manager Architecture

Each node collects and pushes the usage data out to your network via a named service address.

The dashboard reads the telemetry and uses it to generate usage profiles and subscription alerts.

![dashboard](_images/dashboard.png) 

Figure 2\. Fleet Manager Dashboard

> [!IMPORTANT]
> Telemetry collection
> 
> The telemetry collected by Fleet Manager is sent to the portal via the named service and is TLS-encrypted before transmission.
> 
> Collected telemetry is **not** sent to Couchbase.