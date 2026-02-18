---
title: Client Settings
description: Most settings can be changed through the connection string.
editUrl: https://github.com/couchbase/docs-columnar-sdk-python/edit/release/1.0/modules/ref/pages/client-settings.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/python-columnar-sdk/current/ref/client-settings.html)

# Client Settings

> Most settings can be changed through the connection string. 

Settings are changed by adding them to the connection string, as in the following example:

Connection string with two parameters

couchbases://cb.<your-endpoint>.cloud.couchbase.com?timeout.connect_timeout=75s&timeout.query_timeout=100s