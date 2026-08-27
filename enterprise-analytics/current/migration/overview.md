---
title: Overview
description: Learn how to migrate from Couchbase or Capella Analytics Service
  including checklists, best practices, and key steps for a successful
  migration.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/migration/pages/overview.adoc
  xref: xref:enterprise-analytics:migration:overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/migration/overview.html)

# Overview

> Learn how to migrate from Couchbase or Capella Analytics Service including checklists, best practices, and key steps for a successful migration. 

This section provides a comprehensive checklist and best practices to help you prepare to migrate from Couchbase Server Analytics Service or Capella Operational Analytics Service to Capella Analytics or Enterprise Analytics. It covers key steps including data migration scenarios, schema design, and indexing strategies. It also addresses query and SDK migration, and security considerations.

Existing Couchbase Analytics users can migrate applications and workloads to Capella Analytics or Enterprise Analytics for improved performance and features. The migration allows you to use the enhanced performance and advanced features of JSON-native NoSQL analytical database for real-time analytical processing. The process prioritizes efficient data and configuration transfer, minimal downtime, and data integrity.

The migration process consists of 3 key phases:

* [Pre-migration Planning and Preparation](pre-migration.md)
* [Migration](migration-process.md)
* [Post Migration Validation and Cutover](post-migration.md)

## [](#migration-paths)Migration Paths

This migration can occur via 1 of 3 possible paths, determined by your current source and desired target destination.

* Capella Operational (Analytics Service) to Capella Analytics
* Couchbase Server (Analytics Service) to Enterprise Analytics
* Couchbase Server (Analytics Service) to Capella Analytics