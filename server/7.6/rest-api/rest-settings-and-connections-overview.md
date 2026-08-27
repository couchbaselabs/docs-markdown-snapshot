---
title: Settings and Connections
description: Settings and connections for the cluster can be managed by means of
  the REST API.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/rest-api/pages/rest-settings-and-connections-overview.adoc
  xref: xref:7.6@server:rest-api:rest-settings-and-connections-overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/rest-api/rest-settings-and-connections-overview.html)

# Settings and Connections

> Settings and connections for the cluster can be managed by means of the REST API. 

## [](#apis-in-this-section)APIs In this Section

Settings and connections for the cluster can be managed by means of the REST API. Each of the methods and URIs covered in this section is listed in the table provided below.

| HTTP Method | URI                                               | Documented at                                                                                                       |
| ----------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| GET         | /internalSettings                                 | [Managing Internal Settings](rest-get-internal-setting.md)                                                          |
| POST        | /internalSettings                                 | [Managing Internal Settings](rest-get-internal-setting.md)                                                          |
| GET         | /settings/maxParallelIndexers                     | [Managing Internal Settings](rest-get-internal-setting.md)                                                          |
| POST        | /settings/maxParallelIndexers                     | [Managing Internal Settings](rest-get-internal-setting.md)                                                          |
| GET         | /pools/default/settings/memcached/global          | [Managing Cluster Connections](rest-manage-cluster-connections.md)                                                  |
| POST        | /pools/default/settings/memcached/global          | [Managing Cluster Connections](rest-manage-cluster-connections.md)                                                  |
| PUT         | /node/controller/setupAlternateAddresses/external | [Managing Alternate Addresses](rest-set-up-alternate-address.md)                                                    |
| DELETE      | /node/controller/setupAlternateAddresses/external | [Managing Alternate Addresses](rest-set-up-alternate-address.md)                                                    |
| GET         | /settings/alerts                                  | [Getting Alert Settings](rest-cluster-email-notifications.md#rest-cluster-alerts-get)                               |
| POST        | /settings/alerts                                  | [Enabling and Disabling Email Notifications](rest-cluster-email-notifications.md#rest-cluster-alerts-enabledisable) |
| POST        | /settings/alerts/sendTestEmail                    | [Sending Test Emails](rest-cluster-email-notifications.md#rest-cluster-alerts-send)                                 |