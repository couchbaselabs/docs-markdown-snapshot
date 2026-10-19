---
title: Error Messages
description: The standardized error codes and eceptions returned by the
  Operational Insights Java SDK, from cluster connection to SQL++ query.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Java Operational Insights SDK
    version: "1.0"
antora:
  editUrl: https://github.com/couchbase/docs-operational-insights-sdk-java/edit/release/1.0/modules/ref/pages/error-codes.adoc
  xref: xref:java-operational-insights-sdk:ref:error-codes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-operational-insights-sdk/current/ref/error-codes.html)

# Error Messages

> The standardized error codes and eceptions returned by the Operational Insights Java SDK, from cluster connection to SQL++ query. 

An `AnalticsException` is thrown when an interaction with the Operational Insights cluster fails.

## [](#insightsexception)InsightsException

An `AnalticsException` is thrown when an interaction (or attempted interaction) with the Insights cluster fails.

## [](#other-analytics-error-codes)Other Analytics Error Codes

For other errors the Java Operational Insights SDK passes through the Analytics error codes from Operational Insights.

For a full list of these error codes, see [Analytics Error Codes](../../../server/current/analytics/error-codes.md).