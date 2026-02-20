---
title: Sample Application
description: Discover how to program interactions with the Couchbase Server via
  the data, Query, and search services -- using the Travel Sample Application
  with the built-in Travel Sample data Bucket.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.9/modules/hello-world/pages/sample-application.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:2.9@go-sdk:hello-world:sample-application.adoc[]
---

[View original HTML](/go-sdk/2.9/hello-world/sample-application.html)

# Sample Application

> Discover how to program interactions with the Couchbase Server via the data, Query, and search services — using the Travel Sample Application with the built-in Travel Sample data Bucket. 

## [](#quick-start)Quick Start

Fetch the [Couchbase Go SDK travel-sample Application REST Backend](https://github.com/couchbaselabs/try-cb-golang) from github:

```console
git clone https://github.com/couchbaselabs/try-cb-golang.git
cd try-cb-golang
```

With [Docker](https://docs.docker.com/get-docker/) installed, you should now be able to run a bare-bones copy of Couchbase Server, load the travel-sample, add indexes, install the sample-application and its frontend, all by running a single command:

```console
docker-compose --profile local up
```

## [](#running-the-code-against-your-own-development-couchbase-server)Running the code against your own development Couchbase server.

For Couchbase Server 7.6, make sure that you have at least one node each of data; query; index; and search. For a development box, mixing more than one of these on a single node (given enough memory resources) is perfectly acceptable.

If you have yet to install Couchbase Server in your development environment [start here](#7.1@server:getting-started:do-a-quick-install.adoc).

Then load up the Travel Sample Bucket, using either the [Web interface](#7.1@server:manage:manage-settings/install-sample-buckets.adoc#install-sample-buckets-with-the-ui)or the [command line](#7.1@server:manage:manage-settings/install-sample-buckets.adoc#install-sample-buckets-with-the-cli). You will also need to [create a Search Index](#7.1@server:fts:fts-searching-from-the-ui.adoc#create-an-index) — Query indexes are taken care of by the Sample Bucket.

See the README at <https://github.com/couchbaselabs/try-cb-golang> for full details of how to run and tweak the Go SDK travel-sample app.

## [](#using-the-sample-app)Using the Sample App

![Travel Sample Register](../../../sdk/current/shared/_images/Travel-Sample-Register.png) 

Give yourself a username and password and click **Register**.

You can now try out searching for flights, booking flights, and searching for hotels. You can see which Couchbase SDK operations are being executed by clicking the red bar at the bottom of the screen:

![Couchbase Query Bar](../../../sdk/current/shared/_images/Couchbase-Query-Bar.png) 

## [](#sample-app-backend)Sample App Backend

The backend code shows Couchbase Go SDK in action with Query and Search, but also how to plug together all of the elements and build an application with Couchbase Server and the Go SDK.

Here’s the Search code, where `AirportSearch` checks to see whether the search term is a three or four letter FAA or ICAO abbreviation, and if not searches for it as an airport name:

```golang
func AirportSearch(w http.ResponseWriter, req *http.Request) {
	var respData jsonAirportSearchResp

	searchKey := req.FormValue("search")

	var queryStr string
	if len(searchKey) == 3 {
		queryStr = fmt.Sprintf("SELECT airportname FROM `travel-sample` WHERE faa='%s'", strings.ToUpper(searchKey))
	} else if len(searchKey) == 4 && searchKey == strings.ToUpper(searchKey) {
		queryStr = fmt.Sprintf("SELECT airportname FROM `travel-sample` WHERE icao ='%s'", searchKey)
	} else {
		queryStr = fmt.Sprintf("SELECT airportname FROM `travel-sample` WHERE airportname like '%s%%'", searchKey)
	}

	respData.Context.Add(queryStr)
	rows, err := globalCluster.Query(queryStr, nil)
	if err != nil {
		writeJsonFailure(w, 500, err)
		return
	}

	respData.Data = []jsonAirport{}
	var airport jsonAirport
	for rows.Next(&airport) {
		respData.Data = append(respData.Data, airport)
		airport = jsonAirport{}
	}

	encodeRespOrFail(w, respData)
}
```

The [main.go](https://github.com/couchbaselabs/try-cb-golang/blob/HEAD/main.go) file also contains the functions for handling users, registration, and [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) queries.

## [](#data-model)Data Model

See the [Travel App Data Model](../ref/travel-app-data-model.md) reference page for more information about the sample data set used.

## [](#rest-api)REST API

You can explore the REST API here in read-only mode, or once you are running the application, at the `/apidocs` endpoint.