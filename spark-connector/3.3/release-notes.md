---
title: Release Notes
editUrl: https://github.com/couchbase/docs-spark/edit/release/3.3/modules/ROOT/pages/release-notes.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.3@spark-connector::release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/spark-connector/3.3/release-notes.html)

# Release Notes

> Release notes for the Spark Connector. 

## [](#couchbase-spark-connector-3-3-5-ga-30-july-2024)Couchbase Spark Connector 3.3.5 GA (30 July 2024)

Version 3.3.5 is built and tested against Spark 3.3.4.

### [](#improvements)Improvements

* [SPARKC-194](https://issues.couchbase.com/browse/SPARKC-194): Partitioning options added for DataFrame query reads.

## [](#couchbase-spark-connector-3-3-4-ga-8-january-2024)Couchbase Spark Connector 3.3.4 GA (8 January 2024)

Version 3.3.4 is built and tested against Spark 3.3.4.

### [](#bug-fixes-and-stability)Bug fixes and stability

* [SPARKC-181](https://issues.couchbase.com/browse/SPARKC-181): When performing a DataFrame read (`spark.read().format("couchbase.query")`), rows will now be streamed and backpressured, rather than buffered in-memory.

## [](#couchbase-spark-connector-3-3-3-ga-14-november-2023)Couchbase Spark Connector 3.3.3 GA (14 November 2023)

Version 3.3.3 is built and tested against Spark 3.3.0.

### [](#bug-fixes-and-stability-2)Bug fixes and stability

* [SPARKC-181](https://issues.couchbase.com/browse/SPARKC-181): Allow structured streaming to work against clusters that do not have the KV service running on all nodes.

## [](#couchbase-spark-connector-3-3-2-ga-10-october-2023)Couchbase Spark Connector 3.3.2 GA (10 October 2023)

Version 3.3.2 is built and tested against Spark 3.3.0.

### [](#bug-fixes-and-stability-3)Bug fixes and stability

* [SPARKC-178](https://issues.couchbase.com/browse/SPARKC-178): Fix issues with `connectionIdentifier`.

## [](#couchbase-spark-connector-3-3-1-ga-22-february-2023)Couchbase Spark Connector 3.3.1 GA (22 February 2023)

Version 3.3.1 is built and tested against Spark 3.3.0.

### [](#bug-fixes-and-stability-4)Bug fixes and stability

* [SPARKC-177](https://issues.couchbase.com/browse/SPARKC-177): If alternate addresses are configured on the cluster (for instance, for Kubernetes deployments), these will now be used automatically when doing structured streaming.

## [](#couchbase-spark-connector-3-3-0-ga-january-2023)Couchbase Spark Connector 3.3.0 GA (January 2023)

Version 3.3.0 is the first version to support Spark 3.3.0.

### [](#bug-fixes-and-stability-5)Bug fixes and stability

* [SPARKC-166](https://issues.couchbase.com/browse/SPARKC-166): Improved handling of aggregate result datatypes.
* [SPARKC-176](https://issues.couchbase.com/browse/SPARKC-176): Bump DCP client version.
* [SPARKC-174](https://issues.couchbase.com/browse/SPARKC-174): Adjust default DCP bootstrap timeout to improve connection capability in high-latency environments.

### [](#features)Features

* [SPARKC-167](https://issues.couchbase.com/browse/SPARKC-167), [SPARKC-168](https://issues.couchbase.com/browse/SPARKC-168): Support connecting to multiple Clusters.
* [SPARKC-175](https://issues.couchbase.com/browse/SPARKC-175), [SPARKC-165](https://issues.couchbase.com/browse/SPARKC-165): Support Spark 3.3.0.
* [SPARKC-160](https://issues.couchbase.com/browse/SPARKC-160): Shade Reactor dependency into 'fatjar' build to better support the Databricks environment.

## [](#couchbase-spark-connector-3-2-2-ga-july-2022)Couchbase Spark Connector 3.2.2 GA (July 2022)

Version 3.2.2 is the third version to support Spark 3.2.x and is built on top of the Couchbase Scala SDK 1.3.x as well as the Java DCP Client.

### [](#features-2)Features

* [SPARKC-157](https://issues.couchbase.com/browse/SPARKC-157): Add support for "ignore" variants for KeyValue insert, replace and remove operations. This has been available in the Spark Connector 2.x series and has not been ported forward until this point.
* [SPARKC-159](https://issues.couchbase.com/browse/SPARKC-159): TLS configuration is now more flexible. TLS can be enabled trough couchbases:// in the connection string, as well as being more robust in accepting certail security config parameters.
* [SPARKC-160](https://issues.couchbase.com/browse/SPARKC-160): To avoid classpath issues in the Databricks notebook environment, the Reactor library is now shaded in the assembly jar that is available for download. The regular jar still has the unshaded version of Reactor.

### [](#bug-fixes-and-stability-6)Bug fixes and stability

* [SPARKC-158](https://issues.couchbase.com/browse/SPARKC-158): Open the implicitBucket if set for cluster-level operations. This makes sure that cluster-level operations like N1QL queries can be performed against Couchbase Server clusters pre 6.5.

## [](#couchbase-spark-connector-3-2-1-ga-may-2022)Couchbase Spark Connector 3.2.1 GA (May 2022)

Version 3.2.1 is the second version to support Spark 3.2.x and is built on top of the Couchbase Scala SDK 1.3.x as well as the Java DCP Client.

### [](#features-3)Features

* Updated the underlying SDK to 1.3.0, which (along with general enhancements and fixes) bundles the Capella certificate, so it doesn't have to be added manually.
* [SPARKC-133](https://issues.couchbase.com/browse/SPARKC-133): Added support for spark structured streaming. For more details, see the documentation section for streaming.

## [](#couchbase-spark-connector-3-2-0-ga-january-2022)Couchbase Spark Connector 3.2.0 GA (January 2022)

Version 3.1.0 is the first version to support Spark 3.2.x and is built on top of the Couchbase Scala SDK 1.2.x.

### [](#features-4)Features

* Support for Apache Spark 3.2.x
* [SPARKC-146](https://issues.couchbase.com/browse/SPARKC-146): Added support for scope-level Query and Analytics RDDs (through `Keyspace`)
* [SPARKC-148](https://issues.couchbase.com/browse/SPARKC-148): Added support for aggregate pushdown for Query DataFrames.
* [SPARKC-149](https://issues.couchbase.com/browse/SPARKC-148): Added support for aggregate pushdown for Analytics DataFrames.

### [](#bug-fixes-and-stability-7)Bug fixes and stability

* [SPARKC-143](https://issues.couchbase.com/browse/SPARKC-143): Allow passing timeouts to KV, Query and Analytics DataFrame as option.
* [SPARKC-151](https://issues.couchbase.com/browse/SPARKC-151): Fix ScanConsistency not being applied for Analytics and Query DataFrames.
* [SPARKC-144](https://issues.couchbase.com/browse/SPARKC-144), [SPARKC-145](https://issues.couchbase.com/browse/SPARKC-145): Move Jackson JSON handling into the connector. This solves issues in the databricks notebook environment.
* [SPARKC-153](https://issues.couchbase.com/browse/SPARKC-153): Properly escape fields for Analytics and Query DataFrames.

## [](#couchbase-spark-connector-3-1-0-ga-september-2021)Couchbase Spark Connector 3.1.0 GA (September 2021)

Version 3.1.0 is the first version to support Spark 3.1.x and is built on top of the Couchbase Scala SDK 1.1.x.

This release contains identical features to the Spark 3.0.0 connector, the only difference being compiled against Spark 3.1.x. Please refer to the 3.0 migration guide for changes and new features over 2.4.x.

### [](#highlights)Highlights

* Support for Apache Spark 3.1.x

## [](#couchbase-spark-connector-3-0-0-ga-september-2021)Couchbase Spark Connector 3.0.0 GA (September 2021)

Version 3.0.0 is the first version to support Spark 3.0.x and is built on top of the Couchbase Scala SDK 1.1.x.

Please note that this release does not have separate release notes, rather refer to the migration guide page for more information.

### [](#highlights-2)Highlights

* Support for Apache Spark 3.0.x
* Built on top of the new Scala SDK 1.2.x
* Support for Couchbase Server 7.0 and later

## [](#couchbase-spark-connector-2-4-1-ga-november-2020)Couchbase Spark Connector 2.4.1 GA (November 2020)

Version 2.4.1 brings support for Couchbase Cloud as well as:

### [](#features-5)Features

* [SPARKC-110](https://issues.couchbase.com/browse/SPARKC-110): Allow passthrough of timestampFormat and dateFormat for inferring schema
* Updated the Java SDK to 2.7.18
* Allows enabling DNS SRV via a configuration property

### [](#bug-fixes-and-stability-8)Bug fixes and stability

* [SPARKC-104](https://issues.couchbase.com/browse/SPARKC-104): Stopping and restarting of Spark-Couchbase-Streaming-job throws ClassCastException
* Properly propagate the expiry into the `DefaultSource`

## [](#couchbase-spark-connector-2-4-0-ga-july-2019)Couchbase Spark Connector 2.4.0 GA (July 2019)

Version 2.4.0 brings support for Spark 2.4.0, and is compiled exclusively with Scala 2.12.

## [](#couchbase-spark-connector-2-3-0-ga-may-2019)Couchbase Spark Connector 2.3.0 GA (May 2019)

Version 2.3.0 brings support for Spark 2.3.0 along with:

### [](#features-6)Features

* [SPARKC-93](https://issues.couchbase.com/browse/SPARKC-93): Support for Apache Spark 2.3.0
* [SPARKC-89](https://issues.couchbase.com/browse/SPARKC-89): Support Analytics
* [SPARKC-88](https://issues.couchbase.com/browse/SPARKC-88): Allow N1QL queries to run on Spark node(s) co-located with query service
* [SPARKC-96](https://issues.couchbase.com/browse/SPARKC-96): Provide more fault-tolerant batch mutations. `saveToCouchbase` now takes a `maxConcurrent` parameter, giving the application control over the size of batches that will be written, from each executor.

### [](#bug-fixes-and-stability-9)Bug fixes and stability

* [SPARCK-85](https://issues.couchbase.com/browse/SPARKC-85): Raise N1QL errors as exceptions rather than logging them.
* [SPARKC-82](https://issues.couchbase.com/browse/SPARKC-82): When running a N1QLQuery, if multiple buckets have been specified, then the bucket to use must now be explicitly chosen. E.g. `sc.couchbaseQuery(query, bucketName = "default")`. This is safer than choosing an arbitrary bucket.
* [SPARKC-95](https://issues.couchbase.com/browse/SPARKC-95): Fix to get streaming source working with Spark 2.3

## [](#couchbase-spark-connector-2-2-0-ga-september-2017)Couchbase Spark Connector 2.2.0 GA (September 2017)

Version 2.2.0 is the first stable release of the 2.2.x series. It brings support for Spark 2.2 and the following enhancements and bugfixes:

### [](#spark-core)Spark Core

* Support for Apache Spark 2.2.0
* [SPARKC-80](https://issues.couchbase.com/browse/SPARKC-80): Support for Couchbase Server 5.0 and Role-Based Access Control
* [SPARKC-77](https://issues.couchbase.com/browse/SPARKC-77): Global and per-operation timeout configuration is now possible
* [SPARKC-44](https://issues.couchbase.com/browse/SPARKC-44): Support for Subdocument Mutations has been added.
* [SPARKC-79](https://issues.couchbase.com/browse/SPARKC-79): Support for easier SSL/TLS configuration via spark config.

### [](#spark-sql)Spark SQL

* [SPARKC-77](https://issues.couchbase.com/browse/SPARKC-77): per-operation timeout configuration is now possible

### [](#spark-streaming)Spark Streaming

No changes for Spark Streaming have been made in this release.

## [](#older-releases)Older Releases

Although [no longer supported](https://www.couchbase.com/support-policy/enterprise-software), documentation for older releases continues to be available in our [docs archive](https://docs-archive.couchbase.com/home/index.html).