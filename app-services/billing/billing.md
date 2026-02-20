---
title: Billing
description: The cost for App Services is based on the cost of the linked
  Cluster, and comprises a fixed cost, plus a variable amount based on the data
  usage.
editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/billing/billing.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:app-services::billing/billing.adoc[]
---

[View original HTML](/app-services/billing/billing.html)

# Billing

> The cost for App Services is based on the cost of the linked Cluster, and comprises a fixed cost, plus a variable amount based on the data usage. 

## [](#how-your-app-services-bill-is-calculated)How Your App Services Bill is Calculated

The cost of App Services is dependent on the cost of the linked Cluster, and varies depending on region.

Couchbase charges by the clock hour for each hour that Capella App Services are provisioned. The hourly rate for App Services is based on:

* The cloud service provider and region where the App Service is deployed.
* The size of an App Service, determined by:

  * Number of nodes
  * Number of vCPUs
  * Amount of RAM
* A single load balancer per each App Service.

After you deploy an App Service and it enters a running state, it becomes billable. Couchbase also charges for App Services based on a variable amount of the data processed through the App Services load balancer.

The first 1GiB of data processing per clock hour is not charged.

App Services are not billed when they’re turned off.