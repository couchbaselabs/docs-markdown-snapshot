---
title: Introduction
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-spark/edit/release/3.5/modules/ROOT/pages/index.adoc
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

Every version of the Couchbase Spark connector is compiled against a specific Apache Spark target.

E.g. if you are using Apache Spark 3.5.x, you should use a 3.5.x version of the Couchbase Spark Connector.

__Table 1\. Couchbase Spark Connector compatibility__
| Couchbase Spark Connector version | Apache Spark target version |
| --------------------------------- | --------------------------- |
| 3.5.x                             | 3.5.x                       |
| 3.3.x                             | 3.3.x                       |
| 3.2.x                             | 3.2.x                       |
| 3.1.x                             | 3.1.x                       |
| 3.0.x                             | 3.0.x                       |

Note that if the internal Spark APIs do not break between minor versions, it is possible to use different version combinations. The table above shows the combination Couchbase tests and supports.

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