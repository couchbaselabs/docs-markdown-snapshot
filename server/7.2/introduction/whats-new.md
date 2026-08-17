---
title: What&#8217;s New in Version 7.2
description: Couchbase is the modern database for enterprise applications.
  Couchbase Server 7.2 combines the strengths of relational databases with the
  flexibility, performance, and scale of Couchbase.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/introduction/pages/whats-new.adoc
  xref: xref:7.2@server:introduction:whats-new.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/introduction/whats-new.html)

# What&#8217;s New in Version 7.2

> Couchbase is the modern database for enterprise applications. Couchbase Server 7.2 combines the strengths of relational databases with the flexibility, performance, and scale of Couchbase. 

For information about platform support changes, deprecation notifications, notable improvements, and fixed and known issues, refer to the [Release Notes](../release-notes/relnotes.md).

## [](#new-features)New Features and Enhancements

The following new features are provided in this release.

### [](#new-features-727)What's new in 7.2.7

* The following new platforms are supported.

  * Windows Server 2025

### [](#new-features-726)What's new in 7.2.6

* The following new platforms are supported.

  * Linux Ubuntu 24.04
* _New stats and parameters added to Couchbase Server_

| cm\_failover\_total           | The number of non-graceful failover results (initiated, completed, failed, stopped).  |
| ----------------------------- | ------------------------------------------------------------------------------------- |
| cm\_graceful\_failover\_total | The number of graceful failover results (initiated, completed, failed, stopped).      |
| cm\_is\_balanced              | A Prometheus metric that shows if the cluster is balanced.                            |
| cm\_rebalance\_in\_progress   | Boolean value showing if a cluster rebalance is currently in progress.                |
| cm\_rebalance\_total          | The number of rebalance results (initiated, completed, failed, interrupted, stopped). |

### [](#new-features-720)What's new in 7.2

* The following new platforms are supported:

  * Red Hat Enterprise Linux 9
  * Oracle Linux 9
  * SUSE Enterprise Linux 12
  * SUSE Enterprise Linux 15
  * Ubuntu 20 LTS (ARM64)
  * Ubuntu 22 LTS (x86, ARM64)
  * Amazon Linux 2023 (x86, ARM64)
  * macOS 12 Apple Silicon  
See [Supported Platforms](../install/install-platforms.md) for the complete list of supported platforms, and notes on deprecated platforms.
* _New stats added:_

| cm\_auto\_failover\_count      | The number of auto-failovers that have occurred.            |
| ------------------------------ | ----------------------------------------------------------- |
| cm\_auto\_failover\_enabled    | Indicates if auto-failover is enabled (1 = true, 0 = false) |
| cm\_auto\_failover\_max\_count | The maximum number of auto-failovers before being disabled  |  
Each stat contains a label named event (`initiated`, `completed`,`failed`, and `stopped`) and the number of occurrences for the labeled event.
* _Examples added to Tools package._ The documentation references code examples built with the `cbq` command line tool. Since the examples are also used by Capella users, the `cbq` tool is now part of the tools package.
* _Cost Based Optimizer for Analytics_ (_CBO_). The cost-based optimizer for Analytics chooses the optimal plan to execute an Analytics query. The cost-based optimizer gathers and utilizes samples from Analytics collections, and then queries the samples at query planning time to estimate the cost of each operation.  
The Analytics Service introduces new syntax for managing samples, and provides parameters and hints to help specify the behavior of the cost-based optimizer. See [Cost-Based Optimizer for Analytics](../analytics/5b%5Fcbo.md).
* _Time Series Queries_. Time series data is any data which changes over time. It is usually collected frequently, in regular or irregular intervals, from a device or a process.  
The Query Service provides a standard format for time series data, which promotes compact storage and quick processing, and introduces a \_TIMESERIES function to query time series data. See [Time Series Data](../n1ql/n1ql-language-reference/time-series.md) and the [\_TIMESERIES Function](../n1ql/n1ql-language-reference/timeseries.md).
* _Change History_. A change history can be maintained for collections in a bucket. Changes to documents within the collections are included in the change history. A maximum size for the change history can be specified in bytes or seconds. See [Change History](../learn/data/change-history.md).  
For information on establishing change-history default settings, at bucket-creation time, see [Creating and Editing Buckets](../rest-api/rest-bucket-create.md). For information on switching the change history on or off for a specific collection, see [Creating and Editing a Collection](../rest-api/creating-a-collection.md). To examine the change-history status for each collection in a bucket, see the [collections](../cli/cbstats/cbstats-collections.md) option for `cbstats`. To read the change history, use the [Kafka 4.1 Connector](#4.1@kafka-connector::index.adoc).
* New alerts are provided for _change-history size threshold_ and _Index Service low residence threshold_. See [Setting Alerts](../rest-api/rest-cluster-email-notifications.md).
* You can now configure block size for _Magma_ storage when you create a bucket. See [Creating and Editing Buckets](../rest-api/rest-bucket-create.md).
* New metrics are provided for tracking XDCR _conflict resolution_ on the target cluster. See [Monitoring Conflict Resolution on the Target Cluster](../learn/clusters-and-availability/xdcr-conflict-resolution.md#monitoring-conflict-resolution).
* Couchbase Server now checks node certificates to ensure a node-name is correctly identified with a Subject Alternative Name (SAN) when certificates are uploaded and when a node is added or joins a cluster. See [Node-Certificate Validation](../learn/security/certificates.md#node-certificate-validation).
* The Analytics Service now supports external datasets on _Google Cloud Platform_ (GCP) storage. You can manage these datasets using the UI or the Analytics Links REST API. See [Managing Links](../analytics/manage-links.md) and [Analytics Links REST API](../analytics/rest-links.md).
* When connecting from an external network, you can now use the `network=external` option to specify an alternate address when using `cbbackupmgr`, `cbimport`, and `cbexport`. See **Host Formats** information in [cbbackupmgr](../backup-restore/cbbackupmgr.md), [cbimport](../tools/cbimport.md), and [cbexport](../tools/cbexport.md).
* You can now download the `cbbackupmgr`, `cbimport`, and `cbexport` tools from a tools package. This enables developers or testers to use the tools from machines on which Couchbase Server is not installed. See [Server Tools Packages](../cli/cli-intro.md#server-tools-packages).
* _Capella_ databases use Certificate Authorities (CAs), to establish secure connections: these CAs are now automatically trusted when you use Couchbase Web Console or the REST API to establish _fully secure_ XDCR connections between Capella databases and Couchbase Enterprise Server 7.2+. See [Capella Trusted CAs](../manage/manage-xdcr/secure-xdcr-replication.md#capella-trusted-cas).
* Couchbase Server has a new service discovery endpoint to help you configure the Prometheus event monitoring system. The old endpoint, named `/prometheus_sd_config.yaml` is now deprecated. The new endpoint is able to produce the same output as the old endpoint and has additional features. See [Configure Prometheus to Collect Couchbase Metrics](../manage/monitor/set-up-prometheus-for-monitoring.md).
* You can now have Couchbase Server prune rotated audit logs after a period of time. You set how long Couchbase Server should keep audit logs by using the new `pruneAge` parameter for the `/settings/audit` endpoint. The default value of 0 means that Couchbase Server does not prune audit logs. See [Configure Auditing](../rest-api/rest-auditing.md).

* Power BI Connector version 1.0 released. ([Power BI Connector documentation](../../../power-bi-connector/current/index.md))  
You can download the installation package from the following location:  

| Binaries      | [powerbi-connector-1.0.mez](https://packages.couchbase.com/releases/couchbase-powerbi-connector/1.0/couchbase-powerbi-connector-1.0.mez)               |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Binaries SHAs | [powerbi-connector-1.0.mez.sha256](https://packages.couchbase.com/releases/couchbase-powerbi-connector/1.0/couchbase-powerbi-connector-1.0.mez.sha256) |
* The new cluster-wide `enableReplicaCatchupOnRebalance` option lets you make the rebalance process track its progress when copying FTS replica index partitions the same way it tracks active partitions. See [enableReplicaCatchupOnRebalance](../fts/fts-advanced-settings-enableReplicaCatchupOnRebalance.md) for more information.
* The _Search service_ now supports IP addresses as indexable types.

## [](#developer-preview)Developer Preview

The following features are provided as part of the _Developer Preview_ for 7.2.

### [](#support-for-python-machine-learning-models-python-udfs)Support for Python Machine Learning Models (Python UDFs)

Python User-Defined Functions (UDFs) enable the evaluation of Python functions in the context of an SQL++ query. The complexity of these UDFs can range from simple Python code snippets to trained models that are based on machine-learning frameworks like scikit-learn or PyTorch.

### [](#encrypted-backups)Encrypted Backups

Encrypted backups are available with both cbbackupmgr CLI and the Backup Service. See [cbbackupmgr encryption](../backup-restore/cbbackupmgr-encryption.md).

For information on using these features, see [Developer Preview Mode and Features](../developer-preview/preview-mode.md).