---
title: About Billing Alerts
description: Couchbase Capella billing alerts notify you about important
  information related to your usage and billing for operational clusters.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/billing/pages/about-billing-alerts.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:billing:about-billing-alerts.adoc[]
---

[View original HTML](/cloud/billing/about-billing-alerts.html)

# About Billing Alerts

> Couchbase Capella billing alerts notify you about important information related to your usage and billing for operational clusters. 

You can [create and manage your own custom alerts](manage-billing-alerts.md).

## [](#alert-conditions)Alert Conditions

> [!NOTE]
> Alert timing
> 
> Alerts can be delayed by up to a day after usage meets alerting conditions.

The following conditions are available for billing alerts:

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

| Recipient                    | Description                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Organization Role            | Sends an alert to all users with the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner), [Project Creator](../organizations/organization-user-roles.md#organization-role-project-creator), or [Organization Member](#organization-user-roles.adoc#organization-role-member) role in your organization. You can choose multiple roles to receive the alert. |
| User                         | Sends an alert to specific Capella users by email address.                                                                                                                                                                                                                                                                                                                                                     |
| All Users in My Organization | Sends an alert to all current users in your organization.                                                                                                                                                                                                                                                                                                                                                      |

## [](#see-also)See Also

* [Manage Billing Alerts](manage-billing-alerts.md)
* [Manage Your Billing](billing.md)
* [Manage Billing Information](manage-billing.md)
* [View Capella Usage and Invoices](usage-invoices.md)