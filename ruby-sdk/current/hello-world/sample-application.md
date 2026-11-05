---
title: Sample Application
description: Discover how to program interactions with the Couchbase Server via
  the Data, Query, and Search services -- using the Travel Sample Application
  with the built-in Travel Sample data Bucket.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Ruby SDK
    version: "3.9"
  topic_type: tutorial
antora:
  editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/release/3.9/modules/hello-world/pages/sample-application.adoc
  xref: xref:ruby-sdk:hello-world:sample-application.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/current/hello-world/sample-application.html)

# Sample Application

> Discover how to program interactions with the Couchbase Server via the Data, Query, and Search services — using the Travel Sample Application with the built-in Travel Sample data Bucket. Discover how to program interactions with Couchbase via the Data, Query, and Search services. 

## [](#sample-app-backend)Sample App Backend

The backend code shows Couchbase Ruby SDK in action with Query and Search, but also how to plug together all of the elements and build an application with Couchbase Server and the Ruby SDK.

Here's the airport search code, which checks to see whether the search term for the query string is a three or four letter FAA or ICAO abbreviation, and if not searches for it as an airport name:

```ruby
def get_airports(search_param)
  query_type = 'N1QL query - scoped to inventory: '

  query_prep = 'SELECT airportname FROM `travel-sample`.inventory.airport WHERE '

  same_case = search_param == search_param.downcase || search_param == search_param.upcase
  if same_case && search_param.length == 3
    query_prep += "faa=?"
    query_args = [search_param.upcase]
  elsif same_case && search_param.length == 4
    query_prep += "icao=?"
    query_args = [search_param.upcase]
  else
    query_prep += "POSITION(LOWER(airportname), ?) = 0"
    query_args = [search_param.downcase]
  end

  airport_list = []
  options = Cluster::QueryOptions.new
  options.positional_parameters(query_args)

  res = @cluster.query(query_prep, options)
  res.rows.each do |row|
    airport_list.push('airportname' => row['airportname'])
  end

  { 'context' => ["#{query_type} #{query_prep}"], 'data' => airport_list }
end
```

The [travel.rb](https://github.com/couchbaselabs/try-cb-ruby/blob/HEAD/travel.rb) file also contains the functions for handling users, registration, and SQL++ queries.

For this quickstart, we use three collections, `airport`, `airline` and `routes` that contain sample airports, airlines and airline routes respectively. The routes collection connects the airports and airlines as seen in the figure below. We use these connections in the quickstart to generate airports that are directly connected and airlines connecting to a destination airport. Note that these are just examples to highlight how you can use SQL++ queries to join the collections.

![travel-sample data model](ref:image$travel_sample_data_model.png) 

## [](#rest-api)REST API

You can explore the REST API here in read-only mode, or once you are running the application, at the `/apidocs` endpoint.