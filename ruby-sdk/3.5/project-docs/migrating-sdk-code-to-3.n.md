---
title: Migrating from SDK2 to SDK3 API
description: The 3.x API breaks the existing 2.x APIs in order to provide a
  number of improvements. Collections and Scopes are introduced.
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.5/modules/project-docs/pages/migrating-sdk-code-to-3.n.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/ruby-sdk/3.5/project-docs/migrating-sdk-code-to-3.n.html)

# Migrating from SDK2 to SDK3 API

> The 3.x API breaks the existing 2.x APIs in order to provide a number of improvements. Collections and Scopes are introduced. The Document class and structure has been completely removed from the API, and the returned value is now `Result`. Retry behaviour is more proactive, and lazy bootstrapping moves all error handling to a single place. 

The Ruby 2.x Couchbase SDK was not generally available as a supported product, working across all services, so no migration guide is necessary here.

Versions of the documentation for Ruby SDK 1.x can be found in the [archive](https://docs-archive.couchbase.com/home/index.html).