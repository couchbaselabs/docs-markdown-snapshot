---
title: Async and Batching APIs
description: An async implementation is not yet available in the 3.x API Ruby SDK.
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.7/modules/howtos/pages/concurrent-async-apis.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:ruby-sdk:howtos:concurrent-async-apis.adoc[]
---

[View original HTML](/ruby-sdk/current/howtos/concurrent-async-apis.html)

# Async and Batching APIs

> An async implementation is not yet available in the 3.x API Ruby SDK. 

## [](#batching)Batching

Upserting (or fetching or deleting) multiple documents simultaneously may be performed with the `get_multi()`, `upsert_multi()`, and `remove_multi()` methods. These are part of the [Collection](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Collection.html) class.

### [](#using-the-collection-methods)Using the Collection Methods

get\_multi()

```ruby
res = collection.get_multi(["foo", "bar"], Options::GetMulti(timeout: 3_000))

# res[0].content #=> content of "foo"
# res[1].content #=> content of "bar"
```

Details of timeout, `retry_strategy`, and other parameters can be found in the [API docs](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Options/GetMulti.html).

upsert\_multi()

```ruby
res = collection.upsert_multi([
  "foo", {"foo" => 42},
  "bar", {"bar" => "some value"}
], Options::UpsertMulti(expiry: 20))

#  res[0].cas #=> 7751414725654
#  res[1].cas #=> 7751418925851
```

For details of additional parameters, such as transcoder settings, durability level, and parent span, [see the API docs](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Options/UpsertMulti.html).

remove\_multi()

```ruby
res = collection.upsert("mydoc", {"foo" => 42})
res.cas #=> 7751414725654

res = collection.remove_multi(["foo", ["mydoc", res.cas]], Options::RemoveMulti(timeout: 3_000))
if res[1].error.is_a?(Error::CasMismatch)
  puts "Failed to remove the document, it may have been changed by another application."
end
```

Once again, full details of parameters for this method can be found in the [API documentation](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Options/RemoveMulti.html).