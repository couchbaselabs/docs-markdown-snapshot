---
title: Client Settings
description: Most settings can be changed through the connection string.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-analytics-sdk-nodejs/edit/release/1.0/modules/ref/pages/client-settings.adoc
  xref: xref:1.0@nodejs-analytics-sdk:ref:client-settings.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-analytics-sdk/1.0/ref/client-settings.html)

# Client Settings

> Most settings can be changed through the connection string. 

Settings are changed by adding them to the connection string, as in the following example:

Connection string with two parameters

https://analytics.example.com?timeout.connect_timeout=75s&timeout.query_timeout=100s