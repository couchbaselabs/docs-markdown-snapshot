---
title: Buckets and Clusters
description: The Couchbase PHP SDK provides an API for managing a Couchbase
  cluster programmatically.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.4/modules/concept-docs/pages/buckets-and-clusters.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/php-sdk/current/concept-docs/buckets-and-clusters.html)

# Buckets and Clusters

> The Couchbase PHP SDK provides an API for managing a Couchbase cluster programmatically. 

The primary means for managing clusters is through the [Couchbase Web UI](../../../server/current/manage/manage-buckets/bucket-management-overview.md) which provides an easy to use interface for adding, removing, monitoring, and modifying buckets. In some instances you may wish to have a programmatic interface. For example, if you wish to manage a cluster from a setup script, or if you are setting up buckets in test scaffolding.

The SDK also comes with some convenience functionality for common Couchbase management requests — see the [Provisioning Cluster Resources](../howtos/provisioning-cluster-resources.md) guide.