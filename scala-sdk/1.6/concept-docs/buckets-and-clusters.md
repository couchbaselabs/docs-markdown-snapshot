---
title: Buckets and Clusters
description: The Couchbase Scala SDK provides an API for managing a Couchbase
  cluster programmatically.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-scala/edit/temp/1.6/modules/concept-docs/pages/buckets-and-clusters.adoc
  xref: xref:1.6@scala-sdk:concept-docs:buckets-and-clusters.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/1.6/concept-docs/buckets-and-clusters.html)

# Buckets and Clusters

> The Couchbase Scala SDK provides an API for managing a Couchbase cluster programmatically. 

The primary means for managing clusters is through the [Couchbase Web UI](#7.1@server:manage:manage-buckets/bucket-management-overview.adoc) which provides an easy to use interface for adding, removing, monitoring, and modifying buckets. In some instances you may wish to have a programmatic interface. For example, if you wish to manage a cluster from a setup script, or if you are setting up buckets in test scaffolding.

The SDK also comes with some convenience functionality for common Couchbase management requests — see the [Provisioning Cluster Resources](../howtos/provisioning-cluster-resources.md) guide.