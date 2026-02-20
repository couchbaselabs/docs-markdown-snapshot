---
title: Search
description: You can use the Full Text Search service (FTS) to create queryable,
  full-text indexes in Couchbase Server.
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.7/modules/howtos/pages/full-text-searching-with-sdk.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:ruby-sdk:howtos:full-text-searching-with-sdk.adoc[]
---

[View original HTML](/ruby-sdk/current/howtos/full-text-searching-with-sdk.html)

# Search

> You can use the Full Text Search service (FTS) to create queryable, full-text indexes in Couchbase Server. 

Full Text Search (FTS) — or _Search_ for short — allows you to create, manage, and query full text indexes on JSON documents stored in Couchbase buckets. It uses natural language processing for querying documents, provides relevance scoring on the results of your queries, and has fast indexes for querying a wide range of possible text searches.

Some of the supported query types include simple queries like Match and Term queries; range queries like Date Range and Numeric Range; and compound queries for conjunctions, disjunctions, and/or boolean queries.

There are two APIs for querying search: `cluster.searchQuery()`, and `cluster.search()`. Both are also available at the Scope level.

The former API supports FTS queries (`SearchQuery`), while the latter additionally supports the `VectorSearch` added in 7.6\. Most of this documentation will focus on the former API, as the latter is in @Stability.Volatile status.

## [](#index-creation)Index Creation

For the purposes of the below examples we will use the Beer Sample sample bucket. Full Text Search indexes can be [created through the UI or throuth the REST API](../../../server/current/search/create-search-indexes.md), or created programatically as follows:

```ruby
search_indexes = cluster.search_indexes.get_all_indexes
unless search_indexes.any? {|idx| idx.name == "my-index-name"}
  index = Management::SearchIndex.new
  index.type = "fulltext-index"
  index.name = "my-index-name"
  index.source_type = "couchbase"
  index.source_name = "beer-sample"
  index.params = {
      mapping: {
          default_datetime_parser: "dateTimeOptional",
          types: {
              "beer" => {
                  properties: {
                      "abv" => {
                          fields: [
                              {
                                  name: "abv",
                                  type: "number",
                                  include_in_all: true,
                                  index: true,
                                  store: true,
                                  docvalues: true,
                              }
                          ]
                      },
                      "category" => {
                          fields: [
                              {
                                  name: "category",
                                  type: "text",
                                  include_in_all: true,
                                  include_term_vectors: true,
                                  index: true,
                                  store: true,
                                  docvalues: true,
                              }
                          ]
                      },
                      "description" => {
                          fields: [
                              {
                                  name: "description",
                                  type: "text",
                                  include_in_all: true,
                                  include_term_vectors: true,
                                  index: true,
                                  store: true,
                                  docvalues: true,
                              }
                          ]
                      },
                      "name" => {
                          fields: [
                              {
                                  name: "name",
                                  type: "text",
                                  include_in_all: true,
                                  include_term_vectors: true,
                                  index: true,
                                  store: true,
                                  docvalues: true,
                              }
                          ]
                      },
                      "style" => {
                          fields: [
                              {
                                  name: "style",
                                  type: "text",
                                  include_in_all: true,
                                  include_term_vectors: true,
                                  index: true,
                                  store: true,
                                  docvalues: true,
                              }
                          ]
                      },
                      "updated" => {
                          fields: [
                              {
                                  name: "updated",
                                  type: "datetime",
                                  include_in_all: true,
                                  index: true,
                                  store: true,
                                  docvalues: true,
                              }
                          ]
                      },
                  }
              }
          }
      }
  }
  cluster.search_indexes.upsert_index(index)
  num_indexed = 0
  loop do
    sleep(1)
    num = cluster.search_indexes.get_indexed_documents_count(index.name)
    break if num_indexed == num
    num_indexed = num
    puts "#{index.name.inspect} indexed #{num_indexed}"
  end
end
```

## [](#examples)Examples

In versions of Couchbase Server starting from 7.6, Search queries are executed at either the Scope or the Cluster level; in earlier versions, they are just performed at the cluster level. (not bucket or collection).

We will perform an FTS query here - see the [\[vector search\]](#vector search) section for examples of that. Here is a simple query that looks for the text "hop beer" using the defined index:

```ruby
result = cluster.search_query(
    "my-index-name",
    Cluster::SearchQuery.query_string("hop beer")
  )
result.rows.each do |row|
  puts "id: #{row.id}, score: #{row.score}"
end
#=>
# id: great_divide_brewing-fresh_hop_pale_ale, score: 0.8361701974709099
# id: left_coast_brewing-hop_juice_double_ipa, score: 0.7902867513072585
# ...

puts "Reported total rows: #{result.meta_data.metrics.total_rows}"
#=> Reported total rows: 6043
```

`match_phrase()` builds a phrase query is built from the results of an analysis of the terms in the query phrase; here it’s built on a search in the name field.

```ruby
options = Cluster::SearchOptions.new
options.fields = ["name"]
result = cluster.search_query(
    "my-index-name",
    Cluster::SearchQuery.match_phrase("hop beer"),
    options
  )
result.rows.each do |row|
  puts "id: #{row.id}, score: #{row.score}\n  fields: #{row.fields}"
end
#=>
# id: deschutes_brewery-hop_henge_imperial_ipa, score: 0.7752384807123055
#   fields: {"name"=>"Hop Henge Imperial IPA"}
# id: harpoon_brewery_boston-glacier_harvest_09_wet_hop_100_barrel_series_28, score: 0.6862594775775723
#   fields: {"name"=>"Glacier Harvest '09 Wet Hop (100 Barrel Series #28)"}

puts "Reported total rows: #{result.meta_data.metrics.total_rows}"
# Reported total rows: 2
```

## [](#working-with-results)Working with Results

The result of a Search query has three components: rows, facets, and metdata. Rows are the documents that match the query. Facets allow the aggregation of information collected on a particular result set. Metdata holds additional information not directly related to your query, such as success, total hits, and how long the query took to execute in the cluster.

Iterating Rows

Here we are iterating over the rows that were returned in the results. Highlighting has been selected for the description field in each row, and the total number of rows is taken from the `metrics` returned in the metadata:

```ruby
options = Cluster::SearchOptions.new
options.highlight_style = :html
options.highlight_fields = ["description"]
result = cluster.search_query(
    "my-index-name",
    Cluster::SearchQuery.match_phrase("banana"),
    options
  )
result.rows.each do |row|
  puts "id: #{row.id}, score: #{row.score}"
  row.fragments.each do |field, excerpts|
    puts "  #{field}: "
    excerpts.each do |excerpt|
      puts "  * #{excerpt}"
    end
  end
end
#=>
# id: wells_and_youngs_brewing_company_ltd-wells_banana_bread_beer, score: 0.8269933841266812
# description:
#     * A silky, crisp, and rich amber-colored ale with a fluffy head and strong <mark>banana</mark> note on the nose.
# ...

puts "Reported total rows: #{result.meta_data.metrics.total_rows}"
# Reported total rows: 41
```

With `skip` and `limit` a slice of the returned data may be selected:

```ruby
options = Cluster::SearchOptions.new
options.skip = 4
options.limit = 3
result = cluster.search_query(
    "my-index-name",
    Cluster::SearchQuery.query_string("hop beer"),
    options
  )
result.rows.each do |row|
  puts "id: #{row.id}, score: #{row.score}"
end
#=>
# id: harpoon_brewery_boston-glacier_harvest_09_wet_hop_100_barrel_series_28, score: 0.6862594775775723
# id: lift_bridge_brewery-harvestor_fresh_hop_ale, score: 0.6674211556164669
# id: southern_tier_brewing_co-hop_sun, score: 0.6630296619927506

puts "Reported total rows: #{result.meta_data.metrics.total_rows}"
# Reported total rows: 6043
```

Ordering rules can be applied via `sort` and `SearchSort`:

```ruby
options = Cluster::SearchOptions.new
options.sort = [
    Cluster::SearchSort.score,
    Cluster::SearchSort.field("name"),
]
cluster.search_query(
    "my-index-name",
    Cluster::SearchQuery.match_phrase("hop beer"),
    options
  )
```

Facets

```ruby
options = Cluster::SearchOptions.new
categories_facet = Cluster::SearchFacet.term("category")
categories_facet.size = 5
options.facets = {"categories" => categories_facet}
cluster.search_query(
    "my-index-name",
    Cluster::SearchQuery.query_string("hop beer"),
    options
  )
```

## [](#scoped-vs-global-indexes)Scoped vs Global Indexes

The FTS APIs exist at both the `Cluster` and `Scope` levels.

This is because FTS supports, as of Couchbase Server 7.6, a new form of "scoped index" in addition to the traditional "global index".

It’s important to use the `Cluster.searchQuery()` / `Cluster.search()` for global indexes, and `Scope.search()` for scoped indexes.

```ruby
request = SearchRequest.new(
  SearchQuery.match('swanky')
)
result = scope.search('travel-sample-index', request)

result.rows.each do |row|
  puts "Document ID: #{row.id}, search score: #{row.score}"
end
```

The `SearchQuery` is created in the same way as detailed earlier.

## [](#consistency)Consistency

Like the [Couchbase Query Service](n1ql-queries-with-sdk.md#scan-consistency), FTS allows `consistent_with()` queries — _Read-Your-Own\_Writes (RYOW)_ consistency, ensuring results contain information from updated indexes:

```ruby
random_value = rand
result = collection.upsert("cool-beer-#{random_value}", {
    "type" => "beer",
    "name" => "Random Beer ##{random_value}",
    "description" => "The beer full of randomness"
})
mutation_state = MutationState.new(result.mutation_token)

options = Cluster::SearchOptions.new
options.fields = ["name"]
options.consistent_with(mutation_state)
result = cluster.search_query(
    "my-index-name",
    Cluster::SearchQuery.match_phrase("randomness"),
    options
  )
result.rows.each do |row|
  puts "id: #{row.id}, score: #{row.score}\n  fields: #{row.fields}"
end
#=>
# id: cool-beer-0.4332638785378332, score: 2.6573492057051666
#   fields: {"name"=>"Random Beer #0.4332638785378332"}

puts "Reported total rows: #{result.meta_data.metrics.total_rows}"
# Reported total rows: 1
```