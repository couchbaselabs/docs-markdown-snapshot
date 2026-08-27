---
title: Introduction
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbase/docs-spark/edit/release/4.0/modules/ROOT/pages/index.adoc
  xref: xref:spark-connector::index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/spark-connector/current/index.html)

# Introduction

> The Couchbase Spark Connector provides first-class integration between your high performance Couchbase cluster and the Apache Spark data processing platform, and can be used from both Scala and PySpark. 

Please see one of the following getting started guide:

* [Scala getting started](getting-started.md).
* [PySpark getting started](pyspark.md).
* [Java getting started](java-api.md).

The Couchbase Spark Connector supports any type of Couchbase cluster. Users of Capella Columnar should see the [Columnar Support](columnar.md) page.

## [](#compatibility)Compatibility

### [](#apache-spark-4-x-users)Apache Spark 4.x users

From the 4.0.0 release, the Couchbase Spark Connector is changing release models to better accommodate the [upcoming changes to the Apache Spark release model](https://spark.apache.org/versioning-policy.html).

Apache Spark now aim to release one major each year (N.0.0), followed by two feature minor releases (N.1.0 and N.2.0), then one long-term support (LTS) release N.3.0\. This will be adopted fully from 5.0.0, and is being transitioned to mid-major with the upcoming Apache Spark 4.3.0 release.

The connector will now also have one major each year, with connector 4.X releases (2026/27) corresponding to the Apache Spark 4.X major, and connector 5.x releases (expected 2027/28) for Apache Spark 5.x, etc.

Each 4.x connector release will aim where possible to be compatible with a useful subset of Apache Spark 4.x releases, particularly the latest patch of each minor that is currently supported by Apache. Apache plan to support N.0.0, N.1.0 and N.2.0 for 6 months apiece, and the LTS N.3.0 for 18 months. The connector will aim to follow the same support model.

See the [release notes](release-notes.md) for details of which Apache Spark versions are tested and fully supported for each connector release. Users may try Apache Spark 4.x releases that are not listed there, though untested combinations will not be officially supported.

### [](#apache-spark-3-5-users)Apache Spark 3.5 users

Apache Spark 3.5.x users should use the latest 3.5.x of the Couchbase Spark Connector.

### [](#interface-stability)Interface Stability

Couchbase SDKs indicate the stability of an API through documentation. Since there are different meanings when developers mention stability, we mean **interface stability**: how likely the interface is to change or be removed entirely. A stable interface is one that is guaranteed not to change between versions, meaning that you may use an API of a given SDK version and be assured that the given API will retain the same parameters and behavior in subsequent versions. An unstable interface is one which may appear to work or behave in a specific way within a given SDK version, but may change in its behavior or arguments in future SDK versions, causing odd application behavior or compiler/API usage errors. **Implementation stability** is implied to be more reliable at higher levels, but all are tested to the level that is appropriate for their stability.

Couchbase uses three interface stability classifiers. You may find these classifiers appended as annotations or comments within documentation for each API:

* **Committed**: This stability level is used to indicate the most stable interfaces that are guaranteed to be supported and remain stable between SDK versions. This is the default — unless otherwise stated in the documentation, each API has **Committed** status.
* **Uncommitted**: This level is used to indicate APIs that are _unlikely_ to change, but _may_ still change as final consensus on their behavior has not yet been reached. _Uncommitted_ APIs usually end up becoming stable APIs.
* **Volatile**: This level is used to indicate experimental APIs that are still in flux and may likely be changed. It may also be used to indicate inherently private APIs that may be exposed, but "YMMV" (your mileage may vary) principles apply. _Volatile_ APIs typically end up being promoted to _Uncommitted_ after undergoing some modifications.

APIs that are marked as _Committed_ have a stable implementation. _Uncommitted_ and _Volatile_ APIs should be stable within the bounds of any known and often documented issues, but Couchbase has not made a commitment to these APIs and may not respond to reported defects with the same priority.

Additionally, take note of the following interface labels:

* **Deprecated**: Any API marked deprecated may be removed in the next major version released. Couchbase recommends migrating from the deprecated API to the replacement as soon as possible. In rare instances, deprecated API may be rendered non-functional in a dot-minor release when the API cannot continue to be supported.
* **Internal**: This level is used to indicate you should not rely on this API as it is not intended for use outside the module, even to other Couchbase components.

## [](#contributing)Contributing

Couchbase welcomes community contributions to the Spark connector. The [Spark connector source code](https://github.com/couchbase/couchbase-spark-connector) is available on GitHub and contains instructions to contribute.