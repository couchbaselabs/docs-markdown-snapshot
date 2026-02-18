---
title: Sample Application
description: Discover how to program interactions with the Couchbase Server via
  the Data, Query, and Search services -- using the Travel Sample Application
  with the built-in Travel Sample data Bucket.
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.5/modules/hello-world/pages/sample-application.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/ruby-sdk/3.5/hello-world/sample-application.html)

# Sample Application

Unresolved include directive in modules/hello-world/pages/sample-application.adoc - include::7.5@sdk:shared:partial$sample-application.adoc\[\]

Unresolved include directive in modules/hello-world/pages/sample-application.adoc - include::7.5@sdk:shared:partial$sample-application.adoc\[\]

Unresolved include directive in modules/hello-world/pages/sample-application.adoc - include::7.5@sdk:shared:partial$sample-application.adoc\[\]

Unresolved include directive in modules/hello-world/pages/sample-application.adoc - include::7.5@sdk:shared:partial$sample-application.adoc\[\]

## [](#sample-app-backend)Sample App Backend

The backend code shows Couchbase Ruby SDK in action with Query and Search, but also how to plug together all of the elements and build an application with Couchbase Server and the Ruby SDK.

Here’s the airport search code, which checks to see whether the search term for the query string is a three or four letter FAA or ICAO abbreviation, and if not searches for it as an airport name:

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

Unresolved include directive in modules/hello-world/pages/sample-application.adoc - include::7.5@sdk:shared:partial$sample-application.adoc\[\]

## [](#rest-api)REST API

You can explore the REST API here in read-only mode, or once you are running the application, at the `/apidocs` endpoint.