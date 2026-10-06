---
title: Welcome to Capella App Services
description: App Services is a fully managed application backend that
  synchronizes data between Capella and your mobile and IoT apps, with low
  latency, data integrity, and high availability. Pair it with Couchbase Lite to
  build offline-first apps that keep working without a network connection and
  sync their changes to Capella when the connection returns.
pubDate: 2026-10-06T04:29:29.001Z
meta:
  component:
    title: Capella App Services
    version: ""
antora:
  editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/index.adoc
  xref: xref:app-services::index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/index.html)

# Welcome to Capella App Services

# Welcome to Capella App Services

App Services is a fully managed application backend that synchronizes data between Capella and your mobile and IoT apps, with low latency, data integrity, and high availability. Pair it with Couchbase Lite to build offline-first apps that keep working without a network connection and sync their changes to Capella when the connection returns.

## How Do You Want To Start Building Today?

###  Get Started With App Services

Deploy an App Service, create an App Endpoint, and sync your first app.

* [Sign Up](https://cloud.couchbase.com/sign-up)
* [Configure Free Tier App Services](get-started/configuring-app-services.md)
* [Create an App Service](app-services/creating-an-app-service.md)
* [Create an App Endpoint](app-endpoints/creating-an-app-endpoint.md)
* [Connect your Apps to an App Endpoint](app-endpoints/connect-apps-to-endpoint.md)

###  Sync Data With App Endpoints

Link your buckets, scopes, and collections to an App Endpoint and control how data syncs to your apps.

* [About App Endpoints](app-endpoints/about-app-endpoints.md)
* [Advanced Settings for App Endpoints](app-endpoints/advanced-settings.md)
* [Delta Sync](app-endpoints/delta-sync.md)
* [Import Filters](app-endpoints/import-filters.md)
* [Resync your App Endpoint](app-endpoints/resync.md)

###  Manage Access And Security

Control which users can connect, and which documents each user can read and write.

* [About Access Control](app-endpoints/about-access-control.md)
* [Access Control and Data Validation](app-endpoints/access-control-data-validation.md)
* [Create App Users](security/create-user.md)
* [Create App Roles](security/create-app-role.md)
* [Add Security with Channels](security/channels.md)
* [Set Up an Authentication Provider](security/set-up-authentication-provider.md)
* [Private Endpoints for App Services](private-endpoints/app-services-private-endpoints.md)

###  Monitor And Scale

Track the health of your App Services and size them to match your workload.

* [Monitor through the UI](monitoring/monitoring-in-ui.md)
* [Alert Integrations for App Services](monitoring/alert-integration.md)
* [Log Streaming](monitoring/log-streaming.md)
* [Audit Logging](monitoring/audit-logging.md)
* [Scale a Deployed App Service](app-services/scaling-a-deployed-app-service.md)
* [Turn App Services Off or On](app-services/turn-on-off.md)

###  Develop With App Services

Build your apps with the Couchbase Lite SDKs, and automate your deployments with the REST APIs.

* [Couchbase Lite SDKs](../couchbase-lite/current/index.md)
* [REST API Introduction](references/rest-api-introduction.md)
* [Manage Deployments with the Capella App Services Management API](management-api-guide/management-api-intro.md)
* [Grant Admin Access to REST APIs](app-services/accessing-admin-apis.md)

###  Migrate And Upgrade

Move from self-managed Sync Gateway to App Services, and keep your deployment up to date.

* [Migrate from Self-Managed Servers](migrating/on-prem-to-capella.md)
* [Upgrade App Services](maintenance/upgrading-app-services.md)
* [Sync Metadata Isolation](migrating/migrate-sync-metadata.md)
* [App Services Billing](billing/billing.md)
* [Capella App Services Release Notes](release-notes/release-notes.md)