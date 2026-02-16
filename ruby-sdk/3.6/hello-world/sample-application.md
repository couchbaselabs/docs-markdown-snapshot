[View original HTML](/ruby-sdk/3.6/hello-world/sample-application.html)

> Discover how to program interactions with the Couchbase Server via the Data, Query, and Search services — using the Travel Sample Application with the built-in Travel Sample data Bucket. 

## [](#quick-start)Quick Start

Fetch the [Couchbase Ruby SDK travel-sample Application REST Backend](https://github.com/couchbaselabs/try-cb-ruby) from github:

```console
git clone https://github.com/couchbaselabs/try-cb-ruby.git
cd try-cb-ruby
```

With [Docker](https://docs.docker.com/get-docker/) installed, you should now be able to run a bare-bones copy of Couchbase Server, load the travel-sample, add indexes, install the sample-application and its frontend, all by running a single command:

```console
docker-compose --profile local up
```

## [](#running-the-code-against-your-own-development-couchbase-server)Running the code against your own development Couchbase server.

For Couchbase Server 7.6, make sure that you have at least one node each of data; query; index; and search. For a development box, mixing more than one of these on a single node (given enough memory resources) is perfectly acceptable.

If you have yet to install Couchbase Server in your development environment [start here](#7.1@server:getting-started:do-a-quick-install.adoc).

Then load up the Travel Sample Bucket, using either the [Web interface](#7.1@server:manage:manage-settings/install-sample-buckets.adoc#install-sample-buckets-with-the-ui)or the [command line](#7.1@server:manage:manage-settings/install-sample-buckets.adoc#install-sample-buckets-with-the-cli). You will also need to [create a Search Index](#7.1@server:fts:fts-searching-from-the-ui.adoc#create-an-index) — Query indexes are taken care of by the Sample Bucket.

See the README at <https://github.com/couchbaselabs/try-cb-ruby> for full details of how to run and tweak the Ruby SDK travel-sample app.

## [](#using-the-sample-app)Using the Sample App

![Travel Sample Register](../../../sdk/current/shared/_images/Travel-Sample-Register.png) 

Give yourself a username and password and click **Register**.

You can now try out searching for flights, booking flights, and searching for hotels. You can see which Couchbase SDK operations are being executed by clicking the red bar at the bottom of the screen:

![Couchbase Query Bar](../../../sdk/current/shared/_images/Couchbase-Query-Bar.png) 

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

## [](#data-model)Data Model

See the [Travel App Data Model](../ref/travel-app-data-model.md) reference page for more information about the sample data set used.

## [](#rest-api)REST API

You can explore the REST API here in read-only mode, or once you are running the application, at the `/apidocs` endpoint.