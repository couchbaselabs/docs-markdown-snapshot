---
title: About Billing Alerts
description: Couchbase Capella billing alerts notify you about important
  information related to your usage and billing for operational clusters.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/billing/pages/about-billing-alerts.adoc
pubDate: 2026-03-24T03:43:23.693Z
link: xref:cloud:billing:about-billing-alerts.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/billing/about-billing-alerts.html)

# About Billing Alerts

> Couchbase Capella billing alerts notify you about important information related to your usage and billing for operational clusters. 

When you [upgrade your account with a prepaid credit purchase](upgrade-account.md) or purchase additional prepaid credits for your organization, Capella automatically creates [\[default-alerts\]](#default-alerts). You can also [create and manage your own custom alerts](manage-billing-alerts.md).

> [!NOTE]
> Alert timing
> 
> Alerts can be delayed by up to a day after usage meets alerting conditions.

## [](#default-billing-alerts)Default Billing Alerts

Capella automatically creates default billing alerts when you [upgrade your account with a prepaid credit purchase](upgrade-account.md) or purchase additional prepaid credits.

Capella does not create default alerts if you:

* Choose to use [pay-as-you-go](billing.md#pay-as-you-go-credits) for your usage.
* Purchase Capella credits through your [cloud service provider](billing.md#marketplaces).
* Upgrade your account by [adding a credit card](billing.md#credit-cards).

These default billing alerts are sent to the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner):

| Alert Type                                | Condition                                                                         | Description                                                                                                                                                        |
| ----------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Available credits go below**            | <5% of purchased credit balance for each [Support Plan](billing.md#support-plans) | Capella will send an alert when the available pre-paid credit balance for any of your Support Plans is less than 5% of your total purchased credits for that plan. |
| **Pay as you go usage exceeds threshold** | $10 of pay-as-you-go usage                                                        | Capella will send a daily alert if pay-as-you-go usage exceeds $10.                                                                                                |

You can modify or delete these alerts at any time.

## [](#alert-conditions)Custom Alert Conditions

The following conditions are available for creating custom billing alerts:

| Condition                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Available credits go below        | Sends an alert when the available credits in a specific Capella plan go below a specific credit threshold. When you create an alert with the **Available credits go below** condition, you must also set a **Credit Threshold** and select one of the **Basic**, **Developer Pro**, or **Enterprise** plans.                                                                                                                                                                                         |
| No available credits              | Sends an alert when a specific plan runs out of available credits. When you create an alert with the **No available credits** condition, you must also select one of the **Basic**, **Developer Pro**, or **Enterprise** plans.                                                                                                                                                                                                                                                                      |
| Pay as you go usage goes above    | Sends an alert when your organization’s pay-as-you-go usage exceeds a specific amount either daily or monthly. When you create an alert with the **Pay as you go usage goes above** condition, you must also set an **On-demand Threshold** and select one of the **Daily** or **Monthly** frequencies. By default, when you add a credit card to your organization, Capella creates a **Pay as you go usage goes above** alert with an **On-demand Threshold** of $1000 on a **Monthly** frequency. |
| Credit card payment processed     | Sends an alert when a credit card payment has been processed for your organization’s usage. This alert is created by default when you add a credit card to your organization.                                                                                                                                                                                                                                                                                                                        |
| Credit card payment declined      | Sends an alert when a credit card payment was declined. This alert is created by default when you add a credit card to your organization.                                                                                                                                                                                                                                                                                                                                                            |
| Default credit card expiring soon | Sends an alert when the default credit card in your organization is going to expire within the next month and week, and on the following day. [Add a new credit card](manage-billing.md#add-saved-cc) or [update your card’s expiration date](manage-billing.md#edit-saved-cc) to keep your organization’s paid clusters and services. This alert is created by default when you add a credit card to your organization.                                                                             |
| Default credit card expired       | Sends an alert when the default credit card in your organization has expired. [Add a new credit card](manage-billing.md#add-saved-cc) or [update your card’s expiration date](manage-billing.md#edit-saved-cc) to keep your organization’s paid clusters and services. This alert is created by default when you add a credit card to your organization.                                                                                                                                             |

## [](#alert-recipients)Alert Recipients

The following recipients are available for billing alerts:

| Recipient                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Organization Role            | Sends an alert to all users with the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner), [Project Creator](../organizations/organization-user-roles.md#organization-role-project-creator), or [Organization Member](../organizations/organization-user-roles.md#organization-role-member) role in your organization. You can choose multiple roles to receive the alert. |
| User                         | Sends an alert to specific Capella users by email address.                                                                                                                                                                                                                                                                                                                                                                   |
| All Users in My Organization | Sends an alert to all current users in your organization.                                                                                                                                                                                                                                                                                                                                                                    |

## [](#see-also)See Also

* [Manage Billing Alerts](manage-billing-alerts.md)
* [Manage Your Billing](billing.md)
* [Manage Billing Information](manage-billing.md)
* [View Capella Usage and Invoices](usage-invoices.md)