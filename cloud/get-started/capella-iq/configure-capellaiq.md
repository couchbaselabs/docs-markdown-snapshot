---
title: Configure Capella iQ
description: Capella iQ harnesses the power of a third-party large language
  model (LLM) to improve your queries. You can turn this tool on or off for your
  organization.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/get-started/pages/capella-iq/configure-capellaiq.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:get-started:capella-iq/configure-capellaiq.adoc[]
---

[View original HTML](/cloud/get-started/capella-iq/configure-capellaiq.html)

# Configure Capella iQ

> Capella iQ harnesses the power of a third-party large language model (LLM) to improve your queries. You can turn this tool on or off for your organization. 

## [](#prerequisites)Prerequisites

You must have the [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner) role to accept Capella iQ’s supplemental terms and turn it on or off.

### [](#T&C)Accept Capella iQ Supplemental Terms

Before anyone in an organization can use Capella iQ, an [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner) must accept the Capella Supplemental Terms. If the terms are not yet accepted, the iQ button is still visible in query editor. In this state, when users without the `Organization Owner` role click the iQ button, they’re informed that Capella iQ is disabled. If a user with the `Organization Owner` role clicks the iQ button, they can instead review and accept the terms for the current organization.

1. In the [query editor](../../clusters/query-service/query-workbench.md) in Capella’s Data Tools, click **iQ**.
2. In the prompt, review and accept the [Capella iQ Supplemental Terms](https://www.couchbase.com/iQ-terms/).
3. Click **Continue**.  
Capella iQ is now available to all your organization’s users, who can use it with all of your organization’s clusters.

> [!NOTE]
> Accepting the terms for Capella iQ enables iQ for both operational clusters and [Capella Analytics clusters](../../../analytics/intro/intro.md). While iQ helps you write SQL++ queries in an operational cluster, iQ for Capella Analytics helps you write [SQL++ for Capella Analytics queries and statements](../../../analytics/sqlpp/1%5Fintro.md).

### [](#turn-capella-iq-off-for-your-organization)Turn Capella iQ Off for Your Organization

Capella iQ is on by default and you control it at the organization level. To turn Capella iQ on or off for your organization, you need to navigate to your organization’s general settings page:

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **Settings** **General**.
3. Select or deselect **Enable Capella iQ** and click **Save**.  
If Capella iQ is turned off for an organization the iQ button is still visible in the query editor. Any user who clicks this button sees a message that Capella iQ is disabled.

> [!CAUTION]
> When you disable Capella iQ, you also disable [iQ Insights](explore-iq-insights.md).

## [](#next-steps)Next Steps

* [Get Started with Capella iQ](get-started-with-iq.md)