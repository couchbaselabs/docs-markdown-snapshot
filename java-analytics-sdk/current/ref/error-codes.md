---
title: Error Messages
description: The standardized error codes and eceptions returned by the
  Enterprise Analytics Java SDK, from cluster connection to SQL++ query.
pubDate: 2026-10-14T04:27:20.555Z
meta:
  component:
    title: Java Analytics SDK
    version: "1.1"
antora:
  editUrl: https://github.com/couchbase/docs-analytics-sdk-java/edit/release/1.1/modules/ref/pages/error-codes.adoc
  xref: xref:java-analytics-sdk:ref:error-codes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-analytics-sdk/current/ref/error-codes.html)

# Error Messages

> The standardized error codes and eceptions returned by the Enterprise Analytics Java SDK, from cluster connection to SQL++ query. 

An `AnalticsException` is thrown when an interaction with the Analytics cluster fails.

## [](#analticsexception)AnalticsException

An `AnalticsException` is thrown when an interaction (or attempted interaction) with the Analytics cluster fails.

## [](#other-analytics-error-codes)Other Analytics Error Codes

For other errors the Java Analytics SDK passes through the Analytics error codes from Enterprise Analytics.

For a full list of these error codes, see [Analytics Error Codes](../../../server/current/analytics/error-codes.md).