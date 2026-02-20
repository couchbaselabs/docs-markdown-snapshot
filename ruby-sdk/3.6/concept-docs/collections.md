---
title: Collections and Scopes
description: Fully supported in Couchbase Server 7.0.
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.6/modules/concept-docs/pages/collections.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:3.6@ruby-sdk:concept-docs:collections.adoc[]
---

[View original HTML](/ruby-sdk/3.6/concept-docs/collections.html)

# Collections and Scopes

> Fully supported in Couchbase Server 7.0\. 

The Collections feature in Couchbase Server is fully implemented in the 3.2 API version of the Couchbase SDK.

Information on _Collections_ can be found in the [server docs](#7.1@server:learn:data:scopes-and-collections.adoc).

## [](#using-collections-scopes)Using Collections & Scopes

Access a non-default collection, in the default scope, with:

```ruby
bucket.collection('bookings') # in default scope
```

And for a non-default scope:

```ruby
bucket.scope('tenant_agent_00').collection('bookings')
```