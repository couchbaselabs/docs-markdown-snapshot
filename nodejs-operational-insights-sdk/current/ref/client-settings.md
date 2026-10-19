---
title: Client Settings
description: Most settings can be changed through the connection string.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Node.js Operational Insights SDK
    version: "1.0"
antora:
  editUrl: https://github.com/couchbase/docs-operational-insights-sdk-nodejs/edit/release/1.0/modules/ref/pages/client-settings.adoc
  xref: xref:nodejs-operational-insights-sdk:ref:client-settings.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-operational-insights-sdk/current/ref/client-settings.html)

# Client Settings

> Most settings can be changed through the connection string. 

Settings are changed by adding them to the connection string, as in the following example:

Connection string with two parameters

https://insights.example.com?timeout.connect_timeout=75s&timeout.query_timeout=100s