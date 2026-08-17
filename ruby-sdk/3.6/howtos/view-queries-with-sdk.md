---
title: MapReduce Views
description: You can use MapReduce views to create queryable indexes in
  Couchbase Data Platform.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.6/modules/howtos/pages/view-queries-with-sdk.adoc
  xref: xref:3.6@ruby-sdk:howtos:view-queries-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/3.6/howtos/view-queries-with-sdk.html)

# MapReduce Views

> You can use MapReduce views to create queryable indexes in Couchbase Data Platform. 

> [!CAUTION]
> Although still maintained and supported for legacy use, Views date from the earliest days of Couchbase Server development, and as such are rarely the best choice over, say, [our Query service](n1ql-queries-with-sdk.md) if you are starting a fresh application. See our discussion document on [the best service for you to use](../concept-docs/data-services.md).
> 
> Note, if you are provisioning Views on Couchbase Server for a legacy application, _they must run on a [couchstore](#7.6.6@server:learn:buckets-memory-and-storage/storage-engines.adoc#couchstore) bucket_.

The normal CRUD methods allow you to look up a document by its ID. A MapReduce (_view_ query) allows you to lookup one or more documents based on various criteria. MapReduce views are comprised of a _map_ function that is executed once per document (this is done incrementally, so this is not run each time you query the view) and an optional _reduce_ function that performs aggregation on the results of the _map_ function. The _map_ and _reduce_ functions are stored on the server and written in JavaScript.

MapReduce queries can be further customized during query time to allow only a subset (or range) of the data to be returned.

> [!TIP]
> See the [Incremental MapReduce Views](#7.1@server:learn:views/views-writing.adoc) and [Querying Data with Views](#7.1@server:learn:views/views-querying.adoc) sections of the general documentation to learn more about views and their architecture.

## [](#querying-views)Querying Views

Once you have a view defined, it can be queried from the Ruby SDK by using the `view_query` method on a `Bucket` instance.

Here is an example:

```ruby
bucket = cluster.bucket("beer-sample")

options = Bucket::ViewOptions.new
options.limit = 5
view_result = bucket.view_query("beer", "brewery_beers", options)
view_result.rows.each do |row|
  puts "key: #{row.id}, id: #{row.id}"
end
#=>
# key: 21st_amendment_brewery_cafe, id: 21st_amendment_brewery_cafe
# key: 21st_amendment_brewery_cafe-21a_ipa, id: 21st_amendment_brewery_cafe-21a_ipa
# key: 21st_amendment_brewery_cafe-563_stout, id: 21st_amendment_brewery_cafe-563_stout
# key: 21st_amendment_brewery_cafe-amendment_pale_ale, id: 21st_amendment_brewery_cafe-amendment_pale_ale
# key: 21st_amendment_brewery_cafe-bitter_american, id: 21st_amendment_brewery_cafe-bitter_american

puts "Total rows: #{view_result.meta_data.total_rows}"
#=> Total rows: 7303
```

## [](#metadata)MetaData

The `meta_data` returned with the results can be used to show the total number of results, and various debug info:

```ruby
options = Bucket::ViewOptions.new
options.limit = 5
options.debug = true
view_result = bucket.view_query("beer", "brewery_beers", options)
puts "Total rows: #{view_result.meta_data.total_rows}"
#=> Total rows: 7303
puts "Debug info present: #{view_result.meta_data.debug_info.is_a?(Hash)}"
#=> Debug info present: true
```

For more details, see the [API reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Bucket/ViewMetaData.html).