[View original HTML](/python-columnar-sdk/current/project-docs/compatibility.html)

> Platform compatibility, and features available in different SDK versions, and compatibility between Server and SDK. 

|  | Don’t Mix Columnar & Operational SDKs. Do not combine the Python Columnar SDK with the Python Operational SDK on the same app server (or development machine). This combination is not tested and not supported. There may be problems with different versions of shared dependencies if you try this. This only applies to the Node.js and Python Columnar SDKs. Note, this does not apply to combining our Enterprise Analytics SDKs with our Operational SDKs. See the [Analytics SDK page](#home::analytics-sdk.adoc) for a reminder of which Analytics SDK to use with which Analytics service. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#platform-compatibility)Platform Compatibility

### [](#python-version-compatibility)Python Version Compatibility

Currently Python 3.9 - Python 3.13 is supported.

### [](#os-compatibility)OS Compatibility

Columnar SDKs can be expected to run on all of the Operating Systems supported by [Couchbase Server](../../../server/7.6/install/install-platforms.md).

The Python Columnar SDK is tested and supported on the following OSs and platforms:

### GNU/Linux

* Amazon Linux 2 & AL2023.
* Red Hat Enterprise Linux 8 & 9;
* Oracle Linux 8 & 9.
* Ubuntu (LTS) 20.04 (_Focal_) & 22.04 (_Jammy_).
* Debian 11 (_Bullseye_) & Debian 12 (_Bookworm_).
* SUSE Enterprise Linux 12 & 15.

### Microsoft Windows

* Microsoft Windows 10 & 11;
* Windows Server 2019 & 2022.

### Mac OS X

The current and previous two releases of OS X. At time of writing (October 2024): 15 (Sequoia), 14 (Sonoma), and 13 (Ventura). M1 ARM architecture is fully supported in the Python Columnar SDK.

### ARM Processor Support

AWS Amazon Graviton, Apple M1 ARM processors, and ARMv8 on Ubuntu 20.04+.

### [](#network-requirements)Network Requirements

Couchbase SDKs are developed to be run in an environment with local area network (LAN) like throughput and latencies. While there is no technical issue that prevents the use across a wide area network (WAN), SDKs have certain thresholds around timeouts and behaviors to recover that will not be the same once the higher latency and possible bandwidth constraints and congestion of a WAN is introduced. Couchbase tests for correctness under LAN like conditions. For this reason, only LAN-like network environments are officially supported.

Couchbase does document, for purposes of convenience when developing and performing basic operational work, what may need to be tuned when network throughputs and latencies are higher. If you encounter issues, even with these tunables, you should attempt the same workload from a supported, LAN-like environment.

## [](#capella-columnar-compatibility)Capella Columnar Compatibility

Capella Columnar is a fully hosted service, continually updated, and offering the latest version — with users having a few weeks to upgrade from the previous version. As such, the latest Couchbase Columnar SDKs are tested against the latest versions. Where older versions of the Python Columnar SDK pre-date significant new features in Columnar, those differences will be noted in this section.

## [](#sdk-api-stability)SDK API Stability

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