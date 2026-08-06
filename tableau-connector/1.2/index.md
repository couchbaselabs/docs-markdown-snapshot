---
title: Introduction
description: The Couchbase Tableau Connector provides integration between your
  high performance Couchbase Tabular Views (TAVs) and the Tableau interactive
  data visualization platform.
editUrl: https://github.com/couchbase/docs-tableau/edit/release/1.2/modules/ROOT/pages/index.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:1.2@tableau-connector::index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tableau-connector/1.2/index.html)

# Introduction

> The Couchbase Tableau Connector provides integration between your high performance Couchbase Tabular Views (TAVs) and the Tableau interactive data visualization platform. 

The connector integrates Tableau with the following Couchbase data sources:

* Couchbase Server (Analytics Service)
* Capella Operational (Analytics Service)
* Capella Analytics

## [](#prerequisites)Prerequisites

Before you begin, make sure you have the following:

| Component                               | Requirement                                                                                      |
| --------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Capella Analytics                       | An existing Couchbase Capella account.                                                           |
| Couchbase Server (Analytics Service)    | Couchbase Server 7.1.1 or later. The Analytics Service must be running on the target node.       |
| Capella Operational (Analytics Service) | An existing Couchbase Capella account. The Analytics Service must be running on the target node. |
| Tableau Desktop                         | 2020.4.x or higher                                                                               |
| Tableau Server                          | 2021.x or higher                                                                                 |

## [](#operating-system-compatibility)Operating System Compatibility

### [](#tableau-desktop)Tableau Desktop

The Couchbase Tableau Connector for Tableau Desktop is available for Windows and macOS. The following table lists the compatible versions:

__Table 1\. Couchbase Tableau connector for Tableau Desktop operating system compatibility__
| Operating System | Version                                 |
| ---------------- | --------------------------------------- |
| Windows          | 8/8.110 (x64)                           |
| macOS            | Mojave 10.14Catalina 10.15Big Sur 11.4+ |

### [](#tableau-server)Tableau Server

The Couchbase Tableau Connector for Tableau Server is available for Windows and Linux. The following table lists the compatible versions:

__Table 2\. Couchbase Tableau connector for Tableau Server operating system compatibility__
| Operating System | Version                                                                                                                               |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Windows          | Windows Server 2016Windows Server 2019                                                                                                |
| Linux            | You can find the full list of supported OS versions at the link [here](https://help.tableau.com/current/server-linux/en-us/requ.htm). |