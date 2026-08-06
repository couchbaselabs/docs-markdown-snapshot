---
title: Sample Application
description: Discover how to program interactions with the Couchbase Server via
  the Data, Query, and Search services -- using the Travel Sample Application
  with the built-in Travel Sample data Bucket.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.4/modules/hello-world/pages/sample-application.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:4.4@php-sdk:hello-world:sample-application.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/php-sdk/4.4/hello-world/sample-application.html)

# Sample Application

> Discover how to program interactions with the Couchbase Server via the Data, Query, and Search services — using the Travel Sample Application with the built-in Travel Sample data Bucket. 

## [](#quick-start)Quick Start

Fetch the [Couchbase PHP SDK travel-sample Application REST Backend](https://github.com/couchbaselabs/try-cb-php) from github:

```console
git clone https://github.com/couchbaselabs/try-cb-php.git
cd try-cb-php
```

With [Docker](https://docs.docker.com/get-docker/) installed, you should now be able to run a bare-bones copy of Couchbase Server, load the travel-sample, add indexes, install the sample-application and its frontend, all by running a single command:

```console
docker-compose --profile local up
```

## [](#running-the-code-against-your-own-development-couchbase-server)Running the code against your own development Couchbase server.

For Couchbase Server 8.0, make sure that you have at least one node each of data; query; index; and search. For a development box, mixing more than one of these on a single node (given enough memory resources) is perfectly acceptable.

If you have yet to install Couchbase Server in your development environment [start here](../../../server/current/getting-started/do-a-quick-install.md).

Then load up the Travel Sample Bucket, using either the [Web interface](../../../server/current/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui)or the [command line](../../../server/current/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-cli). You will also need to [create a Search Index](#8.0@server:fts:fts-searching-from-the-ui.adoc#create-an-index) — Query indexes are taken care of by the Sample Bucket.

See the README at <https://github.com/couchbaselabs/try-cb-php> for full details of how to run and tweak the PHP SDK travel-sample app.

## [](#using-the-sample-app)Using the Sample App

![Travel Sample Register](../../../sdk/current/shared/_images/Travel-Sample-Register.png) 

Give yourself a username and password and click **Register**.

You can now try out searching for flights, booking flights, and searching for hotels. You can see which Couchbase SDK operations are being executed by clicking the red bar at the bottom of the screen:

![Couchbase Query Bar](../../../sdk/current/shared/_images/Couchbase-Query-Bar.png) 

## [](#data-model)Data Model

See the [Travel App Data Model](../ref/travel-app-data-model.md) reference page for more information about the sample data set used.

## [](#rest-api)REST API

You can explore the REST API here in read-only mode, or once you are running the application, at the `/apidocs` endpoint.