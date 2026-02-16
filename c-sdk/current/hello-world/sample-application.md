[View original HTML](/c-sdk/current/hello-world/sample-application.html)

> Discover how to program interactions with the Couchbase Server via the data, query, and search services — using the Travel Sample Application with the built-in Travel Sample data Bucket. 

> Discover how to program interactions with the Couchbase Server via the data, query, and search services — using the Travel Sample Application with the built-in Travel Sample data Bucket. 

## [](#quick-start)Quick Start

Fetch the [Couchbase C SDK travel-sample Application REST Backend](https://github.com/couchbaselabs/try-cb-lcb) from github:

```console
git clone https://github.com/couchbaselabs/try-cb-lcb.git
cd try-cb-lcb
```

With [Docker](https://docs.docker.com/get-docker/) installed, you should now be able to run a bare-bones copy of Couchbase Server, load the travel-sample, add indexes, install the sample-application and its frontend, all by running a single command:

```console
docker-compose --profile local up
```

## [](#running-the-code-against-your-own-development-couchbase-server)Running the code against your own development Couchbase server.

For Couchbase Server 8.0, make sure that you have at least one node each of data; query; index; and search. For a development box, mixing more than one of these on a single node (given enough memory resources) is perfectly acceptable.

If you have yet to install Couchbase Server in your development environment [start here](../../../server/current/getting-started/do-a-quick-install.md).

Then load up the Travel Sample Bucket, using either the [Web interface](../../../server/current/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui)or the [command line](../../../server/current/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-cli). You will also need to [create a Search Index](#8.0@server:fts:fts-searching-from-the-ui.adoc#create-an-index) — Query indexes are taken care of by the Sample Bucket.

See the README at <https://github.com/couchbaselabs/try-cb-lcb> for full details of how to run and tweak the C SDK travel-sample app.

## [](#using-the-sample-app)Using the Sample App

![Travel Sample Register](../../../sdk/current/shared/_images/Travel-Sample-Register.png) 

Give yourself a username and password and click **Register**.

You can now try out searching for flights, booking flights, and searching for hotels. You can see which Couchbase SDK operations are being executed by clicking the red bar at the bottom of the screen:

![Couchbase Query Bar](../../../sdk/current/shared/_images/Couchbase-Query-Bar.png) 

## [](#sample-app-backend)Sample App Backend

The backend code shows `libcouchbase` in action with Query and Search, but also how to plug together all of the elements and build an application with Couchbase Server and the C SDK.

To start exploring the codebase, look at the [try-cb-lcb.conf](https://github.com/couchbaselabs/try-cb-lcb/blob/master/conf/try-cb-lcb.conf) configuration for the route mappings, and try finding the definitions in the C sources in the [src/](https://github.com/couchbaselabs/try-cb-lcb/tree/master/src) directory.

For example, this snippet of the config:

route  /api/airports  tcblcb_api_airports

is defined in [api-airports.c](https://github.com/couchbaselabs/try-cb-lcb/blob/master/src/api-airports.c#L74)

Other files contain the functions for handling users, registration, and SQL++ (formerly N1QL) queries.

## [](#data-model)Data Model

See the [Travel App Data Model](../ref/travel-app-data-model.md) reference page for more information about the sample data set used.

## [](#rest-api)REST API

You can explore the REST API here in read-only mode.