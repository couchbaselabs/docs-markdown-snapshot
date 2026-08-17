---
title: Collections and Scopes
description: Fully supported in Couchbase Server 7.0.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.7/modules/concept-docs/pages/collections.adoc
  xref: xref:3.7@ruby-sdk:concept-docs:collections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/3.7/concept-docs/collections.html)

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