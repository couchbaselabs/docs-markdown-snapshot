[View original HTML](/enterprise-analytics/current/reference/rest-settings-and-connections-overview.html)

> Settings and connections for the cluster can be managed by means of the REST API. 

## [](#apis-in-this-section)APIs In this Section

Settings and connections for the cluster can be managed by means of the REST API. Each of the methods and URIs covered in this section is listed in the table provided below.

| HTTP Method | URI                                               | Documented at                                                                                                       |
| ----------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| GET         | /internalSettings                                 | [Managing Internal Settings](#reference:rest-get-internal-setting.adoc)                                             |
| POST        | /internalSettings                                 | [Managing Internal Settings](#reference:rest-get-internal-setting.adoc)                                             |
| GET         | /settings/maxParallelIndexers                     | [Managing Internal Settings](#reference:rest-get-internal-setting.adoc)                                             |
| POST        | /settings/maxParallelIndexers                     | [Managing Internal Settings](#reference:rest-get-internal-setting.adoc)                                             |
| GET         | /pools/default/settings/memcached/global          | [Managing Cluster Connections](#reference:rest-manage-cluster-connections.adoc)                                     |
| POST        | /pools/default/settings/memcached/global          | [Managing Cluster Connections](#reference:rest-manage-cluster-connections.adoc)                                     |
| PUT         | /node/controller/setupAlternateAddresses/external | [Managing Alternate Addresses](rest-set-up-alternate-address.md)                                                    |
| DELETE      | /node/controller/setupAlternateAddresses/external | [Managing Alternate Addresses](rest-set-up-alternate-address.md)                                                    |
| GET         | /settings/alerts                                  | [Getting Alert Settings](rest-cluster-email-notifications.md#rest-cluster-alerts-get)                               |
| POST        | /settings/alerts                                  | [Enabling and Disabling Email Notifications](rest-cluster-email-notifications.md#rest-cluster-alerts-enabledisable) |
| POST        | /settings/alerts/sendTestEmail                    | [Sending Test Emails](rest-cluster-email-notifications.md#rest-cluster-alerts-send)                                 |