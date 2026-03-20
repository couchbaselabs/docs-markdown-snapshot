---
title: Client Settings
description: Most settings can be changed through the connection string.
editUrl: https://github.com/couchbase/docs-analytics-sdk-nodejs/edit/release/1.0/modules/ref/pages/client-settings.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:nodejs-analytics-sdk:ref:client-settings.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-analytics-sdk/current/ref/client-settings.html)

# Client Settings

> Most settings can be changed through the connection string. 

Settings are changed by adding them to the connection string, as in the following example:

Connection string with two parameters

https://analytics.example.com?timeout.connect_timeout=75s&timeout.query_timeout=100s