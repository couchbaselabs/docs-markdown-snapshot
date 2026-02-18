---
title: Collections and Scopes
description: Fully supported in Couchbase Server 7.0.
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.7/modules/concept-docs/pages/collections.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/ruby-sdk/current/concept-docs/collections.html)

# Collections and Scopes

> Fully supported in Couchbase Server 7.0\. 

The Collections feature in Couchbase Server is fully implemented in the 3.2 API version of the Couchbase SDK.

Information on _Collections_ can be found in the [server docs](#8.0@server:learn:data:scopes-and-collections.adoc).

## [](#using-collections-scopes)Using Collections & Scopes

Access a non-default collection, in the default scope, with:

```ruby
bucket.collection('bookings') # in default scope
```

And for a non-default scope:

```ruby
bucket.scope('tenant_agent_00').collection('bookings')
```