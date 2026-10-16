---
title: Sample Application
description: Discover how to program interactions with the Couchbase Server via
  the data, query, and search services -- using the Travel Sample Application
  with the built-in Travel Sample data Bucket.
pubDate: 2026-10-16T07:26:40.932Z
meta:
  component:
    title: Scala SDK
    version: "3.13"
antora:
  editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.13/modules/hello-world/pages/sample-application.adoc
  xref: xref:scala-sdk:hello-world:sample-application.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/current/hello-world/sample-application.html)

# Sample Application

> Discover how to program interactions with the Couchbase Server via the data, query, and search services — using the Travel Sample Application with the built-in Travel Sample data Bucket. Discover how to program interactions with Couchbase via the Data, Query, and Search services. 

## [](#sample-app-backend)Sample App Backend

The backend code shows Couchbase Scala SDK in action with Query and Search, but also how to plug together all of the elements and build an application with Couchbase Server and the Scala SDK.

The [app directory](https://github.com/couchbaselabs/try-cb-scala/tree/HEAD/app) contains the various components, classes and functions for handling users, registration, and SQL++ (formerly N1QL) queries.

For this quickstart, we use three collections, `airport`, `airline` and `routes` that contain sample airports, airlines and airline routes respectively. The routes collection connects the airports and airlines as seen in the figure below. We use these connections in the quickstart to generate airports that are directly connected and airlines connecting to a destination airport. Note that these are just examples to highlight how you can use SQL++ queries to join the collections.

![travel-sample data model](ref:image$travel_sample_data_model.png) 

## [](#rest-api)REST API

You can explore the REST API here in read-only mode, or once you are running the application, at the `/apidocs` endpoint.