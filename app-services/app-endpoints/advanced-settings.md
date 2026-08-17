---
title: Advanced Settings for App Endpoints
description: App Endpoints possess a variety of advanced settings to customize
  your applications.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/app-endpoints/advanced-settings.adoc
  xref: xref:app-services::app-endpoints/advanced-settings.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/app-endpoints/advanced-settings.html)

# Advanced Settings for App Endpoints

> App Endpoints possess a variety of advanced settings to customize your applications. 

## [](#delta-sync)Delta Sync

Delta Sync provides the ability to replicate only those parts of a Couchbase document that have changed, syncing the document data across devices. Syncing only changed data can result in significant savings in bandwidth consumption as well as throughput improvements, especially useful where network bandwidth is constrained.

## [](#import-filters)Import Filters

Import Filters identify the subset of documents eligible to be replicated by App services based on user-defined requirements. This subset is applied to all future mutations.

Without a filter (the default), the App Service imports all documents that are inserted or mutated within the associated linked collection of a scope in a given bucket. This default setting is recommended unless and until you find a compelling use-case against it.

## [](#xattrs)XATTRs

You can store channels and roles as user extended attributes (XATTRs). This is a more secure alternative that uses metadata, outside of the document content, to grant access.

## [](#cross-origin-resource-sharing-cors-configuration)Cross-Origin Resource Sharing (CORS) Configuration

You can configure CORS per App Endpoint to relax the [Same-Origin](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin%5Fpolicy) access policy and enable granular access controls across different areas of your applications.

> [!CAUTION]
> At least one Origin must be configured upon confirmation of the CORS configuration.

## [](#see-also)See Also

* [Delta Sync](delta-sync.md)
* [Import Filters](import-filters.md)
* [Extended Attributes (XATTRs)](xattrs-for-app-services.md)
* [Cross-Origin Resource Sharing (CORS)](cors-configuration-for-app-services.md)