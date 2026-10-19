---
title: Settings and Connections
description: Settings and connections for the cluster can be managed by means of
  the REST API.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-settings-and-connections-overview.adoc
  xref: xref:enterprise-analytics:reference:rest-settings-and-connections-overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-settings-and-connections-overview.html)

# Settings and Connections

> Settings and connections for the cluster can be managed by means of the REST API. 

## [](#apis-in-this-section)APIs In this Section

Settings and connections for the cluster can be managed by means of the REST API. Each of the methods and URIs covered in this section is listed in the table provided below.

| HTTP Method | URI                                               | Documented at                                                                                 |
| ----------- | ------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| PUT         | /node/controller/setupAlternateAddresses/external | [Managing Alternate Addresses](rest-set-up-alternate-address.md)                              |
| DELETE      | /node/controller/setupAlternateAddresses/external | [Managing Alternate Addresses](rest-set-up-alternate-address.md)                              |
| GET         | /settings/alerts                                  | [Getting Alert Settings](rest-cluster-email-notifications.md#curl-syntax)                     |
| POST        | /settings/alerts                                  | [Enabling and Disabling Email Notifications](rest-cluster-email-notifications.md#curl-syntax) |
| POST        | /settings/alerts/testEmail                        | [Sending Test Emails](rest-cluster-email-notifications.md#curl-syntax)                        |
| GET         | /settings/alerts/limits                           | [Getting Alert Limits](rest-cluster-email-notifications.md#curl-syntax)                       |
| POST        | /settings/alerts/limits                           | [Setting Alert Limits](rest-cluster-email-notifications.md#curl-syntax)                       |