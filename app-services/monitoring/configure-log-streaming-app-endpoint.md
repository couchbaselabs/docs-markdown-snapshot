---
title: Configure Log Streaming for an App Endpoint
description: Enhance your App Services log streaming with a granular set of Log
  Filters and Levels for each App Endpoint.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/monitoring/configure-log-streaming-app-endpoint.adoc
  xref: xref:app-services::monitoring/configure-log-streaming-app-endpoint.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/monitoring/configure-log-streaming-app-endpoint.html)

# Configure Log Streaming for an App Endpoint

> Enhance your App Services log streaming with a granular set of Log Filters and Levels for each App Endpoint. 

This page describes how to configure log streaming for App Endpoints using the Capella UI. To configure log streaming programmatically using the Management API, see [Manage Log Streaming with the Management API](manage-log-streaming.md).

## [](#app-endpoint-level-config)App Endpoint Level Config

You can configure Log Streaming on a per-App Endpoint basis. This allows you to choose a more granular configuration of Log Filters and Log Levels than the preset default for the App Service.

Changing configuration of Log Level or Log Filters causes your App Endpoint to go offline briefly. This can result in temporary downtime for client applications.

> [!TIP]
> Schedule your updates to log streaming configuration to coincide with maintenance windows or periods of low activity, to reduce the impact on client connectivity.

### [](#log-levels)Log Levels

Log levels are inclusive, meaning e.g. the default Info level includes the information at the lower Warning and Error levels.

Info (_default_)

Logs messages about normal operations. Includes details on application level errors (such as HTTP 404, HTTP 403) that may merit user intervention, depending on the user's application design.

Warning

Logs warning messages. In Capella, warning messages are system related warnings that are very likely to be handled automatically by Capella itself and do not need end user intervention.

Error

Logs error messages. In Capella, error messages are system related warnings that are very likely to be handled automatically by Capella itself and do not need end user intervention..

See the [Filtering](#filtering) section for finer grained control of the log stream.

## [](#filtering)Filtering

The preset App Service configuration includes a number of default filters, which will suit most general needs.

Enabling additional filters will generally result in a larger volume of logs streamed, which will incur higher egress charges.

The Log Filters are as follows:

Admin

Logs about admin processes in App Services.

Auth

Logs about any authentication processes in App Services.

Bucket

Logs related to App Services bucket interactions.

Cache _(default)_

Logs related to App Services in-memory channel cache.

Changes _(default)_

Logs related to processing `/{db}/_changes` requests.

CRUD _(default)_

Logs about document updates, made by App Services.

DCP

Logs related to DCP processing.

Events

Logs related to event processing through App Services webhooks.

HTTP _(default)_

Logs for all requests made to the App Services REST API.

HTTP+ _(default)_

Additional information about HTTP logs (response times, status codes).

Import

Logs related to document imports.

JavaScript

Logs for any JavaScript functions, running in App Services.

Query _(default)_

Logs about SQL++ queries in App Services.

Sync

Logs for any sync activity between Couchbase Lite clients and App Services.

SyncMsg

Additional information about Sync logs.

> [!TIP]
> Only enable non-default filters per-App Endpoint to cover specific observability and troubleshooting needs.