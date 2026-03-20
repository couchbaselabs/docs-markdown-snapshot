---
title: Caching Example
description: A walk-through of the steps to use Couchbase as a caching layer for Rails.
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.6/modules/howtos/pages/caching-example.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.6@ruby-sdk:howtos:caching-example.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/3.6/howtos/caching-example.html)

# Caching Example

> A walk-through of the steps to use Couchbase as a caching layer for Rails. 

This example demonstrates how to integrate Couchbase into a caching layer of the [Rails](https://rubyonrails.org/) web-framework.

You can also find the [full code for _this_ example here](https://github.com/couchbase/docs-sdk-ruby/blob/temp/3.5/modules/howtos/examples/rails-caching-example).

## [](#configuration)Configuration

All necessary classes that implement rails caching API are part of the official SDK for Ruby, so to add it to the application you just need to update your `Gemfile`:

```ruby
gem "couchbase"
```

Do not forget to run `bundle install` to ensure that all dependencies have been satisfied.

Now the application have to be configured to use Couchbase as a caching backend. Corresponding configuration usually kept in the configuration environment file and looks like this:

```ruby
    config.cache_store = :couchbase_store, {
      connection_string: ENV.fetch("COUCHBASE_CONNECTION_STRING", "couchbase://localhost"),
      username: ENV.fetch("COUCHBASE_USERNAME", "Administrator"),
      password: ENV.fetch("COUCHBASE_PASSWORD", "password"),
      bucket: ENV.fetch("COUCHBASE_BUCKET", "default"),
      scope: ENV.fetch("COUCHBASE_SCOPE", "_default"),
      collection: ENV.fetch("COUCHBASE_COLLECTION", "_default")
    }
```

In this development example, we will try to discover cluster location and credentials in the environment variables, with a fallback to localhost and safe default. In a production environment all sensitive information (like passwords) must be managed in secure ways, using secrets providers.

## [](#usage)Usage

With the configuration step, all Couchbase-specific code is done — after that familiar API of the `Rails.cache` will be used. In this example, we cache the current time for the 3 seconds:

```ruby
class WallClockController < ApplicationController
  def now
    @current_time = Rails.cache.fetch("current_time", expires_in: 3.seconds) do
      Time.now
    end
  end
```

## [](#additional-resources)Additional Resources

* You can find an overview of the Rails Caching API at [Rails Guides](https://guides.rubyonrails.org/caching%5Fwith%5Frails.html).
* The API reference of `CouchbaseStore` class can be found at the [official API referece](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/ActiveSupport/Cache/CouchbaseStore.html).