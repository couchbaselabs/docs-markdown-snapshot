[View original HTML](/ruby-sdk/3.5/howtos/view-queries-with-sdk.html)

> You can use MapReduce views to create queryable indexes in Couchbase Data Platform. 

Unresolved include directive in modules/howtos/pages/view-queries-with-sdk.adoc - include::7.5@sdk:shared:partial$views.adoc\[\]

Unresolved include directive in modules/howtos/pages/view-queries-with-sdk.adoc - include::7.5@sdk:shared:partial$views.adoc\[\]

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