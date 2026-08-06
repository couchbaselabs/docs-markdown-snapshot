---
title: Client Settings
description: Most settings can be changed through the connection string.
editUrl: https://github.com/couchbase/docs-analytics-sdk-python/edit/release/1.0/modules/ref/pages/client-settings.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:1.0@python-analytics-sdk:ref:client-settings.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-analytics-sdk/1.0/ref/client-settings.html)

# Client Settings

> Most settings can be changed through the connection string. 

Settings are changed by adding them to the connection string, as in the following example:

Connection string with two parameters

https://analytics.example.com?timeout.connect_timeout=75s&timeout.query_timeout=100s