---
title: XDCR API
description: The XDCR REST API is used to manage Cross Datacenter Replication
  (XDCR) operations.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/rest-xdcr-intro.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/rest-api/rest-xdcr-intro.html)

# XDCR API

> The XDCR REST API is used to manage Cross Datacenter Replication (XDCR) operations. 

## [](#apis-in-this-section)APIs in this Section

Cross Datacenter Replication (XDCR) configuration replicates data between a source bucket and a target bucket. For a detailed introduction and overview, see [Cross Data Center Replication (XDCR)](../learn/clusters-and-availability/xdcr-overview.md). To learn how to secure an XDCR connection, see [Enable Fully Secure Replications](../manage/manage-xdcr/enable-full-secure-replication.md).

For a list of the methods and URIs covered by the pages in this section, see the table below.

| HTTP Method | URI                                                        | Documented at                                                   |
| ----------- | ---------------------------------------------------------- | --------------------------------------------------------------- |
| POST        | /pools/default/remoteClusters                              | [Creating and Editing References](rest-xdcr-create-ref.md)      |
| GET         | /pools/default/remoteClusters                              | [Getting a Reference](rest-xdcr-get-ref.md)                     |
| POST        | /controller/createReplication                              | [Creating a Replication](rest-xdcr-create-replication.md)       |
| POST        | /settings/replications/\[replication\_id\]                 | [Pausing and Resuming a Replication](rest-xdcr-pause-resume.md) |
| DELETE      | /controller/cancelXDCR/\[url\_encoded\_replication\_id\]   | [Deleting a Replication](rest-xdcr-delete-replication.md)       |
| DELETE      | /pools/default/remoteClusters/\[destination-cluster-name\] | [Deleting a Reference](rest-xdcr-delete-ref.md)                 |
| POST        | /settings/replications/                                    | [Managing Advanced Settings](rest-xdcr-adv-settings.md)         |
| POST        | /settings/replications/<settings\_URI>                     | [Managing Advanced Settings](rest-xdcr-adv-settings.md)         |
| GET         | /settings/replications/                                    | [Managing Advanced Settings](rest-xdcr-adv-settings.md)         |
| GET         | /settings/replications/<settings\_URI>                     | [Managing Advanced Settings](rest-xdcr-adv-settings.md)         |
| GET         | /pools/default/stats/range/\[statistics\_name\]            | [Getting a Single Statistic](rest-statistics-single.md)         |