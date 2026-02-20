---
title: 3rd Party Integrations
description: The Couchbase Ruby SDK is often used with unofficial and third
  party tools and applications to integrate into broader language and platform
  ecosystems, and across data lakes in heterogeneous environments.
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.7/modules/project-docs/pages/third-party-integrations.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:ruby-sdk:project-docs:third-party-integrations.adoc[]
---

[View original HTML](/ruby-sdk/current/project-docs/third-party-integrations.html)

# 3rd Party Integrations

> The Couchbase Ruby SDK is often used with unofficial and third party tools and applications to integrate into broader language and platform ecosystems, and across data lakes in heterogeneous environments. 

Couchbase SDKs are often used with unofficial and third party tools and applications to integrate into broader language and platform ecosystems, and across data lakes in heterogeneous environments. These are some of the applications that you need to be aware of.

## [](#across-the-ecosystem)Across the Ecosystem

Although unsupported, and not maintained by Couchbase, several projects are worth a look at. We offer brief notes on what you should consider if integrating with them:

The Couchbase Ruby SDK integrates well with Ruby-on-Rails, particularly for use as a [Rails Cache Store](https://guides.rubyonrails.org/caching%5Fwith%5Frails.html#cache-stores). To do so, add the following to your Rails application config:

```ruby
config.cache_store = :couchbase_store, {
  connection_string: "couchbase://localhost",
  username: "app_cache_user",
  password: "s3cret",
  bucket: "app_cache"
}
```

An implementation of the Cache Store for Rails can be found in our [Ruby client repo](https://github.com/couchbase/couchbase-ruby-client/blob/master/lib/active%5Fsupport/cache/couchbase%5Fstore.rb), and on the [Caching Example page](../howtos/caching-example.md).