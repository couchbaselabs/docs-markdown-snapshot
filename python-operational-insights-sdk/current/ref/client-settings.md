---
title: Client Settings
description: Most settings can be changed through the connection string.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Python Operational Insights SDK
    version: "1.0"
antora:
  editUrl: https://github.com/couchbase/docs-operational-insights-sdk-python/edit/release/1.0/modules/ref/pages/client-settings.adoc
  xref: xref:python-operational-insights-sdk:ref:client-settings.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-operational-insights-sdk/current/ref/client-settings.html)

# Client Settings

> Most settings can be changed through the connection string. 

Settings are changed by adding them to the connection string, as in the following example:

Connection string with two parameters

https://operational-insights.example.com?timeout.connect_timeout=75s&timeout.query_timeout=100s