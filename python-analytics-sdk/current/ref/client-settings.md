---
title: Client Settings
description: Most settings can be changed through the connection string.
editUrl: https://github.com/couchbase/docs-analytics-sdk-python/edit/release/1.0/modules/ref/pages/client-settings.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:python-analytics-sdk:ref:client-settings.adoc[]
---

[View original HTML](/python-analytics-sdk/current/ref/client-settings.html)

# Client Settings

> Most settings can be changed through the connection string. 

Settings are changed by adding them to the connection string, as in the following example:

Connection string with two parameters

https://analytics.example.com?timeout.connect_timeout=75s&timeout.query_timeout=100s