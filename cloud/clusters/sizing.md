---
title: Sizing a Cluster
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/sizing.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:clusters:sizing.adoc[]
---

[View original HTML](/cloud/clusters/sizing.html)

# Sizing a Cluster

> Couchbase provides Capella features to help you size your cluster appropriately. 

Sizing a cluster correctly is critical to its overall stability and performance. Couchbase Capella simplifies and eliminates most of the traditional complexities of sizing a Couchbase Server deployment. This makes it much easier for you to get started with a properly sized cluster.

You can configure cluster sizing during the [cluster creation process](create-database.md) or [scale a cluster](scale-database.md) after it’s created.

> [!IMPORTANT]
> To minimize the risk and severity of cluster outages, Couchbase Capella clusters using Couchbase Server 7.6 or later have guardrails that limit some cluster operations when cluster conditions meets certian thresholds. To learn more, see [Couchbase Server Guardrails](databases.md#guardrails).

The following topics can help you understand Couchbase services and how to size them:

* [Couchbase services](../../server/current/learn/services-and-indexes/services/services.md)
* [Couchbase Server Sizing Guidelines](../../server/current/install/sizing-general.md)

For more information about how to configure a cluster in Capella, see [Configure Your Cluster](databases.md).