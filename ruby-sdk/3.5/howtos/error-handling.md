---
title: Handling Errors
description: Error handling from the Ruby SDK.
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.5/modules/howtos/pages/error-handling.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.5@ruby-sdk:howtos:error-handling.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/3.5/howtos/error-handling.html)

# Handling Errors

> Error handling from the Ruby SDK. 

Errors are inevitable. The developer's job is to be prepared for whatever is likely to come up — and to try and be prepared for anything that conceivably could come up. Couchbase gives you a lot of flexibility, but it is recommended that you equip yourself with an understanding of the possibilities.

## [](#how-the-sdk-handles-errors)How the SDK Handles Errors

Couchbase-specific exceptions are all derived from `Couchbase::Error::CouchbaseError`. Errors that cannot be recovered by the SDK will be returned to the application. These unrecoverable errors are left to the application developer to handle — this section covers handling many of the common error scenarios.

## [](#handling-errors)Handling Errors

The approach will depend upon the type of error thrown. Is it transient? Is it even recoverable? Below we examine error handling strategies in relation to the Couchbase SDKs, then take a practical walk through some common error scenarios you are likely to have to handle when working with a Couchbase cluster.

### [](#failing)Failing

While most of the time you want more sophisticated error handling strategies, sometimes you just need to fail. It makes no sense for some errors to be retried, either because they are not transient, or because you already tried everything to make it work and it still keeps failing. If containment is not able to handle the error, then it needs to propagate up to a parent component that can handle it.

For synchronous programs, every error is converted into an Exception and thrown so that you can use regular `begin`/`rescue` semantics.

If you do not catch the Exception, it will bubble up:

```ruby
Traceback (most recent call last):
	4: from examples/crud.rb:21:in `<main>'
	3: from lib/couchbase/cluster.rb:56:in `bucket'
	2: from lib/couchbase/cluster.rb:56:in `new'
	1: from lib/couchbase/bucket.rb:29:in `initialize'
lib/couchbase/bucket.rb:29:in `open_bucket': unable open bucket "travel-sample": bucket_not_found (Couchbase::Error::BucketNotFound)
```

### [](#logging)Logging

It is always important to log errors, but even more so in the case of reactive applications. Because of the event driven nature, stack traces get harder to look at, and caller context is sometimes lost.

Refer to the [Logging page](collecting-information-and-logging.md) for more details.

### [](#retry)Retry

Transient errors — such as those caused by resource starvation — are best tackled with one of the following retry strategies:

* Retry immediately.
* Retry with a fixed delay.
* Retry with a linearly increasing delay.
* Retry with an exponentially increasing delay.
* Retry with a random delay.

## [](#data-service)Data Service

The Data Service exposes several common errors that can be encountered — both during development, and to be handled by the production app. Here we will cover some of the most common errors.

### [](#document-does-not-exist)Document does not exist

```ruby
begin
  collection.replace("my-key", {"foo" => 42})
rescue Couchbase::Error::DocumentNotFound => ex
  # key does not exist, report and continue
  puts ex
end
```

### [](#document-already-exists)Document already exists

```ruby
begin
  collection.insert("my-key", {"foo" => 32})
rescue Couchbase::Error::DocumentExists => ex
  # key already exists, report and continue
  puts ex
end
```

### [](#document-too-large)Document too large

`Couchbase::Error::ValueTooLarge`

### [](#cas-mismatch)CAS Mismatch

```ruby
begin
  result = collection.get("my-key")
  options = Couchbase::Collection::ReplaceOptions.new
  options.cas = result.cas
  collection.replace("my-key", {"foo" => 42}, options)
rescue Couchbase::Error::CasMismatch => ex
  # the CAS value has changed
  puts ex
end
```

### [](#durability-ambiguous)Durability ambiguous

```ruby
begin
  options = Couchbase::Collection::UpsertOptions.new
  options.durability_level = :persist_to_majority
  collection.upsert("my-key", {"foo" => 42}, options)
rescue Couchbase::Error::DurabilityAmbiguous => ex
  # durable write request has not completed, it is unknown whether the request met the durability requirements or not
  puts ex
end
```

### [](#durability-invalid-level)Durability invalid level

```ruby
begin
  options = Couchbase::Collection::UpsertOptions.new
  options.durability_level = :persist_to_majority
  collection.upsert("my-key", {"foo" => 42}, options)
rescue Couchbase::Error::DurabilityLevelNotAvailable => ex
  # cluster not able to meet durability requirements
  puts ex
end
```

## [](#query-and-analytics-errors)Query and Analytics Errors

Query and Analytics either return results or an error.